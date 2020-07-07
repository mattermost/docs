Configure SAML with Okta
========================

The following process provides steps to configure SAML 2.0 with Okta for Mattermost.

.. contents::
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst

Set Up a Connection App for Mattermost SSO
------------------------------------------

1. Sign into Okta as an administrator.

2. Switch to the **Classic UI**, using the drop-down in the upper left.

3. Go to **Admin Dashboard > Applications > Add Application**.

4. Click **Create New App** and choose **SAML 2.0** as the Sign on method.

	.. image:: ../../source/images/okta_1_new_app.PNG

5. Enter **General Settings** for the application, including **App name** and **App logo** (optional). It's recommended to display the application icon to users, including in the Okta Mobile app.

  If you’d like to use a Mattermost logo for the application, you can download one `from our page <http://www.mattermost.org/brand-guidelines/>`__.

	.. image:: ../../source/images/okta_2_general_settings.PNG

6. Enter **SAML Settings**, including:
 - **Single sign on URL:** ``https://<your-mattermost-url>/login/sso/saml`` where ``https://<your-mattermost-url>`` should typically match the `Mattermost Site URL <https://docs.mattermost.com/administration/config-settings.html#site-url>`__.
 - **Audience URI:** For instance, ``mattermost``
 - **Name ID format:** ``unspecified``
 - **Application username:** ``Email``

	.. image:: ../../source/images/okta_3_initial_saml_settings.PNG

7.  To set up encryption for your SAML connection select **Show Advanced Settings**.

	.. image:: ../../source/images/okta_4_initial_saml_settings.PNG

8. Set **Assertion Encryption** as **Encrypted** and upload the Service Provider Public Certificate you generated in step 2 to the **Encryption Certificate** field.

	.. image:: ../../source/images/okta_5_advanced_saml_settings.PNG

9. Enter attribute statements, which will be used to map attributes between Okta and Mattermost. For more information on which attributes are configurable, see our :ref:`documentation on SAML configuration settings <saml-enterprise>`. Email and username attributes are required. For Mattermost servers running 3.3 and earlier, first name and last name attributes are also required.

	.. image:: ../../source/images/okta_6_attribute_statements.PNG

10. Click **Next**. Then, set Okta support parameters for the application. Recommended settings:
 - **I’m an Okta customer adding an internal app**
 - **This is an internal app that we have created**

	.. image:: ../../source/images/okta_7_support_configuration.PNG

11. Click **Finish**. On the next screen, click the **Sign On** tab and click **View Setup Instructions**.
  11.1 Select the **Identity Provider metadata** link and copy the link from the browser URL box. This will be used during the SAML configuration steps in the next section. 

	.. image:: ../../source/images/okta_8_view_instructions.PNG

12. Take note of **Identity Provider Single Sign-On URL** (also known as **SAML SSO URL**), and the Identity Provider Issuer, as both may be needed to configure SAML for Mattermost. Additionally, ensure you download the X.509 Certificate file and save it. You may need to upload it to Mattermost in a later step.

	.. image:: ../../source/images/okta_9_view_instructions.PNG

Configure SAML Sign-in for Mattermost
--------------------------------------

Start Mattermost server and sign into Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**, and paste the copied Identity Provider Metadata URL in the **Identity Provider Metadata URL** field, then select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer URL** fields automatically and the Identity Provider Public Certificate is also downloaded from the server and set locally. 

Alternatively you can enter the following fields manually:
 - **SAML SSO URL:** ``Identity Provider Single Sign-On URL`` from Okta, specified earlier.
 - **Identity Provider Issuer URL:** ``Identity Provider Issuer`` from Okta, specified earlier.
 - **Identity Provider Public Certificate:** X.509 Public Certificate file you downloaded from Okta earlier.
 
	.. image:: ../../source/images/okta_10_mattermost_basics.PNG

2. Configure Mattermost to verify the signature. The **Service Provider Login URL** is the ``Single sign on URL`` you specified in Okta earlier.

	.. image:: ../../source/images/okta_11_mattermost_verification.PNG

3. Enable encryption based on the parameters provided earlier.

	.. image:: ../../source/images/okta_12_mattermost_encryption.PNG

4. Configure Mattermost to sign SAML requests using the Service Provider Private Key.

5. Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email and username are required and should match the values you entered in Okta earlier. See :ref:`documentation on SAML configuration settings <saml-enterprise>` for more detail.

For Mattermost servers running 3.3 and earlier, the first name and last name attributes are also required fields.

	.. image:: ../../source/images/okta_13_mattermost_attributes.PNG

6. (Optional) Customize the login button text.

	.. image:: ../../source/images/okta_14_mattermost_login_button.PNG

7. Click **Save**.

8. (Optional) If you configured First Name Attribute and Last Name Attribute, go to **System Console** > **Site Configuration** > **Users and Teams** (or **System Console > General > Users and Teams** in versions prior to 5.12) and set **Teammate Name Display** to *Show first and last name*. This is recommended for a better user experience.

Once complete, and to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It's also recommended to post an announcement for your users to explain how the migration will work.

You may also configure SAML for Okta by editing ``config.json`` to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-ldapsync.rst

.. include:: sso-saml-faq.rst
