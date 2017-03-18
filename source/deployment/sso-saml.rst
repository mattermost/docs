=========================
SAML Single-Sign-On (E20)
=========================

SAML Single-Sign-On integration offers the following benefits:

- **Single-sign-on.** Users can sign-in to Mattermost with their SAML credentials.
- **Centralized identity management.** Mattermost accounts can display user information from SAML, such as first and last name, email and username.
- **Automatic account provisioning.** New Mattermost user accounts are automatically created the first time a user signs in with their SAML credentials on the Mattermost server.

Mattermost officially supports Okta, OneLogin and Microsoft ADFS as the identity providers (IDPs), please see links below for more details on how to configure SAML with these providers. If you'd like, you may also try configuring SAML for a custom IDP.

.. toctree::
  :titlesonly:

  Okta SAML Configuration <sso-saml-okta>
  OneLogin SAML Configuration <sso-saml-onelogin.rst>
  Microsoft ADFS SAML Configuration <sso-saml-adfs>
