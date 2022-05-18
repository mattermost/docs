About user roles
================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

There are six types of user roles with different permission levels in Mattermost: System Admins, Team Admins, Channel Admins, Members, Guests, and Inactive accounts. To view a list of users on the team and what their roles are, Team Admins can open the Team menu and select **Manage Members**.

System Admin
------------

The first user added to a newly-installed Mattermost system is assigned the System Admin role.

The System Admin is typically a member of the IT staff and has all the privileges of a Team Admin, along with the following additional privileges:

- Access to the System Console in any team site.
- Ability to change any setting on the Mattermost server available in the System Console.
- Ability to promote and demote other users from Member role to System Admin role (and vice versa).
- Ability to promote and demote other users to and from Guest role.
- Ability to deactivate user accounts and to reactivate them.
- Access to private channels, but only if given the link to the private channel.

A System Admin can view and manage users in **System Console > User Management > Users**. They can search users by name, filter users by teams, and filter to view other System Admins, guests, as well as active and inactive users.

Team Admin
----------

When a team is first created, the person who set it up is made a Team Admin. It is a team-specific role, meaning that someone can be a Team Admin for one team but only a member on another team. Team Admins have the following privileges:

- Access to the **Team Settings** menu.
- Ability to change the team name and import data from Slack export files.
- Access to the **Manage Members** menu, where they can control whether team members are a **Member** or a **Team Admin**.

Channel Admin
-------------

*Available in legacy Mattermost Enterprise Edition E10 or E20*

The person who creates a channel is assigned the Channel Admin role for that channel. People with the Channel Admin role have the following privileges:

- Ability to assign the Channel Admin role to other members of the channel.
- Ability to remove the Channel Admin role from other holders of the Channel Admin role.
- Ability to remove members from the channel.
- Ability to configure channel actions that automate tasks based on trigger conditions, such as `joining a channel <https://docs.mattermost.com/channels/join-leave-channels.html#join-a-channel>`__ or `sending a message <https://docs.mattermost.com/channels/send-messages.html>`__ in a channel.

Depending on your system configuration, Channel Admins can be granted special permissions by the System Admin to rename and delete channels.

Member
------

This is the default role given to users when they join a team. Members have basic permissions on the Mattermost team.

Guest
-----

Guest is a role with restricted permissions, which allow organizations to collaborate with users outside of their organization, and control what channels they are in and who they can collaborate with.

Guests can: 

- Pin messages to channels.
- Use slash commands (with the exception of those used to invite members).
- Favorite channels.
- Mute channels.
- Update their profile.

Guests cannot:

- Discover public channels.
- Join open teams.
- Create direct messages or group messages with members who aren’t within the same channel.

User with personal access token permission
------------------------------------------

A System Admin can enable `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`__ and give permissions for that account to create personal access tokens in **System Console > Users**.

In addition, the System Admin can optionally set the following permissions for the account, useful for integrations and bot accounts:

- **post:all**: Allows the account to post to all Mattermost channels including direct messages.
- **post:channels**: Allows the account to post to all Mattermost public channels.

Deactivate users
----------------

A System Admin can deactivate user accounts via **System Console > Users** for a list of all users on the server. The list can be searched and filtered to make finding users easier. Select the user's role and in the menu that opens, then select **Deactivate**.

When **Deactivate** is selected, the user is logged out of the system, and receives an error message if they try to log back in. The user no longer appears in channel member lists, and they are removed from the team members list. A deactivated account can also be reactivated from the System Console, in which case the user rejoins channels and teams that they previously belonged to.

Direct Message channels with deactivated users are hidden in users' sidebars, but can be reopened using the **More...** button or by pressing CMD/CTRL+K.

Mattermost is designed as a system-of-record, so there isn't an option to delete users from the Mattermost system, as such an operation could compromise the integrity of message archives.

.. note::

    AD/LDAP user accounts can't be deactivated from Mattermost; they must be deactivated from your Active Directory.