Important notes for Mattermost System Admins
============================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.


DO NOT manipulate the Mattermost database
------------------------------------------

In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation. If you need to permanently delete a team or user, use the `mmctl user delete <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-user-delete>`__ command, or the `mattermost user delete <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-user-delete>`__ CLI command. 

Promote a user to System Admin role
-----------------------------------

If the System Admin leaves the organization or is otherwise unavailable, you can use the command line interface to promote a user to the System Admin role using the `mmctl roles <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-roles>`__ command, or by using the `mattermost roles system_admin <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-roles-system-admin>`__ CLI command. The user must log out and then log back in before the System Admin role is applied.

Deactivate users
----------------

To preserve audit history, users are typically never deleted from the system. Instead, users are deactivated. You can access, filter, and search a list of all users by going to **System Console > User Management > Users**. Select the user's role, then select **Deactivate**.

If it's necessary to permanently delete a user, (e.g. for the purposes of `GDPR <https://gdpr-info.eu/>`__), you can use the `mmctl user delete <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-user-delete>`__ command, or the `mattermost user delete <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-user-delete>`__ CLI command. 

.. note::
    AD/LDAP user accounts can't be deactivated from Mattermost. They must be deactivated from Active Directory.

Optimize your workspace
------------------------

From Mattermost v6.5, System Admins review their workspace health and growth scores by going to **System Console > Reporting > Workspace Optimization**, then taking advantage of recommended actions to ensure their workspace is running smoothly and teams are maximizing productivity. See the `workspace optimization <https://docs.mattermost.com/configure/optimize-your-workspace.html>`__ documentation for details.

Mattermost releases regular updates to `Mattermost Team Edition <https://mattermost.com/>`_ and `Mattermost Enterprise Edition <https://mattermost.com/pricing-self-managed/>`_. The `Mattermost self-hosted changelog <https://docs.mattermost.com/install/self-managed-changelog.html>`_ provides details about changes within each release. When you upgrade your Mattermost server frequently, your users can access new features, improved user experiences, bug fixes, security fixes, and Mobile App compatibility.

See the `Upgrade Guide <https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html>`__ for step-by-step instructions on upgrading your Mattermost server.