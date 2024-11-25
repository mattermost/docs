Generate a Support Packet
==========================

.. include:: ../_static/badges/ent-pro-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

Use the System Console or the :ref:`mmctl system supportpacket <manage/mmctl-command-line-tool:mmctl system supportpacket>` command to generate a Mattermost Support Packet that includes configuration information, logs, plugin details, and data on external dependencies across all nodes in a high-availability cluster. Confidential data, such as passwords, are automatically stripped.

Contents of a Support Packet
----------------------------

A Mattermost Support Packet can contain the following files:

- `metadata.yaml <#metadata>`__
- ``mattermost.log``
- ``plugins.json``
- ``sanitized_config.json``
- ``support_packet.yaml``
- `Go performance metrics <#go-performance-metrics>`__, including: ``cpu.prof``, ``heap.prof``, and ``goroutines``
- ``warning.txt`` (present when issues are encountered during packet generation)

.. note:: 

   - Each node in the cluster of a :doc:`high availability </scale/high-availability-cluster-based-deployment>` deployment has its own ``mattermost.log`` file.
   - LDAP groups are not included during Support Packet generation. Only ``LDAP Version`` and ``LDAP Vendor`` are included when present. These values are included in the ``support_packet.yaml`` file. 
   - From Mattermost v9.11, ``LDAP Vendor`` errors are included in the Support Packet. If fetching the LDAP Vendor name fails, the Support Packet generation includes the error in ``warning.txt``. If no LDAP Vendor name is found, the Support Packet lists them as ``unknown``.

Generate
---------

.. important::
   
   Before generating a Support Packet, go to **System Console > Environment > Logging** and ensure **Output logs to file** is set to **true**, and set **File Log Level** to **DEBUG**.

.. tab:: Web/Desktop

   1. Go to the System Console, and select **Commercial Support** from the System Console menu. 

      .. image:: ../images/system-console-commercial-support.png
         :alt: Example of available System Console menu options.

   2. Select **Download Support Packet**. A zip file is downloaded to the local machine. You'll be notified if any packet files are unavailable during packet generation. See the ``warning.txt`` file for details.

.. tab:: mmctl

   Run the :ref:`mmctl system supportpacket <manage/mmctl-command-line-tool:mmctl system supportpacket>` command to generate and download a Support Packet to share with Mattermost Support.

   .. code-block:: sh

    go run ./cmd/mmctl system supportpacket

   .. code-block:: text

    Downloading Support Packet
    Downloaded Support Packet to mattermost_support_packet_.zip

Santitize confidential data
---------------------------

When present, the following information is santized during packet generation: ``LdapSettings.BindPassword``, ``FileSettings.PublicLinkSalt``, ``FileSettings.AmazonS3SecretAccessKey``, ``EmailSettings.SMTPPassword``, ``GitLabSettings.Secret``, ``GoogleSettings.Secret``, ``Office365Settings.Secret``, ``OpenIdSettings.Secret``, ``SqlSettings.DataSource``, ``SqlSettings.AtRestEncryptKey``, ``ElasticsearchSettings.Password``, ``All SqlSettings.DataSourceReplicas``, ``All SqlSettings.DataSourceSearchReplicas``, ``MessageExportSettings.GlobalRelaySettings.SmtpPassword``, and ``ServiceSettings.SplitKey``. Plugins are not sanitized during packet generation.

Ensure you sanitize any additional confidential details in the ``plugin.json`` file before sharing it with Mattermost. Replace details with example strings that contain the same special characters if possible, as special characters are common causes of configuration errors.

Share the packet with Mattermost
--------------------------------

Add the generated Support Packet to a `standard support request <https://support.mattermost.com/hc/en-us/requests/new>`_, or share with with the Mattermost team you're working with.

.. important::

   Disable debug logging once you've generated the Support Packet. Debug logging can cause log files to expand substantially, and may adversely impact server performance. We recommend enabling it temporarily, or in development environments, but not production enviornments.

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
|                       |                       | This field is empty when there’s no license.                                                                      |                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------+
| customer_id           | Optional              | The id of the customer, as defined in the license file.                                                           | a1b2c3d4qbbr5cpkbpbmef123h |
|                       |                       | Expected to be 26 characters or longer.                                                                           |                            |
|                       |                       | Empty when there’s no license.                                                                                    |                            |
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