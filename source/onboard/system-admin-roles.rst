Additional System Admin Roles
==============================

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Managed deployments.

*Available in legacy Mattermost Enterprise Edition E20*

From v5.28, System Admins can use the command line to assign roles that permit members to have admin access to specified areas of the System Console. This allows members of your organization to perform certain administrative tasks without providing them with access to all system administrative capabilities.

From v5.30, System Admins can also use the System Console to manage additional System Admin roles and privileges.

- **System Manager:** The System Manager has read/write permissions for management areas of the System Console, such as user management and integrations (excluding permissions). This role has read only access to authentication, reporting, and license interfaces.
- **User Manager:** The User Manager role is able to read/write to all the user management areas (excluding permissions). The authentication interface is read only.
- **Viewer:** This role is able to access all pages of the System Console but has no write access to any pages.

There are two ways to assign roles:

1. In the System Console under **User Management > System Roles**.

2. Using the `mmctl tool <https://docs.mattermost.com/manage/mmctl-command-line-tool.html>`__.

When a user is assigned a role, they have access to the System Console. As each role has a different set of default permissions the items that they can view depend on the role they've been assigned.

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

**Viewer**

  - Read Only
     - All pages within the System Console

Assigning Admin Roles
---------------------

System Admins can assign roles using the System Console or the mmctl tool. This can be done either locally or remotely.

  **In the System Console**

- Go to **System Console > User Management > System Roles > Assigned People**. 

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions role assign [role_name] [username...]``

**To grant the System Manager role to a single user called Bob Smith:**

  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **System Manager** role.

  2. Under **Assigned People**, choose **Add People**.

  3. Search for and select ``Bob Smith``, then select **Add** to grant the System Manager role to that user.

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions role assign system_manager bob-smith``

**To grant the User Manager role to two users, Bob Smith and Sue Clark:**

  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **User Manager** role.

  2. Under **Assigned People**, choose **Add People**.

  3. Search for and select **Bob Smith** and **Sue Clark**, then select **Add** to grant the User Manager role to those users.

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions role assign system_user_manager bob-smith sue-clark``

**To grant the Viewer role to two users, Bob Smith and Sue Clark:**

  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **Viewer** role.

  2. Under **Assigned People**, select **Add People**.

  3. Search for and select **Bob Smith** and **Sue Clark**, then select **Add** to grant the Viewer role to those users.

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions role assign system_read_only_admin bob-smith sue-clark``

**To remove the System Manager role from a single user called Bob Smith:**

  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **Viewer** role.

  2. Under **Assigned People** search for **Bob Smith**, then select **Remove**.

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions role unassign system_manager bob-smith``

Editing Privileges of Admin Roles (Advanced)
--------------------------------------------

Each of the admin roles have defined, default privileges as outlined above. 

System Admins can grant read and write access to other areas of the System Console, as well as remove read and write access (including default access), for each role. This is completed using the System Console or the mmctl tool, either locally or remotely.

  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **System Manager**, **User Manager**, or **Viewer** role.

  2. For each set of privileges, select the access level as **Can edit**, **Read only**, or **No access**.

  **Note:** If you set privilege subsections to different access levels then the privilege access level displays as **Mixed Access**.

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions add [role_name] [permission...]``

**To grant write access to the Authentication section of the System Console for all users with the User Manager role:**

  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **User Manager** role.

  2. Under **Privileges > Authentication** select **Can edit**, then select **Save**.

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions add system_user_manager sysconsole_write_authentication``

**To grant read only access to the Authentication section of the System Console for all users with the User Manager role:**

  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **User Manager** role.

  2. Under **Privileges > Authentication** select **Read only**, then select **Save**.

  **Using the mmctl tool**

  The format of the mmctl command is:

  ``mmctl permissions remove system_user_manager sysconsole_read_authentication``

**To remove write access to the Authentication section of the System Console for all users with the User Manager role:**
  
  **In the System Console**

  1. Go to **System Console > User Management > System Roles** then select the **User Manager** role.

  2. Under **Privileges > Authentication** select **No access**, then choose **Save**.

  **Using the mmctl tool**
  
  The format of the mmctl command is:

  ``mmctl permissions remove system_user_manager sysconsole_write_authentication``

**To reset a role to its default set of permissions:**

This is completed using the mmctl tool only, either locally or remotely.

The format of the mmctl command is:

``mmctl permissions reset [role_name]``

For example, to reset the permissions of the ``system_read_only_admin`` role:

``mmctl permissions reset system_read_only_admin``

Admin Roles and Privileges
---------------------------

**Roles**

- ``system_manager``
- ``system_user_manager``
- ``system_read_only_admin``

**Privileges**

+------------------------+--------------------------------------------------------------------------+
| System Console Section | Permissions                                                              |
+========================+==========================================================================+
| About                  |  - PERMISSION_SYSCONSOLE_READ_ABOUT_EDITION_AND_LICENSE                  |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ABOUT_EDITION_AND_LICENSE                 |
+------------------------+--------------------------------------------------------------------------+
| Reporting              | **Site Statistics**                                                      |
|                        |  - PERMISSION_SYSCONSOLE_READ_REPORTING_SITE_STATISTICS                  |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_REPORTING_SITE_STATISTICS                 |
|                        |                                                                          |
|                        | **Team Statistics**                                                      |
|                        |  - PERMISSION_SYSCONSOLE_READ_REPORTING_TEAM_STATISTICS                  |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_REPORTING_TEAM_STATISTICS                 |
|                        |                                                                          |
|                        | **Server Logs**                                                          |
|                        |  - PERMISSION_SYSCONSOLE_READ_REPORTING_SERVER_LOGS                      |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_REPORTING_SERVER_LOGS                     |
+------------------------+--------------------------------------------------------------------------+
| User Management        | **Users**                                                                |
|                        |  - PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_USERS                       |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_USERS                      |
|                        |                                                                          |
|                        | **Groups**                                                               |
|                        |  - PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_GROUPS                      |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_GROUPS                     |
|                        |                                                                          |
|                        | **Teams**                                                                |
|                        |  - PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_TEAMS                       |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_TEAMS                      |
|                        |                                                                          |
|                        | **Channels**                                                             |
|                        |  - PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_CHANNELS                    |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_CHANNELS                   |
|                        |                                                                          |
|                        | **Permissions**                                                          |
|                        |  - PERMISSION_SYSCONSOLE_READ_USERMANAGEMENT_PERMISSIONS                 |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_USERMANAGEMENT_PERMISSIONS                |
+------------------------+--------------------------------------------------------------------------+
| Environment            | **Web Server**                                                           |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_WEB_SERVER                     |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_WEB_SERVER                    |
|                        |                                                                          |
|                        | **Database**                                                             |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_DATABASE                       |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_DATABASE                      |
|                        |                                                                          |
|                        | **Elasticsearch**                                                        |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_ELASTICSEARCH                  |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_ELASTICSEARCH                 |
|                        |                                                                          |
|                        | **File Storage**                                                         |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_FILE_STORAGE                   |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_FILE_STORAGE                  |
|                        |                                                                          |
|                        | **Image Proxy**                                                          |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_IMAGE_PROXY                    |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_IMAGE_PROXY                   |
|                        |                                                                          |
|                        | **SMTP**                                                                 |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_SMTP                           |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_SMTP                          |
|                        |                                                                          |
|                        | **Push Notification Server**                                             |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_PUSH_NOTIFICATION_SERVER       |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_PUSH_NOTIFICATION_SERVER      |
|                        |                                                                          |
|                        | **High Availability**                                                    |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_HIGH_AVAILABILITY              |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_HIGH_AVAILABILITY             |
|                        |                                                                          |
|                        | **Rate Limiting**                                                        |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_RATE_LIMITING                  |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_RATE_LIMITING                 |
|                        |                                                                          |
|                        | **Logging**                                                              |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_LOGGING                        |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_LOGGING                       |
|                        |                                                                          |
|                        | **Session Lengths**                                                      |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_SESSION_LENGTHS                |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_SESSION_LENGTHS               |
|                        |                                                                          |
|                        | **Performance Monitoring**                                               |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_PERFORMANCE_MONITORING         |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_PERFORMANCE_MONITORING        |
|                        |                                                                          |
|                        | **Developer**                                                            |
|                        |  - PERMISSION_SYSCONSOLE_READ_ENVIRONMENT_DEVELOPER                      |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_ENVIRONMENT_DEVELOPER                     |
+------------------------+--------------------------------------------------------------------------+
| Site Configuration     | **Customization**                                                        |
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_CUSTOMIZATION                         | 
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_CUSTOMIZATION                        |   
|                        |                                                                          |
|                        | **Localization**                                                         |
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_LOCALIZATION                          | 
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_LOCALIZATION                         |   
|                        |                                                                          |   
|                        | **Users and Teams**                                                      | 
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_USERS_AND_TEAMS                       |   
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_USERS_AND_TEAMS                      | 
|                        |                                                                          | 
|                        | **Notifications**                                                        |   
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_NOTIFICATIONS                         |   
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_NOTIFICATIONS                        |  
|                        |                                                                          |   
|                        | **Announcement Banner**                                                  |    
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_ANNOUNCEMENT_BANNER                   |    
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_ANNOUNCEMENT_BANNER                  |  
|                        |                                                                          | 
|                        | **Emoji**                                                                |     
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_EMOJI                                 |  
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_EMOJI                                |
|                        |                                                                          | 
|                        | **Posts**                                                                |
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_POSTS                                 |  
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_POSTS                                |    
|                        |                                                                          |
|                        | **File Sharing and Downloads**                                           |
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_FILE_SHARING_AND_DOWNLOADS            |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_FILE_SHARING_AND_DOWNLOADS           | 
|                        |                                                                          |  
|                        | **Public Links**                                                         |
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_PUBLIC_LINKS                          | 
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_PUBLIC_LINKS                         |    
|                        |                                                                          |     
|                        | **Notices**                                                              |      
|                        |  - PERMISSION_SYSCONSOLE_READ_SITE_NOTICES                               |   
|                        |  - PERMISSION_SYSCONSOLE_WRITE_SITE_NOTICES                              |    
+------------------------+--------------------------------------------------------------------------+
| Authentication         | **Signup**                                                               |
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_SIGNUP                      |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_SIGNUP                     |
|                        |                                                                          |
|                        | **Email**                                                                |
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_EMAIL                       | 
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_EMAIL                      |  
|                        |                                                                          |
|                        | **Password**                                                             |   
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_PASSWORD                    |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_PASSWORD                   |   
|                        |                                                                          |    
|                        | **MFA**                                                                  |     
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_MFA                         |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_MFA                        |
|                        |                                                                          |
|                        | **AD/LDAP**                                                              |
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_MFA                         |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_MFA                        |     
|                        |                                                                          |    
|                        | **SAML 2.0**                                                             |     
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_SAML                        |   
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_SAML                       | 
|                        |                                                                          |
|                        | **OpenID Connect**                                                       | 
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_OPENID                      |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_OPENID                     |
|                        |                                                                          |
|                        | **Guest Access**                                                         | 
|                        |  - PERMISSION_SYSCONSOLE_READ_AUTHENTICATION_GUEST_ACCESS                |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_AUTHENTICATION_GUEST_ACCESS               | 
+------------------------+--------------------------------------------------------------------------+
| Plugin                 |  - PERMISSION_SYSCONSOLE_READ_PLUGINS                                    |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_PLUGINS                                   |
+------------------------+--------------------------------------------------------------------------+
| Integrations           | **Integration Management**                                               |
|                        |  - PERMISSION_SYSCONSOLE_READ_INTEGRATIONS_INTEGRATION_MANAGEMENT        |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_INTEGRATIONS_INTEGRATION_MANAGEMENT       |
|                        |                                                                          |
|                        | **Bot Accounts**                                                         |   
|                        |  - PERMISSION_SYSCONSOLE_READ_INTEGRATIONS_BOT_ACCOUNTS                  |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_INTEGRATIONS_BOT_ACCOUNTS                 |
|                        |                                                                          |
|                        | **GIF (Beta)**                                                           | 
|                        |  - PERMISSION_SYSCONSOLE_READ_INTEGRATIONS_GIF                           |   
|                        |  - PERMISSION_SYSCONSOLE_WRITE_INTEGRATIONS_GIF                          | 
|                        |                                                                          |       
|                        | **CORS**                                                                 |
|                        |  - PERMISSION_SYSCONSOLE_READ_INTEGRATIONS_CORS                          | 
|                        |  - PERMISSION_SYSCONSOLE_WRITE_INTEGRATIONS_CORS                         |                       
+------------------------+--------------------------------------------------------------------------+
| Compliance             | **Data Retention Policy**                                                |
|                        |  - PERMISSION_SYSCONSOLE_READ_COMPLIANCE_DATA_RETENTION_POLICY           |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_COMPLIANCE_DATA_RETENTION_POLICY          |
|                        |                                                                          |
|                        | **Compliance Export**                                                    |
|                        |  - PERMISSION_SYSCONSOLE_READ_COMPLIANCE_COMPLIANCE_EXPORT               |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_COMPLIANCE_COMPLIANCE_EXPORT              |
|                        |                                                                          |
|                        | **Compliance Monitoring**                                                |
|                        |  - PERMISSION_SYSCONSOLE_READ_COMPLIANCE_COMPLIANCE_MONITORING           |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_COMPLIANCE_COMPLIANCE_MONITORING          |
|                        |                                                                          |
|                        | **Custom Terms of Service**                                              |
|                        |  - PERMISSION_SYSCONSOLE_READ_COMPLIANCE_CUSTOM_TERMS_OF_SERVICE         |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_COMPLIANCE_CUSTOM_TERMS_OF_SERVICE        |
+------------------------+--------------------------------------------------------------------------+
| Experimental           | **Features**                                                             |
|                        |  - PERMISSION_SYSCONSOLE_READ_EXPERIMENTAL_FEATURES                      |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_EXPERIMENTAL_FEATURES                     |
|                        |                                                                          |
|                        | **Feature Flags**                                                        |
|                        |  - PERMISSION_SYSCONSOLE_READ_EXPERIMENTAL_FEATURE_FLAGS                 |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_EXPERIMENTAL_FEATURE_FLAGS                |
|                        |                                                                          |
|                        | **Bleve**                                                                |
|                        |  - PERMISSION_SYSCONSOLE_READ_EXPERIMENTAL_BLEVE                         |
|                        |  - PERMISSION_SYSCONSOLE_WRITE_EXPERIMENTAL_BLEVE                        |
+------------------------+--------------------------------------------------------------------------+

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
