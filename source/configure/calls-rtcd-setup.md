# RTCD Setup and Configuration

```{include} ../_static/badges/calls-rtcd-ent-only.md
```

This guide provides detailed instructions for setting up, configuring, and validating a Mattermost Calls deployment using the dedicated RTCD service.

## Prerequisites

Before deploying RTCD, ensure you have:

- A Mattermost Enterprise license
- A server or VM with sufficient CPU and network capacity (see the [Performance](calls-deployment.html#performance) section for sizing guidance)

## Network Requirements

The following network connectivity is required:

<style>
  table.network-requirements {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.95em;
  }
  table.network-requirements th, table.network-requirements td {
    border: 1px solid #888;
    padding: 6px 8px;
    vertical-align: top;
  }
  /* Dark mode border color */
  body:not([data-custom-theme="light"]) table.network-requirements th, 
  body:not([data-custom-theme="light"]) table.network-requirements td {
    border-color: #666;
  }
  table.network-requirements th {
    background: #f2f2f2;
    font-weight: bold;
    text-align: left;
  }
  /* Dark mode support for table headers */
  body:not([data-custom-theme="light"]) table.network-requirements th {
    background: #444;
    color: #fff;
  }
</style>

<table class="network-requirements">
<thead>
<tr>
<th>Service</th>
<th>Ports</th>
<th>Protocols</th>
<th>Source</th>
<th>Target</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>API (Calls plugin)</td>
<td>80,443</td>
<td>TCP (incoming)</td>
<td>Mattermost clients (web/desktop/mobile)</td>
<td>Mattermost instance (Calls plugin)</td>
<td>To allow for HTTP and WebSocket connectivity from clients to Calls plugin. This API is exposed on the same connection as Mattermost, so there's likely no need to change anything.</td>
</tr>
<tr>
<td>RTC (Calls plugin or <code>rtcd</code>)</td>
<td>8443</td>
<td>UDP (incoming)</td>
<td>Mattermost clients (Web/Desktop/Mobile) and calls-offloader</td>
<td>Mattermost instance or <code>rtcd</code> service</td>
<td>To allow clients to establish connections that transport calls related media (e.g. audio, video). This should be open on any network component (e.g. NAT, firewalls) in between the instance running the plugin (or <code>rtcd</code>) and the clients joining calls so that UDP traffic is correctly routed both ways (from/to clients).</td>
</tr>
<tr>
<td>RTC (Calls plugin or <code>rtcd</code>)</td>
<td>8443</td>
<td>TCP (incoming)</td>
<td>Mattermost clients (Web/Desktop/Mobile) and calls-offloader</td>
<td>Mattermost instance or <code>rtcd</code> service</td>
<td>To allow clients to establish connections that transport calls related media (e.g. audio, video). This should be open on any network component (e.g. NAT, firewalls) in between the instance running the plugin (or <code>rtcd</code>) and the clients joining calls so that TCP traffic is correctly routed both ways (from/to clients). This can be used as a backup channel in case clients are unable to connect using UDP. It requires <code>rtcd</code> version >= v0.11 and Calls version >= v0.17.</td>
</tr>
<tr>
<td>API (<code>rtcd</code>)</td>
<td>8045</td>
<td>TCP (incoming)</td>
<td>Mattermost instance(s) (Calls plugin)</td>
<td><code>rtcd</code> service</td>
<td>To allow for HTTP/WebSocket connectivity from Calls plugin to <code>rtcd</code> service. Can be expose internally as the service only needs to be reachable by the instance(s) running the Mattermost server.</td>
</tr>
<tr>
<td>STUN (Calls plugin or <code>rtcd</code>)</td>
<td>3478</td>
<td>UDP (outgoing)</td>
<td>Mattermost Instance(s) (Calls plugin) or <code>rtcd</code> service</td>
<td>Configured STUN servers</td>
<td>(Optional) To allow for either Calls plugin or <code>rtcd</code> service to discover their instance public IP. Only needed if configuring STUN/TURN servers. This requirement does not apply when manually setting an IP or hostname through the <a href="https://docs.mattermost.com/configure/plugins-configuration-settings.html#ice-host-override">ICE Host Override</a> config option.</td>
</tr>
</tbody>
</table>

## Installation and Deployment

There are multiple ways to deploy RTCD, depending on your environment. We recommend the following order based on production readiness and operational control:

### Bare Metal or VM Deployment (Recommended)

This is the recommended deployment method for non-Kubernetes production environments as it provides the best performance and operational control. For Kubernetes deployments, see the [Calls Deployment on Kubernetes](calls-kubernetes.md) guide.

1. Download the latest release from the [RTCD GitHub repository](https://github.com/mattermost/rtcd/releases)

2. Create a configuration file (`/opt/rtcd/rtcd.toml`) with the following settings:

   ```toml
   [api]
   http.listen_address = ":8045"
   security.allow_self_registration = true

   [rtc]
   ice_address_udp = ""
   ice_port_udp = 8443
   ice_address_tcp = ""
   ice_port_tcp = 8443
   ice_host_override = "YOUR_RTCD_SERVER_PUBLIC_IP"

   # UDP port range for WebRTC connections
   ice.port_range.min = 9000
   ice.port_range.max = 10000

   # STUN/TURN server configuration
   ice_servers = [
     { urls = ["stun:stun.global.calls.mattermost.com:3478"] }
   ]

   [store]
   data_source = "/opt/rtcd/data/db"

   [logger]
   enable_console = true
   console_json = true
   console_level = "INFO"
   enable_file = true
   file_json = true
   file_level = "INFO"
   file_location = "/opt/rtcd/rtcd.log"
   enable_color = true
   ```

3. Create a dedicated user for the RTCD service:

   ```bash
   sudo useradd --system --no-create-home --shell /bin/false mattermost
   ```

4. Create the data directory and set ownership:

   ```bash
   sudo mkdir -p /opt/rtcd/data/db
   sudo chown -R mattermost:mattermost /opt/rtcd
   ```

5. Create a systemd service file (`/etc/systemd/system/rtcd.service`):

   ```ini
   [Unit]
   Description=Mattermost RTCD Server
   After=network.target

   [Service]
   Type=simple
   User=mattermost
   Group=mattermost
   ExecStart=/opt/rtcd/rtcd --config /opt/rtcd/rtcd.toml
   Restart=always
   RestartSec=10
   LimitNOFILE=65536

   [Install]
   WantedBy=multi-user.target
   ```

5. Enable and start the service:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable rtcd
   sudo systemctl start rtcd
   ```

6. Check the service status:

   ```bash
   sudo systemctl status rtcd
   ```

### Docker Deployment

Docker deployment is suitable for development, testing, or containerized production environments:

1. Run the RTCD container with basic configuration:

   ```bash
   docker run -d --name rtcd \
     -e "RTCD_LOGGER_ENABLEFILE=true" \
     -e "RTCD_API_SECURITY_ALLOWSELFREGISTRATION=true" \
     -p 8443:8443/udp \
     -p 8443:8443/tcp \
     -p 8045:8045/tcp \
     mattermost/rtcd:latest
   ```

2. For debugging purposes, you can enable more detailed logging:

   ```bash
   docker run -d --name rtcd \
     -e "RTCD_LOGGER_ENABLEFILE=true" \
     -e "RTCD_LOGGER_CONSOLELEVEL=DEBUG" \
     -e "RTCD_API_SECURITY_ALLOWSELFREGISTRATION=true" \
     -p 8443:8443/udp \
     -p 8443:8443/tcp \
     -p 8045:8045/tcp \
     mattermost/rtcd:latest
   ```

   To view the logs:

   ```bash
   docker logs -f rtcd
   ```

You can also use a mounted configuration file instead of environment variables:

```bash
docker run -d --name rtcd \
  -p 8045:8045 \
  -p 8443:8443/udp \
  -p 8443:8443/tcp \
  -v /path/to/config.toml:/rtcd/config/config.toml \
  mattermost/rtcd:latest
```

For a complete sample configuration file, see the [RTCD config.sample.toml](https://github.com/mattermost/rtcd/blob/master/config/config.sample.toml) in the official repository.

### Kubernetes Deployment

For Kubernetes deployments, use the official Helm chart:

1. Add the Mattermost Helm repository:

   ```bash
   helm repo add mattermost https://helm.mattermost.com
   helm repo update
   ```

2. Install the RTCD chart:

   ```bash
   helm install mattermost-rtcd mattermost/mattermost-rtcd \
     --set ingress.enabled=true \
     --set ingress.host=rtcd.example.com \
     --set service.annotations."service\\.beta\\.kubernetes\\.io/aws-load-balancer-backend-protocol"=udp \
     --set rtcd.ice.hostOverride=rtcd.example.com
   ```

   Refer to the [RTCD Helm chart documentation](https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-rtcd) for additional configuration options.

## Configuration

### RTCD Configuration File

The RTCD service uses a TOML configuration file. Here's an example with commonly used settings:

```toml
[api]
# The address and port to which the HTTP API server will listen
http.listen_address = ":8045"
# Security settings for authentication
security.allow_self_registration = true
security.enable_admin = true
security.admin_secret_key = "YOUR_API_KEY"

[rtc]
# The UDP address and port for media traffic
ice_address_udp = ""
ice_port_udp = 8443
# The TCP address and port for fallback connections 
ice_address_tcp = ""
ice_port_tcp = 8443
# Public hostname or IP that clients will use to connect
ice_host_override = "RTCD_SERVER_PUBLIC_IP"

[logger]
# Logging configuration
enable_console = true
console_json = false
console_level = "INFO"
enable_file = true
file_json = true
file_level = "INFO"
file_location = "/opt/rtcd/rtcd.log"
```

Key Configuration Options:

- **api.http.listen_address**: The address and port where the RTCD HTTP API service listens
- **rtc.ice_address_udp**: The UDP address for media traffic (empty means listen on all interfaces)
- **rtc.ice_port_udp**: The UDP port for media traffic 
- **rtc.ice_address_tcp**: The TCP address for fallback media traffic
- **rtc.ice_port_tcp**: The TCP port for fallback media traffic
- **rtc.ice_host_override**: The public hostname or IP address clients will use to connect to RTCD
- **api.security.admin_secret_key**: API key for Mattermost servers to authenticate with RTCD

### Required Mattermost Server Configuration

When using RTCD, you must configure the Mattermost server's CORS settings to allow proper communication between the server and the RTCD service.

#### CORS Configuration

The `AllowCorsFrom` setting must include your SiteURL and, if using calls-offloader in a private network, the Mattermost server's private IP address:

**Using mmctl:**
```bash
# Basic RTCD configuration - include your SiteURL
mmctl config set ServiceSettings.AllowCorsFrom "https://your-domain.com"

# If using calls-offloader in a private network, also include Mattermost's private IP with port 8065
mmctl config set ServiceSettings.AllowCorsFrom "https://your-domain.com http://192.168.1.100:8065"
```

**Using System Console:**
1. Go to **System Console > Environment > Web Server**
2. Set **Allow cross-origin requests from** to include:
   - Your SiteURL (e.g., `https://your-domain.com`)
   - If using calls-offloader in a private network: Also include Mattermost's private IP with port 8065 (e.g., `http://192.168.1.100:8065`)

**Using config.json:**
```json
{
  "ServiceSettings": {
    "AllowCorsFrom": "https://your-domain.com http://192.168.1.100:8065"
  }
}
```

```{important}
This CORS configuration is specifically required for RTCD deployments and is not needed for integrated mode deployments. Multiple origins should be separated by spaces.
```

### STUN/TURN Configuration

For clients behind strict firewalls, you may need to configure STUN/TURN servers. In the RTCD configuration file, reference your STUN/TURN servers as follows:

```toml
[rtc]
# STUN/TURN server configuration
   ice_servers = [
     { urls = ["stun:stun.global.calls.mattermost.com:3478"] }
   #  { urls = ["turn:turn.example.com:3478"], username = "turnuser", credential = "turnpassword" }
   ]

```

We recommend using [coturn](https://github.com/coturn/coturn) for your TURN server implementation. 

### System Tuning

For high-volume deployments, tune your Linux system:

1. Add the following to `/etc/sysctl.conf`:

   ```bash
   # Increase UDP buffer sizes
   net.core.rmem_max = 16777216
   net.core.wmem_max = 16777216
   net.core.optmem_max = 16777216
   ```

2. Apply the settings:

   ```bash
   sudo sysctl -p
   ```

## Validation and Testing

After deploying RTCD, validate the installation:

1. **Check service status and version**:

   ```bash
   curl http://YOUR_RTCD_SERVER:8045/version
   # Should return a JSON object with service information
   # Example: {"build_hash":"abc123","build_date":"2023-01-15T12:00:00Z","build_version":"0.11.0","goVersion":"go1.20.4"}
   ```

2. **Test UDP connectivity**:

   On the RTCD server:
   
   ```bash
   nc -l -u -p 8443
   ```

   On a client machine:
   
   ```bash
   nc -v -u YOUR_RTCD_SERVER 8443
   ```
      
   Type a message and hit Enter on either side. If messages are received on both ends, UDP connectivity is working.

   Note: This test must be run with the RTCD service stopped, as it binds to the same port.

   ```bash
   sudo systemctl stop rtcd
   ```

3. **Test TCP connectivity** (if enabled):

   Similar to the UDP test, but remove the `-u` flag from both commands.

4. **Monitor metrics**:

   Refer to [Calls Metrics and Monitoring](calls-metrics-monitoring.md) for setting up Calls metrics and monitoring.

## Horizontal Scaling

To scale RTCD horizontally:

1. **Deploy multiple RTCD instances**:
   
   Deploy multiple RTCD servers, each with their own unique IP address.

2. **Configure DNS-based load balancing**:
   
   Set up a DNS record that points to multiple RTCD IP addresses:
   
   ```bash
   rtcd.example.com.    IN A    10.0.0.1
   rtcd.example.com.    IN A    10.0.0.2
   rtcd.example.com.    IN A    10.0.0.3
   ```

3. **Configure health checks**:
   
   Set up health checks to automatically remove unhealthy RTCD instances from DNS.

4. **Configure Mattermost**:
   
   In the Mattermost System Console, set the **RTCD Service URL** to your DNS name (e.g., `rtcd.example.com`).

The Mattermost Calls plugin will distribute calls among the available RTCD hosts. Remember that a single call will always be hosted on one RTCD instance; sessions belonging to the same call are not spread across different instances.

## Integration with Mattermost

Once RTCD is properly set up and validated, configure Mattermost to use it:

1. Go to **System Console > Plugins > Calls**

2. Enable the **Enable RTCD Service** option

3. Set the **RTCD Service URL** to your RTCD service address (either a single server or DNS load-balanced hostname)

4. If configured, enter the **RTCD API Key** that matches the one in your RTCD configuration

5. Save the configuration

6. Test by creating a new call in any Mattermost channel

7. Verify that the call is being routed through RTCD by checking the RTCD logs and metrics

## Other Calls Documentation

- [Calls Overview](calls-deployment.md): Overview of deployment options and architecture
- [Calls Offloader Setup and Configuration](calls-offloader-setup.md): Setup guide for call recording and transcription
- [Calls Metrics and Monitoring](calls-metrics-monitoring.md): Guide to monitoring Calls performance using metrics and observability
- [Calls Deployment on Kubernetes](calls-kubernetes.md): Detailed guide for deploying Calls in Kubernetes environments
- [Calls Troubleshooting](calls-troubleshooting.md): Detailed troubleshooting steps and debugging techniques

For detailed Mattermost Calls configuration options, see the [Calls Plugin Configuration Settings](plugins-configuration-settings.rst#calls) documentation.