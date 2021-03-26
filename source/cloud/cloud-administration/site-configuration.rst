Site Configuration
==================

Announcement Banner
-------------------

An announcement banner is available that allows System Admins to display a notice that's visible to all users on the system.

.. image:: ../../images/announcement-banner-1106x272.png
  :width: 1106
  :height: 272
  :alt: Shows the announcement banner at the top of the user's screen.

By default, users can dismiss the banner until they log in again or until you update the banner. You can update the banner by either changing the text of the banner or by re-enabling the banner after it has been disabled. You can also control the text color and the background color. A setting in the System Console allows you to prevent users from dismissing the banner.

**To enable the banner**:

1. Go to **System Console > Site Configuration > Announcement Banner**.
2. Set **Enable Announcement Banner** to **true**.
3. In the **Banner Text** field, enter the text of the announcement that you want to make.
4. Set banner background and text colors.
5. To prevent users from dismissing the banner, set **Allow Banner Dismissal** section to **false**.
6. Select **Save**.

Emoji
-----

There are three different settings that allow you to control emoji.

1. **Enable Emoji Picker:** An emoji picker that allows users to select emojis to add as reactions or use in messages. Enabling the emoji picker with a large number of Custom Emojis may slow down performance.
2. **Enable Custom Emoji:** You can control whether or not the Custom Emoji option in the Main Menu, where users can go to create customized emoji, is accessible.
3. **Restrict Custom Emoji Creation:** You can set which role is able to create Custom Emoji from **Main Menu > Custom Emoji** (all users, System and Team Admins, or System Admins only).
4. Select **Save**.

In-Product Notices
------------------

Mattermost in-product notices keep users and administrators informed of the newest product improvements, features, and releases. Notices are used to raise awareness of new features as part of our monthly release cadence. 

Users will only receive notices that specifically apply to them. For example, if a user is already running the latest Desktop App version, they will not receive an upgrade notice.

.. image:: ../../images/notices.png

Administrator Notices
^^^^^^^^^^^^^^^^^^^^^

Administrator notices are used to inform System Admins of important updates or recommended configuration options to optimize the user experience of their deployment. Administrator notices are enabled for all Mattermost users.

Administrator notices can be disabled in the **System Console > Site Configuration > Notices** page by setting **Enable Admin Notices** to **false**, then selecting **Save**.

End User Notices
^^^^^^^^^^^^^^^^

End user notices are used to inform users and System Admins of new feature enhancements and when new desktop versions are available. They can be disabled in **System Console > Site Configuration > Notices** by setting **Enable End User Notices** to **false**, then selecting **Save**.

Are notices enabled by default?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notices are enabled by default for all Mattermost users. System Admins may choose to disable administrator or end user notices in **System Console > Site Configuration > Notices**.

How often will users receive notices?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notices will be used to raise awareness of new features as part of our monthly release cadence. Users will only receive notices that specifically apply to them. For example, if a user is already running the latest Desktop App version, they will not receive an upgrade notice.

File Sharing and Downloads
--------------------------

There are three settings that allow you to control file sharing and file downloading on your workspace and on mobile devices.

1. **Allow File Sharing:** When configuration is set to **false**, file sharing is disabled. All file and image uploads on messages are forbidden across clients and devices, including mobile.
2. **Allow File Uploads on Mobile:** When configuration is set to **false**, disables file uploads on mobile apps. All file and image uploads on messages are forbidden across clients and devices, including mobile.
3. **Allow File Downloads on Mobile:** When configuration is set to **false**, disables file downloads on mobile apps. Users can still download files from a mobile web browser.
4. Select **Save**.

Localization
------------

Mattermost can be localized into 18 languages. You can set the default language for newly-created users and pages where the user hasn't logged in and which languages are available for users in **Account Settings > Display > Languages**. 

New languages are added automatically by default. You can add new languages using the dropdown menu manually as they become available. If you're manually adding new languages, the Default Client Language must be added before saving the setting.

Notifications
-------------

There are six settings that allow you to control notifications.

1. **Show @channel and @all confirmation dialog:** Users will be prompted to confirm when posting @channel and @all in channels with over five members.
2. **Email Notification Contents:** You can specify the content shown in email notifications. 
  - **Send full message contents** will include Sender name and channel in email notifications. 
  - **Send generic description with only sender name** will include the team name and name of the person who sent the message. No information about channel name or message contents, is included in email notifications. This is typically used for compliance reasons if Mattermost contains confidential information and policy dictates it cannot be stored in email.
3. **Notification Display Name:** Set the name displayed on the email account used when sending notification emails from Mattermost system.
4. **Notification Reply-To Address:** Set the email address used in the Reply-To header when sending notification emails from Mattermost.
5. **Notification Footer Mailing Address:** Set the name and mailing address displayed in the footer of email notifications from Mattermost, such as *ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA*. If the field is left empty, the organization name and mailing address will not be displayed.
6. **Push Notification Contents:** You can configure what information is provided in push notifications. 
  - **Generic description with only sender name** will include only the name of the person who sent the message but no information about channel name or message text. 
  - **Generic description with sender and channel names** will include names of users and channels but no specific details from the message text. 
  - **Full message content sent in the notification payload** will nclude the message contents in the push notification payload that is relayed through Apple's Push Notification Service (APNS) or Google's Firebase Cloud Messaging (FCM). It is highly recommended this option only be used with an "https" protocol to encrypt the connection and protect confidential information sent in messages.  
  - **Full message content fetched from the server on receipt** means the notification payload relayed through APNS or FCM contains no message content. Instead it contains a unique message ID used to fetch message content from the server when a push notification is received by a device. If the server cannot be reached, a generic notification will be displayed.
7. Select **Save**.

Posts
-----

There are four settings that allow you to control content in posts.

1. **Enable Link Previews:** Link previews are previews of linked website content, image links, and YouTube videos that are displayed below posts when available.Users can enable or disable website previews for themselves from **Account Settings > Display > Website Link Previews**. You can also disable all website link previews, image link previews, and YouTube previews by changing this setting to false.
2. **Enable SVGs:** Controls whether users have the ability to see previews of SVG file attachments and SVG image links.
3. **Enable LaTeX Rendering:** Controls users' ability to render LaTeX code.
4. **Custom URL Schemes:** A list of URL schemes that are used for autolinking in message text. HTTP, HTTPS, FTP, tel, and mailto always create links.
5. Select **Save**.

Users and Teams
---------------

There are seven different settings that allow you to control users and teams.

1. **Max Users Per Team:** The Max Users Per Team refers to the size of the *team site* which is a workspace a *team of people* inhabits. A team of people is considered a small organization where people work closely together towards a specific shared goal and share the same etiquette. In the physical world, a team of people could typically be seated around a single table to have a meal and discuss their project. The default maximum of 1000 people is at the extreme high end of a single team of people. At this point organizations are more often 'multiple teams of people' and investments in explicitly defining etiquette, such as channel organization or turning on policy features in Enterprise Edition, are often used to scale the high levels of productivity found in a team of people using Mattermost to multiple teams of people.
2. **Max Channels Per Team:** Set the maximum number of channels per team, including both active and deleted channels.
3. **Enable users to open Direct Message channels with:** You can configure whether users can message any user on the Mattermost workspace or only users in the same team as them. This setting adjusts the users returned in the Direct Messages **More** menu and CTRL/CMD+K channel switcher only lists users on the current team. This setting only affects the UI, not permissions on the server. For instance, a Direct Message channel can be created with anyone on the server regardless of this setting.
4. **Teammate Name Display:** Specifies how names are displayed in the user interface by default. Please note that users can override this setting in **Account Settings > Display > Teammate Name Display**. 
  - **Show username** displays the user's username. 
  - **Show nickname** if one exists displays the user's nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed. 
  - **Show first and last name** displays the user's full name. If the user does not have a full name, their username is displayed. Recommended when using SAML or LDAP if first name and last name attributes are configured.
5. **Lock Teammate Name Display for all users::** Specifies whether users can change settings under **Main Menu > Account Settings > Display > Teammate Name Display**.
6. **Show Email Address:** When set to **false**, this setting hides email address of users from other users in the user interface, including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see email addresses in the UI.
7. **Show Full Name:** WHen set to false, this setting hides full name of users from other users including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see full names in the UI.
8. Select **Save**.
