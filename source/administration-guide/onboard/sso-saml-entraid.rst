Configure SAML with Microsoft Entra ID
========================================

The following process provides steps to configure SAML with Microsoft Entra ID for Mattermost.

See the encryption options documentation for details on what :ref:`encryption methods <deployment-guide/encryption-options:saml encryption support>` Mattermost supports for SAML.

.. include:: sso-saml-before-you-begin.rst
	:start-after: :nosearch:

Prerequisites
-------------

* A Microsoft Entra tenant containing applicable user data.
* A verified custom domain for your tenant. See Microsoft's `Add your custom domain name to your tenant <https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain>`__ documentation for details.
* A Microsoft Entra ID P1 or P2 license.

Set up an enterprise app for Mattermost SSO in Entra ID
--------------------------------------------------------

1. Log into the Microsoft Azure portal and select the **Microsoft Entra ID** service.
2. In the left menu, select **Manage > Enterprise applications**.
3. Select the **New application** button.
4. In the **Search application** field, search for **Microsoft Entra SAML Toolkit** and select **Microsoft Entra SAML Toolkit**.
5. In the **Name** field, enter **Mattermost SAML** then select the **Create** button.
6. In the **Mattermost SAML** enterprise application settings, select **Manage > Users and Groups** to assign users and/or groups to the application **or** select **Manage > Properties** then set **Assignment required?** to **No** then select **Save**.
7. In the **Mattermost SAML** enterprise application settings, select **Manage > Single sign-on** then select **SAML** under **Select a single sign-on method**.
8. Select **Edit** in the **Basic SAML Configuration section** then set the below fields then select **Save**:

  - **Identity (Entity ID)**: ``https://<your-mattermost-url>``
  - **Reply URL (Assertion Consumer Service URL)**: ``https://<your-mattermost-url>/login/sso/saml``
  - **Sign on URL**: ``https://<your-mattermost-url>/login``

9. Select **Edit** in the **Attributes & Claims** section then set the below attributes:

  a. Set the the **Unique User Identifier (Name ID)** required claim **Name identifier format** and **Source attribute** values as required for your environment. Setting the **Source attribute** to an immutable value such as ``user.objectid`` is recommended.
  b. Edit claim names and namespaces under **Additional claims** to match SAML attribute settings you wish to set in Mattermost. Configurable settings are Email, Username, Id, Guest, Admin, First Name, Last Name, Nickname, Position, and Preferred Language.

10. Select **Edit** in the **SAML Certificates** section. Select **Sign SAML response and assertion** for **Signing Option** and **SHA-256** for **Signing Algorithm** then select **Save**.
11. Select the **Certificate (Base64)** Download link in the **SAML Certificates** section. This is the **Identity Provider Public Certificate** to be uploaded to Mattermost.
12. In the **Mattermost SAML** enterprise application settings, select **Security > Token encryption**. Select **Import Certificate** to import the Service Provider certificate. If you used the Bash script referenced in the **Before you begin** section, this is the ``mattermost-x509.crt`` file. The Import dialog says to upload a certificate with a file extension ``.cer``, but ``.crt`` files are also accepted. Upload the file then select **Add**.
13. Select the ``...`` to the right of the imported certificate details, select **Activate token encryption certificate**, then select **Yes** to activate.
14. On the **Home** page for **Microsoft Entra ID**, select the **Overview** link in the left navigation menu and copy the **Tenant ID** value. The **Tenant ID** will be used in Mattermost **SAML 2.0** URL settings.
15. In the left navigation menu, select **Manage > Enterprise applications**. Select the **Mattermost SAML** application then copy the **Application ID**. The **Application ID** will be used in the **Identity Provider Metadata URL** setting in the Mattermost **SAML 2.0** settings. 

Configure SAML Sign-On for Mattermost
--------------------------------------

1. In the Mattermost **System Console**, select **Authentication > SAML 2.0**.
2. Set **Enable Login With SAML 2.0** to **True**.
3. Set **Identity Provider Metadata URL**: ``https://login.microsoftonline.com/<your-tenant-id>/federationmetadata/2007-06/federationmetadata.xml?appid=<your-app-id>``
4. Select **Get SAML Metadata From IdP** to verify that the SAML metadata can be retrieved successfully.
5. Set **SAML SSO URL**: ``https://login.microsoftonline.com/<your-tenant-id>/saml2``
6. Set **Identity Provider Issuer URL** (trailing slash is required): ``https://sts.windows.net/<your-tenant-id>/``
7. Choose the **Identity Provider Public Certificate** file from step 11 of **Set up an enterprise app for Mattermost SSO in Entra ID** then upload.
8. Set **Verify Signature** to **True**.
9. Set **Service Provider Login URL**: ``https://<your-mattermost-url>/login/sso/saml``
10. Set **Service Provider Identifier**: ``https://<your-mattermost-url>``
11. Set **Enable Encryption** to **True**
12. Choose your **Service Provider Private Key** file then upload.  If you used the Bash script referenced in the **Before you begin** section, this is the ``mattermost-x509.key`` file.
13. Choose your **Service Provider Public Certificate** then upload. If you used the Bash script referenced in the **Before you begin** section, this is the ``mattermost-x509.crt`` file.
14. Set **Sign Request** to suit your environment. The **Signature Algorithm** must match the algorithm set in Entra ID (**RSAwithSHA256** is recommended). 

.. note:: 

  The **Test single sign-on with Mattermost SAML** tool in Microsoft Entra ID does not sign the request even if **Sign Request** is set to **True** in Mattermost. Depending on your security settings and key length, the Entra ID testing tool may successfully sign in while an actual sign in request from your Mattermost login page results in the error **AADSTS90015: Requested query string is too long.** since Entra ID handles the initial request with an HTTP GET redirect rather than HTTP POST.

15. Set attribute settings to match attributes configured in step 9 of the **Set up an enterprise app for Mattermost SSO in Entra ID** section.
16. Set the **Login Button Text** to suit your environment.
17. Select the **Save** button.

.. include:: sso-saml-ldapsync.rst
	:start-after: :nosearch:

.. include:: sso-saml-faq.rst
	:start-after: :nosearch: