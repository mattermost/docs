# Calls Offloader Setup and Configuration

```{include} ../_static/badges/ent-only.md
```


This guide provides detailed instructions for setting up, configuring, and validating the Mattermost calls-offloader service used for call recording and transcription features.

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation and deployment](#installation-and-deployment)
- [Configuration](#configuration)
- [Validation and testing](#validation-and-testing)
- [Integration with Mattermost](#integration-with-mattermost)
- [Troubleshooting](#troubleshooting)

## Overview

The calls-offloader service is a dedicated microservice that handles resource-intensive tasks for Mattermost Calls, including:

- **Call recording**: Captures audio and screen sharing content from calls
- **Call transcription**: Provides automated transcription of recorded calls
- **Live captions** (Experimental): Real-time transcription during active calls

By offloading these tasks to a dedicated service, the main Mattermost server and RTCD service can focus on core functionality while maintaining optimal performance.

## Prerequisites

Before deploying calls-offloader, ensure you have:

- A Mattermost Enterprise license
- A properly configured Mattermost Calls deployment (either integrated or with RTCD)
- Docker installed and running (for Docker-based job execution)
- Sufficient storage space for recordings (see [Storage Requirements](#storage-requirements))
- A server or container environment with adequate resources

### System Requirements

For detailed system requirements and performance recommendations, refer to the [calls-offloader performance documentation](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md).

### Storage Requirements

Call recordings can consume significant storage space:

- Audio-only recordings: ~1MB per minute per participant
- Screen sharing recordings: ~10-50MB per minute depending on content

## Installation and Deployment

### Bare Metal or VM Deployment

1. Download the latest release from the [calls-offloader GitHub repository](https://github.com/mattermost/calls-offloader/releases)

2. Create the necessary directories:

   ```bash
   sudo mkdir -p /opt/calls-offloader/data/db
   sudo useradd --system --home /opt/calls-offloader calls-offloader
   sudo chown -R calls-offloader:calls-offloader /opt/calls-offloader
   ```

3. Create a configuration file (`/opt/calls-offloader/config.toml`):

   ```toml
   [api]
   http.listen_address = ":4545"
   http.tls.enable = false
   http.tls.cert_file = ""
   http.tls.cert_key = ""
   security.allow_self_registration = true
   security.enable_admin = true
   security.admin_secret_key = "changeme"
   security.session_cache.expiration_minutes = 1440

   [store]
   data_source = "/opt/calls-offloader/data/db"

   [jobs]
   api_type = "docker"
   max_concurrent_jobs = 2
   failed_jobs_retention_time = "7d"
   image_registry = "mattermost"

   [logger]
   enable_console = true
   console_json = false
   console_level = "INFO"
   enable_file = true
   file_json = true
   file_level = "INFO"
   file_location = "/opt/calls-offloader/calls-offloader.log"
   enable_color = true
   ```

4. Create a systemd service file (`/etc/systemd/system/calls-offloader.service`):

   ```ini
   [Unit]
   Description=Mattermost Calls Offloader Service
   After=network.target docker.service
   Requires=docker.service

   [Service]
   Type=simple
   User=calls-offloader
   WorkingDirectory=/opt/calls-offloader
   ExecStart=/opt/calls-offloader/calls-offloader --config /opt/calls-offloader/config.toml
   Restart=always
   RestartSec=10
   LimitNOFILE=65536

   [Install]
   WantedBy=multi-user.target
   ```

5. Enable and start the service:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable calls-offloader
   sudo systemctl start calls-offloader
   ```

6. Check the service status:

   ```bash
   sudo systemctl status calls-offloader
   ```

7. Verify the service is responding:

   ```bash
   curl http://localhost:4545/version
   # Example output:
   # {"buildDate":"2025-03-10 19:13","buildVersion":"v0.9.2","buildHash":"a4bd418","goVersion":"go1.23.6"}
   ```

## Configuration

### API Configuration

The API section controls how the service accepts requests:

- **http.listen_address**: The address and port where the service listens (default: `:4545`)
- **http.tls.enable**: Whether to use TLS encryption for the API
- **security.allow_self_registration**: Allow clients to self-register for job management
- **security.enable_admin**: Enable admin functionality
- **security.admin_secret_key**: Secret key for admin authentication (change from default!)

### Store Configuration

Controls persistent data storage:

- **data_source**: Path to directory for storing job metadata and state

### Jobs Configuration

Controls job processing behavior:

- **api_type**: Job execution backend (`docker` or `kubernetes`)
- **max_concurrent_jobs**: Maximum number of simultaneous recording/transcription jobs
- **failed_jobs_retention_time**: How long to keep failed job data before cleanup
- **image_registry**: Docker registry for job runner images (typically `mattermost`)

### Logger Configuration

Controls logging output:

- **enable_console**: Log to console output
- **console_json**: Use JSON format for console logs
- **console_level**: Log level for console (DEBUG, INFO, WARN, ERROR)
- **enable_file**: Log to file
- **file_location**: Path to log file
- **enable_color**: Use colored output for console logs

### Private Network Configuration

When the Mattermost deployment is running in a private network, additional configuration may be necessary for the jobs spawned by the calls-offloader service to reach the Mattermost server.

In such cases, you can override the site URL used by recorder jobs or transcriber jobs to connect to Mattermost by setting the following environment variables on the Mattermost server:

- **MM_CALLS_RECORDER_SITE_URL**: Override the site URL used by recording jobs
- **MM_CALLS_TRANSCRIBER_SITE_URL**: Override the site URL used by transcription jobs

Example configuration:

Create or edit the Mattermost environment file (`/opt/mattermost/config/mattermost.environment`):

```bash
MM_CALLS_RECORDER_SITE_URL="http://internal-mattermost-server:8065"
MM_CALLS_TRANSCRIBER_SITE_URL="http://internal-mattermost-server:8065"
```

Then ensure your Mattermost systemd service references this environment file:

```ini
[Unit]
Description=Mattermost
After=network.target

[Service]
Type=notify
EnvironmentFile=/opt/mattermost/config/mattermost.environment
ExecStart=/opt/mattermost/bin/mattermost
TimeoutStartSec=3600
KillMode=mixed
Restart=always
RestartSec=10
WorkingDirectory=/opt/mattermost
User=mattermost
Group=mattermost

[Install]
WantedBy=multi-user.target
```

This is particularly useful when:

- The calls-offloader service runs in a different network segment than clients
- Internal DNS resolution differs from external URLs
- You need to use internal load balancer endpoints for job communication

## Validation and Testing

After deploying calls-offloader, validate the installation:

1. **Check service status**:

   ```bash
   # For systemd
   sudo systemctl status calls-offloader
   ```

2. **Test API connectivity**:

   **From the calls-offloader server (localhost test)**:

   ```bash
   curl http://localhost:4545/version
   # Should return version information
   # Example: {"buildDate":"2025-03-10 19:13","buildVersion":"v0.9.2","buildHash":"a4bd418","goVersion":"go1.23.6"}
   ```

   **From the Mattermost server**:

   ```bash
   curl http://YOUR_CALLS_OFFLOADER_SERVER:4545/version
   # Should return the same version information
   # This confirms network connectivity from Mattermost to calls-offloader
   ```

   If the localhost test works but the Mattermost server test fails, check:
   
   - Firewall rules or SELinux policies on the calls-offloader server (port 4545 must be accessible)
   - Network connectivity between Mattermost and calls-offloader servers
   - calls-offloader service binding configuration (ensure it's not bound to localhost only)

3. **Verify Docker integration** (if using docker api_type):

   ```bash
   # Check that system user running calls-offloader can access Docker
   sudo -u calls-offloader docker ps
   ```

## Integration with Mattermost

Once calls-offloader is properly set up and validated, configure Mattermost to use it:

1. Go to **System Console > Plugins > Calls**

2. In the **Job Service** section:

   - Set **Job Service URL** to your calls-offloader service (e.g., `http://calls-offloader-server:4545`)

3. Enable recording and transcription features as needed:

   - **Enable Call Recordings**: Toggle to allow call recordings
   - **Enable Call Transcriptions**: Toggle to allow call transcriptions  
   - **Enable Live Captions** (Experimental): Toggle to allow real-time transcription

4. Save the configuration

5. Restart the Calls plugin to re-establish state:

   - Go to **System Console > Plugins > Plugin Management**
   - Find the **Calls** plugin and click **Disable**
   - Wait a few seconds, then click **Enable**

6. Test by starting a call and enabling recording or live captions

## Troubleshooting

### Common Issues

**"failed to create recording job: max concurrent jobs reached"**

This error occurs when the calls-offloader service has reached its configured job limit.

Solutions:

- Increase `max_concurrent_jobs` in the configuration
- Check if jobs are hanging and restart the service
- Monitor system resources and scale up if needed

**Jobs not processing**

Check the following:

- Verify the calls-offloader service is running: `sudo systemctl status calls-offloader`
- Ensure network connectivity between Mattermost and calls-offloader
- Check Docker daemon is running and accessible by the user running `calls-offloader`: `docker ps`
- Verify authentication configuration matches between services
- Review service logs for specific error messages

**Docker permission issues**

If using Docker API and seeing permission errors:

```bash
# Add calls-offloader user to docker group
sudo usermod -a -G docker calls-offloader
sudo systemctl restart calls-offloader
```

### Debugging Commands

Monitor calls-offloader job containers:

```bash
# View running job containers
docker ps --format "{{.ID}} {{.Image}}" | grep "calls"

# Follow logs for debugging
docker ps --format "{{.ID}} {{.Image}}" | grep "calls" | awk '{print $1}' | xargs -I {} docker logs -f {}

# View completed job containers
docker ps -a --filter "status=exited"
```

Monitor service health:

```bash
# Check service version and health
curl http://localhost:4545/version
```

Check service logs:

```bash
# View recent logs
sudo journalctl -u calls-offloader -f

# View log file (if file logging enabled)
tail -f /opt/calls-offloader/calls-offloader.log
```

### Performance Monitoring

Monitor calls-offloader performance and resource usage to ensure optimal operation. See [Calls Metrics and Monitoring](calls-metrics-monitoring.md) for details on setting up metrics and observability.

## Air-Gapped Deployments

When deploying calls-offloader in air-gapped environments, you need to set up a local Docker registry since the service creates Docker containers that normally pull images from Docker Hub.

### Overview

The calls-offloader service creates Docker containers to handle:
- **Call Recording**: Creates containers to record audio/video from calls
- **Call Transcription**: Creates containers to transcribe recorded calls using speech-to-text

These containers are typically pulled from the `mattermost` registry on Docker Hub, but in air-gapped networks, you need to:
1. Set up a local Docker registry
2. Pre-load the required Docker images
3. Configure the calls-offloader to use the local registry

### Required Docker Images

The following Docker images are needed for full calls functionality:

- `mattermost/calls-offloader:v0.9.3` (or latest version)
- `mattermost/calls-transcriber:latest`
- `registry:2` (for the local Docker registry)

### Setup Process

#### Phase 1: Preparation (Internet-Connected Environment)

Run this phase on a machine with internet access to download and prepare the Docker images.

1. **Run the setup script**:
   ```bash
   chmod +x air-gap-docker-registry-setup.sh
   sudo ./air-gap-docker-registry-setup.sh
   ```

2. **What the script does**:
   - Sets up a local Docker registry on port 5000
   - Downloads required Mattermost Docker images
   - Pushes images to the local registry
   - Configures Docker daemon for insecure registry access
   - Creates deployment scripts for the air-gapped environment

3. **Export the registry data**:
   ```bash
   # Create an archive of the registry data
   sudo tar -czf docker-registry-data.tar.gz -C /opt/docker-registry/data .
   
   # Also backup the registry container image
   docker save registry:2 | gzip > registry-image.tar.gz
   ```

#### Phase 2: Air-Gap Deployment

Transfer the following files to your air-gapped network:
- `docker-registry-data.tar.gz`
- `registry-image.tar.gz` 
- `deploy-airgap-calls.sh` (created by setup script)

1. **Load the registry container**:
   ```bash
   gunzip -c registry-image.tar.gz | docker load
   ```

2. **Set up the registry data**:
   ```bash
   sudo mkdir -p /opt/docker-registry/data
   sudo tar -xzf docker-registry-data.tar.gz -C /opt/docker-registry/data
   ```

3. **Start the local registry**:
   ```bash
   docker run -d \
     --name local-registry \
     --restart=always \
     -p 5000:5000 \
     -v /opt/docker-registry/data:/var/lib/registry \
     registry:2
   ```

4. **Configure Docker and calls-offloader**:
   ```bash
   sudo /opt/deploy-airgap-calls.sh
   ```

### Manual Configuration

If you prefer to configure manually instead of using the scripts:

#### 1. Docker Daemon Configuration

Create or update `/etc/docker/daemon.json`:
```json
{
    "insecure-registries": ["localhost:5000"]
}
```

Restart Docker:
```bash
sudo systemctl restart docker
```

#### 2. Calls-Offloader Configuration

Update `/opt/calls-offloader/calls-offloader.toml`:

```toml
[jobs]
# Change this line:
image_registry = "mattermost"

# To this:
image_registry = "localhost:5000/mattermost"
```

Restart the calls-offloader service:
```bash
sudo systemctl restart calls-offloader
```

### Verification

#### Test Registry Access
```bash
# List available repositories
curl http://localhost:5000/v2/_catalog

# Test pulling an image
docker pull localhost:5000/mattermost/calls-offloader:latest
```

#### Test Calls Functionality

1. **Check calls-offloader logs**:
   ```bash
   sudo journalctl -u calls-offloader -f
   ```

2. **Verify calls-offloader API**:
   ```bash
   curl http://localhost:4545/version
   ```

3. **Test recording job creation** (requires proper Mattermost integration):
   - Start a call in Mattermost
   - Enable recording
   - Check that Docker containers are created for recording jobs

### Troubleshooting Air-Gap Deployments

#### Common Issues

1. **Registry not accessible**:
   - Check that the registry container is running: `docker ps | grep registry`
   - Verify Docker daemon configuration includes insecure registry
   - Check firewall settings on port 5000

2. **Image pull failures**:
   - Verify images are in the registry: `curl http://localhost:5000/v2/_catalog`
   - Check Docker daemon logs: `sudo journalctl -u docker`

3. **calls-offloader fails to create jobs**:
   - Check calls-offloader logs: `sudo journalctl -u calls-offloader`
   - Verify the `image_registry` configuration in calls-offloader.toml
   - Ensure the calls-offloader service can reach the registry

#### Log Locations

- Setup script logs: `/tmp/air-gap-registry-setup.log`
- calls-offloader logs: `/opt/calls-offloader/calls-offloader.log`
- Docker daemon logs: `sudo journalctl -u docker`
- Registry container logs: `docker logs local-registry`

#### Security Considerations

1. **Insecure Registry**: The setup uses an insecure HTTP registry for simplicity. For production, consider:
   - Setting up TLS certificates for the registry
   - Implementing authentication
   - Using proper firewall rules

2. **Network Access**: Ensure the registry is only accessible within your private network

3. **Image Verification**: Consider implementing image signing and verification processes

#### Advanced Configuration

**Using a Different Registry Host**

If you want to run the registry on a different host:

```bash
export REGISTRY_HOST="registry.internal.domain"
export REGISTRY_PORT="5000"
./air-gap-docker-registry-setup.sh
```

**Custom Image Versions**

To use specific versions of the calls images:

```bash
export CALLS_OFFLOADER_VERSION="v0.8.0"
export CALLS_TRANSCRIBER_VERSION="v1.2.0"
./air-gap-docker-registry-setup.sh
```

## Other Calls Documentation

- [Calls Overview](calls-deployment.md): Overview of deployment options and architecture
- [RTCD Setup and Configuration](calls-rtcd-setup.md): Comprehensive guide for setting up the dedicated RTCD service
- [Calls Metrics and Monitoring](calls-metrics-monitoring.md): Guide to monitoring Calls performance using metrics and observability
- [Calls Deployment on Kubernetes](calls-kubernetes.md): Detailed guide for deploying Calls in Kubernetes environments
- [Calls Troubleshooting](calls-troubleshooting.md): Detailed troubleshooting steps and debugging techniques
- [calls-offloader performance documentation](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md): Detailed performance tuning and monitoring recommendations