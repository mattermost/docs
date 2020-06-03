.. _mentioning-teammates:

Mentioning Teammates
====================


@Mentions
---------

Use @mentions to get the attention of specific team members. 

Note that editing a message does not trigger new @mention notifications, desktop notifications, or notification sounds.


@username
~~~~~~~~~

You can mention a teammate by using the *@* symbol plus their username to send them a mention notification.

Type *@* to bring up a list of team members who can be mentioned. To filter the list, type the first few letters of any username, first name, last name, or nickname. Use the UP and DOWN arrow keys to scroll through entries in the list, and then press ENTER to select the person to mention. When selected, the username replaces the full name or nickname.

The following example sends a special mention notification to Alice, whose username is **alice**. The notification alerts her of the channel and message where she was mentioned. If Alice is away from Mattermost and has email notifications turned on, then she receives an email alert of her mention along with the message text.

.. code-block:: none

  @alice how did your interview go with the new candidate?

If the person you mentioned does not belong to the channel, a System Message is posted to let you know. This is a temporary message, and you are the only one who can see it. To add the mentioned person to the channel, go to the dropdown menu beside the channel name and select **Add Members**.

@channel and @all
~~~~~~~~~~~~~~~~~

You can mention an entire channel by typing ``@channel`` or ``@all``. All members of the channel receive a mention notification that behaves the same way as if the members had been mentioned personally. If used in Town Square, it notifies all members of your team. 

You can ignore channel-wide mentions in specific channels in the **Channel Menu > Notification Preferences > Ignore mentions for @channel, @here and @all**.

.. code-block:: none

  @channel great work on interviews this week. I think we found some excellent potential candidates!

If a channel has five or more members, you are prompted to confirm that you want notifications sent to everyone in the channel.

@here
~~~~~

You can mention everyone who is online in a channel by typing ``@here``. This sends a desktop notification and push notification to members of the channel who are online. It's counted as a mention in the sidebar. Members who are offline do not receive a notification, and when they come back to the site they will not see a mention counted in the channel sidebar. Members who are away receive a desktop notification only if they have notifications set to "all activity", and they will not see a mention counted in the sidebar.

You can ignore channel-wide mentions in specific channels in the **Channel Menu > Notification Preferences > Ignore mentions for @channel, @here and @all**.

.. code-block:: none

  @here can someone do a quick review of this?
  
@groupname (BETA)(E20)
~~~~~

System Admins can enable mentions for `LDAP synced groups <https://docs.mattermost.com/deployment/ldap-group-sync.html>`_ via the Group Configuration page.

**Note**: This functionality is not yet supported on mobile.

Once enabled for a specific group, users will be able to mention and notify the entire group (similar to @channel or @all). Every member of the group who is also present in the channel the mention was posted, will receive a notification. If members of the group mentioned are not members of the channel, the user who posted the mention is prompted to invite them.

Group mention identifiers (slugs) use the LDAP group name by default, but they can be customized and renamed.

Group mention identfiers (slugs) use the LDAP group name by defualt, but they can also be custmoized/renamed. 

As with @username mentions, use *@* to bring up a list of groups that can be mentioned. To filter the list, type the first few letters of any group. Use the UP and DOWN arrow keys to scroll through entries in the list, and then press ENTER to select the group to mention.

.. code-block:: none

  @dev-managers great work hitting all of our code coverage goals this quarter!


Words That Trigger Mentions
---------------------------

You can customize words that trigger mention notifications in **Account Settings > Notifications > Words that trigger mentions**. By default, you receive mention notifications for your username and for *@channel*, *@all* and *@here*. You can choose to have your first name be a word that triggers mentions.

You can add a list of customized words to get mention notifications for by typing them into the input box, separated by commas. This is useful if you want to be notified of all posts on certain topics, such as "interviewing" or "marketing".

Recent Mentions
---------------

Click **@** next to the search box to query for your most recent @mentions and words that trigger mentions (excluding LDAP group mentions). Click **Jump** next to a search result in the right-hand sidebar to jump the center pane to the channel and location of the message with the mention.

Confirmation dialogue warnings
---------------

Any mention that will trigger notifications for over five users, a confirmation dialog will appear requiring confirmation from the user posting the mention before sending notifications to those users. 
*Dialog will only appear when the following setting is enabled: TeamSettings.EnableConfirmNotificationsToChannel*
*This warning is not displayed for group mentions on mobile*

Highlighting
---------------

All valid mentions will have highlighted font text (with some exceptions, for example if mentions are disabled at the channel level). This text becomes a hyperlink when it displays a username. When clicked, the profile popover is displayed. 

All mentions that trigger a notification, the user who is being notified will see highlighted font text and highlighted font background. This functions as an identifier of what mentions in the post triggered a notification for the user.
