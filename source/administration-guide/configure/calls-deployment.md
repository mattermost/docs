# Calls self-hosted deployment

```{include} ../../_static/badges/all-commercial.md
```

Mattermost Calls is an excellent option for organizations demanding enhanced security and control over their communication infrastructure. Calls is designed to operate securely in self-hosted deployments, including [air-gapped environments](https://docs.mattermost.com/configure/calls-deployment.html#air-gapped-deployments), ensuring private communication without reliance on public internet connectivity with flexible configuration options for complex network requirements.

This document provides information on how to successfully make the Calls plugin work on self-hosted deployments. It also outlines some of the most common deployment strategies with example diagrams, and provides the deployment guidelines for the recording, transcription, and live captions service.

## Terminology

- [WebRTC](https://bloggeek.me/webrtcglossary/webrtc-2/): The set of underlying protocols/specifications on top of which calls are implemented.
- **RTC (Real Time Connection)**: The real-time connection. This is the channel used to send media tracks (audio/video/screen).
- **WS (WebSocket)**: The WebSocket connection. This is the channel used to set up a connection (signaling process).
- [NAT (Network Address Translation)](https://bloggeek.me/webrtcglossary/nat/): A networking technique to map IP addresses.
- [STUN (Session Traversal Utilities for NAT)](https://bloggeek.me/webrtcglossary/stun/): A protocol/service used by WebRTC clients to help traversing NATs. On the server side it's mainly used to figure out the public IP of the instance.
- [TURN (Traversal Using Relays around NAT)](https://bloggeek.me/webrtcglossary/turn/): A protocol/service used to help WebRTC clients behind strict firewalls connect to a call through media relay.

## Plugin components

- **Calls plugin**: This is the main entry point and a requirement to enable channel calls.

- **rtcd**: This is an optional service that can be deployed to offload all the functionality and data processing involved with the WebRTC connections. Read more about when and why to use [rtcd](#the-rtcd-service) below.

## Requirements

### Server

- Run Mattermost server on a secure (HTTPs) connection. This is a necessary requirement on the client to allow capturing devices (e.g., microphone, screen). See the [config TLS](https://docs.mattermost.com/deploy/server/setup-tls.html) section for more info.
- See [network requirements](#network) below.

### Client

- Clients need to be able to connect (send and receive data) to the instance hosting the calls through the UDP port configured as `RTC Server Port`. If this is not possible a TURN server should be used to achieve connectivity.
- Depending on the platform or operating system, clients may need to grant additional permissions to the application (e.g., browser, desktop app) to allow them to capture audio inputs or share the screen.

### Network

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
<td>Mattermost clients (Web/Desktop/Mobile)</td>
<td>Mattermost instance or <code>rtcd</code> service</td>
<td>To allow clients to establish connections that transport calls related media (e.g. audio, video). This should be open on any network component (e.g. NAT, firewalls) in between the instance running the plugin (or <code>rtcd</code>) and the clients joining calls so that UDP traffic is correctly routed both ways (from/to clients).</td>
</tr>
<tr>
<td>RTC (Calls plugin or <code>rtcd</code>)</td>
<td>8443</td>
<td>TCP (incoming)</td>
<td>Mattermost clients (Web/Desktop/Mobile)</td>
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

#### Air-gapped deployments

Mattermost Calls can function in air-gapped environments. Exposing Calls to the public internet is only necessary when users need to connect from outside the local network, and no existing method supports that connection. In such setups:

- Users should connect from within the private/local network. This can be done on-premises, through a VPN, or via virtual machines.
- Configuring a STUN server is unnecessary, as all connections occur within the local network.
- The [ICE Host Override](https://docs.mattermost.com/configure/plugins-configuration-settings.html#ice-host-override) configuration setting can be optionally set with a local IP address (e.g., 192.168.1.45), depending on the specific network configuration and topology.

## Limitations

- All Mattermost customers can start, join, and participate in 1:1 audio calls with optional screen sharing.
- For group calls up to 50 concurrent users, Mattermost Enterprise, Professional, or Mattermost Cloud is required.
- Enterprise customers can also [record calls](https://docs.mattermost.com/collaborate/make-calls.html#record-a-call), enable [live text captions](https://docs.mattermost.com/collaborate/make-calls.html#live-captions-during-calls) during calls, and [transcribe recorded calls](https://docs.mattermost.com/collaborate/make-calls.html#transcribe-recorded-calls). We recommend that Enterprise self-hosted customers looking for group calls beyond 50 concurrent users consider using the [dedicated rtcd service](#the-rtcd-service).
- For Mattermost self-hosted deployments, System admins need to enable and configure the plugin [using the System Console](https://docs.mattermost.com/configure/plugins-configuration-settings.html#calls). The default maximum number of participants is unlimited; however, we recommend a maximum of 50 participants per call. Maximum call participants is configurable by going to **System Console > Plugin Management > Calls > Max call participants**. Call participant limits greatly depends on instance resources. For more details, refer to the [performance section](#performance) below.

## Configuration

For Mattermost self-hosted customers, the calls plugin is pre-packaged, installed, and enabled. Configuration to allow end-users to use it can be found in the [System Console](https://docs.mattermost.com/configure/plugins-configuration-settings.html#calls).

## Modes of operation

Depending on how the Mattermost server is running, there are several modes under which the Calls plugin can operate. Please refer to the section below on [the rtcd service](#the-rtcd-service) to learn about the `rtcd` and the Selective Forwarding Unit (SFU).

| Mattermost deployment | SFU | SFU deployment |
|-----------------------|-----|----------------|
| Single instance | integrated | |
| Single instance | rtcd | |
| High availability cluster-based | integrated | clustered |
| High availability cluster-based | rtcd | |

### Single instance

#### Integrated

This is the default mode when first installing the plugin on a single Mattermost instance setup. The WebRTC service is integrated in the plugin itself and runs alongside the Mattermost server.

![A diagram of the integrated configuration model of a single instance.](/images/calls-deployment-image3.png)

#### rtcd

```{include} ../../_static/badges/ent-plus.md
```

An external, dedicated and scalable WebRTC service (`rtcd`) is used to handle all calls media routing.

![A diagram of a Web RTC deployment configuration.](/images/calls-deployment-image7.png)

### High availability cluster-based

```{include} ../../_static/badges/ent-plus.md
```

#### Clustered

This is the default mode when running the plugin in a high availability cluster-based deployment. Every Mattermost node will run an instance of the plugin that includes a WebRTC service. Calls are distributed across all available nodes through the existing load-balancer: a call is hosted on the instance where the initiating websocket connection (first client to join) is made. A single call will be hosted on a single cluster node.

![A diagram of a clustered calls deployment.](/images/calls-deployment-image5.png)

#### rtcd (High Availability)

![A diagram of an rtcd deployment.](/images/calls-deployment-image2.png)

## Performance

Calls performance primarily depends on two resources: CPU and bandwidth (both network latency and overall throughput). The final consumption exhibits quadratic growth with the number of clients transmitting and receiving media.

As an example, a single call with 10 participants of which two are unmuted (transmitting voice data) will generally consume double the resources than the same call with a single participant unmuted. What ultimately counts towards performance is the overall number of concurrent media flows (in/out) across the server.

### Benchmarks

Here are the results from internally conducted performance and ceiling tests on a dedicated `rtcd` instance:

#### Deployment specifications

- 1x r6i.large nginx proxy
- 3x c5.large MM app nodes (HA)
- 2x db.x2g.xlarge RDS Aurora MySQL v8 (one writer, one reader)
- 1x (c7i.xlarge, c7i.2xlarge, c7i.4xlarge) RTCD
- 2x c7i.2xlarge load-test agents

#### App specifications

- Mattermost v9.6
- Mattermost Calls v0.28.0
- RTCD v0.16.0
- load-test agent v0.28.0

#### Media specifications

- Speech sample bitrate: 80Kbps
- Screen sharing sample bitrate: 1.6Mbps

#### Results

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

```{note}
- The tests focused on a single, vertically scaled RTCD instance to understand the processing limits within a single node. Scaling the RTCD service horizontally should be sufficient to support a higher number of calls.
- RTCD processes were executed with all performance profiling enabled (including block and mutex). This resulted in some computational overhead.
- Both speech and screen samples have slightly higher bitrates than the average produced by a real client (e.g., a browser). This gives us some safety margin over real-world deployments.
```

### Dedicated service

For Enterprise customers we offer a way to offload performance costs through a [dedicated service](https://github.com/mattermost/rtcd) that can be used to further scale up calls.

### Load testing

We provide a [load-test tool](https://github.com/mattermost/mattermost-plugin-calls/tree/main/lt) that can be used to simulate and measure the performance impact of calls.

### Monitoring

Both the plugin and the external `rtcd` service expose some Prometheus metrics to monitor performance. We provide an [official dashboard](https://grafana.com/grafana/dashboards/23225-mattermost-calls-performance-monitoring/) that can be imported in Grafana. You can refer to [Performance monitoring](https://docs.mattermost.com/scale/deploy-prometheus-grafana-for-performance-monitoring.html) for more information on how to set up Prometheus and visualize metrics through Grafana.

#### Calls plugin metrics

Metrics for the calls plugin are exposed through the `/plugins/com.mattermost.calls/metrics` subpath under the existing Mattermost server metrics endpoint. This is controlled by the [Listen address for performance](https://docs.mattermost.com/configure/environment-configuration-settings.html#listen-address-for-performance) configuration setting. It defaults to port ``8067``.

```{note}
- The [Metrics plugin](https://docs.mattermost.com/scale/collect-performance-metrics.html) collects application-level metrics only and does not make system or OS-level calls. As a result, data typically derived from system-level metrics may be missing in the Grafana panel.
- On Mattermost versions prior to v9.5, plugin metrics were exposed through the public `/plugins/com.mattermost.calls/metrics` API endpoint controlled by the [Web server listen address](https://docs.mattermost.com/configure/environment-configuration-settings.html#web-server-listen-address) configuration setting. This defaults to port `8065`.
```

**Process**

- `mattermost_plugin_calls_process_cpu_seconds_total`: Total user and system CPU time spent in seconds.
- `mattermost_plugin_calls_process_max_fds`: Maximum number of open file descriptors.
- `mattermost_plugin_calls_process_open_fds`: Number of open file descriptors.
- `mattermost_plugin_calls_process_resident_memory_bytes`: Resident memory size in bytes.
- `mattermost_plugin_calls_process_virtual_memory_bytes`: Virtual memory size in bytes.

**WebRTC connection**

- `mattermost_plugin_calls_rtc_conn_states_total`: Total number of RTC connection state changes.
- `mattermost_plugin_calls_rtc_errors_total`: Total number of RTC errors.
- `mattermost_plugin_calls_rtc_rtp_bytes_total`: Total number of sent/received RTP packets in bytes.

  - Note: removed as of v0.16.0

- `mattermost_plugin_calls_rtc_rtp_packets_total`: Total number of sent/received RTP packets.

  - Note: removed as of v0.16.0

- `mattermost_plugin_calls_rtc_rtp_tracks_total`: Total number of incoming/outgoing RTP tracks.

  - Note: added as of v0.16.0

- `mattermost_plugin_calls_rtc_sessions_total`: Total number of active RTC sessions.

**Application**

- `mattermost_plugin_calls_app_handlers_time_bucket`: Time taken to execute app handlers.

  - `mattermost_plugin_calls_app_handlers_time_sum`

  - `mattermost_plugin_calls_app_handlers_time_count`

**Database**

- `mattermost_plugin_calls_store_ops_total`: Total number of db store operations.
- `mattermost_plugin_calls_store_methods_time_bucket`: Time taken to execute store methods.

  - `mattermost_plugin_calls_store_methods_time_sum`

  - `mattermost_plugin_calls_store_methods_time_count`
- `mattermost_plugin_calls_cluster_mutex_grab_time_bucket`: Time taken to grab global mutexes.

  - `mattermost_plugin_calls_cluster_mutex_grab_time_sum`

  - `mattermost_plugin_calls_cluster_mutex_grab_time_count`
- `mattermost_plugin_calls_cluster_mutex_locked_time_bucket`: Time spent locked in global mutexes.

  - `mattermost_plugin_calls_cluster_mutex_locked_time_sum`
  
  - `mattermost_plugin_calls_cluster_mutex_locked_time_count`

**WebSocket**

- `mattermost_plugin_calls_websocket_connections_total`: Total number of active WebSocket connections.
- `mattermost_plugin_calls_websocket_events_total`: Total number of WebSocket events.

**Jobs**

- `mattermost_plugin_calls_jobs_live_captions_new_audio_len_ms_bucket`: Duration (in ms) of new audio transcribed for live captions.

  - `mattermost_plugin_calls_jobs_live_captions_new_audio_len_ms_sum`

  - `mattermost_plugin_calls_jobs_live_captions_new_audio_len_ms_count`
- `mattermost_plugin_calls_jobs_live_captions_pktPayloadCh_buf_full`: Total packets of audio data dropped due to full channel.
- `mattermost_plugin_calls_jobs_live_captions_window_dropped`: Total windows of audio data dropped due to pressure on the transcriber.

#### WebRTC service metrics

Metrics for the `rtcd` service are exposed through the `/metrics` API endpoint under the `rtcd` API listener controlled by the `api.http.listen_address` configuration setting. It defaults to port `8045`.

**Process**

- `rtcd_process_cpu_seconds_total`:  Total user and system CPU time spent in seconds.
- `rtcd_plugin_calls_process_max_fds`: Maximum number of open file descriptors.
- `rtcd_plugin_calls_process_open_fds`: Number of open file descriptors.
- `rtcd_plugin_calls_process_resident_memory_bytes`: Resident memory size in bytes.
- `rtcd_plugin_calls_process_virtual_memory_bytes`: Virtual memory size in bytes.

**WebRTC Connection**

- `rtcd_rtc_conn_states_total`: Total number of RTC connection state changes.
- `rtcd_rtc_errors_total`: Total number of RTC errors.
- `rtcd_rtc_rtp_bytes_total`: Total number of sent/received RTP packets in bytes.
- `rtcd_rtc_rtp_packets_total`: Total number of sent/received RTP packets.
- `rtcd_rtc_rtp_tracks_total`: Total number of incoming/outgoing RTP tracks.
- `rtcd_rtc_sessions_total`: Total number of active RTC sessions.
- `rtcd_rtc_rtp_tracks_writes_time_bucket`: Time taken to write to outgoing RTP tracks.

  - `rtcd_rtc_rtp_tracks_writes_time_sum`

  - `rtcd_rtc_rtp_tracks_writes_time_count`

**WebSocket**

- `rtcd_ws_connections_total`: Total number of active WebSocket connections.
- `rtcd_ws_messages_total`: Total number of received/sent WebSocket messages.

#### Configuration

A sample Prometheus configuration to scrape both plugin and `rtcd` metrics could look like this:

```
scrape_configs:
- job_name: node
  static_configs:
    - targets: ['rtcd-0:9100','rtcd-1:9100', 'calls-offloader-1:9100', 'calls-offloader-2:9100']
- job_name: calls
   metrics_path: /plugins/com.mattermost.calls/metrics
   static_configs:
     - targets: ['app-0:8067','app-1:8067','app-2:8067']
- job_name: rtcd
   static_configs:
     - targets: ['rtcd-0:8045', 'rtcd-1:8045']
```

### System tunings

If you want to host many calls or calls with a large number of participants, take a look at the following platform specific (Linux) tunings (this is the only officially supported target for the plugin right now):

```
# Setting the maximum buffer size of the receiving UDP buffer to 16MB
net.core.rmem_max = 16777216

# Setting the maximum buffer size of the sending UDP buffer to 16MB
net.core.wmem_max = 16777216

# Allow to allocate more memory as needed for more control messages that need to be sent for each socket connected
net.core.optmem_max = 16777216
```

## The rtcd service

```{include} ../../_static/badges/ent-plus.md
```

The Calls plugin has a built-in [Selective Forwarding Unit (SFU)](https://bloggeek.me/webrtcglossary/sfu/) to route audio and screensharing data. This is the `integrated` option described in the [Modes of operation](#modes-of-operation) section above. But this SFU functionality can be deployed separately as an external `rtcd` instance.

### Reasons to use the `rtcd` service

This section will help you understand when and why your organization would want to use `rtcd`.

```{note}
`rtcd` is a standalone service, which adds operational complexity, maintenance costs, and requires an enterprise licence. For those who are evaluating  Calls, and for many small instances of Mattermost, the integrated SFU (the one included in the Calls plugin) may be sufficient initially.
```

The `rtcd` service is the recommended way to host Calls for the following reasons:

- **Performance of the main Mattermost server(s).** When the Calls plugin runs the SFU, calls traffic is added to the processing load of the server running the rest of your Mattermost services. If Calls traffic spikes, it can negatively affect the responsiveness of these services. Using an rtcd service isolates the calls traffic processing to those rtcd instances, and also reduces costs by minimizing CPU usage spikes.

- **Performance, scalability, and stability of the Calls product.** If Calls traffic spikes, or more overall capacity is needed, `rtcd` servers can be added to balance the load. As an added benefit, if the Mattermost traffic spikes, or if a Mattermost instance needs to be restarted, those people in a current call will not be affected - current calls won't be dropped.

Some caveats apply here. Web socket events (for example: emoji reactions, hand raising, muting/unmuting) will not be transmitted while the main Mattermost server is down. But the call itself will continue while the main server restarts.

- **Kubernetes deployments.** In a Kubernetes deployment, `rtcd` is strongly recommended; it is currently the only officially supported way to run Calls.
- **Technical benefits.** The dedicated `rtcd` service has been optimized and tuned at the system/network level for real-time audio/video traffic, where latency is generally more important than throughput.

In general, `rtcd` is the preferred solution for a performant and scalable deployment. With `rtcd`, the Mattermost server will be minimally impacted when hosting a high number of calls.

See the [Mattermost rtcd repository documentation](https://github.com/mattermost/rtcd/blob/master/README.md) on GitHub for details on [how to run calls through the service](https://github.com/mattermost/rtcd/blob/master/docs/getting_started.md), as well as:

- [Key implementation details](https://github.com/mattermost/rtcd/blob/master/docs/implementation.md)
- [Project structure](https://github.com/mattermost/rtcd/blob/master/docs/project_structure.md)
- [Configuration overrides](https://github.com/mattermost/rtcd/blob/master/docs/env_config.md)
- [Authentication flow](https://github.com/mattermost/rtcd/blob/master/docs/security.md)

### Horizontal scalability

```{include} ../../_static/badges/ent-plus.md
```

The supported way to enable horizontal scalability for Calls is through a form of DNS based load balancing. This can be achieved regardless of how the `rtcd` service is deployed (bare bone instance, Kubernetes, or an alternate way).

In order for this to work, the [RTCD Service URL](https://docs.mattermost.com/configure/plugins-configuration-settings.html#rtcd-service-url) should point to a hostname that resolves to multiple IP addresses, each pointing to a running `rtcd` instance. The Mattermost Calls plugin will then automatically distribute calls amongst the available hosts.

The expected requirements are the following:

- When a new `rtcd` instance is deployed, it should be added to the DNS record. The plugin side will then be able to pick it up and start assigning calls to the new host.
- If a `rtcd` instance goes down, it should be removed from the DNS record. The plugin side can then detect the change and stop assigning new calls to that host.

```{note}
- Load balancing is done at the call level. This means that a single call will always live on a single `rtcd` instance.
- There's currently no support for spreading sessions belonging to the same call across a fleet of instances.
```

## Configure recording, transcriptions, and live captions

```{include} ../../_static/badges/ent-plus.md
```

Before you can start recording, transcribing, and live captioning calls, you need to configure the `calls-offloader` job service. See the [calls-offloader](https://github.com/mattermost/calls-offloader/blob/master/docs/getting_started.md) documentation on GitHub for details on deploying and running this service. [Performance and scalability recommendations](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md) related to this service are also available on GitHub.

```{note}
If deploying the service in a Kubernetes cluster, refer to the later section on [Helm charts](#helm-charts).
```

Once the `calls-offloader` service is running, recordings should be explicitly enabled through the [Enable call recordings](https://docs.mattermost.com/configure/plugins-configuration-settings.html#enable-call-recordings) config setting and the service's URL should be configured using [Job service URL](https://docs.mattermost.com/configure/plugins-configuration-settings.html#job-service-url).

Call transcriptions can be enabled through the [Enable call transcriptions](https://docs.mattermost.com/configure/plugins-configuration-settings.html#enable-call-transcriptions) configuration setting.

Live captions can be enabled through the [Enable live captions](https://docs.mattermost.com/configure/plugins-configuration-settings.html#enable-live-captions) configuration setting.

```{note}
- The call transcriptions functionality is available starting in Calls version v0.22.0.
- The live captions functionality is available starting in Calls version v0.26.2.
```

## Kubernetes deployments

```{include} ../../_static/badges/ent-plus.md
```

The Calls plugin has been designed to integrate well with Kubernetes to offer improved scalability and control over the deployment.

This is a sample diagram showing how the `rtcd` standalone service can be deployed in a Kubernetes cluster:

![A diagram of calls deployed in a Kubernetes cluster.](/images/calls-deployment-kubernetes.png)

If Mattermost isn't deployed in a Kubernetes cluster, and you want to use this deployment type, see the [Deploy Mattermost on Kubernetes](https://docs.mattermost.com/install/install-kubernetes.html) documentation.

### Helm Charts

The recommended way to deploy Calls related components and services in a Kubernetes deployment is to use the officially provided Helm charts. Related documentation including detailed information on how to deploy these services can be found in our `mattermost-helm` repository:

- [rtcd Helm chart](https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-rtcd)

- [calls-offloader Helm chart](https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-calls-offloader)

### Limitations

Due to the inherent complexities of hosting a WebRTC service, some limitations apply when deploying Calls in a Kubernetes environment.

One key requirement is that each `rtcd` process live in a dedicated Kubernetes node. This is necessary to forward the data correctly while allowing for horizontal scaling. Data should generally not go through a standard ingress but directly to the pod running the `rtcd` process.

The general recommendation is to expose one external IP address per `rtcd` instance (Kubernetes node). This makes it simpler to scale as the application is able to detect its own external address (through STUN) and advertise it to clients to achieve connectivity with minimal configuration.

If, for some reason, exposing multiple IP addresses is not possible in your environment, port mapping (NAT) can be used. In this scenario different ports are used to map the respective `rtcd` nodes behind the single external IP. Example:

```sh
EXT_IP:8443 -> rtcdA:8443
EXT_IP:8444 -> rtcdB:8443
EXT_IP:8445 -> rtcdC:8443
```

This case requires a couple of extra configurations:

- NAT mappings need to be in place for every `rtcd` node. This is usually done at the ingress point (e.g., ELB, NLB, etc).
- The `RTCD_RTC_ICEHOSTPORTOVERRIDE` config should be used to pass a full mapping of node IPs and their respective port.
  - Example: `RTCD_RTC_ICEHOSTPORTOVERRIDE=rtcdA_IP/8443,rtcdB_IP/8444,rtcdC_IP/8445`
- The `RTCD_RTC_ICEHOSTOVERRIDE` should be used to set the external IP address.

```{note}
One option to limit these static mappings is to reduce the size of the local subnet (e.g., to `/29`).
```

## Frequently asked questions

### Is there encryption?

Media (audio/video) is encrypted using security standards as part of WebRTC. It's mainly a combination of DTLS and SRTP. It's not e2e encrypted in the sense that in the current design all media needs to go through Mattermost which acts as a media router and has complete access to it. Media is then encrypted back to the clients so it's secured during transit. In short: only the participant clients and the Mattermost server have access to unencrypted call data.

### Are there any third-party services involved?

The only external service used is a Mattermost official STUN server (`stun.global.calls.mattermost.com`) which is configured as default. This is primarily used to find the public address of the Mattermost instance if none is provided through the [ICE Host Override](https://docs.mattermost.com/configure/plugins-configuration-settings.html#ice-host-override) option. The only information sent to this service is the IP addresses of clients connecting as no other traffic goes through it. It can be removed in cases where the [ICE Host Override](https://docs.mattermost.com/configure/plugins-configuration-settings.html#ice-host-override) setting is provided.

```{note}
In air-gapped deployments, using STUN servers is not necessary since all connections remain within the local network.
```

### Is using UDP a requirement?

Yes, UDP is the recommended protocol to serve real-time media as it allows for the lowest latency between peers. However, there are a couple of possible solutions to cover clients that due to limitations or strict firewalls are unable to use UDP:

- Since plugin version 0.17 and `rtcd` version 0.11 the RTC service will listen for TCP connections in addition to UDP ones. If configured correctly (e.g. using commonly allowed ports such as 80 or 443) it's possible to have clients connect directly through TCP when unable to do it through the preferred UDP channel.

- Run calls through an external TURN server that listens on TCP and relays all media traffic between peers. However, this is a sub-optimal solution that should be avoided if possible as it will introduce extra latency along with added infrastructural cost.

### Do I need a TURN server?

TURN becomes necessary when you expect to have clients that are unable to connect through the configured UDP port. This can happen due to very restrictive firewalls that either block non standard ports even in the outgoing direction or don't allow the use of the UDP protocol altogether (e.g. some corporate firewalls). In such cases TURN is needed to allow connectivity.

We officially support and recommend using [coturn](https://github.com/coturn/coturn) for a stable and performant TURN service implementation.

### How will this work with an existing reverse proxy sitting in front of Mattermost?

Generally clients should connect directly to either Mattermost or, if deployed, the dedicated `rtcd` service through the configured UDP port . However, it's also possible to route the traffic through an existing load balancer as long as this has support for routing the UDP protocol (e.g. nginx). Of course this will require additional configuration and potential changes to how the plugin is run as it won't be possible to load balance the UDP flow across multiple instances like it happens for HTTP.

### Do calls require a dedicated server to work or can they run alongside Mattermost?

The plugin can function in different modes. By default calls are handled completely by the plugin which runs as part of Mattermost. It's also possible to use a dedicated service to offload the computational and bandwidth costs and scale further (Enterprise only).

### Can the traffic between Mattermost and `rtcd`  be kept internal or should it be opened to the public?

When possible, it's recommended to keep communication between the Mattermost cluster and the dedicated `rtcd` service under the same private network as this can greatly simplify deployment and security. There's no requirement to expose `rtcd`'s HTTP API to the public internet.

### Can Calls be rolled out on a per-channel basis?

Yes. Mattermost system admins running self-hosted deployments can enable or disable call functionality per channel. Once [test mode](https://docs.mattermost.com/configure/plugins-configuration-settings.html#test-mode) is enabled for Mattermost Calls:

- Select **Enable calls** for each channel where you want Calls enabled
- Select **Disable calls** for all channels where you want Calls disabled.

Once Calls is enabled for specific channels, users can start making calls in those channels.

```{note}
When [test mode](https://docs.mattermost.com/configure/plugins-configuration-settings.html#test-mode) is disabled for Mattermost Calls, users in any Mattermost channel can make a call.
```

## Troubleshooting

### Connectivity issues

If calls are failing to connect or timing out, it's likely there could be a misconfiguration at either the plugin config or networking level.

For example, the [RTC Server Port (UDP)](https://docs.mattermost.com/configure/plugins-configuration-settings.html#rtc-server-port-udp) or the [RTC Server Port (TCP)](https://docs.mattermost.com/configure/plugins-configuration-settings.html#rtc-server-port-tcp) may not be open or forwarded correctly.

#### Connectivity checks

An easy way to check whether data can go through is to perform some tests using the `netcat` command line tool.

On the host running Calls (could be the Mattermost instance itself or the one running `rtcd` depending on the chosen setup), run the following:

```sh
nc -l -u -p 8443
```

On the client side (i.e., the machine you would normally use to run the Mattermost desktop app or browser), run the following:

```sh
nc -v -u HOST_IP 8443
```

If connection succeeds, you should be able to send and receive text messages by typing and hitting enter on either side.

```{note}
`HOST_IP` should generally be the public (client facing) IP of the Mattermost
(or `rtcd`) instance hosting the calls. When set, it should be the value of the [ICE Host Override](https://docs.mattermost.com/configure/plugins-configuration-settings.html#ice-host-override)
config setting.

`8443` should be changed with the port configured in [RTC Server Port](https://docs.mattermost.com/configure/plugins-configuration-settings.html#rtc-server-port-udp).

The same checks can be performed to test connectivity through the TCP port using the same commands with `-u` flag removed.
```

#### Network packets debugging

A more advanced way to debug networking issues is to use the `tcpdump` command line utility to temporaily monitor network packets flowing in and out of the instance hosting calls.

On the server side, run the following:

```sh
sudo tcpdump -n port 8443
```

This command will output information (i.e. source and destination addresses) for all the network packets being sent or received through port `8443`. This is a good way to check whether data is getting in and out of the instance and can be used to quickly identify network configuration issues.
