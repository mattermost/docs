:nosearch:

SAML Single-Sign-On: technical documentation
============================================

Security Assertion Markup Language (SAML) is an open standard that allows identity providers (IdP), like OneLogin, to pass authorization credentials to service providers (SP), like Mattermost.

In simpler terms, it means you can use one set of credentials to log in to many different sites. With a SAML identity provider account, you can log in to Mattermost and other sites securely with the same account. The main benefit is that it helps administrators centralize user management by controlling which sites users have access to with their SAML identity provider credentials.

Mattermost supports using a single metadata URL to retrieve configuration information for the Identity Provider using your Single Sign-on URL to generate an IdP metadata URL. The IdP metadata XML file contains the IdP certificate, the entity ID, the redirect URL, and the logout URL. 

Using this URL populates the SAML SSO URL and the Identity Provider Issuer URL fields in the configuration process automatically and the Identity Provider Public Certificate is also downloaded from the server and set locally.

.. contents::
  :backlinks: top
  :local:

SAML providers
--------------

**Identity Providers (IdP):** An identity provider performs the authentication. When a user clicks to log in, the identity provider confirms who the user is, and sends data to the service provider with the proper authorization to access the site.

*Examples*: OneLogin, Okta, Microsoft Active Directory (ADFS) or Azure.

**Service Providers (SP):** A service provider gets authentication and authorization information from an IdP. Once received, it gives the user access to the system and logs the user in.

*Examples*: Mattermost, Zendesk, Zoom, Salesforce.

SAML request (AuthNRequest)
---------------------------

When Mattermost initiates an SP-initiated SAML request flow, it generates a **HTTP-Redirect** binding request to the IdP that contains an XML payload as a base64 string:

.. code-block:: none

 bM441nuRIzAjKeMM8RhegMFjZ4L4xPBHhAfHYqgnYDQnSxC++Qn5IocWuzuBGz7JQmT9C57nxjxgbFIatiqUCQN17aYrLn/mWE09C5mJMYlcV68ibEkbR/JKUQ+2u/N+mSD4/C/QvFvuB6BcJaXaz0h7NwGhHROUte6MoGJKMPE=

AuthNRequests can also be signed by Mattermost in which case the XML payload is similar to:

.. code-block:: XML

  <samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:samlsig="https://www.w3.org/2000/09/xmldsig#" ID="_u5mpjadp1fdozfih4cj8ap4brh" Version="2.0" ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" AssertionConsumerServiceURL="http://localhost:8065/login/sso/saml" IssueInstant="2019-06-08T16:00:31Z">
      <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">https://www.okta.com/exkoxukx1D8OIfY03356</saml:Issuer>
      <samlsig:Signature Id="Signature1">
          <samlsig:SignedInfo>
              <samlsig:CanonicalizationMethod Algorithm="https://www.w3.org/2001/10/xml-exc-c14n#"></samlsig:CanonicalizationMethod>
              <samlsig:SignatureMethod Algorithm="https://www.w3.org/2000/09/xmldsig#rsa-sha1"></samlsig:SignatureMethod>
              <samlsig:Reference URI="#_u5mpjadp1fdozfih4cj8ap4brh">
                  <samlsig:Transforms>
                      <samlsig:Transform Algorithm="https://www.w3.org/2000/09/xmldsig#enveloped-signature"></samlsig:Transform>
                  </samlsig:Transforms>
                  <samlsig:DigestMethod Algorithm="https://www.w3.org/2000/09/xmldsig#sha1"></samlsig:DigestMethod>
                  <samlsig:DigestValue></samlsig:DigestValue>
              </samlsig:Reference>
          </samlsig:SignedInfo>
          <samlsig:SignatureValue></samlsig:SignatureValue>
          <samlsig:KeyInfo>
              <samlsig:X509Data>
                  <samlsig:X509Certificate>MIIFmzCCA4OgAwIBAgIJAIusvV3gZIwiMA0GCSqGSIb3DQEBCwUAMGIxCzAJBgNVBAYTAlVTMRIwEAYDVQQHDAlQYWxvIEFsdG8xEzARBgNVBAoMCk1hdHRlcm1vc3QxDzANBgNVBAsMBkRldk9wczEZMBcGA1UEAwwQYmFzZS5leGFtcGxlLmNvbTAeFw0xOTA2MDcxMjQ0MTdaFw0yOTA2MDQxMjQ0MTdaMGIxCzAJBgNVBAYTAlVTMRIwEAYDVQQHDAlQYWxvIEFsdG8xEzARBgNVBAoMCk1hdHRlcm1vc3QxDzANBgNVBAsMBkRldk9wczEZMBcGA1UEAwwQYmFzZS5leGFtcGxlLmNvbTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALAfDj+RyByszTOPRL4b+cilNF/3PB1I0CG3TNzgllgy5CwRGHLKn5/t8rPsJoWLKOUGenzVdXWuoVi3jyl5FZ1N60CBbXfmSWk20dSIkcYCcYEgs1BTBqKKYFw2dV4M0oppzNtlq7A0Glpg/gpaR/2TXEPAhOsUfORC2qAdJt9ev0AQjp5V0TkIKMZz8oo33Coi38TG5r/LG+ihRbpWzO7j9Rc2S5I6bczvG4wOg7nVKG+B5XBvuU9PjSqgxpd/F/fYf+ggAEru58E+VM4veCRV8vSPbBqDG4FMPV6DiA+tH/70n6zuPCS3soxX00kjKtP80QD6UgzvM2NN7PHiNlf0Zj6VCU3VdjEnypg7dzlHJuyyaAaTD5nSfkecamEoJpq7kaUB7uTmBHELRUhOOy24f54HnP72vnxicZL8cWsOkJwQAqIGzBxQ7J0uX4Os71WrV2YIur8QVk6KN6MBPxfiCh3xO/R+cycgx0aMrWZoyzOzP7NCTM5MNE41C48xeGviyCtUID4xiBow+xo6IDUaiCoUVJhz579ore8ic70a19DD0qHy4SpBvrUwCO54kvkgn6HjYlLC/k8nFM9F9W9wVAQD/QwIjd7EtLZLGgbU61Jv3q4kZxxq270hogCRY0lmI3RxkedGHhetF7kaizrikW5zJQEeido/ir37HhX5AgMBAAGjVDBSMBIGA1UdEwEB/wQIMAYBAf8CAQAwPAYDVR0RBDUwM4IQbG9ncy5leGFtcGxlLmNvbYITbWV0cmljcy5leGFtcGxlLmNvbYcEwKgAAYcEfwAAATANBgkqhkiG9w0BAQsFAAOCAgEAH1O91BABHXZjrU7v1OwG+GbU/4TYZqBXXNxax++OFSRCkEEoNKGg49R6J7lY4lrm12zBlw+oGSyjIOerzi39/dcxDkKpzyhGvEN4mExbDlybmdCVrHPeWgZl7uwqn4Bj1xiu97M6eMthgxJE7KVNDGDHthGL0/fTlONIh3qS7Far33hLHJJKy3+lC1MDB8cNltV3mf/ctHCx5Wa0bfZId0MJgd/seP0WU1HCf3kIxhnhsnOYs32xu7EGiM4/lgnquVd/q/f99ueSaDSHrep373/w2ce9iF3U0qcLd2iP8ayF/daGeW1dVPL9R10Oe4BpRjMkjlLwhZdjJeKSg9GBa2GXUEn1Ru9vpSw/C10no3Qx/6ZHweYbSmJ6hBg4T0nDBp6iVS1eQULNXxDuDWb26U0ESOO5jK8ATywuc45o0bqdvD1XOrGYGfGnofx7ofRWwKHWfltvxurnbsyo2vH6nM6K41K2DpVdyQOKAGvKe/oCWfdi+WyBQJGWcIp2OTC1XyWHv7JsY3lo04+islkHEcqJyd8Rf8GWmRHdXz0WzGiZbxWzAuvRRWnzM31VAws8kQBHTBwIJlJoGX4AXfEvPi+NTxkntf8cQdJucK9ZZbP4ycXHULO4LneyJoJ9Q7nxX11xWv7BDWxxclOXy6tyUkg9Fjb7pQ/HCVvGhRzilVU=</samlsig:X509Certificate>
              </samlsig:X509Data>
          </samlsig:KeyInfo>
      </samlsig:Signature>
  </samlp:AuthnRequest>

SAML responses
--------------

There are different types of SAML responses sent by the IdP to the SP. The response contains the Assertion with the NameID and attributes of a user. Below is a table of the different types of responses. Each response type is fully supported except when the SAML assertion is signed while the SAML response itself is not:

.. csv-table::
    :header: "Signed SAML Response", "Signed SAML Assertion", "Encrypted SAML Assertion", "Supported by Mattermost"

    "Yes", "Yes", "Yes", "Yes"
    "Yes", "Yes", "No", "Yes"
    "Yes", "No", "Yes", "Yes"
    "Yes", "No", "No", "Yes"
    "No", "Yes", "Yes", "Partially, validation of assertion signature not supported"
    "No", "Yes", "No", "Partially, validation of assertion signature not supported"
    "No", "No", "Yes", "Yes"
    "No", "No", "No", "Yes"

For example XML responses for each type, see the `OneLogin SAML response examples <https://www.samltool.com/generic_sso_res.php>`_.

Technical description of SAML synchronization with AD/LDAP
----------------------------------------------------------

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
--------------------------

How can I obtain a SAML metadata XML file consumed by Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can obtain the XML file by calling the Mattermost RESTful API endpoint at ``/api/v4/saml/metadata``. For other useful SAML API calls, see the `API reference <https://api.mattermost.com/#tag/SAML>`_.

Can I update user attributes using the API?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. When Mattermost is configured to use SAML for user authentication, the following user attribute changes can't be made through the API:  first name, last name, position, nickname, email, profile image, or username. SAML must be the authoritative source for these user attributes.
