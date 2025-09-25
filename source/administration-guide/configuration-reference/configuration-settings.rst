Configuration settings
======================

.. include:: ../../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

System admins for both self-hosted and Cloud Mattermost deployments can manage Mattermost configuration using the System Console by selecting the **Product** |product-list| menu and selecting **System Console**. 

.. note::
  
  - In self-hosted Mattermost deployments, configuration settings are maintained in the ``config.json`` configuration file, located in the ``mattermost/config`` directory, or :doc:`stored in the database </administration-guide/configuration-reference/configuration-in-your-database>`. System admins managing self-hosted deployments can also modify the ``config.json`` file directly using a text editor.
  - Mattermost requires write permissions to the ``config.json`` file; otherwise, configuration changes made within the System Console will have no effect.

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    Self-hosted workspace edition and license settings </administration-guide/configuration-reference/self-hosted-account-settings>
    Cloud workspace subscription, billing, and account settings </administration-guide/configuration-reference/cloud-billing-account-settings>
    Reporting configuration settings </administration-guide/configuration-reference/reporting-configuration-settings>
    User management configuration settings </administration-guide/configuration-reference/user-management-configuration-settings>
    System attributes </administration-guide/configuration-reference/system-attributes>
    Environment configuration settings </administration-guide/configuration-reference/environment-configuration-settings>
    Site configuration settings </administration-guide/configuration-reference/site-configuration-settings>
    Authentication configuration settings </administration-guide/configuration-reference/authentication-configuration-settings>
    Plugins configuration settings </administration-guide/configuration-reference/plugins-configuration-settings>
    Integrations configuration settings </administration-guide/configuration-reference/integrations-configuration-settings>
    Compliance configuration settings </administration-guide/configuration-reference/compliance-configuration-settings>
    Experimental configuration settings </administration-guide/configuration-reference/experimental-configuration-settings>
    Deprecated configuration settings </administration-guide/configuration-reference/deprecated-configuration-settings>
    Bleve search </administration-guide/configuration-reference/bleve-search>

Mattermost configuration settings are organized into the following categories within the System Console:

- :doc:`Self-hosted workspace edition and license settings </administration-guide/configuration-reference/self-hosted-account-settings>`
- :doc:`Cloud workspace subscription, billing, and account settings</administration-guide/configuration-reference/cloud-billing-account-settings>`
- :doc:`Reporting configuration settings </administration-guide/configuration-reference/reporting-configuration-settings>`
- :doc:`User management configuration settings </administration-guide/configuration-reference/user-management-configuration-settings>`
- :doc:`System attributes </administration-guide/configuration-reference/system-attributes>`
- :doc:`Environment configuration settings </administration-guide/configuration-reference/environment-configuration-settings>`
- :doc:`Site configuration settings </administration-guide/configuration-reference/site-configuration-settings>`
- :doc:`Authentication configuration settings </administration-guide/configuration-reference/authentication-configuration-settings>`
- :doc:`Plugins configuration settings </administration-guide/configuration-reference/plugins-configuration-settings>`
- :doc:`Integrations configuration settings </administration-guide/configuration-reference/integrations-configuration-settings>`
- :doc:`Compliance configuration settings </administration-guide/configuration-reference/compliance-configuration-settings>`
- :doc:`Experimental configuration settings </administration-guide/configuration-reference/experimental-configuration-settings>`
- :doc:`Deprecated configuration settings </administration-guide/configuration-reference/deprecated-configuration-settings>`
- :doc:`Bleve search </administration-guide/configuration-reference/bleve-search>`

Configuration in database
--------------------------

.. include:: ../../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Self-hosted system configuration can be stored in the database. This changes the Mattermost binary from reading the default ``config.json`` file to reading the configuration settings stored within a configuration table in the database. See the :doc:`Mattermost database configuration </administration-guide/configuration-reference/configuration-in-your-database>` documentation for migration details.

Environment variables
---------------------

.. include:: ../../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

You can use :doc:`environment variables </administration-guide/configuration-reference/environment-variables>` to manage Mattermost configuration. Environment variables override settings in ``config.json``. If a change to a setting in ``config.json`` requires a restart to take effect, then changes to the corresponding environment variable also require a server restart. 

Configuration reload
--------------------

.. include:: ../../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

The “config watcher”, the mechanism that automatically reloads the ``config.json`` file, has been deprecated in favor of the :ref:`mmctl config reload <administration-guide/admin-tools/mmctl-command-line-tool:mmctl config reload>` command that you must run to apply configuration changes you've made. This improves configuration performance and robustness.

Deprecated configuration settings
---------------------------------

See the :doc:`deprecated configuration settings documentation </administration-guide/configuration-reference/deprecated-configuration-settings>` for details on all deprecated Mattermost configuration settings that are no longer supported.

