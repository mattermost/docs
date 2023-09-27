Mention people in messages
==========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

When you want to get the attention of specific Mattermost users, you can use @mentions. Mattermost supports the following types of @mentions:

- `@username <#username>`__
- `@channel <#channel-and-all>`__
- `@all <#channel-and-all>`__
- `@here <#here>`__
- `@groupname <#groupname>`__

.. note::

  - If you forget to mention someone in a message, editing the existing message to add an @mention won't trigger new @mention notifications, desktop notifications, or notification sounds.
  - Mattermost supports mentions for names that include accents (also known as diacritics). Names like Zoë, Jesús, Sørina, François, André, Jokūbas, Siân, KŠthe, or Fañch are returned in autocomplete results.

@username
---------

You can mention a teammate by using the *@* symbol plus their username to send them a mention notification.

Type *@* to bring up a list of team members who can be mentioned. To filter the list, type the first few letters of any username, first name, last name, or nickname. 

.. tip::
  
  Using Mattermost in a web browser or the desktop app, you can also press the :kbd:`↑` and :kbd:`↓` arrow keys to scroll through entries in the list, and press :kbd:`ENTER` on Windows or Linux, or :kbd:`↵` on Mac, to select the person to mention. When selected, the username replaces the full name or nickname.

The following example sends a special mention notification to Alice, whose username is **alice**. The notification alerts her of the channel and message where she was mentioned. If Alice is away from Mattermost and has email notifications turned on, she'll receive an email alert of her mention along with the message text.

.. code-block:: none

  @alice how did your interview go with the new candidate?

If the person you mentioned doesn't belong to the channel, a system message is posted to let you know, and you're given the option to add the person to the channel. You are the only one who can see this message.

@channel and @all
-----------------

You can mention an entire channel by typing ``@channel`` or ``@all``. All members of the channel receive a mention notification that behaves the same way as if the members had been mentioned personally. If used in Town Square, it notifies all members of your team.

You can ignore channel-wide mentions in specific channels in the **Channel Menu > Notification Preferences > Ignore mentions for @channel, @here and @all**.

.. code-block:: none

  @channel great work on interviews this week. I think we found some excellent potential candidates!

If a channel has five or more members, you may be prompted to confirm that you want notifications sent to everyone in the channel.

@here
-----

You can mention everyone who is online in a channel by typing ``@here``. This sends a desktop notification and push notification to members of the channel who are online. It's counted as a mention in the sidebar. Members who are offline don't receive a notification. When they return to Mattermost they won't see a mention counted in the channel sidebar. Members who are away receive a desktop notification only if they have notifications set to **For all activity**, and they won't see a mention counted in the sidebar.

.. code-block:: none

  @here can someone complete a quick review of this?

If a channel has five or more members, you may be prompted to confirm that you want notifications sent to everyone in the channel.
  
You can ignore channel-wide mentions in specific channels by enabling the **Channel Menu > Notification Preferences > Ignore mentions for @channel, @here, and @all** option.
  
@groupname
----------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

This feature enables system admins to configure custom mentions for `LDAP synced groups </onboard/ad-ldap-groups-synchronization.html>`__ via the Group Configuration page. This functionality is also supported on the mobile app (from v1.34) if the AD/LDAP groups feature is enabled. The mobile app supports auto-suggesting groups, highlights group member mentions, and also provides a warning dialog when a mention will notify more than five users.

Once enabled for a specific group, users can mention and notify the entire group in a channel (similar to ``@channel`` or ``@all``). Members of the group in that channel will receive a notification. If members of the group mentioned aren't members of the channel, the user who posted the mention is prompted to invite them.

Group mention identifiers (slugs) use the LDAP group name by default. To customize/rename the slug:

1. Open **System Console > User Management > Groups**.
2. Select **Edit** next to the group you want to edit.
3. In **Group Profile > Group Mention** enter the new slug.
4. Select **Save**.

As with ``@username`` mentions, use *@* to bring up a list of groups that can be mentioned. To filter the list, type the first few letters of any group. Press the :kbd:`↑` and :kbd:`↓` arrow keys to scroll through entries in the list, and then press :kbd:`Enter` on Windows or Linux, or pressing :kbd:`↵` on Mac to select the group you want to mention.

.. code-block:: none

  @dev-managers great work hitting all of our code coverage goals this quarter!

Words that trigger mentions
---------------------------

You can customize words that trigger mention notifications in **Settings > Notifications > Words That Trigger Mentions**. By default, you receive mention notifications for your username and for ``@channel``, ``@all`` and ``@here``. You can choose to have your first name be a word that triggers mentions.

You can add a list of customized words to get mention notifications for by typing them into the input box, separated by commas. This is useful if you want to be notified of all posts on certain topics, such as "interviewing" or "marketing".

See all recent mentions
-----------------------

Select **@** to the right of the **Search** box to query for your most recent @mentions and words that trigger mentions (excluding LDAP group mentions).

.. image:: ../images/recent-mentions.png
   :alt: See your most recent @mentions

Your recent mentions are shown for all of your teams.
    
Select **Jump** next to a search result in the right-hand sidebar to jump the center pane to the channel and location of the message with the mention.

Confirmation dialog warnings
----------------------------

When your system admin has configured Mattermost to require confirmations for @messages, you must confirm any mention that will trigger notifications for more than five users before sending the notification.

This confirmation dialog only appears when your system admin has configured this setting in the System Console. See our `configuration settings </configure/configuration-settings.html#show-channel-all-or-here-confirmation-dialog>`__ product documentation for details. This configuration setting is supported on the Mattermost Mobile App (from v1.34) if the `AD/LDAP groups </onboard/ad-ldap-groups-synchronization.html>`__ feature is enabled.

Mention highlights
------------------

Valid mentions will have highlighted font text with some exceptions, for example if mentions are disabled at the channel level. The highlighted text becomes a hyperlink when a username is displayed. When the username is selected, the profile popover is displayed.

When mentions trigger a notification, the user being notified will see highlighted font text and highlighted font background. This functions as an identifier of which mentions in the post triggered a notification for the user.
