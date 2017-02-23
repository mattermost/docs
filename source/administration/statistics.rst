Statistics
================

Statistics on users, posts and channels are tracked for each system and team. Enterprise Editions have access to advanced system statistics.

To maximize performance for large Enterprise deployments, statistics for total posts, total hashtag posts, total file posts, posts per day, and active users with posts per day are disabled. You can re-enable them by changing the ``MaxUsersForStatistics`` value `in config.json <https://docs.mattermost.com/administration/config-settings.html#max-users-for-statistics>`_.

For advanced metrics for Enterprise deployments, `see performance monitoring documentation to learn more <http://docs.mattermost.com/deployment/metrics.html>`_.

Site Statistics
-----------------

System statistics are viewable under **System Console > Reporting > Site Statistics**. The data shown here is a cumulative sum across all teams on the system.

Total Users
    The total number of active accounts created on your system. Excludes inactive accounts.

Total Teams
    The total number of teams created on your system.

Total Channels
    The total number of public channels and private groups created in all the teams on your system, including deleted channels. Doesn't include direct message channels.

Total Posts
    The total number of posts made in all the teams on your system, including deleted posts and posts made using automation.

Daily Active Users
  The number of users who viewed the Mattermost site in the last 24 hours.

Monthly Active Users
  The number of users who viewed the Mattermost site in the last 30 days.

Total Posts (graph)
    The total number of posts made on a certain day in all the teams on your system, including deleted posts and posts made using automation.

Active Users With Posts (graph)
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
    The number of active connections currently on one or more of `your read replica databases <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`_.

Channel Types
    This chart displays the number of public channels and private groups in a visual format, including channels that may have been deleted.

Posts, Files and Hashtags
    This chart displays the number of posts containing files, hashtags or only text. Posts containing both files and hashtags are counted in both categories, and deleted posts are included.

Team Statistics
---------------

Team Statistics are viewable under **System Console > Teams > Statistics**.

Total Users
    The total number of active accounts who are members of this team. Excludes inactive accounts.

Public Channels
    The number of public channels created in this team. Doesn't include deleted channels.

Private Groups
    The number of private groups created in this team. Doesn't include deleted groups.

Total Posts
    The total number of posts made in this team, including deleted posts and posts made using automation.

Total Posts (graph)
    The total number of posts made on a certain day in this team, including deleted posts and posts made using automation.

Active Users With Posts (graph)
    Users who made a post on a certain day in this team, including system messages posted from the user's account.

Recent Active Users
    Twenty most recent users that have logged in and had recent browser activity in Mattermost.

Newly Created Users
    Most recent users that have joined the team.
