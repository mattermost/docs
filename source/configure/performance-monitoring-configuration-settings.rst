:orphan:
:nosearch:

Configure performance monitoring by going to **System Console > Environment > Performance Monitoring**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: perf-enablemonitoring
  :displayname: Enable performance monitoring (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.Enable
  :environment: MM_METRICSSETTINGS_ENABLE
  :description: Enable or disable performance monitoring.

  - **true**: Performance monitoring data collection and profiling is enabled.
  - **false**: **(Default)** Mattermost performance monitoring is disabled.

Enable performance monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| Enable or disable performance monitoring.     | - System Config path: **Environment > Performance Monitoring**      |
|                                               | - ``config.json setting``: ``".MetricsSettings.Enable": false",``   |
| - **true**: Performance monitoring data       | - Environment variable: ``MM_METRICSSETTINGS_ENABLE``               |
|   collection and profiling is enabled.        |                                                                     |
| - **false**: **(Default)** Mattermost         |                                                                     |
|   performance monitoring is disabled.         |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+
| See the :doc:`performance monitoring </scale/performance-monitoring>` documentation                               |
| to learn more.                                                                                                      |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: perf-listenaddress
  :displayname: Listen address for performance (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.ListenAddress
  :environment: MM_METRICSSETTINGS_LISTENADDRESS
  :description: The port the Mattermost server will listen on to expose performance metrics, when enabled. Default is port **8067**.

Listen address for performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------+
| The port the Mattermost server will listen on to expose       | - System Config path: **Environment > Performance Monitoring**          |
| performance metrics, when enabled.                            | - ``config.json setting``: ``".MetricsSettings.ListenAddress": 8067",`` |
|                                                               | - Environment variable: ``MM_METRICSSETTINGS_LISTENADDRESS``            |
| Numerical input. Default is **8067**.                         |                                                                         |
+---------------------------------------------------------------+-------------------------------------------------------------------------+
