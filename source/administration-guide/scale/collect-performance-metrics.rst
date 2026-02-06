Metrics plugin
==============

The Metrics plugin exposes detailed Mattermost performance and health metrics in Prometheus format, enabling integration with enterprise monitoring, alerting, and observability platforms. This plugin is essential for production deployments requiring real-time visibility into system health and performance.

**Key capabilities:**

- Prometheus-compatible ``/metrics`` endpoint
- Comprehensive system, application, and performance metrics
- Pre-configured Grafana dashboards
- Integration with monitoring platforms (Prometheus, Datadog, New Relic, Splunk)
- Real-time alerting based on thresholds
- Multi-node support for High Availability deployments

**Key metrics exposed:**

- System: CPU, memory, database connections
- Application: Active users, posts/sec, WebSocket connections
- Performance: HTTP request duration, database query performance, cache hit rates
- Business: Team count, channel count, user activity patterns

**Common use cases:**

- Proactive performance monitoring and capacity planning
- Real-time alerting for system issues
- SLA monitoring and reporting
- Troubleshooting performance bottlenecks
- Resource utilization optimization

For complete plugin documentation including setup, configuration, Grafana dashboard installation, and metric reference, see: :doc:`Metrics Plugin Documentation </integrations-guide/plugins/metrics-plugin>`

See also: :doc:`Performance Monitoring Configuration </administration-guide/scale/performance-monitoring-metrics>` for related system monitoring settings.
