:orphan:
:nosearch:

User sessions are cleared when a user tries to log in, and sessions are cleared every 24 hours from the sessions database table. Configure session lengths by going to **System Console > Environment > Session Lengths**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

Extend session length with activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

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

Session length for AD/LDAP and email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

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

Session length for mobile
~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Set the number of hours counted from the last time a user      | - System Config path: **Environment > Session Lengths**                           |
| entered their credential into the mobile app to the expiry     | - ``config.json`` setting: ``".ServiceSettings.SessionLengthMobileInHours: 720,`` |
| of the user’s session.                                         | - Environment variable: ``MM_SERVICESETTINGS_SESSONLENGTHMOBILEINHOURS``          |
|                                                                |                                                                                   |
| Numerical input in hours. Default is **720** hours.            |                                                                                   |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Note**: After changing this setting, the new session length takes effect after the next time the user enters their credentials.                  |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------+

Session length for SSO
~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

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

Session cache
~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------+-----------------------------------------------------------------------------+
| Set the number of minutes to cache a session in memory.        | - System Config path: **Environment > Session Lengths**                     |
|                                                                | - ``config.json`` setting: ``".ServiceSettings.SessionCacheInMinutes: 10,`` |
| Numerical input in minutes. Default is **10** minutes.         | - Environment variable: ``MM_SERVICESETTINGS_SESSONCACHEINMINUTES``         |
+----------------------------------------------------------------+-----------------------------------------------------------------------------+

Session idle timeout
~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

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
|   `EMM provider </deploy/deploy-mobile-apps-using-emm-provider.html>`__ to lock the app when not in use.                   |
| - In `high availability mode </scale/high-availability-cluster.html>`__, enable IP hash load balancing for reliable        |
|   timeout measurement.                                                                                                                                |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------+