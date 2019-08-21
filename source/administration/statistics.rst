Statistics
================

Statistics on users, posts and channels are tracked for each system and team. Enterprise Editions have access to advanced system statistics.

.. note::

  To maximize performance for large Enterprise deployments, statistics for total posts, total hashtag posts, total file posts, posts per day, and active users with posts per day are disabled. You can re-enable them by changing the ``MaxUsersForStatistics`` value `in config.json <https://docs.mattermost.com/administration/config-settings.html#maximum-users-for-statistics>`__.

For advanced metrics for Enterprise deployments, `see performance monitoring documentation to learn more <http://docs.mattermost.com/deployment/metrics.html>`__.

Site Statistics
-----------------

System statistics are viewable under **System Console > Site Statistics** in prior versions or **System Console > Reporting** in versions after 5.12. The data shown here is a cumulative sum across all teams on the system.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enterprise Edition includes additional system statistics.

Total Sessions
    The number of active user sessions connected to your system. Expired sessions are not counted.

Total Commands
    The number of active slash commands currently setup on your system. Slash commands that are created and then removed in the Integrations menu are not counted.

Incoming Webhooks
    The number of active Incoming Webhooks currently setup on your system. Incoming webhooks that are created and then removed in the Integrations menu are not counted.

Outgoing Webhooks
    The number of active Outgoing Webhooks currently setup on your system. Outgoing webhooks that are created and then removed in the Integrations menu are not counted.

WebSocket Conns
    The number of active WebSocket connections currently on your server.

Master DB Conns
    The number of active connections currently on your master database.

Replica DB Conns
    The number of active connections currently on one or more of `your read replica databases <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`__.

Channel Types
    This chart displays the number of public channels and private channels in a visual format, including channels that might have been deleted.

Posts, Files and Hashtags
    This chart displays the number of posts containing files, hashtags or only text. Posts containing both files and hashtags are counted in both categories, and deleted posts are included.

Team Statistics
---------------

Team Statistics are viewable under **System Console > Team Statistics**. The data shown here is a cumulative sum across this team only, and excludes posts made in direct message channels, which are not tied to a team.

Total Users
    The total number of active accounts on this team. Excludes deactivated accounts.

Public Channels
    The number of public channels created in this team. Excludes deleted channels.

Private Channels
    The number of private channels created in this team. Excludes deleted channels.

Total Posts
    The total number of posts made in this team, including deleted posts and posts made using automation. Excludes posts made in direct message channels, which are not tied to a team.

Total Posts (graph)
    The total number of posts made on a certain day in this team, including deleted posts and posts made using automation.

Active Users with Posts (graph)
    Users who made a post on a certain day in this team, including system messages posted from the user's account.

Recent Active Users
    Twenty most recent users who have logged in and had recent browser activity in Mattermost.

Newly Created Users
    Most recent users who have joined the team.

Troubleshooting
-----------------

If the statistics page is loading endlessly and you get an error message saying "Not enough data for a meaningful representation", check whether you are using an ad blocker. An ad blocker can prevent this page from loading data. To test this, temporarily disable your ad blocker, or view the page in a browser without an ad blocker installed.
