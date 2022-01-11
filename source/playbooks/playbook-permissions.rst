Roles and Permissions
=====================

There are different ways for teams to access and interact with playbooks. This is managed in the System Console using permissions. Permissions can be granted in a variety of ways, to allow for different combinations of access and visibility.

Permissions are provided using:

* **System Scheme:** Applies permissions universally across all teams, channels, and playbooks.
* **Team Override Schemes:** Allow admins to customize permissions for each team (available in Mattermost Enterprise and Professional).

For more information about System and Team Override Schemes, refer to the `Advanced Permissions <https://docs.mattermost.com/onboard/advanced-permissions.html>`__ documentation.

In the context of Playbooks, members are assigned a role and based on the selected permissions, this determines how they interact with Playbooks. A member can be a member of one playbook, and an admin of another. This allows for granular permissions across teams and departments.

Permissions are applied only to playbooks - there are no permissions that are specific to runs.

Playbook roles
---------------

**Member**

In the context of Playbooks, members are users of Mattermost who are added to a playbook.

**Playbook Admin**

In the context of Playbooks, Playbook Admins are also members, and may have elevated permissions to change playbook and run visibility as well as functional settings. They do not have access to the System Console and their privileges are managed by the System Admin. Members need to be promoted to the role from within Playbooks. The Playbook Admin role is applied per playbook.

.. note::

Before you make changes to permissions and to ensure that you don't lose access to playbooks, . To do this, navigate to the playbook you're a member of. Select the **Manage Access** icon and change your role from **Member** to **Admin**.

Playbooks permissions
---------------------

The default Playbooks settings are completely open which enable all members to participate in runs, edit playbooks, view runs and playbooks, remove other members from runs, edit actions, and make other changes. Permissions provide better control over confidential runs and playbooks, as well as member management.

Create read-only playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following example, only Playbook Admins can edit playbooks. Team members can view public and private playbooks and runs, but can't edit playbooks, check off tasks, or remove members from runs. They also can't create public or private playbooks.

1. Go to **System Console > User Management > Permissions**.
2. In the **All Members** section, uncheck **Manage Public Playbooks** and uncheck **Manage Private Playbooks**.
3. Scroll down to the **Playbook Admin** section and confirm that **Manage Public Playbooks** and **Manage Private Playbooks** are checked.
4. Select **Save**.

You can also set permissions for read-only playbooks that do allow members to create new public or private playbooks.

1. Go to **System Console > User Management > Permissions**.
2. In the **All Members** section, uncheck **Manage Public Playbooks** and uncheck **Manage Private Playbooks**.
3. Then, check **Create Public Playbook** and **Create Private Playbook**.
4. Select **Save**.

I want to manage how playbooks are accessed
-------------------------------------------

A public playbook and its associated runs can be viewed by any member of a team. Playbooks can be converted from public to private, but once a playbook is private it can't be converted back to public.

I want to restrict who can convert playbooks from public to private
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can control whether Members can convert playbooks from public to private.

1. Go to **System Console > User Management > Permissions**.
2. In the **All Members** section, check **Convert Playbooks**.
3. Select **Save**.

To restrict this action so only Playbook Admins can convert playbooks from public to private:

1. Go to **System Console > User Management > Permissions**.
2. Scroll down to **Playbook Admin**.
3. Check **Convert Playbooks**.
4. Select **Save**.

I want to control who starts a run
----------------------------------

By default, all Members can start a run using a playbook. You can restrict this so that only Playbook Admins can start a run. Note that with this configuration, Members are not able to start runs or edit playbooks.

1. Go to **System Console > User Management > Permissions**.
2. In the **All Members** section, uncheck **Manage Runs**. This also unchecks **Create Runs**.
3. Scroll down to **Playbook Admin** and ensure that **Manage Runs** and **Create Runs** are checked.
4. Select **Save**.

If you want to continue to allow Members to edit playbooks, an alternative to this configuration is to make the playbook private.
