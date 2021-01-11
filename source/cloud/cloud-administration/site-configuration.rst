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

1. Open **System Console > Site Configuration > Announcement Banner**.
2. Set **Enable Announcement Banner** to **true**.
3. In the **Banner Text** field, enter the text of the announcement that you want to make.
4. Set banner background and text colors.
5. To prevent users from dismissing the banner, set **Allow Banner Dismissal** section to **false**.
6. Select **Save**.

In-Product Notices
------------------

Mattermost in-product notices keep users and administrators informed of the newest product improvements, features, and releases.

.. image:: ../../images/notices.png

Administrator Notices
^^^^^^^^^^^^^^^^^^^^^

Administrator notices are used to inform System Admins of important updates or recommended configuration options to optimize the user experience of their deployment.

Administrator notices can be disabled in the **System Console > Site Configuration > Notices** page.

End User Notices
^^^^^^^^^^^^^^^^

End user notices are used to inform users and Admins of new feature enhancements and when new desktop versions are available. They can be disabled in **System Console > Site Configuration > Notices**.

FAQs
^^^^

Are notices enabled by default?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notices are enabled by default for all Mattermost users. System Admins may choose to disable administrator or end user notices in **System Console > Site Configuration > Notices**.

Will I still receive notices if my workspace is air-gapped?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, the Mattermost workspace requires a connection to the internet to receive notices.

How often will users receive notices?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notices will be used to raise awareness of new features as part of our monthly release cadence. Users will only receive notices that specifically apply to them. For example, if a user is already running the latest Desktop App version, they will not receive an upgrade notice.

Emoji
-----

There are three different settings that allow you to control emoji.

1. **Enable Emoji Picker:** An emoji picker that allows users to select emojis to add as reactions or use in messages. Enabling the emoji picker with a large number of Custom Emojis may slow down performance.
2. **Enable Custom Emoji:** You can control whether or not the Custom Emoji option in the Main Menu, where users can go to create customized emoji, is accessible.
3. **Restrict Custom Emoji Creation:** You can set which role is able to create Custom Emoji from **Main Menu > Custom Emoji** (all users, System and Team Admins, or System Admins only).

File Sharing and Downloads
--------------------------

There are three different settings that allow you to control file sharing and file downloading on your workspace and on mobile devices.

1. **Allow File Sharing:** When configuration is set to **false**, file sharing is disabled. All file and image uploads on messages are forbidden across clients and devices, including mobile.
2. **Allow File Uploads on Mobile:** When configuration is set to **false**, disables file uploads on mobile apps. All file and image uploads on messages are forbidden across clients and devices, including mobile.
3. **Allow File Downloads on Mobile:** When configuration is set to **false**, disables file downloads on mobile apps. Users can still download files from a mobile web browser.

Localization
------------

Mattermost can be localized into 16 languages. You can set the default language for newly-created users and pages where the user hasn't logged in and which languages are available for users in **Account Settings > Display > Languages**. 

New languages are added automatically by default. You can add new languages using the dropdown menu manually as they become available. If you're manually adding new languages, the Default Client Language must be added before saving the setting.

Notifications
-------------

There are seven different settings that allow you to control notifications.

1. **Show @channel and @all confirmation dialog:** Users will be prompted to confirm when posting @channel and @all in channels with over five members.
2. **Email Notification Contents:** You can specify the content shown in email notifications. 
  - **Send full message contents** will include Sender name and channel in email notifications. 
  - **Send generic description with only sender name** will include the team name and name of the person who sent the message. No information about channel name or message contents, is included in email notifications. This is typically used for compliance reasons if Mattermost contains confidential information and policy dictates it cannot be stored in email.
3. **Notification Display Name:** Set the name displayed on the email account used when sending notification emails from Mattermost system.
4. **Notification From Address:** Set the address displayed on the email account used when sending notification emails from within Mattermost. So you don't miss messages, please make sure to change this value to an email your system administrator receives, such as "admin@yourcompany.com".
5. **Notification Reply-To Address:** Set the email address used in the Reply-To header when sending notification emails from Mattermost.
6. **Notification Footer Mailing Address:** Set the name and mailing address displayed in the footer of email notifications from Mattermost, such as *ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA*. If the field is left empty, the organization name and mailing address will not be displayed.
7. **Push Notification Contents:** You can configure what information is provided in push notifications. 
  - **Generic description with only sender name** will include only the name of the person who sent the message but no information about channel name or message text. 
  - **Generic description with sender and channel names** will include names of users and channels but no specific details from the message text. 
  - **Full message content sent in the notification payload** sends excerpts from messages triggering notifications with specifics and may include confidential information sent in messages.  
  - **Only Push Notifications** means full message content is fetched from Mattermost on receipt. The notification payload relayed through the Apple Push Notification service or Firebase Cloud Messaging service contains no message content. Instead it contains a unique message ID used to fetch message content from Mattermost when a push notification is received by a device via a notification service app extention on iOS or an expandable notification pattern on Android. If Mattermost cannot be reached, a generic push notification message is displayed without message content or sender name. For customers who choose to wrap the Mattermost mobile application in a secure container, such as BlackBerry Dymanics, MobileIron, AirWatch or other solutions, the container needs to execute the fetching of message contents from the unique message ID when push notification are received. If the container is unable to execute the fetch, the push notification contents cannot be received by the customer's mobile application without passing the message contents through either the Apple Push Notification service or Firebase Cloud Messaging service.

Posts
-----

There are five different settings that allow you to control content in posts.

1. **Enable Link Previews:** Link previews are previews of linked website content, image links, and YouTube videos that are displayed below posts when available.Users can enable or disable website previews for themselves from **Account Settings > Display > Website Link Previews**. You can also disable all website link previews, image link previews, and YouTube previews by changing this setting to false.
2. **Enable SVGs:** Controls whether users have the ability to see previews of SVG file attachments and SVG image links.
3. **Enable LaTeX Rendering:** Controls users' ability to render LaTeX code.
4. **Custom URL Schemes:** A list of URL schemes that are used for autolinking in message text. HTTP, HTTPS, FTP, tel, and mailto always create links.
5. **Google API Key:** Mattermost offers the ability to embed YouTube videos from URLs shared by end users. Set this key and add YouTube Data API v3 as a service to your key to enable the display of titles for embedded YouTube video previews. Without the key, YouTube previews will still be created based on hyperlinks appearing in messages or comments but they will not show the video title. If Google detects the number of views is exceedingly high, they may throttle embed access. Should this occur, you can remove the throttle by registering for a Google Developer Key and entering it in this field following these instructions: https://www.youtube.com/watch?v=Im69kzhpR3I. Your Google Developer Key is used in client-side Javascript. Using a Google API Key allows Mattermost to detect when a video is no longer available and display the post with a Video not found label.

Public Links
------------

Enabling Public File Links allows users to generate public links to files and images for sharing outside the Mattermost system with a public URL.

When disabled, the Get Public Link option is hidden from the image preview user interface. Anyone who tries to visit a previously generated public link will receive an error message saying public links have been disabled. When switched back to True, old public links will work again unless the Public Link salt has been regenerated.

Users and Teams
---------------

There are seven different settings that allow you to control users and teams.

1. **Max Users Per Team:** The Max Users Per Team refers to the size of the *team site* which is a workspace a *team of people* inhabits. A team of people is considered a small organization where people work closely together towards a specific shared goal and share the same etiquette. In the physical world, a team of people could typically be seated around a single table to have a meal and discuss their project. The default maximum of 1000 people is at the extreme high end of a single team of people. At this point organizations are more often 'multiple teams of people' and investments in explicitly defining etiquette, such as channel organization or turning on policy features in Enterprise Edition, are often used to scale the high levels of productivity found in a team of people using Mattermost to multiple teams of people.
2. **Max Channels Per Team:** Set the maximum number of channels per team, including both active and deleted channels.
3. **Enable users to open Direct Message channels with:** You can configure whether users can message any user on the Mattermost workspace or only users in the same team as them. This setting adjusts the users returned in the Direct Messages **More** menu and CTRL/CMD+K channel switcher only lists users on the current team. This setting only affects the UI, not permissions on the workspace. For instance, a Direct Message channel can be created with anyone on the workspace regardless of this setting.
4. **Teammate Name Display:** Specifies how names are displayed in the user interface by default. Please note that users can override this setting in **Account Settings > Display > Teammate Name Display**. 
  - **Show username** displays the user's username. 
  - **Show nickname** if one exists displays the user's nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed. 
  - **Show first and last name** displays the user's full name. If the user does not have a full name, their username is displayed. Recommended when using SAML or LDAP if first name and last name attributes are configured.
5. **Allow Users to View Archived Channels (Beta):** Allows users to view, share, and search for content of channels that have been archived. Users can only view the content in channels of which they were a member before the channel was archived.
6. **Show Email Address:** When set to **false**, this setting hides email address of users from other users in the user interface, including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see email addresses in the UI.
7. **Show Full Name:** WHen set to false, this setting hides full name of users from other users including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see full names in the UI.
