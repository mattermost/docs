Authentication configuration settings
=====================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost supports up to four distinct, concurrent methods of **Authentication**:

- An OpenID provider
- A SAML provider
- An LDAP instance (e.g., Active Directory, OpenLDAP)
- Email and Password

Access the following configuration settings in the System Console by going to **Authentication**, or by editing the ``config.json`` file as described in the following tables:

- `Signup <#signup>`__
- `Email <#email>`__
- `Password <#password>`__
- `MFA <#mfa>`__
- `AD/LDAP <#ad-ldap>`__
- `SAML 2.0 <#saml-2-0>`__
- `OAuth 2.0 <#oauth-2-0>`__
- `OpenID Connect <#openid-connect>`__
- `Guest Access <#guest-access>`__

----

Signup
------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > Signup**.

Enable account creation
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** New accounts can be created by an email invitation or a public team invitation link.                           | - System Config path: **Authentication > Signup**                      |
| - **false**: Disables new account creation. Attempting to create an account through an existing email or link displays an error message. | - ``config.json`` setting: ``.TeamSettings.EnableUserCreation: true``  |
|                                                                                                                                          | - Environment variable: ``MM_TEAMSETTINGS_ENABLEUSERCREATION``         |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
 										      
Restrict account creation to specified email domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| This setting limits the email address domains that can be used to create a new account or team. You **must** set `Require Email Verification <https://docs.mattermost.com/configure/configuration-settings.html#require-email-verification>`__ to ``true`` for the restriction to function. This setting only affects email login. | - System Config path: **Authentication > Signup**                       |
|                                                                                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``.TeamSettings.RestrictCreationToDomains``  |
| String input of a comma-separated list of domains, i.e. ``corp.mattermost.com, mattermost.com``                                                                                                                                                                                                                                    | - Environment variable: ``MM_TEAMSETTINGS_RESTRICTCREATIONTODOMAINS``   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

Enable open server
~~~~~~~~~~~~~~~~~~
  
+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| - **true**: Users can create accounts on the server without an invitation.                       | - System Config path: **Authentication > Signup**                   |
| - **false**: **(Default)** Users **must** have an invitation to create an account on the server. | - ``config.json`` setting: ``.TeamSettings.EnableOpenServer``       |
|                                                                                                  | - Environment variable: ``MM_TEAMSETTINGS_ENABLEOPENSERVER``        |
+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

Enable email invitations
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: Allows users to send email invitations.    | - System Config path: **Authentication > Signup**                      |
| - **false**: **(Default)** Disables email invitations. | - ``config.json`` setting: ``.ServiceSettings.EnableEmailInvitations`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_ENABLEEMAILINVITATIONS``  |
+--------------------------------------------------------+------------------------------------------------------------------------+

Invalidate pending email invites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| This button invalidates email invitations that have not been accepted (by default, invitations expire after 48 hours). | - System Config path: **Authentication > Signup** |
|                                                                                                                        | - ``config.json`` setting: N/A                    |
| This option has no ``config.json`` setting or environment variable.                                                    | - Environment variable: N/A                       |
+------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+

----

Email
------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > Email**.

Enable account creation with email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| - **true**: **(Default)** Allows creation of team and user accounts with email and password.                                                        | - System Config path: **Authentication > Email**                    |
| - **false**: Disables creation of team and user accounts with email and password. This requries a single sign-on service to create accounts.        | - ``config.json`` setting: ``.EmailSettings.EnableSignUpWithEmail`` |
|                                                                                                                                                     | - Environment variable: ``MM_EMAILSETTINGS_ENABLESIGNUPWITHEMAIL``  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

Require email verification
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: Requires email verification for new accounts before allowing the user to sign-in.                                       | - System Config path: **Authentication > Email**                       |
| - **false**: **(Default)** Disables email verification. This can be used to speed development by skipping the verification process. | - ``config.json`` setting: ``.EmailSettings.RequireEmailVerification`` |
|                                                                                                                                     | - Environment variable: ``MM_EMAILSETTINGS_REQUIREEMAILVERIFICATION``  |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

Enable sign-in with email
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to sign-in with email and password.                                                                                                      | - System Config path: **Authentication > Email**                    |
| - **false**: Disables authentication with email and password, and removes the option from the login screen. Use this option to limit authentication to single sign-on services. | - ``config.json`` setting: ``.EmailSettings.EnableSignInWithEmail`` |
|                                                                                                                                                                                 | - Environment variable: ``MM_EMAILSETTINGS_ENABLESIGNINWITHEMAIL``  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

Enable sign-in with username
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows authentication with a username and password for accounts created with an email address. This setting does not affect AD/LDAP sign-in. | - System Config path: **Authentication > Email**                               |
| - **false**: Disables authenticaton with a username and removes the option from the login screen.                                                                      | - ``config.json`` setting: ``.EmailSettings.EnableSignInWithUsername``         |
|                                                                                                                                                                        | - Environment variable: ``MM_EMAILSETTINGS_ENABLESIGNINWITHUSERNAME``          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----

Password
--------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > Password**.

Minimum password length
~~~~~~~~~~~~~~~~~~~~~~~

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| This setting determines the minimum number of characters in passwords. It must be a whole number greater than or equal to 5 and less than or equal to 64. | - System Config path: **Authentication > Password**            |
|                                                                                                                                                           | - ``config.json`` setting: ``.PasswordSettings.MinimumLength`` |
| Numerical input. Default is **5**.                                                                                                                        | - Environment variable: ``MM_PASSWORDSETTINGS_MINIMUMLENGTH``  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Password requirements
~~~~~~~~~~~~~~~~~~~~~~

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This setting controls password character requirements. By checking the corresponding box, passwords must contain: | - System Config path: **Authentication > Password**                                                                                                                                  |
|                                                                                                                   | - ``config.json`` settings: ``.PasswordSettings.Lowercase: false``, ``.PasswordSettings.Uppercase: false``, ``.PasswordSettings.Number: false``, ``.PasswordSettings.Symbol: false`` |
| - **At least one lowercase letter**                                                                               | - Environment variables: ``MM_PASSWORDSETTINGS_LOWERCASE``, ``MM_PASSWORDSETTINGS_UPPERCASE``, ``MM_PASSWORDSETTINGS_NUMBER``, ``MM_PASSWORDSETTINGS_SYMBOL``                        |
| - **At least one uppercase letter**                                                                               |                                                                                                                                                                                      |
| - **At least one number**                                                                                         |                                                                                                                                                                                      |
| - **At least one symbol** out of these: ``!"#$%&'()*+,-./:;<=>?@[]^_`|~``.                                        |                                                                                                                                                                                      |
|                                                                                                                   |                                                                                                                                                                                      |
| The error message previewed in the System Console will appear if the user attempts to set an invalid password.    |                                                                                                                                                                                      |
|                                                                                                                   |                                                                                                                                                                                      |
| The default for all boxes is unchecked. The default for all settings in ``config.json`` is ``false``.             |                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Maximum login attempts
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| This setting determines the number of failed sign-in attempts a user can make before being locked out and required to go through a password reset by email. | - System Config path: **Authentication > Password**                      |
|                                                                                                                                                             | - ``config.json`` setting: ``.ServiceSettings.MaximumLoginAttempts: 10`` |
| Numerical input. Default is **10**.                                                                                                                         | - Environment variable: ``MM_SERVICESETTINGS_MAXIMUMLOGINATTEMPTS``      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

----

MFA
----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > MFA**.

We recommend deploying Mattermost within your own private network, and using VPN clients for mobile access, so that Mattermost is secured with your existing protocols. If you choose to run Mattermost outside your private network, bypassing your existing security protocols, we recommend adding a multi-factor authentication service specifically for accessing Mattermost.

Enable multi-factor authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| - **true**: Users who sign-in with AD/LDAP or an email address have the option to add `multi-factor authentication <https://docs.mattermost.com/onboard/multi-factor-authentication.html>`__ to their accounts. | - System Config path: **Authentication > MFA**                                         |
| - **false**: **(Default)** Disables multi-factor authentication                                                                                                                                                 | - ``config.json`` setting: ``.ServiceSettings.EnableMultifactorAuthentication: false`` |
|                                                                                                                                                                                                                 | - Environment variable: ``MM_SERVICESETTINGS_ENABLEMULTIFACTORAUTHENTICATION``         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

Enforce multi-factor authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: Requires `multi-factor authentication (MFA) <https://docs.mattermost.com/onboard/multi-factor-authentication.html>`__ for users who sign-in with AD/LDAP or an email address.  | - System Config path: **Authentication > MFA**                                   |
| New users must configure MFA. Logged in users are redirected to the MFA setup page until configuration is complete.                                                                        | - ``config.json`` setting: ``.ServiceSettings.EnforceMultifactorAuthentication`` |
| - **false**: MFA is optional.                                                                                                                                                              | - Environment variable: ``MM_SERVICESETTINGS_ENFORCEMULTIFACTORAUTHENTICATION``  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Note: If your system has users who authenticate with methods other than AD/LDAP and email, MFA must be enforced with the authentication provider outside of Mattermost.                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

AD/LDAP
-------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > AD/LDAP**.

Enable sign-in with AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-------------------------------------------------------------------------------+------------------------------------------------------------+
| - **true**: Allows sign-in with AD/LDAP or Active Directory.                  | - System Config path: **Authentication > AD/LDAP**         |
| - **false**: **(Default)** Disables sign-in with AD/LDAP or Active Directory. | - ``config.json`` setting: ``.LdapSettings.Enable: false`` |
|                                                                               | - Environment variable: ``MM_LDAPSETTINGS_ENABLE``         |
+-------------------------------------------------------------------------------+------------------------------------------------------------+

Enable synchronization with AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+---------------------------------------------------------------+----------------------------------------------------------------+
| - **true**: Mattermost periodically syncs users from AD/LDAP. | - System Config path: **Authentication > AD/LDAP**             |
| - **false**: **(Default)** Disables AD/LDAP synchronization.  | - ``config.json`` setting: ``.LdapSettings.EnableSync: false`` |
|                                                               | - Environment variable: ``MM_LDAPSETTINGS_ENABLESYNC``         |
+---------------------------------------------------------------+----------------------------------------------------------------+

Login field name
~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| This setting will display placeholder text in the login field of the sign-in page. This text can remind users to sign-in with their AD/LDAP credentials. | - System Config path: **Authentication > AD/LDAP**          |
|                                                                                                                                                          | - ``config.json`` setting: ``.LdapSettings.LoginFieldName`` |
| String input. Default is ``AD/LDAP Username``.                                                                                                           | - Environment variable: ``MM_LDAPSETTINGS_LOGINFIELDNAME``  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+

AD/LDAP server
~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------------+---------------------------------------------------------+
| This is the domain name or IP address of the AD/LDAP server. | - System Config path: **Authentication > AD/LDAP**      |
|                                                              | - ``config.json`` setting: ``.LdapSettings.LdapServer`` |
| String input.                                                | - Environment variable: ``MM_LDAPSETTINGS_LDAPSERVER``  |
+--------------------------------------------------------------+---------------------------------------------------------+

AD/LDAP port
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------------------+------------------------------------------------------------+
| This is the port Mattermost uses to connect to the AD/LDAP server. | - System Config path: **Authentication > AD/LDAP**         |
|                                                                    | - ``config.json`` setting: ``.LdapSettings.LdapPort: 389`` |
| Numerical input. Default is **389**.                               | - Environment variable: ``MM_LDAPSETTINGS_LDAPPORT``       |
+--------------------------------------------------------------------+------------------------------------------------------------+

Connection security
~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| This setting controls the type of security Mattermost uses to connect to the AD/LDAP server, with these options:                                                                                         | - System Config path: **Authentication > AD/LDAP**              |
|                                                                                                                                                                                                          | - ``config.json`` setting: ``.LdapSettings.ConnectionSecurity`` |
| - **None**: **(Default)** No encryption. With this option, it is **highly recommended** that the connection be secured outside of Mattermost, such as by a stunnel proxy. ``config.json`` option: ``""`` | - Environment variable: ``MM_LDAPSETTINGS_CONNECTIONSECURITY``  |
| - **TLS**: Encrypts communication with TLS. ``config.json`` option: ``"TLS"``                                                                                                                            |                                                                 |
| - **STARTTLS**: Attempts to upgrade an existing insecure connection to a secure connection with TLS. ``config.json`` option: ``"STARTTLS"``                                                              |                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

Skip certificate verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **true**: Disables the certificate verification step for TLS and STARTTLS connections. Use this option for testing. **Do not use** this option when TLS is required in production. | - System Config path: **Authentication > AD/LDAP**                              |
| - **false**: **(Default)** Enables certification verification.                                                                                                                       | - ``config.json`` setting: ``.LdapSettings.SkipCertificateVerification: false`` |
|                                                                                                                                                                                      | - Environment variable: ``MM_LDAPSETTINGS_SKIPCERTIFICATEVERIFICATION``         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

Private key
~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Use this setting to upload the private key file from your LDAP authentication provider, if TLS client certificates are the primary authentication mechanism.| - System Config path: **Authentication > AD/LDAP**          |
|                                                                                                                                                             | - ``config.json`` setting: ``.LdapSettings.PrivateKeyFile`` |
| String input.                                                                                                                                               | - Environment variable: ``MM_LDAPSETTINGS_PRIVATEKEYFILE``  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+

Public certificate
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| Use this setting to upload the public TLS certificate from your LDAP authentication provider, if TLS client certificates are the primary authentication mechanism. | - System Config path: **Authentication > AD/LDAP**                 |
|                                                                                                                                                                    | - ``config.json`` setting: ``.LdapSettings.PublicCertificateFile`` |
| String input.                                                                                                                                                      | - Environment variable: ``MM_LDAPSETTINGS_PUBLICCERTIFICATEFILE``  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Bind username
~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| This is the username for the account Mattermost utilizes to perform an AD/LDAP search. This should be an account specific to Mattermost. | - System Config path: **Authentication > AD/LDAP**        |
|                                                                                                                                          | - ``config.json`` setting: ``.LdapSettings.BindUsername`` |
| Limit the permissions of the account to read-only access to the portion of the AD/LDAP tree specified in the **Base DN** setting.        | - Environment variable: ``MM_LDAPSETTINGS_BINDUSERNAME``  |
|                                                                                                                                          |                                                           |
| When using Active Directory, **Bind Username** should specify domain in ``"DOMAIN/username"`` format.                                    |                                                           |
|                                                                                                                                          |                                                           |
| String input.                                                                                                                            |                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| **Note**: This field is required. Anonymous bind is not currently supported.                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Bind password
~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-------------------------------------------------------------------------------+-----------------------------------------------------------+
| This is the password for the username given in the **Bind Username** setting. | - System Config path: **Authentication > AD/LDAP**        |
|                                                                               | - ``config.json`` setting: ``.LdapSettings.BindPassword`` |
| String input.                                                                 | - Environment variable: ``MM_LDAPSETTINGS_BINDPASSWORD``  |
+-------------------------------------------------------------------------------+-----------------------------------------------------------+

Base DN
~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| This is the **Base Distinguished Name** of the location in the AD/LDAP tree where Mattermost will start searching for users. | - System Config path: **Authentication > AD/LDAP**  |
|                                                                                                                              | - ``config.json`` setting: ``.LdapSettings.BaseDN`` |
| String input.                                                                                                                | - Environment variable: ``MM_LDAPSETTINGS_BASEDN``  |
+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+

User filter
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| This setting accepts a `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__ AD/LDAP filter that is applied when searching for user objects. Only the users selected by the query can access Mattermost. For example, to filter out disabled users, the filter is: ``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``.              | - System Config path: **Authentication > AD/LDAP**      |
|                                                                                                                                                                                                                                                                                                                                                                                                         | - ``config.json`` setting: ``.LdapSettings.UserFilter`` |
| To filter by group membership, determine the ``distinguishedName`` of the group, then use group membership general syntax to format the filter. For example, if the security group ``distinguishedName`` is ``CN=group1,OU=groups,DC=example,DC=com``, then the filter is: ``(memberOf=CN=group1,OU=groups,DC=example,DC=com)``. The user must explicitly belong to this group for the filter to apply. | - Environment variable: ``MM_LDAPSETTINGS_USERFILTER``  |
|                                                                                                                                                                                                                                                                                                                                                                                                         |                                                         |
| String input.                                                                                                                                                                                                                                                                                                                                                                                           |                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| **Note**: This filter uses the permissions of the **Bind Username** account to execute the search. This account should be specific to Mattermost and have read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field.                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Group filter
~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| This setting accepts a `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__ AD/LDAP filter that is applied when searching for group objects. Only the groups selected by the query can access Mattermost.| - System Config path: **Authentication > AD/LDAP**       |
|                                                                                                                                                                                                                                                  | - ``config.json`` setting: ``.LdapSettings.GroupFilter`` |
| String input. Default is ``(|(objectClass=group)(objectClass=groupOfNames)(objectClass=groupOfUniqueNames))``.                                                                                                                                   | - Environment variable: ``MM_LDAPSETTINGS_GROUPFILTER``  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| **Note**: This filter is only used when AD/LDAP Group Sync is enabled. See `AD/LDAP Group Sync <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ for more information.                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable admin filter
~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: Enables the **Admin Filter** setting that designates System Admins using an AD/LDAP filter.                                                                                                                     | - System Config path: **Authentication > AD/LDAP**                    |
| - **false**: **(Default)** Disables the **Admin Filter** setting.                                                                                                                                                           | - ``config.json`` setting: ``.LdapSettings.EnableAdminFilter: false`` |
|                                                                                                                                                                                                                             | - Environment variable: ``MM_LDAPSETTINGS_ENABLEADMINFILTER``         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Note**: If this setting is ``false``, no additional users are designated as System Admins by the filter. Users that were previously designated as System Admins retain this role unless the filter is changed or removed.                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Admin filter
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| This setting accepts an AD/LDAP filter that designates the selected users as System Admins. Users are promoted to this role on their next sign-in or on the next scheduled AD/LDAP sync. | - System Config path: **Authentication > AD/LDAP**       |
|                                                                                                                                                                                          | - ``config.json`` setting: ``.LdapSettings.AdminFilter`` |
| If the Admin Filter is removed, users who are currently logged in retain their Admin role until their next sign-in.                                                                      | - Environment variable: ``MM_LDAPSETTINGS_ADMINFILTER``  |
|                                                                                                                                                                                          |                                                          |
| String input.                                                                                                                                                                            |                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+

Guest filter
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| This setting accepts an AD/LDAP filter to apply when searching for external users with Guest Access to Mattermost. Only users selected by the query can access Mattermost as Guests. | - System Config path: **Authentication > AD/LDAP**       |
|                                                                                                                                                                                      | - ``config.json`` setting: ``.LdapSettings.GuestFilter`` |
| See `Guest Accounts <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.                                                                               | - Environment variable: ``MM_LDAPSETTINGS_GUESTFILTER``  |
|                                                                                                                                                                                      |                                                          |
| String input.                                                                                                                                                                        |                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+

ID attribute
~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that is serves as a unique user identifier in Mattermost.                                                                                              | - System Config path: **Authentication > AD/LDAP**                                                                               |
|                                                                                                                                                                                                    | - ``config.json`` setting: ``.LdapSettings.IdAttribute``                                                                         |
| The attribute should have a unique value that does not change, such as ``objectGUID`` or ``entryUUID``. Confirm that these attributes are available in your environment before making any changes. | - Environment variable: ``MM_LDAPSETTINGS_IDATTRIBUTE``                                                                          |
|                                                                                                                                                                                                    |                                                                                                                                  |
| String input.                                                                                                                                                                                      |                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| **Note**: If a user's ID Attribute changes, a new Mattermost account is created that is not associated with the previous account. If you need to change this field after users have signed-in, use the `mattermost ldap idmigrate <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-ldap-idmigrate>`__ CLI tool. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Login ID attribute
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that is used for signing-in to Mattermost. This is normally the same as the **Username Attribute**.                         | - System Config path: **Authentication > AD/LDAP**            |
|                                                                                                                                                                         | - ``config.json`` setting: ``.LdapSettings.LoginIdAttribute`` |
| If your team uses ``domain\username`` to sign-in to other services with AD/LDAP, you may enter ``domain\username`` in this field to maintain consistency between sites. | - Environment variable: ``MM_LDAPSETTINGS_LOGINIDATTRIBUTE``  |
|                                                                                                                                                                         |                                                               |
| String input.                                                                                                                                                           |                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Username attribute
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the username field in Mattermost.                                                                                                                                                                       | - System Config path: **Authentication > AD/LDAP**             |
|                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``.LdapSettings.UsernameAttribute`` |
| This attribute identifies users in the UI. For example, if a Username Attribute is set to ``john.smith``, typing ``@john`` will show ``@john.smith`` as an auto-complete option, and posting a message with ``@john.smith`` will send a notification to that user. | - Environment variable: ``MM_LDAPSETTINGS_USERNAMEATTRIBUTE``  |
|                                                                                                                                                                                                                                                                    |                                                                |
| This is normally the same as the **Login ID Attribute**, but it can be mapped to a different attribute.                                                                                                                                                            |                                                                |
|                                                                                                                                                                                                                                                                    |                                                                |
| String input.                                                                                                                                                                                                                                                      |                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Email attribute
~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| This is the attribute in AD/LDAP server that populates the email address field in Mattermost.                                  | - System Config path: **Authentication > AD/LDAP**         |
|                                                                                                                                | - ``config.json`` setting ``.LdapSettings.EmailAttribute`` |
| Email notifications are sent to this address. The address may be seen by other Mattermost users depending on privacy settings. | - Environment variable: ``MM_LDAPSETTINGS_EMAILATTRIBUTE`` |
|                                                                                                                                |                                                            |
| String input.                                                                                                                  |                                                            |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+

First name attribute
~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the first name field in Mattermost.                 | - System Config path: **Authentication > AD/LDAP**              |
|                                                                                                                | - ``config.json`` setting: ``.LdapSettings.FirstNameAttribute`` |
| When set, users cannot edit their first name.                                                                  | - Environment variable: ``MM_LDAPSETTINGS_FIRSTNAMEATTRIBUTE``  |
|                                                                                                                |                                                                 |
| When not set, users can edit their first name in their :doc:`profile settings </welcome/manage-your-profile>`. |                                                                 |
|                                                                                                                |                                                                 |
| String input.                                                                                                  |                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

Last name attribute
~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the last name field in Mattermost.                         | - System Config path: **Authentication > AD/LDAP**             |
|                                                                                                                       | - ``config.json`` setting: ``.LdapSettings.LastNameAttribute`` |
| When set, users cannot edit their last name.                                                                          | - Environment variable: ``MM_LDAPSETTINGS_LASTNAMEATTRIBUTE``  |
|                                                                                                                       |                                                                |
| When not set, users can edit their last name as part of their :doc:`profile settings </welcome/manage-your-profile>`. |                                                                |
|                                                                                                                       |                                                                |
| String input.                                                                                                         |                                                                |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Nickname attribute
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the nickname field in Mattermost.                         | - System Config path: **Authentication > AD/LDAP**             |
|                                                                                                                      | - ``config.json`` setting: ``.LdapSettings.NicknameAttribute`` |
| When set, users cannot edit their nickname.                                                                          | - Environment variable: ``MM_LDAPSETTINGS_NICKNAMEATTRIBUTE``  |
|                                                                                                                      |                                                                |
| When not set, users can edit their nickname as part of their :doc:`profile settings </welcome/manage-your-profile>`. |                                                                |
|                                                                                                                      |                                                                |
| String input.                                                                                                        |                                                                |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Position attribute
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that populates the position field in Mattermost.                         | - System Config path: **Authentication > AD/LDAP**             |
|                                                                                                                      | - ``config.json`` setting: ``.LdapSettings.PositionAttribute`` |
| When set, users cannot edit their position.                                                                          | - Environment variable: ``MM_LDAPSETTINGS_POSITIONATTRIBUTE``  |
|                                                                                                                      |                                                                |
| When not set, users can edit their position as part of their :doc:`profile settings </welcome/manage-your-profile>`. |                                                                |
|                                                                                                                      |                                                                |
| String input.                                                                                                        |                                                                |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Profile picture attribute
~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This is the attribute in the AD/LDAP server that syncs and locks the profile picture in Mattermost. | - System Config path: **Authentication > AD/LDAP**            |
|                                                                                                     | - ``config.json`` setting: ``.LdapSettings.PictureAttribute`` |
| The image is updated when users sign-in, not when Mattermost syncs with the AD/LDAP server.         | - Environment variable: ``MM_LDAPSETTINGS_PICTUREATTRIBUTE``  |
|                                                                                                     |                                                               |
| The image is not updated if the Mattermost image already matches the AD/LDAP image.                 |                                                               |
|                                                                                                     |                                                               |
| String input.                                                                                       |                                                               |
+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Group display name attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| This is the AD/LDAP Group Display name attribute that populates the Mattermost group name field. | - System Config path: **Authentication > AD/LDAP**                                                                                          |
|                                                                                                  | - ``config.json`` setting: ``.LdapSettings.GroupDisplayNameAttribute``                                                                      |
| String input.                                                                                    | - Environment variable: ``MM_LDAPSETTINGS_GROUPDISPLAYNAMEATTRIBUTE``                                                                       |
+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**: This attribute is only used when AD/LDAP Group Sync is enabled and it is **required**.  See the `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ for more information. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Group ID attribute
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| This is an AD/LDAP Group ID attribute that sets a unique identifier for groups.                              | - System Config path: **Authentication > AD/LDAP**                                                                              |
|                                                                                                              | - ``config.json`` setting: ``.LdapSettings.GroupIdAttribute``                                                                   |
| This should be a value that does not change, such as ``entryUUID`` or ``objectGUID``.                        | - Environment variable: ``MM_LDAPSETTINGS_GROUPIDATTRIBUTE``                                                                    |
|                                                                                                              |                                                                                                                                 |
| String input.                                                                                                |                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| **Note**: This attribute is only used when AD/LDAP Group Sync is enabled and it is **required**.  See the `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ for more information. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Synchronization interval (minutes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This value determines how often Mattermost syncs with the AD/LDAP server by setting the number of minutes between each sync. | - System Config path: **Authentication > AD/LDAP**                   |
|                                                                                                                              | - ``config.json`` setting: ``.LdapSettings.SyncIntervalMinutes: 60`` |
| Syncing with the AD/LDAP server will update Mattermost accounts to match any changes made to AD/LDAP attributes.             | - Environment variable: ``MM_LDAPSETTINGS_SYNCINTERVALMINUTES``      |
|                                                                                                                              |                                                                      |
| Disabled AD/LDAP accounts become inactive users in Mattermost, and any active sessions are revoked.                          |                                                                      |
|                                                                                                                              |                                                                      |
| Use the **AD/LDAP Synchronize Now** button to immediately revoke a session after disabling an AD/LDAP account.               |                                                                      |
|                                                                                                                              |                                                                      |
| Numerical input. Default is **60**.                                                                                          |                                                                      |
+------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| **Note**: LDAP syncs require a large number of database read queries. Monitor database load and adjust the sync interval to minimize performance degradation.                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Maximum page size
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| This setting paginates the results of AD/LDAP server queries. Use this setting if your AD/LDAP server has a page size limit. | - System Config path: **Authentication > AD/LDAP**          |
|                                                                                                                              | - ``config.json`` setting: ``.LdapSettings.MaxPageSize: 0`` |
| The recommended setting is **1500**. This is the default AD/LDAP ``MaxPageSize``.                                            | - Environment variable: ``MM_LDAPSETTINGS_MAXPAGESIZE``     |
|                                                                                                                              |                                                             |
| A page size of **0** disables pagination of results.                                                                         |                                                             |
|                                                                                                                              |                                                             |
| Numerical input. Default is **0**.                                                                                           |                                                             |
+------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+

Query timeout (seconds)
~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This setting determines the timeout period, in seconds, for AD/LDAP queries. Increase this value to avoid timeout errors when querying a slow server. | - System Config path: **Authentication > AD/LDAP**            |
|                                                                                                                                                       | - ``config.json`` setting: ``.LdapSettings.QueryTimeout: 60`` |
| Numerical input. Default is **60**.                                                                                                                   | - Environment variable: ``MM_LDAPSETTINGS_QUERYTIMEOUT``      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

AD/LDAP test
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+---------------------------------------------------------------+----------------------------------------------------+
| Use this button to test the connection to the AD/LDAP server. | - System Config path: **Authentication > AD/LDAP** |
|                                                               | - ``config.json`` setting: N/A                     |
| If the test succeeds, a confirmation message is displayed.    | - Environment variable: N/A                        |
|                                                               |                                                    |
| If the test fails, an error message is displayed.             |                                                    |
+---------------------------------------------------------------+----------------------------------------------------+

AD/LDAP synchronize now
~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Use this button to immediately sync with the AD/LDAP server.                                              | - System Config path: **Authentication > AD/LDAP** |
|                                                                                                           | - ``config.json`` setting: N/A                     |
| The status of the sync is displayed in the table underneath the button (see the figure below).            | - Environment variable: N/A                        |
|                                                                                                           |                                                    |
| Following a manual sync, the next sync will occur after the time set in the **Synchronization Interval**. |                                                    |
+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| **Note**: If a sync is ``Pending`` and does not complete, check that **Enable Synchronization with AD/LDAP** is set to ``true``.                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. figure:: ../images/ldap-sync-table.png

.. _saml-enterprise:

----

SAML 2.0
--------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > SAML 2.0**.

.. note::
   In line with Microsoft ADFS guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`__.

Enable login with SAML
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost allows login using SAML. Please see `documentation <https://docs.mattermost.com/onboard/sso-saml.html>`__ to learn more about configuring SAML for Mattermost.

**False**: Login with SAML is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Enable synchronizing SAML accounts with AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost periodically synchronizes SAML user attributes, including user deactivation and removal, with AD/LDAP. Enable and configure synchronization settings at **Authentication > AD/LDAP**. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Synchronization of SAML accounts with AD/LDAP is disabled.

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSyncWithLdap": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

Ignore guest users when synchronizing with AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Available when ``Enable Synchronizing SAML Accounts With AD/LDAP`` is set to ``true``. 

**True**: Mattermost ignores Guest Users identified by the Guest Attribute when synchronizing with AD/LDAP on user deactivation and removal. Manage guest deactivation manually via **System Console > Users**. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Synchronization of SAML deactivates and removes Guest Users when synchronizing with AD/LDAP.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IgnoreGuestsLdapSync": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Override SAML bind data with AD/LDAP information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost overrides the SAML ID attribute with the AD/LDAP ID attribute if configured or overrides the SAML Email attribute with the AD/LDAP Email attribute if SAML ID attribute is not present. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Mattermost uses the email attribute to bind users to SAML.

.. note::
  Moving from ``true`` to ``false`` will prevent the override from happening. To prevent the disabling of user accounts, SAML IDs must match the LDAP IDs when this feature is enabled. This setting should be set to ``false`` unless LDAP sync is enabled.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSyncWithLdapIncludeAuth": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------------+

Identity provider metadata URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The URL where Mattermost sends a request to obtain setup metadata from the provider.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpMetadataUrl": ""`` with string input. |
+---------------------------------------------------------------------------------------+

SAML SSO URL
~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The URL where Mattermost sends a SAML request to start login sequence.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpURL": ""`` with string input. |
+-------------------------------------------------------------------------------+

Identity provider issuer URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The issuer URL for the Identity Provider you use for SAML requests.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpDescriptorUrl": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Identity provider public certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The public authentication certificate issued by your Identity Provider.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpCertificateFile": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Verify signature
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost verifies that the signature sent from the SAML Response matches the Service Provider Login URL.

**False**: Not recommended for production environments. For testing only.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Verify": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Service provider login URL
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Enter ``https://<your-mattermost-url>/login/sso/saml`` (example: ``https://example.com/login/sso/saml``). Make sure you use HTTP or HTTPS in your URL depending on your server configuration. This field is also known as the Assertion Consumer Service URL.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AssertionConsumerServiceURL": ""`` with string input. |
+----------------------------------------------------------------------------------------------------+

Service provider identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The unique identifier for the Service Provider, usually the same as Service Provider Login URL. In ADFS, this must match the Relying Party Identifier.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ServiceProviderIdentifier": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enable encryption
~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost will decrypt SAML Assertions encrypted with your Service Provider Public Certificate.

**False**: Not recommended for production environments. For testing only.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Encrypt": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Service provider private key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The private key used to decrypt SAML Assertions from the Identity Provider.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivateKeyFile": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Service provider public certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The certificate file used to generate the signature on a SAML request to the Identity Provider for a service provider initiated SAML login, when Mattermost is the Service Provider.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicCertificateFile": ""`` with string input. |
+----------------------------------------------------------------------------------------------+

Sign request
~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

When ``true``, Mattermost signs the SAML request using your Service Provider Private Key. When ``false``, Mattermost does not sign the SAML request.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignRequest": ""`` with string input. |
+------------------------------------------------------------------------------------+

Signature algorithm
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The signature algorithm used to sign the request. Supported options are `RSAwithSHA1 <https://www.w3.org/2000/09/xmldsig#rsa-sha1>`__, `RSAwithSHA256 <https://www.w3.org/2000/09/xmldsig#rsa-sha1>`__, and `RSAwithSHA512 <https://www.w3.org/2001/04/xmldsig-more#rsa-sha512>`__.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignatureAlgorithm": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Canonical algorithm
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The canonicalization algorithm. Supported options are ``Canonical1.0`` for `Exclusive XML Canonicalization 1.0 (omit comments) <https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/>`__ (``http://www.w3.org/2001/10/xml-exc-c14n#``) and ``Canonical1.1`` for `Canonical XML 1.1 (omit comments) <https://www.w3.org/TR/2008/REC-xml-c14n11-20080502/>`__ (``http://www.w3.org/2006/12/xml-c14n11``).

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CanonicalAlgorithm": "Canonical1.0"`` with string input. |
+-------------------------------------------------------------------------------------------------------+

Email attribute
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The attribute in the SAML Assertion that will be used to populate the email addresses of users in Mattermost.

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings chosen by the System Admin.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAttribute": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Username attribute
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The attribute in the SAML Assertion that will be used to populate the username field in Mattermost user interface. This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UsernameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Id attribute
~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion used to bind users from SAML to users in Mattermost.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------+

Guest attribute
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion used to apply a Guest role to users in Mattermost.

See the `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GuestAttribute": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Enable admin attribute
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables System Admins to configure the SAML Assertion.

**False**: Disables the ability for System Admins to configure the SAML Assertion.

Admin attribute
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion for designating System Admins. The user is automatically promoted to this role on their next login. If the Admin Attribute is removed, users who are currently logged in retain their Admin role. When they log out this is revoked and on their next login they will no longer have Admin privileges.

This attribute's default is ``false`` and must be set to ``true`` in order for the Admin Attribute to be used.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAdminAttribute": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

First name attribute
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the first name of users in Mattermost.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FirstNameAttribute": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Last name attribute
~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the last name of users in Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LastNameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Nickname attribute
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the nickname of users in Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NicknameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Position attribute
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the position field for users in Mattermost (typically used to describe a person's job title or role at the company).

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PositionAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Preferred language attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the language of users in Mattermost.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocaleAttribute": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Login button text
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The text that appears in the login button on the login page. Defaults to **SAML**.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonText": ""`` with string input. |
+----------------------------------------------------------------------------------------+

----

OAuth 2.0
---------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > OAuth 2.0**.

.. note::
  
  OAuth 2.0 is being deprecated and will be replaced by `OpenID Connect <https://docs.mattermost.com/configure/configuration-settings.html#openid-connect>`__ in a future release.

Settings to configure OAuth login for account creation and login.

Select OAuth 2.0 service provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

Choose whether OAuth can be used for account creation and login. Options include:

- **Do not allow login via an OAuth 2.0 provider**
- **GitLab** (available in all plans; see `GitLab Settings <https://docs.mattermost.com/configure/configuration-settings.html#gitlab-settings>`__ for details)
- **Google Apps** (Available in Mattermost Enterprise and Professional; see `Google Settings <https://docs.mattermost.com/configure/configuration-settings.html#google-settings>`__ for details)
- **Office 365** (Available in Mattermost Enterprise and Professional; see `Office 365 Settings <https://docs.mattermost.com/configure/configuration-settings.html#office-365-settings>`__ for details)

This feature's setting does not appear in ``config.json``.

GitLab
^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable authentication with GitLab
''''''''''''''''''''''''''''''''''

**True**: Allow team creation and account signup using GitLab OAuth. To configure, input the **Secret** and **Id** credentials.

**False**: GitLab OAuth cannot be used for team creation or account signup.

.. note:: 
   For Enterprise subscriptions, GitLab settings can be found under **OAuth 2.0**

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Application ID
''''''''''''''

Obtain this value by logging into your GitLab account. Go to **Profile Settings > Applications > New Application**, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Application secret key
''''''''''''''''''''''

Obtain this value by logging into your GitLab account. Go to **Profile Settings > Applications > New Application**, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

GitLab site URL
''''''''''''''''

Specify the URL of your GitLab instance (example ``https://example.com:3000``). If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``.

User API endpoint
''''''''''''''''''

Enter ``https://<your-gitlab-url>/api/v3/user`` (example: ``https://example.com:3000/api/v3/user``). Use HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Auth endpoint
'''''''''''''

Enter ``https://<your-gitlab-url>/oauth/authorize`` (example: ``https://example.com:3000/oauth/authorize``). Use HTTP or HTTPS depending on how your server is configured.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Token endpoint
''''''''''''''

Enter ``https://<your-gitlab-url>/oauth/token`` (example: ``https://example.com:3000/oauth/token``). Use HTTP or HTTPS depending on how your server is configured.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": ""`` with string input. |
+--------------------------------------------------------------------------------------+

Google
^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable authentication with Google by selecting ``Google Apps`` from **OAuth 2.0 > Select OAuth 2.0 service provider**.

**True**: Allow team creation and account signup using Google OAuth. To configure, input the **Client ID** and **Client Secret** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-google.html>`__ for more detail.

**False**: Google OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Client ID
'''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client secret
'''''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

User API endpoint
''''''''''''''''''

*Available in legacy Enterprise Edition E20*

We recommend you use ``https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata"``   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Auth endpoint
'''''''''''''

*Available in legacy Enterprise Edition E20*

We recommend you use ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://accounts.google.com/o/oauth2/v2/auth"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------------+

Token endpoint
'''''''''''''''

*Available in legacy Enterprise Edition E20*

We recommend that you use ``https://www.googleapis.com/oauth2/v4/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://www.googleapis.com/oauth2/v4/token"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------+

Office 365
^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

.. note::
   In line with Microsoft ADFS guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`__.

Enable authentication with Office 365 by selecting **Office 365** from **System Console > Authentication > OAuth 2.0 > Select OAuth 2.0 service provider**.

**True**: Allow team creation and account signup using Office 365 OAuth. To configure, input the **Application ID** and **Application Secret Password** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-office.html>`__ for more detail.

**False**: Office 365 OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Application ID
''''''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Application secret password
'''''''''''''''''''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Directory (tenant) ID
''''''''''''''''''''''

*Available in legacy Enterprise Edition E20*

This value is the ID of the application's AAD directory.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DirectoryId": ""`` with string input. |
+------------------------------------------------------------------------------------+

User API endpoint
'''''''''''''''''

*Available in legacy Enterprise Edition E20*

We recommend using ``https://graph.microsoft.com/v1.0/me`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://graph.microsoft.com/v1.0/me"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Auth endpoint
'''''''''''''

*Available in legacy Enterprise Edition E20*

We recommend using ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"`` with string input.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Token endpoint
'''''''''''''''

*Available in legacy Enterprise Edition E20*

We recommend that you use ``https://login.microsoftonline.com/common/oauth2/v2.0/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/token"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

----

OpenID Connect
---------------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > OpenID Connect**.

Select OpenID Connect service provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

Choose whether OpenID Connect can be used for account creation and login. Options include:

- **Do not allow login via an OpenID provider**
- **GitLab** (available in all plans; see `GitLab Settings <https://docs.mattermost.com/configure/configuration-settings.html#gitlab-settings>`__ for details)
- **Google Apps** (Available in Mattermost Enterprise and Professional; see `Google Settings <https://docs.mattermost.com/configure/configuration-settings.html#google-settings>`__ for details)
- **Office 365** (Available in Mattermost Enterprise and Professional; see `Office 365 Settings <https://docs.mattermost.com/configure/configuration-settings.html#office-365-settings>`__ for details)
- **OpenID Connect (Other)** (Available in Mattermost Enterprise and Professional; see `OpenID Connect Settings <https://docs.mattermost.com/configure/configuration-settings.html#openid-connect-other-settings>`__ for more detail)

This feature's setting does not appear in ``config.json``.

GitLab settings
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

GitLab site URL
'''''''''''''''

*Available in legacy Enterprise Edition E10 and E20. Not available in Cloud Free.*

Specify the URL of your GitLab instance (example ``https://example.com:3000``). If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``.

Discovery endpoint
''''''''''''''''''

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Free*

Obtain this value by registering Mattermost as an application in your service provider account. Should be in the format ``https://myopenid.provider.com/{my_company}/.well-known/openid-configuration`` where the value of *{my_company}* is replaced with your organization.

Client ID
'''''''''

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Free*

Obtain this value by registering Mattermost as an application in your service provider account.

Client secret
'''''''''''''

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Free*

Obtain this value by registering Mattermost as an application in your Google account.

Google Settings
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable authentication with Google by selecting ``Google Apps`` from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using Google OpenID Connect. To configure, input the **Client ID**, **Client Secret**, and **DiscoveryEndpoint** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-google.html>`__ for more detail.

**False**: Google OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Discovery endpoint
'''''''''''''''''''

*Available in legacy Enterprise Edition E20*

This value is prepopulated with ``https://accounts.google.com/.well-known/openid-configuration``.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DiscoveryEndpoint": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Client ID
'''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client secret
'''''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Office 365 Settings
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

.. note::
   In line with Microsoft ADFS guidance, we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

Enable authentication with Office 365 by selecting **Office 365** from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using Office 365 OpenID Connect. To configure, input the **Application ID** and **Application Secret Password** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-office.html>`__ for more detail.

**False**: Office 365 OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Directory (tenant) ID
'''''''''''''''''''''

*Available in legacy Enterprise Edition E20*

This value is the ID of the application's AAD directory.

Discovery endpoint
''''''''''''''''''

*Available in legacy Enterprise Edition E20*

This value is prepopulated with https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration.

Client ID
''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

Client secret
'''''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

OpenID Connect (other) 
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable authentication with a service provider by selecting ``OpenID Connect (Other)`` from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using OpenID Connect. To configure, input the **Client ID**, **Client Secret**, and **DiscoveryEndpoint** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-openidconnect.html>`__ for more detail.

**False**: OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Button name
'''''''''''

*Available in legacy Enterprise Edition E20*

Specify the text that displays on the OpenID login button.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ButtonText": ""`` with string input. |
+-----------------------------------------------------------------------------------+

Button color
''''''''''''

Specify the color of the OpenID login button for white labeling purposes. Use a hex code with a #-sign before the code, for example ``#145DBF``.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ButtonColor": ""`` with string input. |
+------------------------------------------------------------------------------------+

Discovery endpoint
''''''''''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account. Should be in the format ``https://myopenid.provider.com/{my_company}/.well-known/openid-configuration`` where the value of *{my_company}* is replaced with your organization.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DiscoveryEndpoint": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Client ID
'''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client secret
'''''''''''''

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

----

Guest access
------------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Authentication > Guest Access**.

Enable guest access
~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

**True**: Allow guest invitations to channels within teams. Please see `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.

**False**: Email signup is disabled. This limits signup to Single sign-on services like OAuth or AD/LDAP.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Whitelisted guest domains
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

When populated, guest accounts can only be created by a verified email from this list of comma-separated domains.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictCreationToDomains": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enforce multi-factor authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10 and E20*

This setting defaults to false and is read-only if multi-factor authentication is not enforced for regular users.

**True**: Multi-factor authentication (MFA) is required for login. New guest users will be required to configure MFA on sign-up. Logged in guest users without MFA configured are redirected to the MFA setup page until configuration is complete.

**False**: Multi-factor authentication for guests is optional.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnforceMultifactorAuthentication": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------------+
