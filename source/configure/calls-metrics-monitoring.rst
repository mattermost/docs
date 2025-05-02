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
            - targets: ['rtcd-server:9090']

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
   - Click Import

3. **Key panels** in the dashboard:

   - Active Calls and Participants
   - RTC Connection States
   - Media Tracks (In/Out)
   - CPU and Memory Usage
   - Network Traffic
   - Error Counts

Custom Dashboard Panels
^^^^^^^^^^^^^^^^^^^^

Consider adding these custom panels to your dashboard:

1. **Error Rate Panel**:

   PromQL query:
   
   .. code-block:: text

      sum(rate(rtcd_rtc_errors_total[5m])) by (type)

2. **Connection Success Rate**:

   PromQL query:
   
   .. code-block:: text

      sum(rtcd_rtc_conn_states_total{state="connected"}) / (sum(rtcd_rtc_conn_states_total{state="connected"}) + sum(rtcd_rtc_conn_states_total{state="failed"}))

3. **Media Track Count by Direction**:

   PromQL query:
   
   .. code-block:: text

      sum(rtcd_rtc_rtp_tracks_total) by (direction)

Alerting Recommendations
---------------------

Setting up alerts helps you respond quickly to potential issues. Here are recommended alert thresholds:

1. **High CPU Usage Alert**:

   PromQL query:
   
   .. code-block:: text

      rate(rtcd_process_cpu_seconds_total[5m]) > 0.8
      
   This alerts when CPU usage exceeds 80% over 5 minutes.

2. **Connection Failure Rate Alert**:

   PromQL query:
   
   .. code-block:: text

      sum(rate(rtcd_rtc_conn_states_total{state="failed"}[5m])) / sum(rate(rtcd_rtc_conn_states_total[5m])) > 0.1
      
   This alerts when more than 10% of connection attempts fail over 5 minutes.

3. **WebSocket Connection Drop Alert**:

   PromQL query:
   
   .. code-block:: text

      rate(rtcd_ws_connections_total{state="closed"}[5m]) > 5
      
   This alerts when more than 5 WebSocket connections are dropping per minute.

4. **Memory Leak Detection**:

   PromQL query:
   
   .. code-block:: text

      rate(rtcd_process_resident_memory_bytes[30m]) > 1024 * 1024 * 10
      
   This alerts when memory usage is increasing by more than 10MB per 30 minutes.

Performance Baselines
------------------

Understanding normal performance patterns helps identify anomalies. Here are baseline expectations based on call volume:

Small Deployment (1-10 concurrent calls)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **CPU Usage**: 5-15% on a modern 4-core server
- **Memory Usage**: 200-500MB
- **Network**: 5-20 Mbps (depending on participant count and unmuted users)

Medium Deployment (10-50 concurrent calls)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **CPU Usage**: 15-40% on a modern 8-core server
- **Memory Usage**: 500MB-1GB
- **Network**: 20-100 Mbps

Large Deployment (50+ concurrent calls)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **CPU Usage**: Consider multiple RTCD instances
- **Memory Usage**: 1-2GB per instance
- **Network**: 100Mbps-1Gbps (with horizontal scaling)

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

Metric Retention Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For historical analysis and trend identification:

- **Short-term metrics**: Keep 15-second resolution data for 2 weeks
- **Medium-term metrics**: Keep 1-minute resolution data for 2 months
- **Long-term metrics**: Keep 5-minute resolution data for 1 year

Configure Prometheus storage accordingly to balance disk usage with retention needs.