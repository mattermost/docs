.. _data-format:

Data Format
===========

The input data file must be a valid `JSONL
<http://jsonlines.org>`_ file with the following objects, each on its own line in the file. The objects must occur in the file in the order listed.

Version
  Mandatory. The Version object must be the first line in the file, and must occur only once.
Team
  Optional. If present, Team objects must occur after the Version object and before any Channel objects.
Channel
  Optional. If present, Channel objects must occur after all Team objects and before any User objects.
User
  Optional. If present, User objects must occur after the Team and Channel objects in the file and before any Post objects. Each User object defines the teams and channels that the user is a member of. If the corresponding teams and channels are not in the data file, then they must exist in the Mattermost database.
Post
  Optional. If present, Post objects must occur after the last User object but before any DirectChannel objects. Each Post object defines the team, the channel, and the username of the user who posted the message. If the corresponding team, channel, or user are not in the data file, then they must exist in the Mattermost database.
DirectChannel
  Optional. If present, DirectChannel objects must occur after all Post objects in the file and before any DirectPost objects.
DirectPost
  Optional. If present, DirectPost objects must occur after all other objects in the file. Each DirectPost object defines the usernames of the channel members and the username of the user who posted the message. If the corresponding usernames are not in the data file, then they must exist in the Mattermost database.

With the exception of the Version object, each object has a field or a combination of fields that is used as the unique identifier of that object. The bulk loader uses the unique identifier to determine if the object being imported is a new object or an update to an existing object.

The identifiers for each object are listed in the following table:

.. csv-table:: Objects and their unique identifiers
  :header: Object, Unique Identifier

  Version, Not Applicable
  Team, *name*
  Channel, "*name*, *team*"
  User, *username*
  UserNotifyProps, *username*
  UserTeamMembership, "*team*, *username*"
  UserChannelMembership, "*team*, *channel*, *username*"
  Post, "*channel*, *message*, *create_at*"
  Reply, "*post*, *message*, *create_at*"
  Reaction, "*post*, *emoji_name*, *create_at*"
  DirectChannel, *members*
  DirectPost,  "*channel_members*, *user*, *message*, *create_at* "

The following fragment is from a file that imports two teams, each with two channels, many users, and many posts.

.. code-block:: javascript
  :linenos:

  { "type": "version", ... }
  { "type": "team", "team": { "name": "TeamA", ...} }
  { "type": "team", "team": { "name": "TeamB", ...} }
  { "type": "channel", "channel": { "team": "TeamA", "name": "ChannelA1", ...} }
  { "type": "channel", "channel": { "team": "TeamA", "name": "ChannelA2", ...} }
  { "type": "channel", "channel": { "team": "TeamB", "name": "ChannelB1", ...} }
  { "type": "channel", "channel": { "team": "TeamB", "name": "ChannelB1", ...} }
  { "type": "user", "user": { "username": "user001", ...} }
  { "type": "user", "user": { "username": "user002", ...} }
  { "type": "user", "user": { "username": "user003", ...} }
  { "type": "user", ... }
  { "type": "user", ... }
  { "type": "user", ... }
  .
  .
  .
  { "type": "post", { "team": "TeamA", "name": "ChannelA1", "user": "user001", ...} }
  { "type": "post", { "team": "TeamA", "name": "ChannelA1", "user": "user001", ...} }
  { "type": "post", { "team": "TeamA", "name": "ChannelA1", "user": "user001", ...} }
  .
  .
  .

Version object
--------------

The Version object must be the first object in the data file, and can appear only once.

Example Version object
~~~~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
    "type": "version",
    "version": 1
  }

Fields of the Version object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">string</td>
      <td>Must be the string "version"</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">version</td>
      <td valign="middle">number</td>
      <td>Must be the number 1.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
  </table>

Team object
-----------

If present, Team objects must occur after the Version object and before any Channel objects.

Example Team object
~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
  "type": "team",
  "team": {
    "name": "team-name",
    "display_name": "Team Display Name",
    "type": "O",
    "description": "The Team Description",
    "allow_open_invite": true
    }
  }

Fields of the Team object
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The team name.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">display_name</td>
      <td valign="middle">string</td>
      <td>The display name for the team.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">type</td>
      <td valign="middle">string</td>
      <td>The type of team. Can have one the following values:<br>
          <kbd>"O"</kbd> for an open team<br>
          <kbd>"I"</kbd> for an invite-only team.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">description</td>
      <td valign="middle">string</td>
      <td>The team description.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">allow_open_invite</td>
      <td valign="middle">bool</td>
      <td>Whether to allow open invitations. Must have one of the following values:<br>
        <kbd>true</kbd><br>
        <kbd>false</kbd>
      </td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

Channel object
--------------

If present, Channel objects must occur after all Team objects and before any User objects.

Example Channel object
~~~~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
    "type": "channel",
    "channel": {
      "team": "team-name",
      "name": "channel-name",
      "display_name": "Channel Name",
      "type": "O",
      "header": "The Channel Header",
      "purpose": "The Channel Purpose",
    }
  }

Fields of the Channel object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[1] Not validated, but an error occurs if no such team exists when running in apply mode.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">string</td>
      <td>The name of the team this channel belongs to.</td>
      <td align="center" valign="middle">No [1]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
  <tr class="row-odd">
    <td valign="middle">name</td>
    <td valign="middle">string</td>
    <td>The name of the channel.</td>
    <td align="center" valign="middle">Yes</td>
    <td align="center" valign="middle">Yes</td>
  </tr>
  <tr class="row-odd">
    <td valign="middle">display_name</td>
    <td valign="middle">string</td>
    <td>The display name for the channel.</td>
    <td align="center" valign="middle">Yes</td>
    <td align="center" valign="middle">yes</td>
  </tr>
  <tr class="row-odd">
    <td valign="middle">type</td>
    <td valign="middle">string</td>
    <td>The type of channel. Can have one the following values:<br>
        <kbd>"O"</kbd> for a public channel.<br>
        <kbd>"P"</kbd> for a private channel.</td>
    <td align="center" valign="middle">Yes</td>
    <td align="center" valign="middle">Yes</td>
  </tr>
  <tr class="row-odd">
    <td valign="middle">header</td>
    <td valign="middle">string</td>
    <td>The channel header.</td>
    <td align="center" valign="middle">Yes</td>
    <td align="center" valign="middle">No</td>
  </tr>
  <tr class="row-odd">
    <td valign="middle">purpose</td>
    <td valign="middle">string</td>
    <td>The channel purpose.</td>
    <td align="center" valign="middle">Yes</td>
    <td align="center" valign="middle">No</td>
  </tr>
  </table>

User object
-----------

If present, User objects must occur after the Team and Channel objects in the file and before any Post objects.

Example User object
~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
    "type": "user",
    "user": {
      "profile_image": "avatar.png",
      "username": "username",
      "email": "email@example.com",
      "auth_service": "",
      "auth_data": "",
      "password": "passw0rd",
      "nickname": "bobuser",
      "first_name": "Bob",
      "last_name": "User",
      "position": "Senior Developer",
      "roles": "system_user",
      "locale": "pt_BR",
      "teams": [
        {
          "name": "team-name",
          "roles": "team_user team_admin",
          "channels": [
            {
              "name": "channel-name",
              "roles": "channel_user",
              "notify_props": {
                "desktop": "default",
                "mark_unread": "all"
              }
            }
          ]
        }
      ]
    }
  }

Fields of the User object
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">profile_image</td>
      <td valign="middle">string</td>
      <td>The user’s profile image. This must be an existing file path.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">username</td>
      <td valign="middle">string</td>
      <td>The user’s username. This is the unique identifier for the user.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">email</td>
      <td valign="middle">string</td>
      <td>The user’s email address.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_service</td>
      <td valign="middle">string</td>
      <td>The authentication service to use for this user account. If not provided, it defaults to password-based authentication. Must be one of the following values:<br>
        <kbd>""</kbd> or not provided - password authentication.<br>
        <kbd>"gitlab"</kbd> - GitLab authentication.<br>
        <kbd>"ldap"</kbd> - LDAP authentication (E10 and E20)<br>
        <kbd>"saml"</kbd> - Generic SAML based authentication (E20)<br>
        <kbd>"google"</kbd> - Google OAuth authentication (E20)<br>
        <kbd>"office365"</kbd> - Microsoft Office 365 OAuth Authentication (E20)</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">auth_data</td>
      <td valign="middle">string</td>
      <td>The authentication data if <kbd>auth_service</kbd> is used. The value depends on the <kbd>auth_service</kbd> that is specified.<br>
        The data comes from the following fields for the respective auth_services:<br>
        <kbd>""</kbd> or not provided - must be omitted.<br>
        <kbd>"gitlab"</kbd> - The value of the Id attribute provided in the Gitlab auth data.<br>
        <kbd>"ldap"</kbd> - The value of the LDAP attribute specified as the "ID Attribute" in the Mattermost LDAP configuration.<br>
        <kbd>"saml"</kbd> - The value of the SAML Email address attribute.<br>
        <kbd>"google"</kbd> - The value of the OAuth Id attribute.<br>
        <kbd>"office365"</kbd> - The value of the OAuth Id attribute.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">password</td>
      <td valign="middle">string</td>
      <td>A password for the user. Can be present only when password-based authentication is used. When password-based authentication is used and the password is not present, the bulk loader generates a password.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">nickname</td>
      <td valign="middle">string</td>
      <td>The user’s nickname.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">first_name</td>
      <td valign="middle">string</td>
      <td>The user’s first name.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">last_name</td>
      <td valign="middle">string</td>
      <td>The user’s last name.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">position</td>
      <td valign="middle">string</td>
      <td>The user’s position.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roles</td>
      <td valign="middle">string</td>
      <td>The user’s roles. Must be one of the following values:<br>
        <kbd>"system_user"</kbd><br>
        <kbd>"system_admin system_user"</kbd></td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">locale</td>
      <td valign="middle">string</td>
      <td>The user’s locale. This must be a valid locale for which Mattermost has been localised.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">teams</td>
      <td valign="middle">array</td>
      <td>The teams which the user will be made a member of. Must be an array of <b>TeamMembership</b> objects.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">theme</td>
      <td valign="middle">string</td>
      <td>The user’s theme. Formatted as a Mattermost theme string.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">use_military_time</td>
      <td valign="middle">string</td>
      <td>How times should be displayed to this user. Must be one of the following values:<br>
        <kbd>"true"</kbd> - Use 24 hour clock.<br>
        <kbd>"false"</kbd> - Use 12 hour clock.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">collapse_previews</td>
      <td valign="middle">string</td>
      <td>Whether to collapse or expand link previews by default. Must be one of the following values:<br>
        <kbd>"true"</kbd> - Collapsed by default.<br>
        <kbd>"false"</kbd> - Expanded by default.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message_display</td>
      <td valign="middle">string</td>
      <td>Which style to use for displayed messages. Must be one of the following values:<br>
        <kbd>"clean"</kbd> - Use the standard style.<br>
        <kbd>"compact"</kbd> - Use the compact style.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channel_display_mode</td>
      <td valign="middle">string</td>
      <td>How to display channel messages. Must be one of the following values:<br>
        <kbd>"full"</kbd> - Use the full width of the screen.<br>
        <kbd>"centered"</kbd> - Use a fixed width, centered block.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">tutorial_step</td>
      <td valign="middle">string</td>
      <td>Where to start the user tutorial. Must be one of the following values:<br>
        <kbd>"1"</kbd>, <kbd>"2"</kbd> or <kbd>"3"</kbd> - Start from the specified tutorial step.<br>
        <kbd>"999"</kbd> - Skip the user tutorial.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

Fields of the UserNotifyProps object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This object is a member of the User object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[1] Not validated, but an error occurs if no such team exists when running in apply mode.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">string</td>
      <td>Preference for sending desktop notifications. Must be one of the following values:<br>
      <kbd>"all"</kbd> - For all activity.<br>
      <kbd>"mention"</kbd> - Only for mentions.<br>
      <kbd>"none"</kbd> - Never.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop_duration</td>
      <td valign="middle">string</td>
      <td>Preference for how long desktop notifications remain on screen. Must be one of the following values:<br>
      <kbd>"3"</kbd> - 3 seconds.<br>
      <kbd>"5"</kbd> - 5 seconds.<br>
      <kbd>"10"</kbd> - 10 seconds.<br>
      <kbd>"0"</kbd> - Unlimited.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop_sound</td>
      <td valign="middle">string</td>
      <td>Preference for whether desktop notification sound is played. Must be one of the following values:<br>
      <kbd>"true"</kbd> - Sound is played.<br>
      <kbd>"false"</kbd> - Sound is not played.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">email</td>
      <td valign="middle">string</td>
      <td>Preference for email notifications. Must be one of the following values:<br>
      <kbd>"true"</kbd> - Email notifications are sent immediately.<br>
      <kbd>"false"</kbd> - Email notifications are not sent.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile</td>
      <td valign="middle">string</td>
      <td>Preference for sending mobile push notifications. Must be one of the following values:<br>
      <kbd>"all"</kbd> - For all activity.<br>
      <kbd>"mention"</kbd> - Only for mentions.<br>
      <kbd>"none"</kbd> - Never.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mobile_push_status</td>
      <td valign="middle">string</td>
      <td>Preference for when push notifications are triggered. Must be one of the following values:<br>
      <kbd>"online"</kbd> - When online, away or offline.<br>
      <kbd>"away"</kbd> - When away or offline.<br>
      <kbd>"offline"</kbd> - When offline.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channel</td>
      <td valign="middle">string</td>
      <td>Whether @all, @channel and @here trigger mentions. Must be one of the following values:<br>
      <kbd>"true"</kbd> - Mentions are triggered.<br>
      <kbd>"false"</kbd> - Mentions are not triggered.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">comments</td>
      <td valign="middle">string</td>
      <td>Preference for reply mention notifications. Must be one of the following values:<br>
      <kbd>"any"</kbd> - Trigger notifications on messages in reply threads that the user starts or participates in.<br>
      <kbd>"root"</kbd> - Trigger notifications on messages in threads that the user starts.<br>
      <kbd>"never"</kbd> - Do not trigger notifications on messages in reply threads unless the user is mentioned.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mention_keys</td>
      <td valign="middle">string</td>
      <td>Preference for custom non-case sensitive words that trigger mentions. Words must be separated by commas.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

Fields of the UserTeamMembership object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This object is a member of the User object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[1] Not validated, but an error occurs if no such team exists when running in apply mode.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The name of the team this user should be a member of.</td>
      <td align="center" valign="middle">No [1]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roles</td>
      <td valign="middle">string</td>
      <td>The roles the user should have within this team. Must be one of the following values:<br>
          <kbd>"team_user"</kbd><br>
          <kbd>"team_admin team_user"</kbd>
      </td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channels</td>
      <td valign="middle">array</td>
      <td>The channels within this team that the user should be made a member of. Must be an array of <b>ChannelMembership</b> objects.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

Fields of the UserChannelMembership object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This object is a member of the TeamMembership object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot><tr><td colspan="5">[1] Not validated, but an error occurs if the parent channel does not exist when running in apply mode.</td></tr></tfoot>
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">name</td>
      <td valign="middle">string</td>
      <td>The name of the channel in the parent team that this user should be a member of.</td>
      <td align="center" valign="middle">No [1]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">roles</td>
      <td valign="middle">string</td>
      <td>The roles the user should have within this channel. Must be one of the following values:<br>
          <kbd>"channel_user"</kbd><br>
          <kbd>"channel_user channel_admin"</kbd>
      </td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">notify_props</td>
      <td valign="middle">object</td>
      <td>The notify preferences for this user in this channel. Must be a <b>ChannelNotifyProps</b> object</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">favorite</td>
      <td valign="middle">boolean</td>
      <td>Whether to favorite the channel. Must be one of the following values:<br>
          <kbd>"true"</kbd> - Yes.<br>
          <kbd>"false"</kbd> - No.</td>
      </td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

Fields of the ChannelNotifyProps object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This object is a member of the ChannelMembership object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">desktop</td>
      <td valign="middle">string</td>
      <td>Preference for sending desktop notifications. Must be one of the following values:<br>
      <kbd>"default"</kbd> - Global default.<br>
      <kbd>"all"</kbd> - For all activity.<br>
      <kbd>"mention"</kbd> - Only for mentions.<br>
      <kbd>"none"</kbd> - Never.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">mark_unread</td>
      <td valign="middle">string</td>
      <td>Preference for marking channel as unread. Must be one of the following values:<br>
          <kbd>"all"</kbd> - For all unread messages.<br>
          <kbd>"mention"</kbd> - Only for mentions.
      </td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

Post object
-----------

If present, Post objects must occur after the last User object in the file, but before any DirectChannel objects.

Example Post object
~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
    "type": "post",
    "post": {
      "team": "team-name",
      "channel": "channel-name",
      "user": "username",
      "message": "The post message",
      "create_at": 140012340013,
      "flagged_by": [
        "username1",
        "username2",
        "username3"
      ],
      "replies": [{
        "user": "username4",
        "message": "The reply message",
        "create_at": 140012352049,
      }, {
        "user": "username5",
        "message": "Other reply message",
        "create_at": 140012353057,
      }],
      "reactions": [{
        "user": "username6",
        "emoji_name": "+1",
        "create_at": 140012356032,
      }, {
        "user": "username7",
        "emoji_name": "heart",
        "create_at": 140012359034,
      }]
    }
  }


Fields of the Post object
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot>
      <tr>
        <td colspan="5">[1] Not validated, but an error occurs if the team does not exist when running in apply mode.<br>
        [2] Not validated, but an error occurs if the channel does not exist in the corresponding team when running in apply mode.<br>
        [3] Not validated, but an error occurs if the user does not exist when running in apply mode.
        </td>
      </tr>
    </tfoot>
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">team</td>
      <td valign="middle">string</td>
      <td>The name of the team that this post is in.</td>
      <td align="center" valign="middle">No [1]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channel</td>
      <td valign="middle">string</td>
      <td>The name of the channel that this post is in.</td>
      <td align="center" valign="middle">No [2]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this post.</td>
      <td align="center" valign="middle">No [3]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message</td>
      <td valign="middle">string</td>
      <td>The message that the post contains.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the post, in milliseconds since the Unix epoch.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">flagged_by</td>
      <td valign="middle">array</td>
      <td>Must contain a list of members who have flagged the post.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">replies</td>
      <td valign="middle">array</td>
      <td>The posts in reply to this post. Must be an array of <a href="#fields-of-the-reply-object">Reply</a> objects.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">reactions</td>
      <td valign="middle">array</td>
      <td>The emoji reactions to this post. Must be an array of <a href="#fields-of-the-reaction-object">Reaction</a> objects.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

Fields of the Reply object
~~~~~~~~~~~~~~~~~~~~~~~~~~

This object is a member of the Post/DirectPost object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this reply.</td>
      <td align="center" valign="middle">No [3]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message</td>
      <td valign="middle">string</td>
      <td>The message that the reply contains.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the reply, in milliseconds since the Unix epoch.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
  </table>

Fields of the Reaction object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This object is a member of the Post/DirectPost object.

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this reply.</td>
      <td align="center" valign="middle">No [3]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">emoji_name</td>
      <td valign="middle">string</td>
      <td>The emoji of the reaction.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the reply, in milliseconds since the Unix epoch.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
  </table>

DirectChannel object
---------------------

A direct channel can have from two to eight users as members of the channel. If there are only two members, Mattermost treats it as a Direct Message channel. If there are three or more members, Mattermost treats it as a Group Message channel.

Example DirectChannel object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
    "type": "direct_channel",
    "direct_channel": {
      "members": [
        "username1",
        "username2",
        "username3"
      ],
      "header": "The Channel Header",
      "favorited_by": [
        "username1",
        "username2",
        "username3"
      ]
    }
  }

Fields of the DirectChannel object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot>
      <tr>
        <td colspan="5">[1] Not validated, but an error occurs if one or more of the users don't exist when running in apply mode.
        </td>
      </tr>
    </tfoot>
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">members</td>
      <td valign="middle">array</td>
      <td>Must contain a list of members, with a minimum of two usernames and a maximum of eight usernames.</td>
      <td align="center" valign="middle">No [1]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">header</td>
      <td valign="middle">string</td>
      <td>The channel header.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">favorited_by</td>
      <td valign="middle">array</td>
      <td>Must contain a list of members who have favorited the channel.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>

DirectPost object
-----------------

DirectPost objects must occur after all other objects in the file.

Example DirectPost object
~~~~~~~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
    "type": "direct_post",
    "direct_post": {
      "channel_members": [
        "username1",
        "username2",
        "username3",
      ],
      "user": "username2",
      "message": "Hello Group Channel",
      "create_at": 140012340013,
      "flagged_by": [
        "username1",
        "username2",
        "username3"
      ],
      "replies": [{
        "user": "username4",
        "message": "The reply message",
        "create_at": 140012352049,
      }, {
        "user": "username5",
        "message": "Other reply message",
        "create_at": 140012353057,
      }],
      "reactions": [{
        "user": "username6",
        "emoji_name": "+1",
        "create_at": 140012356032,
      }, {
        "user": "username7",
        "emoji_name": "heart",
        "create_at": 140012359034,
      }]
    }
  }

Fields of the DirectPost object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <table width="100%" border="1" cellpadding="5px" style="margin-bottom:20px;">
    <tfoot>
      <tr>
        <td colspan="5">[1] Not validated, but an error occurs if no channels contain an identical list when running in apply mode.<br>[2] Not validated, but an error occurs if the user does not exist when running in apply mode.
        </td>
      </tr>
    </tfoot>
    <tr class="row-odd">
      <th class="head">Field name</th>
      <th class="head">Type</th>
      <th class="head">Description</th>
      <th class="head">Validated</th>
      <th class="head">Mandatory</th>
    </tr>
    <tr class="row-odd">
      <td valign="middle">channel_members</td>
      <td valign="middle">array</td>
      <td>Must contain a list of members, with a minimum of two usernames and a maximum of eight usernames.</td>
      <td align="center" valign="middle">No [1]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">user</td>
      <td valign="middle">string</td>
      <td>The username of the user for this post.</td>
      <td align="center" valign="middle">No [2]</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">message</td>
      <td valign="middle">string</td>
      <td>The message that the post contains.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">create_at</td>
      <td valign="middle">int</td>
      <td>The timestamp for the post, in milliseconds since the Unix epoch.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">Yes</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">flagged_by</td>
      <td valign="middle">array</td>
      <td>Must contain a list of members who have flagged the post.</td>
      <td align="center" valign="middle">No</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">replies</td>
      <td valign="middle">array</td>
      <td>The posts in reply to this direct post. Must be an array of <a href="#fields-of-the-reply-object">Reply</a> objects.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
    <tr class="row-odd">
      <td valign="middle">reactions</td>
      <td valign="middle">array</td>
      <td>The emoji reactions to this direct post. Must be an array of <a href="#fields-of-the-reaction-object">Reaction</a> objects.</td>
      <td align="center" valign="middle">Yes</td>
      <td align="center" valign="middle">No</td>
    </tr>
  </table>
