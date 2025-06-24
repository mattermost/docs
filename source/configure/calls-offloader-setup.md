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
- [Air-Gapped Deployments](#air-gapped-deployments)

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
- Check Docker daemon is running and accessible by the user running the Calls Offloader service (E.g., user: ``calls-offloader``)
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

- `mattermost/calls-recorder:v0.8.5` (or version matching your plugin)
- `mattermost/calls-transcriber:v0.6.3` (or version matching your plugin)
- `registry:2` (for the local Docker registry)

```{warning}
**Disk Space Requirements**: Ensure you have sufficient disk space before starting the setup process. The Docker images can be quite large:
- **calls-recorder image**: ~1.5-2GB
- **calls-transcriber image**: ~1.5-2GB  
- **Registry container + data**: ~500MB

**Total recommended free space**: At least 5GB to accommodate image downloads, local registry data, and archive creation.
```

#### Determining the Correct Image Versions

**Important**: The exact versions of `calls-offloader` and `calls-transcriber` images must match what your installed Calls plugin expects. These versions are defined in the Calls plugin source code.

To find the correct versions for your Calls plugin:

1. **Determine your Calls plugin version**:
   - In Mattermost, go to **System Console > Plugins > Plugin Management**
   - Find the **Calls** plugin and note the version number (e.g., `v1.9.0`)

2. **Look up the required image versions**:
   - Visit the Calls plugin repository: https://github.com/mattermost/mattermost-plugin-calls
   - Navigate to the tag or branch corresponding to your plugin version
   - Open the `plugin.json` file 
   - Find the `RecorderImage` and `TranscriberImage` entries (around line 719-720)

   Example from plugin.json:
   ```json
   "RecorderImage": "mattermost/calls-recorder:v0.8.5",
   "TranscriberImage": "mattermost/calls-transcriber:v0.6.3"
   ```

3. **Use these exact versions** in your air-gap setup instead of `latest` tags

**Direct link format**: For plugin version `v1.9.0`, the plugin.json would be at:
`https://github.com/mattermost/mattermost-plugin-calls/blob/v1.9.0/plugin.json`

### Setup Process

#### Phase 1: Preparation (Internet-Connected Environment)

Run this phase on a machine with internet access to download and prepare the Docker images.

**Automated Setup Script**

For convenience, you can use the automated setup script:

```bash
# Download the setup script
curl -O https://docs.mattermost.com/scripts/air-gap-docker-registry-setup.sh
chmod +x air-gap-docker-registry-setup.sh

# Run the setup script with the required image versions
sudo ./air-gap-docker-registry-setup.sh <RECORDER_VERSION> <TRANSCRIBER_VERSION>
```

The script will automatically create the required archive files (`docker-registry-data.tar.gz` and `registry-image.tar.gz`) for transfer to your air-gapped environment.

**Manual Setup Steps**

If you prefer to set up manually or need to customize the process:

1. **Set up a local Docker registry**:
   ```bash
   # Create registry data directory
   sudo mkdir -p /opt/docker-registry/data
   
   # Start a local Docker registry
   docker run -d \
     --name local-registry \
     --restart=always \
     -p 5000:5000 \
     -v /opt/docker-registry/data:/var/lib/registry \
     registry:2
   ```

2. **Download and push required images**:
   ```bash
   # Pull required images from Docker Hub
   docker pull mattermost/calls-recorder:v0.8.5
   docker pull mattermost/calls-transcriber:v0.6.3
   
   # Tag images for local registry
   docker tag mattermost/calls-recorder:v0.8.5 localhost:5000/mattermost/calls-recorder:v0.8.5
   docker tag mattermost/calls-transcriber:v0.6.3 localhost:5000/mattermost/calls-transcriber:v0.6.3
   
   # Push images to local registry
   docker push localhost:5000/mattermost/calls-recorder:v0.8.5
   docker push localhost:5000/mattermost/calls-transcriber:v0.6.3
   ```

3. **Export the registry data**:
   ```bash
   # Create an archive of the registry data
   sudo tar -czf docker-registry-data.tar.gz -C /opt/docker-registry/data .
   
   # Also backup the registry container image
   docker save registry:2 | gzip > registry-image.tar.gz
   ```

#### Phase 2: Air-Gap Deployment

Transfer the following files to your air-gapped network:
- `docker-registry-data.tar.gz` (contains the registry data with pre-loaded images)
- `registry-image.tar.gz` (contains the Docker registry container image)
- `deploy-airgap-calls.sh` (deployment script created by the setup script)

**Complete Air-Gap Deployment Steps:**

1. **Load the registry container image**:
   ```bash
   # Extract and load the registry container from the gzipped archive
   gunzip registry-image.tar.gz
   docker load -i registry-image.tar
   ```

2. **Set up the registry data directory**:
   ```bash
   # Create the registry data directory
   sudo mkdir -p /opt/docker-registry/data
   
   # Extract the pre-loaded registry data
   sudo tar -xzf docker-registry-data.tar.gz -C /opt/docker-registry/data
   ```

3. **Start the local registry with pre-loaded data**:
   ```bash
   # Start the registry container with the extracted data
   docker run -d \
     --name local-registry \
     --restart=always \
     -p 5000:5000 \
     -v /opt/docker-registry/data:/var/lib/registry \
     registry:2
   ```

4. **Configure Docker daemon for insecure registry access**:
   ```bash
   # Create or update Docker daemon configuration
   sudo mkdir -p /etc/docker
   echo '{"insecure-registries": ["localhost:5000"]}' | sudo tee /etc/docker/daemon.json
   sudo systemctl restart docker
   ```

5. **Configure Mattermost server environment variable**:
   ```bash
   # Add the registry configuration to Mattermost environment
   echo 'MM_CALLS_JOB_SERVICE_IMAGE_REGISTRY="localhost:5000/mattermost"' | sudo tee -a /opt/mattermost/config/mattermost.environment
   
   # Restart Mattermost to apply the environment variable
   sudo systemctl restart mattermost
   ```

6. **Run the air-gap deployment script** (if using the automated setup):
   ```bash
   # Make the deployment script executable and run it
   chmod +x deploy-airgap-calls.sh
   sudo ./deploy-airgap-calls.sh
   ```

   Or configure calls-offloader manually (see Manual Configuration section below).

### Manual Configuration

For reference, here are the individual configuration steps:

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
docker pull localhost:5000/mattermost/calls-recorder:latest
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

4. **"invalid Runner value: failed to validate runner" error**:
   This error occurs when calls-offloader cannot validate Docker images from the local registry.
   
   **Common causes and solutions:**
   - **Image not found**: Verify the exact image names and tags in your local registry:
     ```bash
     curl http://localhost:5000/v2/_catalog
     curl http://localhost:5000/v2/mattermost/calls-recorder/tags/list
     curl http://localhost:5000/v2/mattermost/calls-transcriber/tags/list
     ```
   
   - **Registry configuration mismatch**: Ensure the `image_registry` setting in calls-offloader.toml matches your registry:
     ```bash
     grep image_registry /opt/calls-offloader/calls-offloader.toml
     # Should show: image_registry = "localhost:5000/mattermost"
     ```
   
   - **Docker daemon can't reach registry**: Test that Docker can pull from the local registry:
     ```bash
     docker pull localhost:5000/mattermost/calls-recorder:latest
     docker pull localhost:5000/mattermost/calls-transcriber:latest
     ```
   
   - **Image tag mismatch**: The calls-offloader will be looking for specific image tags. Check what the plugin expects vs what's in your registry:
     ```bash
     # Check what tags are available
     curl http://localhost:5000/v2/mattermost/calls-recorder/tags/list
     # Compare with what your plugin.json specifies
     ```
   
   **Solution steps:**
   1. Restart calls-offloader after confirming registry configuration: `sudo systemctl restart calls-offloader`
   2. If the issue persists, check the exact image names and versions expected by your Calls plugin version
   3. Ensure both versioned tags (e.g., `v0.8.5`) and `latest` tags are present in your local registry

#### Log Locations

- Setup script logs: `/tmp/air-gap-registry-setup.log`
- calls-offloader logs: `/opt/calls-offloader/calls-offloader.log`
- Docker daemon logs: `sudo journalctl -u docker`
- Registry container logs: `docker logs local-registry`

#### Advanced Configuration

**Using a Different Registry Host**

If you want to run the registry on a different host, replace `localhost:5000` with your registry host in all commands:

```bash
# Example: using a dedicated registry server
REGISTRY_HOST="registry.internal.domain:5000"

# Update Docker daemon configuration
echo "{\"insecure-registries\": [\"$REGISTRY_HOST\"]}" | sudo tee /etc/docker/daemon.json

# Update calls-offloader configuration
sed -i "s|localhost:5000|$REGISTRY_HOST|g" /opt/calls-offloader/calls-offloader.toml
```

**Custom Image Versions**

To use specific versions of the calls images, update the version tags in the docker commands:

```bash
# Example: using specific versions
RECORDER_VERSION="v0.8.5"
TRANSCRIBER_VERSION="v0.6.3"

docker pull mattermost/calls-recorder:$RECORDER_VERSION
docker pull mattermost/calls-transcriber:$TRANSCRIBER_VERSION
```

### Day 2 Operations: Upgrading Images in Air-Gap Environments

When you upgrade your Mattermost Calls plugin to a newer version, you'll need to update the Docker images in your air-gapped registry to match the new plugin requirements.

#### Upgrade Process Overview

**When to upgrade**: After upgrading the Calls plugin in Mattermost, you must update the Docker images to match the versions expected by the new plugin version.

**Two approaches available**:

1. **Complete Rebuild Method**: Re-run the entire air-gap setup process with new image versions
2. **Incremental Update Method**: Transfer only the new images to minimize data transfer

#### Method 1: Complete Rebuild (Recommended for Major Updates)

This approach rebuilds the entire registry dataset with new image versions:

1. **On internet-connected machine**, run the air-gap setup script with new versions:
   ```bash
   # Find new versions from your updated plugin.json
   ./air-gap-docker-registry-setup.sh v0.8.5 v0.6.3
   ```

2. **Transfer new archives** to air-gapped environment:
   - `docker-registry-data.tar.gz` (contains all images including new versions)
   - `deploy-airgap-calls.sh` (updated deployment script)

3. **In air-gapped environment**, replace the registry data:
   ```bash
   # Stop the existing registry
   docker stop local-registry
   docker rm local-registry
   
   # Backup existing data (optional)
   sudo mv /opt/docker-registry/data /opt/docker-registry/data.backup
   
   # Extract new registry data
   sudo mkdir -p /opt/docker-registry/data
   sudo tar -xzf docker-registry-data.tar.gz -C /opt/docker-registry/data
   
   # Restart registry with new data
   docker run -d \
     --name local-registry \
     --restart=always \
     -p 5000:5000 \
     -v /opt/docker-registry/data:/var/lib/registry \
     registry:2
   ```

#### Method 2: Incremental Update (Efficient for Minor Updates)

This approach transfers only the new image versions without rebuilding the entire registry:

**Phase 1: Preparation (Internet-Connected Environment)**

1. **Download new images**:
   ```bash
   # Determine new versions from updated plugin.json
   NEW_RECORDER_VERSION="v0.8.5"
   NEW_TRANSCRIBER_VERSION="v0.6.3"
   
   # Pull new images
   docker pull mattermost/calls-recorder:$NEW_RECORDER_VERSION
   docker pull mattermost/calls-transcriber:$NEW_TRANSCRIBER_VERSION
   ```

2. **Create individual image archives**:
   ```bash
   # Save each image as a separate tar file
   docker save mattermost/calls-recorder:$NEW_RECORDER_VERSION -o calls-recorder-$NEW_RECORDER_VERSION.tar
   docker save mattermost/calls-transcriber:$NEW_TRANSCRIBER_VERSION -o calls-transcriber-$NEW_TRANSCRIBER_VERSION.tar
   
   # Compress the files for transfer
   gzip calls-recorder-$NEW_RECORDER_VERSION.tar
   gzip calls-transcriber-$NEW_TRANSCRIBER_VERSION.tar
   ```

3. **Create update script**:
   ```bash
   cat > update-air-gap-images.sh << 'EOF'
   #!/bin/bash
   
   # Air-Gap Image Update Script
   set -e
   
   NEW_RECORDER_VERSION="v0.8.5"
   NEW_TRANSCRIBER_VERSION="v0.6.3"
   REGISTRY_HOST="${REGISTRY_HOST:-localhost}"
   REGISTRY_PORT="${REGISTRY_PORT:-5000}"
   
   echo "Updating air-gap registry with new image versions..."
   echo "Recorder: $NEW_RECORDER_VERSION"
   echo "Transcriber: $NEW_TRANSCRIBER_VERSION"
   
   # Load new images into Docker
   echo "Loading new images..."
   gunzip calls-recorder-$NEW_RECORDER_VERSION.tar.gz
   gunzip calls-transcriber-$NEW_TRANSCRIBER_VERSION.tar.gz
   
   docker load -i calls-recorder-$NEW_RECORDER_VERSION.tar
   docker load -i calls-transcriber-$NEW_TRANSCRIBER_VERSION.tar
   
   # Tag images for local registry
   echo "Tagging images for local registry..."
   docker tag mattermost/calls-recorder:$NEW_RECORDER_VERSION $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-recorder:$NEW_RECORDER_VERSION
   docker tag mattermost/calls-transcriber:$NEW_TRANSCRIBER_VERSION $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-transcriber:$NEW_TRANSCRIBER_VERSION
   
   # Also update 'latest' tags
   docker tag mattermost/calls-recorder:$NEW_RECORDER_VERSION $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-recorder:latest
   docker tag mattermost/calls-transcriber:$NEW_TRANSCRIBER_VERSION $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-transcriber:latest
   
   # Push to local registry
   echo "Pushing images to local registry..."
   docker push $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-recorder:$NEW_RECORDER_VERSION
   docker push $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-transcriber:$NEW_TRANSCRIBER_VERSION
   docker push $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-recorder:latest
   docker push $REGISTRY_HOST:$REGISTRY_PORT/mattermost/calls-transcriber:latest
   
   echo "Image update complete!"
   echo ""
   echo "Verification commands:"
   echo "curl http://$REGISTRY_HOST:$REGISTRY_PORT/v2/mattermost/calls-recorder/tags/list"
   echo "curl http://$REGISTRY_HOST:$REGISTRY_PORT/v2/mattermost/calls-transcriber/tags/list"
   
   # Clean up temporary files
   rm calls-recorder-$NEW_RECORDER_VERSION.tar
   rm calls-transcriber-$NEW_TRANSCRIBER_VERSION.tar
   
   echo ""
   echo "Next steps:"
   echo "1. Restart calls-offloader service: sudo systemctl restart calls-offloader"
   echo "2. Test call recording functionality to verify the update"
   EOF
   
   chmod +x update-air-gap-images.sh
   ```

**Phase 2: Air-Gap Update**

1. **Transfer files to air-gapped environment**:
   - `calls-recorder-v0.8.5.tar.gz`
   - `calls-transcriber-v0.6.3.tar.gz`
   - `update-air-gap-images.sh`

2. **Run the update script**:
   ```bash
   chmod +x update-air-gap-images.sh
   sudo ./update-air-gap-images.sh
   ```

3. **Restart calls-offloader**:
   ```bash
   sudo systemctl restart calls-offloader
   ```

4. **Verify the update**:
   ```bash
   # Check available image tags
   curl http://localhost:5000/v2/mattermost/calls-recorder/tags/list
   curl http://localhost:5000/v2/mattermost/calls-transcriber/tags/list
   
   # Test calls-offloader functionality
   curl http://localhost:4545/version
   ```

#### Advantages of Each Method

**Complete Rebuild Method:**
- ✅ Ensures clean state with no leftover data
- ✅ Recommended for major version upgrades
- ✅ Simpler process (reuse existing automation)
- ❌ Larger data transfer requirements
- ❌ More downtime during registry replacement

**Incremental Update Method:**
- ✅ Minimal data transfer (only new images)
- ✅ Faster deployment process
- ✅ Preserves existing registry data
- ✅ Less downtime (registry stays running)
- ❌ More complex process
- ❌ Potential for version conflicts if not managed carefully

#### Choosing the Right Method

**Use Complete Rebuild when:**
- Upgrading across major plugin versions (e.g., v1.8.x to v1.9.x)
- Registry has accumulated significant old/unused images
- You want to ensure a completely clean state
- Data transfer size is not a primary concern

**Use Incremental Update when:**
- Applying minor version updates (e.g., v1.9.0 to v1.9.1)
- Bandwidth or transfer time is limited
- You need to minimize downtime
- The registry is working correctly and just needs new image versions

#### Post-Update Verification

After either upgrade method, perform these verification steps:

1. **Test recording functionality**:
   - Start a call in Mattermost
   - Enable call recording
   - Verify recording starts without errors

2. **Check job container creation**:
   ```bash
   # Monitor for new job containers during recording
   docker ps --format "{{.ID}} {{.Image}}" | grep calls
   ```

3. **Monitor calls-offloader logs**:
   ```bash
   sudo journalctl -u calls-offloader -f
   ```

4. **Verify image versions**:
   ```bash
   # Check that the new image versions are being used
   docker ps --format "{{.Image}}" | grep calls
   ```

## Other Calls Documentation

- [Calls Overview](calls-deployment.md): Overview of deployment options and architecture
- [RTCD Setup and Configuration](calls-rtcd-setup.md): Comprehensive guide for setting up the dedicated RTCD service
- [Calls Metrics and Monitoring](calls-metrics-monitoring.md): Guide to monitoring Calls performance using metrics and observability
- [Calls Deployment on Kubernetes](calls-kubernetes.md): Detailed guide for deploying Calls in Kubernetes environments
- [Calls Troubleshooting](calls-troubleshooting.md): Detailed troubleshooting steps and debugging techniques
- [calls-offloader performance documentation](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md): Detailed performance tuning and monitoring recommendations