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
    
    If a user is deactivated from SAML, their session won't expire until they're deactivated from AD/LDAP. However, they won't be able to log back in to Mattermost.
 
  .. note::
    SAML synchronization with AD/LDAP is designed to pull user attributes such as first name and last name from your AD/LDAP, not to control authentication.
    
    In particular, the user filter cannot be used to control who can log in to Mattermost, this should be controlled by your SAML service provider's group permissions.


Technical description of SAML synchronization with AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When enabled, SAML synchronization with AD/LDAP occurs in phases:

1. Get all the current LDAP users from the Mattermost database who have ``Users.AuthService`` set to ``ldap``. This is a SQL query issued against the Mattermost database: ``SELECT * FROM Users WHERE AuthService = 'ldap'``.
2. Get all the current SAML users from the Mattermost database who have ``Users.AuthService`` set to ``saml``. This is a SQL query issued against the Mattermost database: ``SELECT * FROM Users WHERE AuthService = 'saml'``.
3. Get all the current LDAP users from the LDAP server as defined by ``LdapSettings.UserFilter``. This is an `LDAP query <https://github.com/mattermost/mattermost-server/blob/master/scripts/ldap-check.sh>`_ issued against the LDAP server. Users are retrieved in batches as defined by ``LdapSettings.MaxPageSize``.
4. Update LDAP attributes. For each existing Mattermost user retrieved in step 1, attempt to find a match against the list of LDAP users from step 3. To find matches, ``Users.AuthData`` field of the Mattermost user is compared against the ``LdapSettings.IdAttribute`` LDAP setting.

 - If any attribute of the user has changed, that attribute is copied from the LDAP server and the user is marked as updated.
 - If the corresponding ``LdapSettings.IdAttribute`` is not found, the user is assumed to be deleted from the LDAP server, and deactivated from Mattermost by setting the ``Users.DeleteAt`` field to a valid timestamp.

5. Update SAML attributes. For each existing Mattermost user retrieved in step 2, attempt to find a match against the list of LDAP users from step 3. To find matches, ``SamlSettings.Email`` is compared against the ``LdapSettings.EmailAttribute`` LDAP setting.

 - If any attribute of the user has changed, that attribute is copied from the LDAP server and the user is marked as updated.
 - If the corresponding ``LdapSettings.EmailAttribute`` is not found, the user is assumed to be deleted from the LDAP server, and deactivated from Mattermost by setting the ``Users.DeleteAt`` field to a valid timestamp.
 
Binding SAML to ID Attribute Instead of Email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
Alternatively, you can choose to use the SAML Id Attribute instead of email to bind the user.  

Configuring this will allow you to reuse an email address for a new user without the old user's information being exposed. For instance, if a user with an email address joe.smith@mattermost.com was once an employee, a new employee named Joe Smith can use the same email. This configuration is also useful when a user has a name change and their email needs to be updated instead of needint to create a new email address.

To bind users to the SAML Id Attribute instead of email: 

1. Configure SAML with AD/LDAP synchronization as specified above.  
2. Map the SAML ``Id Attribute`` on **System Console > SAML > Id Attribute**. To ensure existing user accounts do not get disabled in this process, ensure the SAML IDs match the LDAP IDs. 
3. Set **System Console > SAML > Enable Synchronizing SAML Accounts With AD/LDAP** to ``true``.
4. Run AD/LDAP sync in **System Console > AD/LDAP > AD/LDAP Synchronize Now**.

This process was designed for backwards compatibility to email binding. Here is a more detailed explanation of the process that will be applied to any new accounts added after the configuration is set up:  

 - A user authenticated with SAML is bound to the SAML service user using the Id Attribute (as long as it has been configured) or their email. 
 - When the user tries to login, and the SAML server responds with a valid authentication, then the server uses the "Id" field of the SAML authentication to search the user. 
 - If the ID already exists, it logs in as that user. 
 - If the ID does not exist, it checks for the email. 
 - If the email exists, it logs in and updates the autentication data to the ID, instead of the email. 
 - If the ID and the email do not exist, it will create a new Mattermost account and allow the user to log in. 
 
.. note::
  For existing accounts without an updated SAML ID attribute, the AD/LDAP email will be used and duplicate accounts could be created.  
