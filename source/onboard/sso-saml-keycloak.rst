Configure SAML with Keycloak
========================

The following process provides steps to configure SAML with Keycloak for Mattermost.

.. contents::
  :backlinks: top
  :local:

Pre-installation
----------------


1. Before configuring SAML with Keycloak, ensure you have the _`XML Security Library <https://www.aleksey.com/xmlsec/download.html>`__  installed on your Mattermost instance. The XML Security Library is a part of Debian GNU/Linux.

Also confirm if the ``xmlsec1-openssl`` library was successfully installed. If not, run
    - ``apt-get install libxmlsec1-openssl`` on Ubuntu
    - ``yum install xmlsec1-openssl`` on RHEL

Set up a connection app for Mattermost SSO
-------------------------------------------

2. Sign in to Keycloak as an administrator.

3. Click **Clients** then **Create** and save. You'll use this client ID in a later step.
    - ``Client ID`` - mattermost
    - ``Protocol`` - saml

4. Edit the Mattermost client to have the below values:
    - Encrypt Assertions - ON
    - Force Name ID Format - ON
        - Name ID Format - ``Email``
    - Valid Redirects - ``https://<<siteURL>>/login/sso/saml``
    - Base URL - ``https://<<siteURL>>/login/sso/saml``

    .. image:: ../../source/images/keycloak_1_client_settings.png

5. Save the client config.

6. Navigate to **Keys** within the client config.

7. Click **Generate new keys**

8.  Export the keys by clicking **Export**, using the below values, and clicking **Download**.
    a. Archive Format - PKCS12
    b. Key Alias - mattermost
    c. Key Password - mattermost
    d. Store Password - mattermost

    .. image:: ../../source/images/keycloak_2_saml_keys.png

9. Add the default attributes
    a. Within your Mattermost client click **Mappers**
    b. Click **Add Buildin**
    c. Select the **X500 email**, **X500 givenName**, and **X500 surname** attributes
    d. Click **Add selected**

    .. image:: ../../source/images/keycloak_3_add_builtins.png

10. Add the username and id attribute
    a. With the **Mappers** section of your client, click **Create**
    b. Set **name** to ``username``
    c. Under Mapper Type select **User Property**
    d. Set **property** to ``Username`` (This is case sensitive)
    d. Set **SAML Attribute Name** to ``username``
    e. Click **Save**.
    f. Repeat this step and use the property of ``id`` to create the ID Attribute.


    .. image:: ../../source/images/keycloak_4_create_username_attribute.PNG

11. Get the metadata URL from keycloak
    a. Within your Realm, click **Realm Settings**
    b. At the bottom of the **General** tab you should see a **SAML 2.0 Identity Provider Metadata** endpoint. Right-click and copy this URL. Store for the next step.

Configure SAML for Mattermost
-----------------------------

12. Start Mattermost server and sign in to Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**

13. Set the **Identity Provider Metadata URL** to the value you copied from the step above and click **Get SAML Metadata from IdP**. The metadata import will populate fields related to your keycloak configuration.
    If you have any issues with this import, you can check the ``mattermost.log`` file for more information. You will need to turn on debug logging and try again if you do not already have debug logging enabled.

14. Set the below fields:
    - **Verify Signature** : ``true``
    - **Service Provider Login URL** : ``http://<<mattermostSiteURL>>/login/sso/saml``
    - **Service Provider Identifier** : ``mattermost``

    The Service Provider Identifier will match the **Client ID** That you configured on the second Keycloak step.

    .. image:: ../../source/images/keycloak_5_mattermost_config.png

14. Configure the Encryption using the key you downloaded in step 8 of the Keycloak config.
    a. Generate the ``.crt`` file from the ``.p12`` file.
    
        ``openssl pkcs12 -in keystore.p12 -out mattermost.crt -nodes``

    b. Generate the ``.key`` file from the ``.p12`` file.
    
        ``openssl pkcs12 -in keystore.p12 -out mattermost.key -nodes -nocerts``
    
    c. Upload both of these files within the Mattermost System Console. Make sure to click **Upload**.
        - **Service Provider Private Key** : ``mattermost.key``
        - **Service Provider Private Certificate** : ``mattermost.crt``

    .. image:: ../../source/images/keycloak_6_mattermost_encryption.PNG

15. (Optional) Setup request signing with the below parameters.

    .. image:: ../../source/images/keycloak_7_mattermost_request_signing.PNG

16. Set attributes for the SAML Assertions, which will update user information in Mattermost. Attributes for email and username are required to match the values you configured in Keycloak in steps 9 and 10. See [documentation on SAML configuration settings](http://docs.mattermost.com/administration/config-settings.html#saml-enterprise) for more detail.

    - **Username Attribute** : ``username``
    - **Email Attribute** : ``email``
    - **Id Attribute** : ``id``

    .. image:: ../../source/images/keycloak_7_mattermost_attributes.png

18. Click **Save**.

You’re done! If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It is also recommended to post an announcement about how the migration will work for users.

You may also configure SAML for Keycloak by editing ``config.json``. Before starting the Mattermost server, edit ``config.json`` to enable SAML based on [SAML configuration settings](http://docs.mattermost.com/administration/config-settings.html#saml-enterprise). You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-ldapsync.rst

.. include:: sso-saml-faq.rst
