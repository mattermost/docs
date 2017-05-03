.. _data-format:

Data Format
===========

The input data file must be a valid JSON file with the following objects, each on its own line in the file. The objects must occur in the file in the order listed.

Version
  Mandatory. The Version object must be the first line in the file, and must occur only once.
Team
  Optional. If present, Team objects must occur after the Version object and before any Channel objects.
Channel
  Optional. If present, Channel objects must occur after all Team objects and before any User objects.
User
  Optional. If present, User objects must occur after the Team and Channel objects in the file and before any Post objects. Each User object defines the teams and channels that the user is a member of. If the corresponding teams and channels are not in the data file, then they must exist in the Mattermost database.
Post
  Optional. If present, Post objects must occur after all other objects in the file. Each Post object defines the team, the channel, and the username of the user who posted the message. If the corresponding team, channel, or user are not in the data file, then they must exist in the Mattermost database.

With the exception of the Version object, each object has a field or a combination of fields that is used as the unique identifier of that object. The bulk loader uses the unique identifier to determine if the object being imported is a new object or an update to an existing object.

The identifiers for each object are listed in the following table:

.. csv-table:: Objects and their unique identifiers
  :header: Object, Unique Identifier

  Version, Not Applicable
  Team, *name*
  Channel, "*name*, *team*"
  User, *username*
  UserTeamMembership, "*team*, *username*"
  UserChannelMembership, "*team*, *channel*, *username*"
  Post, "*channel*, *message*, *create_at*"

The following fragment is from a file that imports two teams, each with two channels, many users, and many posts.

.. code-block:: javascript
  :linenos:

  { type: "version", ... }
  { type: "team", team: { name: "TeamA", ...} }
  { type: "team", team: { name: "TeamB", ...} }
  { type: "channel", channel: { team: "TeamA", name: "ChannelA1", ...} }
  { type: "channel", channel: { team: "TeamA", name: "ChannelA2", ...} }
  { type: "channel", channel: { team: "TeamB", name: "ChannelB1", ...} }
  { type: "channel", channel: { team: "TeamB", name: "ChannelB1", ...} }
  { type: "user", user: { username: "user001", ...} }
  { type: "user", user: { username: "user002", ...} }
  { type: "user", user: { username: "user003", ...} }
  { type: "user", ... }
  { type: "user", ... }
  { type: "user", ... }
  .
  .
  .
  { type: "post", { team: "TeamA", name: "ChannelA1", user: "user001", ...} }
  { type: "post", { team: "TeamA", name: "ChannelA1", user: "user001", ...} }
  { type: "post", { team: "TeamA", name: "ChannelA1", user: "user001", ...} }
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
    type: "version",
    version: 1
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
  type: "team",
  team: {
    name: "team-name",
    display_name: "Team Display Name",
    type: "O",
    description: "The Team Description",
    allow_open_invite: true
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
    type: "channel",
    channel: {
      team: "team-name",
      name: "channel-name",
      display_name: "Channel Name",
      type: "O",
      header: "The Channel Header",
      purpose: "The Channel Purpose",
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
    type: "user",
    user: {
      username: "username",
      email: "email@example.com",
      auth_service: "password",
      auth_data: "ldap_id",
      password: "passw0rd",
      nickname: "bobuser",
      first_name: "Bob",
      last_name: "User",
      position: "Senior Developer",
      roles: "system_user",
      locale: "pt_BR",
      teams: [
        {
          name: "team-name",
          roles: "team_member team_admin",
          channels: [
            {
              name: "channel-name",
              roles: "channel_member",
              notify_props: {
                desktop: "default",
                mark_unread: "all"
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
      <td>The authentication service to use for this user account. If not provided, it will default to password&#8209based authentication. Must be one of the following values:<br>
        <kbd>""</kbd> - password authentication.<br>
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
        <kbd>""</kbd> or left out - must be left out.<br>
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
      <td>A password for the user. If not present, the bulk loader generates a password.</td>
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
      <td valign="middle">selected_font</td>
      <td valign="middle">string</td>
      <td>The user’s display font, from the list available in Mattermost.</td>
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
      <td valign="middle">name_format</td>
      <td valign="middle">string</td>
      <td>How names should be displayed to this user. Must be one of the following values:<br>
        <kbd>"username"</kbd> - Show the username.<br>
        <kbd>"nickname_full_name"</kbd> - Show the nickname if one exists, otherwise the first and last name.<br>
        <kbd>"full_name"</kbd> - Show the first and last name.</td>
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
  </table>

Fields of the TeamMembership object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Fields of the ChannelMembership object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Post objects must occur after all other objects in the file.

Example Post object
~~~~~~~~~~~~~~~~~~~

For clarity, the object is shown using regular JSON formatting, but in the data file it cannot be spread across several lines. It must be all on one line.

.. code-block:: javascript

  {
    type: "post",
    post: {
      team: "team-name",
      channel: "channel-name",
      user: "username",
      message: "The post message",
      create_at: 140012340013
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
  </table>
