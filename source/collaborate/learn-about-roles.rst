Learn about Mattermost roles
============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

There are 6 types of user roles with different permission levels in Mattermost: `system admin <#system-admin>`__, `team admin <#team-admin>`__, `channel admin <#channel-admin>`__, `member <#member>`__, `guest <#guest>`__, and `deactivated <#deactivated>`__. 

.. tip::
  
  To view a list of users on the team and what their roles are, you need to be A Team Admin using Mattermost in a web browser or the desktop app. Open the Team menu and select **Manage Members**.

System admin
------------

The first user added to a newly-installed Mattermost system is assigned the system admin role. The system admin is typically a member of the IT staff and has all the privileges of a Team Admin, along with the following additional privileges:

- Access to the System Console in any team site.
- Ability to change any setting on the Mattermost server available in the System Console.
- Ability to promote and demote other users from Member role to system admin role (and vice versa).
- Ability to promote and demote other users to and from Guest role.
- Ability to deactivate user accounts and to reactivate them.
- Access to private channels, but only if given the link to the private channel.

A system admin can view and manage users in **System Console > User Management > Users**. They can search users by name, filter users by teams, and filter to view other system admins, guests, as well as active and inactive users. Only a system admin can make changes to another system admin user account in Mattermost.

Grant personal access tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System admin also can enable `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`__ for user accounts. This gives specific users permissions to create personal access tokens via **System Console > Users**.

In addition, a system admin can optionally set the following permissions for the account, which are useful for integrations and bot accounts:

- **post:all**: Allows the account to post to all Mattermost channels including direct messages.
- **post:channels**: Allows the account to post to all Mattermost public channels.

Team admin
----------

When a team is first created, the person who set it up is made a Team Admin. It is a team-specific role, meaning that someone can be a Team Admin for one team but only a member on another team. Team Admins have the following privileges:

- Access to the **Team Settings** menu.
- Ability to change the team name and import data from Slack export files.
- Access to the **Manage Members** menu, where they can control whether team members are a **Member** or a **Team Admin**.

Channel admin
-------------

*Available in legacy Mattermost Enterprise Edition E10 or E20*

The person who creates a channel is assigned the Channel Admin role for that channel. People with the Channel Admin role have the following privileges:

- Ability to assign the Channel Admin role to other members of the channel.
- Ability to remove the Channel Admin role from other holders of the Channel Admin role.
- Ability to remove members from the channel.
- Ability to configure channel actions that automate tasks based on trigger conditions, such as `joining a channel </collaborate/join-leave-channels.html#join-a-channel>`__ or `sending a message </collaborate/send-messages.html>`__ in a channel.

Depending on your system configuration, channel admins can be granted special permissions by the system admin to rename and delete channels.

Member
------

This is the default role given to users when they join a team. Members have basic permissions on a Mattermost team.

Guest
-----

A guest is a role with restricted permissions. Guests enable organizations to collaborate with users outside of their organization, and control what channels they are in and who they can collaborate with.

.. include:: /onboard/guest-account-access.rst
  :start-after: :nosearch:

See the `guest accounts </onboard/guest-accounts.html>`__ documentation for details on working with guest accounts.

Deactivated
-----------

A system admin can deactivate user accounts via **System Console > Users**. A list of all users on the server can be searched and filtered to make finding users easier. Select the user's role and in the menu that opens, then select **Deactivate**.

When **Deactivate** is selected, the user is logged out of the system, and receives an error message if they try to log back in. The user no longer appears in channel member lists, and they are removed from the team members list. A deactivated account can also be reactivated from the System Console, in which case the user rejoins channels and teams that they previously belonged to.

Direct Message channels with deactivated users are hidden in users' sidebars, but can be reopened using the **More...** button or by pressing  :kbd:`Ctrl` :kbd:`K` on Windows or Linux, or :kbd:`⌘` :kbd:`K` on Mac.

Mattermost is designed as a system-of-record, so there isn't an option to delete users from the Mattermost system, as such an operation could compromise the integrity of message archives.

.. note::

    AD/LDAP user accounts can't be deactivated from Mattermost; they must be deactivated from your Active Directory.


User ID
-------
Users can be specified in Mattermost by username or user ID. Usernames automatically resolve when a match is detected.
Below are three ways a User's ID can be determined.

Determining a User ID through the System Console (Admin)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Log in to your Mattermost instance as an administrator.
Go to the System Console by clicking on the gear icon in the top left corner and selecting "System Console."
In the System Console, navigate to "Users" or a similar section where user management settings are available.
You should see a list of users, and their IDs should be displayed alongside their usernames.
Find the user whose ID you want to determine and note it down.

Determining a User ID Using the API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, it is possible to find a user's ID using the Mattermost API. You can use this method if you need to automate user-related tasks or integrate with external systems.
Make an HTTP GET request to the following endpoint: https://your-mattermost-url/api/v4/users/username/username_here.
Replace your-mattermost-url with the URL of your Mattermost instance and username_here with the actual username of the user you are looking for.
The API response will contain a JSON object that includes the user's ID among other details.

Determining a User ID Using mmctl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer command-line tools, Mattermost offers mmctl for system administration.
Open your terminal or command prompt.
Use the following command to list all users and their IDs: mmctl user list.
You will receive a list of users with their IDs, making it easy to identify the user you're interested in.