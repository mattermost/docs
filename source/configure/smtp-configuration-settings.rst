:orphan:

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 25
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 25
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

:nosearch:

View statistics for your overall deployment and specific teams as well as access server logs by going to **System Console > Reporting**. 

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

SMTP server
~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The location of the SMTP email server used for email            | - System Config path: **Environment > SMTP**                  |
| notifications.                                                  | - ``config.json setting``: ``".EmailSettings.SMTPServer",``   |
|                                                                 | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVER``       |
+-----------------------------------------------------------------+---------------------------------------------------------------+

SMTP server port
~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The port of SMTP email server.                                  | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPort",``     |
| Numerical input.                                                | - Environment variable: ``MM_EMAILSETTINGS_SMTPPORT``         |
+-----------------------------------------------------------------+---------------------------------------------------------------+

Enable SMTP authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable SMTP authentication.                          | - System Config path: **Environment > SMTP**                              |
|                                                                 | - ``config.json setting``: ``".EmailSettings.EnableSMTPAuth": false",``   |
| - **true**: SMTP username and password are used for             | - Environment variable: ``MM_EMAILSETTINGS_ENABLESMTPAUTH``               |
|   authenticating to the SMTP server.                            |                                                                           |
| - **false**: **(Default)** Mattermost doesn’t attempt to        |                                                                           |
|   authenticate to the SMTP server.                              |                                                                           |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+

SMTP server username
~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The username for authenticating to the SMTP server.             | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPUsername",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPUSERNAME``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

SMTP server password
~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The password associated with the SMTP username.                 | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPassword",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPPASSWORD``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

SMTP connection security
~~~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| Specify connection security for emails sent using SMTP.         | - System Config path: **Environment > SMTP**                          |
|                                                                 | - ``config.json setting``: ``".EmailSettings.ConnectionSecurity",``   |
| - **Not specified**: **(Default)** Send email over an           | - Environment variable: ``MM_EMAILSETTINGS_CONNECTIONSECURITY``       |
|   unsecure connection.                                          |                                                                       |
| - **TLS**: Communication between Mattermost and your email      |                                                                       |
|   server is encrypted.                                          |                                                                       |
| - **STARTTLS**: Attempts to upgrade an existing insecure        |                                                                       |
|   connection to a secure connection using TLS.                  |                                                                       | 
+-----------------------------------------------------------------+-----------------------------------------------------------------------+

Skip server certificate verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Configure Mattermost to skip the verification of the email server     | - System Config path: **Environment > SMTP**                                                 |
| certificate.                                                          | - ``config.json setting``: ``".EmailSettings.SkipServerCertificateVerification": false",``   | 
|                                                                       | - Environment variable: ``MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION``               |
| - **true**: Mattermost won't verify the email server certificate.     |                                                                                              |
| - **false**: **(Default)** Mattermost verifies the email              |                                                                                              |
|   server certificate.                                                 |                                                                                              |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

Enable security alerts
~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| Enable or disable security alerts.                              | - System Config path: **Environment > SMTP**                                     |
|                                                                 | - ``config.json setting``: ``".EmailSettings.EnableSecurityFixAlert": true",``   |
| - **true**: **(Default)** System Admins are notified by email   | - Environment variable: ``MM_EMAILSETTINGS_ENABLESECURITYFIXALERT``              |
|   if a relevant security fix alert is announced. Requires email |                                                                                  |
|   to be enabled.                                                |                                                                                  |
| - **false**: Security alerts are disabled.                      |                                                                                  |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| See the `Telemetry <https://docs.mattermost.com/manage/telemetry.html#security-update-check-feature>`__ documentation to learn more.               |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+

SMTP server timeout
~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------+
| The maximum amount of time, in seconds, allowed for             | - System Config path: **Environment > SMTP**                         |
| establishing a TCP connection between Mattermost and the SMTP   | - ``config.json setting``: ``".EmailSettings.SMTPServerTimeout",``   |
| server to be idle before being terminated.                      | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVERTIMEOUT``       |
|                                                                 |                                                                      |
| Numerical value in seconds.                                     |                                                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------+