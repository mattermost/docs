=============================
Configuring Admin Roles (E20)
=============================

From v5.28, System Admins can assign roles to members, allowing them access only to designated areas of the System Console. This allows other members of your organization to perform certain administrative tasks without providing access to all administrative capabilities.

- **System Manager:** The System Manager has read/write permissions for management areas of the System Console, such as user management and integrations (excluding permissions). This role has read only access to authentication, reporting, and license interfaces.
- **User Manager:** The User Manager role is able to read/write to all the user management areas (excluding permissions). The authentication interface is read only.
- **Read Only Admin:** This role is able to access all pages of the System Console but has no write access to any.

Roles are assigned via the command line, using the `mmctl tool <https://docs.mattermost.com/administration/mmctl-cli-tool.html>`_.

Each role has a set of default permissions, and when a user is assigned a role, they are able to access the System Console. The items that they can view depend on the role they've been assigned.

**System Manager**

  - Read/Write
      - User Management
      - Environment
      - Site Configuration
      - Integrations
  - Read Only
     - (User Management) Permissions
     - Edition/License
     - Reporting
     - Authentication
     - Plugins

**User Manager**

  - Read/Write
      - User Management 
         - Groups
         - Teams
         - Channels       
  - Read Only
      - (User Management) Permissions
      - Authentication

**Read Only Admin**

  - Read Only
     - All pages within the System Console

Assigning Admin Roles
---------------------

System Admins can assign roles and modify privileges using the mmctl tool. This can be done either locally or remotely.

The format of the mmctl command is:

``mmctl permissions role assign [role_name] [username...]``

**To grant the System Manager role to a single user called Bob Smith:**

``mmctl permissions role assign system_manager bob-smith``

**To grant the User Manager role to two users, Bob Smith and Sue Clark:**

``mmctl permissions role assign system_user_manager bob-smith sue-clark``

``mmctl permissions role assign system_read_only_admin captain-marvel clark-kent``

Frequently Asked Questions
--------------------------

Can a User Manager or System Manager reset an administrator’s email or password without their knowledge?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. The ability to reset passwords, or email addresses of administrators is limited to System Admins.

Are all actions of admin roles logged?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every change made by any admin is included in the audit log.

Can a System Manager change their own permissions or elevate their role?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. System Managers can't elevate their role, and aren't able to elevate other members' roles.

Can any of the new roles view API keys/passwords or other sensitive information within the System Console (such as SMTP, AWS, Elastic Search)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, password information is only visible to System Admins and is obfuscated for other roles.

If download links for compliance exports are enabled in the System Console, can a Read Only Admin download the reports? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only roles that are explicitly granted access to **System Console > Compliance** have access to download compliance reports. 

Can any of the new roles force-join Private channels?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes at this time they can, however, we will be improving on this behavior in the future with a prompt that lets them know they are entering a private channel. We are also planning on adding a permission which would remove the ability to access Private channels.

Can I create a new role or clone an existing role?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, but we are actively seeking feedback on this capability.

Can I use an LDAP filter to assign these roles?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, but we are considering this functionality for a future enhancement.

Can I rename the roles?
^^^^^^^^^^^^^^^^^^^^^^^

This is being considered for future development.

Can a System Manager or User Manager demote or deactivate another Admin or Manager?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No privilege grants the authority to deactivate or demote another admin.

Can a System Manager or User Manager assign or unassign admin roles?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only the System Admin has access to edit system roles.
