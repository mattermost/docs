.. _ldap-group-sync:

AD/LDAP Groups (Alpha) (E20)
===========================

This feature is current offered as an alpha release for Enterprise Edition 20 customers via a custom build. Please see `this forum post <https://TODO.com>`_ for more details. 

Overview
--------------------

Groups are a convenient way to manage default membership for users in teams and channels.  This is a useful feature for organizations that have many new users to onboard. The group feature currently supports creating groups by synchronization with your AD/LDAP system groups. AD/LDAP nested groups are also supported.

Pre-installation notes
----------------------
The group filter is configuration setting available under **System Console > AD/LDAP** and the synchronization of groups happens with the synchronization of users. The group feature has no implications to users' authentication to Mattermost. 

Getting started
---------------

Mattermost groups synced to AD/LDAP groups are configured first at **System Console > Authentication > AD/LDAP** and then on the new **Access Control > Groups** page.

AD/LDAP group synchronization
-----------------------------

To synchronize your AD/LDAP groups to Mattermost, you will need to specify the filter used to retrieve groups. Enter in the filter for your AD/LDAP group under **System Console > Authentication > AD/LDAP > Group Filter**. 
 
.. image:: ../images/Group_filter.png

During the initial synchronization, AD/LDAP groups, nested groups, and associated users will be retrieved based on the filter you entered.  Synchronization of groups will occur after user synchronization.  

On subsequent synchronizations:
 - Additional AD/LDAP groups will be retrieved if they match your group filter.
 - AD/LDAP groups that are no longer included in your filter that have a corresponding Mattermost group will be deleted.  
 - Users that have been removed from a AD/LDAP group will be removed from the synchronized Mattermost group (their memberships will not be removed from the team and channel, however). 

.. note::
The sync process does not create Mattermost groups.  Mattermost groups are created when you “link” the AD/LDAP group as outlined in the next section. Users are added to Mattermost groups on their first login after the synchronization.

.. image:: ../images/Group_Group_Member_Sync.png
 
After the AD/LDAP groups have been synchronized, you can go to **System Console > Access Control > Groups** to link and configure Mattermost groups. 

Linking AD/LDAP groups to Mattermost groups
--------------------------------------------

Groups that have been returned from your AD/LDAP group filter will be available in a list view on the Groups page. The link action will create Mattermost groups corresponding to the AD/LDAP group. AD/LDAP groups that have been linked to a Mattermost group will display the ‘Linked’ icon. AD/LDAP groups that have not been linked to a Mattermost group will display the ‘Not Linked’ icon. 

.. image:: ../images/Groups_listing.png

Groups can be linked individually by the inline “Linked” button or by using the checkbox next the group name to select multiple groups and using the blue “Link Selected Groups” button. When selecting multiple groups and there is a mix of “Linked” and “Not Linked” states, the bulk action of the button will be “Link Selected Groups” until all selected are marked “Linked”

If you see a “Linked Failed” message, click on the message or you can check the box before the group name exposing the inline link message again, allowing you to try the link again.

Configure the group
-------------------

AD/LDAP groups that have been linked to Mattermost groups are able to be configured.  To configure the group select “Configure”.  This will open up the Group Configuration page.  On this page you will see the group Profile, which includes the group name.  This name is automatically mapped from the AD/LDAP group common name attribute and is read-only.  

Add default teams or channels for the group
--------------------------------------------
To add the default Team or Channels that you want the group members to default in, select either “Add Team” or “Add Channel” on from the blue “Add Team or Channel” button.  You may select multiple teams and channels.  

.. image:: ../images/Add_Team_Or_Channel.png

Channels are nested below the Team they belong to in the team and channel list.  

 - Teams that are open for anyone to join are indicated by:
.. image::  ../images/open_team.png  
   
 - Teams that are not open for anyone to join are indicated by:
.. image:: ../images/private_team.png 
 
 - Public channels are indicated by: 
.. image:: ../images/public_channel.png icon 

 - private channels are indicated by:
.. image::../images/private_channel.png icon.  

Teams added will include default channels, Town Square, and Off-Topic. Adding a channel without setting the team will add the implied team to the listing below, but not to the group specifically.

Teams and channels membership synchronization
----------------------------------------------

Default teams and channels will be added to the group members user interface when they login for the first time after the group has been configured with the specified teams and channels. It may take a few seconds to load all team and channel memberships for a user depending on the number of teams and channels the group is defaulted to.  This process is independent of the AD/LDAP synchronization process to support future functionality of groups. 

.. note::
Users are not removed from the team or channel on subsequent synchronizations of the AD/LDAP groups.  Users will need to be manually removed from the Team or Channel per the existing functionality.  They will not be re-added if they were manually removed.

.. image:: ../images/Team_Channel_Membership_Sync.png

Remove configured teams and channels from a group
-------------------------------------------------
To remove a team or channel configured for a group, click “Remove” to the right of the team or channel name. 

View users belonging to the group
---------------------------------

Users who have logged in and accessed Mattermost will be visible in the members list on the group object. Members are read-only at this time and new members can be added through management in your AD/LDAP system. 

.. image:: ../images/Group_Members.png

Users will be removed from the group on subsequent synchronizations, however they will not be removed from the teams and channels that they were defaulted to in the synchronization. If a user is removed from a AD/LDAP group and then later re-added, they will be defaulted again into the teams and channels configured in the group. If a member is removed all together from the AD/LDAP system all their team and channel memberships will be removed. 

..note:: 
When a member removes themselves manually from a channel, that action is tracked in the Channel Member History table.  Users are not re-added to channels in which they previously removed themselves. 

Managing groups
---------------
Once a group has been configured, it can be edited to change the default team and channels, by clicking “Edit” on the group on the list view.  

Deleting groups
---------------
Groups can be deleted by adjusting your AD/LDAP group filter to remove the group or by unlinking the group on the groups listing page. If you add the group back by re-adjusting the AD/LDAP group filter and link the group again on the group configuration page, the previous configurations will be available.

Frequently Asked Questions
----------------------------

Why is AD/LDAP Group Sync in alpha?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to make sure we have tested this feature in environments that have different AD/LDAP system and group structures to ensure the feature works well in the different varieties of environments our clients have. 

When will AD/LDAP Group Sync be in beta?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We expect AD/LDAP Group Sync to be in beta early in 2019. 

LDAP group sync will be in beta for a period of time until: 
1. Searching and support for managing large volumes of groups and users is released. 
2. This feature has been tested on a system with 10,000s of concurrent active users.


Why can't my users see the teams and channels they have been synced to?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users are synced to channels on their first login and on scheduled synchronization jobs as defined in the AD/LDAP configuration.  If the user is already a user within the system prior to the configuration of the teams and channels for the group, the next scheduled synchronization job will add the teams and channels.  

You can manually initiate a synchronization from **System Console > Authentication > AD/LDAP > AD/LDAP Synchronize Now**.  Users may need to refresh to see the updates. 


How do nested groups work with AD/LDAP Group Sync?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users within nested groups are included as members of parent groups. The group filter that you specify can include any type of LDAP group on your system. The 'memberof' LDAP attribute is used to determine nested groups that belong to a parent group.   
