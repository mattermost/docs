:orphan:
:nosearch:

Configure SMTP email server settings by going to **System Console > Environment > SMTP**, or by editing the ``config.json`` file as described in the following tables. 

SMTP server
~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The location of the SMTP email server used for email            | - System Config path: **Environment > SMTP**                  |
| notifications.                                                  | - ``config.json setting``: ``".EmailSettings.SMTPServer",``   |
|                                                                 | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVER``       |
+-----------------------------------------------------------------+---------------------------------------------------------------+

SMTP server port
~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The port of SMTP email server.                                  | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPort",``     |
| Numerical input.                                                | - Environment variable: ``MM_EMAILSETTINGS_SMTPPORT``         |
+-----------------------------------------------------------------+---------------------------------------------------------------+

Enable SMTP authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~

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

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The username for authenticating to the SMTP server.             | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPUsername",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPUSERNAME``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

SMTP server password
~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The password associated with the SMTP username.                 | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPassword",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPPASSWORD``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

SMTP connection security
~~~~~~~~~~~~~~~~~~~~~~~~

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

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| Enable or disable security alerts.                              | - System Config path: **Environment > SMTP**                                     |
|                                                                 | - ``config.json setting``: ``".EmailSettings.EnableSecurityFixAlert": true",``   |
| - **true**: **(Default)** System Admins are notified by email   | - Environment variable: ``MM_EMAILSETTINGS_ENABLESECURITYFIXALERT``              |
|   if a relevant security fix alert is announced. Requires email |                                                                                  |
|   to be enabled.                                                |                                                                                  |
| - **false**: Security alerts are disabled.                      |                                                                                  |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| See the `Telemetry </manage/telemetry.html#security-update-check-feature>`__ documentation to learn more.               |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+

SMTP server timeout
~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------+
| The maximum amount of time, in seconds, allowed for             | - System Config path: **Environment > SMTP**                         |
| establishing a TCP connection between Mattermost and the SMTP   | - ``config.json setting``: ``".EmailSettings.SMTPServerTimeout",``   |
| server to be idle before being terminated.                      | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVERTIMEOUT``       |
|                                                                 |                                                                      |
| Numerical value in seconds.                                     |                                                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------+