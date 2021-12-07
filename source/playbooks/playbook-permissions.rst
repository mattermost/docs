Roles and Permissions
=====================

There are different ways to access and interact with playbooks and this is controlled in the System Console by Playbook Admins in the form of permissions. Permissions can be granted in a variety of ways, to allow for different combinations of access and visibility, and to different roles.

Permissions in Playbooks are inherited from System Schemes which apply across Mattermost. The settings for the Playbook Admin role are managed by the System Admin - the Playbook Admin doesn't have access to the System Console to modify permissions. The Playbook Admin role is a default role, and members need to be promoted to the role from within Playbooks. The Playbook Admin role then applies across the Playbooks platform.

Getting started
---------------

The Playbooks default settings allow for members to access and modify everything. This means that members can add and remove other members, edit playbooks, convert Public playbooks to Private playbooks and so on.

Roles
-----

There are two types of roles that apply to playbooks:

System roles
~~~~~~~~~~~~~

**Member**

* Members are users of Mattermost who belong to the team within which the run is active and who may have a vested interest in the run.
* A member can follow a run or a playbook.
* A member is part of a run either as an active participant or spectator. 

**Playbook Admin**

* Playbook Admins are also members, but have elevated permissions to change playbook and run visibility and functional settings. They can be System or Team Admins as well but don’t have to be.
* A playbook Admin’s purpose is to manage the configuration settings and member permissions.
* A playbook Admin can follow a run or a playbook.

Playbook-specific roles
~~~~~~~~~~~~~~~~~~~~~~~

**Participant**

* Participants are members of a run and have the same function as them. The only difference is active vs. passive participation.
* A participant is a member of a run either as an active participant or spectator. 
* A participant can follow a run or a playbook.

**Owner**

* Owners are the touchpoint of a run and coordinate its start and finish. They can be replaced with another owner.
* An owner is a team member who starts a run using a specific playbook. 
* An owner can follow a run or a playbook, including the ones they own.
* There are no additional permissions or benefits an owner has.

Permissions
-----------

The default settings allow all members to participate in runs, edit playbooks, view runs and playbooks, remove other members from runs, etc. Using permissions provides better control over confidential runs and playbooks, as well as member management.

Create read-only playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~

Restrict who can convert playbooks from Public to Private
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

