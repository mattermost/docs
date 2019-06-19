=========================
SAML Single-Sign-On (E20)
=========================

Mattermost can be configured to act as a SAML 2.0 Service Provider. The SAML Single-Sign-On integration offers the following benefits:

- **Single-sign-on.** Users can sign-in to Mattermost with their SAML credentials.
- **Centralized identity management.** Mattermost accounts can display user information from SAML, such as first and last name, email and username.
- **Automatic account provisioning.** New Mattermost user accounts are automatically created the first time a user signs in with their SAML credentials on the Mattermost server.

Mattermost officially supports Okta, OneLogin and Microsoft ADFS as the identity providers (IDPs), please see links below for more details on how to configure SAML with these providers. 

.. toctree::
  :titlesonly:

  Okta SAML Configuration <sso-saml-okta>
  OneLogin SAML Configuration <sso-saml-onelogin.rst>
  Microsoft ADFS SAML Configuration <sso-saml-adfs>

If you'd like, you may also try configuring SAML for a custom IDP.  For instance, customers have successfully set up Duo, PingFederate and SimpleSAMLphp as a custom IDPs. We are open to providing assistance when configuring your custom IDP by answering Mattermost technical configuration questions and working with your IDP provider in support of resolving issues as they relate to Mattermost SAML configuration settings. However, we cannot guarantee your connection will work with Mattermost.

To assist with the process of getting a user file for your custom IDP, please see this `documentation <https://github.com/icelander/mattermost_generate_user_file>`_.

Please see more information on getting support `here <https://mattermost.com/support/>`_ and submit requests for official support of a particular provider on our `feature idea forum <https://mattermost.uservoice.com>`_.

Please note that we may not be able to guarantee that your connection will work with Mattermost, however we will consider improvements to our feature as we are able.  Please submit requests for official support of a particular provider on our `feature idea forum <https://mattermost.uservoice.com>`_. 
