Bulk export data
=================
At this time, the export supports attributes of the objects listed below. All Mattermost Bulk Export data files will begin with a `Version` object as the first line of the file. This indicates the version of the Mattermost Bulk Import file format with which the exported data is compatible.

You can export the following data types:

- Teams
- Channels (Public and Private)
- Users
- Users' Team memberships
- Users' Channel memberships
- Users' notification preferences
- Posts (regular, non-reply posts)
- Posts' Replies
- Posts' Reactions
- Custom Emoji
- Direct Message Channels 
- Direct Message Posts

Configuration for exporting specific areas of the server, exporting additional types of posts, permissions schemes, file attachments, webhooks and bot messages are not yet supported. Deleted objects are also not yet supported.  

For requests to add additional attributes or objects to our exporter, please add a feature request on our `feature idea forum <https://mattermost.uservoice.com/forums/306457-general>`__.  

Version object
--------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">string</td>
      <td>The string "version"</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">version</td>
      <td valign="middle">number</td>
      <td>The number 1.</td>
    </tr>
  </table>
  
Team object
-----------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The team name.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">display_name</td>
      <td valign="middle">string</td>
      <td>The display name for the team.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">string</td>
      <td>The type of team. Will have one the following values:<br>
          <kbd>"O"</kbd> for an open team<br>
          <kbd>"I"</kbd> for an invite-only team.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">description</td>
      <td valign="middle">string</td>
      <td>The team description.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">allow_open_invite</td>
      <td valign="middle">bool</td>
      <td>Whether to allow open invitations. Will have one of the following values:<br>
        <kbd>true</kbd><br>
        <kbd>false</kbd>
      </td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">scheme</td>
      <td valign="middle">string</td>
      <td>The name of the permissions scheme that applies to this team.</td>
    </tr>
  </table>

Channel object
--------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">string</td>
      <td>The name of the team this channel belongs to.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The name of the channel.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">display_name</td>
      <td valign="middle">string</td>
      <td>The display name for the channel.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">string</td>
      <td>The type of channel. Will have one the following values:<br>
          <kbd>"O"</kbd> for a public channel.<br>
          <kbd>"P"</kbd> for a private channel.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">header</td>
      <td valign="middle">string</td>
      <td>The channel header.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">purpose</td>
      <td valign="middle">string</td>
      <td>The channel purpose.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">scheme</td>
      <td valign="middle">string</td>
      <td>The name of the permissions scheme that applies to this team.</td>
    </tr>
  </table>
  
User object
-----------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">username</td>
      <td valign="middle">string</td>
      <td>The user’s username. This is the unique identifier for the user.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">email</td>
      <td valign="middle">string</td>
      <td>The user’s email address.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_service</td>
      <td valign="middle">string</td>
      <td>The authentication service used for this user account. This field will be absent for user/password authentication.<br>
        <kbd>"gitlab"</kbd> - GitLab authentication.<br>
        <kbd>"ldap"</kbd> - LDAP authentication (E10 and E20)<br>
        <kbd>"saml"</kbd> - Generic SAML based authentication (E20)<br>
        <kbd>"google"</kbd> - Google OAuth authentication (E20)<br>
        <kbd>"office365"</kbd> - Microsoft Office 365 OAuth Authentication (E20)</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_data</td>
      <td valign="middle">string</td>
      <td>The authentication data if <kbd>auth_service</kbd> is used. The value depends on the <kbd>auth_service</kbd> that is specified.<br>
        The data comes from the following fields for the respective auth_services:<br>
        <kbd>"gitlab"</kbd> - The value of the Id attribute provided in the Gitlab auth data.<br>
        <kbd>"ldap"</kbd> - The value of the LDAP attribute specified as the "ID Attribute" in the Mattermost LDAP configuration.<br>
        <kbd>"saml"</kbd> - The value of the SAML Email address attribute.<br>
        <kbd>"google"</kbd> - The value of the OAuth Id attribute.<br>
        <kbd>"office365"</kbd> - The value of the OAuth Id attribute.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">nickname</td>
      <td valign="middle">string</td>
      <td>The user’s nickname.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">first_name</td>
      <td valign="middle">string</td>
      <td>The user’s first name.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">last_name</td>
      <td valign="middle">string</td>
      <td>The user’s last name.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">position</td>
      <td valign="middle">string</td>
      <td>The user’s position.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roles</td>
      <td valign="middle">string</td>
      <td>The user’s roles. </td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">locale</td>
      <td valign="middle">string</td>
      <td>The user’s localization configuration.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">use_markdown_preview</td>
      <td valign="middle">bool</td>
      <td>"True" if the user has enabled markdown preview in the message input box.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">use_formatting</td>
      <td valign="middle">bool</td>
      <td>"True" if the user has enabled post formatting for links, emoji, text styles and line breaks.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">show_unread_section</td>
      <td valign="middle">string</td>
      <td>"True" if the user has enabled showing unread messages at top of channel sidebar.</td>
    </tr> 
    <tr class="row-odd">
      <td valign="middle">theme</td>
      <td valign="middle">string</td>
      <td>The user’s theme. Formatted as a Mattermost theme string.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">military_time</td>
      <td valign="middle">string</td>
      <td>"True" if the user has enabled a 24 hour clock. "False" if using a 12 hour clock.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">collapse_previews</td>
      <td valign="middle">string</td>
      <td>"True" if user collapses link preview by default. "False" is user expands link previews by default.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message_display</td>
      <td valign="middle">string</td>
      <td>The style the user prefers for displayed messages. Options are "clean" if the user uses the standard style or "compact" if the user uses compact style.</td>
    </tr> 
    <tr class="row-odd">
      <td valign="middle">channel_display_mode</td>
      <td valign="middle">string</td>
      <td>"Full" if the users displays channel messages at the full width of the screen or "centered" if the user uses a fixed width, centered block</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">tutorial_step</td>
      <td valign="middle">string</td>
      <td>"1", "2" or "3" indicates which specified tutorial step to start with for the user. "999" skips the tutorial.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">email_interval</td>
      <td valign="middle">string</td>
      <td>Email batching interval to use during bulk import. </td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">delete_at</td>
      <td valign="middle">int64</td>
      <td>Timestamp of when the user was deactivated.</td>
    </tr>    
    <tr class="row-odd">
      <td valign="middle">teams</td>
      <td valign="middle">array</td>
      <td>The teams which the user is member of. Is an array of <b>UserTeamMembership</b> objects.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">notify_props</td>
      <td valign="middle">object</td>
      <td>The user’s notify preferences, as defined by the <b>UserNotifyProps</b> object.</td>
    </tr>
  </table>

UserNotifyProps object
----------------------
This object is a member of the User object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">string</td>
      <td>Preference for sending desktop notifications. Will be one of the following values:<br>
      <kbd>"all"</kbd> - For all activity.<br>
      <kbd>"mention"</kbd> - Only for mentions.<br>
      <kbd>"none"</kbd> - Never.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop_sound</td>
      <td valign="middle">string</td>
      <td>Preference for whether desktop notification sound is played. Will be one of the following values:<br>
      <kbd>"true"</kbd> - Sound is played.<br>
      <kbd>"false"</kbd> - Sound is not played.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">email</td>
      <td valign="middle">string</td>
      <td>Preference for email notifications. Will be one of the following values:<br>
      <kbd>"true"</kbd> - Email notifications are sent immediately.<br>
      <kbd>"false"</kbd> - Email notifications are not sent.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile</td>
      <td valign="middle">string</td>
      <td>Preference for sending mobile push notifications. Will be one of the following values:<br>
      <kbd>"all"</kbd> - For all activity.<br>
      <kbd>"mention"</kbd> - Only for mentions.<br>
      <kbd>"none"</kbd> - Never.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile_push_status</td>
      <td valign="middle">string</td>
      <td>Preference for when push notifications are triggered. Will be one of the following values:<br>
      <kbd>"online"</kbd> - When online, away or offline.<br>
      <kbd>"away"</kbd> - When away or offline.<br>
      <kbd>"offline"</kbd> - When offline.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channel</td>
      <td valign="middle">string</td>
      <td>Preference for whether @all, @channel and @here trigger mentions. Will be one of the following values:<br>
      <kbd>"true"</kbd> - Mentions are triggered.<br>
      <kbd>"false"</kbd> - Mentions are not triggered.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">comments</td>
      <td valign="middle">string</td>
      <td>Preference for reply mention notifications. Will be one of the following values:<br>
      <kbd>"any"</kbd> - Trigger notifications on messages in reply threads that the user starts or participates in.<br>
      <kbd>"root"</kbd> - Trigger notifications on messages in threads that the user starts.<br>
      <kbd>"never"</kbd> - Do not trigger notifications on messages in reply threads unless the user is mentioned.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mention_keys</td>
      <td valign="middle">string</td>
      <td>Preference for custom non-case sensitive words that trigger mentions. Words are separated by commas.</td>
    </tr>
  </table>


UserTeamMembership object
-------------------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The name of the team this user is a member of.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roles</td>
      <td valign="middle">string</td>
      <td>The roles the user has within this team. </td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">theme</td>
      <td valign="middle">string</td>
      <td>The user’s theme for this team. Formatted as a Mattermost theme string.</td>
    </tr>
     <tr class="row-odd">
      <td valign="middle">channels</td>
      <td valign="middle">array</td>
      <td>The channels within this team that the user is a member of. Listed as an array of <b>UserChannelMembership</b> objects.</td>
    </tr>
  </table>

UserChannelMembership object
----------------------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The name of the channel in the parent team that this user is a member of.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roles</td>
      <td valign="middle">string</td>
      <td>The roles the user has within this channel. </td>
    </tr>
        <tr class="row-odd">
      <td valign="middle">notify_props</td>
      <td valign="middle">object</td>
      <td>The notify preferences for this user in this channelas defined by the <b>ChannelNotifyProps</b> object.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">favorite</td>
      <td valign="middle">boolean</td>
      <td>Whether the channel is marked as a favorite for this user. Will be one of the following values<br>
          <kbd>"true"</kbd> - Yes.<br>
          <kbd>"false"</kbd> - No.</td>
      </td>
    </tr>
  </table>

ChannelNotifyProps object
~~~~~~~~~~~~~~~~~~~~~~~~~

This object is a member of the ChannelMembership object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">string</td>
      <td>Preference for sending desktop notifications. Will be one of the following values:<br>
      <kbd>"default"</kbd> - Global default.<br>
      <kbd>"all"</kbd> - For all activity.<br>
      <kbd>"mention"</kbd> - Only for mentions.<br>
      <kbd>"none"</kbd> - Never.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile</td>
      <td valign="middle">string</td>
      <td>Preference for sending mobile notifications. Will be one of the following values:<br>
      <kbd>"default"</kbd> - Global default.<br>
      <kbd>"all"</kbd> - For all activity.<br>
      <kbd>"mention"</kbd> - Only for mentions.<br>
      <kbd>"none"</kbd> - Never.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mark_unread</td>
      <td valign="middle">string</td>
      <td>Preference for marking channel as unread. Will be one of the following values:<br>
          <kbd>"all"</kbd> - For all unread messages.<br>
          <kbd>"mention"</kbd> - Only for mentions.
      </td>
    </tr>
  </table>

Post object
-----------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">string</td>
      <td>The name of the team that this post is in.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channel</td>
      <td valign="middle">string</td>
      <td>The name of the channel that this post is in.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this post.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message</td>
      <td valign="middle">string</td>
      <td>The message that the post contains.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">props</td>
      <td valign="middle">object</td>
      <td>The props for a post. Contains additional formatting information used by integrations and bot posts. For a more detailed explanation see the <a href="https://docs.mattermost.com/developer/message-attachments.html">message attachments documentation</a>.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the post, in milliseconds since the Unix epoch.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">reactions</td>
      <td valign="middle">array</td>
      <td>The emoji reactions to this post. Will be an array of Reaction objects.</td>
  </table>
  
Reply object
------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this reply.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message</td>
      <td valign="middle">string</td>
      <td>The message that the reply contains.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the reply, in milliseconds since the Unix epoch.</td>
    </tr>
  </table>
  
Reaction object
---------------

This object is a member of the Post object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this reply.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">emoji_name</td>
      <td valign="middle">string</td>
      <td>The emoji of the reaction.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the reply, in milliseconds since the Unix epoch.</td>
    </tr>
  </table>

Emoji object
------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The emoji name.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">image</td>
      <td valign="middle">string</td>
      <td>The path (either absolute or relative to the current working directory) to the image file for this emoji.</td>
    </tr>
  </table>
  
DirectChannel object
----------------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">members</td>
      <td valign="middle">array</td>
      <td>List of channel members.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">header</td>
      <td valign="middle">string</td>
      <td>The channel header.</td>
    </tr>
  </table>
  
DirectPost object
----------------------
.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this post.</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message</td>
      <td valign="middle">string</td>
      <td>The message that the post contains.</td>
    </tr>
        <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the post, in milliseconds since the Unix epoch.</td>
  </table>
