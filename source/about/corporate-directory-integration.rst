Corporate directory integration 
================================

Mattermost offers advanced security and authentication options for integrating with corporate directories. This guide outlines the options available.

Basic authentication 
---------------------

By default, Mattermost offers authentication via email and password, which offers basic features including:

- Account sign up using email and password.
- Password reset via email.
- Ability to use the same credentials to log into web, desktop, and mobile app experiences.
- Ability to use a username and password in place of email and password.

Security features for authentication 
------------------------------------

A core set of features is available with all authentication options to help increase security:

- Ability to :ref:`set session length <configure/environment-configuration-settings:session lengths>` to define how long a user can use Mattermost before needing to re-enter credentials.
- Ability for users to remotely sign out of devices.
- Ability for IT admin to force sign out of a user from devices.
- Ability to set rate limits on authentication API calls to deter password-guessing attacks.
- Ability to require multi-factor authentication on log in.
- For advanced deployments, password requirements for length and special characters can be added.

Active Directory/LDAP authentication
------------------------------------

:doc:`AD/LDAP </onboard/ad-ldap>` is the most popular corporate directory integration option for deploying Mattermost behind a corporate firewall. Features include:

- Account creation using AD/LDAP credentials.
- AD/LDAP user filters to define which users get access to Mattermost in the form of a query.
- Ability to use a low-privileged AD/LDAP account to run queries over a secure TLS or STARTTLS connection.
- Attribute mapping to place First Name, Last Name, Nickname, and other attributes from AD/LDAP into Mattermost.
- Customization of login screen to specify whether users are logging in with email, username, or other attribute.
- Synchronization with AD/LDAP to disable, enable, and update Mattermost users based on AD/LDAP.

.. note:: 
   - New user accounts are created when new users log in with their AD/LDAP credentials. You can optionally pre-create user accounts using the :doc:`bulk loading </onboard/bulk-loading-data>` tool.
   - If you're using email or username and password authentication :ref:`users can switch to AD/LDAP manually <onboard/ad-ldap:getting started>`, and the conversion to AD/LDAP can also be done using the :ref:`mmctl user migrate auth <manage/mmctl-command-line-tool:mmctl user migrate-auth>` command by an IT admin.

For very large AD/LDAP instances you can also configure max page size to divide a Mattermost AD/LDAP query into several pieces to not overtax the authentication server when synchronizing.

Authentication options outside of a private network
---------------------------------------------------

When deploying Mattermost to a DMZ location outside the security of a private network, additional authentication options include:

- :doc:`Okta integration via SAML </onboard/sso-saml-okta>`
- :doc:`OneLogin integration via SAML </onboard/sso-saml-onelogin>`
- :doc:`Active Directory Federation Services via SAML </onboard/sso-saml-adfs>`
- :doc:`SAML 2.0 authentication </onboard/sso-saml>`
- :doc:`Google Apps </onboard/sso-google>`
- :doc:`Office 365 </onboard/sso-office>`
- :doc:`OpenID Connect </onboard/sso-openidconnect>`

Generic OAuth is not currently supported.

Future authentication methods
-----------------------------

Mattermost releases new improvements monthly. Several additional authentication methods are planned, but not yet scheduled. If you're an enterprise interested in deploying with an option not yet provided in our documentation, please contact sales@mattermost.com to start a discussion.
