Configure SAML with Okta
========================

The following process provides steps to configure SAML 2.0 with Okta for Mattermost.

.. contents:: On this page
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst
	:start-after: :nosearch:

Set Up a connection app for Mattermost Single Sign-On
-----------------------------------------------------

1. Log in to Okta as an administrator.

2. Switch to the **Classic UI**, using the drop-down in the upper left.

3. Go to **Admin Dashboard > Applications > Add Application**.

4. Select **Create New App**, then choose **SAML 2.0** as the Sign on method.

	.. image:: ../../source/images/okta_1_new_app.png
	   :alt: In Okta, switch to the Classic UI, then go to the Admin Dashboard > Applications > Add Application to create a new app. Choose SAML 2.0 as the Sign on method.

5. Enter **General Settings** for the application, including **App name** and **App logo** (optional). It's recommended to display the application icon to users, including in the Okta Mobile app. If you’d like to use a Mattermost logo for the application, you can download one `from our page <https://handbook.mattermost.com/operations/operations/publishing/publishing-guidelines/brand-and-visual-design-guidelines>`__.

	.. image:: ../../source/images/okta_2_general_settings.png
	   :alt: In Okta, under General Settings, enter an App name and an optional logo. Mattermost recommends displaying the application icon to users and within the Okta mobile app. Select Next to continue.

6. Enter **SAML Settings**, including:

 - **Single sign on URL:** ``https://<your-mattermost-url>/login/sso/saml`` where ``https://<your-mattermost-url>`` should typically match the `Mattermost Site URL </configure/configuration-settings.html#site-url>`__.
 - **Audience URI:** For instance, ``mattermost``
 - **Name ID format:** ``unspecified``
 - **Application username:** ``Email``

	.. image:: ../../source/images/okta_3_initial_saml_settings.png
	   :alt: In Okta, under Configure SAML, enter required SAML settings.

7.  To set up encryption for your SAML connection, select **Show Advanced Settings**.

	.. image:: ../../source/images/okta_4_initial_saml_settings.png
	   :alt: In Okta, under Configure SAML, set up encryption for your SAML connection by selecting Show Advanced Settings.

8. Set **Assertion Encryption** as **Encrypted**, then upload the Service Provider Public Certificate you generated earlier to the **Encryption Certificate** field.

	.. image:: ../../source/images/okta_5_advanced_saml_settings.png
	   :alt: In Advanced Settings, set the Assertion Encryption as Encrypted, then upload the generated Service Provider Public Certificate to the Encryption Certificate field

9. Enter attribute statements used to map attributes between Okta and Mattermost. For more information on which attributes are configurable, see our `documentation on SAML configuration settings </configure/configuration-settings.html#saml>`__. Email and username attributes are required. For SAML with Okta, an `ID attribute </configure/configuration-settings.html#id-attribute>`__ is also required, and that ID must be mapped to ``user.id``. 

	.. image:: ../../source/images/okta_6_attribute_statements.png
	   :alt: Enter attribute statements used to map attributes between Okta and Mattermost. Email and username attributes are required. Okta also requires an ID attribute that must be mapped to user.id.

10. Select **Next**. Then, set Okta support parameters for the application. Recommended settings:

 - **I’m an Okta customer adding an internal app**
 - **This is an internal app that we have created**

	.. image:: ../../source/images/okta_7_support_configuration.png
	   :alt: Set recommended Okta support parameters for the application, including I'm an Okta customer adding an internal app and This is an internal app that we have created.

11. Select **Finish**. 

12. In the Mattermost System Console, go to **Authentication > SAML 2.0**, then set **Override SAML bind data with AD/LDAP information** to **false** if currently set to **true**. You can re-enable `this configuration setting </configure/configuration-settings.html#override-saml-bind-data-with-ad-ldap-information>`__ later when once setup is complete.

13. On the next screen, select the **Sign On** tab, then select **View Setup Instructions**.

14. Select the **Identity Provider metadata** link, then copy the link from the browser URL field. This will be used during the SAML configuration steps in the next section. 

	.. image:: ../../source/images/okta_8_view_instructions.png
	   :alt: In the Mattermost System Console, after disabling the Override SAML bind data with AD/LDAP information setting, select the Sign On tab, then select View Setup Instructions. Select the Identity Provider metadata link, then copy the link from the browser URL field to a convenient location.

15. Take note of **Identity Provider Single Sign-On URL** (also known as **SAML SSO URL**), and the Identity Provider Issuer, as both may be needed to configure SAML for Mattermost. 

16. Download the X.509 Certificate file and save it. You may need to upload it to Mattermost in a later step.

	.. image:: ../../source/images/okta_9_view_instructions.png
	   :alt: Download the X.509 certificate file and save it. You'll upload this certificate file to Mattermost later.


Configure SAML Sign-On for Mattermost
--------------------------------------

Start the Mattermost server and log in to Mattermost as a System Admin. Go to **System Console > Authentication > SAML 2.0**, then paste the copied Identity Provider Metadata URL in the **Identity Provider Metadata URL** field and select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer URL** fields automatically. The Identity Provider Public Certificate is also downloaded from the server and set locally. 

Alternatively you can enter the following fields manually:
 - **SAML SSO URL:** ``Identity Provider Single Sign-On URL`` from Okta, specified earlier.
 - **Identity Provider Issuer URL:** ``Identity Provider Issuer`` from Okta, specified earlier.
 - **Identity Provider Public Certificate:** X.509 Public Certificate file you downloaded from Okta earlier.
 
	.. image:: ../../source/images/okta_10_mattermost_basics.png
	   :alt: In the Mattermost System Console, go to Authentication > SAML 2.0 to manually enter the SAML SSO URL and Identity Provider Issuer URL, and upload the Identity Provider Public Certificate manually.


2. Configure Mattermost to verify the signature. The **Service Provider Login URL** is the ``Single sign on URL`` you specified in Okta earlier.

	.. image:: ../../source/images/okta_11_mattermost_verification.png
	   :alt: On the SAML 2.0 page, configure Mattermost to verify the signature, and set the Service Provider Login ULR as the Single sign on URL configured in Okta.


3. Enable encryption based on the parameters provided earlier.

	.. image:: ../../source/images/okta_12_mattermost_encryption.png
	   :alt: On the SAML 2.0 page, enable encryption and upload both the Service Provider Private Key and the Service Provider Public Certificate.


4. Configure Mattermost to sign SAML requests using the Service Provider Private Key.

5. Set attributes for the SAML Assertions used to update user information in Mattermost. 
	- Attributes for Email, Username, and Id are required and should match the values you entered in Okta earlier.
	
	.. image:: ../../source/images/okta_13_mattermost_attributes.png
	   :alt: Set attributes for the SAML Assertions used to update user information in Mattermost. 	Attributes for Email, Username, and Id are required and should match the values set in Okta.


6. (Optional) Customize the login button text.

	.. image:: ../../source/images/okta_14_mattermost_login_button.png
	   :alt: You can customize the login button text. By default, the text displays as "With SAML".

7. Select **Save**.

8. (Optional) If you configured ``First Name`` Attribute and ``Last Name`` Attribute, go to **System Console > Site Configuration > Users and Teams**, then set **Teammate Name Display** to **Show first and last name**. This is recommended for a better user experience.

Once complete, and to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication from your profile picture via **Profile > Security > Sign-in Method > Switch to SAML SSO**, then log in with your SAML credentials to complete the switch.

We also recommend that you post an announcement for your users to explain how the migration will work.

You may also configure SAML for Okta by editing the ``config.json`` file to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-ldapsync.rst
	:start-after: :nosearch:

.. include:: sso-saml-faq.rst
	:start-after: :nosearch:
