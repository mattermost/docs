SAML Single-Sign-On (E20)
-------------------------

Overview
~~~~~~~~

SAML Single-Sign-On integration offers the following benefits:

-  **Single-sign-on.** Users can sign-in to Mattermost with their SAML
   credentials.
-  **Centralized identity management.** Mattermost accounts can display
   user information from SAML, such as first and last name, email and
   username.
-  **Automatic account provisioning.** New Mattermost user accounts are
   automatically created the first time a user signs in with their SAML
   credentials on the Mattermost server.

Note that the standard SAML specification doesn't support a "lazy sync"
option like AD/LDAP - instead, the SAML system is called every time the
user authenticates in to Mattermost. Therefore, a user who has been
deactivated in their identity provider will have access to Mattermost
until their session expires and they need to log in again, or until
`they are also deactivated in
Mattermost <https://docs.mattermost.com/deployment/on-boarding.html#common-tasks>`__.

Mattermost officially supports Okta and Microsoft ADFS as the identity
providers (IDPs), please see links below for more details on how to
configure SAML with Okta and Microsoft ADFS. If you'd like, you may also
try configuring SAML for a custom IDP.

`Configure SAML with Okta <http://docs.mattermost.com/deployment/sso-saml-okta.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Configure SAML with Microsoft ADFS <http://docs.mattermost.com/deployment/sso-saml-adfs.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pre-installation
~~~~~~~~~~~~~~~~

Before configuring SAML with Okta or Microsoft ADFS, make sure you have
the `XML Security
Library <https://www.aleksey.com/xmlsec/download.html>`__ installed on
your Mattermost instance. The XML Security Library is usually included
as part of Debian GNU/Linux.

Also confirm if the ``xmlsec1-openssl`` library was successfully
installed. If not, run - ``apt-get install libxmlsec1-openssl`` on
Ubuntu - ``yum install xmlsec1-openssl`` on RHEL

Troubleshooting
^^^^^^^^^^^^^^^

The following are troubleshooting suggestions on common error messages
and issues.

1. System Administrator locks themselves out of the system
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

If the System Administrator is locked out of the system during SAML
configuration process, they can set an existing account to System
Administrator using `a commandline
tool <http://docs.mattermost.com/deployment/on-boarding.html#creating-system-administrator-account-from-commandline>`__.

2. Received error message: ``An account with that username already exists. Please contact your Administrator.``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

This usually means an existing account has another authentication method
enabled. If so, the user should sign in using that method (such as email
and password), then change their sign-in method to SAML via **Account
Settings > Security > Sign-in method**.

This error message can also be received if the ``Username Attribute`` of
their SAML credentials doesn't match the username of their Mattermost
account. If so, the user can update the attribute at their identity
provider (for instance, back to the old value if it had been previously
updated).

3. Received error message: ``An account with that email already exists. Please contact your Administrator.``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

This usually means an existing account has another authentication method
enabled. If so, the user should sign in using that method (such as email
and password), then change their sign-in method to SAML via **Account
Settings > Security > Sign-in method**.

This error message can also be received if the ``Email Attribute`` of
their SAML credentials doesn't match the email address of their
Mattermost account. If so, the user can update the attribute at their
identity provider (for instance, back to the old value if it had been
previously updated).

4. Received error message: ``SAML login was unsuccessful because one of the attributes is incorrect. Please contact your System Administrator.``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Confirm all attributes, including ``Email Attribute`` and
``Username Attribute``, are correct in both the Identity Provider
configuration and in **System Console > SAML**.

5. Unable to switch to SAML authentication successfully
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

First, ensure you have installed the `XML Security
Library <https://www.aleksey.com/xmlsec/download.html>`__ on your
Mattermost instance and that **it is available in your** ``PATH``.

Second, ensure you have completed each step in our guides for
`configuring SAML with
Okta <http://docs.mattermost.com/deployment/sso-saml-okta.html>`__ or
for `configuring SAML with Microsoft
ADFS <http://docs.mattermost.com/deployment/sso-saml-adfs.html>`__.

Lastly, if you are still having trouble with configuration, please post
in our `Troubleshooting
forum <http://www.mattermost.org/troubleshoot/>`__ and we'll be happy to
help with issues during setup.
