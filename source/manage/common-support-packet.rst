:nosearch:

Use the System Console or the `mmctl system supportpacket </manage/mmctl-command-line-tool.html#mmctl-system-supportpacket>`__ command to generate a Mattermost Support Packet that includes configuration information, logs, plugin details, and data on external dependencies. Confidential data, such as passwords, are automatically stripped.

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

   When present, the following information is santized during packet generation: ``LdapSettings.BindPassword``, ``FileSettings.PublicLinkSalt``, ``FileSettings.AmazonS3SecretAccessKey``, ``EmailSettings.SMTPPassword``, ``GitLabSettings.Secret``, ``GoogleSettings.Secret``, ``Office365Settings.Secret``, ``OpenIdSettings.Secret``, ``SqlSettings.DataSource``, ``SqlSettings.AtRestEncryptKey``, ``ElasticsearchSettings.Password``, ``All SqlSettings.DataSourceReplicas``, ``All SqlSettings.DataSourceSearchReplicas``, ``MessageExportSettings.GlobalRelaySettings.SmtpPassword``, ``ServiceSettings.GfycatApiSecret``, and ``ServiceSettings.SplitKey``. Plugins are not sanitized during packet generation.

.. tab:: Web/Desktop

   1. Go to the System Console, and select **Commercial Support** from the System Console menu. 

      .. image:: ../images/system-console-commercial-support.png
         :alt: Example of available System Console menu options.

   2. Select **Download Support Packet**. A zip file is downloaded to the local machine. You'll be notified if any packet files are unavailable during packet generation. See the ``warning.txt`` file for details.

   3. Sanitize any confidential details in the ``plugin.json`` file before sending the Support Packet to Mattermost Support. When sanitizing Support Packet data, replace details with example strings that contain the same special characters if possible, as special characters are common causes of configuration errors.

   .. note::

      LDAP groups are not included during Support Packet generation. Only ``LDAP Version`` and ``LDAP Vendor`` are included when present. These values are included in the ``support_packet.yaml`` file.

.. tab:: mmctl

   Run the `mmctl system supportpacket </manage/mmctl-command-line-tool.html#mmctl-system-supportpacket>`__ command to generate and download a Support Packet to share with Mattermost Support.

   .. code-block:: none

      go run ./cmd/mmctl system supportpacket
      Downloading Support Packet
      Downloaded Support Packet to mattermost_support_packet_.zip

Go performance metrics
----------------------

The Support Packet contains 3 go runtime profiling files:

- ``cpu.prof`` contains a 5-second CPU profile
- ``heap.prof`` contains a heap profile
- ``goroutines`` contains a dump of all the running go routines

These files can be read using `pprof <https://golang.google.cn/pkg/cmd/pprof/>`__.

Use ``go tool pprof -web X`` to open a visualization of the profile in your browser, replacing ``X`` with the profile's file name.
