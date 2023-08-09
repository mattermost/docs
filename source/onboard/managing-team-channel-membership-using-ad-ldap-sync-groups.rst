.. _ldap-group-constrained-team-channel:

Using AD/LDAP synchronized groups to manage team or private channel membership
------------------------------------------------------------------------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E20*

Mattermost groups created with `synchronized AD/LDAP groups </onboard/ad-ldap-groups-synchronization.html>`_ can be used to manage the membership of private teams and private channels. When a team or private channel is managed by synchronized groups, users will be added and removed based on their membership to the synchronized AD/LDAP group.

For instance, you may have an AD/LDAP group that contains your development team that you want to synchronize to a developer team.  By using this feature, new developers will get added to the team when they are added to the synchronized AD/LDAP group and they will be removed from the team when removed from the AD/LDAP group.

Similarly, you may have an AD/LDAP group that contains your leadership team that you want to synchronize to a private channel for coordination and updates. This feature will help control the membership of the channel so that users outside of the synchronized group are prevented from being added to the channel mistakenly.

On teams that are managed by synchronized groups, users outside of the group are restricted from:

 - Invitation through a team invite link
 - Invitation through an email invite

Similarly on private channels that are managed by synchronized groups, users outside of the group are restricted from:

 - Invitation through a mention
 - Invitation through the ``/invite`` slash command
 - Being added to the channel with **Add members**

Users can remove themselves from teams and private channels managed by synchronized groups.

Managing membership of a team or channel with synchronized groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To manage membership of a private team with synchronized groups:

1. Navigate to **System Console > User Management > Teams**. 
2. Select the team you want to manage with group synchronization.
3. Under **Team Management**, enable **Sync Group Members**. If **Anyone can join this team** is enabled or if specific email domains are set, they will be disabled by the sync group members feature.
4. Add one or more groups to the team. If there are groups already associated to default users into the team, they will already be present.
5. Review the notice in the footer of the screen for any users that are not part of groups who will be removed from the team on the next synchronization.
6. Select **Save**. Members will be updated on the next scheduled AD/LDAP synchronization.

Alternatively you can use the mmctl tools to set the team to be managed by groups:

1. Ensure there's at least one group already associated to the team. You can view and add default teams to a group via **System Console > User Management > Groups > Group Configuration**. See the `mmctl group team list </manage/mmctl-command-line-tool.html#mmctl-group-team-list>`__ documentation for more information on adding default teams and channels and confirming whether if there is already a group associated to the team.
2. Ensure **Team Settings > General > Allow any user with an account on this server to join this team** is set to ``No``.
3. Convert the team to have its membership managed by synchronized groups by running the `mmctl group team enable </manage/mmctl-command-line-tool.html#mmctl-group-team-enable>`__ command.

To manage membership of a private channel with synchronized groups:

1. Navigate to **System Console > User Management > Channels**. 
2. Select the channel you want to manage with group synchronization.
3. Under **Channel Management**, enable **Sync Group Members**. Please ensure the channel is set to ``private``.
4. Add one or more groups to the channel. If there are groups already associated to default users in the channel, they'll already be present.
5. Review the notice in the footer of the screen for any users that are not part of groups who will be removed from the channel on the next synchronization.
6. Select **Save**. Members will be updated on the next scheduled AD/LDAP synchronization.

Alternatively you can use the mmctl tool to set a private channel to be managed by groups:

1. Ensure there's at least one group already associated to the channel. You can view and add default channels to a group via **System Console > User Management > Groups > Group Configuration**. See our `AD/LDAP </onboard/ad-ldap-groups-synchronization.html#adding-default-teams-or-channels-for-the-group>`__ documentation for more information on adding default teams and channels. Additionally, you can use the mmctl  to view if there is already a group associated to the channel by running the `mmctl group channel list </manage/mmctl-command-line-tool.html#mmctl-group-channel-list>`__ command.
2. Convert the team to have its membership managed by synchronized groups by running the `mmctl group channel enable </manage/mmctl-command-line-tool.html#mmctl-group-channel-enable>`__ command.

Add or remove groups from teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the management of the team is converted to be managed by synchronized groups, a Team or System Admin can add additional groups from **Main Menu > Add Groups to Team**. This will add users on the next AD/LDAP synchronization and any new users to the group will be added to the team on subsequent synchronizations. Team Admins will be prevented from changing the team to public by enabling **Team Settings > Allow any user with an account on this server to join this team**.

Team or System Admins can also remove groups from a team from **Main Menu > Manage Groups**. This will disassociate the group from the team. Users are removed on the next AD/LDAP synchronization.

The System Admin can also remove groups from  **System Console > User Management > Teams > Team Configuration > Synced Groups**.

Add or remove groups from private channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the management of the channel is converted to be managed by synchronized groups, a Team or System Admin can add additional groups from **Channel Menu > Add Groups to Channel**. This will add users on the next AD/LDAP synchronization and any new users to the group will be added to the channel on subsequent synchronizations.

Team or System Admins can also remove groups from a team from **Main Menu > Manage Groups**. This will disassociate the group from the team. Users are removed on the next AD/LDAP synchronization.

The System Admin can also remove groups from  **System Console > User Management > Channels > Channel Configuration > Synced Groups**.

Managing members
^^^^^^^^^^^^^^^^

Users are automatically removed from the team or private channel when removed from a synchronized AD/LDAP group that is managing the membership of that team or channel. Additionally, users who are not in the synchronized groups are prevented from being added through the ``/invite`` and mention flows within a channel.

A user can remove themselves from the team or from the private channel when it is managed by synchronized groups. They can be added back by users who have permission to manage members for a team or private channel by using the ``/invite`` slash command or by mentioning the user in a channel.

If the user is removed from a synchronized group and later readded to the group, they can be manually added back to the team or private channel as noted above.

.. note:: 
  Users will not be automatically added back by the AD/LDAP synchronization once they remove themselves or are removed by the LDAP synchronized group.

Disabling group synchronized management of teams and private channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To remove the management of members by synchronized groups in a team, disable **Sync Group Members** under **System Console > User Management > Teams > Team Management**, or run the `mmctl group team disable </manage/mmctl-command-line-tool.html#mmctl-group-team-disable>`__ command.

To remove the management of members by synchronized groups in a channel, disable **Sync Group Members** under **System Console > User Management > Channels > Channel Management**, or run the `mmctl group channel disable </manage/mmctl-command-line-tool.html#mmctl-group-channel-disable>`__ command.

Frequently asked questions
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Why aren’t public channels supported with this feature?**

Public channels are available to all members to discover and join. Managing membership with synchronized groups removes the ability for public channels to be accessible to users on the team. Private channels typically require a more controlled membership management, which is why this feature applies to Private channels. Groups can be assigned to public teams and public channels as described in `this documentation </onboard/ad-ldap-groups-synchronization.html#adding-default-teams-or-channels-for-the-group>`_.

**Does a team with its membership managed by groups have any effect on Public channel access?**

Only users that are members of groups synchronized to team are able to discover and join public channels. Private channels can also be managed by synchronized groups when a team is managed by synchronized groups.

**Why don't users get readded to teams or channels once they have been removed from and then later re-added to the LDAP group?**

The implementation of group removals does not currently differentiate between users who have removed themselves or have been removed by the LDAP synchronization process. Our design optimizes for users who have removed themselves from a team or channel. In the future, we may add the ability for admins to re-add users who have been removed, and even prevent users from leaving a team or channel.

Additionally, LDAP users who aren't accessible to Mattermost based on filters will be removed from the groups and from group-synced teams and channels. If they were removed from teams and channels then they will not be re-added to those teams and channels upon becoming subsequently re-accessible to Mattermost.
