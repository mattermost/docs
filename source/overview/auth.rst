============================
Authentication and Security
============================

Mattermost has two levels of authentication and security at present.
Future versions of Mattermost will extend these two options,
but for now, the two main classes of authentication and security are the Mattermost Team Edition and the Mattermost Enterprise Editions.
The Mattermost Enterprise Editions have the distinct advantage of corporate directory integration. 

Basic authentication 
--------------------

The Mattermost Team Edition uses email and password for authentication.
Email and password may be used with any version of Mattermost.
Users may reset a password by email,
sign in to the web application, 
desktop application,
and mobile application with the same email and password,
and email can be substituted for username along with the same password.

Core Security
-------------

The core security features straddle the Mattermost Team Edition and the Mattermost Enterprise Editions.
In all versions of Mattermost users have the ability to:

- `Set session length <https://docs.mattermost.com/administration/config-settings.html#id33>`_, allowing administrators to define how long a user can use Mattermost before needing to re-enter credentials. 
- Remotely sign-out of devices
- Force sign-out of a user from devices
- Set rate limits on authentication API calls to deter password-guessing attacks
- Affix multi-factor authentication to sign-in.

Advanced deployments allow organizations to define password requirements for length and special characters. 

Existing Corporate Directories
------------------------------

One of The Mattermost Enterprise Editions must be used to incorporate existing directories like Microsoft's Active Directory (AD)or a Local Directory Access Protocol (LDAP) directory. AD and LDAP are the most popular corporate directory integrations for Mattermost deployments behind a corporate firewall. They both allow for:

- Account creation using AD/LDAP credentials 
- AD/LDAP user filters to define which users get access to Mattermost in the form of a query
- Low-privileged AD/LDAP accounts to run queries over a secure TLS or STARTTLS connection
- Attribute mapping to place First Name, Last Name, Nickname and other attributes of AD/LDAP into Mattermost 
- Customization of login screen to specify whether users are logging in with email, username, or another attribute
- Synchronization with AD/LDAP to disable, enable, and update Mattermost users based on AD/LDAP.

.. note::
New Mattermost accounts are created the first time a user signs in with AD/LDAP credentials,
or the `bulk loading <https://docs.mattermost.com/deployment/bulk-loading.html>`_ tool can create many at once.
Users with email/username and password authentications can `switch to AD/LDAP manually <https://docs.mattermost.com/deployment/sso-ldap.html#configure-ad-ldap-using-the-system-console-user-interface>`_,
or a `conversion to AD/LDAP can be accomplished with the command line interface <https://docs.mattermost.com/administration/command-line-tools.html?highlight=cli#platform-user-migrate-auth>`_ by an IT admin. 

For very large AD/LDAP instances, you can also configure max page size to divide a Mattermost AD/LDAP query into several pieces to not over-tax the authentication server when synchronizing.

Authentication Outside Private Networks 
---------------------------------------

Additional authentication options are available for deploying Mattermost to a DMZ location outside the security of a private network. They are as follows:

- `Okta integration through SAML <https://docs.mattermost.com/deployment/sso-saml-okta.html>`_
- `OneLogin integration through SAML <https://docs.mattermost.com/deployment/sso-saml-onelogin.html>`_
- `Active Directory Federation Services through SAML <https://docs.mattermost.com/deployment/sso-saml-adfs.html>`_
- `SAML 2.0 authentication <https://docs.mattermost.com/deployment/sso-saml.html>`_
- `Google Apps <https://docs.mattermost.com/deployment/sso-google.html>`_
- `Office 365 <https://docs.mattermost.com/deployment/sso-office.html>`_.

Generic OAuth and OpenID are not currently supported. 

The Future of Authentication with Mattermost
--------------------------------------------

Mattermost Enterprise Editions release new improvements monthly. 
Several additional authentication methods are in planning. 
If your organization is interested in deploying certificates, 
reverse proxy, 
Kerberos, or another option, 
please contact sales@mattermost.com to start a discussion. 

