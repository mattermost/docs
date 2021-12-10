Roles and Permissions
=====================

There are different ways to access and interact with playbooks and this is controlled in the System Console in the form of permissions. Permissions can be granted in a variety of ways, to allow for different combinations of access and visibility, and to different roles. Two permission schemes are provided in Mattermost:

* **System Scheme:** Applies permissions universally across all teams and channels.
* **Team Override Schemes:** Allow admins to customize permissions for each team (available in Mattermost Enterprise and Professional).

You can set the default permissions granted to System Admins, Team Admins, Channel Admins, Playbook Admins, Guests (if enabled), and All Members. The permissions granted in the System Scheme apply system-wide, meaning:

* **Guests:** If Guest Accounts are enabled, permissions apply to guest users in all channels, in all teams.
* **All Members:** Permissions apply to all members, including Admins, in all channels, in all teams.
* **Channel Administrators:** Permissions apply to all Channel Admins in all channels, in all teams.
* **Playbook Admins:** Permissions apply to all Playbook Admins in all channels, in all teams.
* **Team Administrators:** Permissions apply to all Team Admins, in all teams.

For more information about System and Team Override Schemes, refer to the `Advanced Permissions <https://docs.mattermost.com/onboard/advanced-permissions.html>`__ documentation.

Roles
-----

**Member**

In the context of Playbooks, members are users of Mattermost who belong to the team within which the run is active and who may have a vested interest in the run. Depending on the permissions granted, members can have the same privileges as Playbook Admins or restricted privileges. Members are also referred to as participants in a run.

**Playbook Admin**

In the context of Playbooks, Playbook Admins are also members, and may have elevated permissions to change playbook and run visibility and functional settings. The Playbook Admin role is a default role, and members need to be promoted to the role from within Playbooks. The Playbook Admin role is applied per playbook. They do not have access to the System Console and their privileges are managed by System Admin.

Manage playbook visibility
--------------------------

The default Playbooks settings are completely open and the default settings allow all members to participate in runs, edit playbooks, view runs and playbooks, remove other members from runs, edit actions and make other changes. Permissions provide better control over confidential runs and playbooks, as well as member management.

Create read-only playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, set permissions to only allow Playbook Admins to edit playbooks and start runs. Team members can view Public and Private playbooks and runs but can't edit playbooks, check off tasks, or remove members from runs.

1. Go to **System Console > User Management > Permissions**.
2. In the **All Members** section, uncheck **Manage Public Playbooks** and uncheck **Manage Private Playbooks**.
3. Scroll down to the **Playbook Admin** section and confirm that **Manage Public Playbooks** and **Manage Private Playbooks** are checked.
4. Select **Save**.

Manage how playbooks are accessed
---------------------------------

By default, playbooks are Public. This means that any member of the team can view the playbook and associated runs. Playbooks can be converted from Public to Private, but once a playbook is Private it can't be converted back to Public.

Restrict who can convert playbooks from Public to Private
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, you can control whether Members can convert playbooks from Public to Private.

1. Go to **System Console > User Management > Permissions**.
2. In the **All Members** section, check **Convert Playbooks**.
3. Select **Save**.

To restrict this action so only Playbook Admins can convert playbooks from Public to Private:

1. Go to **System Console > User Management > Permissions**.
2. Scroll down to **Playbook Admin**.
3. Uncheck **Convert Playbooks**.
4. Select **Save**.

Control who can start runs
--------------------------

By default, all Members can start a run using a playbook. This setting restricts that action to Playbook Admins.

1. Go to **System Console > User Management > Permissions**.
2. In the **All Members** section, uncheck **Manage Runs**.
3. Scroll down to **Playbook Admin** and ensure that **Manage Runs** is checked.
4. Select **Save**.
