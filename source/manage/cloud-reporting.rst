Statistics
==========

Statistics on users, posts, and channels are tracked for each system and team. 

Site Statistics
---------------

|all-plans| |cloud|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

System statistics are viewable under **System Console > Reporting > Site Statistics**. The data shown here is a cumulative sum across all teams on the system.

Total Users
    The total number of active accounts created on your system. Excludes deactivated accounts.

Total Teams
    The total number of teams created on your system.

Total Channels
    The total number of public channels and private channels created in all the teams on your system, including deleted channels. Doesn't include direct message channels.

Total Posts
    The total number of posts made in all the teams on your system, including deleted posts and posts made using automation.

Daily Active Users
  The total number of users who viewed the Mattermost site in the last 24 hours. Excludes bot users.

Monthly Active Users
  The total number of users who viewed the Mattermost site in the last 30 days. Excludes bot users.

Total Posts (graph)
    The total number of posts made on a certain day in all the teams on your system, including deleted posts and posts made using automation.

Total Posts from Bots (graph)
    The total number of posts made by a `bot account <https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/>`_ on a certain day in all the teams on your system, including deleted posts and posts made using automation.

Active Users with Posts (graph)
    Users who made a post on a certain day in all the teams on your system, including system messages posted from the user's account.

Team Statistics
---------------

|all-plans| |cloud|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

Team Statistics are viewable under **System Console > Reporting > Team Statistics**. The data shown here is a cumulative sum across this team only, and excludes posts made in direct message channels, which are not tied to a team.

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

Troubleshooting/FAQ
-------------------

I see an error: "Not enough data for a meaningful representation"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the statistics page is loading endlessly and you get an error message saying "Not enough data for a meaningful representation", check whether you're using an ad blocker. An ad blocker can prevent this page from loading data. To test this, temporarily disable your ad blocker, or view the page in a browser without an ad blocker installed.

Can Team Admins review their own team's statistics?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Admins can designate the **Viewer** `System Admin Role <https://docs.mattermost.com/onboard/system-admin-roles.html>`__ to enable Team Admin to see team statistics.

Once Team Admins are assigned to the **Viewer** role, they can access all statistics for all teams.

System Admins must then `edit the privileges <https://docs.mattermost.com/onboard/system-admin-roles.html#editing-privileges-of-admin-roles-advanced>`__ of the **Viewer** role. Only the **Reporting** privileges need to be enabled to allow Team Admins to see statistics for their teams.

Once the **Viewer** role is set up for reporting access only, System Admins can then `assign <https://docs.mattermost.com/onboard/system-admin-roles.html#assigning-admin-roles>`__ the **Viewer** role to Team Admins.

.. note::
  - System Admins must manually add or remove members from the **Viewer** role to address Team Admin changes, such as promotions or demotions.
  - Team Admins using the **Viewer** role will also have access to system level statistics in addition to statistics for their teams.
