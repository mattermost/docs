Active Directory/LDAP Setup
===========================

|enterprise| |professional| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Overview
--------

Active Directory (AD) is a service that stores authentication and authorization details of users on your organization's network. When you integrate your AD/LDAP system with Mattermost, users can log into Mattermost without having to create new credentials. User accounts are managed in AD/LDAP, and changes are synced with Mattermost.

Benefits of integrating AD/LDAP with Mattermost include:

- **Single sign-on.** Users can sign in to Mattermost with their AD/LDAP credentials.
- **Centralized identity management.** Mattermost accounts can display user information from AD/LDAP, such as first and last name, email, and username.
- **Automatic account provisioning.** A Mattermost user account is automatically created the first time a user signs in with their AD/LDAP credentials.
- **Sync groups to predefined roles in Mattermost.** Assign team and channel roles to groups via LDAP Group Sync.
- **Compliance alignment with administrator management.** Manage Administrator access to Mattermost in the System Console using LDAP filters.

Pre-installation notes
-----------------------

If you're using Active Directory with **nested security groups** you need to write a PowerShell script, or similar, to flatten and aggregate the tree into a single security group to map into Mattermost.

Getting started
----------------

There are two ways to set up AD/LDAP:

1. **Configure AD/LDAP using the System Console user interface**
     - Log in to your workspace and create a new account using email and password. This is assigned the System Admin role as the first user created.
     - Next, configure AD/LDAP and then convert your System Admin account to use the AD/LDAP sign in method.

2. **Configure AD/LDAP by editing ``config.json``**
     - Edit ``config.json`` to enable AD/LDAP based on the `AD/LDAP settings documentation <https://docs.mattermost.com/configure/configuration-settings.html#ad-ldap>`__. When you log in to Mattermost the first user to log in with valid AD/LDAP credentials will be assigned the System Admin role.

Configure AD/LDAP sign in
--------------------------

1. **Create a System Admin account using email authentication.**
     - Create a new workspace and create an account using email and password, which is automatically assigned the **System Administrator** role since it is the first account created. You may also assign the role to another account.

2. **Configure AD/LDAP.**
     - Go to **System Console > Authentication > AD/LDAP** and fill in AD/LDAP settings based on the `configuration settings documentation <https://docs.mattermost.com/configure/configuration-settings.html#ad-ldap>`__.

3. **Confirm that AD/LDAP sign-on is enabled.**
     - After AD/LDAP has been enabled, confirm that users can sign in using AD/LDAP credentials.

4. **Switch your System Admin account from email to AD/LDAP authentication.**
     - Navigate to **Settings > Security > Sign-in Method > Switch to AD/LDAP** and sign in with your AD/LDAP credentials to complete the switch.

5. **(Optional) Restrict authentication to AD/LDAP.**
     - Go to **System Console > Authentication > Email** and set **Enable sign-in with email** to **false** and **Enable sign-in with username** to **false**.
     - Then choose **Save** to save the changes. This should leave Active Directory/LDAP as the only sign in option.

6. **(Optional) If you configured `First Name Attribute` and `Last Name Attribute` in the System Console.**
     - Navigate to **System Console > Site Configuration > Users and Teams** and set **Teammate Name Display** to **Show first and last name**. This is recommended for a better user experience.

.. note::

   If you've made a mistake and lock yourself out of the system somehow, you can `set an existing account to System Administrator using the command line tool <https://docs.mattermost.com/getting-started/admin-onboarding-tasks.html#common-tasks>`__.

Configure AD/LDAP synchronization
----------------------------------

In addition to configuring AD/LDAP sign-in, you can also configure AD/LDAP synchronization. When synchronizing, Mattermost queries AD/LDAP for relevant account information and updates Mattermost accounts based on changes to attributes (first name, last name, and nickname). When accounts are disabled in AD/LDAP users are made inactive in Mattermost, and their active sessions are revoked once Mattermost synchronizes the updated attributes.

The AD/LDAP synchronization depends on email. Make sure all users on your AD/LDAP server have an email address, or ensure their account is deactivated in Mattermost.

When Mattermost is configured to use LDAP for user authentication, the following user attribute changes can't be made through the API: first name, last name, position, nickname, email, profile image, or username. LDAP must be the authoritative source for these user attributes.

To configure AD/LDAP synchronization with AD/LDAP sign-in:

1. Go to **System Console > Authentication > AD/LDAP** and set **Enable Synchronization with AD/LDAP** to **true**.

2. Scroll down to **Synchronization Interval (minutes)** to specify how often Mattermost accounts synchronize attributes with AD/LDAP. The default setting is 60 minutes. The profile picture attribute is only synchronized when the user logs in.
     - If you want to synchronize immediately after disabling an account, use the **AD/LDAP Synchronize Now** button in **System Console > AD/LDAP**.
     - To configure AD/LDAP synchronization with SAML sign-in, see the `SAML documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__.

.. note::
   Make sure that at least one LDAP user is in Mattermost or the sync will not complete.

Configure AD/LDAP Sign-in Using Filters
----------------------------------------

Using filters assigns roles to specified users on login. To access AD/LDAP filter settings navigate to **System Console > AD/LDAP**.

User Filter
~~~~~~~~~~~

(Optional) Enter an AD/LDAP filter to use when searching for user objects. Only the users selected by the query will be able to access Mattermost. For Active Directory, the query to filter out disabled users is ``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``.

1. Navigate to **System Console > Authentication > AD/LDAP**.
2. Complete the **User Filter** field.
3. Choose **Save**.

When the user accesses Mattermost, they log in with same username and password that they use for organizational logins.

Filters can also be used for excluding users who belong to certain groups. For Active Directory, the query to filter out groups is ``(&(memberof=cn=ACME_ALL,ou=Users,dc=sademo,dc=com)(!(memberof=cn=DEV_OPS,ou=Users,dc=sademo,dc=com)))``.

Guest Filter
~~~~~~~~~~~~

(Optional) When enabled, the Guest Filter in Mattermost identifies external users whose AD/LDAP role is guest and who are invited to join your Mattermost workspace. These users will have the Guest role applied immediately upon first sign-in instead of the default member user role. This eliminates having to manually assign the role in the System Console.

If this filter is removed/changed, active guests will not be promoted to a member and will retain their Guest role. Guests can be promoted in **System Console > User Management**.

1. Navigate to **System Console > Authentication > Guest Access (Beta)** and set Guest Access to ``true``.
2. Navigate to **System Console > Authentication > AD/LDAP**.
3. Complete the **Guest Filter** field.
4. Choose **Save**.

When a guest logs in for the first time they are presented with a default landing page until they are added to channels.

See the `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information about this feature.

Admin Filter
~~~~~~~~~~~~

(Optional) Enter an AD/LDAP filter to use for designating System Admins. The users selected by the query will have access to your Mattermost workspace as System Admins. By default, System Admins have complete access to the Mattermost System Console. Existing members that are identified by this attribute will be promoted from member to System Admin upon next login.

The next login is based upon Session lengths set in **System Console > Session Lengths**. It is recommended that users are demoted to members manually in **System Console > User Management** to ensure access is restricted immediately.

1. Navigate to **System Console > Authentication > AD/LDAP**.
2. Set **Admin Filter** to **true**.
3. Complete the **Admin Filter** field.
4. Choose **Save**.

**Note:** If the Admin Filter is set to ``false`` the member's role as System Admin is retained. However if this filter is removed/changed, System Admins that were promoted via this filter will be demoted to members and will not retain access to the System Console.

When this filter isn't in use, members can be manually promoted/demoted via **System Console > User Management**.

Configure AD/LDAP deployments with multiple domains
-----------------------------------------------------

Organizations using multiple domains can integrate with Mattermost using a "Forest" configuration to bring together multiple domains. Please see `Forests as Collections of Domain Controllers that Trust Each Other <https://technet.microsoft.com/en-us/library/cc759073%28v=ws.10%29.aspx?f=255&MSPPError=-2147217396>`__ for more information.

For forest configurations that contain multiple domains which do NOT share a common root, you can search across all of the domains using the Global Catalog. To do so, update your ``config.json`` as follows:

- Set the LdapPort to 3268 (instead of 389)
- Set the BaseDN to " " (A single space character)

See `Global Catalog and LDAP Searches <https://technet.microsoft.com/en-us/library/cc978012.aspx>`__ for additional details.

Troubleshooting/FAQ
-------------------

The following are frequently asked questions and troubleshooting suggestions on common error messages and issues. It is recommended that you check your logs for errors as they can provide an idea of what the issue is.

If the **AD/LDAP Test** button fails, how can I troubleshoot the connection?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check that your AD/LDAP connection settings are correct by running an AD/LDAP user query in an external system. See `LDAP Connection Test Example <http://ldaptool.sourceforge.net>`__. If the AD/LDAP connection is verified to be working outside of Mattermost, try the following:

- Check your AD/LDAP system to verify your ``Bind Username`` format.
- Check your **AD/LDAP Port** and **Connection Security** settings in the System Console. (**AD/LDAP Port** set to 389 typically uses **Connection Security** set to ``None``. **AD/LDAP Port** set to 636 typically ties to **Connection Security** set to **TLS**).
- If you're seeing ``x509: certificate signed by unknown authority`` in your logs, try installing an intermediate SSL certificate or have your LDAP server send the complete certificate chain.

If these options don't work, please contact Mattermost support via the email address that came with your license key.

When I first set up and synchronize AD/LDAP, are the users automatically created in Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, each user is created on their first login.

When I try to synchronize AD/LDAP, why does the Status show as ``Pending`` and not complete?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **System Console > AD/LDAP** and make sure that the **Enable Synchronization with AD/LDAP** setting is set to **true**.

If the issue persists, try performing a sync with the **User Filter** field blank. If the sync completes in this scenario, then the general syntax was formatted incorrectly. Refer to this `document <https://docs.mattermost.com/configure/configuration-settings.html#user-filter>`__ for guidance on setting a correct syntax format.

Make sure that you also have at least one LDAP user in Mattermost or the sync will not complete.

What's the difference between the Username Attribute, ID Attribute, and Login ID Attribute?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are three AD/LDAP attributes that apear to be similar but serve a different purpose:

1. **Username Attribute:** Used within the Mattermost user interface to identify and mention users. For example, if **Username Attribute** is set to ``john.smith``, a user typing ``@john`` will see ``@john.smith`` in their autocomplete options and posting a message with ``@john.smith`` will send a notification to that user that they’ve been mentioned.
2. **ID Attribute:** Used as the unique identifier in Mattermost. It should be an AD/LDAP attribute with a value that does not change, such as ``ObjectGUID``. If a user's ID attribute changes, it will create a new Mattermost account unassociated with their old one. If you need to change this field after users have already logged in, use the `mattermost ldap idmigrate mmctl tool <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-ldap-idmigrate>`__.
3. **Login ID Attribute:** The attribute in the AD/LDAP server used to log in to Mattermost. Normally this attribute is the same as the **Username Attribute** field above, or another field that users can easily remember.

How do I deactivate users?
~~~~~~~~~~~~~~~~~~~~~~~~~~

When AD/LDAP authentication is used in Mattermost, user deactivation must be done via the AD/LDAP server.

There are two main ways to do this:

1. **User deletion:** If the user is completely removed from the AD/LDAP server, they will be deactivated in Mattermost on the next synchronization.
2. **User filter:** Set the `user filter <https://docs.mattermost.com/configure/configuration-settings.html#user-filter>`__ to only select the subset of AD/LDAP users you want to have access to Mattermost. When someone is removed from the selected group, they will be deactivated in Mattermost on the next synchronization.

For Active Directory, to filter out deactivated users you must set the user filter to:

``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``

Filters can also be used for excluding users who belong to certain groups. For Active Directory, the query to filter out groups is: 

``(&(memberof=cn=ACME_ALL,ou=Users,dc=sademo,dc=com)``

``(!(memberof=cn=DEV_OPS,ou=Users,dc=sademo,dc=com)))``

When a user is deactivated in Mattermost, all the user's current sessions are revoked and they will be unable to log in or access Mattermost.

Can I connect to multiple Active Directory servers?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is currently no built-in way to connect to multiple AD servers. You will need to connect the instances in a forest before connecting to Mattermost. Consider upvoting the `feature request <https://mattermost.uservoice.com/forums/306457-general/suggestions/13589904-add-the-abilitiry>`__ on our forum.

When trying to sign in, I see the error ``AD/LDAP not available on this server``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This indicates that there is a problem somewhere with your configuration. We recommend that you check your Mattermost configuration settings to ensure that AD/LDAP is enabled, and the settings are correct.

If you're still having issues, you can `contact support <https://mattermost.com/support/>`__ for additional troubleshooting.

I see the error ``User not registered on AD/LDAP server``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This means the query sent back to the AD/LDAP server returned no results. We recommend that you:

1. Check that the user credentials were entered properly - you should log in with the field set as the `*ID Attribute* <https://docs.mattermost.com/configure/configuration-settings.html#id-attribute>`__.
2. Check that the user account exists in the AD/LDAP server.
3. Check the AD/LDAP configuration settings are correct.

If you're still having issues, you can `contact Mattermost Support <https://mattermost.com/support/>`__  for additional troubleshooting.

I updated a user account in AD/LDAP, and they can no longer log in to Mattermost.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the user can no longer log in to Mattermost with their AD/LDAP credentials - for example, they get an error message ``An account with that email already exists``, or a new Mattermost account is created when they try to log in - this means the **ID Attribute** for their account has changed.

The issue can be fixed by changing the value of the field used for the **ID Attribute** back to the old value. If you're currently using a field that sometimes changes for an **ID Attribute** (e.g. username, email that changes when someone gets married), we recommend you switch to using a non-changing field such as a GUID.

To do this, you can set the `Login ID Attribute <https://docs.mattermost.com/configure/configuration-settings.html#id-attribute>`__ to whatever you would like users to log in with (e.g. username or email).

.. note::
   Currently the value is case sensitive. If the **ID Attribute** is set to the username and the username changes from ``John.Smith`` to ``john.smith``, the user will experience problems logging in.

I see the log error ``LDAP Result Code 4 "Size Limit Exceeded"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This indicates your AD/LDAP server configuration has a maximum page size set and the query coming from Mattermost is returning a result set in excess of that limit.

To address this issue you can set the `max page size <https://docs.mattermost.com/configure/configuration-settings.html#maximum-page-size>`__ in your Mattermost configuration to match the limit on your AD/LDAP server. This will return a sequence of result sets that do not exceed the max page size, rather than returning all results in a single query. A max page size setting of 1500 is recommended.

If the error is still occurring, it is likely that no AD/LDAP users have logged into Mattermost yet. Ensure that at least one AD/LDAP user has logged into Mattermost and re-run the sync. The error should disappear at that point.

Can the AD/LDAP User Filter read security groups?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes it can, but make sure that:

- Permissions are correctly configured on the service account you are using.
- Each user object is a direct member of the security group.

How do I know if an AD/LDAP sync job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each AD/LDAP sync job in **System Console > Authentication > AD/LDAP**. Here you can see the number of users updated and if the job succeeded or failed.
