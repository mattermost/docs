Statistics
==========

Statistics on users, posts, and channels are tracked for each system and team. Enterprise Editions have access to advanced system statistics.

.. note::

  To maximize performance for large Enterprise deployments, statistics for total posts, total hashtag posts, total file posts, posts per day, and active users with posts per day are disabled. You can re-enable them by changing the ``MaxUsersForStatistics`` value `in config.json <https://docs.mattermost.com/administration/config-settings.html#maximum-users-for-statistics>`__.

For advanced metrics for Enterprise deployments, `see performance monitoring documentation to learn more <https://docs.mattermost.com/deployment/metrics.html>`__.

Site Statistics
---------------

System statistics are viewable under **System Console > Reporting**. The data shown here is a cumulative sum across all teams on the system.

Total Users
    The total number of active accounts created on your system. Excludes deactivated accounts.

Total Teams
    The total number of teams created on your system.

Total Channels
    The total number of public channels and private channels created in all the teams on your system, including deleted channels. Doesn't include direct message channels.

Total Posts
    The total number of posts made in all the teams on your system, including deleted posts and posts made using automation.

Daily Active Users
  The total number of users who viewed the Mattermost site in the last 24 hours. Excludes bot users as of v5.14.

Monthly Active Users
  The total number of users who viewed the Mattermost site in the last 30 days. Excludes bot users as of v5.14.

Total Posts (graph)
    The total number of posts made on a certain day in all the teams on your system, including deleted posts and posts made using automation.

Total Posts from Bots (graph)
    The total number of posts made by a `bot account <https://docs.mattermost.com/developer/bot-accounts.html>`_ on a certain day in all the teams on your system, including deleted posts and posts made using automation.

Active Users with Posts (graph)
    Users who made a post on a certain day in all the teams on your system, including system messages posted from the user's account.

Advanced system statistics (Enterprise)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enterprise Edition includes additional system statistics.

Total Sessions
    The number of active user sessions connected to your system. Expired sessions are not counted.

Total Commands
    The number of active slash commands currently set up on your system. Slash commands that are created and then removed in the **Integrations** menu are not counted.

Incoming Webhooks
    The number of active incoming webhooks currently setup on your system. Incoming webhooks that are created and then removed in the **Integrations** menu are not counted.

Outgoing Webhooks
    The number of active outgoing webhooks currently set up on your system. Outgoing webhooks that are created and then removed in the **Integrations** menu are not counted.

WebSocket Conns
    The number of active WebSocket connections currently on your server.

Master DB Conns
    The number of active connections currently on your master database.

Replica DB Conns
    The number of active connections currently on one or more of `your read replica databases <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`__.

Channel Types
    This chart displays the number of public channels and private channels in a visual format, including channels that might have been deleted.

Posts, Files and Hashtags
    This chart displays the number of posts containing files, hashtags, or only text. Posts containing both files and hashtags are counted in both categories, and deleted posts are included.

Team Statistics
---------------

Team Statistics are viewable under **System Console > Team Statistics**. The data shown here is a cumulative sum across this team only, and excludes posts made in Direct Message channels, which are not tied to a team.

Total Users
    The total number of active accounts on this team. Excludes deactivated accounts.

Public Channels
    The number of public channels created in this team. Excludes deleted channels.

Private Channels
    The number of private channels created in this team. Excludes deleted channels.

Total Posts
    The total number of posts made in this team, including deleted posts and posts made using automation. Excludes posts made in Direct Message channels, which are not tied to a team.

Total Posts (graph)
    The total number of posts made on a certain day in this team, including deleted posts and posts made using automation.

Active Users with Posts (graph)
    Users who made a post on a certain day in this team, including system messages posted from the user's account.

Recent Active Users
    Twenty most recent users who have logged in and had recent browser activity in Mattermost.

Newly Created Users
    Most recent users who have joined the team.

Troubleshooting/FAQ
-------------------

I see an error: "Not enough data for a meaningful representation"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the statistics page is loading endlessly and you get an error message saying "Not enough data for a meaningful representation", check whether you're using an ad blocker. An ad blocker can prevent this page from loading data. To test this, temporarily disable your ad blocker, or view the page in a browser without an ad blocker installed.

Can Team Admins review their own team's statistics?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in Mattermost Enterprise Edition E20*

System Admins can designate the **Viewer** `System Admin Role <https://docs.mattermost.com/deployment/admin-roles.html>`__ to enable Team Admins to see team statistics.

Once Team Admins are assigned to the **Viewer** role, they can access all statistics for all teams.

System Admins must then `edit the privileges <https://docs.mattermost.com/deployment/admin-roles.html#editing-privileges-of-admin-roles-advanced>`__ of the **Viewer** role. Only the **Reporting** privileges need to be enabled to allow Team Admins to see statistics for their teams.

Once the **Viewer** role is set up for reporting access only, System Admins can then `assign <https://docs.mattermost.com/deployment/admin-roles.html#assigning-admin-roles>`__ the **Viewer** role to Team Admins.

.. note::

  - System Admins must manually add people to or remove people from the **Viewer** admin role to address Team Admin changes, such as promotions or demotions.
  - Team Admins using the **Viewer** admin role will also have access to system-level statistics in addition to statistics for their teams.
