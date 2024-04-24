Collect performance metrics
============================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |plus-icon| image:: ../images/plus_F0415.svg
  :alt: Open menus using the plus icon.

System admins can collect application metrics from Mattermost that doesn't require you the installation and integration `Prometheus <https://prometheus.io/>`__ with Mattermost.

Collect and store the :doc:`same performance monitoring metrics </scale/performance-monitoring-metrics>` as Prometheus, without having to deploy these third-party tools. Data is collected every minute and is stored in a path you configure. The data is synchronized to either a cloud-based or local file store every hour, and retained for 15 days. 

Download and share the collected data with Mattermost to understand application performance, troubleshoot system stability and performance, as well as inform route cause analysis.

.. tip::

   Already have Prometheus and Grafana deployed? You can :doc:`use these tools to monitor performance of your Mattermost deployment </scale/deploy-prometheus-grafana-for-performance-monitoring>`.

Enable
------

.. note::

  For Mattermost Cloud deployments, no setup is required. See the `usage <#usage>`__ section below for details on collecting performance metrics.

For self-hosted deployments, enable performance metrics in the System Console.

1. Go to **System Console > Plugins > Plugin Management**.
2. Under **Installed Plugins**, scroll to **Mattermost Metrics Plugin**, and select **Enable**.

You can disable performance metrics collection in the System Console by going to **Plugins > Mattermost Metrics Plugin** or to **Plugin Management > Installed Plugins > Mattermost Metrics Plugin**.

Configure
---------

Go to **System Console > Plugins > Plugin Management > Mattermost Metrics Plugin** to manage configuration settings for this plugin.

Upgrade
~~~~~~~~

We recommend upgrading this feature as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost. Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-metrics/releases>`__ for the latest release, available releases, and compatibiilty considerations.

Usage
------

You need to be a Mattermost system admin to collect performance metrics. Select **Create Dump** to generate dump files. 

To use the generated dump file, you can simply clone the `Dockprom <https://github.com/stefanprodan/dockpromo>`__ repository. Change the Prometheus data volume to point to the dump that you just downloaded. The downloaded file is compressed, so to be able to use it, you need to decompress it first.

The volume configuration for Prometheus should look like the code below in the ``docker-compose.yml`` file:

.. code:: yaml

    volumes:
      - ./prometheus:/etc/prometheus
      - /Path/To/Dump/Directory:/prometheus/data

Once you set this up, run ``docker-compose`` as described in `Dockprom Repository <https://github.com/stefanprodan/dockprom?tab=readme-ov-file#install>`__. 

You can also use our `Mattermost Performance Monitoring v2 <https://grafana.com/grafana/dashboards/15582>`__ dashboard by simply importing it into Grafana.

1. Open Grafana (``<localhost>:3000`` by default) and then log into it. 
2. Once you log in, go to the **Plus** |plus-icon| icon on the left sidebar, and then select **Import**. 
3. Enter the dashboard ID (``15582``) in the **Grafana.com Dashboard** field, and then select **Load** to fetch the dashboard. 

What's collected?
-----------------

Mattermost provides :ref:`custom metrics <scale/performance-monitoring-metrics:custom Mattermost metrics>` and :ref:`standard Go metrics <scale/performance-monitoring-metrics:standard go metrics>` that can be used to monitor your system's performance.