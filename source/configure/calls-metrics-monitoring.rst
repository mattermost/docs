Calls Metrics and Monitoring
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This guide provides detailed information on monitoring Mattermost Calls performance and health through metrics and observability tools. Effective monitoring is essential for maintaining optimal call quality and quickly addressing any issues that arise.

- `Metrics overview <#metrics-overview>`__
- `Setting up monitoring <#setting-up-monitoring>`__
- `Key metrics to monitor <#key-metrics-to-monitor>`__
- `Grafana dashboards <#grafana-dashboards>`__
- `Alerting recommendations <#alerting-recommendations>`__
- `Performance baselines <#performance-baselines>`__

Metrics Overview
--------------

Mattermost Calls provides metrics through Prometheus for both the Calls plugin and the RTCD service. These metrics help track:

- Active call sessions and participants
- Media track statistics
- Connection states and errors
- Resource utilization (CPU, memory, network)
- WebSocket connections and events

The metrics are exposed through HTTP endpoints:

- **Calls Plugin**: ``/plugins/com.mattermost.calls/metrics``
- **RTCD Service**: ``/metrics`` (default) or a configured endpoint

Setting Up Monitoring
-------------------

Prerequisites
^^^^^^^^^^^

To monitor Calls metrics, you'll need:

1. **Prometheus**: For collecting and storing metrics
2. **Grafana**: For visualizing metrics (optional but recommended)

Installing Prometheus
^^^^^^^^^^^^^^^^^^

1. **Download and install Prometheus**:

   Visit the [Prometheus download page](https://prometheus.io/download/) for installation instructions.

2. **Configure Prometheus** to scrape metrics from Mattermost and RTCD:

   Example ``prometheus.yml`` configuration:

   .. code-block:: yaml

      scrape_configs:
        - job_name: 'mattermost-calls'
          scrape_interval: 15s
          metrics_path: '/plugins/com.mattermost.calls/metrics'
          static_configs:
            - targets: ['mattermost-server:8065']
              
        - job_name: 'rtcd'
          scrape_interval: 15s
          static_configs:
            - targets: ['rtcd-server:8045']

   .. important::
      **Metrics Configuration Notice**: The Calls dashboard expects targets to be in ``<host>:<port>`` format. Avoid using ``labels`` in your Prometheus configuration for Calls metrics, as this can cause compatibility issues with the dashboard. For example, use ``targets: ['rtcd-server:8045']`` instead of labels-based targeting.

Installing Grafana
^^^^^^^^^^^^^^^

1. **Download and install Grafana**:

   Visit the [Grafana download page](https://grafana.com/grafana/download) for installation instructions.

2. **Configure Grafana** to use Prometheus as a data source:
   
   - Add a new data source in Grafana
   - Select Prometheus as the type
   - Enter the URL of your Prometheus server
   - Test and save the configuration

Enabling Metrics in RTCD
^^^^^^^^^^^^^^^^^^^^^^

Add the following to your RTCD configuration file:

.. code-block:: json

   {
     "metrics": {
       "enableProm": true,
       "promPort": 9090
     }
   }

Key Metrics to Monitor
--------------------

RTCD Metrics
^^^^^^^^^^

Process Metrics
""""""""""""""

These metrics help monitor the health and resource usage of the RTCD process:

- ``rtcd_process_cpu_seconds_total``: Total CPU time spent
- ``rtcd_process_open_fds``: Number of open file descriptors
- ``rtcd_process_max_fds``: Maximum number of file descriptors
- ``rtcd_process_resident_memory_bytes``: Memory usage in bytes
- ``rtcd_process_virtual_memory_bytes``: Virtual memory used

**Interpretation**: 

- High CPU usage (>70%) may indicate the need for additional RTCD instances
- Steadily increasing memory usage might indicate a memory leak
- High number of file descriptors could indicate connection handling issues

WebRTC Connection Metrics
"""""""""""""""""""""""

These metrics track the WebRTC connections and media flow:

- ``rtcd_rtc_conn_states_total{state="X"}``: Count of connections in different states
- ``rtcd_rtc_errors_total{type="X"}``: Count of RTC errors by type
- ``rtcd_rtc_rtp_tracks_total{direction="X"}``: Count of RTP tracks (incoming/outgoing)
- ``rtcd_rtc_sessions_total``: Total number of active RTC sessions

**Interpretation**:

- Increasing error counts may indicate connectivity or configuration issues
- Track by state to see if connections are failing to establish or dropping
- Larger track counts require proportionally more CPU and bandwidth

WebSocket Metrics
"""""""""""""""

These metrics track the signaling channel:

- ``rtcd_ws_connections_total``: Total number of active WebSocket connections
- ``rtcd_ws_messages_total{direction="X"}``: Count of WebSocket messages (sent/received)

**Interpretation**:

- Connection count should match expected participant numbers
- Unusually high message counts might indicate protocol issues
- Connection drops might indicate network issues

Calls Plugin Metrics
^^^^^^^^^^^^^^^^^

Similar metrics are available for the Calls plugin with the following prefixes:

- Process metrics: ``mattermost_plugin_calls_process_*``
- WebRTC connection metrics: ``mattermost_plugin_calls_rtc_*``
- WebSocket metrics: ``mattermost_plugin_calls_websocket_*``
- Store metrics: ``mattermost_plugin_calls_store_ops_total``

Grafana Dashboards
----------------

Official Dashboard
^^^^^^^^^^^^^^^^

Mattermost provides an official Grafana dashboard for monitoring Calls performance:

1. **Download the dashboard JSON**:
   
   Get it from [GitHub](https://github.com/mattermost/mattermost-performance-assets/blob/master/grafana/mattermost-calls-performance-monitoring.json)

2. **Import the dashboard** into Grafana:
   
   - Navigate to Dashboards > Import
   - Upload the JSON file or paste its contents
   - Select your Prometheus data source
   - Confirm the correct rtcd (`5045`) and calls plugin (`8065`) targets are set
   - Click Import

Performance Baselines
------------------

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

+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| Calls | Users/call | Unmuted/call | Screen sharing | CPU (avg) | Memory (avg) | Bandwidth (in/out) | Instance (EC2) |
+=======+============+==============+================+===========+==============+====================+================+
| 100   | 8          | 2            | no             | 60%       | 0.5GB        | 22Mbps / 125Mbps   | c6i.xlarge     |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 100   | 8          | 2            | no             | 30%       | 0.5GB        | 22Mbps / 125Mbps   | c6i.2xlarge    |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 100   | 8          | 2            | yes            | 86%       | 0.7GB        | 280Mbps / 2.2Gbps  | c6i.2xlarge    |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 10    | 50         | 2            | no             | 35%       | 0.3GB        | 5.25Mbps / 86Mbps  | c6i.xlarge     |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 10    | 50         | 2            | no             | 16%       | 0.3GB        | 5.25Mbps / 86Mbps  | c6i.2xlarge    |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 10    | 50         | 2            | yes            | 90%       | 0.3GB        | 32Mbps / 1.33Gbps  | c6i.xlarge     |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 10    | 50         | 2            | yes            | 45%       | 0.3GB        | 32Mbps / 1.33Gbps  | c6i.2xlarge    |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 5     | 200        | 2            | no             | 65%       | 0.6GB        | 8.2Mbps / 180Mbps  | c6i.xlarge     |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 5     | 200        | 2            | no             | 30%       | 0.6GB        | 8.2Mbps / 180Mbps  | c6i.2xlarge    |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+
| 5     | 200        | 2            | yes            | 90%       | 0.7GB        | 31Mbps / 2.2Gbps   | c6i.2xlarge    |
+-------+------------+--------------+----------------+-----------+--------------+--------------------+----------------+

Other Calls Documentation
----------------

- `Calls Overview <calls-deployment.html>`__: Overview of deployment options and architecture
- `RTCD Setup and Configuration <calls-rtcd-setup.html>`__: Comprehensive guide for setting up the dedicated RTCD service
- `Calls Offloader Setup and Configuration <calls-offloader-setup.html>`__: Setup guide for call recording and transcription
- `Calls Deployment on Kubernetes <calls-kubernetes.html>`__: Detailed guide for deploying Calls in Kubernetes environments
- `Calls Troubleshooting <calls-troubleshooting.html>`__: Detailed troubleshooting steps and debugging techniques

Configure Prometheus storage accordingly to balance disk usage with retention needs.