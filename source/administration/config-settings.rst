Configuration Settings
======================

Mattermost configuration settings are maintained in the configuration file ``config.json``, located in the ``mattermost/config`` directory. You can modify the configuration file using the System Console, or by using a text editor to modify it directly.

The default location of ``config.json`` is in the ``mattermost/config`` directory. Mattermost must have write permissions to ``config.json``, otherwise changes made in the System Console will have no effect.

**Environment Variables**
Starting in Mattermost version 3.8, you can use environment variables to manage the configuration. Environment variables override settings in ``config.json``. If a change to a setting in ``config.json`` requires a restart for it to take effect, then changes to the corresponding environment variable also require a server restart.

The name of the environment variable for any setting can be derived from the name of that setting in ``config.json``.

For example, to derive the name of the Site URL setting:

1. Find the setting in ``config.json``. In this case, *ServiceSettings.SiteURL*.
2. Add ``MM_`` to the beginning and convert all characters to uppercase and replace the ``.`` with ``_``. For example, *MM_SERVICESETTINGS_SITEURL*.
3. The setting becomes ``export MM_SERVICESETTINGS_SITEURL="http://example.com"``

For any setting that is not set in ``config.json`` or in environment variables, the Mattermost server uses the default value as documented here.

.. contents::
  :depth: 2
  :local:
  :backlinks: entry

General
-------
General settings for server configuration, language defaults, user and team management, privacy, compliance reporting and logs.

Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Site URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The URL that users will use to access Mattermost. The port number is required if it's not a standard port such as 80 or 443.

This field is required in Mattermost v3.8 and later.

.. note:: Do not append a team name to the end of the site URL.

Correct example: ``https://mattermost.example.com:8065``

Incorrect example: ``https://mattermost.example.com/team_name``

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SiteURL": ""`` with string input.                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

Listen Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The address and port to which to bind and listen. Specifying ":8065" will bind to all network interfaces. Specifying ``127.0.0.1:8065`` will only bind to the network interface having that IP address.

If you choose a port of a lower level (called "system ports" or "well-known ports", in the range of 0-1023), you must have permissions to bind to that port.

On Linux you can use: ``sudo setcap cap_net_bind_service=+ep ./bin/platform`` to allow Mattermost to bind to well-known ports.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ListenAddress": ":8065"`` with string input  |
+-------------------------------------------------------------------------------------------+

Connection Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**None**: Mattermost will connect over an unsecure connection.

**TLS**: Encrypts the communication between Mattermost and your server. See `documentation <https://docs.mattermost.com/install/config-tls-mattermost.html>`_ for more details.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionSecurity": ""`` with options ``""`` and ``TLS`` for the above settings respectively  |
+---------------------------------------------------------------------------------------------------------------------------------------------+

TLS Certificate File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The path to the certificate file to use for TLS connection security.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSCertFile": ""`` with string input  |
+------------------------------------------------------------------------------------+


TLS Key File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The path to the TLS key file to use for TLS connection security.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSKeyFile": ""`` with string input  |
+-----------------------------------------------------------------------------------+

Use Let's Encrypt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Enable the automatic retrieval of certificates from Let's Encrypt. The certificate will be retrieved when a client attempts to connect from a new domain. This will work with multiple domains. See :doc:`../install/config-tls-mattermost` for more details on setting up Let's Encrypt.

**False**: Manual certificate specification based on the **TLS Certificate File** and **TLS Key File** specified above.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseLetsEncrypt": false`` with options ``true`` and ``false`` for above settings respectively.                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Let's Encrypt Certificate Cache File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The path to the file where certificates and other data about the Let's Encrypt service will be stored.

+-----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LetsEncryptCertificateCacheFile": "./config/letsencrypt.cache"`` with string input.  |
+-----------------------------------------------------------------------------------------------------------------------------------+

Forward port 80 to 443
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Forwards all insecure traffic from port 80 to secure port 443.

**False**: When using a proxy such as NGINX in front of Mattermost this setting is unnecessary and should be set to `false`.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Forward80To443": false`` with options ``true`` and ``false`` for above settings respectively.                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Read Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Maximum time allowed from when the connection is accepted to when the request body is fully read.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReadTimeout": 300`` with string input  |
+-------------------------------------------------------------------------------------+

Write Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If using HTTP (insecure), this is the maximum time allowed from the end of reading the request headers until the response is written. If using HTTPS, it is the total time from when the connection is accepted until the response is written.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WriteTimeout": 300`` with string input  |
+--------------------------------------------------------------------------------------+

Allow use of API v3 endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set to false to disable all version 3 endpoints of the REST API. Integrations that rely on API v3 will fail and can then be identified for migration to API v4. API v3 is deprecated and will be removed in the near future. See https://api.mattermost.com for details.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIv3": true`` with options ``true`` and ``false``.  |
+---------------------------------------------------------------------------------------------------------+

Webserver Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
gzip compression applies to the HTML, CSS, Javascript, and other static content files that make up the Mattermost web client. It is recommended to enable gzip to improve performance unless your environment has specific restrictions, such as a web proxy that distributes gzip files poorly. This setting requires a server restart to take effect.

**gzip**: The Mattermost server will serve static files compressed with gzip to improve performance.

**Uncompressed**: The Mattermost server will serve static files uncompressed.

**Disabled**: The Mattermost server will not serve static files.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WebserverMode": "gzip"`` with options ``gzip``, ``uncompressed`` and ``disabled`` for above settings respectively.      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Reload Configuration from Disk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E20*

This button resets the configuration settings by reloading the settings from the disk. The server will still need to be restarted if a setting requiring server restart was changed.

The workflow for failover without downing the server is to change the database line in the config.json file, click **Reload Configuration from Disk** then click **Recycle Database Connections** in the Advanced > Database section.

Purge All Caches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This button purges all the in-memory caches for sessions, accounts and channels. Deployments using High Availability will attempt to purge all the servers in the cluster. Purging the caches may adversely impact performance.

________

Localization
~~~~~~~~~~~~~~~~~~~~~~~~~
Default Server Language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Default language for system messages and logs. Changing this will require a server restart before taking effect.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultServerLocale": "en"`` with options ``de``, ``en``, ``es``, ``fr``, ``it``, ``ja``, ``ko``, ``nl``, ``pl``, ``pt-br``, ``ru``, ``tr``, ``zh_CN`` and ``zh_TW``   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Default Client Language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Default language for newly created users and pages where the user hasn't logged in.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultClientLocale": "en"`` with options ``de``, ``en``, ``es``, ``fr``, ``it``, ``ja``, ``ko``, ``nl``, ``pl``, ``pt-br``, ``ru``, ``tr``, ``zh_CN`` and ``zh_TW``   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Available Languages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sets which languages are available for users in **Account Settings** > **Display** > **Languages**. Leave the field blank to add new languages automatically by default, or add new languages using the dropdown menu manually as they become available. If you're manually adding new languages, the **Default Client Language** must be added before saving the setting.

Note: Servers which upgraded to v3.1 need to manually set this field blank to have new languages added by default.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AvailableLocales": ""`` with options ``""``, ``de``, ``en``, ``es``, ``fr``, ``it``, ``ja``, ``ko``, ``nl``, ``pl``, ``pt-br``, ``ru``, ``tr``, ``zh_CN`` and ``zh_TW``   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Users and Teams
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Account Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Ability to create new accounts is enabled via inviting new members or sharing the team invite link.

**False**: Ability to create accounts is disabled. The **Create Account** button displays an error when trying to signup via an email invite or team invite link.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserCreation": true`` with options ``true`` and ``false`` for above settings respectively.                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Enable Team Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Ability to create a new team is enabled for all users.

**False**: Only System Administrators can create teams from the team selection page. The **Create A New Team** button is hidden in the main menu UI.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTeamCreation": true`` with options ``true`` and ``false`` for above settings respectively.                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Max Users Per Team
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Maximum number of users per team, excluding inactive users.


The **Max Users Per Team** refers to the size of the "team site" which is workspace a "team of people" inhabits. A team of people is considered a small organization where people work closely together towards a specific shared goal and share the same etiquette. In the physical world, a team of people could typically be seated around a single table to have a meal and discuss their project.

The default maximum of 50 people, is at the extreme high end of a single team of people. At this point organizations are more often "multiple teams of people" and investments in explicitly defining etiquette, such as `channel organization <https://docs.mattermost.com/help/getting-started/organizing.html>`_ or turning on `policy features <https://docs.mattermost.com/administration/config-settings.html#policy>`_ in Enterprise Edition, are often used to scale the high levels of productivity found in a team of people using Mattermost to multiple teams of people.

In terms of technical performance, `with appropriate hardware, Mattermost can easily scale to hundreds and even thousands of users <https://docs.mattermost.com/install/requirements.html>`_, and provided the administrator believes the appropriate etiquette is in place, they should feel free to increase the default value.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersPerTeam": 50`` with whole number input.                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Max Channels Per Team
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Maximum number of channels per team, including both active and deleted channels.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxChannelsPerTeam": 2000`` with whole number input.                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Max Notifications Per Channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Maximum total number of users in a channel before @all, @here, and @channel no longer send notifications to maximize performance.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxNotificationsPerChannel": 1000`` with whole number input.                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Restrict account creation to specified email domains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Teams and user accounts can only be created by a verified email from this list of comma-separated domains (e.g. "corp.mattermost.com, mattermost.org").

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictCreationToDomains": ""`` with string input.                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Restrict Team Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Removed in November 16th, 2016 release*

**True**: Newly created team names cannot contain the following restricted words: www, web, admin, support, notify, test, demo, mail, team, channel, internal, localhost, dockerhost, stag, post, cluster, api, oauth.

**False**: Newly created team names are not restricted.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictTeamNames": true`` with options ``true`` and ``false`` for above settings respectively.                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable users to open Direct Message channels with
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Any user on the Mattermost server**: The Direct Messages "More" menu has the option to open a Direct Message channel with any user on the server.

**Any member of the team**: The Direct Messages "More" menu only has the option to open a Direct Message channel with users on the current team.  If a user belongs to multiple teams, direct messages will still be received regardless of what team they are currently on.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictDirectMessage": "any"`` with options ``any`` and ``team`` for above settings respectively.                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Team Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Removed in May 16th, 2016 release*

**True**: Teams that are configured to appear in the team directory will appear on the system main page. Teams can configure this setting from **Team Settings > Include this team in the Team Directory**.

**False**: Team directory on the system main page is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTeamListing": false`` with options ``true`` and ``false`` for above settings respectively.                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Teammate Name Display
^^^^^^^^^^^^^^^^^^^^^
Specifies how names are displayed in the user interface.

**Show username**: Displays the user's username.

**Show nickname if one exists**: Displays the user's nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed.

**Show first and last name**: Displays the user's full name. If the user does not have a full name, their username is displayed. Recommended when using SAML or LDAP if first name and last name attributes are configured.

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TeammateNameDisplay": "username"`` with options ``username``, ``nickname_full_name``, and ``full_name``. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Policy
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E10 and higher*

Settings to configure the permission restrictions for sending team invite links and managing channels.

Enable sending team invites from
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set policy on who can invite others to a team using the **Send Email Invite**, **Get Team Invite Link**, and **Add Members to Team** options on the main menu. If **Get Team Invite Link** is used to share a link, you can expire the invite code from **Team Settings > Invite Code** after the desired users have joined the team. Options include:

**All team members**: Allows any team member to invite others using an email invitation or team invite link.

**Team and System Admins**: Hides the email invitation and team invite link in the Main Menu from users who are not Team Admins or System Admins.

**System Admins**: Hides the email invitation and team invite link in the Main Menu from users who are not System Admins.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictTeamInvite": "all"`` with options ``all``, ``team_admin`` and ``system_admin`` for above settings respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel creation for
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Restrict the permission level required to create public channels.

**All team members**: Allow all team members to create public channels.

**Team Admins and System Admins**: Restrict creating public channels to Team Admins and System Admins.

**System Admins**: Restrict creating public channels to System Admins.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelCreation": "all"`` with options ``all``, ``team_admin`` and ``system_admin`` for above settings respectively.   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel renaming for
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Restrict the permission level required to rename and set the header or purpose for public channels.

**All channel members**: Allow all channel members to rename public channels.

**Channel Admins, Team Admins, and System Admins**: Restrict renaming public channels to Channel Admins, Team Admins, and System Admins that are members of the channel.

**Team Admins and System Admins**: Restrict renaming public channels to Team Admins and System Admins that are members of the channel.

**System Admins**: Restrict renaming public channels to System Admins that are members of the channel.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelManagement": "all"`` with options ``all``, ``channel_admin``, ``team_admin``, and ``system_admin`` for above settings respectively.   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel deletion for
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Restrict the permission level required to delete public channels. Deleted channels can be recovered from the database using a `command line tool <https://docs.mattermost.com/administration/command-line-tools.html>`_.

**All channel members**: Allow all channel members to delete public channels.

**Channel Admins, Team Admins, and System Admins**: Restrict deleting public channels to Channel Admins, Team Admins, and System Admins that are members of the channel.

**Team Admins and System Admins**: Restrict deleting public channels to Team Admins and System Admins that are members of the channel.

**System Admins**: Restrict deleting public channels to System Admins that are members of the channel.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelDeletion": "all"`` with options ``all``, ``channel_admin``, ``team_admin``, and ``system_admin`` for above settings respectively.   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel creation for
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Restrict the permission level required to create private channels.

**All team members**: Allow all team members to create private channels.

**Team Admins and System Admins**: Restrict creating private channels to Team Admins and System Admins.

**System Admins**: Restrict creating private channels to System Admins.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelCreation": "all"`` with options ``all``, ``team_admin`` and ``system_admin`` for above settings respectively.   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel renaming for
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Restrict the permission level required to rename and set the header or purpose for private channels.

**All channel members**: Allow all channel members to rename private channels.

**Channel Admins, Team Admins, and System Admins**: Restrict renaming private channels to Channel Admins, Team Admins, and System Admins that are members of the private channel.

**Team Admins and System Admins**: Restrict renaming private channels to Team Admins and System Admins that are members of the private channel.

**System Admins**: Restrict renaming private channels to System Admins that are members of the private channel.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelManagement": "all"`` with options ``all``, ``channel_admin``, ``team_admin``, and ``system_admin`` for above settings respectively.   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel deletion for
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Restrict the permission level required to delete private channels. Deleted channels can be recovered from the database using a `command line tool <https://docs.mattermost.com/administration/command-line-tools.html>`_.

**All channel members**: Allow all channel members to delete private channels.

**Channel Admins, Team Admins, and System Admins**: Restrict deleting private channels to Channel Admins, Team Admins, and System Admins that are members of the private channel.

**Team Admins and System Admins**: Restrict deleting private channels to Team Admins and System Admins that are members of the private channel.

**System Admins**: Restrict deleting private channels to System Admins that are members of the private channel.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelDeletion": "all"`` with options ``all``, ``channel_admin``, ``team_admin``, and ``system_admin`` for above settings respectively.   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable managing of private channel members for
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set policy on who can add and remove members from private channels.

**All team members**: Allow all team members to add and remove members.

**Team Admins, Channel Admins, and System Admins**: Allow only Team Admins, Channel Admins, and System Admins to add and remove members.

**Team Admins, and System Admins**: Allow only Team Admins and System Admins to add and remove members.

**System Admins**: Allow only System Admins to add and remove members.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelManageMembers": "all"`` with options ``all``, ``channel_admin``, ``team_admin``, and ``system_admin`` for above settings respectively. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow which users to delete messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Restrict the permission level required to delete messages. Team Admins, Channel Admins, and System Admins can delete messages only in channels where they are members. Messages can be deleted anytime.

**Message authors can delete their own messages, and Administrators can delete any message**: Allow authors to delete their own messages, and allow Team Admins, Channel Admins, and System Admins to delete any message.

**Team Admins and System Admins**: Allow only Team Admins and System Admins to delete messages.

**System Admins**: Allow only System Admins to delete messages.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPostDelete": "all"`` with options ``all``, ``team_admin`` and ``system_admin`` for above settings respectively.               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow users to edit their messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set the time limit that users have to edit their messages after posting.

**Any time**: Allow users to edit their messages at any time after posting.

**Never**: Do not allow users to edit their messages.

**{n} seconds after posting**: Users can edit their messages within the specified time limit after posting.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature has two settings in ``config.json``. The first setting is ``"AllowEditPost": "always"`` with options ``always``, ``never``, and ``time_limit``.  |
|                                                                                                                                                               |
| The second setting is ``"PostEditTimeLimit": 300`` with whole number input. To enable ``PostEditTimeLimit``, set ``AllowEditPost`` to ``time_limit``.         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Announcement Banner
^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable an announcement banner across all teams. The banner is displayed at the top of the screen and is the entire width of the screen. By default, users can dismiss the banner until you either change the text of the banner or until you re-enable the banner after it has been disabled. You can prevent users from dismissing the banner, and you can control the text color and the background color.

**True**: Enable the announcement banner. The banner is displayed only if ``BannerText`` has a value.

**False**: Disable the announcement banner.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBanner": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------+

Banner Text
^^^^^^^^^^^

The text of the announcement banner.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerText": ""`` with string input.  |
+------------------------------------------------------------------------------------+

Banner Color
^^^^^^^^^^^^

The background color of the announcement banner.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``""BannerColor": "#f2a93b"`` with string input.  |
+---------------------------------------------------------------------------------------------+

Banner Text Color
^^^^^^^^^^^^^^^^^

The color of the text in the announcement banner.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``""BannerTextColor": "#333333"`` with string input.  |
+-------------------------------------------------------------------------------------------------+

Allow Banner Dismissal
^^^^^^^^^^^^^^^^^^^^^^

**True**: Users can dismiss the banner until the next time they log in or the banner is updated.

**False**: The banner is permanently visible until it is turned off by the System Admin.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``""AllowBannerDismissal": true`` with options ``true`` and ``false``.  |
+-------------------------------------------------------------------------------------------------------------------+


Privacy
~~~~~~~~~~~~~~~~~~~~~~~~~
Settings to configure the name and email privacy of users on your system.

Show Email Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Show email address of all users.

**False**: Hide email address of users from other users in the user interface, including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Administrators will still be able to see email addresses in the UI.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowEmailAddress": true`` with options ``true`` and ``false`` for above settings respectively.                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show Full Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Show full name of all users.

**False**: hide full name of users from other users including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Administrators will still be able to see full names in the UI.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowFullName": true`` with options ``true`` and ``false`` for above settings respectively.                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Compliance
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

Settings used to enable and configure Mattermost compliance reports.

Enable Compliance Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Compliance reporting is enabled in Mattermost.

**False**: Compliance reporting is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Compliance Report Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sets the directory where compliance reports are written.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./data/"`` with string input.                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Daily Report
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Mattermost generates a daily compliance report.

**False**: Daily reports are not generated.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDaily": false`` with options ``true`` and ``false`` for above settings respectively.                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Logging
~~~~~~~~~~~~~~~~~~~~~~~~~
Output logs to console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Output log messages to the console based on **ConsoleLevel** option. The server writes messages to the standard output stream (stdout).

**False**: Output log messages are not written to the console.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableConsole": true`` with options ``true`` and ``false`` for above settings respectively.                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Console Log Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Level of detail at which log events are written to the console when **EnableConsole** = ``true``.

**DEBUG**: Prints high detail for developers debugging issues.

**ERROR**: Outputs only error messages.

**INFO**: Outputs error messages and information around startup and initialization.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConsoleLevel": "DEBUG"`` with options ``DEBUG``, ``ERROR`` and ``INFO`` for above settings respectively.                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Output logs to file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Typically set to true in production. When true, logged events are written to the ``mattermost.log`` file in the directory specified by the **FileLocation** setting. The logs are rotated at 10,000 lines and archived to a file in the same directory, and given a name with a datestamp and serial number. For example, ``mattermost.2017-03-31.001``.

**True**:  Log files are written to files specified in **FileLocation**.

**False**: Log files are not written.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFile": true`` with options ``true`` and ``false`` for above settings respectively.  |
+----------------------------------------------------------------------------------------------------------------------------------------+

File Log Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Level of detail at which log events are written to log files when **EnableFile** = ``true``.

**ERROR**: Outputs only error messages.

**INFO**: Outputs error messages and information around startup and initialization.

**DEBUG**: Prints high detail for developers debugging issues.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLevel": "INFO"`` with options ``DEBUG``, ``ERROR`` and ``INFO`` for above settings respectively.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

File Log Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The location of the log files. If blank, they are stored in the ``./logs`` directory. The path that you set must exist and Mattermost must have write permissions in it.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLocation": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

File Log Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Format of log message output. If blank, FileFormat = "[%D %T] [%L] (%S) %M", where:

.. list-table::
   :widths: 20 80

   * - %T
     - Time (15:04:05 MST)
   * - %t
     - Time (15:04)
   * - %D
     - Date (2006/01/02)
   * - %d
     - Date (01/02/06)
   * - %L
     - Level (FNST, FINE, DEBG, TRAC, WARN, EROR, CRIT)
   * - %S
     - Source
   * - %M
     - Message

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileFormat": ""`` with string input.                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Enable Webhook Debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Contents of incoming webhooks are printed to log files for debugging.

**False**: Contents of incoming webhooks are not printed to log files.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableWebhookDebugging": true`` with options ``true`` and ``false`` for above settings respectively.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Enable Diagnostics and Error Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: To improve the quality and performance of future Mattermost updates, this option sends error reporting and diagnostic information to Mattermost, Inc. To learn more about this feature, see :doc:`telemetry`.

**False**: Diagnostics and error reporting are disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDiagnostics": true`` with options ``true`` and ``false`` for above settings respectively.                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+



________

Authentication
-------------------------------
Authentication settings to enable account creation and sign in with email, GitLab, Google or Office 365 OAuth, AD/LDAP, or SAML.

Email Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable account creation with email
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Allow team creation and account signup using email and password.

**False**: Email signup is disabled. This limits signup to single sign-on services like OAuth or AD/LDAP.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSignUpWithEmail": true`` with options ``true`` and ``false`` for above settings respectively.                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable sign-in with email
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Mattermost allows account creation using email and password.

**False**: Sign in with email is disabled and does not appear on the login screen. Use this value when you want to limit sign up to a single sign-on service like AD/LDAP, SAML or GitLab.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSignInWithEmail": true`` with options ``true`` and ``false`` for above settings respectively.                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable sign-in with username
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Mattermost allows users with email login to sign in using their username and password. This setting does not affect AD/LDAP login.

**False**: Sign in with username is disabled and does not appear on the login screen.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EnableSignInWithUsername": true`` with options ``true`` and ``false`` for above settings respectively.                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

OAuth 2.0
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E10 and higher*

Settings to configure OAuth login for account creation and login.

Select OAuth 2.0 service provider:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Choose whether OAuth can be used for account creation and login. Options include:

    - **Do not allow sign-in via an OAuth 2.0 provider**
    - **GitLab** (see `GitLab Settings <http://docs.mattermost.com/administration/config-settings.html#id14>`_ for more detail)
    - **Google Apps** (see `Google Settings <http://docs.mattermost.com/administration/config-settings.html#google-enterprise>`_ for more detail)
    - **Office 365 (Beta)** (see `Office 365 Settings <http://docs.mattermost.com/administration/config-settings.html#office-365-enterprise>`_ for more detail)

This feature's setting does not appear in ``config.json``.

________

GitLab
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable authentication with GitLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Allow team creation and account signup using GitLab OAuth. To configure, input the **Secret** and **Id** credentials.

**False**: GitLab OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note**: For Enterprise, GitLab settigs can be found under **OAuth 2.0**

Application ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this value by logging into your GitLab account. Go to Profile Settings > Applications > New Application, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input.                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Application Secret Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this value by logging into your GitLab account. Go to Profile Settings > Applications > New Application, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input.                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

User API Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter ``https://<your-gitlab-url>/api/v3/user`` (example: ``https://example.com:3000/api/v3/user``). Use HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": ""`` with string input.                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Auth Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter ``https://<your-gitlab-url>/oauth/authorize`` (example: ``https://example.com:3000/oauth/authorize``). Use HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Token Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter ``https://<your-gitlab-url>/oauth/token`` (example: ``https://example.com:3000/oauth/token``). Use HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": ""`` with string input.                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Google
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

Enable authentication with Google by selecting ``Google Apps`` from **OAuth 2.0 > Select OAuth 2.0 service provider**

**True**: Allow team creation and account signup using Google OAuth. To configure, input the **Client ID** and **Client Secret** credentials. See `Documentation <https://docs.mattermost.com/deployment/sso-google.html>`_ for more detail.

**False**: Google OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Client ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this value by registering Mattermost as an application in your Google account.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input.                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Client Secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this value by registering Mattermost as an application in your Google account.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input.                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

User API Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to use `https://www.googleapis.com/plus/v1/people/me` as the User API Endpoint. Otherwise, enter a custom endpoint in `config.json` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://www.googleapis.com/plus/v1/people/me"`` with string input.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Auth Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to use `https://accounts.google.com/o/oauth2/v2/auth` as the Auth Endpoint. Otherwise, enter a custom endpoint in `config.json` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://accounts.google.com/o/oauth2/v2/auth"`` with string input.                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Token Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to use `https://www.googleapis.com/oauth2/v4/token` as the Token Endpoint. Otherwise, enter a custom endpoint in `config.json` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://www.googleapis.com/oauth2/v4/token"`` with string input.                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Office 365
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

Enable authentication with Office 365 by selecting ``Office 365 (Beta)`` from **OAuth 2.0 > Select OAuth 2.0 service provider**

**True**: Allow team creation and account signup using Office 365 OAuth. To configure, input the **Application ID** and **Application Secret Password** credentials. See `Documentation <https://docs.mattermost.com/deployment/sso-office.html>`_ for more detail.

**False**: Office 365 OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Application ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input.                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Application Secret Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input.                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

User API Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to use `https://graph.microsoft.com/v1.0/me` as the User API Endpoint. Otherwise, enter a custom endpoint in `config.json` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://graph.microsoft.com/v1.0/me"`` with string input.                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Auth Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to use `https://accounts.google.com/o/oauth2/v2/auth` as the Auth Endpoint. Otherwise, enter a custom endpoint in `config.json` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"`` with string input.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Token Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to use `https://login.microsoftonline.com/common/oauth2/v2.0/token` as the Token Endpoint. Otherwise, enter a custom endpoint in `config.json` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/token"`` with string input.                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

AD/LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E10 and higher*

Enable sign-in with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Mattermost allows login using AD/LDAP or Active Directory.

**False**: Login with AD/LDAP is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The domain or IP address of the AD/LDAP server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LdapServer": ""`` with string input.                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The port Mattermost will use to connect to the AD/LDAP server. Default is 389.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LdapPort": 389`` with numerical input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Connection Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The type of connection security Mattermost uses to connect to AD/LDAP.

**None**: No encryption, Mattermost will not attempt to establish an encrypted connection to the AD/LDAP server.

**TLS**: Encrypts the communication between Mattermost and your server using TLS.

**STARTTLS**: Takes an existing insecure connection and attempts to upgrade it to a secure connection using TLS.

If the "No encryption" option is selected it is highly recommended that the AD/LDAP connection is secured outside of Mattermost, for example, by adding a stunnel proxy.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionSecurity": ""`` with options ``""``, ``TLS`` and ``STARTTLS`` for above settings respectively.                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Skip Certificate Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the AD/LDAP server that will be used to populate the nickname of users in Mattermost.

**True**: Skips the certificate verification step for TLS or STARTTLS connections. Not recommended for production environments where TLS is required. For testing only.

**False**: Mattermost does not skip certificate verification.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SkipCertificateVerification": false`` with options ``true`` and ``false`` for above settings respectively.              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Base DN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The **Base Distinguished Name** of the location where Mattermost should start its search for users in the AD/LDAP tree.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BaseDN": ""`` with string input.                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Bind Username
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The username used to perform the AD/LDAP search. This should be an account created specifically for use with Mattermost  Its permissions should be limited to read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field. When using Active Directory, **Bind Username** should specify domain in ``DOMAIN/username`` format. This field is required, and anonymous bind is not currently supported.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BindUsername": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Bind Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Password of the user given in **Bind Username**. This field is required, and anonymous bind is not currently supported.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BindPassword": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

User Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) Enter an AD/LDAP Filter to use when searching for user objects (accepts `general syntax <http://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`_). Only the users selected by the query will be able to access Mattermost. For Active Directory, the query to filter out disabled users is ``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``

This filter uses the permissions of the **Bind Username** account to execute the search. Administrators should make sure to use a specially created account for Bind Username with read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserFilter": ""`` with string input.                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

First Name Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the AD/LDAP server that will be used to populate the first name of users in Mattermost. When set, users will not be able to edit their First Name, since it is synchronized with the LDAP server. When left blank, users can set their own First Name in Account Settings.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FirstNameAttribute": ""``  with string input.                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Last Name Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the AD/LDAP server that will be used to populate the last name of users in Mattermost. When set, users will not be able to edit their Last Name, since it is synchronized with the LDAP server. When blank, users can set their own Last Name in Account Settings.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LastNameAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Nickname Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the AD/LDAP server that will be used to populate the nickname of users in Mattermost. When set, users will not be able to edit their Nickname, since it is synchronized with the LDAP server. When blank, users can set their own Nickname in Account Settings.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NicknameAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Position Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the AD/LDAP server that will be used to populate the position field in Mattermost (typically used to describe a person's job title or role at the company). When set, users will not be able to edit their position, since it is synchronized with the LDAP server. When blank, users can set their own Position in Account Settings.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PositionAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Email Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The attribute in the AD/LDAP server that will be used to populate the email addresses of users in Mattermost.

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings choosen by the System Admin.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAttribute": ""`` with string input.                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Username Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The attribute in the AD/LDAP server that will be used to populate the username field in Mattermost user interface. This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned.

The **Username Attribute** may be set to the same value used to sign-in to the system, called an **ID Attribute**, or it can be mapped to a different value.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UsernameAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ID Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The attribute in the AD/LDAP server that will be used as a unique identifier in Mattermost. It serves two purposes:

This value is used to sign in to Mattermost in the **AD/LDAP Username** field on the sign in page. This attribute can be the same as the **Username Attribute** field above, which is what is used to identify users in the Mattermost interface, or it can be a different value, for example a User ID number. If your team typically uses ``DOMAIN\username`` to sign in to other services with AD/LDAP, you may enter a field name that maps to ``DOMAIN\username`` to maintain consistency between sites.

**This is the attribute that will be used to create unique Mattermost accounts.** This attribute should be an AD/LDAP attribute with a value that does not change, such as ``username`` or ``uid``. If a user’s **ID Attribute** changes and the user attempts to login the Mattermost server will attempt to create a new Mattermost user account based on the new **ID Attribute** and fail since new Mattermost users accounts can't be created with duplicate email addresses or Mattermost usernames (as defined in the **Username Attribute**).

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdAttribute": ""`` with string input.                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Login Field Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The placeholder text that appears in the login field on the login page. Typically this would be whatever name is used to refer to AD/LDAP credentials in your company, so it is recognizable to your users. Defaults to **AD/LDAP Username**.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginFieldName": ""`` with string input.                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Synchronization Interval (minutes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set how often Mattermost accounts synchronize attributes with AD/LDAP, in minutes. When synchronizing, Mattermost queries AD/LDAP for relevant account information and updates Mattermost accounts based on changes to attributes (first name, last name, and nickname). When accounts are disabled in AD/LDAP users are made inactive in Mattermost, and their active sessions are revoked once Mattermost synchronizes attributes. To synchronize immediately after disabling an account, use the "AD/LDAP Synchronize Now" button.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SyncIntervalMinutes": 60`` with whole number input.                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Maximum Page Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The maximum number of users the Mattermost server will request from the AD/LDAP server at one time. Use this setting if your AD/LDAP server limits the number of users that can be requested at once. 0 is unlimited.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxPageSize": 0`` with whole number input.                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Query Timeout (seconds)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The timeout value for queries to the AD/LDAP server. Increase this value if you are getting timeout errors caused by a slow AD/LDAP server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"QueryTimeout": 60`` with whole number input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP Synchronize Now
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This button causes AD/LDAP synchronization to occur as soon as it is pressed. Use it whenever you have made a change in the AD/LDAP server you want to take effect immediately. After using the button, the next AD/LDAP synchronization will occur after the time specified by the Synchronization Interval.

AD/LDAP Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This button can be used to test the connection to the AD/LDAP server. If the test us successful, it shows a confirmation message and if there is a problem with the configuration settings it will show an error message.

________

.. _saml-enterprise:

SAML
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

Enable Login With SAML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Mattermost allows login using SAML. Please see `documentation <http://docs.mattermost.com/deployment/sso-saml.html>`_ to learn more about configuring SAML for Mattermost.

**False**: Login with SAML is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SAML SSO URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The URL where Mattermost sends a SAML request to start login sequence.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpURL": ""``  with string input.                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Identity Provider Issuer URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The issuer URL for the Identity Provider you use for SAML requests.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpDescriptorUrl": ""``  with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Identity Provider Public Certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The public authentication certificate issued by your Identity Provider.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpCertificateFile": ""`` with string input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Verify Signature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Mattermost verifies that the signature sent from the SAML Response matches the Service Provider Login URL.

**False**: Not recommended for production environments. For testing only.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Verify": true`` with options ``true`` and ``false``.                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Service Provider Login URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter ``https://<your-mattermost-url>/login/sso/saml`` (example: ``https://example.com/login/sso/saml``). Make sure you use HTTP or HTTPS in your URL depending on your server configuration. This field is also known as the Assertion Consumer Service URL.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AssertionConsumerServiceURL": ""`` with string input.                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Mattermost will decrypt SAML Assertions encrypted with your Service Provider Public Certificate.

**False**: Not recommended for production environments. For testing only.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Encrypt": true`` with options ``true`` and ``false``.                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Service Provider Private Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The private key used to decrypt SAML Assertions from the Identity Provider.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivateKeyFile": ""`` with string input.                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Service Provider Public Certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The certificate file used to generate the signature on a SAML request to the Identity Provider for a service provider initiated SAML login, when Mattermost is the Service Provider.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicCertificateFile": ""`` with string input.                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Email Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The attribute in the SAML Assertion that will be used to populate the email addresses of users in Mattermost.

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings choosen by the System Admin.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAttribute": ""`` with string input.                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Username Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The attribute in the SAML Assertion that will be used to populate the username field in Mattermost user interface. This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UsernameAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

First Name Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the SAML Assertion that will be used to populate the first name of users in Mattermost.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FirstNameAttribute": ""`` with string input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Last Name Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the SAML Assertion that will be used to populate the last name of users in Mattermost.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LastNameAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Nickname Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the SAML Assertion that will be used to populate the nickname of users in Mattermost.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NicknameAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Position Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the SAML Assertion that will be used to populate the position field for users in Mattermost (typically used to describe a person's job title or role at the company).

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PositionAttribute": ""`` with string input.                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Preferred Language Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The attribute in the SAML Assertion that will be used to populate the language of users in Mattermost.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocaleAttribute": ""`` with string input.                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Login Button Text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The text that appears in the login button on the login page. Defaults to ``With SAML``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonText": ""`` with string input.                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________


MFA
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E10 and higher*

Configure security settings for multi-factor authentication.

The default recommendation for secure deployment is to host Mattermost within your own private network, with VPN clients on mobile, so everything works under your existing security policies and authentication protocols, which may already include multi-factor authentication.

If you choose to run Mattermost outside your private network, bypassing your existing security protocols, it is recommended you upgrade to Mattermost Enterprise Edition to set up a multi-factor authentication service specifically for accessing Mattermost.

Enable Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: When true, users with LDAP and email authentication will be given the option to require a phone-based passcode, in addition to their password-based authentication, to sign-in to the Mattermost server. Specifically, they will be asked to download the `Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator>`_ app to their iOS or Android mobile device, connect the app with their account, and then enter a passcode generated by the app on their phone whenever they log in to the Mattermost server.

**False**: Multi-factor authentication is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMultifactorAuthentication": false`` with options ``true`` and ``false`` for above settings respectively.           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enforce Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: When true, `multi-factor authentication (MFA) <https://docs.mattermost.com/deployment/auth.html>`_ is required for login. New users will be required to configure MFA on sign-up. Logged in users without MFA configured are redirected to the MFA setup page until configuration is complete. If your system has users with login options other than AD/LDAP and email, MFA must be enforced with the authentication provider outside of Mattermost.

**False**: Multi-factor authentication is optional.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnforceMultifactorAuthentication": false`` with options ``true`` and ``false`` for above settings respectively.           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________


Security
--------------------------------
Configure security settings for account creation, login, public links and connection requests.

Sign Up
~~~~~~~~~~~~~~~~~~~~~~~~~
Require Email Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Require email verification after account creation prior to allowing login.

**False**: Users do not need to verify their email address prior to login. Developers may set this field to false so skip sending verification emails for faster development.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RequireEmailVerification": false`` with options ``true`` and ``false`` for above settings respectively.                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Email Invite Salt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
32-character (to be randomly generated via System Console) salt added to signing of email invites. Click **Regenerate** to create new salt.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InviteSalt": ""`` with string input.                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Open Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Users can sign up to the server from the root page without an invite.

**False**: Users can only sign up to the server if they receive an invite.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOpenServer": false`` with options ``true`` and ``false`` for above settings respectively.                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Password
~~~~~~~~~~~~~~~~~~~~~~~~~
Minimum Password Length
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

Minimum number of characters required for a valid password. Must be a whole number greater than or equal to 5 and less than or equal to 64.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MinimumLength": 5"`` with whole number input.                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Password Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

Set the required character types to be included in a valid password. Defaults to allow any characters unless otherwise specified by the checkboxes. The error messasage previewed in the System Console will appear on the account creation page if a user enters an invalid password.

- **At least one lowercase letter**: Select this checkbox if a valid password must contain at least one lowercase letter.
- **At least one uppercase letter**: Select this checkbox if a valid password must contain at least one uppercase letter.
- **At least one number**: Select this checkbox if a valid password must contain at least one number.
- **At least one symbol**: Select this checkbox if a valid password must contain at least one symbol. Valid symbols include: ``!"#$%&'()*+,-./:;<=>?@[]^_`|~``

This feature's ``config.json`` settings are, respectively:

.. list-table::
    :widths: 80

    * - ``"Lowercase": false`` with options ``true`` and ``false``
    * - ``"Number": false`` with options ``true`` and ``false``
    * - ``"Uppercase": false`` with options ``true`` and ``false``
    * - ``"Symbol": false`` with options ``true`` and ``false``

Maximum Login Attempts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Failed login attempts allowed before a user is locked out and required to reset their password via email.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaximumLoginAttempts": 10`` with whole number input.                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Public Links
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Public File Links
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Allow users to generate public links to files and images for sharing outside the Mattermost system with a public URL.

**False**: The Get Public Link option is hidden from the image preview user interface.

**Note:** When switched to **False**, anyone who tries to visit a previously generated public link will receive an error message saying public links have been disabled. When switched back to **True**, old public links will work again unless the **Public Link Salt** has been regenerated.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePublicLink": true`` with options ``true`` and ``false`` for above settings respectively.                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Public Link Salt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
32-character salt added to the URL of public links when public links are enabled. Click **Regenerate** in the System Console to create a new salt, which will invalidate all existing public links.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicLinkSalt": ""``  with string input.                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

_________

Sessions
~~~~~~~~~~~~~~~~~~~~~~~~~
Session length for email and AD/LDAP authentication (days)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set the number of days before web sessions expire and users will need to log in again.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionLengthWebInDays" : 30`` with whole number input.                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Session length for mobile apps (days)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set the number of days before native mobile sessions expire.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionLengthMobileInDays" : 30`` with whole number input.                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Session length for GitLab SSO authentication (days)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set the number of days before SSO sessions expire.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionLengthSSOInDays" : 30`` with whole number input.                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Session Cache (minutes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set the number of minutes to cache a session in memory.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionCacheInMinutes" : 10`` with whole number input.                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Connections
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable cross-origin requests from
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enable HTTP cross-origin requests from specific domains separated by spaces. Type ``*`` to allow CORS from any domain or leave it blank to disable it.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCorsFrom": ""`` with string input.                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Insecure Outgoing Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Outgoing HTTPS requests can accept unverified, self-signed certificates. For example, outgoing webhooks to a server with a self-signed TLS certificate, using any domain, will be allowed.

**False**: Only secure HTTPS requests are allowed.

Security note: Enabling this feature makes these connections susceptible to man-in-the-middle attacks.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableInsecureOutgoingConnections": false`` with options ``true`` and ``false`` for above settings respectively.        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Notifications
--------------------------------
Settings to configure email and mobile push notifications.

Email
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Email Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Enables sending of email notifications.

**False**: Disables email notifications for developers who may want to skip email setup for faster development. Setting this to true removes the **Preview Mode: Email notifications have not been configured** banner (requires logging out and logging back in after setting is changed)

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SendEmailNotifications": false`` with options ``true`` and ``false`` for above settings respectively.                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Email Batching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Users can select how often to receive email notifications, and multiple notifications within that timeframe will be combined into a single email. Batching will occur at a default interval of 15 minutes, configurable in **Account Settings** > **Notifications**. Note: Email batching cannot be enabled unless the `SiteURL <https://docs.mattermost.com/administration/config-settings.html#site-url>`_ is configured. Email batching in `High Availability mode <https://docs.mattermost.com/administration/config-settings.html#enable-high-availability-mode>`_ is planned but not yet supported.

**False**: If email notifications are enabled in Account Settings, emails will be sent individually for every mention or direct message received.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmailBatching": false`` with options ``true`` and ``false`` for above settings respectively.                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Notification Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Send full message contents**: Sender name and channel are included in email notifications. 

**Send generic description with only sender name**: The team name and name of the person who sent the message, with no information about channel name or message contents, is included in email notifications. Typically used for compliance reasons if Mattermost contains confidential information and policy dictates it cannot be stored in email.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailNotificationContentsType": "full"`` with options ``full`` and ``generic`` for above settings respectively.                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Notification Display Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Name displayed on email account used when sending notification emails from Mattermost system.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackName": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Notification From Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Address displayed on email account used when sending notification emails from Mattermost system.

So you don't miss messages, please make sure to change this value to an email your system administrator receives, example: `admin@yourcompany.com`.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackEmail": ""`` with string input.                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Notification Footer Mailing Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Organization name and mailing address displayed in the footer of email notifications from Mattermost, such as "© ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA". If the field is left empty, the organization name and mailing address will not be displayed.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackOrganization": ""`` with string input.                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SMTP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Location of SMTP email server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPServer": ""``  with string input.                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SMTP Server Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Port of SMTP email server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPPort": ""`` with string input.                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable SMTP Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: SMTP username and password are used for authenticating to the SMTP server.

**False**: Mattermost doesn't attempt to autehenticate to the SMTP server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSMTPAuth": false`` with options ``true`` and ``false`` for above settings respectively.                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SMTP Server Username
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The username for authenticating to the SMTP server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPUsername": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SMTP Server Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The password associated with the SMTP username.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPPassword": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Connection Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``None``: Send email over an unsecure connection.

``TLS``: Communication between Mattermost and your email server is encrypted.

``STARTTLS``: Attempts to upgrade an existing insecure connection to a secure connection using TLS.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionSecurity": ""`` with options ``""``, ``TLS`` and ``STARTTLS`` for above settings respectively.                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Security Alerts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Enable System Admins to be notified by email if a relevant security fix alert is announced. Requires email to be enabled. To learn more about this feature, see :doc:`telemetry`.

**False**: Security alerts are disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSecurityFixAlert": true`` with options ``true`` and ``false`` for above settings respectively.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Mobile Push
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Push Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Your Mattermost server sends mobile push notifications to the server specified in **PushNotificationServer**.

**False**: Mobile push notifications are disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SendPushNotifications": false`` with options ``true`` and ``false`` for above settings respectively.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Push Notification Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Location of Mattermost Push Notification Service (MPNS), which re-sends push notifications from Mattermost to services like Apple Push Notification Service (APNS) and Google Cloud Messaging (GCM).

To confirm push notifications are working, connect to the `Mattermost iOS App on iTunes <https://about.mattermost.com/mattermost-ios-app>`_ or the `Mattermost Android App on Google Play <https://about.mattermost.com/mattermost-android-app>`_:

- For Enterprise Edition, enter ``http://push.mattermost.com``
- For Team Edition, enter ``http://push-test.mattermost.com``

Please review full documentation on `push Notifications and mobile applications <http://docs.mattermost.com/deployment/push.html>`_ including guidance on compiling your own mobile apps and MPNS before deploying to production.

Note: The ``http://push-test.mattermost.com`` provided for testing push notifications prior to compiling your own service please make sure `to read about its limitations <http://docs.mattermost.com/deployment/push.html#push-notifications-for-team-edition-users>`_.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PushNotificationServer": ""`` with string input.                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Push Notification Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Send generic description with only sender name**: Push notifications include only the name of the person who sent the message but no information about channel name or message text.

**Send generic description with user and channel names**: Push notifications include names of users and channels but no specific details from the message text.

**Send full message snippet**: Selecting "Send full message snippet" sends excerpts from messages triggering notifications with specifics and may include confidential information sent in messages. If your Push Notification Service is outside your firewall, it is HIGHLY RECOMMENDED this option only be used with an "https" protocol to encrypt the connection.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PushNotificationContents": "generic"`` with options ``generic_no_channel``, ``generic`` and ``full`` for above settings respectively.           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Troubleshooting Push Notifications**

To confirm push notifications are working:

1. Go to **System Console > Notifications > Mobile Push > Send Push Notifications** and select **Use iOS and Android apps on iTunes and Google Play with TPNS**.
2. Set **Push Notification Server** to *http://push.mattermost.com* if using Enterprise Edition. If using Team Edition, set the value to *http://push-test.mattermost.com*.
3. To confirm push notifications are working, connect to the `Mattermost iOS App on iTunes <https://about.mattermost.com/mattermost-ios-app>`_ or the `Mattermost Android App on Google Play <https://about.mattermost.com/mattermost-android-app>`_ and log in to your team site.
4. Close the app on your device, and close any other connections to your team site.
5. Wait 5 minutes and have another team member send you a direct message, which should trigger a push notification to the Mattermost app on your mobile device.
6. You should receive a push notification on your device alerting you of the direct message.

If you did not receive an alert:

1. Set **System Console > General > Logging > File Log Level** to *DEBUG* (make sure to set this back to *INFO* after troubleshooting to save disk space).
2. Repeat the above steps.
3. Go to **System Console > Logs** and copy the log output into a file.
4. For Enterprise Edition customers, `submit a support request with the file attached <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. For Team Edition users, please start a thread in the `Troubleshooting forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`_ for peer-to-peer support.

________

Integrations
--------------------------------
Settings to configure webhooks, slash commands and external integration services.

Custom Integrations
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Incoming Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Developers building integrations can create webhook URLs for public channels and private channels. Please see our `documentation page <http://docs.mattermost.com/developer/webhooks-incoming.html>`_ to learn about creating webhooks, view samples, and to let the community know about integrations you have built.

**True**: Incoming webhooks will be allowed. To manage incoming webhooks, go to **Account Settings > Integrations**. The webhook URLs created in Account Settings can be used by external applications to create posts in any public or private channels that you have access to.

**False**: The Integrations > Incoming Webhooks section of Account Settings is hidden and all incoming webhooks are disabled.

Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIncomingWebhooks": true`` with options ``true`` and ``false`` for above settings respectively.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Outgoing Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Developers building integrations can create webhook tokens for public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in public channels. Please see our `documentation page <http://docs.mattermost.com/developer/webhooks-outgoing.html>`_ to learn about creating webhooks and view samples.

**True**: Outgoing webhooks will be allowed. To manage outgoing webhooks, go to **Account Settings > Integrations**.

**False**: The Integrations > Outgoing Webhooks section of Account Settings is hidden and all outgoing webhooks are disabled.

Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOutgoingWebhooks": true`` with options ``true`` and ``false`` for above settings respectively.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Custom Slash Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Slash commands send events to external integrations that send a response back to Mattermost.

**True**: Allow users to create custom slash commands from **Main Menu** > **Integrations** > **Commands**.

**False**: Slash Commands are hidden in the **Integrations** user interface.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCommands": false`` with options ``true`` and ``false`` for above settings respectively.                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable OAuth 2.0 Service Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.

**False**: Mattermost does not function as an OAuth 2.0 service provider.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"EnableOAuthServiceProvider": false`` with options ``true`` and ``false`` for above settings respectively.               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Restrict managing integrations to Admins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: When true, webhooks and slash commands can only be created, edited and viewed by Team and System Admins, and OAuth 2.0 applications by System Admins. Integrations are available to all users after they have been created by the Admin.

**False**: Any team members can create webhooks, slash commands and OAuth 2.0 applications from **Main Menu** > **Integrations**.

Note: OAuth 2.0 applications can be authorized by all users if they have the **Client ID** and **Client Secret** for an app setup on the server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOnlyAdminIntegrations": true`` with options ``true`` and ``false`` for above settings respectively.               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override usernames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`_, will be allowed to change the username they are posting as. If no username is present, the username for the post is the same as it would be for a setting of **False**.

**False**: Custom slash commands can only post as the username of the user who used the slash command. OAuth 2.0 apps can only post as the username of the user who set up the integration. For incoming webhooks and outgoing webhooks, the username is "webhook". See http://mattermost.org/webhooks for more details.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostUsernameOverride": false`` with options ``true`` and ``false`` for above settings respectively.               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override profile picture icons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Webhooks, slash commands and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`_, will be allowed to change the profile picture they post with.

**False**: Webhooks, slash commands and OAuth 2.0 apps can only post with the profile picture of the account they were set up with. See http://mattermost.org/webhooks for more details.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostIconOverride": false`` with options ``true`` and ``false`` for above settings respectively.                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Personal Access Tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: When true, users can create `personal access tokens <https://about.mattermost.com/default-user-access-tokens>`_ for integrations in **Account Settings > Security**. They can be used to authenticate against the API and give full access to the account.

To manage who can create personal access tokens or to search users by token ID, go to the **System Console > Users** page.

**False**: Personal access tokens are disabled on the server.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserAccessTokens": false`` with options ``true`` and ``false`` for above settings respectively.                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

JIRA (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable JIRA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: You can configure JIRA webhooks to post message in Mattermost. To help combat phishing attacks, all posts are labelled by a BOT tag.

**False**: JIRA webhook integration is not enabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enabled": false`` with options ``true`` and ``false`` for above settings respectively.                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select the username that this integration is attached to.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserName": ""`` with string input                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The secret used to authenticate to Mattermost. Regenerating the secret for the webhook URL endpoint invalidates your existing JIRA integrations.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note that to set up a JIRA integration via ``config.json``, you can use the following format:

  .. code-block:: text

    "Plugins": {
        "jira": {
            "Enabled": true,
            "Secret": "k-ZtjoTrmIdPs7eAGjalDEK_3Q8r3gXJ",
            "UserName": "jira"
        }
    }

where ``Enabled``, ``Secret`` and ``UserName`` are specified above.
________

WebRTC (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Mattermost WebRTC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Mattermost will allow making one-on-one video calls on Chrome, Firefox and `Mattermost Desktop Apps <https://about.mattermost.com/download/#mattermostApps>`_ on a server running in SSL mode.

**False**: Mattermost doesn't allow one-on-one video calls.

Note: To enable the Mattermost WebRTC service, the System Administrator agrees to the `Terms of Service <https://about.mattermost.com/webrtc-terms/>`_ and `Privacy Policy <https://about.mattermost.com/webrtc-privacy/>`_.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Gateway Websocket URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is the websocket used to signal and establish communication between the peers. Enter ``wss://<mattermost-webrtc-gateway-url>:<port>``. Make sure you use WS or WSS in your URL depending on your server configuration.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GatewayWebsocketUrl": ""`` with string input                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Gateway Admin URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost WebRTC uses this URL to obtain valid tokens for each peer to establish the connection. Enter ``https://<mattermost-webrtc-gateway-url>:<port>/admin``. Make sure you use HTTP or HTTPS in your URL depending on your server configuration.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GatewayAdminUrl": ""`` with string input                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Gateway Admin Secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter your admin secret password to access the Gateway Admin URL.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GatewayAdminSecret": ""`` with string input                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

STUN URI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter your STUN URI as ``stun:<your-stun-url>:<port>``. STUN is a standardized network protocol to allow an end host to assist devices to access its public IP address if it is located behind a NAT.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"StunURI": ""`` with string input                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

TURN URI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter your TURN URI as ``turn:<your-turn-url>:<port>``. TURN is a standardized network protocol to allow an end host to assist devices to establish a connection by using a relay public IP address if it is located behind a symmetric NAT.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TurnURI": ""`` with string input                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

TURN Username
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter your TURN Server Username.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TurnUsername": ""`` with string input                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

TURN Shared Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enter your TURN Server Shared Key. This is used to created dynamic passwords to establish the connection. Each password is valid for a short period of time.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TurnSharedKey": ""`` with string input                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

External Services
~~~~~~~~~~~~~~~~~~~~~~~~~
Google API Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Mattermost offers the ability to embed YouTube videos from URLs shared by end users. Set this key to enable the display of titles for embedded YouTube video previews. Without the key, YouTube previews will still be created based on hyperlinks appearing in messages or comments but they will not show the video title. If Google detects the number of views is exceedingly high, they may throttle embed access. Should this occur, you can remove the throttle by registering for a Google Developer Key and entering it in this field following these instructions: https://www.youtube.com/watch?v=Im69kzhpR3I. Your Google Developer Key is used in client-side Javascript.

Using a Google API Key allows Mattermost to detect when a video is no longer available and display the post with a *Video not found* label.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GoogleDeveloperKey": ""`` with string input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Files
--------------------------------
Settings to configure files storage and image handling.

Storage
~~~~~~~~~~~~~~~~~~~~~~~~~
File Storage System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Storage system where files and image attachments are saved.

**Local File System**: Files and images are stored in the specified local file directory.

**Amazon S3**: Files and images are stored on Amazon S3 based on the provided access key, bucket and region fields. The ``amazons3`` driver is compatible with Minio (Beta) based on the provided access key, bucket and region fields.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DriverName": "local"`` with options ``local`` and ``amazons3`` for above settings respectively.                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Local Storage Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Directory to which files are written. If blank, directory will be set to ./data/.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./data/"`` with string input.                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Access Key ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this credential from your Amazon AWS administrator.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3AccessKeyId": ""`` with string input.                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Secret Access Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obtain this credential from your Amazon AWS administrator.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SecretAccessKey": ""`` with string input.                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Bucket
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Name you selected for your S3 bucket in AWS.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3Bucket": ""`` with string input.                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Hostname of your S3 Compatible Storage provider. Defaults to ``s3.amazonaws.com``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3Endpoint": "s3.amazonaws.com"`` with string input.                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Secure Amazon S3 Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Enables only secure Amazon S3 Connections.

**False**: Allows insecure connections to Amazon S3.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SSL": true`` with options ``true`` and ``false`` for above settings respectively.                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Server-Side Encryption for Amazon S3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Available in Enterprise Edition E20*

**True**: Encrypts files in Amazon S3 using server-side encryption with `Amazon S3-managed keys <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`_.

**False**: Doesn't encrypt files in Amazon S3.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SSE": true`` with options ``true`` and ``false`` for above settings respectively.                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Amazon S3 Debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Additional debugging information is included in the system logs. Typically set to `false` in production.

**False**: No Amazon S3 debugging information is included in the system logs.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3Trace": false`` with options ``true`` and ``false`` for above settings respectively.                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow File Sharing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When false, disables file sharing on the server. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileAttachments": true`` with options ``true`` and ``false``.    |
+---------------------------------------------------------------------------------------------------------------------+

Allow File Uploads on Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E20*

When false, disables file uploads on mobile apps. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileUpload": true`` with options ``true`` and ``false``.       |
+---------------------------------------------------------------------------------------------------------------------+

Allow File Downloads on Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E20*

When false, disables file downloads on mobile apps. Users can still download files from a mobile web browser.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileDownload": true`` with options ``true`` and ``false``.     |
+---------------------------------------------------------------------------------------------------------------------+

Maximum File Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Maximum file size for message attachments entered in megabytes in the System Console UI. Converted to bytes in ``config.json`` at 1048576 bytes per megabyte.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxFileSize": 52428800`` with whole number input.                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. warning:: Verify server memory can support your setting choice. Large file sizes increase the risk of server crashes and failed uploads due to network disruptions.

________

Images
~~~~~~~~~~~~~~~~~~~~~~~~~
Attachment Thumbnail Width
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Removed in July 16th, 2017 release*

Width of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ThumbnailWidth": 120`` with whole number input.                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Attachment Thumbnail Height
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Removed in July 16th, 2017 release*

Height of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ThumbnailHeight": 100`` with whole number input.                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Image Preview Width
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Removed in July 16th, 2017 release*

Maximum width of preview image. Updating this value changes how preview images render in future, but does not change images created in the past.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PreviewWidth": 1024`` with whole number input.                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Image Preview Height
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Removed in July 16th, 2017 release*

Maximum height of preview image ("0": Sets to auto-size). Updating this value changes how preview images render in future, but does not change images created in the past.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PreviewHeight": 0`` with whole number input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Profile Picture Width
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Removed in July 16th, 2017 release*

The width to which profile pictures are resized after being uploaded via Account Settings.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ProfileWidth": 128`` with whole number input.                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Profile Picture Height
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Removed in July 16th, 2017 release*

The height to which profile pictures are resized after being uploaded via Account Settings.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ProfileHeight": 128`` with whole number input.                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Customization
--------------------------------
Settings to customize your deployment with custom branding and legal and support links.

Custom Branding
~~~~~~~~~~~~~~~~~~~~~~~~~

Site Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Name of service shown in login screens and UI. Maximum 30 characters.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SiteName": "Mattermost"`` with string input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Custom Branding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

**True**: Enables custom branding to show a JPG image some custom text on the server login page.

**False**: Custom branding is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomBrand": false`` with options ``true`` and ``false`` for above settings respectively.                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Custom Brand Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

Custom JPG image is displayed on left side of server login page. Recommended maximum image size is less than 2 MB because image will be loaded for every user who logs in.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This features has no ``config.json`` setting and must be set in the System Console user interface.                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Custom Brand Text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

Custom text will be shown below custom brand image on left side of server login page. Maximum 500 characters allowed. You can format this text using the same `Markdown formatting codes <http://docs.mattermost.com/help/messaging/formatting-text.html>`_ as using in Mattermost messages.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomBrandText": ""`` with string input.                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Site Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*
Description of service shown in login screens and UI. When not specified, "All team communication in one place, searchable and accessible anywhere" is displayed.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"CustomDescriptionText": ""`` with string input.                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Link Previews
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Link Previews
^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Enables users to display a preview of website content below the message, if available. When true, website previews can be enabled from Account Settings > Advanced > Preview pre-release features.

**False**: Website link previews are disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLinkPreviews": false`` with options ``true`` and ``false`` for above settings respectively.                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Emoji
~~~~~~~~~~~~~~~~~~~~~~~~~
Enable Emoji Picker
^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Enables an emoji picker that allows users to select emoji to add as reactions or use in messages. Enabling the emoji picker with a large number of custom emoji may slow down performance.

**False**: Emoji picker is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomEmoji": true`` with options ``true`` and ``false`` for above settings respectively.                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Custom Emoji
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Enables a Custom Emoji option in the Main Menu, where users can go to create customized emoji.

**False**: Custom emojis are disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomEmoji": false`` with options ``true`` and ``false`` for above settings respectively.                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Restrict Custom Emoji Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

**Allow everyone to create custom emoji**: Allows everyone to create custom emoji from the **Main Menu** > **Custom Emoji**.

**Allow System and Team Admins to create custom emoji**: The Custom Emoji option is hidden from the Main Menu for users who are not System or Team Admins.

**Only allow System Admins to create custom emoji**: The Custom Emoji option is hidden from the Main Menu for users who are not System or Team Admins.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictCustomEmojiCreation": "all"`` with options ``all``, ``admin`` and ``system_admin`` for above settings respectively. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Legal and Support
~~~~~~~~~~~~~~~~~~~~~~~~~
Legal and Support links will be hidden in the user interface if these fields are left blank.

Terms of Service link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configurable link to Terms of Service your organization may provide to end users. By default, links to a Terms of Service page hosted on about.mattermost.com. If changing the link to a different Terms of Service, make sure to include the "Mattermost Conditions of Use" notice to end users that must also be shown to users from the "Terms of Service" link.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TermsOfServiceLink": "https://about.mattermost.com/default-terms/"`` with string input.                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Privacy Policy link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configurable link to Privacy Policy your organization may provide to end users.  By default, links to a Privacy Policy page hosted on about.mattermost.com.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivacyPolicyLink": "https://about.mattermost.com/default-privacy-policy/"`` with string input.                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

About link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configurable link to an About page describing your organization may provide to end users. By default, links to an About page hosted on about.mattermost.com.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AboutLink": "https://about.mattermost.com/default-about/"`` with string input.                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Help link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configurable link to a Help page your organization may provide to end users. By default, links to Mattermost help documentation hosted on `docs.mattermost.com <https://docs.mattermost.com/>`_ .

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"HelpLink": "https://about.mattermost.com/default-help/"`` with string input.                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Report a Problem link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set the link for the support website.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReportAProblemLink": "https://about.mattermost.com/default-report-a-problem/"`` with string input.                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Support Email
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set an email for feedback or support requests.

So you don't miss messages, please make sure to change this value to an email your system administrator receives, example: `support@yourcompany.com`.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SupportEmail":"feedback@mattermost.com"`` with string input.                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Mattermost App Links
~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Apps Download Page Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configurable link to a download page for Mattermost Apps. When a link is present, an option to "Download Apps" will be added in the Main Menu so users can find the download page. Leave this field blank to hide the option from the Main Menu. Defaults to a page on about.mattermost.com where users can download the iOS, Android, and Desktop clients. If you are using an `Enterprise App Store <https://docs.mattermost.com/deployment/push.html?highlight=enterprise%20app#push-notifications-and-mobile-devices>`_ for your mobile apps, change this link to point to a customized download page where users can find the correct apps.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AppDownloadLink": "https://about.mattermost.com/downloads/"`` with string input.                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Android App Download Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configurable link to download the Android app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an `Enterprise App Store <https://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>`_ for your mobile apps, change this link to point to the correct app.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidAppDownloadLink": "https://about.mattermost.com/mattermost-android-app/"`` with string input.                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

iOS App Download Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configurable link to download the iOS app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an `Enterprise App Store <https://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>`_ for your mobile apps, change this link to point to the correct app.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosAppDownloadLink": "https://about.mattermost.com/mattermost-ios-app/"`` with string input.                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Advanced
--------------------------------
Advanced settings to configure rate limiting, databases and developer options.

Rate Limiting
~~~~~~~~~~~~~~~~~~~~~~~~~
Changing properties in this section will require a server restart before taking effect.

Enable Rate Limiting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: APIs are throttled at the rate specified by **PerSec**.

**False**: APIs are not throttled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Maximum Queries per Second
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Throttle API at this number of requests per second if rate limiting is enabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PerSec": 10`` with whole number input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Maximum Burst Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Maximum number of requests allowed beyond the per second query limit.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxBurst": 100`` with whole number input.                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Memory Store Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Maximum number of user sessions connected to the system as determined by **VaryByRemoteAddr** and **VaryByHeader** variables.

Typically set to the number of users in the system.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MemoryStoreSize": 10000`` with whole number input.                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Vary rate limit by remote address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Rate limit API access by IP address. Recommended to set to ``true`` if you're using a proxy.

**False**: Rate limiting does not vary by IP address.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"VaryByRemoteAddr": true`` with options ``true`` and ``false`` for above settings respectively.                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Vary rate limit by HTTP header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Vary rate limiting by HTTP header field specified (e.g. when configuring Ngnix set to "X-Real-IP", when configuring AmazonELB set to "X-Forwarded-For"). Recommended to be set if you're using a proxy.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"VaryByHeader": ""`` with string input.                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________


Database
~~~~~~~~~~~~~~~~~~~~~~~~~
Changing properties in this section will require a server restart before taking effect.

Driver Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This setting can only be changed from config.json file, it cannot be changed from the System Console user interface.

``mysql``: enables driver to MySQL database.

``postgres``: enables driver to PostgreSQL database.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DriverName": "mysql"`` with string input.                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Data Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is the connection string to the master database. When **DriverName** ="postgres" then use a connection string in the form ``postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10``. This setting can only be changed from config.json file, it cannot be changed from the System Console user interface.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DataSource": ""`` with string input.                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Maximum Idle Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Maximum number of idle connections held open to the database.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxIdleConns": 10`` with whole number input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Maximum Open Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Maximum number of open connections held open to the database.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxOpenConns": 10`` with whole number input.                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SQL Query Timeout
^^^^^^^^^^^^^^^^^
The number of seconds to wait for a response from the database after opening a connection and sending the query. Errors that you see in the UI or in the logs as a result of a query timeout can vary depending on the type of query.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"QueryTimeout": 30`` with whole number input, in the *SqlSettings* section. |
+-------------------------------------------------------------------------------------------------------------------------+

At Rest Encrypt Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A 32-character key for encrypting and decrypting sensitive fields in the database. You can generate your own cryptographically random alphanumeric string, or you can go to **System Console > Advanced > Database** and click **Regenerate**, which displays the value until you click **Save**.

When using High Availability, the salt must be identical in each instance of Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AtRestEncryptKey": ""`` with string input.  |
+------------------------------------------------------------------------------------------+

Trace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Executing SQL statements are written to the log for development.

**False**: SQL statements are not written to the log.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Trace": false`` with options ``true`` and ``false`` for above settings respectively.                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Recycle Database Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E20*

This button reconnects to the database listed in the configuration settings. All old connections are closed after 20s.

The workflow for failover without downing the server is to change the database line in the config.json file, click **Reload Configuration from Disk** in the General > Configuration section then click **Recycle Database Connections**.

________


Elasticsearch (Beta)
~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

Changing properties in this section will require a server restart before taking effect.

Enable Elasticsearch Indexing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True:** indexing of new posts occurs automatically. Search queries will use database search until "Enable Elasticsearch for search queries" is enabled. `Learn more about Elasticsearch in our documentation.<https://about.mattermost.com/default-elasticsearch-documentation/>`_

**False:** Elasticsearch indexing is disabled and new posts are not indexed. If indexing is disabled and re-enabled after an index is created, it is recommended to purge and rebuild the index to ensure complete search results. 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIndexing": false`` with options ``true`` and ``false`` for above settings respectively.                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Server Connection Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The address of the Elasticsearch server. `Learn more about Elasticsearch in our documentation.<https://about.mattermost.com/default-elasticsearch-documentation/>`_

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionUrl": ""`` with string input.                                   |
+------------------------------------------------------------------------------------------------------------------------+

Server Username
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The username to authenticate to the Elasticsearch server.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Username": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------+

Server Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Optional) The password to authenticate to the Elasticsearch server.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Password": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------+

Enable Cluster Sniffing
^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Sniffing finds and connects to all data nodes in your cluster automatically.
**False**: Sniffing is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Sniff": false`` with options ``true`` and ``false`` for above settings respectively.                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Bulk Indexing
^^^^^^^^^^^^^^^^^^^^^^^^
This button starts a bulk index of all existing posts in the database. If the indexing process is cancelled the index and search results will be incomplete. 

Purge Indexes
^^^^^^^^^^^^^^^^^^^^^^^^
This button purges the entire Elasticsearch index. Typically only used if the index has corrupted and search is not behaving as expected. After purging the index a new index can be created with the **Bulk Index** button.

Enable Elasticsearch for search queries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Elasticsearch will be used for all search queries using the latest index. Search results may be incomplete until a bulk index of the existing post database is finished.
**False**: Database search is used for search queries.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSearching": false`` with options ``true`` and ``false`` for above settings respectively.                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________


Developer
~~~~~~~~~~~~~~~~~~~~~~~~~

Enable Testing Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: `/test` slash command is enabled to load test accounts and test data.

**False**: `/test` slash command is disabled.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTesting": false`` with options ``true`` and ``false`` for above settings respectively.                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Developer Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Javascript errors are shown in a purple bar at the top of the user interface. Not recommended for use in production.

**False**: Users are not alerted to Javascript errors.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDeveloper": false`` with options ``true`` and ``false`` for above settings respectively.                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow untrusted internal connections to
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In testing environments, such as when developing integrations locally on a development machine, use this setting to specify domains, IP addresses, or CIDR notations to allow internal connections. **Not recommended for use in production**, since this can allow a user to extract confidential data from your server or internal network.

By default, user-supplied URLs such as those used for Open Graph metadata, webhooks, or slash commands will not be allowed to connect to reserved IP addresses including loopback or link-local addresses used for internal networks. Push notification, OAuth 2.0 and WebRTC server URLs are trusted and not affected by this setting.

Separate two or more domains with spaces instead of commas, for example: ``webhooks.internal.example.com 127.0.0.1 10.0.16.0/28``

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowedUntrustedInternalConnections": ""`` with string input.                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
________________________________________________________________________________________________________________________________________________________________________

.. _high-availability:

High Availability
~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

Changing properties in this section will require a server restart before taking effect.

When High Availability mode is enabled, the System Console is set to read-only and settings can only be changed by editing the configuration file directly. However, for testing and validating a High Availability setup, you can set *ReadOnlyConfig* to ``false``, which allows changes made in the System Console to be saved back to the configuration file.

To learn more about configuring High Availability, see `High Availability Cluster <../deployment/cluster.html>`_.

Enable High Availability Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: The Mattermost Server will attempt inter-node communication with the other servers in the cluster that have the same Cluster Name. This sets the System Console to read-only mode to keep the servers ``config.json`` files in sync.

**False**: Mattermost high availability is disabled.

+-----------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------+

Cluster Name
^^^^^^^^^^^^
The cluster to join by name. Only nodes with the same cluster name will join together. This is to support Blue-Green deployments or staging pointing to the same database.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClusterName": ""`` with string input. |
+------------------------------------------------------------------------------------+

Override Hostname
^^^^^^^^^^^^^^^^^
If blank, Mattermost attempts to get the Hostname from the OS or use the IP Address. You can override the hostname of this server with this property. It is not recommended to override the Hostname unless needed. This property can also be set to a specific IP Address if needed.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"OverrideHostname": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Use IP Address
^^^^^^^^^^^^^^
**True**: The cluster attempts to communicate using the IP Address.

**False**: The cluster attempts to communicate using the hostname.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseIpAddress": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Use Experimental Gossip
^^^^^^^^^^^^^^^^^^^^^^^
**True**: The server attempts to communicate via the gossip protocol over the gossip port.

**False**: The server attempts to communicate over the streaming port.

Note that the gossip port and gossip protocol are used to determine cluster health even when this setting is ``false``.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseExperimentalGossip": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Read Only Config
^^^^^^^^^^^^^^^^
**True**: Changes made to settings in the System Console are ignored.

**False**: Changes made to settings in the System Console are written to ``config.json``.

When running in production it is recommended to set this to true.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReadOnlyConfig": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

Gossip Port
^^^^^^^^^^^
The port used for the gossip protocol. Both UDP and TCP should be allowed on this port.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GossipPort": 8074`` with whole number input. |
+-------------------------------------------------------------------------------------------+

Streaming Port
^^^^^^^^^^^^^^
The port used for streaming data between servers.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"StreamingPort": 8075`` with whole number input. |
+----------------------------------------------------------------------------------------------+

Inter-Node Listen Address
^^^^^^^^^^^^^^^^^^^^^^^^^
*Deprecated. Not used in version 4.0 and later*

The address the Mattermost Server will listen on for inter-node communication. When setting up your network you should secure the listen address so that only machines in the cluster have access to that port. This can be done in different ways, for example, using IPsec, security groups, or routing tables.

+-----------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"InterNodeListenAddress": ":8075"`` with string input. |
+-----------------------------------------------------------------------------------------------------+

Inter-Node URLs
^^^^^^^^^^^^^^^
*Deprecated. Not used in version 4.0 and later*

A list of all the machines in the cluster, separated by commas, for example, ``["http://10.10.10.2", "http://10.10.10.4"]``. It is recommended to use the internal IP addresses so all the traffic can be secured.

+--------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"InterNodeUrls": []`` with string input. |
+--------------------------------------------------------------------------------------+

________________________________________________________________________________________________________________________________________________________________________

Performance Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

Enable Performance Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Mattermost enables performance monitoring collection and profiling. Please see `documentation <https://docs.mattermost.com/deployment/metrics.html>`_ to learn more about configuring performance monitoring for Mattermost.

**False**: Mattermost performance monitoring is disabled.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false`` for above settings respectively.                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Listen Address
^^^^^^^^^^^^^^^^^^
The address the Mattermost server will listen on to expose performance metrics.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"InterNodeListenAddress": ":8067"`` with string input.                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

------

Settings configurable only in config.json
-----------------------------------------

There are a number of settings customizable in ``config.json`` unavailable in the System Console and require updating from the file itself.

Service Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

License File Location
^^^^^^^^^^^^^^^^^^^^^

Path and filename of the license file on disk. On startup, if Mattermost cannot find a valid license in the database from a previous upload, it looks here. It can be an absolute path, or a path relative to the ``mattermost`` directory.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LicenseFileLocation": ""`` with string input.  |
+---------------------------------------------------------------------------------------------+

Cluster Log Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This setting defines the frequency of cluster request time logging for :doc:`../deployment/metrics`, measured in milliseconds.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClusterLogTimeoutMilliseconds": 2000`` with whole number input.                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Searching of Posts
^^^^^^^^^^^^^^^^^^^^^^^^^

If this setting is enabled, users can search messages. Disabling search can result in a performance increase, but users get an error message when they attempt to use the search box.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Enable User Typing Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This setting determines whether "user is typing..." messages are displayed below the message box. Disabling the setting in larger deployments may improve server performance.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserTypingMessages": "true"`` with string input.                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Time Between User Typing Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This setting defines how frequently "user is typing..." messages are updated, measured in milliseconds.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TimeBetweenUserTypingUpdatesMilliseconds": 5000`` with whole number input.                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable User Status Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^
Turn status updates off to improve performance. When status updates are off, users appear online only for brief periods when posting a message, and only to members of the channel in which the message is posted.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserStatuses": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Enable Channel Viewed WebSocket Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This setting determines whether channel_viewed WebSocket events are sent, which synchronize unread notifications across clients and devices. Disabling the setting in larger deployments may improve server performance.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableChannelViewedMessages": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Segment Write Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Removed in March 16, 2017 release*

For deployments seeking additional tracking of system behavior using Segment.com, you can enter a Segment WRITE_KEY using this field. This value works like a tracking code and is used in client-side Javascript and will send events to Segment.com attributed to the account you used to generate the WRITE_KEY.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SegmentDeveloperKey": ""`` with string input.                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

WebSocket Secure Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Optional) This setting defines the port on which the secured WebSocket will listen using the `wss` protocol. Otherwise it defaults to `443`. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is  ``"WebsocketSecurePort" : 443`` with whole number input.                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

WebSocket Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Optional) this setting defines the port on which the unsecured WebSocket will listen using the `ws` protocol. Otherwise it defaults to `80`. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``WebsocketPort": 80`` with whole number input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

SQL Settings
~~~~~~~~~~~~

Read Replicas (Enterprise Edition)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Specifies the connection strings for the read replica databases. Each string must be in the same form as used for the `Data Source`_ setting. A server restart is required for changes to this setting to take effect.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DataSourceReplicas": []`` with a comma-separated list of database connection strings as input. |
+---------------------------------------------------------------------------------------------------------------------------------------------+

Search Replicas (Enterprise Edition)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Specifies the connection strings for the search replica databases. A search replica is similar to a read replica, but is used only for handling search queries. Each string must be in the same form as used for the `Data Source`_ setting. A server restart is required for changes to this setting to take effect.

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DataSourceSearchReplicas": []`` with a comma-separated list of database connection strings as input. |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

Team Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

User Status Away Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^

This setting defines the number of seconds after which the user's status indicator changes to "Away", when they are away from Mattermost.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"UserStatusAwayTimeout": 300`` with whole number input.                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable X to Leave Channels from Left-Hand Sidebar (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: Users can leave Public and Private Channels by clicking the "x" beside the channel name.

**False**: Users must use the **Leave Channel** option from the channel menu to leave channels.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableXToLeaveChannelsFromLHS": false`` with options ``true`` and ``false`` for above settings respectively.               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Town Square is Read-Only (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

**True**: Only Administrators can post in Town Square.

**False**: Anyone can post in Town Square.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``""ExperimentalTownSquareIsReadOnly"": false`` with options ``true`` and ``false`` for above settings respectively.               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

File Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
Initial Font
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Font used in auto-generated profile pics with colored backgrounds.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InitialFont": "luximbi.ttf"`` with string input.                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Region
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AWS region you selected for creating your S3 bucket. Refer to `AWS Reference Documentation <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`_ and choose this variable from the Region column.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3Region": ""`` with string input.                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Bucket Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set an endpoint URL for Amazon S3 buckets.

*Removed in November 16th, 2016 release*

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3BucketEndpoint": ""`` with string input.                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Location Constraint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: S3 region is location constrained.

**False**: S3 region is not location constrained.

*Removed in November 16th, 2016 release*

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3LocationConstraint": false`` with options ``true`` and ``false`` for above settings respectively.               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Lowercase Bucket
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**True**: S3 bucket names are fully lowercase.

**False**: S3 bucket names may contain uppercase and lowercase letters.

*Removed in November 16th, 2016 release*

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3LowercaseBucket": false`` with options ``true`` and ``false`` for above settings respectively.                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Amazon S3 Signature V2
^^^^^^^^^^^^^^^^^^^^^^

By default, Mattermost uses Signature V4 to sign API calls to AWS, but under some circumstances, V2 is required. For more information about when to use V2, see http://docs.aws.amazon.com/general/latest/gr/signature-version-2.html

**True**: Use Signature Version 2 Signing Process

**False**: Use Signature Version 4 Signing Process

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SignV2": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Email Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
Email Batching Buffer Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Specify the maximum number of notifications batched into a single email.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingBufferSize": 256`` with whole number input                      |
+--------------------------------------------------------------------------------------------------------------------------+

Email Batching Interval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Specify the maximum frequency, in seconds, which the batching job checks for new notifications. Longer batching intervals will increase performance.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingInterval": 30`` with whole number input                      |
+-----------------------------------------------------------------------------------------------------------------------+

Skip Server Certificate Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Do not validate SMTP servers when connecting to them.

**False**: Validate SMTP servers when connecting to them.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SkipServerCertificateVerification": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

GitLab Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Standard setting for OAuth to determine the scope of information shared with OAuth client. Not currently supported by GitLab OAuth.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": ""`` with string input.                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Google Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``profile email``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "profile email"`` with string input.                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Office 365 Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
Scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``User.Read``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "User.Read"`` with string input                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

________

Metrics Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
Block Profile Rate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Value that controls the `fraction of goroutine blocking events reported in the blocking profile <https://golang.org/pkg/runtime/#SetBlockProfileRate>`_.

The profiler aims to sample an average of one blocking event per rate nanoseconds spent blocked.

To include every blocking event in the profile, set the rate to 1. To turn off profiling entirely, set the rate to 0.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BlockProfileRate": "0"`` with decimal and whole number input between 0 and 1.                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Analytics Settings
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E10 and higher*

Maximum Users for Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sets the maximum number of users on the server before statistics for total posts, total hashtag posts, total file posts, posts per day, and active users with posts per day are disabled.

This setting is used to maximize performance for large Enterprise deployments.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersForStatistics": 2500`` with whole number input                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Elasticsearch Settings (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Post Index Replicas
^^^^^^^^^^^^^^^^^^^^^
The number of replicas to use for each post index. If this setting is changed, it only applies to newly created indexes. To apply the change to existing indexes, purge and rebuild the index after changing this setting.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PostIndexReplicas": 2`` with whole number input      |
+---------------------------------------------------------------------------------------------------+

Post Index Shards
^^^^^^^^^^^^^^^^^^^^^
The number of shards to use for each post index. If this setting is changed, it only applies to newly created indexes. To apply the change to existing indexes, purge and rebuild the index after changing this setting.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PostIndexShards": 1`` with whole number input      |
+-------------------------------------------------------------------------------------------------+

Aggregate Search Indexes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Elasticsearch indexes over the age specified by this setting will be aggregated during the daily scheduled job.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AggregatePostsAfterDays": 365`` with whole number input      |
+-----------------------------------------------------------------------------------------------------------+

Post Aggregator Start Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The start time of the daily scheduled aggregator job.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PostsAggregatorJobStartTime": 03:00`` with 24-hour time stamp input in the form HH:MM      |
+-----------------------------------------------------------------------------------------------------------------------------------------+

Client Requirement Settings (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Latest Android Version
^^^^^^^^^^^^^^^^^^^^^^^^^
The latest version of the Android React Native app that is recommended for use.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidLatestVersion": ""`` with whole number and decimal input. For example, `1.2.0`        |
+-----------------------------------------------------------------------------------------------------------------------------------------+

Minimum Android Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The minimum version of the Android React Native app that is required to be used.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidMinVersion": ""`` with whole number and decimal input. For example, `1.2.0`        |
+----------------------------------------------------------------------------------------------------------------------------------------+

Latest Desktop Version
^^^^^^^^^^^^^^^^^^^^^^^^^^
The latest version of the desktop app that is recommended for use.

+-------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DesktopLatestVersion": ""`` with whole number and decimal input. For example, `1.2.0`        |
+-------------------------------------------------------------------------------------------------------------------------------------------+

Minimum Destop Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The minimum version of the desktop app that is required to be used.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DesktopMinVersion": ""`` with whole number and decimal input. For example, `1.2.0`        |
+----------------------------------------------------------------------------------------------------------------------------------------+

Latest iOS Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The latest version of the iOS app that is recommended for use.

+---------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosLatestVersion": ""`` with whole number and decimal input. For example, `1.2.0`        |
+---------------------------------------------------------------------------------------------------------------------------------------+

Minimum iOS Version
^^^^^^^^^^^^^^^^^^^^^
The minimum version of the iOS React Native app that is required to be used.

+------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosMinVersion": ""`` with whole number and decimal input. For example, `1.2.0`        |
+------------------------------------------------------------------------------------------------------------------------------------+

Theme Settings  (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable Theme Selection
^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

**True:** Enables the **Display** > **Theme** tab in Account Settings so users can select their theme.

**False:** Users cannot select a different theme. The **Display** > **Theme** tab is hidden in Account Settings.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableThemeSelection": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Default Theme
^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

Set a default theme that applies to all new users on the system.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultTheme": "default"`` with options ``default``, ``organization``, ``mattermostDark`` and ``windows10``. |
+-----------------------------------------------------------------------------------------------------------------+

Allow Custom Themes
^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

**True:** Enables the **Display** > **Theme** > **Custom Theme** section in Account Settings.

**False:** Users cannot use a custom theme. The **Display** > **Theme** > **Custom Theme** section is hidden in Account Settings.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCustomThemes": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Allowed Themes
^^^^^^^^^^^^^^^^^^^^^^^^^
*Available in Enterprise Edition E10 and higher*

Select the themes that can be chosen by users when ``"EnableThemeSelection"`` is set to ``true``.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowedThemes": "default"`` with options ``default``, ``organization``, ``mattermostDark`` and ``windows10`` optionally separated by commas. For example, ``["mattermostDark", "windows10"]`` |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
