Authentication configuration settings
=====================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Mattermost supports up to 4 distinct, concurrent methods of user authentication:

- An OpenID provider
- A SAML provider
- An LDAP instance (e.g., Active Directory, OpenLDAP)
- Email and Password

Review and manage the following authentication configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Authentication**:

- `Signup <#signup>`__
- `Email <#email>`__
- `Password <#password>`__
- `MFA <#mfa>`__
- `AD/LDAP <#ad-ldap>`__
- `SAML 2.0 <#saml-2-0>`__
- `OAuth 2.0 <#oauth-2-0>`__
- `OpenID Connect <#openid-connect>`__
- `Guest Access <#guest-access>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``EnableUserCreation`` value is under ``TeamSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.TeamSettings.EnableUserCreation'``
  - When working with the ``config.json`` file manually, look for an object such as ``TeamSettings``, then within that object, find the key ``EnableUserCreation``.

----

Signup
------

Access the following configuration settings in the System Console by going to **Authentication > Signup**.

.. config:setting:: enable-account-creation
  :displayname: Enable account creation (Signup)
  :systemconsole: Authentication > Signup
  :configjson: .TeamSettings.EnableUserCreation
  :environment: MM_TEAMSETTINGS_ENABLEUSERCREATION

  - **true**: **(Default)** Anyone can sign up for a user account on this server without needing to be invited. Applies to email-based signups only.
  - **false**: The ability to create accounts is disabled. Selecting **Create Account** displays an error. Applies to email, OpenID Connect, and OAuth 2.0 user account authentication.

Enable account creation
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** Anyone can sign up for a user account                 | - System Config path: **Authentication > Signup**                                |
|   on this server without needing to be invited.                                 | - ``config.json`` setting: ``TeamSettings`` > ``EnableUserCreation`` > ``true``  |
|   Applies to email-based signups only.                                          | - Environment variable: ``MM_TEAMSETTINGS_ENABLEUSERCREATION``                   |
| - **false**: The ability to create accounts is disabled.                        |                                                                                  |
|   Selecting **Create Account** displays an error.                               |                                                                                  |
|   Applies to email, OpenID Connect, and OAuth 2.0 user account authentication.  |                                                                                  |
+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::
  - LDAP and SAML users can always create a Mattermost account by logging in using LDAP or SAML user credentials, regardless of whether this configuration setting is enabled.
  - From Mattermost v10.9, email addresses enclosed in angle brackets (e.g., ``<billy@example.com>``) will be rejected. To avoid issues, ensure all user emails comply with the plain address format (e.g., ``billy@example.com``). In addition, we strongly recommend taking proactive steps to audit and update Mattermost user data to align with this product change, as impacted users may face issues accessing Mattermost or managing their user profile. You can update these user emails manually using :ref:`mmctl user email <administration-guide/manage/mmctl-command-line-tool:mmctl user email>`.
  - See the encryption options documentation for details on what :ref:`encryption methods <deployment-guide/encryption-options:saml encryption support>` Mattermost supports for SAML.

.. config:setting:: restrict-account-creation-to-specified-email-domains
  :displayname: Restrict account creation to specified email domains (Signup)
  :systemconsole: Authentication > Signup
  :configjson: .TeamSettings.RestrictCreationToDomains
  :environment: MM_TEAMSETTINGS_RESTRICTCREATIONTODOMAINS

  This setting limits the email address domains that can be used to create a new account or team.
  You **must** set `Require Email Verification <https://docs.mattermost.com/administration-guide/configure/configuration-settings.html#require-email-verification>`__ to ``true`` for the restriction to function.
  This setting only affects email login.

  String input of a comma-separated list of domains, i.e. ``corp.mattermost.com, mattermost.com``

Restrict account creation to specified email domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| This setting limits the email address domains that can be used to create a new account or team.                                                        | - System Config path: **Authentication > Signup**                            |
| You **must** set :ref:`Require Email Verification <administration-guide/configure/authentication-configuration-settings:require email verification>`   | - ``config.json`` setting: ``TeamSettings`` > ``RestrictCreationToDomains``  |
| to ``true`` for the restriction to function. This setting only affects email login.                                                                    | - Environment variable: ``MM_TEAMSETTINGS_RESTRICTCREATIONTODOMAINS``        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-open-server
  :displayname: Enable open server (Signup)
  :systemconsole: Authentication > Signup
  :configjson: .TeamSettings.EnableOpenServer
  :environment: MM_TEAMSETTINGS_ENABLEOPENSERVER

  - **true**: Users can create accounts on the server without an invitation.
  - **false**: **(Default)** Users **must** have an invitation to create an account on the server.

Enable open server
~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Users can create accounts on the server without an invitation.                       | - System Config path: **Authentication > Signup**                        |
| - **false**: **(Default)** Users **must** have an invitation to create an account on the server. | - ``config.json`` setting: ``TeamSettings`` > ``EnableOpenServer``       |
|                                                                                                  | - Environment variable: ``MM_TEAMSETTINGS_ENABLEOPENSERVER``             | 
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: enable-email-invitations
  :displayname: Enable email invitations (Signup)
  :systemconsole: Authentication > Signup
  :configjson: .ServiceSettings.EnableEmailInvitations
  :environment: MM_SERVICESETTINGS_ENABLEEMAILINVITATIONS

  - **true**: Allows users to send email invitations.
  - **false**: **(Default)** Disables email invitations.

Enable email invitations
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------------------------------+
| - **true**: **(Default for Cloud deployments)**        | - System Config path: **Authentication > Signup**                                       |
|   Allows users to send email invitations.              | - ``config.json`` setting: ``ServiceSettings`` > ``EnableEmailInvitations`` > ``false`` |
| - **false**: **(Default for self-hosted deployments)** | - Environment variable: ``MM_SERVICESETTINGS_ENABLEEMAILINVITATIONS``                   |
|   Disables email invitations.                          |                                                                                         |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. note::
  Cloud admins can't modify this configuration setting.

Invalidate pending email invites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| This button invalidates email invitations that have not been accepted (by default, invitations expire after 48 hours). | - System Config path: **Authentication > Signup** |
|                                                                                                                        | - ``config.json`` setting: N/A                    |
| This option has no ``config.json`` setting or environment variable.                                                    | - Environment variable: N/A                       |
+------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+

----

Email
-----

Access the following configuration settings in the System Console by going to **Authentication > Email**.

.. config:setting:: enable-account-creation-with-email
  :displayname: Enable account creation with email (Email)
  :systemconsole: Authentication > Email
  :configjson: .EmailSettings.EnableSignUpWithEmail
  :environment: MM_EMAILSETTINGS_ENABLESIGNUPWITHEMAIL

  - **true**: **(Default)** Allows creation of team and user accounts with email and password.
  - **false**: Disables creation of team and user accounts with email and password. This requires a single sign-on service to create accounts.

Enable account creation with email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: **(Default)** Allows creation of team and user accounts with email and password.  | - System Config path: **Authentication > Email**                         | 
| - **false**: Disables creation of team and user accounts with email and password. Requires    | - ``config.json`` setting: ``EmailSettings`` > ``EnableSignUpWithEmail`` |
|   a single sign-on (SSO) service to create accounts.                                          | - Environment variable: ``MM_EMAILSETTINGS_ENABLESIGNUPWITHEMAIL``       |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::
  Cloud admins can't modify this configuration setting.

.. config:setting:: require-email-verification
  :displayname: Require email verification (Signup)
  :systemconsole: Authentication > Email
  :configjson: .EmailSettings.RequireEmailVerification
  :environment: MM_EMAILSETTINGS_REQUIREEMAILVERIFICATION

  - **true**: Requires email verification for new accounts before allowing the user to sign-in.
  - **false**: **(Default)** Disables email verification. This can be used to speed development by skipping the verification process.

Require email verification
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| - **true**: **(Default for Cloud deployments)**                               | - System Config path: **Authentication > Email**                                        |
|   Requires email verification for new accounts                                | - ``config.json`` setting: ``EmailSettings`` > ``RequireEmailVerification`` > ``false`` |
|   before allowing the user to sign-in.                                        | - Environment variable: ``MM_EMAILSETTINGS_REQUIREEMAILVERIFICATION``                   |
| - **false**: **(Default for self-hosted deployments)**                        |                                                                                         |
|   Disables email verification. can be used to speed development by            |                                                                                         |
|   skipping the verification process.                                          |                                                                                         |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: enable-sign-in-with-email
  :displayname: Enable sign-in with email (Signup)
  :systemconsole: Authentication > Email
  :configjson: .EmailSettings.EnableSignInWithEmail
  :environment: MM_EMAILSETTINGS_ENABLESIGNINWITHEMAIL

  - **true**: **(Default)** Allows users to sign-in with email and password.
  - **false**: Disables authentication with email and password, and removes the option from the login screen. Use this option to limit authentication to single sign-on services.

Enable sign-in with email
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+-------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to sign-in with email and password.  | - System Config path: **Authentication > Email**                        |
| - **false**: Disables authentication with email and password,               | - ``config.json`` setting: ``EmailSettings`` > ``EnableSignInWithEmail``|
|   and removes the option from the login screen. Use this option to limit    | - Environment variable: ``MM_EMAILSETTINGS_ENABLESIGNINWITHEMAIL``      |
|   authentication to single sign-on services.                                |                                                                         |
+-----------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::
  - To provide users with only a single email sign in option on the login page, ensure that the `enable sign-in with username <#enable-sign-in-with-username>`__ configuration setting is set to **false**.
  - From Mattermost v10.9, email addresses enclosed in angle brackets (e.g., ``<billy@example.com>``) will be rejected. To avoid issues, ensure all user emails comply with the plain address format (e.g., ``billy@example.com``). In addition, we strongly recommend taking proactive steps to audit and update Mattermost user data to align with this product change, as impacted users may face issues accessing Mattermost or managing their user profile. You can update these user emails manually using :ref:`mmctl user email <administration-guide/manage/mmctl-command-line-tool:mmctl user email>`.


.. config:setting:: enable-sign-in-with-username
  :displayname: Enable sign-in with username (Signup)
  :systemconsole: Authentication > Email
  :configjson: .EmailSettings.EnableSignInWithUsername
  :environment: MM_EMAILSETTINGS_ENABLESIGNINWITHUSERNAME

  - **true**: **(Default)** Allows authentication with a username and password for accounts created with an email address. This setting does not affect AD/LDAP sign-in.
  - **false**: Disables authenticaton with a username and removes the option from the login screen.

Enable sign-in with username
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Allows authentication with a username and password for         | - System Config path: **Authentication > Email**                            |
|   accounts created with an email address. This setting does not affect AD/LDAP           | - ``config.json`` setting: ``EmailSettings`` > ``EnableSignInWithUsername`` |
|   sign-in.                                                                               | - Environment variable: ``MM_EMAILSETTINGS_ENABLESIGNINWITHUSERNAME``       |
| - **false**: Disables authenticaton with a username and removes the sign in option from. |                                                                             |
|   from the login screen.                                                                 |                                                                             |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. note::
  We highly recommended that email-based authentication is only used in small teams on private networks.

----

Password
--------

Access the following configuration settings in the System Console by going to **Authentication > Password**.

.. note::

  From Mattermost v11.0, password hashing uses PBKDF2 for enhanced security. User passwords are automatically migrated when they log in after upgrading to v11.0 or later. This migration is progressive and happens transparently when users authenticate.

.. config:setting:: minimum-password-length
  :displayname: Minimum password length (Password)
  :systemconsole: Authentication > Password
  :configjson: .PasswordSettings.MinimumLength
  :environment: MM_PASSWORDSETTINGS_MINIMUMLENGTH
  :description: This setting determines the minimum number of characters in passwords. It must be a whole number greater than or equal to 5 and less than or equal to 72. Default is **5**.

Minimum password length
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| This setting determines the minimum number of characters in passwords. It must be a whole number greater than or equal to 5 and less than or equal to 72. | - System Config path: **Authentication > Password**                 |
|                                                                                                                                                           | - ``config.json`` setting: ``PasswordSettings`` > ``MinimumLength`` |
| Numerical input. Default is **5**.                                                                                                                        | - Environment variable: ``MM_PASSWORDSETTINGS_MINIMUMLENGTH``       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: password-requirements
  :displayname: Password requirements - At least one lowercase letter (Password)
  :systemconsole: Authentication > Password
  :configjson: .PasswordSettings.Lowercase
  :environment: MM_PASSWORDSETTINGS_LOWERCASE
  :description: This setting controls password character requirements. When **true**, passwords must contain at least one lowercase letter. Default is **false**.

.. config:setting:: password-uppercase
  :displayname: Password requirements - At least one uppercase letter (Password)
  :systemconsole: Authentication > Password
  :configjson: .PasswordSettings.Uppercase
  :environment: MM_PASSWORDSETTINGS_UPPERCASE
  :description: This setting controls password character requirements. When **true**, passwords must contain at least one uppercase letter. Default is **false**.

.. config:setting:: password-number
  :displayname: Password requirements - At least one number (Password)
  :systemconsole: Authentication > Password
  :configjson: .PasswordSettings.Number
  :environment: MM_PASSWORDSETTINGS_NUMBER
  :description: This setting controls password character requirements. When **true**, passwords must contain at least one number. Default is **false**.

.. config:setting:: password-symbol
  :displayname: Password requirements - At least one symbol (Password)
  :systemconsole: Authentication > Password
  :configjson: .PasswordSettings.Symbol
  :environment: MM_PASSWORDSETTINGS_SYMBOL
  :description: This setting controls password character requirements. When **true**, passwords must contain at least one symbol from ``!"#$%&'()*+,-./:;<=>?@[]^_`|~``. Default is **false**.

Password requirements
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This setting controls password character requirements. By checking the corresponding box, passwords must contain: | - System Config path: **Authentication > Password**                                                                                                                                                                          |
|                                                                                                                   | - ``config.json`` settings: ``PasswordSettings`` > ``Lowercase`` > ``false``, ``PasswordSettings`` > ``Uppercase`` > ``false``, ``PasswordSettings`` > ``Number`` > ``false``, ``PasswordSettings`` > ``Symbol`` > ``false`` |
| - **At least one lowercase letter**                                                                               | - Environment variables: ``MM_PASSWORDSETTINGS_LOWERCASE``, ``MM_PASSWORDSETTINGS_UPPERCASE``, ``MM_PASSWORDSETTINGS_NUMBER``, ``MM_PASSWORDSETTINGS_SYMBOL``                                                                |
| - **At least one uppercase letter**                                                                               |                                                                                                                                                                                                                              |
| - **At least one number**                                                                                         |                                                                                                                                                                                                                              |
| - **At least one symbol** out of these: ``!"#$%&'()*+,-./:;<=>?@[]^_`|~``.                                        |                                                                                                                                                                                                                              |
|                                                                                                                   |                                                                                                                                                                                                                              |
| The error message previewed in the System Console will appear if the user attempts to set an invalid password.    |                                                                                                                                                                                                                              |
|                                                                                                                   |                                                                                                                                                                                                                              |
| The default for all boxes is unchecked. The default for all settings in ``config.json`` is ``false``.             |                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: maximum-login-attempts
  :displayname: Maximum login attempts (Password)
  :systemconsole: Authentication > Password
  :configjson: .ServiceSettings.MaximumLoginAttempts
  :environment: MM_SERVICESETTINGS_MAXIMUMLOGINATTEMPTS
  :description: This setting determines the number of failed sign-in attempts a user can make before being locked out and required to go through a password reset by email. Default is **10**.

Maximum login attempts
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| This setting determines the number of failed sign-in attempts a user can make before being locked out and required to go through a password reset by email. | - System Config path: **Authentication > Password**                                |
|                                                                                                                                                             | - ``config.json`` setting: ``ServiceSettings`` > ``MaximumLoginAttempts`` > ``10`` |
| Numerical input. Default is **10**.                                                                                                                         | - Environment variable: ``MM_SERVICESETTINGS_MAXIMUMLOGINATTEMPTS``                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: enable-forgot-password-link
  :displayname: Enable forgot password link (Password)
  :systemconsole: Authentication > Password
  :configjson: .ServiceSettings.ForgotPasswordLink
  :environment: MM_SERVICESETTINGS_FORGOTPASSWORDLINK
  :description: Show or hide the Forgot Password link on the Mattermost login page.

  - **true**: **(Default)** Displays the Forgot Password link on the Mattermost login page.
  - **false**: Hides the Forgot Password link from the Mattermost login page.

Enable forgot password link
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** Displays the **Forget Password** link on the          | - System Config path: **Authentication > Enable forgot password link**           | 
|   Mattermost login page.                                                        | - ``config.json`` setting: ``LdapSettings`` > ``ForgotPasswordLink`` > ``true``  |
| - **false**: Hides the **Forgot Password** link from the Mattermost login page. | - Environment variable: ``MM_LDAPSETTINGS_FORGOTPASSWORDLINK``                   |
+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::
  You can customize the **Forgot Password** link URL by going to **Site Configuration > Customization > Forgot Password Custom Link**.
  See the :ref:`configuration <administration-guide/configure/site-configuration-settings:forgot password custom link>` documentation for details.

----

MFA
---

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > MFA**.

We recommend deploying Mattermost within your own private network, and using VPN clients for mobile access, so that Mattermost is secured with your existing protocols. If you choose to run Mattermost outside your private network, bypassing your existing security protocols, we recommend adding a multi-factor authentication service specifically for accessing Mattermost.

.. config:setting:: enable-multi-factor-authentication
  :displayname: Enable multi-factor authentication (MFA)
  :systemconsole: Authentication > MFA
  :configjson: .ServiceSettings.EnableMultifactorAuthentication
  :environment: MM_SERVICESETTINGS_ENABLEMULTIFACTORAUTHENTICATION

  - **true**: Users who sign-in with AD/LDAP or an email address have the option to add `multi-factor authentication <https://docs.mattermost.com/administration-guide/onboard/multi-factor-authentication.html>`__ to their accounts.
  - **false**: **(Default)** Disables multi-factor authentication.

Enable multi-factor authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| - **true**: Users who sign-in with AD/LDAP or an email address have the option to add                                  | - System Config path: **Authentication > MFA**                                                   |
|   :doc:`multi-factor authentication </administration-guide/onboard/multi-factor-authentication>` to their accounts.    | - ``config.json`` setting: ``ServiceSettings`` > ``EnableMultifactorAuthentication`` > ``false`` |
| - **false**: **(Default)** Disables multi-factor authentication.                                                       | - Environment variable: ``MM_SERVICESETTINGS_ENABLEMULTIFACTORAUTHENTICATION``                   |
+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. config:setting:: enforce-multi-factor-authentication
  :displayname: Enforce multi-factor authentication (MFA)
  :systemconsole: Authentication > MFA
  :configjson: .ServiceSettings.EnforceMultifactorAuthentication
  :environment: MM_SERVICESETTINGS_ENFORCEMULTIFACTORAUTHENTICATION

  - **true**: Requires `multi-factor authentication (MFA) <https://docs.mattermost.com/administration-guide/onboard/multi-factor-authentication.html>`__ for users who sign-in with AD/LDAP or an email address.
    New users must configure MFA. Logged in users are redirected to the MFA setup page until configuration is complete.
  - **false**: **(Default)** MFA is optional.

Enforce multi-factor authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| - **true**: Requires :doc:`multi-factor authentication (MFA)                                          | - System Config path: **Authentication > MFA**                                                    |
|   </administration-guide/onboard/multi-factor-authentication>`                                        | - ``config.json`` setting: ``ServiceSettings`` > ``EnforceMultifactorAuthentication`` > ``false`` |
|   for users who sign-in with AD/LDAP or an email address.                                             | - Environment variable: ``MM_SERVICESETTINGS_ENFORCEMULTIFACTORAUTHENTICATION``                   |
|   New users must set up MFA. Logged in users are redirected to the MFA                                |                                                                                                   |
|   setup page until configuration is complete.                                                         |                                                                                                   |
| - **false**: **(Default)** MFA is optional.                                                           |                                                                                                   |
+-------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. note::
  If your system has users who authenticate with methods other than AD/LDAP and email, MFA must be enforced with the authentication provider
  outside of Mattermost.

----

AD/LDAP
--------

Access the following configuration settings in the System Console by going to **Authentication > AD/LDAP**. This opens the AD/LDAP setup wizard with step-by-step sections and testing to help configure each setting.

The wizard is organized into the following sections:

- `Connection settings <#connection-settings>`__: Configure server connection details
- `User filters <#user-filters>`__: Set up user identification and filtering
- `Account synchronization <#account-synchronization>`__: Map AD/LDAP attributes to Mattermost user fields
- `Group synchronization <#group-synchronization>`__: Configure group settings and group attributes (if using LDAP groups)
- `Synchronization performance <#synchronization-performance>`__: Adjust synchronization timing and performance settings
- `Synchronization history <#synchronization-history>`__: View synchronization status and manually trigger syncs

.. note::
  Each section includes a **Test** option you can use to verify your configuration incrementally, helping identify and resolve issues early in the setup process.

Connection settings
~~~~~~~~~~~~~~~~~~~

Configure your AD/LDAP server connection and basic authentication settings. Use the **Test Connection** button in this section to verify your server connection before proceeding to other configuration steps.

.. config:setting:: enable-sign-in-with-adldap
  :displayname: Enable sign-in with AD/LDAP (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.Enable
  :environment: MM_LDAPSETTINGS_ENABLE

  - **true**: Allows sign-in with AD/LDAP or Active Directory.
  - **false**: **(Default)** Disables sign-in with Entrai ID.

Enable sign-in with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| - **true**: Allows sign-in with AD/LDAP.                                      | - System Config path: **Authentication > AD/LDAP**                        |
| - **false**: **(Default)** Disables sign-in with AD/LDAP.                     | - ``config.json`` setting: ``LdapSettings`` > ``Enable`` > ``false``      |
|                                                                               | - Environment variable: ``MM_LDAPSETTINGS_ENABLE``                        |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: enable-synchronization-with-adldap
  :displayname: Enable synchronization with AD/LDAP (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.EnableSync
  :environment: MM_LDAPSETTINGS_ENABLESYNC

  - **true**: Mattermost periodically syncs users from AD/LDAP.
  - **false**: **(Default)** Disables AD/LDAP synchronization.

Enable synchronization with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Mattermost periodically syncs users from AD/LDAP. | - System Config path: **Authentication > AD/LDAP**                       |
| - **false**: **(Default)** Disables AD/LDAP synchronization.  | - ``config.json`` setting: ``LdapSettings`` > ``EnableSync`` > ``false`` |
|                                                               | - Environment variable: ``MM_LDAPSETTINGS_ENABLESYNC``                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::
  Synchronization with AD/LDAP settings in the System Console can be used to determine the connectivity and 
  availability of arbitrary hosts. System admins concerned about this can use custom admin roles to limit access to 
  modifying these settings. See the 
  :ref:`delegated granular administration <administration-guide/onboard/delegated-granular-administration:edit privileges of admin roles (advanced)>` 
  documentation for details.

.. config:setting:: login-field-name
  :displayname: Login field name (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.LoginFieldName
  :environment: MM_LDAPSETTINGS_LOGINFIELDNAME
  :description: This setting will display placeholder text in the login field of the sign-in page. This text can remind users to sign-in with their AD/LDAP credentials. Default is ``AD/LDAP Username``.

Login field name
^^^^^^^^^^^^^^^^

+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting will display placeholder text in the login field of the sign-in page. This text can remind users to sign-in with their AD/LDAP credentials. | - System Config path: **Authentication > AD/LDAP**               |
|                                                                                                                                                          | - ``config.json`` setting: ``LdapSettings`` > ``LoginFieldName`` |
| String input. Default is ``AD/LDAP Username``.                                                                                                           | - Environment variable: ``MM_LDAPSETTINGS_LOGINFIELDNAME``       | 
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

 
.. config:setting:: adldap-server
  :displayname: AD/LDAP server (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.LdapServer
  :environment: MM_LDAPSETTINGS_LDAPSERVER
  :description: This is the domain name or IP address of the AD/LDAP server.

AD/LDAP server
^^^^^^^^^^^^^^^

+--------------------------------------------------------------+-----------------------------------------------------------------------+
| This is the domain name or IP address of the AD/LDAP server. | - System Config path: **Authentication > AD/LDAP**                    |
|                                                              | - ``config.json`` setting: ``LdapSettings`` > ``LdapServer``          |
|                                                              | - Environment variable: ``MM_LDAPSETTINGS_LDAPSERVER``                |
|                                                              |                                                                       |
| String input.                                                |                                                                       |
+--------------------------------------------------------------+-----------------------------------------------------------------------+ 

.. note::
  Synchronization with AD/LDAP settings in the System Console can be used to determine the connectivity and
  availability of arbitrary hosts. System admins concerned about this can use custom admin roles to limit access to
  modifying these settings. See the :ref:`delegated granular administration <administration-guide/onboard/delegated-granular-administration:edit privileges of admin roles (advanced)>` documentation for details.

.. config:setting:: adldap-port
  :displayname: AD/LDAP port (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.LdapPort
  :environment: MM_LDAPSETTINGS_LDAPPORT
  :description: This is the port Mattermost uses to connect to the AD/LDAP server. Default is **389**.

AD/LDAP port
^^^^^^^^^^^^

+--------------------------------------------------------------------+----------------------------------------------------------------------+
| This is the port Mattermost uses to connect to the AD/LDAP server. | - System Config path: **Authentication > AD/LDAP**                   |
|                                                                    | - ``config.json`` setting: ``LdapSettings`` > ``LdapPort`` > ``389`` |
|                                                                    | - Environment variable: ``MM_LDAPSETTINGS_LDAPPORT``                 |
|                                                                    |                                                                      |
| Numerical input. Default is **389**.                               |                                                                      |
+--------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: bind-username
  :displayname: Bind username (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.BindUsername
  :environment: MM_LDAPSETTINGS_BINDUSERNAME

  This is the username for the account Mattermost utilizes to perform an AD/LDAP search. This should be an account specific to Mattermost.

  Limit the permissions of the account to read-only access to the portion of the AD/LDAP tree specified in the **Base DN** setting.

  When using Active Directory, **Bind Username** should specify domain in ``"DOMAIN/username"`` format.

Bind username
^^^^^^^^^^^^^

+------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| This is the username for the account Mattermost utilizes to perform an AD/LDAP search. This should be an account specific to Mattermost. | - System Config path: **Authentication > AD/LDAP**             |
|                                                                                                                                          | - ``config.json`` setting: ``LdapSettings`` > ``BindUsername`` |
| Limit the permissions of the account to read-only access to the portion of the AD/LDAP tree specified in the **Base DN** setting.        | - Environment variable: ``MM_LDAPSETTINGS_BINDUSERNAME``       |
|                                                                                                                                          |                                                                |
| When using Active Directory, **Bind Username** should specify domain in ``"DOMAIN/username"`` format.                                    |                                                                |
|                                                                                                                                          |                                                                |
| String input.                                                                                                                            |                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

.. note::
  This field is required. Anonymous bind is not currently supported.

.. config:setting:: bind-password
  :displayname: Bind password (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.BindPassword
  :environment: MM_LDAPSETTINGS_BINDPASSWORD
  :description: This is the password for the username given in the **Bind Username** setting.

Bind password
^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------+----------------------------------------------------------------+
| This is the password for the username given in the **Bind Username** setting. | - System Config path: **Authentication > AD/LDAP**             |
|                                                                               | - ``config.json`` setting: ``LdapSettings`` > ``BindPassword`` |
| String input.                                                                 | - Environment variable: ``MM_LDAPSETTINGS_BINDPASSWORD``       |
+-------------------------------------------------------------------------------+----------------------------------------------------------------+

.. config:setting:: connection-security
  :displayname: Connection security (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.ConnectionSecurity
  :environment: MM_LDAPSETTINGS_CONNECTIONSECURITY

  This setting controls the type of security Mattermost uses to connect to the AD/LDAP server, with these options:

  - **none**: **(Default)** No encryption. With this option, it is **highly recommended** that the connection be secured outside of Mattermost, such as by a stunnel proxy.
  - **TLS**: Encrypts communication with TLS.
  - **STARTTLS**: Attempts to upgrade an existing insecure connection to a secure connection with TLS.

Connection security
^^^^^^^^^^^^^^^^^^^^

+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| This setting controls the type of security Mattermost uses to                | - System Config path: **Authentication > AD/LDAP**                            |
| connect to the AD/LDAP server, with these options:                           | - ``config.json`` setting: ``LdapSettings`` > ``ConnectionSecurity`` > ``""`` |
|                                                                              | - Environment variable: ``MM_LDAPSETTINGS_CONNECTIONSECURITY``                |
| - **None**: **(Default for self-hosted deployments)** No encryption.         |                                                                               |
|   With this option, it is **highly recommended** that the connection be      |                                                                               |
|   secured outside of Mattermost, such as by a stunnel proxy.                 |                                                                               |
|   ``config.json`` option: ``""``                                             |                                                                               |
| - **TLS**: **(Default for Cloud deployments)** Encrypts                      |                                                                               |
|   communication with TLS. ``config.json`` option: ``"TLS"``                  |                                                                               |
| - **STARTTLS**: Attempts to upgrade an existing insecure connection          |                                                                               |
|   to a secure connection with TLS. ``config.json`` option: ``"STARTTLS"``    |                                                                               |
+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: skip-certificate-verification
  :displayname: Skip certificate verification (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.SkipCertificateVerification
  :environment: MM_LDAPSETTINGS_SKIPCERTIFICATEVERIFICATION

  - **true**: Disables the certificate verification step for TLS and STARTTLS connections. Use this option for testing. **Do not use** this option when TLS is required in production.
  - **false**: **(Default)** Enables certification verification.

Skip certificate verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| - **true**: Disables the certificate verification step for TLS and STARTTLS connections. Use this option for testing. **Do not use** this option when TLS is required in production. | - System Config path: **Authentication > AD/LDAP**                                        |
| - **false**: **(Default)** Enables certification verification.                                                                                                                       | - ``config.json`` setting: ``LdapSettings`` > ``SkipCertificateVerification`` > ``false`` |
|                                                                                                                                                                                      | - Environment variable: ``MM_LDAPSETTINGS_SKIPCERTIFICATEVERIFICATION``                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. config:setting:: private-key
  :displayname: Private key (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.PrivateKeyFile
  :environment: MM_LDAPSETTINGS_PRIVATEKEYFILE
  :description: Use this setting to upload the private key file from your LDAP authentication provider, if TLS client certificates are the primary authentication mechanism.

Private key
^^^^^^^^^^^^

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Use this setting to upload the private key file from your LDAP authentication provider, if TLS client certificates are the primary authentication mechanism.| - System Config path: **Authentication > AD/LDAP**               |
|                                                                                                                                                             | - ``config.json`` setting: ``LdapSettings`` > ``PrivateKeyFile`` |
| String input.                                                                                                                                               | - Environment variable: ``MM_LDAPSETTINGS_PRIVATEKEYFILE``       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: public-certificate
  :displayname: Public certificate (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.PublicCertificateFile
  :environment: MM_LDAPSETTINGS_PUBLICCERTIFICATEFILE
  :description: Use this setting to upload the public TLS certificate from your LDAP authentication provider, if TLS client certificates are the primary authentication mechanism.

Public certificate
^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Use this setting to upload the public TLS certificate from your LDAP authentication provider, if TLS client certificates are the primary authentication mechanism. | - System Config path: **Authentication > AD/LDAP**                      |
|                                                                                                                                                                    | - ``config.json`` setting: ``LdapSettings`` > ``PublicCertificateFile`` |
| String input.                                                                                                                                                      | - Environment variable: ``MM_LDAPSETTINGS_PUBLICCERTIFICATEFILE``       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: maximum-login-attempts-ldap
  :displayname: Maximum login attempts (AD/LDAP > Connection Settings)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.MaximumLoginAttempts
  :environment: MM_LDAPSETTINGS_MAXIMUMLOGINATTEMPTS
  :description: This setting determines the number of failed sign-in attempts a user can make before being locked out and required to go through a password reset by email. Default is **10**.

Maximum login attempts
^^^^^^^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| This setting determines the number of failed sign-in attempts a user can make before being locked out and required to go through a password reset by email. | - System Config path: **Authentication > AD/LDAP**                                 |
|                                                                                                                                                             | - ``config.json`` setting: ``LdapSettings`` > ``MaximumLoginAttempts`` > ``10``    |
| You can unlock the account in System Console on the users page. Setting this value lower than your LDAP maximum login attempts ensures that the users       | - Environment variable: ``MM_LDAPSETTINGS_MAXIMUMLOGINATTEMPTS``                   |
| won't be locked out of your LDAP server because of failed login attempts in Mattermost.                                                                     |                                                                                    |
|                                                                                                                                                             |                                                                                    |
| Numerical input. Default is **10**.                                                                                                                         |                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. note::

  - Adjust this value to align with your organization’s authentication policies.
  - If a user's account is locked, you can unlock it manually by going to **System console > User Management > Users**.


User filters
~~~~~~~~~~~~

Define how Mattermost identifies and filters users and groups from your AD/LDAP directory. Use the **Test Filters** button in this section to verify your filters work correctly before proceeding to other configuration steps.

.. config:setting:: base-dn
  :displayname: Base DN (AD/LDAP > User Filters)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.BaseDN
  :environment: MM_LDAPSETTINGS_BASEDN
  :description: This is the **Base Distinguished Name** of the location in the AD/LDAP tree where Mattermost will start searching for users.

Base DN
^^^^^^^^

+------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| This is the **Base Distinguished Name** of the location in the AD/LDAP tree where Mattermost will start searching for users. | - System Config path: **Authentication > AD/LDAP**       |
|                                                                                                                              | - ``config.json`` setting: ``LdapSettings`` > ``BaseDN`` |
| String input.                                                                                                                | - Environment variable: ``MM_LDAPSETTINGS_BASEDN``       |
+------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+

.. config:setting:: user-filter
  :displayname: User filter (AD/LDAP > User Filters)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.UserFilter
  :environment: MM_LDAPSETTINGS_USERFILTER
  :description: This setting accepts a `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__ AD/LDAP filter that is applied when searching for user objects. Only the users selected by the query can access Mattermost.

User filter
^^^^^^^^^^^

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| This setting accepts a `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__ AD/LDAP filter that is applied when searching for user objects. Only the users selected by the query can access Mattermost. For example, to filter out disabled users, the filter is: ``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``.              | - System Config path: **Authentication > AD/LDAP**           |
|                                                                                                                                                                                                                                                                                                                                                                                                         | - ``config.json`` setting: ``LdapSettings`` > ``UserFilter`` |
| To filter by group membership, determine the ``distinguishedName`` of the group, then use group membership general syntax to format the filter. For example, if the security group ``distinguishedName`` is ``CN=group1,OU=groups,DC=example,DC=com``, then the filter is: ``(memberOf=CN=group1,OU=groups,DC=example,DC=com)``. The user must explicitly belong to this group for the filter to apply. | - Environment variable: ``MM_LDAPSETTINGS_USERFILTER``       |
|                                                                                                                                                                                                                                                                                                                                                                                                         |                                                              |
| String input.                                                                                                                                                                                                                                                                                                                                                                                           |                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. note::
  This filter uses the permissions of the **Bind Username** account to execute the search. This account should be specific to Mattermost and have read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field.

.. config:setting:: group-filter
  :displayname: Group filter (AD/LDAP > User Filters)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.GroupFilter
  :environment: MM_LDAPSETTINGS_GROUPFILTER
  :description: This setting accepts a `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__ AD/LDAP filter that is applied when searching for group objects. Only the groups selected by the query can access Mattermost.

Group filter
^^^^^^^^^^^^

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This setting accepts a `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__ AD/LDAP filter that is applied when searching for group objects. Only the groups selected by the query can access Mattermost.| - System Config path: **Authentication > AD/LDAP**            |
|                                                                                                                                                                                                                                                  | - ``config.json`` setting: ``LdapSettings`` > ``GroupFilter`` |
| String input. Default is ``(|(objectClass=group)(objectClass=groupOfNames)(objectClass=groupOfUniqueNames))``.                                                                                                                                   | - Environment variable: ``MM_LDAPSETTINGS_GROUPFILTER``       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. note::
  This filter is only used when AD/LDAP Group Sync is enabled. See :doc:`AD/LDAP Group Sync </administration-guide/onboard/ad-ldap-groups-synchronization>` for more information.

.. config:setting:: enable-admin-filter
  :displayname: Enable admin filter (AD/LDAP > User Filters)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.EnableAdminFilter
  :environment: MM_LDAPSETTINGS_ENABLEADMINFILTER

  - **true**: Enables the **Admin Filter** setting that designates system admins using an AD/LDAP filter.
  - **false**: **(Default)** Disables the **Admin Filter** setting.

Enable admin filter
^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **true**: Enables the **Admin Filter** setting that designates system admins using an AD/LDAP filter.                                                                                                                     | - System Config path: **Authentication > AD/LDAP**                              |
| - **false**: **(Default)** Disables the **Admin Filter** setting.                                                                                                                                                           | - ``config.json`` setting: ``LdapSettings`` > ``EnableAdminFilter`` > ``false`` |
|                                                                                                                                                                                                                             | - Environment variable: ``MM_LDAPSETTINGS_ENABLEADMINFILTER``                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. note::
  If this setting is ``false``, no additional users are designated as system admins by the filter. Users that were previously designated as system admins retain this role unless the filter is changed or removed.

.. config:setting:: admin-filter
  :displayname: Admin filter (AD/LDAP > User Filters)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.AdminFilter
  :environment: MM_LDAPSETTINGS_ADMINFILTER
  :description: This setting accepts an AD/LDAP filter that designates the selected users as system admins. Users are promoted to this role on their next sign-in or on the next scheduled AD/LDAP sync.

Admin filter
^^^^^^^^^^^^^

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This setting accepts an AD/LDAP filter that designates the selected users as system admins. Users are promoted to this role on their next sign-in or on the next scheduled AD/LDAP sync. | - System Config path: **Authentication > AD/LDAP**            |
|                                                                                                                                                                                          | - ``config.json`` setting: ``LdapSettings`` > ``AdminFilter`` |
| If the Admin Filter is removed, users who are currently logged in retain their Admin role until their next sign-in.                                                                      | - Environment variable: ``MM_LDAPSETTINGS_ADMINFILTER``       |
|                                                                                                                                                                                          |                                                               |
| String input.                                                                                                                                                                            |                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: guest-filter
  :displayname: Guest filter (AD/LDAP > User Filters)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.GuestFilter
  :environment: MM_LDAPSETTINGS_GUESTFILTER
  :description: This setting accepts an AD/LDAP filter to apply when searching for external users with Guest Access to Mattermost. Only users selected by the query can access Mattermost as Guests.

Guest filter
^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This setting accepts an AD/LDAP filter to apply when searching for external users with Guest Access to Mattermost. Only users selected by the query can access Mattermost as Guests. | - System Config path: **Authentication > AD/LDAP**            |
|                                                                                                                                                                                      | - ``config.json`` setting: ``LdapSettings`` > ``GuestFilter`` |
| See :doc:`Guest Accounts </administration-guide/onboard/guest-accounts>` for more information.                                                                                       | - Environment variable: ``MM_LDAPSETTINGS_GUESTFILTER``       |
|                                                                                                                                                                                      |                                                               |
| String input.                                                                                                                                                                        |                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Account synchronization
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

Map AD/LDAP user attributes to Mattermost user profile fields. Use the **Test Attributes** button in this section to verify correct attribute mapping and data synchronization before proceeding to other configuration steps.

.. config:setting:: id-attribute
  :displayname: ID attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.IdAttribute
  :environment: MM_LDAPSETTINGS_IDATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that is serves as a unique user identifier in Mattermost. The attribute should have a unique value that does not change, such as ``objectGUID`` or ``entryUUID``.

ID attribute
^^^^^^^^^^^^^

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that is serves as a unique user identifier in Mattermost.                                                                                              | - System Config path: **Authentication > AD/LDAP**                                                                               |
|                                                                                                                                                                                                    | - ``config.json`` setting: ``LdapSettings`` > ``IdAttribute``                                                                    |
| The attribute should have a unique value that does not change, such as ``objectGUID`` or ``entryUUID``. Confirm that these attributes are available in your environment before making any changes. | - Environment variable: ``MM_LDAPSETTINGS_IDATTRIBUTE``                                                                          |
|                                                                                                                                                                                                    |                                                                                                                                  |
| String input.                                                                                                                                                                                      |                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. note::
  If a user's ID Attribute changes, a new Mattermost account is created that is not associated with the previous account. If you need to change this field after users have signed-in, use the :ref:`mmctl ldap idmigrate <administration-guide/manage/mmctl-command-line-tool:mmctl ldap idmigrate>` command.

.. config:setting:: login-id-attribute
  :displayname: Login ID attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.LoginIdAttribute
  :environment: MM_LDAPSETTINGS_LOGINIDATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that is used for signing-in to Mattermost. This is normally the same as the **Username Attribute**.

Login ID attribute
^^^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that is used for signing-in to Mattermost. This is normally the same as the **Username Attribute**.                         | - System Config path: **Authentication > AD/LDAP**                 |
|                                                                                                                                                                         | - ``config.json`` setting: ``LdapSettings`` > ``LoginIdAttribute`` |
| If your team uses ``domain\username`` to sign-in to other services with AD/LDAP, you may enter ``domain\username`` in this field to maintain consistency between sites. | - Environment variable: ``MM_LDAPSETTINGS_LOGINIDATTRIBUTE``       |
|                                                                                                                                                                         |                                                                    |
| String input.                                                                                                                                                           |                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: username-attribute
  :displayname: Username attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.UsernameAttribute
  :environment: MM_LDAPSETTINGS_USERNAMEATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that populates the username field in Mattermost. This is normally the same as the **Login ID Attribute**, but it can be mapped to a different attribute.

Username attribute
^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the username field in Mattermost.                                                                                                                                                                       | - System Config path: **Authentication > AD/LDAP**                  |
|                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``LdapSettings`` > ``UsernameAttribute`` |
| This attribute identifies users in the UI. For example, if a Username Attribute is set to ``john.smith``, typing ``@john`` will show ``@john.smith`` as an auto-complete option, and posting a message with ``@john.smith`` will send a notification to that user. | - Environment variable: ``MM_LDAPSETTINGS_USERNAMEATTRIBUTE``       |
|                                                                                                                                                                                                                                                                    |                                                                     |
| This is normally the same as the **Login ID Attribute**, but it can be mapped to a different attribute.                                                                                                                                                            |                                                                     |
|                                                                                                                                                                                                                                                                    |                                                                     |
| String input.                                                                                                                                                                                                                                                      |                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: email-attribute
  :displayname: Email attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.EmailAttribute
  :environment: MM_LDAPSETTINGS_EMAILATTRIBUTE
  :description: This is the attribute in AD/LDAP server that populates the email address field in Mattermost. Email notifications are sent to this address.

Email attribute
^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| This is the attribute in AD/LDAP server that populates the email address field in Mattermost.                                  | - System Config path: **Authentication > AD/LDAP**              |
|                                                                                                                                | - ``config.json`` setting ``LdapSettings`` > ``EmailAttribute`` |
| Email notifications are sent to this address. The address may be seen by other Mattermost users depending on privacy settings. | - Environment variable: ``MM_LDAPSETTINGS_EMAILATTRIBUTE``      |
|                                                                                                                                |                                                                 |
| String input.                                                                                                                  |                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: first-name-attribute
  :displayname: First name attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.FirstNameAttribute
  :environment: MM_LDAPSETTINGS_FIRSTNAMEATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that populates the first name field in Mattermost. When set, users cannot edit their first name.

First name attribute
^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the first name field in Mattermost.                     | - System Config path: **Authentication > AD/LDAP**                   |
|                                                                                                                    | - ``config.json`` setting: ``LdapSettings`` > ``FirstNameAttribute`` |
| When set, users cannot edit their first name.                                                                      | - Environment variable: ``MM_LDAPSETTINGS_FIRSTNAMEATTRIBUTE``       |
|                                                                                                                    |                                                                      |
| When not set, users can edit their first name in their                                                             |                                                                      |
| :doc:`profile settings </end-user-guide/preferences/manage-your-profile>`.                                         |                                                                      |
|                                                                                                                    |                                                                      |
| String input.                                                                                                      |                                                                      |
+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: last-name-attribute
  :displayname: Last name attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.LastNameAttribute
  :environment: MM_LDAPSETTINGS_LASTNAMEATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that populates the last name field in Mattermost. When set, users cannot edit their last name.

Last name attribute
^^^^^^^^^^^^^^^^^^^^

+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the last name field in Mattermost.                             | - System Config path: **Authentication > AD/LDAP**                  |
|                                                                                                                           | - ``config.json`` setting: ``LdapSettings`` > ``LastNameAttribute`` |
| When set, users cannot edit their last name.                                                                              | - Environment variable: ``MM_LDAPSETTINGS_LASTNAMEATTRIBUTE``       |
|                                                                                                                           |                                                                     |
| When not set, users can edit their last name as part of their                                                             |                                                                     |
| :doc:`profile settings </end-user-guide/preferences/manage-your-profile>`. |                                              |                                                                     |
|                                                                                                                           |                                                                     |
| String input.                                                                                                             |                                                                     |
+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: nickname-attribute
  :displayname: Nickname attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.NicknameAttribute
  :environment: MM_LDAPSETTINGS_NICKNAMEATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that populates the nickname field in Mattermost. When set, users cannot edit their nickname.

Nickname attribute
^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the nickname field in Mattermost.                             | - System Config path: **Authentication > AD/LDAP**                  |
|                                                                                                                          | - ``config.json`` setting: ``LdapSettings`` > ``NicknameAttribute`` |
| When set, users cannot edit their nickname.                                                                              | - Environment variable: ``MM_LDAPSETTINGS_NICKNAMEATTRIBUTE``       |
|                                                                                                                          |                                                                     |
| When not set, users can edit their nickname as part of their                                                             |                                                                     |
| :doc:`profile settings </end-user-guide/preferences/manage-your-profile>`.                                               |                                                                     |
|                                                                                                                          |                                                                     |
| String input.                                                                                                            |                                                                     |
+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: position-attribute
  :displayname: Position attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.PositionAttribute
  :environment: MM_LDAPSETTINGS_POSITIONATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that populates the position field in Mattermost. When set, users cannot edit their position.

Position attribute
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the position field in Mattermost.                             | - System Config path: **Authentication > AD/LDAP**                  |
|                                                                                                                          | - ``config.json`` setting: ``LdapSettings`` > ``PositionAttribute`` |
| When set, users cannot edit their position.                                                                              | - Environment variable: ``MM_LDAPSETTINGS_POSITIONATTRIBUTE``       |
|                                                                                                                          |                                                                     |
| When not set, users can edit their position as part of their                                                             |                                                                     |  
| :doc:`profile settings </end-user-guide/preferences/manage-your-profile>`.                                               |                                                                     |
|                                                                                                                          |                                                                     |
| String input.                                                                                                            |                                                                     |
+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: profile-picture-attribute
  :displayname: Profile picture attribute (AD/LDAP > Account Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.PictureAttribute
  :environment: MM_LDAPSETTINGS_PICTUREATTRIBUTE
  :description: This is the attribute in the AD/LDAP server that syncs and locks the profile picture in Mattermost. The image is updated when users sign-in, not when Mattermost syncs with the AD/LDAP server.

Profile picture attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that syncs and locks the profile picture in Mattermost. | - System Config path: **Authentication > AD/LDAP**                 |
|                                                                                                     | - ``config.json`` setting: ``LdapSettings`` > ``PictureAttribute`` |
| The image is updated when users sign-in, not when Mattermost syncs with the AD/LDAP server.         | - Environment variable: ``MM_LDAPSETTINGS_PICTUREATTRIBUTE``       |
|                                                                                                     |                                                                    |
| The image is not updated if the Mattermost image already matches the AD/LDAP image.                 |                                                                    |
|                                                                                                     |                                                                    |
| String input.                                                                                       |                                                                    |
+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Group synchronization
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

Configure group mapping for AD/LDAP group synchronization. Use the **Test Group Attributes** button in this section to verify proper group attribute mapping before proceeding to other configuration steps.

.. config:setting:: group-display-name-attribute
  :displayname: Group display name attribute (AD/LDAP > Group Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.GroupDisplayNameAttribute
  :environment: MM_LDAPSETTINGS_GROUPDISPLAYNAMEATTRIBUTE
  :description: This is the AD/LDAP Group Display name attribute that populates the Mattermost group name field.

Group display name attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| This is the AD/LDAP Group Display name attribute that populates the Mattermost group name field. | - System Config path: **Authentication > AD/LDAP**                                                                                          |
|                                                                                                  | - ``config.json`` setting: ``LdapSettings`` > ``GroupDisplayNameAttribute``                                                                 |
| String input.                                                                                    | - Environment variable: ``MM_LDAPSETTINGS_GROUPDISPLAYNAMEATTRIBUTE``                                                                       |
+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

.. note::
  This attribute is only used when AD/LDAP Group Sync is enabled and it is **required**.  See the :doc:`AD/LDAP Group Sync documentation </administration-guide/onboard/ad-ldap-groups-synchronization>` for more information.

.. config:setting:: group-id-attribute
  :displayname: Group ID attribute (AD/LDAP > Group Synchronization)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.GroupIdAttribute
  :environment: MM_LDAPSETTINGS_GROUPIDATTRIBUTE
  :description: This is an AD/LDAP Group ID attribute that sets a unique identifier for groups. This should be a value that does not change, such as ``entryUUID`` or ``objectGUID``.

Group ID attribute
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| This is an AD/LDAP Group ID attribute that sets a unique identifier for groups.                              | - System Config path: **Authentication > AD/LDAP**                                                                              |
|                                                                                                              | - ``config.json`` setting: ``LdapSettings`` > ``GroupIdAttribute``                                                              |
| This should be a value that does not change, such as ``entryUUID`` or ``objectGUID``.                        | - Environment variable: ``MM_LDAPSETTINGS_GROUPIDATTRIBUTE``                                                                    |
|                                                                                                              |                                                                                                                                 |
| String input.                                                                                                |                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

.. note::
  This attribute is only used when AD/LDAP Group Sync is enabled and it is **required**.  See the :doc:`AD/LDAP Group Sync documentation </administration-guide/onboard/ad-ldap-groups-synchronization>` for more information.

Synchronization performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

Configure timing and performance settings for AD/LDAP synchronization. These settings control how often Mattermost syncs with your AD/LDAP server.

.. config:setting:: synchronization-interval-minutes
  :displayname: Synchronization interval (AD/LDAP > Synchronization Performance)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.SyncIntervalMinutes
  :environment: MM_LDAPSETTINGS_SYNCINTERVALMINUTES
  :description: This value determines how often Mattermost syncs with the AD/LDAP server by setting the number of minutes between each sync. Default is **60**.

Synchronization interval (minutes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| This value determines how often Mattermost syncs with the AD/LDAP server by setting the number of minutes between each sync. | - System Config path: **Authentication > AD/LDAP**                             |
|                                                                                                                              | - ``config.json`` setting: ``LdapSettings`` > ``SyncIntervalMinutes`` > ``60`` |
| Syncing with the AD/LDAP server will update Mattermost accounts to match any changes made to AD/LDAP attributes.             | - Environment variable: ``MM_LDAPSETTINGS_SYNCINTERVALMINUTES``                |
|                                                                                                                              |                                                                                |
| Disabled AD/LDAP accounts become deactivated users in Mattermost, and any active sessions are revoked.                       |                                                                                |
|                                                                                                                              |                                                                                |
| Use the **AD/LDAP Synchronize Now** button to immediately revoke a session after disabling an AD/LDAP account.               |                                                                                |
|                                                                                                                              |                                                                                |
| Numerical input. Default is **60**.                                                                                          |                                                                                |
+------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. note::
  LDAP syncs require a large number of database read queries. Monitor database load and adjust the sync interval to minimize performance degradation.

.. config:setting:: maximum-page-size
  :displayname: Maximum page size (AD/LDAP > Synchronization Performance)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.MaxPageSize
  :environment: MM_LDAPSETTINGS_MAXPAGESIZE
  :description: This setting paginates the results of AD/LDAP server queries. Use this setting if your AD/LDAP server has a page size limit. A page size of **0** disables pagination of results. Default is **0**.

Maximum page size
^^^^^^^^^^^^^^^^^^

+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| This setting paginates the results of AD/LDAP server queries. Use this setting if your AD/LDAP server has a page size limit. | - System Config path: **Authentication > AD/LDAP**                    |
|                                                                                                                              | - ``config.json`` setting: ``LdapSettings`` > ``MaxPageSize`` > ``0`` |
| The recommended setting is **1500**. This is the default AD/LDAP ``MaxPageSize``.                                            | - Environment variable: ``MM_LDAPSETTINGS_MAXPAGESIZE``               |
|                                                                                                                              |                                                                       |
| A page size of **0** disables pagination of results.                                                                         |                                                                       |
|                                                                                                                              |                                                                       |
| Numerical input. Default is **0**.                                                                                           |                                                                       |
+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: query-timeout-seconds
  :displayname: Query timeout (AD/LDAP > Synchronization Performance)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.QueryTimeout
  :environment: MM_LDAPSETTINGS_QUERYTIMEOUT
  :description: This setting determines the timeout period, in seconds, for AD/LDAP queries. Default is **60**.

Query timeout (seconds)
^^^^^^^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| This setting determines the timeout period, in seconds, for AD/LDAP queries. Increase this value to avoid timeout errors when querying a slow server. | - System Config path: **Authentication > AD/LDAP**                      |
|                                                                                                                                                       | - ``config.json`` setting: ``LdapSettings`` > ``QueryTimeout`` > ``60`` |
| Numerical input. Default is **60**.                                                                                                                   | - Environment variable: ``MM_LDAPSETTINGS_QUERYTIMEOUT``                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

Synchronization history
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

View synchronization status and manually trigger AD/LDAP synchronization. This section includes the **AD/LDAP Synchronize Now** button for immediate synchronization.

AD/LDAP synchronize now
^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Use this button to immediately sync with the AD/LDAP server.                                              | - System Config path: **Authentication > AD/LDAP** |
|                                                                                                           | - ``config.json`` setting: N/A                     |
| The status of the sync is displayed in the table underneath the button (see the figure below).            | - Environment variable: N/A                        |
|                                                                                                           |                                                    |
| Following a manual sync, the next sync will occur after the time set in the **Synchronization Interval**. |                                                    |
+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------+

.. note::
  If a sync is ``Pending`` and does not complete, check that **Enable Synchronization with AD/LDAP** is set to ``true``.
  
.. figure:: ../../images/ldap-sync-table.png
  :alt: An example screenshot of an AD/LDAP Synchronization table in the Mattermost System Console.

Config settings not available in the AD/LDAP Wizard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

The following AD/LDAP configuration settings are available in the ``config.json`` file only and aren't available via the AD/LDAP wizard interface in the System Console.

.. config:setting:: re-add-removed-members-on-sync
  :displayname: Re-add removed members on sync (AD/LDAP)
  :systemconsole: Authentication > AD/LDAP
  :configjson: .LdapSettings.ReAddRemovedMembers
  :environment: MM_LDAPSETTINGS_READDREMOVEDMEMBERS
  :description: Enable this setting to re-add members of the LDAP group that were previously removed from group-synchronized teams or channels during LDAP synchronization. Disabled by default.

Re-add removed members on sync
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------------------------------------------------------------+-------------------------------------------------------------------------+
| Enable this setting to re-add members of the LDAP group that were   | - System Config path: **Authentication > AD/LDAP**                      |
| previously removed from group-synchronized teams or channels        | - ``config.json`` setting: ``LdapSettings`` > ``ReAddRemovedMembers``   |
| during LDAP synchronization.                                        | - Environment variable: ``MM_LDAPSETTINGS_READDREMOVEDMEMBERS``         |
|                                                                     |                                                                         |
| - **true**: Members of the LDAP group who were previously removed   |                                                                         |
|   are re-added to group-synchronized teams or channels during LDAP  |                                                                         |
|   synchronization.                                                  |                                                                         |
| - **false**: **(Default)** Members of the LDAP group who were       |                                                                         |
|   previously removed are not re-added to group-synchronized         |                                                                         |
|   teams or channels during LDAP synchronization.                    |                                                                         |
+---------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::

  The :ref:`mmctl ldap sync <administration-guide/manage/mmctl-command-line-tool:mmctl ldap sync>` command takes precedence over this server configuration setting. If you have this setting disabled, and run the mmctl command with the ``--include-removed-members`` flag, removed members will be re-added during LDAP synchronization.

.. _saml-enterprise:

----

SAML 2.0
--------

Access the following configuration settings in the System Console by going to **Authentication > SAML 2.0**.

See the encryption options documentation for details on what :ref:`encryption methods <deployment-guide/encryption-options:saml encryption support>` Mattermost supports for SAML.

.. important::

  In line with Microsoft ADFS guidance, we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

.. config:setting:: enable-login-with-saml
  :displayname: Enable login with SAML (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.Enable
  :environment: MM_SAMLSETTINGS_ENABLE

  - **true**: Enables sign-in with SAML. See `SAML Single Sign-On <https://docs.mattermost.com/administration-guide/onboard/sso-saml.html>`__ to learn more.
  - **false**: **(Default)** Disables sign-in with SAML.

Enable login with SAML
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| - **true**: Enables sign-in with SAML. See :doc:`SAML Single Sign-On </administration-guide/onboard/sso-saml>` to learn more.         | - System Config path: **Authentication > SAML 2.0**                  |
| - **false**: **(Default)** Disables sign-in with SAML.                                                                                | - ``config.json`` setting: ``SamlSettings`` > ``Enable`` > ``false`` |
|                                                                                                                                       | - Environment variable: ``MM_SAMLSETTINGS_ENABLE``                   |
+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: enable-synchronizing-saml-accounts-with-adldap
  :displayname: Enable synchronizing SAML accounts with AD/LDAP (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.EnableSyncWithLdap
  :environment: MM_SAMLSETTINGS_ENABLESYNCWITHLDAP

  - **true**: Mattermost updates configured Mattermost user attributes (ex. FirstName, Position, Email) with their values from AD/LDAP. From Mattermost v10.9, Mattermost checks whether a user exists on the connected LDAP server during login. If the user doesn't exist on the LDAP server, login fails.
  - **false**: **(Default)** Disables syncing of SAML-authenticated Mattermost users with AD/LDAP. From Mattermost v10.9, Mattermost doesn't check whether a user exists on the connected LDAP server during login.

Enable synchronizing SAML accounts with AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: Mattermost updates configured Mattermost user attributes                                         | - System Config path: **Authentication > SAML 2.0**                              |
|   (ex. FirstName, Position, Email) with their values from AD/LDAP.                                           | - ``config.json`` setting: ``SamlSettings`` > ``EnableSyncWithLdap`` > ``false`` |
|   From v10.9, Mattermost checks whether a user exists on the connected LDAP server during login.             | - Environment variable: ``MM_SAMLSETTINGS_ENABLESYNCWITHLDAP``                   |
|   If the user doesn't exist on the LDAP server, login fails.                                                 |                                                                                  |
|                                                                                                              |                                                                                  |
| - **false**: **(Default)** Disables syncing of SAML-authenticated Mattermost users with AD/LDAP.             |                                                                                  |
|   From Mattermost v10.9, Mattermost doesn't check whether a user exists on the connected LDAP server         |                                                                                  |
|   during login.                                                                                              |                                                                                  |
+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::

  - AD/LDAP synchronization must be enabled and configured through the settings under **Authentication > AD/LDAP**.
  - Prior to Mattermost v10.9, users not present on the LDAP server could log in, but would be deactivated on the next LDAP sync.
  - See :doc:`AD/LDAP Setup </administration-guide/onboard/ad-ldap>` to learn more about configuring AD/LDAP.

.. config:setting:: ignore-guest-users-when-synchronizing-with-adldap
  :displayname: Ignore guest users when synchronizing with AD/LDAP (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.IgnoreGuestsLdapSync
  :environment: MM_SAMLSETTINGS_IGNOREGUESTSLDAPSYNC

  - **true**: When syncing with the AD/LDAP server, Mattermost does not sync any information about SAML-authenticated Guest Users from the AD/LDAP server.
  - **false**: **(Default)** Syncing Mattermost with the AD/LDAP server updates Guest User attributes and deactivates and removes SAML-authenticated accounts for Guest Users that are no longer active on the AD/LDAP server.

Ignore guest users when synchronizing with AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - **true**: When syncing with the AD/LDAP server, Mattermost does not                   | - System Config path: **Authentication > SAML 2.0**                                |
|   sync any information about SAML-authenticated Guest Users from the AD/LDAP server.    | - ``config.json`` setting: ``SamlSettings`` > ``IgnoreGuestsLdapSync`` > ``false`` |
|   Manage guest deactivation manually via **System Console > Users**.                    | - Environment variable: ``MM_SAMLSETTINGS_IGNOREGUESTSLDAPSYNC``                   |
| - **false**: **(Default)** Syncing Mattermost with the AD/LDAP server updates Guest     |                                                                                    |
|   User attributes and deactivates and removes SAML-authenticated accounts for           |                                                                                    |
|   Guest Users that are no longer active on the AD/LDAP server.                          |                                                                                    |
+-----------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

For more information, see :doc:`AD/LDAP Setup </administration-guide/onboard/ad-ldap>` for details. 

.. config:setting:: override-saml-bind-data-with-adldap-information
  :displayname: Override SAML bind data with AD/LDAP information (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.EnableSyncWithLdapIncludeAuth
  :environment: MM_SAMLSETTINGS_ENABLESYNCWITHLDAPINCLUDEAUTH

  - **true**: If the SAML ID attribute is configured, Mattermost overrides the SAML ID attribute with the AD/LDAP ID attribute.
  - **false**: **(Default)** Mattermost uses the email attribute to bind users to SAML.

Override SAML bind data with AD/LDAP information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| - **true**: If the SAML ID attribute is configured, Mattermost overrides the SAML ID attribute with the AD/LDAP ID attribute.   | - System Config path: **Authentication > SAML 2.0**                                         |
|   If the SAML ID attribute is not present, Mattermost overrides the SAML Email attribute with the AD/LDAP Email attribute.      | - ``config.json`` setting: ``SamlSettings`` > ``EnableSyncWithLdapIncludeAuth`` > ``false`` |
| - **false**: **(Default)** Mattermost uses the email attribute to bind users to SAML.                                           | - Environment variable: ``MM_SAMLSETTINGS_ENABLESYNCWITHLDAPINCLUDEAUTH``                   |
|                                                                                                                                 |                                                                                             |
| This setting is only available when SAML authentication is enabled and AD/LDAP synchronization is enabled.                      |                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. note::
  - This setting should be **false** unless LDAP sync is enabled. Changing this setting from **true** to **false** will disable the override.
  - SAML IDs must match LDAP IDs when the override is enabled.
  - For more information, see :doc:`AD/LDAP Setup </administration-guide/onboard/ad-ldap>` for details.

.. config:setting:: identity-provider-metadata-url
  :displayname: Identity provider metadata URL (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.IdpMetadataURL
  :environment: MM_SAMLSETTINGS_IDPMETADATAURL
  :description: This setting is the URL from which Mattermost requests setup metadata from the provider.

Identity provider metadata URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This setting is the URL from which Mattermost requests setup metadata from the provider. | - System Config path: **Authentication > SAML 2.0**                  |
|                                                                                          | - ``config.json`` setting: ``SamlSettings`` > ``IdpMetadataURL``     |
| String input.                                                                            | - Environment variable: ``MM_SAMLSETTINGS_IDPMETADATAURL``           |
+------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: saml-sso-url
  :displayname: SAML SSO URL (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.IdpURL
  :environment: MM_SAMLSETTINGS_IDPURL
  :description: This setting is the URL where Mattermost sends a SAML request to start the login sequence.

SAML SSO URL
~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------+
| This setting is the URL where Mattermost sends a SAML request to start the login sequence. | - System Config path: **Authentication > SAML 2.0**      |
|                                                                                            | - ``config.json`` setting: ``SamlSettings`` > ``IdpURL`` |
| String input.                                                                              | - Environment variable: ``MM_SAMLSETTINGS_IDPURL``       |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------+

.. config:setting:: identity-provider-issuer-url
  :displayname: Identity provider issuer URL (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.IdpDescriptorURL
  :environment: MM_SAMLSETTINGS_IDPDESCRIPTORURL
  :description: This setting is the issuer URL for the Identity Provider for SAML requests.

Identity provider issuer URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+------------------------------------------------------------------------+
| This setting is the issuer URL for the Identity Provider for SAML requests. | - System Config path: **Authentication > SAML 2.0**                    |
|                                                                             | - ``config.json`` setting: ``SamlSettings`` > ``IdpDescriptorURL``     |
| String input.                                                               | - Environment variable: ``MM_SAMLSETTINGS_IDPDESCRIPTORURL``           |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: identity-provider-public-certificate
  :displayname: Identity provider public certificate (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.IdpCertificateFile
  :environment: MM_SAMLSETTINGS_IDPCERTIFICATEFILE
  :description: The public authentication certificate issued by your Identity Provider.

Identity provider public certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------+--------------------------------------------------------------------------+
| The public authentication certificate issued by your Identity Provider. | - System Config path: **Authentication > SAML 2.0**                      |
|                                                                         | - ``config.json`` setting: ``SamlSettings`` > ``IdpCertificateFile``     |
| String input.                                                           | - Environment variable: ``MM_SAMLSETTINGS_IDPCERTIFICATEFILE``           |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: verify-signature
  :displayname: Verify signature (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.Verify
  :environment: MM_SAMLSETTINGS_VERIFY

  - **true**: **(Default)** Mattermost checks that the SAML Response signature matches the Service Provider Login URL.
  - **false**: The signature is not verified. This is **not recommended** for production. Use this option for testing only.

Verify signature
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost checks that the SAML Response signature matches the Service Provider Login URL.      | - System Config path: **Authentication > SAML 2.0**                 |
| - **false**: The signature is not verified. This is **not recommended** for production. Use this option for testing only. | - ``config.json`` setting: ``SamlSettings`` > ``Verify`` > ``true`` |
|                                                                                                                           | - Environment variable: ``MM_SAMLSETTINGS_VERIFY``                  |
+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: service-provider-login-url
  :displayname: Service provider login URL (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.AssertionConsumerServiceURL
  :environment: MM_SAMLSETTINGS_ASSERTIONCONSUMERSERVICEURL

  Enter the URL of your Mattermost server, followed by ``/login/sso/saml``, i.e. ``https://example.com/login/sso/saml``.
  This setting is also known as the Assertion Consumer Service URL.

Service provider login URL
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Enter the URL of your Mattermost server, followed by ``/login/sso/saml``, i.e. ``https://example.com/login/sso/saml``. | - System Config path: **Authentication > SAML 2.0**                               |
|                                                                                                                        | - ``config.json`` setting: ``SamlSettings`` > ``AssertionConsumerServiceURL``     |
| Use HTTP or HTTPS depending on the configuration of the server.                                                        | - Environment variable: ``MM_SAMLSETTINGS_ASSERTIONCONSUMERSERVICEURL``           |
|                                                                                                                        |                                                                                   |
| This setting is also known as the Assertion Consumer Service URL.                                                      |                                                                                   |
+------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. config:setting:: service-provider-identifier
  :displayname: Service provider identifier (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.ServiceProviderIdentifier
  :environment: MM_SAMLSETTINGS_SERVICEPROVIDERIDENTIFIER
  :description: This setting is the unique identifier for the Service Provider, which in most cases is the same as the Service Provider Login URL. In ADFS, this must match the Relying Party Identifier.

Service provider identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| This setting is the unique identifier for the Service Provider, which in most cases is the same as the Service Provider Login URL. In ADFS, this must match the Relying Party Identifier. | - System Config path: **Authentication > SAML 2.0**                             |
|                                                                                                                                                                                           | - ``config.json`` setting: ``SamlSettings`` > ``ServiceProviderIdentifier``     |
| String input.                                                                                                                                                                             | - Environment variable: ``MM_SAMLSETTINGS_SERVICEPROVIDERIDENTIFIER``           | 
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: enable-encryption
  :displayname: Enable encryption (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.Encrypt
  :environment: MM_SAMLSETTINGS_ENCRYPT

  - **true**: **(Default)** Mattermost will decrypt SAML Assertions that are encrypted with your Service Provider Public Certificate.
  - **false**: Mattermost does not decrypt SAML Assertions. Use this option for testing only. It is **not recommended** for production.

Enable encryption
~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost will decrypt SAML Assertions that are encrypted with your Service Provider Public Certificate.   | - System Config path: **Authentication > SAML 2.0**                  |
| - **false**: Mattermost does not decrypt SAML Assertions. Use this option for testing only. It is **not recommended** for production. | - ``config.json`` setting: ``SamlSettings`` > ``Encrypt`` > ``true`` |
|                                                                                                                                       | - Environment variable: ``MM_SAMLSETTINGS_ENCRYPT``                  |
+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: service-provider-private-key
  :displayname: Service provider private key (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.PrivateKeyFile
  :environment: MM_SAMLSETTINGS_PRIVATEKEYFILE
  :description: This setting stores the private key used to decrypt SAML Assertions from the Identity Provider.

Service provider private key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This setting stores the private key used to decrypt SAML Assertions from the Identity Provider. | - System Config path: **Authentication > SAML 2.0**                  |
|                                                                                                 | - ``config.json`` setting: ``SamlSettings`` > ``PrivateKeyFile``     |
| String input.                                                                                   | - Environment variable: ``MM_SAMLSETTINGS_PRIVATEKEYFILE``           |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: service-provider-public-certificate
  :displayname: Service provider public certificate (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.PublicCertificateFile
  :environment: MM_SAMLSETTINGS_PUBLICCERTIFICATEFILE
  :description: This setting stores the certificate file used to sign a SAML request to the Identity Provider for a SAML login when Mattermost is initiating the login as the Service Provider.

Service provider public certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| This setting stores the certificate file used to sign a SAML request to the Identity Provider for a SAML login when Mattermost is initiating the login as the Service Provider. | - System Config path: **Authentication > SAML 2.0**                         |
|                                                                                                                                                                                 | - ``config.json`` setting: ``SamlSettings`` > ``PublicCertificateFile``     |
| String input.                                                                                                                                                                   | - Environment variable: ``MM_SAMLSETTINGS_PUBLICCERTIFICATEFILE``           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: sign-request
  :displayname: Sign request (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.SignRequest
  :environment: MM_SAMLSETTINGS_SIGNREQUEST

  - **true**: Mattermost signs the SAML request with the Service Provider Private Key.
  - **false**: Mattermost does not sign the SAML request.

Sign request
~~~~~~~~~~~~

+--------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| - **true**: Mattermost signs the SAML request with the Service Provider Private Key. | - System Config path: **Authentication > SAML 2.0**             |
| - **false**: Mattermost does not sign the SAML request.                              | - ``config.json`` setting: ``SamlSettings`` > ``SignRequest``   |
|                                                                                      | - Environment variable: ``MM_SAMLSETTINGS_SIGNREQUEST``         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: signature-algorithm
  :displayname: Signature algorithm
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.SignatureAlgorithm
  :environment: MM_SAMLSETTINGS_SIGNATUREALGORITHM
  :description: This setting determines the signature algorithm used to sign the SAML request. Options are: ``RSAwithSHA1``, ``RSAwithSHA256``, ``RSAwithSHA512``. From v11, default is ``RSAwithSHA256``. Previously ``RSAwithSHA1``.

Signature algorithm
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| This setting determines the signature algorithm used to sign the SAML request. Options are: ``RSAwithSHA1``, ``RSAwithSHA256``, ``RSAwithSHA512``. | - System Config path: **Authentication > SAML 2.0**                      |
|                                                                                                                                                    | - ``config.json`` setting: ``SamlSettings`` > ``SignatureAlgorithm``     |
| String input.                                                                                                                                      | - Environment variable: ``MM_SAMLSETTINGS_SIGNATUREALGORITHM``           |
|                                                                                                                                                    |                                                                          |
| .. note::                                                                                                                                          |                                                                          |
|                                                                                                                                                    |                                                                          |
|   From Mattermost v11, the default signature algorithm has been updated from ``RSAwithSHA1`` to ``RSAwithSHA256`` for improved security.           |                                                                          |
|   Existing configurations will continue to work, but new installations will default to ``RSAwithSHA256``.                                          |                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: canonical-algorithm
  :displayname: Canonical algorithm (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.CanonicalAlgorithm
  :environment: MM_SAMLSETTINGS_CANONICALALGORITHM

  This setting determines the canonicalization algorithm. With these options:
  - ``Canonical1.0`` **(Default)** for `Exclusive XML Canonicalization 1.0 (omit comments) <https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/>`__ (``http://www.w3.org/2001/10/xml-exc-c14n#``)
  - ``Canonical1.1`` for `Canonical XML 1.1 (omit comments) <https://www.w3.org/TR/2008/REC-xml-c14n11-20080502/>`__ (``http://www.w3.org/2006/12/xml-c14n11``)

Canonical algorithm
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| This setting determines the canonicalization algorithm. With these options:                                                                                                                                                                | - System Config path: **Authentication > SAML 2.0**                             |
|                                                                                                                                                                                                                                            | - ``config.json`` setting: ``SamlSettings`` > ``CanonicalAlgorithm``            |
| - **Canonical1.0**: **(Default)** `Exclusive XML Canonicalization 1.0 (omit comments) <https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/>`__ (``http://www.w3.org/2001/10/xml-exc-c14n#``). ``config.json`` setting: ``Canonical1.0``. | - Environment variable: ``MM_SAMLSETTINGS_CANONICALALGORITHM``                  |
| - **Canonical1.1**:  `Canonical XML 1.1 (omit comments) <https://www.w3.org/TR/2008/REC-xml-c14n11-20080502/>`__ (``http://www.w3.org/2006/12/xml-c14n11``). ``config.json`` setting: ``Canonical1.1``.                                    |                                                                                 |
|                                                                                                                                                                                                                                            |                                                                                 |
| String input.                                                                                                                                                                                                                              |                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: email-attribute
  :displayname: Email attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.EmailAttribute
  :environment: MM_SAMLSETTINGS_EMAILATTRIBUTE
  :description: This setting determines the attribute from the SAML Assertion that populates the user email address field in Mattermost.

Email attribute
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This setting determines the attribute from the SAML Assertion that populates the user email address field in Mattermost.                                   | - System Config path: **Authentication > SAML 2.0**                  |
|                                                                                                                                                            | - ``config.json`` setting: ``SamlSettings`` > ``EmailAttribute``     |
| Notifications are sent to this email address. This email address may be visible to other users, depending on how the system admin has set-up user privacy. | - Environment variable: ``MM_SAMLSETTINGS_EMAILATTRIBUTE``           |
|                                                                                                                                                            |                                                                      |
| String input.                                                                                                                                              |                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: username-attribute
  :displayname: Username attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.UsernameAttribute
  :environment: MM_SAMLSETTINGS_USERNAMEATTRIBUTE
  :description: This setting determines the SAML Assertion attribute that populates the username field in the Mattermost UI.

Username attribute
~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| This setting determines the SAML Assertion attribute that populates the username field in the Mattermost UI.                                                                                                                                             | - System Config path: **Authentication > SAML 2.0**                     |
|                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``SamlSettings`` > ``UsernameAttribute``     |
| This attribute identifies users in the UI. For example, if a username is set to ``john.smith``, typing ``@john`` will show ``@john.smith`` as an auto-complete option, and posting a message with ``@john.smith`` will send a notification to that user. | - Environment variable: ``MM_SAMLSETTINGS_USERNAMEATTRIBUTE``           |
|                                                                                                                                                                                                                                                          |                                                                         |
| String input.                                                                                                                                                                                                                                            |                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: id-attribute
  :displayname: Id attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.IdAttribute
  :environment: MM_SAMLSETTINGS_IDATTRIBUTE
  :description: (Optional) This setting determines the SAML Assertion attribute used to bind users from SAML to users in Mattermost.

Id attribute
~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute used to bind users from SAML to users in Mattermost. | - System Config path: **Authentication > SAML 2.0**          |
|                                                                                                                      | - ``config.json`` setting: ``SamlSettings`` > ``IdAttribute``|
| String input.                                                                                                        | - Environment variable: ``MM_SAMLSETTINGS_IDATTRIBUTE``      |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. config:setting:: guest-attribute
  :displayname: Guest attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.GuestAttribute
  :environment: MM_SAMLSETTINGS_GUESTATTRIBUTE
  :description: (Optional) This setting determines the SAML Assertion attribute used to apply a Guest role to users in Mattermost.

Guest attribute
~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute used to apply a Guest role to users in Mattermost.       | - System Config path: **Authentication > SAML 2.0**             |
|                                                                                                                          | - ``config.json`` setting: ``SamlSettings`` > ``GuestAttribute``|
| See the :doc:`Guest Accounts documentation </administration-guide/onboard/guest-accounts>` for more information.         | - Environment variable: ``MM_SAMLSETTINGS_GUESTATTRIBUTE``      |
|                                                                                                                          |                                                                 |
| String input.                                                                                                            |                                                                 |
+--------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: enable-admin-attribute
  :displayname: Enable admin attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.EnableAdminAttribute
  :environment: MM_SAMLSETTINGS_ENABLEADMINATTRIBUTE

  - **true**: System admin status is determined by the SAML Assertion attribute set in **Admin attribute**.
  - **false**: **(Default)** System admin status is **not** determined by the SAML Assertion attribute

Enable admin attribute
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - **true**: System admin status is determined by the SAML Assertion attribute set in **Admin attribute**. | - System Config path: **Authentication > SAML 2.0**                                |
| - **false**: **(Default)** System admin status is **not** determined by the SAML Assertion attribute.     | - ``config.json`` setting: ``SamlSettings`` > ``EnableAdminAttribute`` > ``false`` |
|                                                                                                           | - Environment variable: ``MM_SAMLSETTINGS_ENABLEADMINATTRIBUTE``                   |
+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: admin-attribute
  :displayname: Admin attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.AdminAttribute
  :environment: MM_SAMLSETTINGS_ADMINATTRIBUTE
  :description: (Optional) This setting determines the attribute in the SAML Assertion for designating system admins.

Admin attribute
~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| (Optional) This setting determines the attribute in the SAML Assertion for designating system admins.                         | - System Config path: **Authentication > SAML 2.0**                  |
|                                                                                                                               | - ``config.json`` setting: ``SamlSettings`` > ``AdminAttribute``     |
| Users are automatically promoted to this role when logging in to Mattermost.                                                  | - Environment variable: ``MM_SAMLSETTINGS_ADMINATTRIBUTE``           |
|                                                                                                                               |                                                                      |
| If the Admin attribute is removed, users that are logged in retain Admin status. The role is revoked only when users log out. |                                                                      |
|                                                                                                                               |                                                                      |
| String input.                                                                                                                 |                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: first-name-attribute
  :displayname: First name attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.FirstNameAttribute
  :environment: MM_SAMLSETTINGS_FIRSTNAMEATTRIBUTE
  :description: (Optional) This setting determines the SAML Assertion attribute that populates the first name of users in Mattermost.

First name attribute
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute that populates the first name of users in Mattermost. | - System Config path: **Authentication > SAML 2.0**                      |
|                                                                                                                       | - ``config.json`` setting: ``SamlSettings`` > ``FirstNameAttribute``     |
|                                                                                                                       | - Environment variable: ``MM_SAMLSETTINGS_FIRSTNAMEATTRIBUTE``           |
| String input.                                                                                                         |                                                                          |
+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: last-name-attribute
  :displayname: Last name attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.LastNameAttribute
  :environment: MM_SAMLSETTINGS_LASTNAMEATTRIBUTE
  :description: (Optional) This setting determines the SAML Assertion attribute that populates the last name of users in Mattermost.

Last name attribute
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute that populates the last name of users in Mattermost. | - System Config path: **Authentication > SAML 2.0**                     |
|                                                                                                                      | - ``config.json`` setting: ``SamlSettings`` > ``LastNameAttribute``     |
|                                                                                                                      | - Environment variable: ``MM_SAMLSETTINGS_LASTNAMEATTRIBUTE``           |
| String input.                                                                                                        |                                                                         |
+----------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: nickname-attribute
  :displayname: Nickname attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.NicknameAttribute
  :environment: MM_SAMLSETTINGS_NICKNAMEATTRIBUTE
  :description: (Optional) This setting determines the SAML Assertion attribute that populates the nickname of users in Mattermost.

Nickname attribute
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute that populates the nickname of users in Mattermost. | - System Config path: **Authentication > SAML 2.0**                     |
|                                                                                                                     | - ``config.json`` setting: ``SamlSettings`` > ``NicknameAttribute``     |
|                                                                                                                     | - Environment variable: ``MM_SAMLSETTINGS_NICKNAMEATTRIBUTE``           |
| String input.                                                                                                       |                                                                         |
+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: position-attribute
  :displayname: Position atribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.PositionAttribute
  :environment: MM_SAMLSETTINGS_POSITIONATTRIBUTE
  :description: (Optional) This setting determines the SAML Assertion attribute that populates the position (job title or role at company) of users in Mattermost.

Position attribute
~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute that populates the position (job title or role at company) of users in Mattermost. | - System Config path: **Authentication > SAML 2.0**                     |
|                                                                                                                                                    | - ``config.json`` setting: ``SamlSettings`` > ``PositionAttribute``     |
|                                                                                                                                                    | - Environment variable: ``MM_SAMLSETTINGS_POSITIONATTRIBUTE``           |
| String input.                                                                                                                                      |                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: preferred-language-attribute
  :displayname: Preferred language attribute (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.LocaleAttribute
  :environment: MM_SAMLSETTINGS_LOCALEATTRIBUTE
  :description: (Optional) This setting determines the SAML Assertion attribute that populates the language preference of users in Mattermost.

Preferred language attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute that populates the language preference of users in Mattermost. | - System Config path: **Authentication > SAML 2.0**              |
|                                                                                                                                | - ``config.json`` setting: ``SamlSettings`` > ``LocaleAttribute``|
|                                                                                                                                | - Environment variable: ``MM_SAMLSETTINGS_LOCALEATTRIBUTE``      |
| String input.                                                                                                                  |                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: login-button-text
  :displayname: Login button text (SAML)
  :systemconsole: Authentication > SAML 2.0
  :configjson: .SamlSettings.LoginButtonText
  :environment: MM_SAMLSETTINGS_LOGINBUTTONTEXT
  :description: (Optional) The text that appears in the login button on the login page. Default is **SAML**.

Login button text
~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------+-------------------------------------------------------------------+
| (Optional) The text that appears in the login button on the sign-in page. | - System Config path: **Authentication > SAML 2.0**               |
|                                                                           | - ``config.json`` setting: ``SamlSettings`` > ``LoginButtonText`` |
| String input. Default is **SAML**.                                        | - Environment variable: ``MM_SAMLSETTINGS_LOGINBUTTONTEXT``       |
+---------------------------------------------------------------------------+-------------------------------------------------------------------+

----

OAuth 2.0
---------

Access the following configuration settings in the System Console by going to **Authentication > OAuth 2.0**. Settings for GitLab OAuth authentication can also be accessed under **Authentication > GitLab** in self-hosted deployments.

Use these settings to configure OAuth 2.0 for account creation and login.

.. config:setting:: select-oauth-20-service-provider
  :displayname: Select OAuth 2.0 service provider (OAuth)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: N/A
  :environment: N/A
  :description: Use this setting to enable OAuth and specify the service provider.

Select OAuth 2.0 service provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| Use this setting to enable OAuth and specify the service provider, with these options:                                                         | - System Config path: **Authentication > OAuth 2.0** |
|                                                                                                                                                | - ``config.json`` setting: N/A                       |
| - **Do not allow login via an OAuth 2.0 provider**                                                                                             | - Environment variable: N/A                          |
| - **GitLab** (Available in all plans; see `GitLab 2.0 OAuth settings <#gitlab-oauth-2-0-settings>`__)                                          |                                                      |
| - **Google Apps** (Available in Mattermost Enterprise and Professional; see `Google OAuth 2.0 settings <#google-oauth-2-0-settings>`__)        |                                                      |
| - **Entra ID** (Available in Mattermost Enterprise and Professional; see `Entra ID OAuth 2.0 settings <#entraid-oauth-2-0-settings>`__)        |                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+

GitLab OAuth 2.0 settings
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   For Enterprise subscriptions, GitLab settings can be found under **OAuth 2.0**

.. config:setting:: openid-connect
  :displayname: Enable OAuth 2.0 authentication with GitLab (OAuth - GitLab)
  :systemconsole: Authentication > OAuth 2.0 (or GitLab)
  :configjson: .GitLabSettings.Enable
  :environment: MM_GITLABSETTINGS_ENABLE

  - **true**: Allows team and account creation using GitLab OAuth authentication. Input the **Secret** and **ID** credentials to configure.
  - **false**: **(Default)** Disables GitLab OAuth authentication.

Enable OAuth 2.0 authentication with GitLab
'''''''''''''''''''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| - **true**: Allows team and account creation using GitLab OAuth authentication. Input the **Secret** and **ID** credentials to configure. | - System Config path: **Authentication > OAuth 2.0 (or GitLab)**           | 
| - **false**: **(Default)** Disables GitLab OAuth authentication.                                                                          | - ``config.json`` setting: ``GitLabSettings`` > ``Enable`` > ``false``     |
|                                                                                                                                           | - Environment variable: ``MM_GITLABSETTINGS_ENABLE``                       |
+-------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: oauth-gitlabappid
  :displayname: GitLab OAuth 2.0 Application ID (OAuth - GitLab)
  :systemconsole: Authentication > OAuth 2.0 (or GitLab)
  :configjson: .GitLabSettings.Id
  :environment: MM_GITLABSETTINGS_ID
  :description: This setting holds the OAuth Application ID from GitLab.

GitLab OAuth 2.0 Application ID
'''''''''''''''''''''''''''''''

+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting holds the OAuth Application ID from GitLab. Generate the ID by these steps:                                                             | - System Config path: **Authentication > OAuth 2.0 (or GitLab)** |
|                                                                                                                                                      | - ``config.json`` setting: ``GitLabSettings`` > ``Id``           |
| 1. Login to your GitLab account.                                                                                                                     | - Environment variable: ``MM_GITLABSETTINGS_ID``                 |
| 2. Go to **Profile Settings > Applications > New Application** and enter a name.                                                                     |                                                                  |
| 3. Enter the Redirect URLs: ``https://<your-mattermost-url>/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.    |                                                                  |
| 4. Take the Application ID provided by GitLab and enter it in the Mattermost System Console field, ``config.json`` setting, or Environment variable. |                                                                  |
|                                                                                                                                                      |                                                                  |
| String input.                                                                                                                                        |                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. note::
  GitLab provides the `Application Secret Key <#gitlab-oauth-2-0-application-secret-key>`__ along with the the ID.

.. config:setting:: oauth-gitlabappsecretkey
  :displayname: GitLab OAuth 2.0 Application secret key (OAuth - GitLab)
  :systemconsole: Authentication > OAuth 2.0 (or GitLab)
  :configjson: .GitLabSettings.Secret
  :environment: MM_GITLABSETTINGS_SECRET
  :description: This setting holds the OAuth Application Secret Key from GitLab.

GitLab OAuth 2.0 Application secret key
'''''''''''''''''''''''''''''''''''''''

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting holds the OAuth Application Secret Key from GitLab. The key is generated at the same time as the **Application ID** (see `GitLab OAuth 2.0 Application ID <#gitlab-oauth-2-0-application-id>`__). | - System Config path: **Authentication > OAuth 2.0 (or GitLab)** |
|                                                                                                                                                                                                                | - ``config.json`` setting: ``GitLabSettings`` > ``Secret``       |
| Enter the key provided by GitLab in the Mattermost System Console field, ``config.json`` setting, or Environment variable.                                                                                     | - Environment variable: ``MM_GITLABSETTINGS_SECRET``             |
|                                                                                                                                                                                                                |                                                                  |
| String input.                                                                                                                                                                                                  |                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: oauth-gitlabsiteurl
  :displayname: GitLab OAuth 2.0 site URL (OAuth - GitLab)
  :systemconsole: Authentication > OAuth 2.0 (or GitLab)
  :configjson: N/A
  :environment: N/A
  :description: This setting holds the URL of your GitLab instance, e.g. ``https://example.com:3000``.

GitLab OAuth 2.0 site URL
'''''''''''''''''''''''''

+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting holds the URL of your GitLab instance, e.g. ``https://example.com:3000``. Use ``http://`` if SSL is not enabled on your GitLab instance. | - System Config path: **Authentication > OAuth 2.0 (or GitLab)** |
|                                                                                                                                                       | - ``config.json`` setting: N/A                                   |
|                                                                                                                                                       | - Environment variable: N/A                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: oauth-gitlabuserapiendpoint
  :displayname: GitLab OAuth 2.0 User API endpoint (OAuth - GitLab)
  :systemconsole: Authentication > OAuth 2.0 (or GitLab)
  :configjson: .GitLabSettings.UserAPIEndpoint
  :environment: MM_GITLABSETTINGS_USERAPIENDPOINT
  :description: This setting holds the URL of your GitLab User API endpoint, e.g. ``https://<your-gitlab-url>/api/v3/user``.

GitLab OAuth 2.0 User API endpoint
''''''''''''''''''''''''''''''''''

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| This setting holds the URL of your GitLab User API endpoint, e.g. ``https://<your-gitlab-url>/api/v3/user``. Use ``http://`` if SSL is not enabled on your GitLab instance. | - System Config path: **Authentication > OAuth 2.0 (or GitLab)**      |
|                                                                                                                                                                             | - ``config.json`` setting: ``GitLabSettings`` > ``UserAPIEndpoint``   |
| Enter the URL in the Mattermost System Console field, ``config.json`` setting, or Environment variable.                                                                     | - Environment variable: ``MM_GITLABSETTINGS_USERAPIENDPOINT``         |
|                                                                                                                                                                             |                                                                       |
| String input.                                                                                                                                                               |                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: oauth-gitlabauthendpoint
  :displayname: GitLab OAuth 2.0 Auth endpoint (OAuth - GitLab)
  :systemconsole: Authentication > OAuth 2.0 (or GitLab)
  :configjson: .GitLabSettings.AuthEndpoint
  :environment: MM_GITLABSETTINGS_AUTHENDPOINT
  :description: This setting holds the URL of your GitLab Auth endpoint, e.g. ``https://<your-gitlab-url>/oauth/authorize``.

GitLab OAuth 2.0 Auth endpoint
''''''''''''''''''''''''''''''

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting holds the URL of your GitLab Auth endpoint, e.g. ``https://<your-gitlab-url>/oauth/authorize``. Use ``http://`` if SSL is not enabled on your GitLab instance. | - System Config path: **Authentication > OAuth 2.0 (or GitLab)** |
|                                                                                                                                                                             | - ``config.json`` setting: ``GitLabSettings`` > ``AuthEndpoint`` |
| Enter the URL in the Mattermost System Console field, ``config.json`` setting, or Environment variable.                                                                     | - Environment variable: ``MM_GITLABSETTINGS_AUTHENDPOINT``       |
|                                                                                                                                                                             |                                                                  |
| String input.                                                                                                                                                               |                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: oauth-gitlabtokenendpoint
  :displayname: GitLab OAuth 2.0 Token endpoint (OAuth - GitLab)
  :systemconsole: Authentication > OAuth 2.0 (or GitLab)
  :configjson: .GitLabSettings.TokenEndpoint
  :environment: MM_GITLABSETTINGS_TOKENENDPOINT
  :description: This setting holds the URL of your GitLab OAuth Token endpoint, e.g. ``https://<your-gitlab-url>/oauth/token``.

GitLab OAuth 2.0 Token endpoint
'''''''''''''''''''''''''''''''

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting holds the URL of your GitLab OAuth Token endpoint, e.g. ``https://<your-gitlab-url>/oauth/token``. Use ``http://`` if SSL is not enabled on your GitLab instance. | - System Config path: **Authentication > OAuth 2.0 (or GitLab)** |
|                                                                                                                                                                                | - ``config.json`` setting: ``GitLabSettings`` > ``TokenEndpoint``|
| Enter the URL in the Mattermost System Console field, ``config.json`` setting, or Environment variable.                                                                        | - Environment variable: ``MM_GITLABSETTINGS_TOKENENDPOINT``      |
|                                                                                                                                                                                |                                                                  |
| String input.                                                                                                                                                                  |                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

Google OAuth 2.0 settings
^^^^^^^^^^^^^^^^^^^^^^^^^

.. config:setting:: oauth-googleenable
  :displayname: Enable OAuth 2.0 authentication with Google (OAuth - Google)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .GoogleSettings.Enable
  :environment: MM_GOOGLESETTINGS_ENABLE

  - **true**: Allows team and account creation using Google OAuth authentication.
  - **false**: **(Default)** Disables Google OAuth authentication.

Enable OAuth 2.0 authentication with Google
'''''''''''''''''''''''''''''''''''''''''''

+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: Allows team and account creation using Google OAuth authentication. Input the **Client ID** and **Client Secret** credentials to configure. | - System Config path: **Authentication > OAuth 2.0**                  |
| - **false**: **(Default)** Disables Google OAuth authentication.                                                                                        | - ``config.json`` setting: ``GoogleSettings`` > ``Enable`` > ``false``|
|                                                                                                                                                         | - Environment variable: ``MM_GOOGLESETTINGS_ENABLE``                  |
| See :doc:`Google Single Sign-On </administration-guide/onboard/sso-google>` implementation instructions.                                                |                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: oauth-googleclientid
  :displayname: Google OAuth 2.0 Client ID (OAuth - Google)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .GoogleSettings.Id
  :environment: MM_GOOGLESETTINGS_ID
  :description: This setting stores the OAuth Client ID from Google.

Google OAuth 2.0 Client ID
''''''''''''''''''''''''''

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+
| This setting stores the OAuth Client ID from Google. Generate the ID by going to the **Credentials** section of the Google Cloud Platform APIs & Services menu and selecting **Create Credentials > OAuth client ID**. | - System Config path: **Authentication > OAuth 2.0**  |
|                                                                                                                                                                                                                        | - ``config.json`` setting: ``GoogleSettings`` > ``Id``|
| See :doc:`Google Single Sign-On </administration-guide/onboard/sso-google>`  for instructions that can be used to implement Google OAuth or OpenID authentication.                                                     | - Environment variable: ``MM_GOOGLESETTINGS_ID``      |
|                                                                                                                                                                                                                        |                                                       |
| String input.                                                                                                                                                                                                          |                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+

.. config:setting:: oauth-googleclientsecret
  :displayname: Google OAuth 2.0 Client secret (OAuth - Google)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .GoogleSettings.Secret
  :environment: MM_GOOGLESETTINGS_SECRET
  :description: This setting stores the OAuth Client Secret from Google. The Secret is generated at the same time as the Client ID.

Google OAuth 2.0 Client secret
''''''''''''''''''''''''''''''

+---------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| This setting stores the OAuth Client Secret from Google. The Secret is generated at the same time as the Client ID. | - System Config path: **Authentication > OAuth 2.0**       |
|                                                                                                                     | - ``config.json`` setting: ``GoogleSettings`` > ``Secret`` |
| String input.                                                                                                       | - Environment variable: ``MM_GOOGLESETTINGS_SECRET``       |
+---------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+

.. config:setting:: oauth-googleuserapiendpoint
  :displayname: Google OAuth 2.0 User API endpoint (OAuth - Google)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .GoogleSettings.UserApiEndpoint
  :environment: MM_GOOGLESETTINGS_USERAPIENDPOINT
  :description: We recommend ``https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata`` as the User API Endpoint.

Google OAuth 2.0 User API endpoint
''''''''''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| We recommend ``https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP, or HTTPS, if available on the API server. | - System Config path: **Authentication > OAuth 2.0**                |
|                                                                                                                                                                                                                                                       | - ``config.json`` setting: ``GoogleSettings`` > ``UserAPIEndpoint`` |
| String input.                                                                                                                                                                                                                                         | - Environment variable: ``MM_GOOGLESETTINGS_USERAPIENDPOINT``       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: oauth-googleauthendpoint
  :displayname: Google OAuth 2.0 Auth endpoint (OAuth - Google)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .GoogleSettings.AuthEndpoint
  :environment: MM_GOOGLESETTINGS_AUTHENDPOINT
  :description: We recommend ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint.

Google OAuth 2.0 Auth endpoint
''''''''''''''''''''''''''''''

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| We recommend ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP, or HTTPS, if available on the server. | - System Config path: **Authentication > OAuth 2.0**             |   
|                                                                                                                                                                                            | - ``config.json`` setting: ``GoogleSettings`` > ``AuthEndpoint`` |
| String input.                                                                                                                                                                              | - Environment variable: ``MM_GOOGLESETTINGS_AUTHENDPOINT``       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: oauth-googletokenendpoint
  :displayname: Google OAuth 2.0 Token endpoint (OAuth - Google)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .GoogleSettings.TokenEndpoint
  :environment: MM_GOOGLESETTINGS_TOKENENDPOINT
  :description: We recommend ``https://www.googleapis.com/oauth2/v4/token`` as the Token Endpoint.

Google OAuth 2.0 Token endpoint
'''''''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| We recommend ``https://www.googleapis.com/oauth2/v4/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP, or HTTPS, if available on the server. | - System Config path: **Authentication > OAuth 2.0**              |
|                                                                                                                                                                                           | - ``config.json`` setting: ``GoogleSettings`` > ``TokenEndpoint`` |
| String input.                                                                                                                                                                             | - Environment variable: ``MM_GOOGLESETTINGS_TOKENENDPOINT``       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

Entra ID OAuth 2.0 settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   In line with Microsoft ADFS guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

.. config:setting:: oauth-entra-id-enable
  :displayname: Enable (OAuth - Entra ID)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .Office365Settings.Enable
  :environment: MM_OFFICE365SETTINGS_ENABLE

  - **true**: Allow team creation and account signup using Entra ID OAuth.
  - **false**: **(Default)** Entra ID OAuth cannot be used for team creation or account signup.

Enable OAuth 2.0 Authentication with Entra ID
'''''''''''''''''''''''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Allows team and account creation using Entra ID OAuth authentication.   | - System Config path: **Authentication > OAuth 2.0**                     |
| - **false**: **(Default)** Disables Entra ID OAuth authentication.                  | - ``config.json`` setting: ``Office365Settings`` > ``Enable`` > ``false``|
|                                                                                     | - Environment variable: ``MM_OFFICE365SETTINGS_ENABLE``                  |
+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::
  See the :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` documentation for details.

.. config:setting:: oauth-entra-id-appid
  :displayname: Application ID (OAuth - Entra ID)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .Office365Settings.Id
  :environment: MM_OFFICE365SETTINGS_ID
  :description: This setting holds the Application ID generated when configuring Entra ID as a Single Sign-On service through the Microsoft Azure Portal.

Entra ID OAuth 2.0 Application ID
'''''''''''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This setting holds the **Application ID** generated when configuring Entra ID as a Single Sign-On service through the Microsoft Azure Portal.   | - System Config path: **Authentication > OAuth 2.0**      |
|                                                                                                                                                 | - ``config.json`` setting: ``Office365Settings`` > ``Id`` |
| String input.                                                                                                                                   | - Environment variable: ``MM_OFFICE365SETTINGS_ID``       |
+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. note::
  See the :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` documentation for details.

.. config:setting:: oauth-entra-id-appsecret
  :displayname: Application secret password (OAuth - Entra ID)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .Office365Settings.Secret
  :environment: MM_OFFICE365SETTINGS_SECRET
  :description: This setting holds the Application Secret Password generated when configuring Entra ID as a Single Sign-On service through the Microsoft Azure Portal.

Entra ID OAuth 2.0 Application secret password
''''''''''''''''''''''''''''''''''''''''''''''''

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This setting holds the **Application Secret Password** generated when configuring Entra ID as a Single Sign-On service through the Microsoft Azure Portal.   | - System Config path: **Authentication > OAuth 2.0**          |
|                                                                                                                                                              | - ``config.json`` setting: ``Office365Settings`` > ``Secret`` |
| String input.                                                                                                                                                | - Environment variable: ``MM_OFFICE365SETTINGS_SECRET``       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. note::
  See the :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` documentation for details.

.. config:setting:: oauth-entra-id-directoryid
  :displayname: Directory ID (OAuth - Entra ID)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .Office365Settings.DirectoryId
  :environment: MM_OFFICE365SETTINGS_DIRECTORYID
  :description: This setting holds the Directory (tenant) ID set for Mattermost through the Azure Portal.

Entra ID OAuth 2.0 Directory (tenant) ID
''''''''''''''''''''''''''''''''''''''''''

+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This setting holds the **Directory (tenant) ID** set for Mattermost through the Azure Portal. | - System Config path: **Authentication > OAuth 2.0**               |
|                                                                                               | - ``config.json`` setting: ``Office365Settings`` > ``DirectoryId`` |
| String input.                                                                                 | - Environment variable: ``MM_OFFICE365SETTINGS_DIRECTORYID``       |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. note::
  See the :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` documentation for details.

.. config:setting:: oauth-entra-id-userapiendpoint
  :displayname: User API endpoint (OAuth - Entra ID)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .Office365Settings.UserAPIEndpoint
  :environment: MM_OFFICE365SETTINGS_USERAPIENDPOINT
  :description: We recommend using ``https://graph.microsoft.com/v1.0/me`` as the User API Endpoint. It is the default value.

Entra ID OAuth 2.0 User API endpoint
''''''''''''''''''''''''''''''''''''''

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| We recommend ``https://graph.microsoft.com/v1.0/me`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with ``http``, or ``https``, if available on the server. | - System Config path: **Authentication > OAuth 2.0**                   |
|                                                                                                                                                                                               | - ``config.json`` setting: ``Office365Settings`` > ``UserAPIEndpoint`` |
| String input.                                                                                                                                                                                 | - Environment variable: ``MM_OFFICE365SETTINGS_USERAPIENDPOINT``       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: oauth-entra-id-authendpoint
  :displayname: Auth endpoint (OAuth - Entra ID)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .Office365Settings.AuthEndpoint
  :environment: MM_OFFICE365SETTINGS_AUTHENDPOINT
  :description: We recommend ``https://login.microsoftonline.com/common/oauth2/v2.0/authorize`` as the Auth Endpoint.

Entra ID OAuth 2.0 Auth endpoint
''''''''''''''''''''''''''''''''''

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| We recommend ``https://login.microsoftonline.com/common/oauth2/v2.0/authorize`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with ``http``, or ``https``, if available on the server. | - System Config path: **Authentication > OAuth 2.0**                |
|                                                                                                                                                                                                                      | - ``config.json`` setting: ``Office365Settings`` > ``AuthEndpoint`` |
| String input.                                                                                                                                                                                                        | - Environment variable: ``MM_OFFICE365SETTINGS_AUTHENDPOINT``       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: oauth-entra-id-tokenendpoint
  :displayname: Token endpoint (OAuth - Entra ID)
  :systemconsole: Authentication > OAuth 2.0
  :configjson: .Office365Settings.TokenEndpoint
  :environment: MM_OFFICE365SETTINGS_TOKENENDPOINT
  :description: We recommend that you use ``https://login.microsoftonline.com/common/oauth2/v2.0/token`` as the Token Endpoint. It is the default value.

Entra ID OAuth 2.0 Token endpoint
'''''''''''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| We recommend ``https://login.microsoftonline.com/common/oauth2/v2.0/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with ``http``, or ``https``, if available on the server. | - System Config path: **Authentication > OAuth 2.0**                 |
|                                                                                                                                                                                                                   | - ``config.json`` setting: ``Office365Settings`` > ``TokenEndpoint`` |
| String input.                                                                                                                                                                                                     | - Environment variable: ``MM_OFFICE365SETTINGS_TOKENENDPOINT``       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

----

OpenID Connect
---------------

Access the following configuration settings in the System Console by going to **Authentication > OpenID Connect**.

.. config:setting:: select-openid-connect-service-provider
  :displayname: Select OpenID Connect service provider (OpenID Connect)
  :systemconsole: Authentication > OpenID Connect
  :configjson: N/A
  :environment: N/A
  :description: Choose whether OpenID Connect can be used for account creation and login.

Select OpenID Connect service provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------+-----------------------------------------------------------+
| Use this setting to enable OpenID Connect, with these options:                   | - System Config path: **Authentication > OpenID Connect** |
|                                                                                  | - ``config.json`` setting: N/A                            |
| - **Do not allow login via an OpenID provider**                                  | - Environment variable: N/A                               |
| - **GitLab** (`see settings <#gitlab-openid-settings>`__)                        |                                                           |
| - **Google Apps** (`see settings <#google-openid-settings>`__)                   |                                                           |
| - **Entra ID** (`see settings <#entra-id-openid-settings>`__)                    |                                                           |
| - **OpenID Connect (Other)** (`see settings <#openid-connect-other-settings>`__) |                                                           |
+----------------------------------------------------------------------------------+-----------------------------------------------------------+

.. note::
  **GitLab** OpenID is available in all plans. All other providers require Mattermost Enterprise or Professional.

GitLab OpenID settings
^^^^^^^^^^^^^^^^^^^^^^

.. config:setting:: gitlab-oidc-enable
  :displayname: Enable (OpenID Connect - GitLab)
  :systemconsole: Authentication > OpenID Connect
  :configjson: N/A
  :environment: N/A

  - **true**: Allow team creation and account signup using Gitlab OpenID Connect authentication.
  - **false**: **(Default)** Disables GitLab OpenID Connect authentication.

Enable OpenID Connect authentication with GitLab
''''''''''''''''''''''''''''''''''''''''''''''''

+------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: Allows team and account creation using GitLab OpenID Connect authentication. | - System Config path: **Authentication > OpenID Connect**              |
| - **false**: **(Default)** Disables GitLab OpenID Connect authentication.                | - ``config.json`` setting: ``GitLabSettings`` > ``Enable`` > ``false`` |
|                                                                                          | - Environment variable: ``MM_GITLABSETTINGS_ENABLE``                   |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. note::
  See the :doc:`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>` documentation for details.

.. config:setting:: oidc-gitlabsiteurl
  :displayname: GitLab site URL (OpenID Connect - GitLab)
  :systemconsole: Authentication > OpenID Connect
  :configjson: N/A
  :environment: N/A
  :description: Specify the URL of your GitLab instance (example ``https://example.com:3000``).

GitLab OpenID site URL
''''''''''''''''''''''

+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This setting stores the URL of your GitLab instance, e.g. **https://example.com:3000**. | - System Config path: **Authentication > OpenID Connect** |
|                                                                                         | - ``config.json`` setting: N/A                            |
|                                                                                         | - Environment variable: N/A                               |
| String input.                                                                           |                                                           |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. note::
  See **Step 2** of the :doc:`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>` documentation for details.

.. config:setting:: oidc-gitlabdiscoveryendpoint
  :displayname: Discovery endpoint (OpenID Connect - GitLab)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .GitLabSettings.DiscoveryEndpoint
  :environment: MM_GITLABSETTINGS_DISCOVERYENDPOINT
  :description: Obtain this value by registering Mattermost as an application in your service provider account.

GitLab OpenID Discovery endpoint
''''''''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This setting is prepopulated with the Discovery Endpoint for GitLab OpenID Connect. | - System Config path: **Authentication > OpenID Connect**            |
|                                                                                     | - ``config.json`` setting: ``GitLabSettings`` > ``DiscoveryEndpoint``|
|                                                                                     | - Environment variable: ``MM_GITLABSETTINGS_DISCOVERYENDPOINT``      |
| String input. Default is ``https://gitlab.com/.well-known/openid-configuration``    |                                                                      |
+-------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. note::
  See **Step 2** of the :doc:`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>` documentation for details.

.. config:setting:: oidc-gitlabclientid
  :displayname: Client ID (OpenID Connect - GitLab)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .GitLabSettings.Id
  :environment: MM_GITLABSETTINGS_ID
  :description: Obtain this value by registering Mattermost as an application in your service provider account.

GitLab OpenID Client ID
'''''''''''''''''''''''

+-----------------------------------------------------------------+--------------------------------------------------------------------------+
| This setting stores the **Application ID** generated by GitLab. | - System Config path: **Authentication > OpenID Connect**                |
|                                                                 | - ``config.json`` setting: ``GitLabSettings`` > ``Id``                   |
|                                                                 | - Environment variable: ``MM_GITLABSETTINGS_ID``                         |
| String input.                                                   |                                                                          |
+-----------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::
  See **Step 2** of the :doc:`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>` documentation for details.

.. config:setting:: oidc-gitlabclientsecret
  :displayname: Client secret (OpenID Connect - GitLab)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .GitLabSettings.Secret
  :environment: MM_GITLABSETTINGS_SECRET
  :description: Obtain this value by registering Mattermost as an application in your service provider account.

GitLab OpenID Client secret
'''''''''''''''''''''''''''

+-------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting stores the **Application Secret Key** generated by GitLab. | - System Config path: **Authentication > OpenID Connect**        |
|                                                                         | - ``config.json`` setting: ``GitLabSettings`` > ``Secret``       |
|                                                                         | - Environment variable: ``MM_GITLABSETTINGS_SECRET``             |
| String input.                                                           |                                                                  |
+-------------------------------------------------------------------------+------------------------------------------------------------------+

.. note::
  See **Step 2** of the :doc:`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>` documentation for details.

Google OpenID settings
^^^^^^^^^^^^^^^^^^^^^^


.. config:setting:: oidc-googleenable
  :displayname: Enable Google Settings (OpenID Connect - Google)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .GoogleSettings.Enable
  :environment: MM_GOOGLESETTINGS_ENABLE

Enable OpenID Connect authentication with Google
''''''''''''''''''''''''''''''''''''''''''''''''

  - **true**: Allow team creation and account signup using Google OpenID Connect.
  - **false**: **(Default)** Google OpenID Connect cannot be used for team creation or account signup.

+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: Allows team and account creation using Google OpenID authentication.                                 | - System Config path: **Authentication > OpenID Connect**              |
| - **false**: **(Default)** Disables Google OpenID authentication.                                                | - ``config.json`` setting: ``GoogleSettings`` > ``Enable`` > ``false`` |
|                                                                                                                  | - Environment variable: ``MM_GOOGLESETTINGS_ENABLE``                   |
| See :doc:`Google Single Sign-On </administration-guide/onboard/sso-google>` implementation instructions.         |                                                                        |
+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: oidc-googlediscoveryendpoint
  :displayname: Discovery endpoint (OpenID Connect - Google)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .GoogleSettings.DiscoveryEndpoint
  :environment: MM_GOOGLESETTINGS_DISCOVERYENDPOINT
  :description: This value is prepopulated with ``https://accounts.google.com/.well-known/openid-configuration``.

Google OpenID Discovery endpoint
''''''''''''''''''''''''''''''''

+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| This setting is prepopulated with the Discovery Endpoint for Google OpenID Connect.                                                                     | - System Config path: **Authentication > OpenID Connect**             |
|                                                                                                                                                         | - ``config.json`` setting: ``GoogleSettings`` > ``DiscoveryEndpoint`` |
| See :ref:`Configure Mattermost for Google Apps SSO <administration-guide/onboard/sso-google:step 3: configure mattermost for google apps sso>`.         | - Environment variable: ``MM_GOOGLESETTINGS_DISCOVERYENDPOINT``       |
|                                                                                                                                                         |                                                                       |
| String input. Default is ``https://accounts.google.com/.well-known/openid-configuration``                                                               |                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: oidc-googleclientid
  :displayname: Client ID (OpenID Connect - Google)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .GoogleSettings.Id
  :environment: MM_GOOGLESETTINGS_ID
  :description: Obtain this value by registering Mattermost as an application in your Google account.

Google OpenID Client ID
'''''''''''''''''''''''

+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This setting stores the Client ID generated by Google.                                                           | - System Config path: **Authentication > OpenID Connect** |
|                                                                                                                  | - ``config.json`` setting: ``GoogleSettings`` > ``Id``    |
| See :doc:`Google Single Sign-On </administration-guide/onboard/sso-google>` implementation instructions.         | - Environment variable: ``MM_GOOGLESETTINGS_ID``          |
|                                                                                                                  |                                                           |
| String input.                                                                                                    |                                                           |
+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. config:setting:: oidc-googleclientsecret
  :displayname: Client secret (OpenID Connect - Google)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .GoogleSettings.Secret
  :environment: MM_GOOGLESETTINGS_SECRET
  :description: Obtain this value by registering Mattermost as an application in your Google account.

Google OpenID Client secret
'''''''''''''''''''''''''''

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This setting stores the Client Secret generated by Google.                                                        | - System Config path: **Authentication > OpenID Connect** |
|                                                                                                                   | - ``config.json`` setting: ``GoogleSettings`` > ``Secret``|
| See :doc:`Google Single Sign-On </administration-guide/onboard/sso-google>`  implementation instructions.         | - Environment variable: ``MM_GOOGLESETTINGS_SECRET``      |
|                                                                                                                   |                                                           |
| String input.                                                                                                     |                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

Entra ID OpenID settings
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   In line with Microsoft ADFS guidance, we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

.. config:setting:: oidc-o365enable
  :displayname: Enable Entra ID Settings (OpenID Connect - Entra ID)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .Office365Settings.Enable
  :environment: MM_OFFICE365SETTINGS_ENABLE

  - **true**: Allow team creation and account signup using Entra ID OpenID Connect.
  - **false**: **(Default)** Entra ID OpenID Connect cannot be used for team creation or account signup.

Enable OpenID Connect authentication with Entra ID
''''''''''''''''''''''''''''''''''''''''''''''''''''

+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| - **true**: Allows team and account creation using Entra ID OpenID Connect authentication.                           | - System Config path: **Authentication > OpenID Connect**                 |
| - **false**: **(Default)** Disables Entra ID OpenID Connect authentication.                                          | - ``config.json`` setting: ``Office365Settings`` > ``Enable`` > ``false`` |
|                                                                                                                      | - Environment variable: ``MM_OFFICE365SETTINGS_ENABLE``                   |
| See :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` implementation instructions.          |                                                                           |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: oidc-o365directoryid
  :displayname: Directory ID (OpenID Connect - Entra ID)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .Office365Settings.DirectoryId
  :environment: MM_OFFICE365SETTINGS_DIRECTORYID
  :description: This setting holds the Directory (tenant) ID set for Mattermost through the Microsoft Azure Portal.

Entra ID OpenID Directory (tenant) ID
'''''''''''''''''''''''''''''''''''''''

+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This setting holds the Directory (tenant) ID set for Mattermost through the Microsoft Azure Portal.                  | - System Config path: **Authentication > OpenID Connect**          |
|                                                                                                                      | - ``config.json`` setting: ``Office365Settings`` > ``DirectoryId`` |
| See :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` implementation instructions.          | - Environment variable: ``MM_OFFICE365SETTINGS_DIRECTORYID``       |
|                                                                                                                      |                                                                    |
| String input.                                                                                                        |                                                                    |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: oidc-o365discoveryendpoint
  :displayname: Discovery endpoint (OpenID Connect - Entra ID)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .Office365Settings.DiscoveryEndpoint
  :environment: MM_OFFICE365SETTINGS_DISCOVERYENDPOINT
  :description: This value is prepopulated with ``https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration``.

Entra ID OpenID Discovery endpoint
''''''''''''''''''''''''''''''''''''

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| This setting is prepopulated with the Discovery Endpoint for Entra ID OpenID Connect.                                                                                                                      | - System Config path: **Authentication > OpenID Connect**                                                          |
|                                                                                                                                                                                                            | - ``config.json`` setting: ``Office365Settings`` > ``DiscoveryEndpoint``                                           |
| See :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` implementation instructions.                                                                                                | - Environment variable: ``MM_OFFICE365SETTINGS_DISCOVERYENDPOINT``                                                 |
|                                                                                                                                                                                                            |                                                                                                                    |
| String input. Default is ``https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration``                                                                                                |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: oidc-o365clientid
  :displayname: Client ID (OpenID Connect - Entra ID)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .Office365Settings.Id
  :environment: MM_OFFICE365SETTINGS_ID
  :description: This setting stores the Application (client) ID  generated through the Microsoft Azure Portal.

Entra ID Client ID
''''''''''''''''''''

+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This setting stores the **Application (client) ID** generated through the Microsoft Azure Portal.                    | - System Config path: **Authentication > OpenID Connect** |
|                                                                                                                      | - ``config.json`` setting: ``Office365Settings`` > ``Id`` |
| See :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` implementation instructions.          | - Environment variable: ``MM_OFFICE365SETTINGS_ID``       |
|                                                                                                                      |                                                           |
| String input.                                                                                                        |                                                           |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. config:setting:: oidc-entra-id-clientsecret
  :displayname: Client secret (OpenID Connect - Entra ID)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .Office365Settings.Secret
  :environment: MM_OFFICE365SETTINGS_SECRET
  :description: This setting stores the Client Secret generated through the Microsoft Azure Portal.

Entra ID Client secret
''''''''''''''''''''''''

+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| This setting stores the **Client Secret** generated through the Microsoft Azure Portal.                              | - System Config path: **Authentication > OpenID Connect**      |
|                                                                                                                      | - ``config.json`` setting: ``Office365Settings`` > ``Secret``  |
| See :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` implementation instructions.          | - Environment variable: ``MM_OFFICE365SETTINGS_SECRET``        |
|                                                                                                                      |                                                                |
| String input.                                                                                                        |                                                                |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

OpenID Connect (other) settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. config:setting:: oidc-enable
  :displayname: Enable (OpenID Connect)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .OpenIdSettings.Enable
  :environment: MM_OPENIDSETTINGS_ENABLE

  - **True**: Allow team creation and account signup using OpenID Connect.
  - **False**: **(Default)** OpenID Connect cannot be used for team creation or account signup.

Enable OpenID Connect authentication with other service providers
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

+---------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: Allows team and account creation using other OpenID Connect service providers.                                      | - System Config path: **Authentication > OpenID Connect**              |
| - **false**: **(Default)** Disables OpenID Connect authentication with other service providers.                                 | - ``config.json`` setting: ``OpenIdSettings`` > ``Enable`` > ``false`` |
|                                                                                                                                 | - Environment variable: ``MM_OPENIDSETTINGS_ENABLE``                   |
| See :doc:`OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>` implementation instructions.         |                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: oidc-buttonname
  :displayname: Button name (OpenID Connect)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .OpenIdSettings.ButtonText
  :environment: MM_OPENIDSETTINGS_BUTTONTEXT
  :description: Specify the text that displays on the OpenID login button.

OpenID Connect (other) Button name
''''''''''''''''''''''''''''''''''

+-------------------------------------------------------+----------------------------------------------------------------+
| This setting is the text for the OpenID login button. | - System Config path: **Authentication > OpenID Connect**      | 
|                                                       | - ``config.json`` setting: ``OpenIdSettings`` > ``ButtonText`` |
| String input.                                         | - Environment variable: ``MM_OPENIDSETTINGS_BUTTONTEXT``       |
+-------------------------------------------------------+----------------------------------------------------------------+

.. config:setting:: oidc-buttoncolor
  :displayname: Button color
  :systemconsole: Authentication > OpenID Connect
  :configjson: .OpenIdSettings.ButtonColor
  :environment: MM_OPENIDSETTINGS_BUTTONCOLOR
  :description: Specify the color of the OpenID login button for white labeling purposes. Use a hex code with a #-sign before the code, for example ``#145DBF``.

OpenID Connect (other) Button color
'''''''''''''''''''''''''''''''''''

+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| This setting is the color of the OpenID login button. Use a hex code with a #-sign before the code, for example ``#145DBF``. | - System Config path: **Authentication > OpenID Connect**       |
|                                                                                                                              | - ``config.json`` setting: ``OpenIdSettings`` > ``ButtonColor`` |
| String input.                                                                                                                | - Environment variable: ``MM_OPENIDSETTINGS_BUTTONCOLOR``       |
+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: oidc-discoveryendpoint
  :displayname: Discovery endpoint (OpenID Connect)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .OpenIdSettings.DiscoveryEndpoint
  :environment: MM_OPENIDSETTINGS_DISCOVERYENDPOINT
  :description: Obtain this value by registering Mattermost as an application in your service provider account.

OpenID Connect (other) Discovery endpoint
'''''''''''''''''''''''''''''''''''''''''

+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| This setting stores the Discovery Endpoint URL from the OpenID provider.                               | - System Config path: **Authentication > OpenID Connect**             |
| The URL should be in the format of ``https://myopenid.provider.com/{my_organization}/                  | - ``config.json`` setting: ``OpenIdSettings`` > ``DiscoveryEndpoint`` |
| .well-known/openid-configuration``.                                                                    | - Environment variable: ``MM_OPENIDSETTINGS_DISCOVERYENDPOINT``       |
|                                                                                                        |                                                                       |
| See :doc:`OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>`             |                                                                       |
| implementation instructions.                                                                           |                                                                       |
|                                                                                                        |                                                                       |
| String input.                                                                                          |                                                                       |
+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. note::
  The **Discovery Endpoint** setting can be used to determine the connectivity and availability of arbitrary hosts. System admins concerned about this can use
  custom admin roles to limit access to modifying these settings. See the 
  :ref:`delegated granular administration <administration-guide/onboard/delegated-granular-administration:edit privileges of admin roles (advanced)>` documentation for details.

.. config:setting:: oidc-clientid
  :displayname: Client ID (OpenID Connect)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .OpenIdSettings.Id
  :environment: MM_OPENIDSETTINGS_ID
  :description: Obtain this value by registering Mattermost as an application in your service provider account.

OpenID Connect (other) Client ID
''''''''''''''''''''''''''''''''

+---------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This setting stores the Client ID from the OpenID provider.                                                                     | - System Config path: **Authentication > OpenID Connect** |
|                                                                                                                                 | - ``config.json`` setting: ``OpenIdSettings`` > ``Id``    |
| See :doc:`OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>` implementation instructions.         | - Environment variable: ``MM_OPENIDSETTINGS_ID``          |
|                                                                                                                                 |                                                           |
| String input.                                                                                                                   |                                                           |
+---------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. config:setting:: oidc-clientsecret
  :displayname: Client secret (OpenID Connect)
  :systemconsole: Authentication > OpenID Connect
  :configjson: .OpenIdSettings.Secret
  :environment: MM_OPENIDSETTINGS_SECRET
  :description: Obtain this value by registering Mattermost as an application in your service provider account.

OpenID Connect (other) Client secret
''''''''''''''''''''''''''''''''''''

+---------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This setting stores the Client Secret from the OpenID provider.                                                                 | - System Config path: **Authentication > OpenID Connect** |
|                                                                                                                                 | - ``config.json`` setting: ``OpenIdSettings`` > ``Secret``|
| See :doc:`OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>` implementation instructions.         | - Environment variable: ``MM_OPENIDSETTINGS_SECRET``      |
|                                                                                                                                 |                                                           |
| String input.                                                                                                                   |                                                           |
+---------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

----

Guest access
------------

Access the following configuration settings in the System Console by going to **Authentication > Guest Access**.

.. config:setting:: enable-guest-access
  :displayname: Enable guest access (Guest Access)
  :systemconsole: Authentication > Guest Access
  :configjson: .GuestAccountsSettings.Enable
  :environment: MM_GUESTACCOUNTSSETTINGS_ENABLE

  - **true**: Enables the guest account feature.
  - **false**: **(Default)** Disables the guest account feature.

Enable guest access
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+-------------------------------------------------------------------------------+
| - **true**: Enables the guest account feature.                 | - System Config path: **Authentication > Guest Access**                       |
| - **false**: **(Default)** Disables the guest account feature. | - ``config.json`` setting: ``GuestAccountsSettings`` > ``Enable`` > ``false`` |
|                                                                | - Environment variable: ``MM_GUESTACCOUNTSSETTINGS_ENABLE``                   |
+----------------------------------------------------------------+-------------------------------------------------------------------------------+

.. note::
  For billing purposes, activated guest accounts do consume a licensed seat, which is returned when the guest account is
  deactivated.This means that guest accounts count as a paid user in your Mattermost :doc:`workspace </end-user-guide/end-user-guide-index>`.

.. config:setting:: whitelisted-guest-domains
  :displayname: Whitelisted guest domains (Guest Access)
  :systemconsole: Authentication > Guest Access
  :configjson: .GuestAccountsSettings.RestrictCreationToDomains
  :environment: MM_GUESTACCOUNTSSETTINGS_RESTRICTCREATIONTODOMAINS
  :description: When populated, guest accounts can only be created by a verified email from this list of comma-separated domains.

Whitelisted guest domains
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Use this setting to restrict the creation of guest accounts. When set, guest accounts require a verified email address from one of the listed domains. | - System Config path: **Authentication > Guest Access**                              |
|                                                                                                                                                        | - ``config.json`` setting: ``GuestAccountsSettings`` > ``RestrictCreationToDomains`` |
| String input of one or more domains, separated by commas.                                                                                              | - Environment variable: ``MM_GUESTACCOUNTSSETTINGS_RESTRICTCREATIONTODOMAINS``       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. config:setting:: enforce-multi-factor-authentication
  :displayname: Enforce multi-factor authentication (Guest Access)
  :systemconsole: Authentication > Guest Access
  :configjson: .GuestAccountsSettings.EnforceMultifactorAuthentication
  :environment: MM_GUESTACCOUNTSSETTINGS_ENFORCEMULTIFACTORAUTHENTICATION

  - **True**: Multi-factor authentication (MFA) is required for login.
  - **False**: **(Default)** Multi-factor authentication for guests is optional.

.. config:setting:: show-guest-tag
  :displayname: Show guest tag (Guest Access)
  :systemconsole: Authentication > Guest Access
  :configjson: .GuestAccountsSettings.HideTags
  :environment: MM_GUESTACCOUNTSSETTINGS_HIDETAGS

  - **True**: **(Default)** Guest tags are visible in Mattermost.
  - **False**: **(Default)** Guest tags aren't visible in Mattermost.

Show guest tag
~~~~~~~~~~~~~~

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| - **true**: **(Default)** Guest tags are visible in Mattermost. | - System Config path: **Authentication > Guest Access**                        |
| - **false**:  Guest tags aren't visible in Mattermost.          | - ``config.json`` setting: ``GuestAccountsSettings`` > ``HideTags`` > ``true`` |
|                                                                 | - Environment variable: ``MM_GUESTACCOUNTSSETTINGS_HIDETAGS``                  |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. note::
  This configuration setting applies to all Mattermost clients, including web, desktop app, and mobile app. See the :doc:`guest accounts </administration-guide/onboard/guest-accounts>` documentation for details.

.. config:setting:: enable-guest-magic-link
  :displayname: Enable guest magic link authentication (Guest Access)
  :systemconsole: Authentication > Guest Access
  :configjson: .GuestAccountsSettings.EnableGuestMagicLink
  :environment: MM_GUESTACCOUNTSSETTINGS_ENABLEGUESTMAGICLINK

  - **true**: Enables magic link passwordless authentication for guest users.
  - **false**: **(Default)** Magic link authentication for guest users is disabled.

Enable guest magic link authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| - **true**: Enables magic link passwordless authentication for guest users.               | - System Config path: **Authentication > Guest Access**                                     |
| - **false**: **(Default)** Magic link authentication for guest users is disabled.         | - ``config.json`` setting: ``GuestAccountsSettings`` > ``EnableGuestMagicLink`` > ``false`` |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. note::
  See the :ref:`guest accounts <administration-guide/onboard/guest-accounts:configure magic links for guests>` documentation for guest user setup details.