Configure SAML with Microsoft Entra ID
========================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

This page provides guidance on configuring SAML with Microsoft Entra ID for Mattermost. 

.. tip::
  
  - Need to configure Entra ID for **OpenID Connect** authentication instead? See the :doc:`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>` documentation for details.
  - See the encryption options documentation for details on what :ref:`encryption methods <deployment-guide/encryption-options:saml encryption support>` Mattermost supports for SAML.

.. include:: sso-saml-before-you-begin.rst
	:start-after: :nosearch:

Prerequisites
-------------

* A Microsoft Entra tenant containing applicable user data.
* A verified custom domain for your tenant. See Microsoft's `Add your custom domain name to your tenant <https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain>`__ documentation for details.
* A Microsoft Entra ID P1 or P2 license.
* An account with at least the **Application Administrator** role in your Entra tenant.

Set up an enterprise app for Mattermost SSO in Entra ID
--------------------------------------------------------

1. Sign in to the `Microsoft Entra admin center <https://entra.microsoft.com>`__ with an account that has at least the **Application Administrator** role.
2. In the left navigation menu, select **Entra ID > Enterprise applications**.
3. Select **+ New application**.
4. Select **+ Create your own application**.
5. In the **What's the name of your app?** field, enter **Mattermost**.
6. Under **What are you looking to do with your application?**, select **Integrate any other application you don't find in the gallery (Non-gallery)**.
7. Select **Create**. Entra provisions the application; this may take a few seconds.
8. In the **Mattermost** enterprise application settings, select **Manage > Users and groups** to assign users and/or groups to the application, **or** select **Manage > Properties**, set **Assignment required?** to **No**, then select **Save**.
9. In the **Mattermost** enterprise application settings, select **Manage > Single sign-on**, then select **SAML** under **Select a single sign-on method**.
10. Select **Edit** in the **Basic SAML Configuration** section, then set the fields below and select **Save**:

   - **Identifier (Entity ID)**: ``https://<your-mattermost-url>``
   - **Reply URL (Assertion Consumer Service URL)**: ``https://<your-mattermost-url>/login/sso/saml``
   - **Sign on URL**: ``https://<your-mattermost-url>/login``

11. Select **Edit** in the **Attributes & Claims** section, then configure the required claim and additional claims as described below.

    **How Entra claims map to Mattermost**

    The SAML assertion Entra sends to Mattermost contains a set of *claims* — name/value pairs describing the user. Mattermost reads these claims based on the attribute names you configure in **System Console > Authentication > SAML 2.0 > Attributes** (for example, **Email Attribute**, **Username Attribute**, **First Name Attribute**).

    The **Claim name** you set in Entra must match the value you enter in the corresponding Mattermost attribute field exactly, character for character. The **Value** (also called **Source attribute**) tells Entra which user property to send — for example, ``user.mail`` sends the user's email address.

    a. **Required claim — Unique User Identifier (Name ID)**

       Set the **Name identifier format** and **Source attribute** values as required for your environment. The Name ID is part of the SAML assertion, but Mattermost account binding is controlled by the **Id Attribute (SAML)** setting if you configure it, or by email otherwise. If you want immutable user binding in Mattermost, add a separate ``Id`` claim under **Additional claims** and set its **Value** (source attribute) to an immutable Entra attribute such as ``user.objectid``. ``user.userprincipalname`` is also a common choice for Name ID when a human-readable identifier is preferred, with the trade-off that renames in Entra can orphan the corresponding Mattermost account if you rely on it for identity matching.

    b. **Additional claims**

       By default, Entra populates this section with four claims using the ``http://schemas.xmlsoap.org/ws/2005/05/identity/claims/...`` namespace. These work, but we recommend replacing them with short, readable names that match the attribute fields in Mattermost. To edit a claim, select it, update the **Name** field (and clear the **Namespace** field), then save.

       The following claim configuration covers a typical Mattermost setup:

       .. list-table::
          :header-rows: 1
          :widths: 30 25 45

          * - Mattermost attribute field
            - Entra claim name
            - Entra source attribute
          * - Email Attribute
            - ``email``
            - ``user.mail``
          * - Username Attribute
            - ``username``
            - ``user.mailnickname``
          * - First Name Attribute
            - ``firstname``
            - ``user.givenname``
          * - Last Name Attribute
            - ``lastname``
            - ``user.surname``
          * - Position Attribute
            - ``position``
            - ``user.jobtitle``

       .. note::
          Use ``user.mailnickname`` rather than ``user.userprincipalname`` as the source for the username claim. The user principal name is typically formatted as an email address (``user@domain.com``), but Mattermost usernames cannot contain the ``@`` character, so SAML logins using ``user.userprincipalname`` will fail. The mail nickname is the local part of the email address (the portion before ``@``) and maps cleanly to a valid Mattermost username.

          If your organization doesn't populate ``mailnickname`` consistently, another option is a custom Entra attribute or a transformation that strips the domain from the UPN.

       After editing, your **Attributes & Claims** page should look similar to the screenshot below:

       .. image:: ../../images/entra-attributes-and-claims.png
          :alt: Entra Attributes & Claims page showing simplified claim names
          :width: 100%

       The **Guest**, **Admin**, **Nickname**, and **Preferred Language** attributes are also configurable in Mattermost if you want to drive them from Entra. Use the same pattern: pick a short claim name in Entra, set its source attribute, and enter the matching claim name in the corresponding Mattermost attribute field.

12. Select **Edit** in the **SAML Certificates** section. Select **Sign SAML response and assertion** for **Signing Option** and **SHA-256** for **Signing Algorithm**, then select **Save**.
13. Select the **Certificate (Base64)** Download link in the **SAML Certificates** section. This is the **Identity Provider Public Certificate** to be uploaded to Mattermost.
14. In the **Mattermost** enterprise application settings, select **Security > Token encryption**. Select **Import Certificate** to import the Service Provider certificate. If you used the Bash script referenced in the **Before you begin** section, this is the ``mattermost-x509.crt`` file. The Import dialog says to upload a certificate with a file extension ``.cer``, but ``.crt`` files are also accepted. Upload the file then select **Add**.
15. Select the ``...`` to the right of the imported certificate details, select **Activate token encryption certificate**, then select **Yes** to activate.
16. Copy the **Tenant ID** for use in the Mattermost **SAML 2.0** URL settings.

    .. note::
       Entra exposes three different GUIDs during this setup, and it's easy to confuse them. The **Tenant ID** identifies your entire Entra directory, while the **Application ID** and **Object ID** (visible on the enterprise application's **Properties** page) identify the Mattermost SAML application within that directory. Mattermost uses the Tenant ID and Application ID; the Object ID is not used.

    To find the Tenant ID, select **Entra ID** from the admin center home, then locate the **Tenant ID** value in the **Basic information** panel on the **Overview** page.

    .. image:: ../../images/entra-tenant-id.png
       :alt: Where to find the Tenant ID
       :width: 100%

17. Copy the **Application ID** for use in the **Identity Provider Metadata URL** setting in the Mattermost **SAML 2.0** settings.

    To find the Application ID, select **Entra ID > Enterprise applications** from the left navigation menu, select the **Mattermost** application, then copy the **Application ID** from the **Properties** page (shown alongside the Object ID, which is not needed).

Configure SAML Sign-On for Mattermost
--------------------------------------

1. In the Mattermost **System Console**, select **Authentication > SAML 2.0**.
2. Set **Enable Login With SAML 2.0** to **True**.
3. Set **Identity Provider Metadata URL**: ``https://login.microsoftonline.com/<your-tenant-id>/federationmetadata/2007-06/federationmetadata.xml?appid=<your-app-id>``
4. Select **Get SAML Metadata From IdP** to verify that the SAML metadata can be retrieved successfully.
5. Set **SAML SSO URL**: ``https://login.microsoftonline.com/<your-tenant-id>/saml2``
6. Set **Identity Provider Issuer URL** (trailing slash is required): ``https://sts.windows.net/<your-tenant-id>/``
7. Choose the **Identity Provider Public Certificate** file from step 13 of **Set up an enterprise app for Mattermost SSO in Entra ID** then upload.
8. Set **Verify Signature** to **True**.
9. Set **Service Provider Login URL**: ``https://<your-mattermost-url>/login/sso/saml``
10. Set **Service Provider Identifier**: ``https://<your-mattermost-url>``
11. Set **Enable Encryption** to **True**.
12. Choose your **Service Provider Private Key** file then upload. If you used the Bash script referenced in the **Before you begin** section, this is the ``mattermost-x509.key`` file.
13. Choose your **Service Provider Public Certificate** then upload. If you used the Bash script referenced in the **Before you begin** section, this is the ``mattermost-x509.crt`` file.
14. Set **Sign Request** to suit your environment. The **Signature Algorithm** must match the algorithm set in Entra ID (**RSAwithSHA256** is recommended). 

.. note:: 

  The **Test single sign-on with Mattermost SAML** tool in Microsoft Entra ID does not sign the request even if **Sign Request** is set to **True** in Mattermost. Depending on your security settings and key length, the Entra ID testing tool may successfully sign in while an actual sign in request from your Mattermost login page results in the error **AADSTS90015: Requested query string is too long.** since Entra ID handles the initial request with an HTTP GET redirect rather than HTTP POST.

15. Set attribute settings to match the attributes configured in step 11 of the **Set up an enterprise app for Mattermost SSO in Entra ID** section.
16. Set the **Login Button Text** to suit your environment.
17. Select the **Save** button.

.. include:: sso-saml-ldapsync.rst
	:start-after: :nosearch:

.. include:: sso-saml-faq.rst
	:start-after: :nosearch:
