Deploy Prometheus and Grafana for performance monitoring
========================================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Performance monitoring support enables admins to track system health for large Enterprise deployments through integrations with `Prometheus <https://prometheus.io/>`_ and `Grafana <https://grafana.org/>`__. These integrations support data collection from several Mattermost servers, which is particularly useful if you're running Mattermost :doc:`in high availability mode </scale/high-availability-cluster>`. Once you're tracking system health, you can :doc:`set up performance alerts </scale/performance-alerting>` on your Grafana dashboard.

Admins can collect and store various data points from the Mattermost application in an `OpenMetrics <https://openmetrics.io>`_ format by `deploying Prometheus <#install-prometheus>`_ and `Grafana <#install-grafana>`_.

.. tip::

   Don't want to deploy Prometheus and Grafana? You can also :doc:`collect performance metrics using the Mattermost Metrics plugin </scale/collect-performance-metrics>`.

Install Prometheus
-------------------

.. important::

   While Prometheus and Grafana may be installed on the same server as Mattermost, we recommend installing these integrations on separate servers, and configure Prometheus to pull all metrics from Mattermost and other connected servers.

1. `Download a precompiled binary for Prometheus <https://prometheus.io/download/>`_. Binaries are provided for many popular distributions, including Darwin, Linux, and Windows. For installation instructions, see the `Prometheus install guides <https://prometheus.io/docs/introduction/getting_started/>`_.

2. The following settings are recommended in the Prometheus configuration file named ``prometheus.yml``:

   .. code:: yaml

      # my global config
      global:
         scrape_interval:     60s # By default, scrape targets every 15 seconds.
         evaluation_interval: 60s # By default, scrape targets every 15 seconds.
         # scrape_timeout is set to the global default (10s).

         # Attach these labels to any time series or alerts when communicating with
         # external systems (federation, remote storage, Alertmanager).
         external_labels:
            monitor: 'mattermost-monitor'

      # Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
      rule_files:
         # - "first.rules"
         # - "second.rules"

      # A scrape configuration containing exactly one endpoint to scrape:
      # Here it's Prometheus itself.
      scrape_configs:
         # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
         - job_name: 'prometheus'

         # Override the global default and scrape targets from this job every five seconds.
         # scrape_interval: 5s

         # metrics_path defaults to '/metrics'
         # scheme defaults to 'http'.

         static_configs:
            - targets: ["<hostname1>:<port>", "<hostname2>:<port>"]

3. Replace the ``<hostname1>:<port>`` parameter with your Mattermost host IP address and port to scrape the data. It connects to ``/metrics`` using HTTP. 

4. In the Mattermost System Console, go to **Environment > Performance Monitoring** to set **Enable Performance Monitoring** to **true**, then specify the **Listen Address** and select **Save**. See our :ref:`Configuration Settings <configure/environment-configuration-settings:performance monitoring>` documentation for details.

   .. image:: ../images/perf_monitoring_system_console.png
      :scale: 70
      :alt: Enable performance monitoring options in the System Console by going to Environment > Performance Monitoring, then specifying a listen address.

5. To test that the server is running, go to ``<ip>:<port>/metrics``.

.. note::
   A Mattermost Enterprise license is required to connect to ``/metrics`` using HTTP.

6. Finally, run ``vi prometheus.yml`` to finish configuring Prometheus. For starting the Prometheus service, read the `comprehensive guides provided by Prometheus <https://prometheus.io/docs/introduction/getting_started/#starting-prometheus>`_.

7. Once the service has started, you can access the data in ``<localhost>:<port>/graph``. While you can use the Prometheus service to create graphs, we'll focus on creating metric and analytics dashboards in Grafana.

.. tip:: 
  For troubleshooting advice, check the `Prometheus FAQ page <https://prometheus.io/docs/introduction/faq/>`_.

Install Grafana
----------------

.. important::

   While Prometheus and Grafana may be installed on the same server as Mattermost, we recommend installing these integrations on separate servers, and configure Prometheus to pull all metrics from Mattermost and other connected servers.

1. `Download a precompiled binary for Grafana <https://grafana.com/docs/grafana/latest/installation/debian/>`_ on Ubuntu or Debian. Binaries are also available for other distributions, including Redhat, Windows and Mac. For install instructions, see `Grafana install guides <https://grafana.com/docs/grafana/latest/installation/debian/>`_

2. The Grafana package is installed as a service, so it is easy to start the server. See their `install guides <https://grafana.com/docs/grafana/latest/installation/debian/>`_ to learn more.

3. The default HTTP port is ``3000`` and default username and password are ``admin``.

4. Add a Mattermost data source with the following settings as defined in the screenshot below

   .. image:: ../images/mattermost_datasource.png
      :alt: Mattermost data source configuration settings for a Grafana installation.

.. tip:: 

  - For troubleshooting advice, check the `Grafana Troubleshooting page <https://grafana.com/docs/grafana/latest/troubleshooting/>`_. 
  - For user guides and tutorials, check the `Grafana documentation to learn more <https://grafana.com/docs/grafana/latest/>`_.

Getting started
---------------

To help you get started, you can download three sample dashboards shared in Grafana:

.. tip::

   See `this Grafana guide <https://grafana.com/docs/grafana/v7.5/dashboards/export-import/>`_ to learn how to import Grafana dashboards either from the UI or from the HTTP API.

- `Mattermost Performance Monitoring v2 <https://grafana.com/grafana/dashboards/15582>`_, which contains detailed charts for performance monitoring including application, cluster, job server, and system metrics.
- `Mattermost Notification Health metrics <https://grafana.com/grafana/dashboards/21305-mattermost-notification-health>`_, which can be used to track different types of notifications sent from Mattermost. Accessing Mattermost Notification Health requires the feature flag ``NotificationMetrics`` to be set to ``true``. System admins can :ref:`disable notification metrics data collection <configure/environment-configuration-settings:enable notification metrics>` through the System Console.
- `Mattermost Web App Performance Metrics <https://grafana.com/grafana/dashboards/21460-web-app-metrics/>`_, which contains detailed metrics for client-side performance, including web vitals and Mattermost-specifc metrics. Accessing Mattermost Web App Performance Metrics requires the feature flag ``ClientMetrics`` to be set to ``true``.
- `Mattermost Collapsed Reply Threads Metrics <https://grafana.com/grafana/dashboards/15581>`_, which contains detailed metrics on the queries involved in our Collapsed Reply Threads feature.
- `Mattermost Performance KPI Metrics <https://grafana.com/grafana/dashboards/2539>`_, which contains key metrics for monitoring performance and system health.
- `Mattermost Performance Monitoring (Bonus Metrics) <https://grafana.com/grafana/dashboards/2545>`_, which contains additional metrics such as emails sent or files uploaded, which may be important to monitor in some deployments.

What's collected?
-----------------

Mattermost provides :ref:`custom metrics <scale/performance-monitoring-metrics:custom Mattermost metrics>` and :ref:`standard Go metrics <scale/performance-monitoring-metrics:standard go metrics>` that can be used to monitor your system's performance.