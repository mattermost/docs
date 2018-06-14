Advanced Permissions: Backend Infrastructure
=============================================

This document outlines the backend server infrastructure for permissions in Mattermost and is recommended only for technical Admins or developers looking to make modifications to their installation.


.. note::

  The contents of this document apply to Mattermost Server version 5.0 and later. 


.. contents::
  :backlinks: top
  :local:
  
Entity Definitions
--------------------

Permissions
~~~~~~~~~~~~

A **permission** describes a permitted action which may be carried out on an object. It describes the action that users who have been granted the permission may perform in the context in which they have been granted it.

Roles
~~~~~~

A **role** is something to which permissions are granted, that is then assigned to users, in contexts, in order to grant them the assigned permissions in that context. One user may end up with different sets of permissions granted by different roles in different contexts.

Scope
~~~~~~

Permissions live within a given scope. There are three scopes in the Mattermost system: System, Team and Channel. Permissions cascade down the scopes from the context in which they are applied. For example, if a “Channel” scoped permission is applied to a “Team” context, the permission applies to any channels within that team. A permission is considered,

- **System scope** if it makes sense only on the system level. For example, ``manage_oauth``.
- **Team scope** if it makes sense at the team level and system level. For example, ``create_public_channel``.
- **Channel scope** if it makes sense at channel, team and system level. For example, ``manage_public_channel_properties``.

Context
~~~~~~~~

A **context** is an instance of a scope. For example, a channel called "Developers Hangout" is an instance of channel scope. Contexts have hierarchical relationships between them that reflect the hierarchical ordering of scopes. Each context has one parent, and may have multiple children, with the ultimate parent context being the system context:

- A channel context has a parent team context, whose parent is the system context. For example, the "Developers Hangout" channel is the channel context, with parent team context "Contributors Team", with parent system context.
- A team context has a parent system context and child channel contexts. For example, the "Contributors Team" is the team context, with parent system context, and with children channel contexts such as "Developers Hangout", "Reception" and "Marketing".

When determining whether a user is allowed to carry out a given action in a given context, the union of the permissions of all roles that user has been assigned in the current context and its parent contexts is calculated. This enables permissions to cascade down the scope hierarchy. For example, if a users is granted the ``manage_public_channel_properties`` permission in a role in the system context, then the user has permissions to manage public channel properties in all channels, in all teams, of which they are a member.

Schemes
~~~~~~~~~

Schemes describe the default roles applied to users in a context, and all child contexts. Schemes are either defined specifically for a context, or if they are not specified, the relevant parts of the parent context’s scheme are applied, ultimately climbing the hierarchy to the System Scheme, which serves the purpose of providing the system-wide defaults. For example, if Team A does not have a team-scoped scheme defined, the System Scheme will provide the defaults for all contexts in Team A.

Additionally, the lowest-scoped scheme always takes precedence in the context. For example, if Team B has a team-scoped scheme, that scheme takes precedence over the System Scheme defaults for all contexts in Team B. 

Data Structure
----------------

Permissions
~~~~~~~~~~~~

Permissions in Mattermost are a property of the server code base and are not created or modified dynamically. The current set of permissions are as described in the table below.

XXXXXX GG: Please review/tweak this and then I'll create the RST table to put here: https://docs.google.com/spreadsheets/d/1z3yUIQs2JaxmUjD5Q8MZSijvbE2o8CoHdvV5Vfj-y4Y/edit#gid=0 

Applicable database fields and tables.

``User`` ``TeamMember`` ``ChannelMember`` Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Roles are applied to objects that represents that user’s membership in a context. These are represented by the following objects in the Mattermost data model:

- ChannelMember for a channel context.
- TeamMember for a team context.
- User for the system context. 

XXXXXX GG: can we expand on this, what fields are relevant in these tables?

``Roles`` Table
~~~~~~~~~~~~~~~~

Roles are dynamic and user configurable, necessitating a database table with the following fields:

- Id (Autoincrement, Primary Key)
- Name (Unique String with Character Constraints, e.g. “team_user”).
- Display Name (String)
- Description (String)
- Permissions (String - golang style “fields” with permission IDs).
- Scheme Managed (bool) - indicates whether this role is managed as part of a scheme.

``Schemes`` Table
~~~~~~~~~~~~~~~~~~

Schemes are dynamic and user configurable, necessitating a database table with the following fields:

- Id (Autoincrement, Primary Key)
- Name (Unique String with Character Constraints, e.g. “corporate_scheme”)
- Description (String)
- Scope (String): Team or Channel
- Team Admin Role (String): Empty if Channel Scope
- Team User Role (String): Empty if Channel Scope
- Channel Admin Role (String): Always provided
- Channel User Role (String): Always provided

XXXXXX GG: What about the system admin and system user roles for the system default scheme? How are those defined if the schemes table doesn't have those fields?
