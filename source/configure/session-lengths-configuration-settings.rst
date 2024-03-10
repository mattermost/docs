:orphan:
:nosearch:

User sessions are cleared when a user tries to log in, and sessions are cleared every 24 hours from the sessions database table. Configure session lengths by going to **System Console > Environment > Session Lengths**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: sessionlength-extendwithactivity
  :displayname: Extend session length with activity (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.ExtendSessionLengthWithActivity
  :environment: MM_SERVICESETTINGS_EXTENDSESSONLENGTHWITHACTIVITY

  - **true**: **(Default)** Sessions are automatically extended when users are active in their Mattermost client.
  - **false**: Sessions won't extend with activity in Mattermost.

Extend session length with activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Improves the user experience by extending sessions and keeping | - System Config path: **Environment > Session Lengths**                                 |
| users logged in if they are active in their Mattermost apps.   | - ``config.json`` setting: ``".ServiceSettings.ExtendSessionLengthWithActivity: true,`` |
|                                                                | - Environment variable: ``MM_SERVICESETTINGS_EXTENDSESSONLENGTHWITHACTIVITY``           |
| - **true**: **(Default)** Sessions are automatically           |                                                                                         |
|   extended when users are active in their Mattermost           |                                                                                         |
|   client. User sessions only expire when users aren’t active   |                                                                                         |
|   in their Mattermost client for the entire duration of the    |                                                                                         |
|   session lengths defined.                                     |                                                                                         |
| - **false**: Sessions won't extend with activity in            |                                                                                         |
|   Mattermost. User sessions immediately expire at the          |                                                                                         |
|   end of the session length or based on the                    |                                                                                         |
|   `session idle timeout <#session-idle-timeout>`__ configured. |                                                                                         |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: sessionlength-webinhours
  :displayname: Session length for AD/LDAP and email (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthWebInHours
  :environment: MM_SERVICESETTINGS_SESSONLENGTHWEBINHOURS

  Set the number of hours counted from the last time a user entered their credentials into the web app or the desktop app to the expiry of the user’s session on email and AD/LDAP authentication.
  Default is **720** hours.

Session length for AD/LDAP and email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------------+
| Set the number of hours counted from the last time a user      | - System Config path: **Environment > Session Lengths**                        |
| entered their credentials into the web app or the desktop      | - ``config.json`` setting: ``".ServiceSettings.SessionLengthWebInHours: 720,`` |
| app to the expiry of the user’s session on email and AD/LDAP   | - Environment variable: ``MM_SERVICESETTINGS_SESSONLENGTHWEBINHOURS``          |
| authentication.                                                |                                                                                |
|                                                                |                                                                                |
| Numerical input in hours. Default is **720** hours.            |                                                                                |
+----------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Note**: After changing this setting, the new session length takes effect after the next time the user enters their credentials.               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: sessionlength-mobileinhours
  :displayname: Session length for mobile (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthMobileInHours
  :environment: MM_SERVICESETTINGS_SESSONLENGTHMOBILEINHOURS
  :description: Set the number of hours counted from the last time a user entered their credential into the mobile app to the expiry of the user’s session. Default is **720** hours.

Session length for mobile
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Set the number of hours counted from the last time a user      | - System Config path: **Environment > Session Lengths**                           |
| entered their credential into the mobile app to the expiry     | - ``config.json`` setting: ``".ServiceSettings.SessionLengthMobileInHours: 720,`` |
| of the user’s session.                                         | - Environment variable: ``MM_SERVICESETTINGS_SESSONLENGTHMOBILEINHOURS``          |
|                                                                |                                                                                   |
| Numerical input in hours. Default is **720** hours.            |                                                                                   |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Note**: After changing this setting, the new session length takes effect after the next time the user enters their credentials.                  |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. config:setting:: sessionlength-ssoinhours
  :displayname: Session length for SSO (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthSSOInHours
  :environment: MM_SERVICESETTINGS_SESSONLENGTHSSOINHOURS
  :description: Set the number of hours from the last time a user entered their SSO credentials to the expiry of the user’s session. Default is **720** hours.

Session length for SSO
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+----------------------------------------------------------------------------------+
| Set the number of hours from the last time a user entered      | - System Config path: **Environment > Session Lengths**                          |
| their SSO credentials to the expiry of the user’s session.     | - ``config.json`` setting: ``".ServiceSettings.SessionLengthSSOInHours: 720,``   |
| This setting defines the session length for SSO                | - Environment variable: ``MM_SERVICESETTINGS_SESSONLENGTHSSOINHOURS``            |
| authentication, such as SAML, GitLab, and OAuth 2.0.           |                                                                                  |
|                                                                |                                                                                  |
| Numerical input in hours. Default is **720** hours.            |                                                                                  |
| Numbers as decimals are also valid values for this             |                                                                                  |
| configuration setting.                                         |                                                                                  |
+----------------------------------------------------------------+----------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                        |
|                                                                                                                                                   |
| - After changing this setting, the new session length takes effect after the next time the user enters their credentials.                         |
| - If the authentication method is SAML, GitLab, or OAuth 2.0, users may automatically be logged back in to Mattermost if they are already logged  |
|   in to SAML, GitLab, or with OAuth 2.0.                                                                                                          |
+----------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: sessionlength-sessioncache
  :displayname: Session cache (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionCacheInMinutes
  :environment: MM_SERVICESETTINGS_SESSONCACHEINMINUTES
  :description: Set the number of minutes to cache a session in memory. Default is **10** minutes.

Session cache
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+-----------------------------------------------------------------------------+
| Set the number of minutes to cache a session in memory.        | - System Config path: **Environment > Session Lengths**                     |
|                                                                | - ``config.json`` setting: ``".ServiceSettings.SessionCacheInMinutes: 10,`` |
| Numerical input in minutes. Default is **10** minutes.         | - Environment variable: ``MM_SERVICESETTINGS_SESSONCACHEINMINUTES``         |
+----------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: sessionlength-sessionidletimeout
  :displayname: Session idle timeout (Session Lengths)
  :systemconsole: N/A
  :configjson: .ServiceSettings.SessionIdleTimeoutInMinutes
  :environment: MM_SERVICESETTINGS_SESSONIDLETIMEOUTINMINUTES

  The number of minutes from the last time a user was active on the system to the expiry of the user’s session. Once expired, the user will need to log in to continue.
  Default is **43200** minutes (30 days). Minimum value is 5 minutes, and a value of 0 sets the time as unlimited.

Session idle timeout
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The number of minutes from the last time a user was active     | - System Config path: N/A                                                            |
| on the system to the expiry of the user’s session.             | - ``config.json`` setting: ``".ServiceSettings.SessionIdleTimeoutInMinutes: 43200,`` |
| Once expired, the user will need to log in to continue.        | - Environment variable: ``MM_SERVICESETTINGS_SESSONIDLETIMEOUTINMINUTES``            |
|                                                                |                                                                                      |
| Numerical input in minutes. Default is **43200** (30 days).    |                                                                                      |
| Minimum value is **5** minutes, and a value of **0** sets      |                                                                                      |
| the time as unlimited.                                         |                                                                                      |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                            |
|                                                                                                                                                       |
| - This setting has no effect when `extend session length with activity <#extend-session-length-with-activity>`__ is set to **true**.                  |
| - This setting applies to the webapp and the desktop app. For mobile apps, use an                                                                     |
|   :doc:`EMM provider </deploy/deploy-mobile-apps-using-emm-provider>` to lock the app when not in use.                                              |
| - In :doc:`high availability mode </scale/high-availability-cluster>`, enable IP hash load balancing for reliable                                   |
|   timeout measurement.                                                                                                                                |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------+
