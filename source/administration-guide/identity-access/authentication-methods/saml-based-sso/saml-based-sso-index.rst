SAML-based SSO
==============

Use :doc:`SAML 2.0 </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml>` to authenticate users with your identity provider. Follow provider-specific guides and supporting references to plan, implement, and troubleshoot SAML SSO for :doc:`Microsoft ADFS for Windows Server 2012 </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml-adfs-msws2012>`, :doc:`Microsoft ADFS using Microsoft Windows Server 2016 </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml-adfs-msws2016>`, :doc:`OneLogin </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml-onelogin>`, :doc:`Okta </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml-okta>`, and :doc:`Keycloak </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml-keycloak>`.

.. toctree::
    :maxdepth: 1
    :titlesonly:

    sso-saml
    sso-saml-before-you-begin
    sso-saml-adfs
    sso-saml-adfs-msws2016
    sso-saml-okta
    sso-saml-onelogin
    sso-saml-keycloak
    sso-saml-ldapsync
    sso-saml-technical
    sso-saml-faq

You can :doc:`configure SAML synchronization with AD/LDAP </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml-ldapsync>` to keep user attributes up to date, manage account deactivation, and override SAML data to ensure user attributes are consistent across systems. 

See :doc:`SAML SSO technical guidance </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml-technical>` for additional information, including troubleshooting tips, frequently asked questions, and examples for both requests and responses.