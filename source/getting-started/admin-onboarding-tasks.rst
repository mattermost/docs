Administrator onboarding tasks
==============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This document provides instructions for common administrator tasks, including some recommendations on tasks to prepare your Mattermost deployment to onboard users.

Getting started tasks
---------------------

1. Once you've installed and deployed Mattermost, ensure all configuration settings are appropriately set under **System Console > Environment** including:

 - Web server
 - Database
 - File storage
 - SMTP
 - Push Notification server
  
These settings can also be set in the ``config.json`` file. Please see our `configuration settings documentation </configure/configuration-settings.html>`__ for a full listing of all configuration settings.

2. Adjust settings under **System Console > Site Configuration** to brand and customize how users will interact with the site. Be sure to update the Support Email and Help Link in Mattermost under **System Console > Site Configuration > Customization** to provide your users a resource for password resets or questions on their Mattermost account.

 - The Support email is used on email notifications and during tutorial for users to ask support questions.
 - The Help Link is on the Mattermost login page, sign-up pages, and Main Menu and can be used to to link to your help desk ticketing system.
 
These settings can also be set in the ``config.json`` file.  Please see our `configuration settings documentation </configure/configuration-settings.html>`__ for a full listing of all configuration settings.

3. Begin to onboard users by enabling account creation or by connecting an authentication service to assist with user provisioning.

- Users can be pre-provisioned with migration and bulk loading data processes based on prior collaboration systems. Please see our `migration guide </onboard/migrating-to-mattermost.html#migration-guide>`_ and `bulk loading documentation </onboard/bulk-loading-data.html>`_ for additional details.
- `AD/LDAP authentication </onboard/ad-ldap.html#active-directory-ldap-setup>`_ and `SAML authentication </onboard/sso-saml.html>`_ are available for some subscription plans, providing identity management, single sign-on, and automatic account provisioning.

If your organization requires more structure and project management artifacts for the implementation of Mattermost, please see our `Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist.html>`__.

Important administration notes 
------------------------------

**DO NOT manipulate the Mattermost database**

- In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation.
- If you need to permanently delete a team or user, use the `mmctl user delete </manage/mmctl-command-line-tool.html#mmctl-user-delete>`__ command or the `mmctl user deletall </manage/mmctl-command-line-tool.html#mmctl-user-deleteall>`__ command.

Common tasks
------------

**Creating System Admin account from the command line**

- If the System Admin leaves the organization or is otherwise unavailable, you can use the `mmctl roles </manage/mmctl-command-line-tool.html#mmctl-roles>`__ commands to assign the *system_admin* role to an existing user. 
- The user needs to log out and log back in before the *system_admin* role is applied.
  
**Migrating to AD/LDAP or SAML from email-based authentication**

- If you have Professional or Enterprise plans, you can migrate from email authentication to Active Directory/LDAP or to SAML Single Sign-on. To set up Active Directory/LDAP, see `Active Directory/LDAP Setup </onboard/ad-ldap.html#active-directory-ldap-setup-e10-e20>`_. To set up SAML Single Sign-on, see `SAML Single-Sign-On </onboard/sso-saml.html>`_.
- After the new authentication method is enabled, existing users cannot use the new method until they go to **Settings > Security > Sign-in method** and select **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After they have switched, they can no longer use their email and password to log in.  
  
**Deactivating a user**

- System Admins can go to **System Console > Users** for a list of all users on the server. The list can be searched and filtered to make finding the user easier. Click the user's role and in the menu that opens, click **Deactivate**.
- To preserve audit history, users are typically never deleted from the system. If permanently deleting a user is necessary (e.g. for the purposes of `GDPR <https://gdpr-info.eu/>`__), an `mmctl command </manage/mmctl-command-line-tool.html>`__ can be used to do so.
- Note that AD/LDAP user accounts cannot be deactivated from Mattermost; they must be deactivated from your Active Directory.

**Checking for a valid license in Enterprise Edition without logging in**

- Open the log file ``mattermost.log``. It's usually in the ``mattermost/logs/`` directory but might be elsewhere on your system. Find the last occurrence of a log entry that starts with the text ``[INFO] License key``. If the license key is valid, the complete line should be similar to the following example:

.. code-block:: text

  [2017/05/19 16:51:40 UTC] [INFO] License key valid unlocking enterprise features.
      
User experience optimizations
-----------------------------

We highly recommend the following best practices, configuration options, and features for an optimal Mattermost user experience.

**1. Upgrade your Mattermost server**

When you upgrade your Mattermost server frequently, your users can access new features, improved user experiences, bug fixes, security fixes, and mobile app compatibility.

Mattermost releases regular updates to `Mattermost Team Edition <https://mattermost.com/>`_ and `Mattermost Enterprise Edition <https://mattermost.com/pricing-self-managed/>`_. The `Mattermost Changelog </install/self-managed-changelog.html>`_ provides all information about changes in each version.

Upgrading your Mattermost server only takes a few minutes. See the `Upgrade Guide </upgrade/upgrading-mattermost-server.html>`__ for step-by-step instructions.

**2. Install plugins**

You can enable plugins and integrations to connect your team's workflows and toolsets into Mattermost. Plugins and integrations customize and extend the Mattermost platform.

**Install and manage plugins**

To enable and manage plugins, go to **System Console > Plugins**. Next, install plugins from **Product menu > Marketplace**. See the `Marketplace  <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/#marketplace>`__ documentation for details.

Consider installing, configuring, and enabling the following community integrations for your users:   
  - Create polls with `Matterpoll <https://mattermost.com/marketplace/matterpoll/>`__.
  - Share GIFs with `GIF Commands <https://mattermost.com/marketplace/giphy-plugin/>`__.
  - Create and share memes with `Memes <https://mattermost.com/marketplace/memes-plugin/>`__.
  - Set personal reminders with `Remind <https://mattermost.com/marketplace/remind-plugin/>`__.
  - Create and share to do items with `Todo <https://github.com/mattermost/mattermost-plugin-todo>`__.
  - Customize welcome messages for new users with `WelcomeBot <https://mattermost.com/marketplace/welcomebot-plugin/>`__.

Explore all plugins and integrations available in the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__.

**Enable and manage integrations**

To enable integrations such as webhooks, slash commands, OAuth2.0, and bots, to go **System Console > Integrations**. More information on these integrations can be found `here <https://developers.mattermost.com/integrate/other-integrations/>`_. 

**3. Enable automatically extended sessions**

Keep your desktop and mobile users logged in and `extend user sessions automatically <https://mattermost.com/blog/session-expiry-experience/>`__ by setting **System Console > Sessions > Extend session length with activity** to **true**. See the `Extend session length with activity </configure/configuration-settings.html#extend-session-length-with-activity>`__ configuration settings documentation for details.

**4. Enable full content push notifications**

Enable push notifications on mobile devices to deliver messages in real time by setting **System Console > Push Notification Server > Enable Push Notifications** to **Use TPNS**. See the `Push notification server </configure/configuration-settings.html#push-notification-server>`__ configuration settings documentation for details.

Enable full content push notifications, including the sender’s name, the channel name, and the message text, by setting **System Console > Notifications > Push Notification Contents** to **Full message contents**. See the `Push notification contents </configure/configuration-settings.html#push-notification-contents>`__ configuration settings documentation for details.

.. note::

  - Mattermost subscription plans allow you to `enable HPNS </deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ that includes production-level uptime SLAs.

  - Mattermost Enterprise customers can `enable ID-Only push notifications </configure/configuration-settings.html#push-notification-contents>`__ so push notification content is not passed through Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) before reaching the device. The ID-only push notification setting `offers a high level of privacy <https://mattermost.com/blog/id-only-push-notifications/>`__ while allowing team members to benefit from mobile push notifications.

**5. Enable custom emoji**

`Emojis </messaging/using-emoji.html>`__ enable users to express concepts such as emotions and physical gestures in messages. Enable the emoji picker by setting **System Console > Emoji > Enable Emoji Picker** to **true**. See the `Enable emoji picker </configure/configuration-settings.html#enable-emoji-picker>`__ configuration settings documentation for details.

Empower users to create and share their own custom emojis by setting **System Console > Emoji > Enable Custom Emoji** to **true**. See the `Enable custom emoji </configure/configuration-settings.html#enable-custom-emoji>`__ configuration settings documentation for details.

**6. Enable GIF picker**

GIFs are animated images that can make messaging more fun and engaging. Enable users to access the Mattermost GIF picker from the message draft area by setting **System Console > GIF (Beta) > Enable GIF Picker** to **true**. See the `Enable GIF picker </configure/configuration-settings.html#enable-gif-picker>`__ configuration settings documentation for details.

**7. Enable link previews**

Link previews provide a visual glimpse of relevant content for links shared in messages. Enable link previews by setting **System Console > Posts > Enable Link Previews** to **true**. See the `Enable link previews </configure/configuration-settings.html#enable-link-previews>`__ configuration settings documentation for details.
 
**8. Enable batched email notifications**

Email notifications can be batched together so users don’t get overwhelmed with too many emails.

Enable email notifications first by setting **System Console > Notifications > Enable Email Notifications** to **true**. See the `Enable email notifications </configure/configuration-settings.html#enable-email-notifications>`__ configuration settings documentation for details. Note that email notifications require an `SMTP email server </configure/configuration-settings.html#smtp-email-server>`__ to be configured.

Then, enable batched email notifications by setting **System Console > Notifications > Enable Email Batching** to **true**. See the `Enable email batching </configure/configuration-settings.html#enable-email-batching>`__ configuration settings documentation for details. Note that email batching is not available if you are running your deployment in `High Availability </scale/high-availability-cluster.html>`__.

**9. Enable Elasticsearch**

Mattermost Enterprise customers can enable `Elasticsearch </scale/elasticsearch.html>`__ for optimized search performance at enterprise-scale. Elasticsearch solves many known issues with full text database search, such as dots, dashes, and email addresses returning unexpected results.

Enable Elasticsearch by setting **System Console > Elasticsearch > Enable Indexing** to **true**. See the `Elasticsearch </configure/configuration-settings.html#elasticsearch>`__ configuration settings documentation for details. Enabling Elasticsearch requires `setting up an Elasticsearch server </scale/elasticsearch.html#setting-up-an-elasticsearch-server>`__.
