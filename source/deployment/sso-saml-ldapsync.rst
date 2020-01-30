Configure SAML synchronization with AD/LDAP
--------------------------------------------

In addition to configuring SAML sign-in, you can optionally configure synchronizing SAML accounts with AD/LDAP. When configured:

 - Mattermost queries AD/LDAP for relevant account information and updates SAML accounts based on changes to attributes (first name, last name, and nickname)
 - Accounts disabled in AD/LDAP are made inactive in Mattermost, and their active sessions are revoked once Mattermost synchronizes attributes.

To configure SAML synchronization with AD/LDAP:

1. Go to **System Console > Authentication > SAML 2.0** (or **System Console > SAML** in versions prior to 5.12) and set **Enable Synchronizing SAML Accounts With AD/LDAP** to ``true``.
2. Go to  **System Console > Authentication > AD/LDAP** (or **System Console > AD/LDAP** in versions prior to 5.12) and set **Enable Synchronization with AD/LDAP** to ``true``.
3. Set the rest of the AD/LDAP settings based on `configuration settings documentation <http://docs.mattermost.com/administration/config-settings.html#ad-ldap>`__ to connect Mattermost with your AD/LDAP server.

 - If you don't want to enable AD/LDAP sign-in, keep **Enable sign-in with AD/LDAP** as ``false``.

4. Set **Syncronization Interval** to specify how often Mattermost synchronizes SAML user accounts with AD/LDAP. The default setting is 60 minutes. If you want to synchronize immediately after disabling an account, use the "AD/LDAP Synchronize Now" button in **System Console > AD/LDAP** in prior versions or **System Console** > **Authentication** > **AD/LDAP** in versions after 5.12.
5. To test Mattermost can successfully connect to your AD/LDAP server, click the **AD/LDAP Test** button.

Once the synchronization with AD/LDAP is enabled, user attributes are synchronized with AD/LDAP based on their email address. If a user with a given email address doesn't have an AD/LDAP account, they will be deactivated in Mattermost on the next AD/LDAP sync. To re-activate the account:

1. Add the user to your AD/LDAP server.
2. Purge all caches in Mattermost in **System Console > Web Server > Purge All Caches** (or **System Console > Configuration > Purge All Caches** in versions prior to 5.12).
3. Run AD/LDAP sync in **System Console > Authentication > AD/LDAP > AD/LDAP Synchronize Now** (or **System Console > AD/LDAP > AD/LDAP Synchronize Now** in versions prior to 5.12).
4. Purge all caches again in Mattermost in **System Console > Web Server > Purge All Caches** (or **System Console > Configuration > Purge All Caches** in versions prior to 5.12), which re-activates the account in Mattermost.

  .. note::
    If a user is deactivated from AD/LDAP, they will be deactivated in Mattermost on the next sync. They will be shown as "Inactive" in the System Console users list, all of their sessions will expire and they won't be able to log back in to Mattermost.

    If a user is deactivated from SAML, their session won't expire until they're deactivated from AD/LDAP. However, they won't be able to log back in to Mattermost.

  .. note::
    SAML synchronization with AD/LDAP is designed to pull user attributes such as first name and last name from your AD/LDAP, not to control authentication.

    In particular, the user filter cannot be used to control who can log in to Mattermost, this should be controlled by your SAML service provider's group permissions.

See :ref:`technical description of SAML synchronization with AD/LDAP <sso-saml-technical>` for more details.

Override SAML Data with AD/LDAP Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can choose to override SAML bind data with AD/LDAP information. For more infomation on binding a user with the SAML ID Attribute, please refer to this `documentation <https://docs.mattermost.com/deployment/sso-saml-okta.html#bind-authentication-to-id-attribute-instead-of-email>`__.

This process overrides SAML email address with AD/LDAP email address data or SAML Id Attribute with AD/LDAP Id Attribute if configured. We recommend using this configuration with the SAML ID Attribute to help ensure new users are not created when the email address changes for a user.

To ensure existing user accounts do not get disabled in this process, ensure the SAML IDs match the LDAP IDs by exporting data from both systems and comparing the ID data. Mapping ID Attributes for both AD/LDAP and SAML within Mattermost to fields that hold the same data will ensure the IDs match as well.

1. Set the SAML ``Id Attribute`` on **System Console > Authentication > SAML 2.0** > **Id Attribute** (or **System Console > SAML > Id Attribute** in versions prior to 5.12)
2. Set **System Console > Authentication > SAML 2.0 > Override SAML bind data with AD/LDAP information** (or **System Console > SAML > Override SAML bind data with AD/LDAP information** in versions prior to 5.12) to ``true``.
3. Set **System Console** > **Authentication** > **SAML 2.0** > **Enable Synchronizing SAML Accounts With AD/LDAP** (or **System Console > SAML > Enable Synchronizing SAML Accounts With AD/LDAP** in versions prior to 5.12) to ``true``.
4. Run AD/LDAP sync in **System Console > Authentication > AD/LDAP > AD/LDAP Synchronize Now** (or **System Console > AD/LDAP > AD/LDAP Synchronize Now** in versions prior to 5.12).
