Use the System Console to generate a Mattermost Support Packet that includes configuration information, logs, and data on external dependencies. Confidential data, such as passwords, are automatically stripped. 

.. note:: 

  System Admins should always remove sensitive information before sending the support packet to Mattermost by email or via a support ticket. 

To generate a support packet:

1. Go to System Console, then select **Commercial Support** from the **Main Menu**.
2. Select **Download Support Packet**. A zip file is downloaded to the local machine.

A Mattermost Support Packet contains the following five files:

- ``mattermost.log``
- ``plugins.json``
- sanitized_config.json
- ``support_packet.yaml``
- ``warning.txt``

You are notified if any packet files are unavailable during packet generation. See the ``warning.txt`` file for details.

3. Sanitize configuration and log files in the Support Packet files to remove usernames, passwords, and LDAP groups. Replace these details with example strings that contain the same special characters if possible, as special characters are common causes of configuration errors.
