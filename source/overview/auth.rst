==================================
Corporate Directory Integration 
==================================

Mattermost Enterprise Edition offers advanced security and authentication options for integrating with corporate directories. This guide outlines the options available. 

Basic authentication 
----------------------------------

By default Mattermost offers authentication via email and password, which offers basic features including: 

- Account sign-up using email and password
- Password reset via email
- Ability to use same credentials to sign-in to web, desktop app and mobile app experiences 
- Ability to use username and password in place of email and password

Security features for authentication 
-------------------------------------------

A core set of features is available with all authentication options to help increase security: 

- Ability to `set session length <https://docs.mattermost.com/administration/config-settings.html#id33>`_ to define how long a user can use Mattermost before needing to re-enter credentials. 
- Ability for users to remotely sign-out of devices.
- Ability for IT admin to force sign-out of a user from devices.
- Ability to set rate limits on authentication API calls to deter password-guessing attacks.
- Ability to require multi-factor authentication on sign-in.
- For advanced deployments, password requirements for length and special characters can be added. 

Active Directory / LDAP authentication 
---------------------------------------

AD/LDAP is the most popular corporate directory integration option for deploying Mattermost behind a corporate firewall. Features include: 

- Account creation using AD/LDAP credentials 
- AD/LDAP user filters to define which users get access to Mattermost in the form of a query
- Ability to use a low-privileged AD/LDAP account to run queries over a secure TLS or STARTTLS connection
- Attribute mapping to place First Name, Last Name, Nickname and other attributes from AD/LDAP into Mattermost 
- Sychronization with AD/LDAP to disable, enable and update Mattermost users based on AD/LDAP 

For very large AD/LDAP instances you can also configure max page size to divide a Mattermost AD/LDAP query into several pieces to not over-tax the authentication server when synchronizing.

For private network deployments in development teams using GitLab for source control, `GitLab single sign-on <https://docs.mattermost.com/deployment/sso-gitlab.html>`_ is also available. 

DMZ authentication options 
--------------------------

When deploying Mattermost to a DMZ location outside the security of a private network, additional authentication options: 

- `Okta integration via SAML <https://docs.mattermost.com/deployment/sso-saml-okta.html>`_
- `Active Directory Federation Services via SAML <https://docs.mattermost.com/deployment/sso-saml-adfs.html>`_
- `SAML 2.0 authentication <https://docs.mattermost.com/deployment/sso-saml.html>`_
- `Google Apps <https://docs.mattermost.com/deployment/sso-google.html>`_
- `Office 365 <https://docs.mattermost.com/deployment/sso-office.html>`_

Generic OAuth and OpenID are not currently supported. 

Future authentication methods 
-----------------------------

Mattermost Enterprise Edition releases new improvements bi-monthly. Several additional authentication methods are planned, but not yet scheduled. If you're an enterprise interested in deploying with one of the following options, or another option not yet listed, please contact sales@mattermost.com to start a discussion. 

- Certificate-based authentication
- Authentication via reverse proxy
- Kerberos-based authentication 
