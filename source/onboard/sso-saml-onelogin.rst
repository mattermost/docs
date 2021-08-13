Configure SAML with OneLogin
=============================

The following process provides steps to configure SAML 2.0 with OneLogin for Mattermost.

.. contents::
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst

Create a OneLogin Connection App for Mattermost SSO
---------------------------------------------------

1. Add a SAML test connector app.

  a. Sign in to OneLogin as an administrator.
  b. Go to **Apps > Add Apps**.
  c. Search for "SAML Test Connector", then select **SAML Test Connector (Advanced)**.

  .. image:: ../../source/images/onelogin_1_new_app.png

  d. In the **Display Name** field, enter a name for the application, then optionally upload an app icon. You can use the Mattermost logo for the icon, which you can download from `Branding Guidelines <https://mattermost.org/brand-guidelines/>`__ page.

  .. image:: ../../source/images/onelogin_2_basic_configuration.png

  e. Make sure that the **Visible in portal** option is enabled.
  f. Select **Save**.

2. Configure the app.

  a. Select the **Configuration** tab, then enter the following values:

    - **RelayState**: leave blank
    - **Audience**: leave blank
    - **Recipient**: ``https://<your-mattermost-url>/login/sso/saml`` where ``https://<your-mattermost-url>`` should typically match the `Mattermost Site URL <https://docs.mattermost.com/administration/config-settings.html#site-url>`__.
    - **ACS (Consumer) URL Validator**: ``https:\/\/<your-mattermost-url>\/login\/sso\/saml``
    - **ACS (Consumer) URL**: ``https://<your-mattermost-url>/login/sso/saml``

  .. image:: ../../source/images/onelogin_3_configuration_1.png
  
  b. In System Console,  `enable encryption <https://docs.mattermost.com/administration/prev-config-settings.html#enable-encryption>`__, then click **Save**. You're redirected to the **Info** tab. From there, select the **Configuration** tab to access the **SAML Encryption** field.

  c. Paste the Public Key that you generated earlier into the **SAML Encryption** field at the bottom of the page. This field displays in OneLogin only when encryption is enabled in Mattermost.

  .. image:: ../../source/images/onelogin_4_configuration_2.png

  d. Select **Save**.

3. Enter the attribute parameters. The following attributes are recommended:

+----------------+-------------+
| Name           | Value       | 
+================+=============+
| ID             | UUID        |
+----------------+-------------+
| Email          | Email       |  
+----------------+-------------+
| FirstName      | First Name  |  
+----------------+-------------+
| LastName       | Last Name   |  
+----------------+-------------+
| Name ID value  | Email       |  
+----------------+-------------+
| Username       | Username    |
+----------------+-------------+

  Attribute parameters map attributes between OneLogin and Mattermost. For more information on which attributes are configurable, see our :ref:`documentation on SAML configuration settings <saml-enterprise>`.

  *Email* attributes are required. For Mattermost servers running version 3.3 and earlier, ``FirstName`` and ``LastName`` attributes are also required.

  a. Select the **Parameters** tab.
  b. Select **Add Parameter**.

  .. image:: ../../source/images/onelogin_5_parameters_add.png

  c. In the **Field name** field, enter an attribute parameter such as ``Email``.
  d. Select the **Include in SAML assertion** checkbox.
  e. Select **Save**.

  .. image:: ../../source/images/onelogin_6_parameters_add_2.png

  f. Select **Edit**.
  g. In the **Value** field, select the OneLogin value that corresponds to the attribute parameter.

  .. image:: ../../source/images/onelogin_7_parameters_add_3.png

  h. Repeat the steps above to add any other attributes that you need. After you've added all the attributes you want to use, the parameter list should look similar to the following image:

    .. image:: ../../source/images/onelogin_8_parameters_add_4.png

4. Copy the SSO information.

  a. Select the **SSO** tab.
  b. Copy the values in the **Issuer URL** and **SAML 2.0 Endpoint (HTTP)** fields, then save them for later use.

  .. image:: ../../source/images/onelogin_9_sso.png

  c. Select **View Details** to view the X.509 certificate.
  d. Make sure that the **X.509 PEM** option is selected in the drop-down.

  .. image:: ../../source/images/onelogin_10_sso_certificate.png

  e. Select **DOWNLOAD**, then save the file in a convenient location for later use.

5. Save all your changes.

Configure SAML Sign-in for Mattermost
--------------------------------------

1. Start the Mattermost server, then sign into Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**.

  a. Enter the **OneLogin Issuer URL** into the **Identity Provider Metadata URL** field.
  b. Select **Get SAML Metadata from IdP** to download the metadata.

2. Configure Mattermost to verify the signature.

  a. In the **Verify Signature** field, select **True**.
  b. In the **Service Provider Login URL**, enter ``https//<your-mattermost-url>/login/sso/saml``.

  .. image:: ../../source/images/okta_11_mattermost_verification.png

3. Configure Mattermost to sign SAML requests using the Service Provider Private Key.

4. Enable encryption.

  a. In the **Enable Encryption** field, select **True**.
  b. In the **Service Provider Private Key** field, upload the private key that you generated earlier.
  c. In the **Service Provider Public Certificate** field, upload the public key that you generated earlier.

  .. image:: ../../source/images/okta_12_mattermost_encryption.png

5. Set attributes for the SAML Assertions, which are used for updating user information in Mattermost.

  The **Email Atttribute** field and the **Username Attribute** field are required, and should match the values that you entered earlier when you configured the SAML Test Connector on OneLogin.

  For Mattermost servers running version 3.3 and earlier, ``FirstName`` and ``LastName`` attributes are also required.

  .. image:: ../../source/images/okta_13_mattermost_attributes.png

6. (Optional) Customize the login button text.

7. Select **Save**.

8. (Optional) If you configured ``First Name`` Attribute and ``Last Name`` Attribute, go to **System Console > Site Configuration > Users and Teams**, then set **Teammate Name Display** to **Show first and last name**. This is recommended for a better user experience.

To confirm that SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO**, then sign in with your SAML credentials to complete the switch.

We also recommend that you post an announcement to your users detailing how the migration will work.

You can also configure SAML for OneLogin by editing the ``config.json`` file to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-ldapsync.rst

.. include:: sso-saml-faq.rst
