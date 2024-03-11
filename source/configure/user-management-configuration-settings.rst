User management configuration settings
======================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Manage your Mattermost users including their access permissions, groups, teams, channels, as well as their access to the System Console. Configure this feature in the System Console by going to **User Management**:

- `Users <#users>`__
- `Groups <#groups>`__
- `Teams <#teams>`__
- `Channels <#channels>`__
- `Permissions <#permissions>`__
- `System roles <#system-roles>`__

----

Users
-----

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

Getting people set up with a Mattermost account is typically something that system admins do when deploying and configuring the Mattermost workspace. A Mattermost admin can :doc:`provision Mattermost users </onboard/user-provisioning-workflows>` using one or more of the following methods:

- :ref:`Enable account creation <configure/authentication-configuration-settings:enable account creation>`.
- Use :ref:`mmctl user create <manage/mmctl-command-line-tool:mmctl user create>` or Mattermost `APIs <https://api.mattermost.com/#tag/users>`__ to create user accounts.
- :ref:`Migrate user accounts <onboard/migrating-to-mattermost:migration guide>` from other collaboration systems and :doc:`bulk load </onboard/bulk-loading-data>` that user data into Mattermost.
- Connect an authentication service to assist with user provisioning, such as :doc:`AD/LDAP authentication </onboard/ad-ldap>` or :doc:`SAML authentication </onboard/sso-saml>`.

+----------------------------------------------------------------+-------------------------------------------------------------+
| Manage activated and deactivated users, revoke all user        | - System Config path: **User Management > Users**           |
| sessions, access individual users to view their User ID,       | - ``config.json setting``: N/A                              |
| add users to other teams, and view the teams they are on,      | - Environment variable: N/A                                 |
| and what their role is on a team.                              |                                                             |
+----------------------------------------------------------------+-------------------------------------------------------------+
| **Note**: You can search for users by partial first name, last name, nickname, or username.                                  |
+----------------------------------------------------------------+-------------------------------------------------------------+

Identify a User's ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Users can be specified in Mattermost by username or user ID. Usernames automatically resolve when a match is detected.
System admins can identify a user's ID using the Mattermost API or mmctl. 

Using the API
^^^^^^^^^^^^^^^^

Use this method if you need to automate user-related tasks or integrate with external systems.
Make an HTTP GET request to the following endpoint: ``https://your-mattermost-url/api/v4/users/username/username_here``.
Replace ``your-mattermost-url`` with the URL of your Mattermost instance and ``username_here`` with the username you are looking for.
The API response contains a JSON object that includes the user's ID among other details.

Using mmctl
^^^^^^^^^^^^^^^^

If you prefer command-line tools, Mattermost offers mmctl for system administration.
In a terminal window, use the following command to list all users and their IDs: ``mmctl user list`` to return a list of user IDs.

Deactivate user accounts
~~~~~~~~~~~~~~~~~~~~~~~~

If you need to remove a user from your Mattermost deployment, you can deactivate the user account. Deactivated users have an deactivated status, are logged out of Mattermost as soon as they are deactivated, and deactivated users can no longer log back in. While a user account is deactivated, you can manage the user's role, password, and email address.

Deactivate a user account by selecting their role, then select **Deactivate**. You can re-activate that user account later by selecting **Activate**.

----

Groups
------

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------+
| Manage default teams and channels by linking AD/LDAP groups   | - System Config path: **User Management > Groups**          |
| to Mattermost groups.                                         | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| See the :doc:`AD/LDAP groups </onboard/ad-ldap-groups-synchronization>` documentation for                                   |
| details.                                                                                                                    |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Teams
-----

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------+
| Manage team settings, including group synchronization for     | - System Config path: **User Management > Teams**           |
| teams.                                                        | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| See the :ref:`using AD/LDAP synchronized groups to manage team or private channel membership                                |
| <onboard/ad-ldap-groups:synchronize ad/ldap groups to mattermost>` documentation for details.                               |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Channels
--------

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-------------------------------------------------------------------------+-------------------------------------------------------------+
| Manage channel settings, including group synchronization on channels.   | - System Config path: **User Management > Channels**        |
|                                                                         | - ``config.json setting``: N/A                              |
|                                                                         | - Environment variable: N/A                                 |
+-------------------------------------------------------------------------+-------------------------------------------------------------+
| **Notes**:                                                                                                                            |
|                                                                                                                                       |
| - Channels can be deleted with all content, including posts in the database, using the `mmctl channel delete </manage/mmctl-command-  |
|   line-tool.html#mmctl-channel-delete>`__ tool.                                                                                       |
| - You can search for channels by channel name or by channel ID.                                                                       |
+-------------------------------------------------------------------------+-------------------------------------------------------------+

----

Permissions
-----------

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------------+-------------------------------------------------------------+
| Restrict actions in Mattermost to authorized users only.            | - System Config path: **User Management > Permissions**     |
|                                                                     | - ``config.json setting``: N/A                              |
|                                                                     | - Environment variable: N/A                                 |
+---------------------------------------------------------------------+-------------------------------------------------------------+
| See :doc:`advanced permissions </onboard/advanced-permissions>` documentation for details                                         |
+---------------------------------------------------------------------+-------------------------------------------------------------+

----

System roles
------------

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------------+------------------------------------------------------------+
| Restrict System Console access to authorized users only.             | - System Config path: **User Management > System Roles**   |
|                                                                      | - ``config.json setting``: N/A                             |
|                                                                      | - Environment variable: N/A                                |
+----------------------------------------------------------------------+------------------------------------------------------------+
| See :doc:`additional system admin roles </onboard/system-admin-roles>` documentation for details                                  |
+----------------------------------------------------------------------+------------------------------------------------------------+