.. _ldap-group-constrained-team-channel:

Using AD/LDAP Synchronized Groups to Manage Team or Private Channel Membership
===============================================================
Mattermost groups created with `synchronized AD/LDAP groups <https://docs.mattermost.com/deployment/ldap-group-sync.html>`_ can be used to manage the membership of private teams and private channels. When a team or private channel is managed by synchronized groups, users will be added and removed based on their membership to the synchronized AD/LDAP group. 

For instance, you may have a AD/LDAP group that contains your development team that you want to synchronize to a developer team.  By using this feature, new developers will get added to the team when they are added to the synchronized AD/LDAP group and they will be removed from the team when removed from the AD/LDAP group. 

Similarily, you may have a AD/LDAP group that contains your leadership team that you want to synchronize to a private channel for coordination and updates.  This feature will help control the membership of the channel so that users outside of the synchronized group are prevented from being added the channel mistakenly. 

On teams that are managed by synchronized groups, users outside of the group are restricted from:

 - invitation through a team invite link 
 - Invations through email invite 
 
Similarily on private channels that are managed by synchronized groups, users outside of the group are restricted from:  
 - invitation through a mention
 - invitation through the /invite slash command 
 - directly added to the channel with “add members”

Users, however, can remove themselves from teams and private channels managed by synchronized groups.  

Managing Membership of a Team or Channel with Synchronized Groups
----------

To manage membership of a private team with synchronized groups: 

1. Ensure there is at least one group already associated to the team. You can view and add default teams to a group via **System Console > User Management > Groups > Group Configuration**. Please see more information on adding default teams and channels `here <https://docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group>`_. Additionally, you can use the CLI tool to view if there is already a group associated to the team by running the `group team list CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-list>`_. 
2. Ensure **Team Settings > General > Allow any user with an account on this server to join this team** is set to ``No``. 
3. Convert the team to have its membership managed by synchronized groups by running the `group team enable CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-enable>`_ .

To manage membership of a private channel with synchronized groups: 

1. Ensure there is at least one group already associated to the channel. You can view and add default channels to a group via **System Console > User Management > Groups > Group Configuration**. Please see more information on adding default teams and channels `here <https://docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group>`_. Additionally, you can use the CLI tool to view if there is already a group associated to the channel by running the `group channel list CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-list>`_. 
2.Convert the team to have its membership managed by synchronized groups by running the `group channel enable CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-group-channel-enable>`_ .  

.. note:: 
   System console support to set teams and private channels to managing membership with group synchronization is planned in the 5.14 (August 2019) release. 

Add or Remove Groups from Teams
----------

Once the management of the team is converted to be managed by synchronized groups, a team admin can add additional groups from **Main Menu > Add Groups to Team**.  This will add users on the next AD/LDAP synchronization and any new users to the group will be added to the team on subsequent synchronizations. 

Team administrators can also remove groups from a team from **Main Menu > Manage Groups**. This will disassociate the group from the team. Users are removed on the next AD/LDAP synchronization.

Add or Remove Groups from Private Channels
----------

Once the management of the channel is converted to be managed by synchronized groups, a team admin can add additional groups from **Channel Menu > Add Groups to Channel**.  This will add users on the next AD/LDAP synchronization and any new users to the group will be added to the channel on subsequent synchronizations. 

Team administrators can also remove groups from a team from **Main Menu > Manage Groups**. This will disassociate the group from the team. Users are removed on the next AD/LDAP synchronization. 


Managing Members
----------
Users are automatically removed from the team or private channel when removed from a synchronized AD/LDAP group that is managing the membership of that team or channel.  Additionally, users who are not in the synchronized groups are prevented from being added through the ``/invite`` and mention flows within a channel.  

A user can remove themselves from the team or from the private channel when it is managed by synchronized groups.  They can be added back by users who have permission to manage members for a team or private channel by using the ``/invite`` slash command or by mentioning the user in a channel.  

Disabling Group Synchronized Management of Teams and Private Channels
----------
To remove the management of members by synchronized groups in a team, run the `group team disable CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-group-team-disable>`_.

To remove the management of members by synchronized groups in a team, run the `group channel disable CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-group-channel-disable>`_.


FAQs
----------
**Why aren’t public channels supported with this feature?**

Public channels are available to all members to discover and join. Managing membership with synchronized Groups removes the ability for public channels to be accessible to users on the team. Private channels typically require a more controlled membership management, which is why this feature applies to private channels. Groups can be assigned to public teams and public channels as described in `this documentation<https://docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group>`_. 

**Does a team with its membership managed by groups have any effect on public channel access?**

Only users that are members of groups synchronized to team are able to discover and join public channels.  Private channels can also be managed by synchronized groups when a team is managed by synchronized groups. 
