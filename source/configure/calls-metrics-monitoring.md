# Calls Metrics and Monitoring

```{include} ../_static/badges/ent-only.md
```

This guide provides detailed information on monitoring Mattermost Calls performance and health through metrics and observability tools. Effective monitoring is essential for maintaining optimal call quality and quickly addressing any issues that arise.

- [Metrics overview](#metrics-overview)
- [Setting up monitoring](#setting-up-monitoring)
- [Key metrics to monitor](#key-metrics-to-monitor)
- [Performance baselines](#performance-baselines)
- [Troubleshooting metrics collection](#troubleshooting-metrics-collection)

## Metrics Overview

Mattermost Calls provides metrics through Prometheus for both the Calls plugin and the RTCD service. These metrics help track:

- Active call sessions and participants
- Media track statistics
- Connection states and errors
- Resource utilization (CPU, memory, network)
- WebSocket connections and events

The metrics are exposed through HTTP endpoints:

- **Calls Plugin**: `/plugins/com.mattermost.calls/metrics`
- **RTCD Service**: `/metrics` (default) or a configured endpoint

## Setting Up Monitoring

### Prerequisites

To monitor Calls metrics, you'll need:

1. **Prometheus**: For collecting and storing metrics
2. **Grafana**: For visualizing metrics (optional but recommended)

### Installing Prometheus

1. **Download and install Prometheus**:

   Visit the [Prometheus download page](https://prometheus.io/download/) for installation instructions.

2. **Configure Prometheus** to scrape metrics from all Calls-related services:

   Complete `prometheus.yml` configuration for Calls monitoring:

   ```yaml
   global:
     scrape_interval: 15s
     evaluation_interval: 15s

   scrape_configs:
     - job_name: 'prometheus'
       static_configs:
         - targets: ['PROMETHEUS_IP:9090']

     - job_name: 'mattermost'
       metrics_path: /metrics
       static_configs:
         - targets: ['MATTERMOST_SERVER_IP:8067']

     - job_name: 'calls-plugin'
       metrics_path: /plugins/com.mattermost.calls/metrics
       static_configs:
         - targets: ['MATTERMOST_SERVER_IP:8067']
           labels:
             service_name: 'calls-plugin'

     - job_name: 'rtcd'
       metrics_path: /metrics
       static_configs:
         - targets: ['RTCD_SERVER_IP:8045']
           labels:
             service_name: 'rtcd'

     - job_name: 'rtcd-node-exporter'
       metrics_path: /metrics
       static_configs:
         - targets: ['RTCD_SERVER_IP:9100']
           labels:
             service_name: 'rtcd'

     - job_name: 'calls_offloader-node-exporter'
       metrics_path: /metrics
       static_configs:
         - targets: ['CALLS_OFFLOADER_SERVER_IP:9100']
           labels:
             service_name: 'offloader'
   ```

   Replace the placeholder IP addresses with your actual server addresses:
   
   - `MATTERMOST_SERVER_IP`: IP address of your Mattermost server
   - `RTCD_SERVER_IP`: IP address of your RTCD server  
   - `CALLS_OFFLOADER_SERVER_IP`: IP address of your calls-offloader server (if deployed)
   - `PROMETHEUS_IP`: IP address of your Prometheus server
   - **Note**: The configuration above uses the default ports (RTCD: `8045`, Mattermost metrics: `8067`, etc.).  Adjust these ports in `prometheus.yml` if you have customized them.

   ```{important}
   **Metrics Path**: Ensure the metrics paths are correct. The RTCD service exposes metrics at `/metrics` by default, and the Calls plugin at `/plugins/com.mattermost.calls/metrics`.
   ```

   ```{important}
   **Metrics Configuration Notice**: Use the `service_name` labels as shown in the configuration above. These labels help organize metrics in dashboards and enable proper service identification. 
   ```

   ```{note}
   - **node_exporter**: Optional but recommended for system-level metrics (CPU, memory, disk, network). See [node_exporter setup guide](https://prometheus.io/docs/guides/node-exporter/) for installation instructions.
   - **calls-offloader**: Only needed if you have call recording/transcription enabled
   ```

### Installing Grafana

1. **Download and install Grafana**:

   Visit the [Grafana download page](https://grafana.com/grafana/download) for installation instructions.

2. **Configure Grafana** to use Prometheus as a data source:
   
   - Add a new data source in Grafana
   - Select Prometheus as the type
   - Enter the URL of your Prometheus server
   - Test and save the configuration

3. **Import the Mattermost Calls dashboard**:

   - Navigate to Dashboards > Import in Grafana
   - Enter dashboard ID: `23225` or use the direct link: [Mattermost Calls Performance Monitoring](https://grafana.com/grafana/dashboards/23225-mattermost-calls-performance-monitoring/)
   - Select your Prometheus data source, and enter values for the
   - Confirm the port used for RTCD metrics (default is `8045`), and the port used for the Calls plugin metrics (default is `8067`)
   - Click Import to add the dashboard to your Grafana instance

   ```{note}
   The dashboard is also available as JSON source from the [Mattermost performance assets repository](https://github.com/mattermost/mattermost-performance-assets/blob/master/grafana/mattermost-calls-performance-monitoring.json) for manual import or customization.
   ```

## Key Metrics to Monitor

### RTCD Metrics

#### Process Metrics

These metrics help monitor the health and resource usage of the RTCD process:

- `rtcd_process_cpu_seconds_total`: Total CPU time spent
- `rtcd_process_open_fds`: Number of open file descriptors
- `rtcd_process_max_fds`: Maximum number of file descriptors
- `rtcd_process_resident_memory_bytes`: Memory usage in bytes
- `rtcd_process_virtual_memory_bytes`: Virtual memory used

**Interpretation**: 

- High CPU usage (>70%) may indicate the need for additional RTCD instances
- Steadily increasing memory usage might indicate a memory leak
- High number of file descriptors could indicate connection handling issues

#### WebRTC Connection Metrics

These metrics track the WebRTC connections and media flow:

- `rtcd_rtc_conn_states_total{state="X"}`: Count of connections in different states
- `rtcd_rtc_errors_total{type="X"}`: Count of RTC errors by type
- `rtcd_rtc_rtp_tracks_total{direction="X"}`: Count of RTP tracks (incoming/outgoing)
- `rtcd_rtc_sessions_total`: Total number of active RTC sessions

**Interpretation**:

- Increasing error counts may indicate connectivity or configuration issues
- Track by state to see if connections are failing to establish or dropping
- Larger track counts require proportionally more CPU and bandwidth

#### WebSocket Metrics

These metrics track the signaling channel:

- `rtcd_ws_connections_total`: Total number of active WebSocket connections
- `rtcd_ws_messages_total{direction="X"}`: Count of WebSocket messages (sent/received)

**Interpretation**:

- Connection count should match expected participant numbers
- Unusually high message counts might indicate protocol issues
- Connection drops might indicate network issues

### Calls Plugin Metrics

Similar metrics are available for the Calls plugin with the following prefixes:

- Process metrics: `mattermost_plugin_calls_process_*`
- WebRTC connection metrics: `mattermost_plugin_calls_rtc_*`
- WebSocket metrics: `mattermost_plugin_calls_websocket_*`
- Store metrics: `mattermost_plugin_calls_store_ops_total`

## Performance Baselines

The following performance benchmarks provide baseline metrics for RTCD deployments under various load conditions and configurations.

**Deployment specifications**

- 1x r6i.large nginx proxy
- 3x c5.large MM app nodes (HA)
- 2x db.x2g.xlarge RDS Aurora MySQL v8 (one writer, one reader)
- 1x (c7i.xlarge, c7i.2xlarge, c7i.4xlarge) RTCD
- 2x c7i.2xlarge load-test agents

**App specifications**

- Mattermost v9.6
- Mattermost Calls v0.28.0
- RTCD v0.16.0
- load-test agent v0.28.0

**Media specifications**

- Speech sample bitrate: 80Kbps
- Screen sharing sample bitrate: 1.6Mbps

**Results**

Below are the detailed benchmarks based on internal performance testing:

<table class="network-requirements">
<thead>
<tr>
<th>Calls</th>
<th>Participants/call</th>
<th>Unmuted/call</th>
<th>Screen sharing</th>
<th>CPU (avg)</th>
<th>Memory (avg)</th>
<th>Bandwidth (in/out)</th>
<th>Instance type (RTCD)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1000</td>
<td>2</td>
<td>no</td>
<td>47%</td>
<td>1.46GB</td>
<td>1Mbps / 194Mbps</td>
<td>c7i.xlarge</td>
</tr>
<tr>
<td>1</td>
<td>800</td>
<td>1</td>
<td>yes</td>
<td>64%</td>
<td>1.43GB</td>
<td>2.7Mbps / 1.36Gbps</td>
<td>c7i.xlarge</td>
</tr>
<tr>
<td>1</td>
<td>1000</td>
<td>1</td>
<td>yes</td>
<td>79%</td>
<td>1.54GB</td>
<td>2.9Mbps / 1.68Gbps</td>
<td>c7i.xlarge</td>
</tr>
<tr>
<td>10</td>
<td>100</td>
<td>1</td>
<td>yes</td>
<td>74%</td>
<td>1.56GB</td>
<td>18.2Mbps / 1.68Gbps</td>
<td>c7i.xlarge</td>
</tr>
<tr>
<td>100</td>
<td>10</td>
<td>2</td>
<td>no</td>
<td>49%</td>
<td>1.46GB</td>
<td>18.7Mbps / 175Mbps</td>
<td>c7i.xlarge</td>
</tr>
<tr>
<td>100</td>
<td>10</td>
<td>1</td>
<td>yes</td>
<td>84%</td>
<td>1.73GB</td>
<td>171Mbps / 1.53Gbps</td>
<td>c7i.xlarge</td>
</tr>
<tr>
<td>1</td>
<td>1000</td>
<td>2</td>
<td>no</td>
<td>20%</td>
<td>1.44GB</td>
<td>1.4Mbps / 194Mbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>1</td>
<td>1000</td>
<td>2</td>
<td>yes</td>
<td>49%</td>
<td>1.53GB</td>
<td>3.6Mbps / 1.79Gbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>2</td>
<td>1000</td>
<td>1</td>
<td>yes</td>
<td>73%</td>
<td>2.38GB</td>
<td>5.7Mbps / 3.06Gbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>100</td>
<td>10</td>
<td>2</td>
<td>yes</td>
<td>60%</td>
<td>1.74GB</td>
<td>181Mbps / 1.62Gbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>150</td>
<td>10</td>
<td>1</td>
<td>yes</td>
<td>72%</td>
<td>2.26GB</td>
<td>257Mbps / 2.30Gbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>150</td>
<td>10</td>
<td>2</td>
<td>yes</td>
<td>79%</td>
<td>2.34GB</td>
<td>271Mbps / 2.41Gbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>250</td>
<td>10</td>
<td>2</td>
<td>no</td>
<td>58%</td>
<td>2.66GB</td>
<td>47Mbps / 439Mbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>1000</td>
<td>2</td>
<td>2</td>
<td>no</td>
<td>78%</td>
<td>2.31GB</td>
<td>178Mbps / 195Mbps</td>
<td>c7i.2xlarge</td>
</tr>
<tr>
<td>2</td>
<td>1000</td>
<td>2</td>
<td>yes</td>
<td>41%</td>
<td>2.6GB</td>
<td>7.23Mbps / 3.60Gbps</td>
<td>c7i.4xlarge</td>
</tr>
<tr>
<td>3</td>
<td>1000</td>
<td>2</td>
<td>yes</td>
<td>63%</td>
<td>3.53GB</td>
<td>10.9Mbps / 5.38Gbps</td>
<td>c7i.4xlarge</td>
</tr>
<tr>
<td>4</td>
<td>1000</td>
<td>2</td>
<td>yes</td>
<td>83%</td>
<td>4.40GB</td>
<td>14.5Mbps / 7.17Gbps</td>
<td>c7i.4xlarge</td>
</tr>
<tr>
<td>250</td>
<td>10</td>
<td>2</td>
<td>yes</td>
<td>79%</td>
<td>3.49GB</td>
<td>431Mbps / 3.73Gbps</td>
<td>c7i.4xlarge</td>
</tr>
<tr>
<td>500</td>
<td>2</td>
<td>2</td>
<td>yes</td>
<td>71%</td>
<td>2.54GB</td>
<td>896Mbps / 919Mbps</td>
<td>c7i.4xlarge</td>
</tr>
</tbody>
</table>

## Troubleshooting Metrics Collection

### Verify RTCD Metrics are Being Collected

To verify that Prometheus is successfully collecting RTCD metrics, use this command:

```bash
curl http://PROMETHEUS_IP:9090/api/v1/label/__name__/values | jq '.' | grep rtcd
```

This command queries Prometheus for all available metric names and filters for RTCD-related metrics.

If no RTCD metrics appear, check:
1. RTCD is running
2. Prometheus is configured to scrape the RTCD metrics endpoint
3. RTCD metrics port is accessible from Prometheus (default: 8045)

### Check Prometheus Scrape Targets

To verify all Calls-related services are being scraped successfully:

1. Open the Prometheus web interface (typically `http://PROMETHEUS_IP:9090`)
2. Navigate to **Status > Targets**
3. Look for your configured Calls services:
   - Mattermost server (for Calls plugin metrics)
   - RTCD service

Each target should show status "UP" in green. If a target shows "DOWN" or errors:
- Verify the service is running
- Check network connectivity between Prometheus and the target
- Verify the metrics endpoint is accessible

## Other Calls Documentation

- [Calls Overview](calls-deployment.md): Overview of deployment options and architecture
- [RTCD Setup and Configuration](calls-rtcd-setup.md): Comprehensive guide for setting up the dedicated RTCD service
- [Calls Offloader Setup and Configuration](calls-offloader-setup.md): Setup guide for call recording and transcription
- [Calls Deployment on Kubernetes](calls-kubernetes.md): Detailed guide for deploying Calls in Kubernetes environments
- [Calls Troubleshooting](calls-troubleshooting.md): Detailed troubleshooting steps and debugging techniques

Configure Prometheus storage accordingly to balance disk usage with retention needs.