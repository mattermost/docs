## Configure SAML with Okta

The following process provides steps to configure SAML with Okta for Mattermost.

### Set up a connection app for Mattermost SSO

1) Sign into Okta as an administrator.

2) Go to **Admin Dashboard > Applications > Add Application**.

3) Click **Create New App** and choose `SAML 2.0` as the Sign on method.

![okta_1_new_app](../../source/images/okta_1_new_app.PNG)

4) Enter **General Settings** for the application, including `App name` and `App logo` (optional). It is recommended to display the application icon to users, including in the Okta Mobile app.

If you’d like to use a Mattermost logo for the application, you are free to download one [here](../../source/images/okta_mattermost_logo.PNG)

![okta_2_general_settings](../../source/images/okta_2_general_settings.PNG)

5) Enter **SAML Settings**, including:
 - Single sign on URL: `https://<your-mattermost-url>/login/sso/saml`
 - Audience URL: For instance, `mattermost`
 - Name ID format: `unspecified`
 - Application username: `Email`

![okta_3_initial_saml_settings.PNG](../../source/images/okta_3_initial_saml_settings.PNG)

6) (Optional) Set up encryption for your SAML connection. First, click **Show Advanced Settings**

![okta_4_initial_saml_settings.PNG](../../source/images/okta_4_initial_saml_settings.PNG)

Then, set **Assertion Encryption** as `Encrypted` and generate the encryption certificates. You are free to generate the certificates by [downloading a built script here](broken link, to be added).

After generating your x509.crt encryption certificate, upload it to **Encryption Certificate** field.

![okta_5_advanced_saml_settings.PNG](../../source/images/okta_5_advanced_saml_settings.PNG)

7) Enter attribute statements, which will be used to map attributes between Okta and Mattermost. For more information on which attributes are configurable, see our [documentation on SAML configuration settings](http://docs.mattermost.com/administration/config-settings.html#saml-enterprise). Email, first name, last name and username attributes are required.

![okta_6_attribute_statements.PNG](../../source/images/okta_6_attribute_statements.PNG)

8) Click **Next**. Then, set Okta support parameters for the application. Recommended settings:
 - I’m an Okta customer adding an internal app
 - This is an internal app that we have created

![okta_7_support_configuration.PNG](../../source/images/okta_7_support_configuration.PNG)

9) Click **Finish**. On the next screen, click the **Sign On** tab and click **View Setup Instructions**.

![okta_8_view_instructions.PNG](../../source/images/okta_8_view_instructions.PNG)

10) Take note of `Identity Provider Single Sign-On URL` (also known as `SAML SSO URL`), and the Identity Provider Issuer, as both will be needed to configure SAML for Mattermost. 

Furthermore, you **must download the X.509 Public Certificate file** and save it. You will need to upload it to Mattermost at a later step.

![okta_9_view_instructions.PNG](../../source/images/okta_9_view_instructions.PNG)

##### Configure SAML for Mattermost

11) Start Mattermost server and sign into Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**, and enter the following fields:
 - **SAML SSO URL**: `Identity Provider Single Sign-On URL` from Okta, specified in step 10.
 - **Identity Provider Issuer URL**: `Identity Provider Issuer` from Okta, specified in step 10.
 - **Identity Provider Public Certificate**: X.509 Public Certificate file you downloaded from Okta in step 10.

![okta_10_mattermost_basics.PNG](../../source/images/okta_10_mattermost_basics.PNG)

12) (Optional) Configure Mattermost to verify the signature. The **Service Provider Login URL** is the `Single sign on URL` you specified in Okta in step 5.

![okta_11_mattermost_verification.PNG](../../source/images/okta_11_mattermost_verification.PNG)

13) (Optional) Enable encryption based on the parameters provided in step 6.

![okta_12_mattermost_encryption.PNG](../../source/images/okta_12_mattermost_encryption.PNG)

14) Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email, username, first name and last name are required and should match the values you entered in Okta in step 7. See [documentation on SAML configuration settings](http://docs.mattermost.com/administration/config-settings.html#saml-enterprise) for more detail.

![okta_13_mattermost_attributes.PNG](../../source/images/okta_13_mattermost_attributes.PNG)

15) (Optional) Lastly, customize the login button text.

![okta_14_mattermost_login_button.PNG](../../source/images/okta_14_mattermost_login_button.PNG)

16) Click **Save**.

You’re done! If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It is also recommended to post an announcement about how the migration will work to users.

You may also configure SAML for Okta by editing `config.json`. Before starting the Mattermost server, edit `config.json` to enable SAML based on [SAML configuration settings](http://docs.mattermost.com/administration/config-settings.html#saml-enterprise). After starting the Mattermost server, the first user to log in with valid SAML credentials will be assigned the System Administrator role.
