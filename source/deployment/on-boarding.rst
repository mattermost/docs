Administrator Tasks
===================

This document provides instructions for common administrator tasks, including some recommendations on tasks to prepare your Mattermost instance to onboard users.

Getting Started Tasks
-----------------------
1. Once you've installed and deployed Mattermost, ensure all configuration settings are appropriately set under **System Console > Environment** including: 
 - Web Server
 - Database
 - File Storage
 - SMTP
 - Push Notification Server 
  
These settings can also be set in the ``config.json`` file. Please see our `configuration settings documentation <https://docs.mattermost.com/administration/config-settings.html>`__ for a full listing of all configuration settings. 

2. Adjust settings under **System Console > Site Configuration** to brand and customize how users will interact with the site.  
Be sure to update the Support Email and Help Link in Mattermost under **System Console > Site Configuration > Customization** to provide your users a resource for password resets or questions on their Mattermost account.

 - The Support Email is used on email notifications and during tutorial for users to ask support questions.
 - The Help Link is on the Mattermost login page, sign-up pages, and Main Menu and can be used to to link to your help desk ticketing system.  
 
These settings can also be set in the ``config.json`` file.  Please see our `configuration settings documenation <https://docs.mattermost.com/administration/config-settings.html>`__ for a full listing of all configuration settings.  

3. Begin to onboard users by enabling account creation or by connecting an authentication service to assist with user provisioning.  

 - Users can be pre-provisioned with migration and bulk loading data processes based on prior collaboration systems. Please see our `migration guide <https://docs.mattermost.com/administration/migrating.html#migration-guide>`_ and `bulk loading documentation <https://docs.mattermost.com/deployment/bulk-loading.html>`_ for additional details.
 - `AD/LDAP authentication <https://docs.mattermost.com/deployment/sso-ldap.html#active-directory-ldap-setup-e10-e20>`_ and `SAML authentication <https://docs.mattermost.com/deployment/sso-saml.html>`_ are available for Enterprise Edition, providing identity management, single sign-on, and automatic account provisioning.   

4. Enable integrations and plugins to connect your team's workflows and toolsets into Mattermost. 

 - To enable integrations such as webhooks, slash commands, OAuth2.0, and bots, to go **System Console > Integrations**. More information on these integrations can be found `here <https://docs.mattermost.com/guides/integration.html>`_. 
 - To enable and manage plugins, go to **System Console > Plugins**.  Mattermost offers an `integration marketplace <https://integrations.mattermost.com/>`_ where you can see all available plugins available for upload. 

If your organization requires more structure and project management artifacts for the implementation of Mattermost, please see our `Enterprise roll out checklist <https://docs.mattermost.com/getting-started/enterprise-roll-out-checklist.html>`__.

Important Administration Notes 
------------------------------
**DO NOT manipulate the Mattermost database**

 - In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation.
 - If you need to permanently delete a team or user, use the `Command Line Tool <https://docs.mattermost.com/administration/command-line-tools.html>`__.

Common Tasks
------------

**Creating System Admin account from the command line**
 - If the System Admin leaves the organization or is otherwise unavailable, you can use the command line interface to assign the *system_admin* role to an existing user. In the ``/opt/mattermost`` directory, type ``sudo -u mattermost bin/mattermost roles system_admin {user-name}``, where *{user-name}* is the username of the person with the new role. For more information about using the command line interface, see `Command Line Tools <https://docs.mattermost.com/administration/command-line-tools.html>`_.
 - The user needs to log out and log back in before the *system_admin* role is applied.
  
**Migrating to AD/LDAP or SAML from email-based authentication**
 - If you have Enterprise Edition, you can migrate from email authentication to Active Directory/LDAP or to SAML Single Sign-on. To set up Active Directory/LDAP, see `Active Directory/LDAP Setup (E10/E20) <https://docs.mattermost.com/deployment/sso-ldap.html#active-directory-ldap-setup-e10-e20>`_. To set up SAML Single Sign-on, see `SAML Single-Sign-On (E20) <https://docs.mattermost.com/deployment/sso-saml.html>`_.
 - After the new authentication method is enabled, existing users cannot use the new method until they go to **Account Settings > Security > Sign-in method** and click **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After they have switched, they can no longer use their email and password to sign in.  

**Deactivating a user**
 - System Admins can go to **System Console > Users** for a list of all users on the server. The list can be searched and filtered to make finding the user easier. Click the user's role and in the menu that opens, click **Deactivate**.
 - To preserve audit history, users are typically never deleted from the system. If permanently deleting a user is necessary (e.g. for the purposes of `GDPR <https://gdpr-info.eu/>`__), a `CLI tool <https://docs.mattermost.com/administration/command-line-tools.html>`_ can be used to do so.
 - Note that AD/LDAP user accounts cannot be deactivated from Mattermost; they must be deactivated from your Active Directory.

**Checking for a valid license in Enterprise Edition without logging in**
 - Open the log file ``mattermost.log``. It's usually in the ``mattermost/logs/`` directory but might be elsewhere on your system. Find the last occurrence of a log entry that starts with the text ``[INFO] License key``. If the license key is valid, the complete line should be similar to the following example:

    .. code-block:: text

      [2017/05/19 16:51:40 UTC] [INFO] License key valid unlocking enterprise features.
      
**Upgrading Mattermost**
 - Mattermost releases updates monthly to `Mattermost Team Edition <https://mattermost.com/>`_ and `Mattermost Enterprise Edition <https://mattermost.com/pricing-self-managed/>`_. The `Mattermost Changelog <https://docs.mattermost.com/administration/changelog.html>`_ provides all information about changes in each version. We recommend servers be upgraded often to keep up with critical bug fixes and security fixes. 
 - Follow the steps outlined in the `upgrade documentation <https://docs.mattermost.com/administration/upgrade.html>`_ to perform upgrades.   

User Experience Optimizations
-----------------------------

We highly recommend the following best practices, configuration options, and features for an optimal Mattermost user experience.

**1. Upgrade your Mattermost Server**

Frequent server upgrades are critical to maintain an optimized user experience. When you upgrade your Mattermost server frequently, your users can access new features, improved user experiences, bug fixes, and guaranteed mobile app compatibility. Upgrading your Mattermost server only takes a few minutes. See the `Upgrade Guide <https://docs.mattermost.com/administration/upgrade.html>`__ for step-by-step instructions. 

**2. Install Plugins**

Plugins customize and extend the Mattermost platform. Install plugins with a single click from the **Main Menu > Plugin Marketplace**. See the `Plugin Marketplace  <https://docs.mattermost.com/administration/plugins.html#plugin-marketplace>`__ documentation for details.

  Consider installing and enabling the following productivity plugins for your users:   
    - Enable audio/video calling and screen sharing with `Jitsi <https://integrations.mattermost.com/?s=Jitsi%20Plugin>`__ or `Zoom <https://integrations.mattermost.com/?s=Zoom%20Plugin>`__.
    - Create polls with `Matterpoll <https://integrations.mattermost.com/?s=Matterpoll%20Plugin>`__.
    - Share GIFs with `GIF Commands <https://integrations.mattermost.com/?s=gif&submit=>`__.
    - Create and share memes with `Memes <https://integrations.mattermost.com/?s=Memes%20Plugin>`__.
    - Set personal reminders with `Remind <https://integrations.mattermost.com/?s=Remind%20Plugin>`__.
    - Create and share to do items with `Todo <https://github.com/mattermost/mattermost-plugin-todo>`__.
    - Customize welcome messages for new users with `WelcomeBot <https://integrations.mattermost.com/?s=WelcomeBot%20Plugin>`__.

Explore all plugins and integrations available in the `Mattermost Plugin Marketplace <https://integrations.mattermost.com/>`__.

**3. Enable Automatically Extended Sessions**

Keep your desktop and mobile users logged in and refresh user sessions automatically by setting **System Console > Sessions > Extend session length with activity** to ``true``. See the `Extend session length with activity <https://docs.mattermost.com/administration/config-settings.html#extend-session-length-with-activity>`__ configuration settings documentation for details.

**4. Enable Full Content Push Notifications**

Enable push notifications on mobile devices to deliver messages in real time by setting **System Console > Push Notification Server > Enable Push Notifications** to ``Use TPNS``. See the `Push notification server <https://docs.mattermost.com/administration/config-settings.html#push-notification-server>`__ configuration settings documentation for details.

Enable full content push notifications, including the sender’s name, the channel name, and the message text, by configuring the following: **System Console > Notifications > Push Notification Contents**: ``Full message contents``. See the `Push notification contents <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`__ configuration settings documentation for details.

.. note::

  - Mattermost Enterprise E10 and E20 customers can `enable HPNS <https://docs.mattermost.com/mobile/mobile-hpns.html>`__ that includes production-level uptime SLAs.

  - Mattermost Enterprise Edition E20 customers can `enable ID-Only push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`__ so the notification message contents are not passed through Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) before reaching the device.

**5. Enable Custom Emoji**

`Emojis <https://docs.mattermost.com/help/messaging/emoji.html>`__ enable users to express concepts such as emotions and physical gestures in messages. Enable the emoji picker by configuring the following: **System Console > Emoji > Enable Emoji Picker**: ``true``. See the `Enable emoji picker <https://docs.mattermost.com/administration/config-settings.html#enable-emoji-picker>`__ configuration settings documentation for details.

Empower users to create and share their own custom emojis by setting **System Console > Emoji > Enable Custom Emoji** to ``true``. See the `Enable custom emoji <https://docs.mattermost.com/administration/config-settings.html#enable-custom-emoji>`__ configuration settings documentation for details.

**6. Enable GIF Picker (Beta)**

GIFs are animated images that can make messaging more fun and engaging. Enable users to access the Mattermost GIF picker from the message draft area by configuring the following: **System Console > GIF (Beta) > Enable GIF Picker**: ``true``. See the `Enable GIF picker <https://docs.mattermost.com/administration/config-settings.html#enable-gif-picker>`__ configuration settings documentation for details.

**7. Enable Link Previews**

Link previews provide a visual glimpse of relevant content for links shared in messages. Enable link previews by setting **System Console > Posts > Enable Link Previews** to ``true``. See the `Enable link previews <https://docs.mattermost.com/administration/config-settings.html#enable-link-previews>`__ configuration settings documentation for details.
 
**8. Enable Batched Email Notifications**

Email notifications can be batched together so users don’t get overwhelmed with too many emails.

Enable email notifications first by setting **System Console > Notifications > Enable Email Notifications** to ``true``. See the `Enable email notifications <https://docs.mattermost.com/administration/config-settings.html#enable-email-notifications>`__ configuration settings documentation for details. Note that email notifications require an `SMTP email server <https://docs.mattermost.com/administration/config-settings.html#smtp-server>`__ to be configured.

Then, enable batched email notifications by configuring the following: **System Console > Notifications > Enable Email Batching**: ``true``. See the `Enable email batching <https://docs.mattermost.com/administration/config-settings.html#enable-email-batching>`__ configuration settings documentation for details.Email batching is not available if you are running your deployment in `High Availability <https://docs.mattermost.com/deployment/cluster.html>`__.

**9. Enable Elasticsearch (E20)**

Mattermost Enterprise Edition E20 customers can enable `Elasticsearch <https://docs.mattermost.com/deployment/elasticsearch.html>`__ for optimized search performance at enterprise-scale. Elasticsearch solves many known issues with full text database search, such as dots, dashes, and email addresses returning unexpected results.

Enable Elasticsearch by configuring the following: **System Console > Elasticsearch > Enable Indexing**: ``true``. See the `Elasticsearch <https://docs.mattermost.com/administration/config-settings.html#elasticsearch>`__ configuration settings documentation for details. Enabling Elasticsearch requires `setting up an Elasticsearch server <https://docs.mattermost.com/deployment/elasticsearch.html#setting-up-an-elasticsearch-server>`__.

**10. Try Experimental Features**

Mattermost often releases experimental features to get user feedback on new functionality and product enhancements. For example, new `experimental sidebar features <https://mattermost.com/blog/dev-sneak-peek-experimental-sidebar-features>`__ include custom, collapsible channel categories, unread filtering, and many more enhancements for managing channels in your sidebar.  

Enable experimental sidebar features by configuring the following: **System Console > Experimental > Experimental Sidebar Features**. See the `Experimental sidebar features (Experimental) <https://docs.mattermost.com/administration/config-settings.html#experimental-sidebar-features-experimental>`__ configuration settings documentation for details.
