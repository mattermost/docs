Configure SAML synchronization with AD/LDAP
--------------------------------------------

In addition to configuring SAML sign-in, you can optionally configure synchronizing SAML accounts with AD/LDAP. When configured:

 - Mattermost queries AD/LDAP for relevant account information and updates SAML accounts based on changes to attributes (first name, last name, and nickname)
 - Accounts disabled in AD/LDAP are made inactive in Mattermost, and their active sessions are revoked once Mattermost synchronizes attributes.

To configure SAML synchronization with AD/LDAP:

1. Go to **System Console > SAML** and set **Enable Synchronizing SAML Accounts With AD/LDAP** to `true`.
2. Go to **System Console > AD/LDAP** and set **Enable Synchronization with AD/LDAP** to `true`.
3. Set the rest of the AD/LDAP settings based on `configuration settings documentation <http://docs.mattermost.com/administration/config-settings.html#ad-ldap>`_ to connect Mattermost with your AD/LDAP server.

 - If you don't want to enable AD/LDAP sign-in, keep **Enable sign-in with AD/LDAP** as ``false``.

4. Set **Syncronization Interval** to specify how often Mattermost synchronizes SAML user accounts with AD/LDAP. The default setting is 60 minutes. If you want to synchronize immediately after disabling an account, use the "AD/LDAP Synchronize Now" button in **System Console > AD/LDAP**.
5. To test Mattermost can successfully connect to your AD/LDAP server, click the **AD/LDAP Test** button.

Once the synchronization with AD/LDAP is enabled, user attributes are synchronized with AD/LDAP based on their email address. If a user with a given email address doesn't have an AD/LDAP account, they will be deactivated in Mattermost on the next AD/LDAP sync. To re-activate the account:

1. Add the user to your AD/LDAP server.
2. Purge all caches in Mattermost in **System Console > Configuration > Purge All Caches**.
3. Run AD/LDAP sync in **System Console > AD/LDAP > AD/LDAP Synchronize Now**.
4. Purge all caches again in Mattermost in **System Console > Configuration > Purge All Caches**, which re-activates the account in Mattermost.

  .. note::
    If a user is deactivated from AD/LDAP, they will be deactivated in Mattermost on the next sync. They will be shown as "Inactive" in the System Console users list, all of their sessions will expire and they won't be able to log back in to Mattermost.
    
    If a user is deactivated from SAML, their session won't expire until they're deactivated from AD/LDAP. However, they won't be able to log back in.
 
