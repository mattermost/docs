Configuration settings
======================

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost configuration settings are maintained in the ``config.json`` configuration file, located in the ``mattermost/config`` directory. System Admins can manage Mattermost configuration using the System Console, or by modifying the ``config.json`` file directly using a text editor. 

.. note::

   Mattermost must have write permissions to ``config.json``, otherwise configuration changes made within the System Console will have no effect.

Configuration in database
--------------------------

|all-plans| |self-hosted|

From Mattermost v5.10, self-hosted system configuration can be stored in the database. This changes the Mattermost binary from reading the default ``config.json`` file to reading the configuration settings stored within a configuration table in the database. See the `Mattermost database configuration <https://docs.mattermost.com/configure/configuation-in-mattermost-database.html>`__ documentation for migration details.

Environment variables
---------------------

|all-plans| |self-hosted|

From Mattermost v3.8, you can use `environment variables <https://docs.mattermost.com/configure/environment-variables.html>`__ to manage Mattermost configuration. Environment variables override settings in ``config.json``. If a change to a setting in ``config.json`` requires a restart to take effect, then changes to the corresponding environment variable also require a server restart. 

Configuration reload
--------------------

|all-plans| |self-hosted|

From Mattermost v5.38, the “config watcher”, the mechanism that automatically reloads the ``config.json`` file, has been deprecated in favor of the `mmctl config reload <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-config-reload>`__ command that must be run to apply configuration changes after they’re made. This change will improve configuration performance and robustness.

Deprecated configuration settings
---------------------------------

See the `deprecated configuration settings documentation <https://docs.mattermost.com/configure/deprecated-configuration-settings.html>`__ for details on all deprecated Mattermost configuration settings that are no longer supported.

Site Configuration
-------------------

Authentication
---------------

Authentication settings to enable account creation and log in with email, GitLab, Google or Office 365 OAuth, AD/LDAP, or SAML.

Plugins
-------

Integrations
------------

Compliance
----------

Experimental
------------




