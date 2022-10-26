About teams
===========

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

A team is a digital workspace where you and your teammates can collaborate in Mattermost. Depending on how Mattermost is set up in your organization, you can belong to one team or multiple teams. 

Only users with the **Create Teams** permission can `create new teams <#create-a-team>`__ and `manage team settings </welcome/team-settings.html>`__ for existing teams.

Single team versus multiple teams
----------------------------------

Mattermost can be deployed both to a single team and to multiple teams. Currently, we recommend deploying to a single team for the following reasons:

- Single team deployments promote communication across the organization. When you add multiple teams, groups can become isolated.
- We don't yet support search or channels across teams, which can impact the cross-team user experience. This includes general searches, saved posts, and recent mentions.
- Integrations (e.g., webhooks and slash commands) are only persistent across single team deployments.

However, some Mattermost customers prefer multiple team deployments for the following reasons:

- Teams are useful when there is a purpose for each of them. For example, one team is used for staff members and another team for external users.
- Performance is better when users are scattered across multiple teams instead of all in the same one. With multiple teams, there is less content to load per team or channel switch and database queries are faster.
- Creating a shared team for all users, and using advanced permissions to control who can create channels and add members to the shared team, improves cross-team collaboration when using multiple teams. Additionally, an annoucement banner can be used to provide system-wide announcements.

Team sidebar
------------

If you belong to more than one team, a team sidebar displays to the left of the channel sidebar. Drag teams to reorder them in the sidebar. You can also use keyboard shortcuts to navigate between teams.

.. image:: ../images/teams.gif
   :alt: Navigating between teams in Mattermost.

Create a team
--------------

If team creation is enabled by the System Admin, teams can be created from the team sidebar or the channel sidebar. The person who creates a team is automatically  assigned the Team Admin role for that team.

If you have appropriate permissions, select the **Plus** icon at the top of the team sidebar, then select **Create a New Team** on the team selection page, which guides you through the rest of the team creation steps. If this option is not visible on the web page, then the System Admin has disabled team creation.

If you have no other teams to join, selecting the **Plus** icon takes you directly to the team creation page if team creation is enabled.

.. tip::

  From your current Mattermost team, you can also select your team name, then select **Create a Team**. If this option is not visible in the menu, then the System Admin has disabled team creation.

Team name and URL selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few details and restrictions to consider when selecting a team name and team URL.

Team name
^^^^^^^^^

This is the display name of your team that appears in menus and headings.

- Team names can contain any letters, numbers, or symbols.
- Team names are case sensitive.
- Team names must be 2 - 64 characters in length.

Team URL
^^^^^^^^

The team URL is part of the web address that navigates to your team on the system domain, ``https://domain.com/teamurl/``.

- Teams may contain only lowercase letters, numbers, and dashes.
- Teams must start with a letter and cannot end in a dash.
- Teams must be 2 - 64 characters in length.
- Team names cannot start with the following restricted words: admin, api, channel, claim, error, files, help, landing, login, mfa, oauth, plug, plugins, post, signup, playbooks, or boards.

Join a team
-----------

You can join any team configured to `"allow any user with an account on this server to join this team" </welcome/team-settings.html#allow-anyone-to-join-this-team>`__, or when you receive an invitation to join.

If you haven't yet joined any teams in Mattermost, you're prompted to join available teams when you `log in </welcome/log-in.html>`__.

You can be a member of multiple teams at the same time. To join additional teams, select the current team name, choose **Join Another Team**, and select the name of the team you want to join.

.. image:: ../images/join-team.png
  :alt: Select a team name to join another team.

Invite people to teams
----------------------

If you have the required permissions, you can add people, including members of your organization as well as guests, to your team via a direct invite, a public team invite link, or if they already have an account on the server, you can add them to the team yourself.

A guest is a special role that is restricted to only the channels they have been invited to. When guest access is enabled, you can invite guests or users external to the organization, such as vendors or customers.

Send a direct invite
~~~~~~~~~~~~~~~~~~~~~

Direct invites are invitation emails sent from your team's server directly to the invited person's email address. A link within the invitation directs them to an account creation page. Invitation links sent by email expire after 48 hours and can only be used once. 

.. note::
  A System Admin can invalidate all active invitation links via **System Console > Authentication > Signup > Invalidate pending email invites**.

1. Select the Team menu at the top of the Navigation Panel.
2. Select **Invite People**.
3. If there's an option to invite members and guests, choose **Invite Members**.
4. In the **Invite People** field, enter the email address of the person you want to add. You can add multiple email addresses at a time.
5. When sending a direct invite to a guest, you must specify the channels the guest can access, and your invitation can include an optional custom message.
6. Select **Invite Members** or **Invite Guests**.

.. note::

  - If you aren't able to see the **Invite Guests** option, confirm with your System Admin that you have the correct permissions.
  - If you don't see the **Send Email Invite** option, confirm with your System Admin that **System Console > Authentication > Signup > Enable Email Invitations** is set to **true**.

Send a team invite link
~~~~~~~~~~~~~~~~~~~~~~~

The team invite link is a unique URL that directs people to an account creation page for a team. A team invite link can be used by anyone and does not change unless it is re-generated by a System Admin or Team Admin via **Team Settings > General > Invite Code**. For example, the team invite link can be included in a company-wide email to invite all employees to join a Mattermost team.

1. Select the Team menu at the top of the Navigation Panel.
2. Select **Invite People**.
3. If there's an option to invite members and guests, choose **Invite Members**.
4. Select the **Copy Link** button to save the URL to your clipboard and share it with those you want to invite to the team.

Adding someone to your team
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If someone you want to add to your team already has an account on the server, you can add them to your team without sending an invitation.

1. Select the Team menu at the top of the Navigation Panel.
2. Select **Invite People**.
3. Choose **Invite Members** or **Invite Guests**.
4. Search for the person you want to add. If the people you want to add are not on the list, then they do not have an account on your server.
5. When adding a guest, you must specify the channels the guest can access.
6. Select **Invite Members** or **Invite Guests**.

.. note:: 
   
   - If you aren't able to see the **Invite Guests** option, confirm with your System Admin that you have the correct permissions.
   - System Admins can view and add team membership to individual users on the user profile page (via **System Console > Users > User Profile**) by selecting **Add Team**.

Remove people from teams
------------------------

A Team Admin can remove a user from a team via **Team menu > Manage Members > Remove From Team** in the dropdown menu beside a user entry.

When a user is removed from a team, the team will no longer show up in their team sidebar. If they currently have the team open, they are redirected to the first team that appears on their team sidebar. If they didn't belong to any other teams, the user is sent to the team selection page.

Removing a user from the team does not deactivate the account. The user will still be able to log in to the site, and join other teams. They will also be able to rejoin the team they were removed from if they receive another invite, or if the team is set to `"Allow any user with an account on this server to join this team" </welcome/team-settings.html#allow-anyone-to-join-this-team>`__. If the user does rejoin the team, they will no longer belong to the channels they were previously a part of, and they will lose all Admin privileges if they had them previously.

A System Admin can also remove users from teams via **System Console > Users**, and selecting the dropdown beside a user entry and selecting **Manage Teams**. The list of teams an individual user belongs to can be viewed on the user's profile page via **System Console > Users** and selecting the member's name from the list provided in the **User Configuration** screen.

Leave a team
------------

Users can also choose to remove themselves from a team, from **Team menu > Leave Team**. This will remove the user from the team, and from all public channels and private channels on the team.

They will only be able to rejoin the team if it is set to `"Allow any user with an account on this server to join this team" </welcome/team-settings.html#allow-anyone-to-join-this-team>`__ team, or if they receive a new invite. If they do rejoin, they will no longer be a part of their old channels.