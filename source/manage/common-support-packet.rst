:nosearch:

Use the System Console or the :ref:`mmctl system supportpacket <manage/mmctl-command-line-tool:mmctl system supportpacket>` command to generate a Mattermost Support Packet that includes configuration information, logs, plugin details, and data on external dependencies. Confidential data, such as passwords, are automatically stripped.

Contents of a support packet
----------------------------

A Mattermost Support Packet can contain the following files:

- ``mattermost.log``
- ``plugins.json``
- ``sanitized_config.json``
- ``support_packet.yaml``
- ``cpu.prof``
- ``heap.prof``
- ``goroutines``
- ``warning.txt`` (present when issues are encountered during packet generation)

.. note:: 

   LDAP groups are not included during Support Packet generation. Only ``LDAP Version`` and ``LDAP Vendor`` are included when present. These values are included in the ``support_packet.yaml`` file.

Generate the support packet
---------------------------

.. important::
   
   Before generating a support packet, go to **System Console > Environment > Logging** and ensure **Output logs to file** is set to **true**, and set **File Log Level** to **DEBUG**.

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

Add the generated support packet to a Mattermost Support ticket, or share with with the Mattermost team you're working with.

.. important::

   Disable debug logging once you've generated the support packet. Debug logging can cause log files to expand substantially, and may adversely impact server performance. We recommend enabling it temporarily, or in development environments, but not production enviornments.

Go performance metrics
----------------------

The Support Packet contains 3 go runtime profiling files:

- ``cpu.prof`` contains a 5-second CPU profile
- ``heap.prof`` contains a heap profile
- ``goroutines`` contains a dump of all the running go routines

These files can be read using `pprof <https://golang.google.cn/pkg/cmd/pprof/>`__.

Use ``go tool pprof -web X`` to open a visualization of the profile in your browser, replacing ``X`` with the profile's file name.
