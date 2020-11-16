====================================
Additional System Admin Roles (E20)
====================================

From v5.28, System Admins can assign roles to members, allowing them access only to designated areas of the System Console. This allows other members of your organization to perform certain administrative tasks without providing access to all system administrative capabilities.

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

**To grant the Read Only Admin role to two users, Bob Smith and Sue Clark:**

``mmctl permissions role assign system_read_only_admin bob-smith sue-clark``

**To remove the System Manager role from a single user called Bob Smith:**

``mmctl permissions role unassign system_manager bob-smith``

Editing Privileges of Admin Roles (Advanced)
--------------------------------------------

Each of the admin roles have defined, default privileges as outlined above. 

System Admins can grant read and write access to other areas of the System Console, as well as remove read write access (including default access), for each role. This is completed using the mmctl tool, either locally or remotely.

The format of the mmctl command is:

``mmctl permissions add [role_name] [permission...]``

**To grant write access to the Authentication section of the System Console for all users with the User Manager role:**

``mmctl permissions add system_user_manager sysconsole_write_authentication``

**To grant read only access to the Authentication section of the System Console for all users with the User Manager role:**

``mmctl permissions remove system_user_manager sysconsole_read_authentication``

**To remove write access to the Authentication section of the System Console for all users with the User Manager role:**

``mmctl permissions remove system_user_manager sysconsole_write_authentication``

Admin Roles and Privileges
---------------------------

**Roles**

- ``system_manager``
- ``system_user_manager``
- ``system_read_only_admin``

**Privileges**

- ``PERMISSION_SYSCONSOLE_READ_ABOUT``
- ``PERMISSION_SYSCONSOLE_WRITE_ABOUT``

- ``PERMISSION_SYSCONSOLE_READ_REPORTING``
- ``PERMISSION_SYSCONSOLE_WRITE_REPORTING``

- ``PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_USERS``
- ``PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_USERS``

- ``PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_GROUPS``
- ``PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_GROUPS``

- ``PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_TEAMS``
- ``PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_TEAMS``

- ``PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_CHANNELS``
- ``PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_CHANNELS``

- ``PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_PERMISSIONS``
- ``PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_PERMISSIONS``

- ``PERMISSION_SYSCONSOLE_READ_ENVIRONMENT``
- ``PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT``

- ``PERMISSION_SYSCONSOLE_READ_SITE``
- ``PERMISSION_SYSCONSOLE_WRITE_SITE``

- ``PERMISSION_SYSCONSOLE_READ_AUTHENTICATION``
- ``PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION``

- ``PERMISSION_SYSCONSOLE_READ_PLUGINS``
- ``PERMISSION_SYSCONSOLE_WRITE_PLUGINS``

- ``PERMISSION_SYSCONSOLE_READ_INTEGRATIONS``
- ``PERMISSION_SYSCONSOLE_WRITE_INTEGRATIONS``

- ``PERMISSION_SYSCONSOLE_READ_COMPLIANCE``
- ``PERMISSION_SYSCONSOLE_WRITE_COMPLIANCE``

- ``PERMISSION_SYSCONSOLE_READ_EXPERIMENTAL``
- ``PERMISSION_SYSCONSOLE_WRITE_EXPERIMENTAL``

Frequently Asked Questions
--------------------------

Can a User Manager or System Manager reset an administrator’s email or password without their knowledge?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is not possible with the default privileges of these roles. The ability to reset passwords or email addresses of administrators is limited to System Admins.  

Can a User Manager or System Manager access the configuration file? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. However, they will only have access to read actual values and modify values in accordance with their permissions. If appropriate read permissions do not exist, the default key values will be displayed.

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
