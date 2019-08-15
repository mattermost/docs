===================================================
SAML Single-Sign-On (E20): Technical Documentation
===================================================

Security Assertion Markup Language (SAML) is an open standard that allows identity providers (IdP), like OneLogin, to pass authorization credentials to service providers (SP), like Mattermost.

In simpler terms, it means you can use one set of credentials to log in to many different sites. With OneLogin account, you can log in to Mattermost, Zendesk, Salesforce and other sites securely with the same account.

The main benefit is that it helps administrators centralize user management by controlling which sites users have access to with their OneLogin credentials.

SAML Providers
--------------------------------------------

**Identity Providers (IdP)**: An identity provider performs the authentication. When a user clicks to log in, the identity provider confirms who the user is, and sends data to the service provider with the proper authorization to access the site.

Examples: OneLogin, Okta, Microsoft Active Directory (ADFS) or Azure. This is the Wristband Tent.

**Service Providers (SP)**: A service provider gets authentication and authorization information from an IdP such as OneLogin. Once received, it gives the user access to the system and logs the user in.

Examples: Mattermost, Zendesk, Zoom, Salesforce.
