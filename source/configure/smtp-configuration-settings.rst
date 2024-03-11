:orphan:
:nosearch:

Configure SMTP email server settings by going to **System Console > Environment > SMTP**, or by editing the ``config.json`` file as described in the following tables.

.. config:setting:: smtp-server
  :displayname: SMTP server (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPServer
  :environment: MM_EMAILSETTINGS_SMTPSERVER
  :description: The location of the SMTP email server used for email notifications.

SMTP server
~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The location of the SMTP email server used for email            | - System Config path: **Environment > SMTP**                  |
| notifications.                                                  | - ``config.json setting``: ``".EmailSettings.SMTPServer",``   |
|                                                                 | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVER``       |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-port
  :displayname: SMTP server port (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPPort
  :environment: MM_EMAILSETTINGS_SMTPPORT
  :description: The port of SMTP email server.

SMTP server port
~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The port of SMTP email server.                                  | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPort",``     |
| Numerical input.                                                | - Environment variable: ``MM_EMAILSETTINGS_SMTPPORT``         |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-enableauth
  :displayname: Enable SMTP authentication (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.EnableSMTPAuth
  :environment: MM_EMAILSETTINGS_ENABLESMTPAUTH

  - **true**: SMTP username and password are used for authenticating to the SMTP server.
  - **false**: **(Default)** Mattermost doesn’t attempt to authenticate to the SMTP server.

Enable SMTP authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable SMTP authentication.                          | - System Config path: **Environment > SMTP**                              |
|                                                                 | - ``config.json setting``: ``".EmailSettings.EnableSMTPAuth": false",``   |
| - **true**: SMTP username and password are used for             | - Environment variable: ``MM_EMAILSETTINGS_ENABLESMTPAUTH``               |
|   authenticating to the SMTP server.                            |                                                                           |
| - **false**: **(Default)** Mattermost doesn’t attempt to        |                                                                           |
|   authenticate to the SMTP server.                              |                                                                           |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: smtp-username
  :displayname: SMTP server username (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPUsername
  :environment: MM_EMAILSETTINGS_SMTPUSERNAME
  :description: The username for authenticating to the SMTP server.

SMTP server username
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The username for authenticating to the SMTP server.             | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPUsername",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPUSERNAME``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-password
  :displayname: SMTP server password (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPPassword
  :environment: MM_EMAILSETTINGS_SMTPPASSWORD
  :description: The password associated with the SMTP username.

SMTP server password
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The password associated with the SMTP username.                 | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPassword",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPPASSWORD``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-connectionsecurity
  :displayname: SMTP connection security (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.ConnectionSecurity
  :environment: MM_EMAILSETTINGS_CONNECTIONSECURITY

  - **Not specified**: **(Default)** Send email over an unsecure connection.
  - **TLS**: Communication between Mattermost and your email server is encrypted.
  - **STARTTLS**: Attempts to upgrade an existing insecure connection to a secure connection using TLS.

SMTP connection security
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

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

.. config:setting:: smtp-skipservercertverification
  :displayname: Skip server certificate verification (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SkipServerCertificateVerification
  :environment: MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION

  - **true**: Mattermost won't verify the email server certificate.
  - **false**: **(Default)** Mattermost verifies the email server certificate.

Skip server certificate verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Configure Mattermost to skip the verification of the email server     | - System Config path: **Environment > SMTP**                                                 |
| certificate.                                                          | - ``config.json setting``: ``".EmailSettings.SkipServerCertificateVerification": false",``   |
|                                                                       | - Environment variable: ``MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION``               |
| - **true**: Mattermost won't verify the email server certificate.     |                                                                                              |
| - **false**: **(Default)** Mattermost verifies the email              |                                                                                              |
|   server certificate.                                                 |                                                                                              |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. config:setting:: smtp-enablesecurityalerts
  :displayname: Enable security alerts (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.EnableSecurityFixAlert
  :environment: MM_EMAILSETTINGS_ENABLESECURITYFIXALERT

  - **true**: **(Default)** System Admins are notified by email if a relevant security fix alert is announced. Requires email to be enabled.
  - **false**: Security alerts are disabled.

Enable security alerts
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| Enable or disable security alerts.                              | - System Config path: **Environment > SMTP**                                     |
|                                                                 | - ``config.json setting``: ``".EmailSettings.EnableSecurityFixAlert": true",``   |
| - **true**: **(Default)** System Admins are notified by email   | - Environment variable: ``MM_EMAILSETTINGS_ENABLESECURITYFIXALERT``              |
|   if a relevant security fix alert is announced. Requires email |                                                                                  |
|   to be enabled.                                                |                                                                                  |
| - **false**: Security alerts are disabled.                      |                                                                                  |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| See the :ref:`Telemetry <manage/telemetry:security update check feature>` documentation to learn more.                                             |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: smtp-servertimeout
  :displayname: SMTP server timeout (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPServerTimeout
  :environment: MM_EMAILSETTINGS_SMTPSERVERTIMEOUT
  :description: The maximum amount of time, in seconds, allowed for establishing a TCP connection between Mattermost and the SMTP server.

SMTP server timeout
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------+
| The maximum amount of time, in seconds, allowed for             | - System Config path: **Environment > SMTP**                         |
| establishing a TCP connection between Mattermost and the SMTP   | - ``config.json setting``: ``".EmailSettings.SMTPServerTimeout",``   |
| server.                                                         | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVERTIMEOUT``       |
|                                                                 |                                                                      |
| Numerical value in seconds.                                     |                                                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------+
