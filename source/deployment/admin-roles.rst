=============================
Configuring Admin Roles (E20)
=============================

From v5.28, additional system admin roles can be configured to only have access to designated areas of the System Console. This enables you to delegate certain administrative tasks to other members of your organization without providing access to all administrative capabilities.

**System Manager**

  - Read/Write
      - User Management
        - Permissions (Read Only)
      - Environment
      - Site Configuration
      - Integrations
  - Read Only
     - Edition/License
     - Reporting
     - Authentication
     - Plugins

**User Manager**

  - Read/Write
      - User Management 
       - Permissions (Read Only)
  - Read Only
      - Authentication

**Read Only Admin**

  - Read Only
     - All pages within the System Console

Assigning Admin Roles
----------------------

System Admins can assign roles and modify privileges using mmctl, either locally or remotely.

``mmctl permissions role assign [role_name] [username...]``

To grant roles to captain-marvel and clark kent

``mmctl permissions role assign system_manager captain-marvel clark-kent``

``mmctl permissions role assign system_user_manager captain-marvel clark-kent``

``mmctl permissions role assign system_read_only_admin captain-marvel clark-kent``

To add a specific page (user management in this example) to roles:

``mmctl permissions add system_user_manager sysconsole_read_user_management_users``

``mmctl permissions role assign system_manager system_manager``
