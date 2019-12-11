==========================
SAML Single-Sign-On (E20)
==========================

Mattermost can be configured to act as a SAML 2.0 Service Provider. The SAML Single-Sign-On integration offers the following benefits:

- **Single-sign-on.** Users can sign-in to Mattermost with their SAML credentials.
- **Centralized identity management.** Mattermost accounts automatically pull user attributes from SAML upon login, such as full name, email and username.
- **Automatic account provisioning.** New Mattermost user accounts are automatically created the first time a user signs in with their SAML credentials on the Mattermost server.

SAML Single-Sign-On itself does not support periodic updates of user attributes nor automatic deprovisioning. However, SAML with AD/LDAP sync can be configured to support these use cases.

For more information about SAML, see `this article from Varonis <https://www.varonis.com/blog/what-is-saml/>`_, and `this conceptual example from DUO <https://duo.com/blog/the-beer-drinkers-guide-to-saml>`_.

Mattermost officially supports Okta, OneLogin and Microsoft ADFS as the identity providers (IDPs), please see links below for more details on how to configure SAML with these providers. 

.. toctree::
  :titlesonly:

  Okta SAML Configuration <sso-saml-okta>
  OneLogin SAML Configuration <sso-saml-onelogin.rst>
  Microsoft ADFS SAML Configuration <sso-saml-adfs>

In addition to the officially supported identity providers, you can also configure SAML for a custom IdP. For instance, customers have successfully set up Azure AD, DUO, PingFederate and SimpleSAMLphp as a custom IdPs. You can also set up MFA on top of your SAML provider for additional security.

Roadmap
----------

In Mattermost v5.14, you can optionally configure Mattermost to sign the SAML request using a private key to meet InfoSec requirements at your organization.

In future roadmap, the main consideration is an integration with SCIM, via plugin. Such an integration allows system administrators to create SAML provisioned users before their first login, and sync them against Mattermost permissions.

Currently user provisioning and deprovisioning can be handled with SAML sync, but relies on AD/LDAP - SCIM enables admins to control user provisioning and deprovisioning within the IdP itself.

For examples, see `Microsoft Azure AD integration with SCIM <https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/use-scim-to-provision-users-and-groups>`_ and `Okta user provisioning with SCIM <https://www.okta.com/integrate/documentation/scim/>`_.

Configuration Assistance
---------------------------------

We are open to providing assistance when configuring your custom IdP by answering Mattermost technical configuration questions and working with your IdP provider in support of resolving issues as they relate to Mattermost SAML configuration settings. However, we cannot guarantee your connection will work with Mattermost.

For technical documentation on SAML, see :doc:`sso-saml-technical`.

To assist with the process of getting a user file for your custom IDP, please see this `documentation <https://github.com/icelander/mattermost_generate_user_file>`_.

Please see more information on getting support `here <https://mattermost.com/support/>`_ and submit requests for official support of a particular provider on our `feature idea forum <https://mattermost.uservoice.com>`_.

Please note that we may not be able to guarantee that your connection will work with Mattermost, however we will consider improvements to our feature as we are able.  Please submit requests for official support of a particular provider on our `feature idea forum <https://mattermost.uservoice.com>`_.
