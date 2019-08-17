===================================================
SAML Single-Sign-On (E20): Technical Documentation
===================================================

Security Assertion Markup Language (SAML) is an open standard that allows identity providers (IdP), like OneLogin, to pass authorization credentials to service providers (SP), like Mattermost.

In simpler terms, it means you can use one set of credentials to log in to many different sites. With OneLogin account, you can log in to Mattermost, Zendesk, Salesforce and other sites securely with the same account.

The main benefit is that it helps administrators centralize user management by controlling which sites users have access to with their OneLogin credentials.

.. contents::
  :backlinks: top
  :local:

SAML Providers
--------------------------------------------

**Identity Providers (IdP)**: An identity provider performs the authentication. When a user clicks to log in, the identity provider confirms who the user is, and sends data to the service provider with the proper authorization to access the site.

Examples: OneLogin, Okta, Microsoft Active Directory (ADFS) or Azure. This is the Wristband Tent.

**Service Providers (SP)**: A service provider gets authentication and authorization information from an IdP such as OneLogin. Once received, it gives the user access to the system and logs the user in.

Examples: Mattermost, Zendesk, Zoom, Salesforce.

Technical description of SAML synchronization with AD/LDAP
------------------------------------------------------------

When enabled, SAML synchronization with AD/LDAP occurs in phases:

1. Get all the current LDAP users from the Mattermost database who have ``Users.AuthService`` set to ``ldap``. This is a SQL query issued against the Mattermost database: ``SELECT * FROM Users WHERE AuthService = 'ldap'``.
2. Get all the current SAML users from the Mattermost database who have ``Users.AuthService`` set to ``saml``. This is a SQL query issued against the Mattermost database: ``SELECT * FROM Users WHERE AuthService = 'saml'``.
3. Get all the current LDAP users from the LDAP server as defined by ``LdapSettings.UserFilter``. This is an `LDAP query <https://github.com/mattermost/mattermost-server/blob/master/scripts/ldap-check.sh>`__ issued against the LDAP server. Users are retrieved in batches as defined by ``LdapSettings.MaxPageSize``.
4. Update LDAP attributes. For each existing Mattermost user retrieved in step 1, attempt to find a match against the list of LDAP users from step 3. To find matches, ``Users.AuthData`` field of the Mattermost user is compared against the ``LdapSettings.IdAttribute`` LDAP setting.

 - If any attribute of the user has changed, that attribute is copied from the LDAP server and the user is marked as updated.
 - If the corresponding ``LdapSettings.IdAttribute`` is not found, the user is assumed to be deleted from the LDAP server, and deactivated from Mattermost by setting the ``Users.DeleteAt`` field to a valid timestamp.

5. Update SAML attributes. For each existing Mattermost user retrieved in step 2, attempt to find a match against the list of LDAP users from step 3. To find matches, ``SamlSettings.Email`` is compared against the ``LdapSettings.EmailAttribute`` LDAP setting.

 - If any attribute of the user has changed, that attribute is copied from the LDAP server and the user is marked as updated.
 - If the corresponding ``LdapSettings.EmailAttribute`` is not found, the user is assumed to be deleted from the LDAP server, and deactivated from Mattermost by setting the ``Users.DeleteAt`` field to a valid timestamp.

Frequently Asked Questions
------------------------------------------------------------

How can I obtain a SAML metadata XML file consumed by Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can obtain the XML file by calling the Mattermost RESTful API endpoint at ``/api/v4/saml/metadata``.

For other useful SAML API calls, see the `API reference <https://api.mattermost.com/#tag/SAML>`_.
