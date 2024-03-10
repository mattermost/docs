Configure SAML with OneLogin
=============================

The following process provides steps to configure SAML 2.0 with OneLogin for Mattermost.

.. include:: sso-saml-before-you-begin.rst
  :start-after: :nosearch:

Create a OneLogin connection app for Mattermost SSO
---------------------------------------------------

1. Add a SAML test connector app.

  a. Log in to OneLogin as an administrator.
  b. Go to **Apps > Add Apps**.
  c. Search for "SAML Test Connector", then select **SAML Test Connector (Advanced)**.

  .. image:: ../../source/images/onelogin_1_new_app.png
     :alt: In OneLogin, go to Apps > Add Apps, search for SAML Test Connector, then select the matching result in the list

  d. In the **Display Name** field, enter a name for the application, then optionally upload an app icon. You can use the Mattermost logo for the icon, which you can download from `Branding Guidelines <https://handbook.mattermost.com/operations/operations/publishing/publishing-guidelines/brand-and-visual-design-guidelines>`__ page.

  .. image:: ../../source/images/onelogin_2_basic_configuration.png
     :alt: Enter a display name for the application in the Display Name field. You can optionally upload an app icon. Ensure the Visible in portal option is enabled, and save your OneLogin changes.

  e. Make sure that the **Visible in portal** option is enabled.
  f. Select **Save**.

2. Configure the app.

  a. Select the **Configuration** tab, then enter the following values:

    - **RelayState**: leave blank
    - **Audience**: leave blank
    - **Recipient**: ``https://<your-mattermost-url>/login/sso/saml`` where ``https://<your-mattermost-url>`` should typically match the :ref:`Mattermost Site URL <configure/environment-configuration-settings:site url>`.
    - **ACS (Consumer) URL Validator**: ``https:\/\/<your-mattermost-url>\/login\/sso\/saml``
    - **ACS (Consumer) URL**: ``https://<your-mattermost-url>/login/sso/saml``

  .. image:: ../../source/images/onelogin_3_configuration_1.png
     :alt: In OneLogin, select the Configuration tab to configure the SSO integration with required values.
  
  b. In System Console,  :ref:`enable encryption <configure/authentication-configuration-settings:enable encryption>`, then select **Save**. You're redirected to the **Info** tab. From there, select the **Configuration** tab to access the **SAML Encryption** field.

  c. Paste the Public Key that you generated earlier into the **SAML Encryption** field at the bottom of the page. This field displays in OneLogin only when encryption is enabled in Mattermost.

  .. image:: ../../source/images/onelogin_4_configuration_2.png
     :alt: In the Mattermost System Console, enable encryption and save your changes. When you return to OneLogin, return to the Configuration tab, access the SAML Encryption field, and paste the generated Public Key into the SAML Encryption field. This field isn't visible in OneLogin until encryption is enabled in Mattermost. Save your OneLogin changes.

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
     :alt: In OneLogin, select the Parameters tab, then select Add parameter. Map attribute parameters between OneLogin and Mattermost. Email attributes are required.

  c. In the **Field name** field, enter an attribute parameter such as ``Email``.
  d. Select the **Include in SAML assertion** checkbox.
  e. Select **Save**.

  .. image:: ../../source/images/onelogin_6_parameters_add_2.png
     :alt: For each field you map in OneLogin, ensure the Include in SAML assertion flag is enabled.

  f. Select **Edit**.
  g. In the **Value** field, select the OneLogin value that corresponds to the attribute parameter.

  .. image:: ../../source/images/onelogin_7_parameters_add_3.png
     :alt: For each field you map in OneLogin, select the OneLogin value that corresponds to the attribute parameter.

  h. Repeat the steps above to add any other attributes that you need. After you've added all the attributes you want to use, the parameter list should look similar to the following image:

    .. image:: ../../source/images/onelogin_8_parameters_add_4.png
       :alt: Example of attribute parameters mapped between OneLogin and Mattermost.

4. Copy the SSO information.

  a. Select the **SSO** tab.
  b. Copy the values in the **Issuer URL** and **SAML 2.0 Endpoint (HTTP)** fields, then save them for later use.

  .. image:: ../../source/images/onelogin_9_sso.png
     :alt: In OneLogin, select the SSO tab, copy the Issuer URL and SAML 2.0 Endpoint (HTTP) values to a convenient location. 

  c. Select **View Details** to view the X.509 certificate.
  d. Make sure that the **X.509 PEM** option is selected in the drop-down.

  .. image:: ../../source/images/onelogin_10_sso_certificate.png
     :alt: On the SSO tab in OneLogin, select View Details to access the X.509 certificate. Ensure that the X.509 PEM option is selected. Select Download and save the file in a convenient location.

  e. Select **DOWNLOAD**, then save the file in a convenient location for later use.

5. Save all your changes.

Configure SAML Sign-On for Mattermost
--------------------------------------

1. Start the Mattermost server, then log in to Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**.

  a. Enter the **OneLogin Issuer URL** into the **Identity Provider Metadata URL** field.
  b. Select **Get SAML Metadata from IdP** to download the metadata.

2. Configure Mattermost to verify the signature.

  a. In the **Verify Signature** field, select **True**.
  b. In the **Service Provider Login URL**, enter ``https//<your-mattermost-url>/login/sso/saml``.

  .. image:: ../../source/images/okta_11_mattermost_verification.png
     :alt: On the System Console SAML page, enable the Verify Signature option by setting it to true, then enter your specific Service Provider Login URL based on your Mattermost URL

3. Configure Mattermost to sign SAML requests using the Service Provider Private Key.

4. Enable encryption.

  a. In the **Enable Encryption** field, select **True**.
  b. In the **Service Provider Private Key** field, upload the private key that you generated earlier.
  c. In the **Service Provider Public Certificate** field, upload the public key that you generated earlier.

  .. image:: ../../source/images/okta_12_mattermost_encryption.png
     :alt: On the System Console SAML page, enable encryption, then upload both the private and public generated keys.

5. Set attributes for the SAML Assertions, which are used for updating user information in Mattermost.

  The **Email Atttribute** field and the **Username Attribute** field are required, and should match the values that you entered earlier when you configured the SAML Test Connector on OneLogin.

  For Mattermost servers running version 3.3 and earlier, ``FirstName`` and ``LastName`` attributes are also required.

  .. image:: ../../source/images/okta_13_mattermost_attributes.png
     :alt: On the System Console SAML page, set attributes for the SAML Assertions used to update user information in Mattermost. Both Email Attribute and Username Attribute are required, and should match the values entered when configuring the SAML Test Connector in OneLogin.

6. (Optional) Customize the login button text.

7. Select **Save**.

8. (Optional) If you configured ``First Name`` Attribute and ``Last Name`` Attribute, go to **System Console > Site Configuration > Users and Teams**, then set **Teammate Name Display** to **Show first and last name**. This is recommended for a better user experience.

To confirm that SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication from your profile picture via **Profile > Security > Sign-in Method > Switch to SAML SSO**, then log in with your SAML credentials to complete the switch.

We also recommend that you post an announcement to your users detailing how the migration will work.

You can also configure SAML for OneLogin by editing the ``config.json`` file to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-ldapsync.rst
  :start-after: :nosearch:

.. include:: sso-saml-faq.rst
  :start-after: :nosearch:
