Administrator Onboarding Tasks
==============================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Following a Mattermost deployment or upgrade, we recommend that you review and follow the key configurations, optimizations, and recommendations listed below to provide your organization with the best possible Mattermost user experience.

.. tip::
  
  If your organization requires more structure and project management artifacts for the implementation of Mattermost, see our `Enterprise roll out checklist <https://docs.mattermost.com/getting-started/enterprise-roll-out-checklist.html>`__ documentation. 

Review System Console settings
------------------------------

.. note::

  The following settings can also be set in the ``config.json`` file. See our `configuration settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation for details on all available configuration settings.

1. Ensure all environment configuration settings are appropriately set under **System Console > Environment**, including:

 - `Web server <https://docs.mattermost.com/configure/configuration-settings.html#web-server>`__
 - `Database <https://docs.mattermost.com/configure/configuration-settings.html#database>`__
 - `File storage <https://docs.mattermost.com/configure/configuration-settings.html#file-storage>`__
 - `SMTP <https://docs.mattermost.com/configure/configuration-settings.html#smtp>`__
 - `Push Notification server <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-server>`__

2. Keep your desktop and mobile users logged in and `extend user sessions automatically with activity <https://docs.mattermost.com/configure/configuration-settings.html#extend-session-length-with-activity>`__.

3. `Enable push notifications on mobile devices <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-server>`__ to deliver messages in real time to your users.

4. `Enable full content push notifications <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-contents>`__, to display the sender’s name, the channel name, and the message text. Mattermost subscription plans allow you to `enable HPNS <https://docs.mattermost.com/deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ that includes production-level uptime SLAs.

.. note::

  Mattermost Enterprise customers can `enable ID-Only push notifications <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-contents>`__ so push notification content is not passed through Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) before reaching the device. The ID-only push notification setting `offers a high level of privacy <https://mattermost.com/blog/id-only-push-notifications/>`__ while allowing team members to benefit from mobile push notifications.

5. Provide your users with a visual glimpse of relevant content for links shared in messages by `enabling link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__.
 
6. Enable and batch email notifications so users don’t get overwhelmed with too many emails:

 - `Enable email notifications <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-notifications>`__ first. Email notifications require an `SMTP email server <https://docs.mattermost.com/configure/configuration-settings.html#smtp-email-server>`__ to be configured.
 - Then, `enable batched email notifications <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-batching>`__. Email batching isn't available when you're running your deployment in `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__.

7. Brand and customize how your users will interact with your Mattermost workspace by configuring your organization's:

 - `Support Email <https://docs.mattermost.com/configure/configuration-settings.html#support-email>`__ used on email notifications and during the onboarding tutorials for users to ask support questions.
 - `Help Link <https://docs.mattermost.com/configure/configuration-settings.html#help-link>`__ used on the Mattermost login page, sign-up pages, and can be used to link to your help desk ticketing system.

Review workspace health insights 
---------------------------------

From Mattermost v6.5, you can review a dashboard featuring insights related to the health of your Mattermost workspace in the System Console. This dashboard provides initial deployment configuration recommendations and guidance. Review your server health dashboard by going to **Reporting > Workplace Optimization**.

- On the dashboard, you can see whether there's a Mattermost update you should install. Mattermost releases regular updates to `Mattermost Team Edition <https://mattermost.com/>`_ and `Mattermost Enterprise Edition <https://mattermost.com/pricing-self-managed/>`_. The `Mattermost Changelog <https://docs.mattermost.com/install/self-managed-changelog.html>`_ provides all information about changes in each version. When you upgrade your Mattermost server frequently, your users can access new features, improved user experiences, bug fixes, security fixes, and Mobile App compatibility. Upgrading your Mattermost server only takes a few minutes. See the `Upgrade Guide <https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html>`__ for step-by-step instructions.

- Mattermost Enterprise customers can `enable Elasticsearch <https://docs.mattermost.com/scale/elasticsearch.html>`__ for optimized search performance at enterprise-scale. `Elasticsearch <https://docs.mattermost.com/scale/elasticsearch.html>`__ solves many known issues with full text database search, such as dots, dashes, and email addresses returning unexpected results. `Set up an Elasticsearch server <https://docs.mattermost.com/scale/elasticsearch.html#setting-up-an-elasticsearch-server>`__ and `enable Elasticsearch <https://docs.mattermost.com/configure/configuration-settings.html#elasticsearch>`__.

High Availability with PostgreSQL databases
-------------------------------------------

Customers with High Availability Mattermost environments using PostgreSQL should also consider specific configuration optimizations. See our `High Availability Cluster recommendations <https://docs.mattermost.com/scale/high-availability-cluster.html#recommended-configuration-settings>`__ documentation for details.

Integrate with your directory services
--------------------------------------

You likely already have your users grouped by role, location, or level. Mattermost provides identity management, single sign-on, and automatic account provisioning to make it easy for you to integrate with your existing identity and access management (IAM) services and systems with `Active Directory and LDAP <https://docs.mattermost.com/onboard/ad-ldap.html>`__ and `SAML 2.0 SSO <https://docs.mattermost.com/onboard/sso-saml.html>`__ integrations featuring providers like `Active Directory Federation Services <https://docs.mattermost.com/onboard/ad-ldap.html#configure-ad-ldap-deployments-with-multiple-domains>`__, `Okta <https://docs.mattermost.com/onboard/sso-saml-okta.html>`__, `GitLab <https://docs.mattermost.com/onboard/sso-gitlab.html>`__, `Google <https://docs.mattermost.com/onboard/sso-google.html>`__, and `Office 365 <https://docs.mattermost.com/onboard/sso-office.html>`__

- Begin to onboard users by `enabling account creation <https://docs.mattermost.com/configure/configuration-settings.html#enable-account-creation>`__ or by connecting an authentication service to assist with user provisioning.

- For bulk onboarding, enable `AD/LDAP Group Synchronization <https://docs.mattermost.com/configure/configuration-settings.html#enable-ad-ldap-group-sync>`__ to ensure new users are added to default teams and channels as they join Mattermost. See our `AD/LDAP Groups <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ documentation to learn more.

- See our `migration guide <https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migration-guide>`_ and `bulk loading documentation <https://docs.mattermost.com/onboard/bulk-loading-data.html>`_ for additional details.

Control product access with permissions
----------------------------------------

You can customize which users can perform specific actions, such as creating teams, managing channels, posting reactions, `adding custom emojis <https://docs.mattermost.com/configure/configuration-settings.html#enable-custom-emoji>`__, or editing or deleting posts. See our `Advanced Permissions <https://docs.mattermost.com/onboard/advanced-permissions.html>`__ documentation for details.

Team creation
-------------

Mattermost won’t limit you to the number of teams you can create; however, a public and an internal team are typically sufficient. See our `Creating Teams <https://docs.mattermost.com/messaging/creating-teams.html>`__ documentation for details.

Streamline conversations with channels
--------------------------------------

1. Channels can be public and open, private and restrictive, direct with another user, direct with multiple users, or read-only. 

 - Convert channels from private to public and from public to private as needed. See our `Managing Channels <https://docs.mattermost.com/messaging/managing-channels.html>`__ documentation for details.
 - Read-only channels are perfect for announcements because it’s easy to recall that information later. Update `channel moderation settings <https://docs.mattermost.com/onboard/advanced-permissions.html#read-only-channels-e20>`__ to set any channel as read-only.

2. When creating any channel, we recommend using Markdown to populate the channel header with useful information and links relevant to all channel members, such as specifications, agendas, or other shared files. In addition, a soft channel naming convention helps users create and name new channels consistency, and find those channels easily later.

3. All users can create their own personal channel categories. See our `Creating Custom Categories <https://docs.mattermost.com/messaging/organizing-your-sidebar.html#creating-custom-categories>`__ documentation for details.

4. Within a channel, pinning messages is an efficient way to find and reference important messages later, such as setup, onboarding, or troubleshooting steps. All users can save messages for later follow-up or reference.

Manage your notifications
--------------------------

Every Mattermost user can configure Mattermost notifications based on how and when to be notified of Mattermost activity by selecting **Settings > Notifications**. Help your users focus on what matters most with the following notification optimization settings:

+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Option                           | Recommendations                                                                                                                      |
+==================================+======================================================================================================================================+
| Desktop Notifications            | For efficient focus, select the following options:                                                                                   |
|                                  |                                                                                                                                      |
|                                  | - Only for mentions and direct messages                                                                                              |
|                                  | - Notify me about threads I’m following                                                                                              |
|                                  |                                                                                                                                      |
|                                  | Tips:                                                                                                                                |
|                                  |                                                                                                                                      |
|                                  | - A notification sound can be enabled or disabled based on preference.                                                               |
|                                  | - For deployments with Collapsed Reply Threads (Beta) enabled:                                                                       |
|                                  |   - Follow threads of interest on demand.                                                                                            |
|                                  |   - Unfollow threads that become less relevant over time.                                                                            |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Email Notifications              | Valuable to new users, but may be noisy for experienced users.                                                                       |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Mobile Push Notifications        | For efficient focus, select the following options:                                                                                   |
|                                  |                                                                                                                                      |
|                                  | - Only for mentions and direct messages                                                                                              |
|                                  | - Trigger push notifications can be updated based on specific circumstances, such as when in meetings or workshops.                  |
|                                  | - Notify me about threads I’m following                                                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Words that Trigger Mentions      | Specify any additional non-case sensitive words to be notified on, such as hashtags, subjects, or customer names.                    |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Reply notifications              | For deployments with Collapsed Reply Threads (Beta) disabled, each user can choose to receive notifications when someone replies to  |
|                                  | a thread the user started or both started and participated in.                                                                       |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Automatic Direct Message Replies | Enable `Automatic Replies <https://docs.mattermost.com/configure/configuration-settings.html#enable-automatic-replies>`__            |
|                                  | by going to **System Console > Experimental > Features** to allow all users to set an automated custom message that will             |
|                                  | be sent once per day in response to direct messages.                                                                                 |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

Enable file attachments and search
----------------------------------

When you `enable file sharing <https://docs.mattermost.com/configure/configuration-settings.html#allow-file-sharing>`__, your Mattermost users can attach files or images to their messages. You are in full control of the `maximum size of file attachments <https://docs.mattermost.com/configure/configuration-settings.html#maximum-image-resolution>`__. If your organization frequently works with SVG files, `enable previews of SVG attachments <https://docs.mattermost.com/configure/configuration-settings.html#enable-svgs>`__. 

- For additional security and protection with file attachments, a `ClamAV antivirus <https://mattermost.com/marketplace/antivirus-plugin/>`__ integration is available which scans files uploaded to Mattermost.

- Once you’ve enabled file attachments, extend Mattermost Channels search to include file contents by `enabling document search by content <https://docs.mattermost.com/configure/configuration-settings.html#enable-document-search-by-content>`__.

Extend Mattermost with integrations
-----------------------------------

Mattermost features powerful collaboration using context-rich actions. When you extend Mattermost functionality with integrations like `Zoom <https://mattermost.com/marketplace/zoom-plugin/>`__, `Jira <https://mattermost.com/marketplace/jira-plugin/>`__, `GitHub <https://mattermost.com/marketplace/github-plugin/>`__ or `GitLab <https://mattermost.com/marketplace/gitlab-plugin/>`__, moving around the ecosystem and staying informed is as simple as sending a message and subscribing channels to project or repository updates. 

More common Mattermost integrations your users may love:

- Create polls with `Matterpoll <https://mattermost.com/marketplace/matterpoll/>`__.
- Share GIFs with `GIF Commands <https://mattermost.com/marketplace/giphy-plugin/>`__.
- Create and share memes with `Memes <https://mattermost.com/marketplace/memes-plugin/>`__.
- Set personal reminders with `Remind <https://mattermost.com/marketplace/remind-plugin/>`__.
- Create and share to do items with `Todo <https://github.com/mattermost/mattermost-plugin-todo>`__.
- Customize welcome messages for new users with `WelcomeBot <https://mattermost.com/marketplace/welcomebot-plugin/>`__.

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to learn about the many ways you can extend Mattermost functionality for your needs. To enable and manage plugins, go to **System Console > Plugins**. Then, download plugins from the Mattermost Marketplace.

To enable integrations such as webhooks, slash commands, OAuth2.0, and bots, to go **System Console > Integrations**. See our `developer and integrator documentation <https://developers.mattermost.com/integrate/other-integrations/>`__ for details. 

Did you know?
-------------

- Anything you can do through the Mattermost interface you can also do through the `Mattermost REST API <https://api.mattermost.com/>`__. 
- You can share important announcements within Mattermost by `displaying an announcement banner <https://docs.mattermost.com/manage/announcement-banner.html>`__ visible to all users.
- You can `organize discussions as threads <https://docs.mattermost.com/messaging/organizing-conversations.html>`__ to make asynchronous collaboration easier.

Important Mattermost administration notes 
-----------------------------------------

**DO NOT manipulate the Mattermost database**

- In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation.
- If you need to permanently delete a team or user, use the `mattermost user delete <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-user-delete>`__ CLI command, or use the `mmctl user delete <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-user-delete>`__ command.

Create a System Admin account from the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- If the System Admin leaves the organization or is otherwise unavailable, you can use the command line interface to assign the *system_admin* role to an existing user. In the ``/opt/mattermost`` directory, type ``sudo -u mattermost bin/mattermost roles system_admin {user-name}``, where *{user-name}* is the username of the person with the new role. For more information about using the command line interface, see `Command Line Tools <https://docs.mattermost.com/manage/command-line-tools.html>`__.
- The user needs to log out and log back in before the *system_admin* role is applied.
  
Migrate to AD/LDAP or SAML from email-based authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Mattermost Professional or Enterprise customers can migrate from email authentication to Active Directory/LDAP or to SAML Single Sign-on. To set up Active Directory/LDAP, see `Active Directory/LDAP Setup <https://docs.mattermost.com/onboard/ad-ldap.html#active-directory-ldap-setup-e10-e20>`_. To set up SAML Single Sign-on, see `SAML Single-Sign-On <https://docs.mattermost.com/onboard/sso-saml.html>`_.
- After the new authentication method is enabled, existing users cannot use the new method until they go to **Settings > Security > Sign-in method** and select **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After they have switched, they can no longer use their email and password to sign in.  
  
Deactivate a user
~~~~~~~~~~~~~~~~~

System Admins can go to **System Console > Users** for a list of all users on the server. Search and filter the list to make finding users easier. Select the user's role, then choose **Deactivate**. To preserve audit history, users are typically never deleted from the system. 

If permanently deleting a user is necessary (e.g. for the purposes of `GDPR <https://gdpr-info.eu/>`__), an `mmctl command <https://docs.mattermost.com/manage/mmctl-command-line-tool.html>`__ or a `CLI command <https://docs.mattermost.com/manage/command-line-tools.html>`_ can be used to do so. AD/LDAP user accounts can't be deactivated from Mattermost; they must be deactivated from your Active Directory.

Check for a valid license in Enterprise Edition without logging in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you manage a self-hosted Mattermost deployment, open the log file ``mattermost.log``. It's usually in the ``mattermost/logs/`` directory but might be elsewhere on your system. Find the last occurrence of a log entry that starts with the text ``[INFO] License key``. If the license key is valid, the complete line should be similar to the following example:

.. code-block:: text

  [2017/05/19 16:51:40 UTC] [INFO] License key valid unlocking enterprise features.
