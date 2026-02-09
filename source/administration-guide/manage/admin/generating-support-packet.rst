Generate a Support Packet
==========================

.. include:: ../../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

The Support Packet is used to help customers diagnose and troubleshoot issues. Use the System Console or the :ref:`mmctl system supportpacket <administration-guide/manage/mmctl-command-line-tool:mmctl system supportpacket>` command to generate a zip file that includes configuration information, logs, plugin details, and data on external dependencies across all nodes in a high-availability cluster. Confidential data, such as passwords, are automatically stripped.

Generate
---------

.. important::

   - Before generating a Support Packet, go to **System Console > Environment > Logging** and ensure **Output logs to file** is set to **true**, and set **File Log Level** to **DEBUG**
   - From Mattermost v11.4, support packet generation is recorded in the audit log (when :ref:`audit logging is enabled and configured <administration-guide/manage/logging:audit logging>`). The audit event includes the username, timestamp, success/failure status, whether logs were included, plugin packets requested, and the output filename. This audit trail helps track access to potentially sensitive log data for compliance purposes.

.. tab:: Web/Desktop

   1. Go to the System Console, and select **Commercial Support** from the System Console menu. 

      .. image:: ../../../images/system-console-commercial-support.png
         :alt: Example of available System Console menu options.

   2. Select **Download Support Packet**. A zip file is downloaded to the local machine. You'll be notified if any packet files are unavailable during packet generation. See the ``warning.txt`` file for details.

.. tab:: mmctl

   Run the :ref:`mmctl system supportpacket <administration-guide/manage/mmctl-command-line-tool:mmctl system supportpacket>` command to generate and download a Support Packet to share with Mattermost Support.

   .. code-block:: sh

    go run ./cmd/mmctl system supportpacket

   .. code-block:: text

    Downloading Support Packet
    Downloaded Support Packet to mattermost_support_packet_.zip

Santitize confidential data
---------------------------

Please sanitize any confidential data you wish to exclude before sharing the packet with Mattermost. 

When present, the following information is automatically santized during packet generation: ``LdapSettings.BindPassword``, ``FileSettings.PublicLinkSalt``, ``FileSettings.AmazonS3SecretAccessKey``, ``EmailSettings.SMTPPassword``, ``GitLabSettings.Secret``, ``GoogleSettings.Secret``, ``Office365Settings.Secret``, ``OpenIdSettings.Secret``, ``SqlSettings.DataSource``, ``SqlSettings.AtRestEncryptKey``, ``ElasticsearchSettings.Password``, ``All SqlSettings.DataSourceReplicas``, ``All SqlSettings.DataSourceSearchReplicas``, ``MessageExportSettings.GlobalRelaySettings.SmtpPassword``, and ``ServiceSettings.SplitKey``. 

.. important::

   Plugins may not be sanitized during packet generation.

   - From Mattermost v10.1, plugins can mark their configuration as hidden. If a plugin marks its configuration as hidden, the configuration is sanitized during packet generation.
   - Otherwise, ensure you sanitize any additional confidential details in the ``plugin.json`` file before sharing it with Mattermost. Replace details with example strings that contain the same special characters if possible, as special characters are common causes of configuration errors.

Share the packet with Mattermost
--------------------------------

Add the generated Support Packet to a `standard support request <https://support.mattermost.com/hc/en-us/requests/new>`_, or share with with the Mattermost team you're working with.

.. important::

   Disable debug logging once you've generated the Support Packet. Debug logging can cause log files to expand substantially, and may adversely impact server performance. We recommend enabling it temporarily, or in development environments, but not production enviornments.

Contents of a Support Packet
----------------------------

The contents of a Mattermost Support Packet can differ by server version. Select the tab that corresponds to your Mattermost version to see the files included in the Support Packet.

.. tab:: v11.0 and later
   :parse-titles:

   Cluster-wide files
   ~~~~~~~~~~~~~~~~~~

   The following cluster-wide files are located in the root directory of the Support Packet:

   - `metadata.yaml <#metadata>`__
   - ``plugins.json`` (all active and inactive plugins)
   - ``sanitized_config.json`` (sanitized copy of the Mattermost configuration)
   - ``stats.yaml`` (Mattermost usage statistics)
   - ``jobs.yaml`` (last runs of important jobs)
   - ``diagnostics.yaml`` (system and plugin diagnostics)
   - ``permissions.yaml`` (role and scheme information)
   - ``postgres_schema_dump.sql`` (PostgreSQL database schema information including tables, indexes, constraints, and other metadata to assist with database configuration diagnosis)
   - ``warning.txt`` (present when issues are encountered during packet generation)
   - ``tsdb_dump.tar.gz`` (present when the Metrics plugin is installed and the **Performance metrics** option is selected when generating the Support Packet)

   Node-specific files
   ~~~~~~~~~~~~~~~~~~~~~~

   The following node-specific files are located in node subdirectories:

   - ``<node-id>/mattermost.log`` (Mattermost logs for each node)
   - ``<node-id>/audit.log`` (Mattermost audit logs for each node)
   - ``<node-id>/ldap.log`` (AD/LDAP logs for each node)
   - ``<node-id>/notifications.log`` (notifications logs for each node)
   - ``<node-id>/cpu.prof`` (`Go performance metrics <#go-performance-metrics>`__ for each node)
   - ``<node-id>/heap.prof`` (`Go performance metrics <#go-performance-metrics>`__ for each node)
   - ``<node-id>/goroutines`` (`Go performance metrics <#go-performance-metrics>`__ for each node)

   Diagnostics highlights
   ~~~~~~~~~~~~~~~~~~~~~~

   The Support Packet ``diagnostics.yaml`` file includes system and plugin diagnostics to support troubleshooting and configuration validation.

   Plugin diagnostic data
   ~~~~~~~~~~~~~~~~~~~~~~~

   The following additional plugin diagnostic data is available when the plugin is enabled and operational:

   - GitHub: ``/github/diagnostics.yaml``
   - GitLab: ``/com.github.manland.mattermost-plugin-gitlab/diagnostics.yaml``
   - Jira: ``/jira/diagnostics.yaml``
   - Calls: ``/com.mattermost.calls/diagnostics.yaml``
   - Boards: ``/focalboard/diagnostics.yaml``
   - Playbooks: ``/playbooks/diagnostics.yaml``
   - MSCalendar: ``/com.mattermost.mscalendar/diagnostics.yaml``
   - Google Calendar: ``/com.mattermost.gcal/diagnostics.yaml``

.. tab:: v10.11

   From v10.11, Support Packets include PostgreSQL database schema dump information that provides comprehensive metadata to help diagnose database configuration issues, performance problems, collation mismatches, and other database-related issues.

   **Cluster-wide files (root directory):**

   - `metadata.yaml <#metadata>`__
   - ``plugins.json`` (all active and inactive plugins)
   - ``sanitized_config.json`` (sanitized copy of the Mattermost configuration)
   - ``stats.yaml`` (Mattermost usage statistics)
   - ``jobs.yaml`` (last runs of important jobs)
   - ``diagnostics.yaml`` (core plugin diagnostics data)
   - ``permissions.yaml`` (role & scheme information)
   - ``postgres_schema_dump.sql`` (PostgreSQL database schema information including tables, indexes, constraints, and other database metadata to assist with database configuration diagnosis)
   - ``warning.txt`` (present when issues are encountered during packet generation)
   - ``tsdb_dump.tar.gz`` (present when the Metrics plugin is installed and the **Performance metrics** option is selected when generating the Support Packet)

   **Cluster-specific files (in node subdirectories):**

   - ``<node-id>/mattermost.log`` (Mattermost logs for each node)
   - ``<node-id>/audit.log`` (Mattermost audit logs for each node)
   - ``<node-id>/ldap.log`` (AD/LDAP logs for each node)
   - ``<node-id>/notifications.log`` (notifications logs for each node)
   - ``<node-id>/cpu.prof`` (`Go performance metrics <#go-performance-metrics>`__ for each node)
   - ``<node-id>/heap.prof`` (`Go performance metrics <#go-performance-metrics>`__ for each node)
   - ``<node-id>/goroutines`` (`Go performance metrics <#go-performance-metrics>`__ for each node)

   The following additional plugin diagnostic data is included in the generated Support Packet when the plugin is enabled and operational:

   - GitHub: ``/github/diagnostics.yaml``
   - GitLab: ``/com.github.manland.mattermost-plugin-gitlab/diagnostics.yaml``
   - Jira: ``/jira/diagnostics.yaml``
   - Calls: ``/com.mattermost.calls/diagnostics.yaml``
   - Boards: ``/focalboard/diagnostics.yaml``
   - Playbooks: ``/playbooks/diagnostics.yaml``
   - MSCalendar: ``/com.mattermost.mscalendar/diagnostics.yaml``
   - Google Calendar: ``/com.mattermost.gcal/diagnostics.yaml``

.. tab:: v10.10

   From Mattermost v10.10, Support Packets from :doc:`high availability </administration-guide/scale/high-availability-cluster-based-deployment>` deployments organize cluster-specific files (such as log files) in subdirectories named after each cluster node, while cluster-wide files remain in the root directory. 
      
   Support packet file organization has been improved to make it easier to identify cluster-wide versus cluster-specific files:

   - **Cluster-wide files** (identical across all nodes in a :doc:`high-availability cluster </administration-guide/scale/high-availability-cluster-based-deployment>`) remain in the root directory of the support packet.
   - **Cluster-specific files** (unique per node) are now organized in subdirectories named after each cluster node.

   **Cluster-wide files (root directory):**

   - `metadata.yaml <#metadata>`__
   - ``plugins.json`` (all active and inactive plugins)
   - ``sanitized_config.json`` (sanitized copy of the Mattermost configuration)
   - ``stats.yaml`` (Mattermost usage statistics)
   - ``jobs.yaml`` (last runs of important jobs)
   - ``diagnostics.yaml`` (core plugin diagnostics data)
   - ``permissions.yaml`` (role & scheme information)
   - ``warning.txt`` (present when issues are encountered during packet generation)
   - ``tsdb_dump.tar.gz`` (present when the Metrics plugin is installed and the **Performance metrics** option is selected when generating the Support Packet)

   **Cluster-specific files (in node subdirectories):**

   - ``<node-id>/mattermost.log`` (Mattermost logs for each node)
   - ``<node-id>/audit.log`` (Mattermost audit logs for each node)
   - ``<node-id>/ldap.log`` (AD/LDAP logs for each node)
   - ``<node-id>/notifications.log`` (notifications logs for each node)
   - ``<node-id>/cpu.prof`` (`Go performance metrics <#go-performance-metrics>`__ for each node)
   - ``<node-id>/heap.prof`` (`Go performance metrics <#go-performance-metrics>`__ for each node)
   - ``<node-id>/goroutines`` (`Go performance metrics <#go-performance-metrics>`__ for each node)

   The following additional plugin diagnostic data is included in the generated support packet when the plugin is enabled and operational:

   - GitHub: ``/github/diagnostics.yaml``
   - GitLab: ``/com.github.manland.mattermost-plugin-gitlab/diagnostics.yaml``
   - Jira: ``/jira/diagnostics.yaml``
   - Calls: ``/com.mattermost.calls/diagnostics.yaml``
   - Boards: ``/focalboard/diagnostics.yaml``
   - Playbooks: ``/playbooks/diagnostics.yaml``
   - MSCalendar: ``/com.mattermost.mscalendar/diagnostics.yaml``
   - Google Calendar: ``/com.mattermost.gcal/diagnostics.yaml``

.. tab:: v10.5 to v10.9

   Prior to v10.10, each node in the cluster of a high availability deployment has its own ``mattermost.log`` file and advanced logging files included directly in the Support Packet.

   From v10.5, the following Support Packet data has changed:

   - The ``support_packet.yaml`` file has been removed and split into ``diagnostics.yaml`` and ``stats.yaml`` files.
   - All fields in ``diagnostics.yaml`` have been moved into their own objects for improved readability.
   - Field names are normalized.
   - New data includes server statistics, logs, permissions, and extended job list details.
   - Mattermost-supported plugin diagnostic data is included where applicable.

   The contents of a support packet include:

   - `metadata.yaml <#metadata>`__
   - ``mattermost.log`` (Mattermost logs)
   - ``audit.log`` (Mattermost audit logs)
   - ``ldap.log`` (AD/LDAP logs)
   - ``notifications.log`` (notifications logs)
   - ``plugins.json`` (all active and inactive plugins)
   - ``sanitized_config.json`` (sanitized copy of the Mattermost configuration)
   - ``stats.yaml`` (Mattermost usage statistics)
   - ``jobs.yaml`` (last runs of important jobs)
   - ``diagnostics.yaml`` (core plugin diagnostics data)
   - ``permissions.yaml`` (role & scheme information)
   - `Go performance metrics <#go-performance-metrics>`__, including: ``cpu.prof``, ``heap.prof``, and ``goroutines``
   - ``warning.txt`` (present when issues are encountered during packet generation)
   - ``tsdb_dump.tar.gz`` (present when the Metrics plugin is installed and the **Performance metrics** option is selected when generating the Support Packet)

   The following additional plugin diagnostic data is included in the generated support packet when the plugin is enabled and operational:

   - GitHub: ``/github/diagnostics.yaml``
   - GitLab: ``/com.github.manland.mattermost-plugin-gitlab/diagnostics.yaml``
   - Jira: ``/jira/diagnostics.yaml``
   - Calls: ``/com.mattermost.calls/diagnostics.yaml``
   - Boards: ``/focalboard/diagnostics.yaml``
   - Playbooks: ``/playbooks/diagnostics.yaml``
   - MSCalendar: ``/com.mattermost.mscalendar/diagnostics.yaml``
   - Google Calendar: ``/com.mattermost.gcal/diagnostics.yaml``

.. tab:: Prior to v10.5

   From Mattermost v10.4, a new ``diagnostics.yaml`` file includes Mattermost Calls diagostics data, including plugin version, calls and active session counts, as well as average duration and participant counts.

   - `metadata.yaml <#metadata>`__
   - ``mattermost.log``
   - ``plugins.json``
   - ``sanitized_config.json``
   - ``support_packet.yaml``
   - ``diagnostics.yaml`` (core plugin diagnostics data)
   - `Go performance metrics <#go-performance-metrics>`__, including: ``cpu.prof``, ``heap.prof``, and ``goroutines``
   - ``warning.txt`` (present when issues are encountered during packet generation)

.. note:: 

   - LDAP groups are not included during Support Packet generation. Only ``LDAP Version`` and ``LDAP Vendor`` are included when present. These values are included in the ``support_packet.yaml`` file. 
   - From Mattermost v9.11, ``LDAP Vendor`` errors are included in the Support Packet. If fetching the LDAP Vendor name fails, the Support Packet generation includes the error in ``warning.txt``. If no LDAP Vendor name is found, the Support Packet lists them as ``unknown``.

Metadata
---------

From Mattermost v9.11, generated Support Packets include a ``metadata.yaml`` file that contains the following information.

+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| **Field name**        | **Required/Optional** | **Description**                                                                                                   |         **Example**        |
+=======================+=======================+===================================================================================================================+============================+
| version               | Required              | Version of the schema that the current metadata file is compatible with.                                          | 1                          |
|                       |                       | Current version is 1.                                                                                             |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| type                  | Required              | The type of the packet.                                                                                           | mattermost                 |
|                       |                       | Each type of Support Packet can be mapped to a specific component generating the Support Packet.                  |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| generated_at          | Required              | The date and time the packet was created.                                                                         | 1707473288731              |
|                       |                       | Value is in epoch (ms).                                                                                           |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| server_version        | Required              | Version of the server that the Support Packet was generated at.                                                   | 9.1.1                      |
|                       |                       | Semver is expected.                                                                                               |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| server_id             | Required              | Unique identifier of the server.                                                                                  | 9qpiszyjr3g8bxda35abcd1234 |
|                       |                       | Expected to be 26 characters or longer.                                                                           |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| license_id            | Optional              | Unique identifier of the current server's license.                                                                | abcdejisd67yigqhmkz4ho1234 |
|                       |                       | Expected to be 26 characters or longer.                                                                           |                            |
|                       |                       | This field is empty when there's no license.                                                                      |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| customer_id           | Optional              | The id of the customer, as defined in the license file.                                                           | a1b2c3d4qbbr5cpkbpbmef123h |
|                       |                       | Expected to be 26 characters or longer.                                                                           |                            |
|                       |                       | Empty when there's no license.                                                                                    |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| extras                | Optional              | Key/value of any additional information, specific to the plugin/component that generated the file.                |                            |
|                       |                       | Can be useful for identifying the contents of the data.                                                           |                            |
|                       |                       | Consider adding plugin (or component) versions in order to set expectation regarding the contents of this object. |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| extras.plugin_id      | Required for plugins  | The ID of the plugin.                                                                                             |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| extras.plugin_version | Required for plugins  | The version of the plugin.                                                                                        |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+

For example:

.. code-block:: yaml
  :class: mm-code-block

  version: 1
  type: support-packet
  generated_at: 1622569200
  server_version: 9.1.1
  server_id: 8fqk9rti13fmpxdd5934a3xsxh
  license_id: 3g3pqn8in3brzjkozcn1kdidgr
  customer_id: 74cmws7gf3ykpj31car7zahsny
  extras:
   plugin_version: 0.1.0

Go performance metrics
----------------------

The Support Packet contains 3 go runtime profiling files:

- ``cpu.prof`` contains a 5-second CPU profile
- ``heap.prof`` contains a heap profile
- ``goroutines`` contains a dump of all the running go routines

These files can be read using `pprof <https://golang.google.cn/cmd/pprof/>`_.

Use ``go tool pprof -web X`` to open a visualization of the profile in your browser, replacing ``X`` with the profile's file name.

Load metric
------------

From Mattermost v10.10, the **Load Metric** field under **Product Menu > About Mattermost** displays monthly active users relative to the total number of licensed users. This value gives Mattermost support teams a contextual reference point for understanding deployment active usage for troubleshooting and guidance. It isn’t a comprehensive performance monitoring tool or health indicator, but serves as a supplementary data point when traditional diagnostic methods aren’t available. 