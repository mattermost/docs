## Configure SAML with Keycloak

The following process provides steps to configure SAML with Keycloak for Mattermost.

### Pre-installation

1 - Before configuring SAML with Okta, make sure you have the [XML Security Library](https://www.aleksey.com/xmlsec/download.html) installed on your Mattermost instance. The XML Security Library is usually included as part of Debian GNU/Linux.

Also confirm if the `xmlsec1-openssl` library was successfully installed. If not, run
 - `apt-get install libxmlsec1-openssl` on Ubuntu
 - `yum install xmlsec1-openssl` on RHEL


### Set up a connection app for Mattermost SSO

2 - Sign into Keycloak as an administrator.

3 - Click **Clients** then **Create** and save. You'll use this client ID in a later step.
    - `Client ID` - mattermost
    - `Protocol` - saml
4 - Edit the mattermost client to have the below values:
    - Encrypt Assertions - ON
    - Force Name ID Format - ON
        - Name ID Format - Email
    - Valid Redirects - https://<<siteURL>>/login/sso/saml
    - Base URL - https://<<siteURL>>/login/sso/saml

![keycloak_1_client_settings](../../source/images/keycloak_1_client_settings.PNG)

5 - Save the client config.
6 - Navigate to **Keys** within the client config.
7 - Click **Generate new keys**
8 - Export the keys by clicking **Export**, using the below values, and clicking **Download**.
    a. Archive Format - PKCS12
    b. Key Alias - mattermost
    c. Key Password - mattermost
    d. Store Password - mattermost

![keycloak_2_saml_keys](../../source/images/keycloak_2_saml_keys.PNG)

9 - Add the default attributes
    a. Within your Mattermost client click **Mappers**
    b. Click **Add Buildin**
    c. Select the **X500 email**, **X500 givenName**, and **X500 surname** attributes
    d. Click **Add selected**

![keycloak_3_add_builtins](../../source/images/keycloak_3_add_builtins.PNG)

10 - Add the username and id attribute
    a. With the **Mappers** section of your client click **Create**
    b. Set **name** to ``username``
    c. Under Mapper Type select **User Property**
    d. Set **property** to ``Username`` (This is case sensitive)
    d. Set **SAML Attribute Name** to ``username``
    e. Click **Save**.
    f. Repeat this step again and use the property of ``id`` to create the ID Attribute.


![keycloak_4_create_username_attribute](../../source/images/keycloak_4_create_username_attribute.PNG)

11 - Get the metadata url from keycloak
    a. Within your Realm click **Realm Settings**
    b. At the bottom of the **General** tab you should see a **SAML 2.0 Identity Provider Metadata** endpoint. Right click and copy this url. Store for the next step.

### Configure SAML for Mattermost

12 - Start Mattermost server and sign into Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**

13 - Set the **Identity Provider Metadata URL** to the value you copied from the step above and click **Get SAML Metadata from IdP**. This will populate most of the important fields related to your keycloak configuration.
    If you have any issues with this import you can check the ``mattermost.log`` file for more information. You will need to turn on debug logging and try again if you do not already have debug logging enabled.

14 - Set the below fields:
    - **Verify Signature** : ``true``
    - **Service Provider Login URL** : ``http://<<mattermostSiteURL>>/login/sso/saml``
    - **Service Provider Identifier** : ``mattermost``

    The Service Provider Identifier will match the **Client ID** That you configured on the second Keycloak step.

![keycloak_5_mattermost_config](../../source/images/keycloak_5_mattermost_config.PNG)

14 - Configure the Encryption using the key you downloaded in step 8 of the Keycloak config.
    a. Generate the ``.crt`` file from the ``.p12`` file.
    
        ``openssl pkcs12 -in keystore.p12 -out mattermost.crt -nodes``

    b. Generate the ``.key`` file from the ``.p12`` file.
    
        ``openssl pkcs12 -in keystore.p12 -out mattermost.key -nodes -nocerts``
    
    c. Upload both of these files within the Mattermost System Console. Make sure to click **Upload**.
        - **Service Provider Private Key** : ``mattermost.key``
        - **Service Provider Private Certificate** : ``mattermost.crt``

![keycloak_6_mattermost_encryption](../../source/images/keycloak_6_mattermost_encryption.PNG)

15 - (Optional) Setup request signing with the below parameters.

![keycloak_7_mattermost_request_signing](../../source/images/keycloak_7_mattermost_request_signing.PNG)

16 - Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email and username are required and should match the values you configured in Keycloak in step 9 and 10. See [documentation on SAML configuration settings](http://docs.mattermost.com/administration/config-settings.html#saml-enterprise) for more detail.

    - **Username Attribute** : ``username``
    - **Email Attribute** : ``email``
    - **Id Attribute** : ``id``

![keycloak_7_mattermost_attributes](../../source/images/keycloak_7_mattermost_attributes.PNG)

18 - Click **Save**.

You’re done! If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It is also recommended to post an announcement about how the migration will work to users.

You may also configure SAML for Keycloak by editing `config.json`. Before starting the Mattermost server, edit `config.json` to enable SAML based on [SAML configuration settings](http://docs.mattermost.com/administration/config-settings.html#saml-enterprise). You must restart the Mattermost server for the changes to take effect.

#### Troubleshooting

The following are troubleshooting suggestions on common error messages and issues. 

##### 1. System Administrator locks themselves out of the system

If the System Administrator is locked out of the system during SAML configuration process, they can set an existing account to System Administrator using [a commandline tool](http://docs.mattermost.com/deployment/on-boarding.html#creating-system-administrator-account-from-commandline). 

##### 2. Received error message: `An account with that username already exists. Please contact your Administrator.`

This usually means an existing account has another authentication method enabled. If so, the user should sign in using that method (such as email and password), then change their sign-in method to SAML via **Account Settings > Security > Sign-in method**.

##### 3. Received error message: `An account with that email already exists. Please contact your Administrator.`

This usually means an existing account has another authentication method enabled. If so, the user should sign in using that method (such as email and password), then change their sign-in method to SAML via **Account Settings > Security > Sign-in method**.

##### 4. Received error message: `SAML login was unsuccessful because one of the attributes is incorrect. Please contact your System Administrator.`

Confirm all attributes, including `Email Attribute` and `Username Attribute`, are correct in both the Okta configuration and in **System Console > SAML**.

##### 5. Unable to switch to SAML authentication successfully

First, ensure you have installed the [XML Security Library](https://www.aleksey.com/xmlsec/download.html) on your Mattermost instance and that **it is available in your** `PATH`.

Second, ensure you have completed each step in our guide above for configuring SAML with Okta.

Lastly, if you are still having trouble with configuration, feel free to post in our [Troubleshooting forum](http://www.mattermost.org/troubleshoot/) and we'll be happy to help with issues during setup.
