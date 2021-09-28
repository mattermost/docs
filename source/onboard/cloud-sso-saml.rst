
SAML Single Sign-On
====================

Single sign-on (SSO) is a way for users to log into multiple applications with a single user ID and password without having to re-enter their credentials. The SAML standard allows identity providers to pass credentials to service providers. Mattermost can be configured to act as a SAML 2.0 Service Provider. 

Mattermost can be configured to act as a SAML 2.0 Service Provider. The SAML Single sign-on integration offers the following benefits:

- **Single sign-on.** Users can sign-in to Mattermost with their SAML credentials.
- **Centralized identity management.** Mattermost accounts automatically pull user attributes from SAML upon login, such as full name, email, and username.
- **Automatic account provisioning.** Mattermost user accounts are automatically created the first time a user signs in with their SAML credentials on the Mattermost workspace.
- **Sync groups to predefined roles in Mattermost.** Assign team and channel roles to groups via LDAP Group Sync.
- **Compliance alignment with administrator management.** Manage Administrator access to Mattermost in the System Console using SAML attributes.

SAML Single sign-on itself does not support periodic updates of user attributes nor automatic deprovisioning. However, SAML with AD/LDAP sync can be configured to support these use cases.

For more information about SAML, see `this article from Varonis <https://www.varonis.com/blog/what-is-saml/>`_, and `this conceptual example from DUO <https://duo.com/blog/the-beer-drinkers-guide-to-saml>`_.

Mattermost officially supports Okta, OneLogin, and Microsoft ADFS as the identity providers (IDPs), please see links below for more details on how to configure SAML with these providers.

 - `Okta SAML Configuration <https://docs.mattermost.com/onboard/sso-saml-okta.html>`_
 - `OneLogin SAML Configuration <https://docs.mattermost.com/onboard/sso-saml-onelogin.html>`_
 - `Microsoft ADFS SAML Configuration for Windows Server 2012 <https://docs.mattermost.com/onboard/sso-saml-adfs.html#configure-saml-with-microsoft-adfs-for-windows-server-2012>`_
 - `Microsoft ADFS SAML Configuration for Windows Server 2016 <https://docs.mattermost.com/onboard/sso-saml-adfs-msws2016.html#configure-saml-with-microsoft-adfs-using-microsoft-windows-server-2016>`_

In addition to the officially supported identity providers, you can also configure SAML for a custom IdP. For instance, customers have successfully set up Azure AD, DUO, PingFederate, Keycloak, and SimpleSAMLphp as a custom IdPs. Because we do not test against these identity providers, it is important that you test new versions of Mattermost in a staging environment to confirm it will work with your identity provider. You can also set up MFA on top of your SAML provider for additional security.

Using SAML Attributes to Apply Roles
------------------------------------

You can use attributes to assign roles to specified users on login. To access the SAML attribute settings navigate to **System Console > Authentication > SAML 2.0**.

Username Attribute
~~~~~~~~~~~~~~~~~~

(Optional) Enter a SAML assertion filter to use when searching for users.

1. Go to **System Console > Authentication > SAML 2.0**.
2. Complete the **Username Attribute** field.
3. Select **Save**.

When the user accesses the Mattermost URL, they log in with same username and password that they use for organizational logins.

Guest Attribute
~~~~~~~~~~~~~~~

When enabled, the Guest Attribute in Mattermost identifies external users whose SAML assertion is guest and who are invited to join your Mattermost workspace. These users will have the Guest role applied immediately upon first sign-in instead of the default member user role. This eliminates having to manually assign the role in the System Console.

If a Mattermost Guest user has the guest role removed in the SAML system, the synchronization processes will not automatically promote them to a member user role. This is done manually via **System Console > User Management**. If a member user has the Guest Attribute added, the synchronization processes will automatically demote the member user to the guest role.

**Enable Guest Access**
1. Go to **System Console > Authentication > SAML 2.0**.
2. Complete the Guest Attribute field.
3. Select **Save**.

When a guest logs in for the first time they are presented with a default landing page until they are added to channels.

See the `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`_ for more information about this feature.

Admin Attribute
~~~~~~~~~~~~~~~

(Optional) The attribute in the SAML Assertion for designating System Admins. The users selected by the query will have access to your Mattermost workspace as System Admins. By default, System Admins have complete access to the Mattermost System Console.

Existing members that are identified by this attribute will be promoted from member to System Admin upon next login. The next login is based upon Session lengths set in **System Console > Session Lengths**. It is recommended that users are manually demoted to members in **System Console > User Management** to ensure access is restricted immediately.

1. Go to **System Console > Authentication > SAML 2.0**.
2. Set **Enable Admin Attribute** to **true**.
3. Complete the **Admin Attribute** field.
4. Select **Save**.

**Note:** If the Admin Attribute is set to ``false`` the member's role as System Admin is retained. However, if the attribute is removed/changed, System Admins that were promoted via the attribute will be demoted to members and will not retain access to the System Console. When this attribute is not in use, System Admins can be manually promoted/demoted in **System Console > User Management**.

Configuration Assistance
-------------------------

We are open to providing assistance when configuring your custom IdP by answering Mattermost technical configuration questions and working with your IdP provider in support of resolving issues as they relate to Mattermost SAML configuration settings. However, we cannot guarantee your connection will work with Mattermost.

To assist with the process of getting a user file for your custom IdP, see this `documentation <https://github.com/icelander/mattermost_generate_user_file>`_.

For technical documentation on SAML, see `SAML Single-Sign-On: Technical Documentation <https://docs.mattermost.com/onboard/cloud-sso-saml-technical.html>`_.

Please note that we may not be able to guarantee that your connection will work with Mattermost, however we will consider improvements to our feature as we are able. You can see more information on getting support `here <https://mattermost.com/support/>`_ and submit requests for official support of a particular provider on our `feature idea forum <https://mattermost.uservoice.com>`_.
