Configure SAML with Okta
========================

The following process provides steps to configure SAML with Okta for Mattermost.

.. contents::
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst

Set up a connection app for Mattermost SSO
------------------------------------------

1. Sign into Okta as an administrator.

2. Go to **Admin Dashboard > Applications > Add Application**.

3. Click **Create New App** and choose ``SAML 2.0`` as the Sign on method.

	.. image:: ../../source/images/okta_1_new_app.PNG

4. Enter **General Settings** for the application, including ``App name`` and ``App logo`` (optional). It is recommended to display the application icon to users, including in the Okta Mobile app.

  If you’d like to use a Mattermost logo for the application, you are free to download one `from our page <http://www.mattermost.org/brand-guidelines/>`_.

	.. image:: ../../source/images/okta_2_general_settings.PNG

5. Enter **SAML Settings**, including:
 - Single sign on URL: ``https://<your-mattermost-url>/login/sso/saml``
 - Audience URL: For instance, ``mattermost``
 - Name ID format: ``unspecified``
 - Application username: ``Email``

	.. image:: ../../source/images/okta_3_initial_saml_settings.PNG

6. (Optional) Set up encryption for your SAML connection. First, click **Show Advanced Settings**.

	.. image:: ../../source/images/okta_4_initial_saml_settings.PNG

Then, set **Assertion Encryption** as ``Encrypted`` and upload the **Service Provider Public Certificate** you generated in step 2 to the **Encryption Certificate** field.

	.. image:: ../../source/images/okta_5_advanced_saml_settings.PNG

7. Enter attribute statements, which will be used to map attributes between Okta and Mattermost. For more information on which attributes are configurable, see our :ref:`documentation on SAML configuration settings <saml-enterprise>`. Email and username attributes are required. For Mattermost servers running 3.3 and earlier, first name and last name attributes are also required.

	.. image:: ../../source/images/okta_6_attribute_statements.PNG

8. Click **Next**. Then, set Okta support parameters for the application. Recommended settings:
 - I’m an Okta customer adding an internal app
 - This is an internal app that we have created

	.. image:: ../../source/images/okta_7_support_configuration.PNG

9. Click **Finish**. On the next screen, click the **Sign On** tab and click **View Setup Instructions**.

	.. image:: ../../source/images/okta_8_view_instructions.PNG

10. Take note of ``Identity Provider Single Sign-On URL`` (also known as ``SAML SSO URL``), and the Identity Provider Issuer, as both will be needed to configure SAML for Mattermost.

Furthermore, you **must download the X.509 Public Certificate file** and save it. You will need to upload it to Mattermost at a later step.

	.. image:: ../../source/images/okta_9_view_instructions.PNG

Configure SAML for Mattermost
-----------------------------

1. Start Mattermost server and sign into Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**, and enter the following fields:
 - **SAML SSO URL**: ``Identity Provider Single Sign-On URL`` from Okta, specified earlier.
 - **Identity Provider Issuer URL**: ``Identity Provider Issuer`` from Okta, specified earlier.
 - **Identity Provider Public Certificate**: X.509 Public Certificate file you downloaded from Okta earlier.

	.. image:: ../../source/images/okta_10_mattermost_basics.PNG

2. (Optional) Configure Mattermost to verify the signature. The **Service Provider Login URL** is the ``Single sign on URL`` you specified in Okta earlier.

	.. image:: ../../source/images/okta_11_mattermost_verification.PNG

3. (Optional) Enable encryption based on the parameters provided earlier.

	.. image:: ../../source/images/okta_12_mattermost_encryption.PNG

4. Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email and username are required and should match the values you entered in Okta earlier. See :ref:`documentation on SAML configuration settings <saml-enterprise>` for more detail.

For Mattermost servers running 3.3 and earlier, the first name and last name attributes are also required fields.

	.. image:: ../../source/images/okta_13_mattermost_attributes.PNG

5. (Optional) Lastly, customize the login button text.

	.. image:: ../../source/images/okta_14_mattermost_login_button.PNG

6. Click **Save**.

You’re done! If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It is also recommended to post an announcement about how the migration will work to users.

You may also configure SAML for Okta by editing ``config.json`` to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-troubleshooting.rst
