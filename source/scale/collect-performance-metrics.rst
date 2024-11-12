Collect performance metrics
============================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

System admins can collect and store the :doc:`same performance monitoring metrics </scale/performance-monitoring-metrics>` as Prometheus, without having to deploy these third-party tools. Data is collected every minute and is stored in a path you configure. The data is synchronized to either a cloud-based or local file store every hour, and retained for 15 days. 

Download and share the collected data with Mattermost to understand application performance, troubleshoot system stability and performance, as well as inform route cause analysis.

.. tip::

   Already have Prometheus and Grafana deployed? You can :doc:`use these tools to monitor performance of your Mattermost deployment </scale/deploy-prometheus-grafana-for-performance-monitoring>`.

Mattermost configuration
------------------------

.. note::

  For Mattermost Cloud deployments, no setup is required. See the `usage <#usage>`__ section below for details on collecting performance metrics.

For a self-hosted Mattermost deployment, a Mattermost system admin must perform the following steps in Mattermost.

1. Log in to your Mattermost :doc:`workspace </guides/use-mattermost>` as a system admin.
2. From Mattermost v10.1, you can install the Metrics plugin from the in-product Mattermost Marketplace by selecting the **Product** |product-list| icon and selecting **App Marketplace**. Search for **Metrics** and select **Install**.
3. Go to **System Console > Plugins > Plugin Management**. In the **Installed Plugins** section, scroll to **Mattermost Metrics Plugin**, and select **Enable Plugin**.
4. Specify the path of the time-series database, and select **Save**.
5. Go to **System Console > Environment > Performance Monitoring**, and set **Enable Performance Monitoring** to **true**. Select **Save**.

.. note::

  For Mattermost deployments prior to v10.1, you must download the latest version of `the plugin binary release <https://github.com/mattermost/mattermost-plugin-metrics/releases>`__, compatible with Mattermost v8.0.1 and later. Go to **System Console > Plugins > Plugin Management > Upload Plugin**, and upload the plugin binary you downloaded.

Upgrade
-------

We recommend upgrading this feature as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost. Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-metrics/releases>`__ for the latest release, available releases, and compatibiilty considerations.

Usage
------

You need to be a Mattermost system admin to collect performance metrics. Select **Create Dump** to generate dump files. 

To use the generated dump file, you can simply clone the `Dockprom <https://github.com/stefanprodan/dockprom>`__ repository. Change the Prometheus data volume to point to the dump that you just downloaded. The downloaded file is compressed, so to be able to use it, you need to decompress it first.

The volume configuration for Prometheus should look like the code below in the ``docker-compose.yml`` file:

.. code-block:: yaml

    volumes:
      - ./prometheus:/etc/prometheus
      - /Path/To/Dump/Directory:/prometheus/data

Once you set this up, run ``docker-compose`` as described in `Dockprom Repository <https://github.com/stefanprodan/dockprom?tab=readme-ov-file#install>`__. 

You can also use our `Mattermost Performance Monitoring v2 <https://grafana.com/grafana/dashboards/15582>`__ dashboard by simply importing it into Grafana.

1. Open Grafana (``<localhost>:3000`` by default) and then log into it. 
2. Once you log in, go to the **Plus** |plus| icon on the left sidebar, and then select **Import**.
3. Enter the dashboard ID (``15582``) in the **Grafana.com Dashboard** field, and then select **Load** to fetch the dashboard. 

What's collected?
-----------------

Mattermost provides :ref:`custom metrics <scale/performance-monitoring-metrics:custom Mattermost metrics>` and :ref:`standard Go metrics <scale/performance-monitoring-metrics:standard go metrics>` that can be used to monitor your system's performance.
