Configure SAML with OneLogin
=============================

The following process provides steps to configure SAML with OneLogin for Mattermost.

.. contents::
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst

Create a OneLogin connection app for Mattermost SSO
---------------------------------------------------

1. Add a SAML test connector app.
  a. Sign into OneLogin as an administrator.
  b. Go to **Apps > Add Apps**.
  c. Search for "SAML Test Connector" and choose **SAML Test Connector (IdP) w/encrypt**.

  .. image:: ../../source/images/onelogin_1_new_app.png

  d. In the **Display Name** field, enter a name for the application, and optionally upload an app icon. You can use the Mattermost logo for the icon, which you can download from `Branding Guidelines <http://www.mattermost.org/brand-guidelines/>`_ page.

  .. image:: ../../source/images/onelogin_2_basic_configuration.png

  e. Make sure that the **Visible in portal** option is enabled.
  f. Click **Save**.

2. Configure the app.
  a. Click the **Configuration** tab and enter the following values:
    - **Recipient**: ``https://<your-mattermost-url>/login/sso/saml``
    - **ACS (Consumer) URL**: ``https://<your-mattermost-url>/login/sso/saml``
    - **ACS (Consumer) URL Validator**: ``https:\/\/<your-mattermost-url>\/login\/sso\/saml``

  .. image:: ../../source/images/onelogin_3_configuration_1.png

  b. Paste the Public Key that you generated earlier into the **SAML Encryption** field.

  .. image:: ../../source/images/onelogin_4_configuration_2.png

  c. Click **Save**.

3. Enter the attribute parameters.

  Attribute parameters map attributes between OneLogin and Mattermost. For more information on which attributes are configurable, see our :ref:`documentation on SAML configuration settings <saml-enterprise>`.

  *Email* and *Username* attributes are required. For Mattermost servers running version 3.3 and earlier, *FirstName* and *LastName* attributes are also required.

  a. Click the **Parameters** tab.
  b. Click **Add Parameter**.

  .. image:: ../../source/images/onelogin_5_parameters_add.png

  c. In the **Field name** field, enter an attribute parameter such as ``Email``.
  d. Select the **Include in SAML assertion** checkbox.
  e. Click **Save**

  .. image:: ../../source/images/onelogin_6_parameters_add_2.png

  f. Click **Edit**.
  g. In the **Value** field, select the OneLogin value that corresponds to the attribute parameter.

  .. image:: ../../source/images/onelogin_7_parameters_add_3.png

  h. Repeat steps b through g to add the *Username* attribute and any other attributes that you need.

    After you've added all the attributes you want to use, the parameter list should look similar to the following image:

    .. image:: ../../source/images/onelogin_8_parameters_add_4.png

4. Copy the SSO information.
  a. Click the **SSO** tab.
  b. Copy the values in the **Issuer URL** and **SAML 2.0 Endpoint (HTTP)** fields and save them for use later.

  .. image:: ../../source/images/onelogin_9_sso.png

  c. Click **View Details** to view the X.509 certificate.
  d. Make sure that the **X.509 PEM** option is selected in the drop-down.

  .. image:: ../../source/images/onelogin_10_sso_certificate.png

  e. Click **DOWNLOAD** and save the file in a convenient location for use later.
5. Save all your changes.

Configure SAML for Mattermost
-----------------------------

1. Sign into Mattermost as a System Administrator.
2. Go to **System Console > Authentication > SAML**.
  a. In the **SAML SSO URL** field, paste the value for the OneLogin *SAML 2.0 Endpoint (HTTP)* that you copied earlier.
  b. In the **Identity Provider Issuer URL** field, paste the value for the OneLogin *Issuer URL* that you copied earlier.
  c. In the **Identity Provider Public Certificate** field, upload the OneLogin X.509 PEM certificate file that you downloaded earlier.

  .. image:: ../../source/images/okta_10_mattermost_basics.png

3. (Optional) Configure Mattermost to verify the signature.
  a. In the **Verify Signature** field, click **True**.
  b. In the **Service Provider Login URL**, enter ``https//<your-mattermost-url>/login/sso/saml``

  .. image:: ../../source/images/okta_11_mattermost_verification.png

4. Enable encryption.
  a. In the **Enable Encryption** field, click **True**.
  b. In the **Service Provider Private Key** field, upload the private key that you generated earlier.
  c. In the **Service Provider Public Certificate** field, upload the public key that you generated earlier.

  .. image:: ../../source/images/okta_12_mattermost_encryption.png

5. Set attributes for the SAML Assertions, which are used for updating user information in Mattermost.

  The **Email Atttribute** field and the **Username Attribute** field are required, and should match the values that you entered earlier when you configured the SAML Test Connector on OneLogin.

  For Mattermost servers running version 3.3 and earlier, *FirstName* and *LastName* attributes are also required.

  .. image:: ../../source/images/okta_13_mattermost_attributes.png

6. (Optional) Customize the login button text.

7. Click **Save**.

To confirm that SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It is also recommended to post an announcement about how the migration will work to users.

You can also configure SAML for OneLogin by editing ``config.json`` to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-troubleshooting.rst
