.. _manage-plugins:

Install and manage plugins
==========================

Plugins extend Mattermost with new features and integrations, from pre-built integrations such as GitHub, Jira, and Zoom to custom plugins your team builds in-house. As a system admin, you can install, enable, configure, update, and remove plugins using either the System Console or the :doc:`mmctl command line tool </administration-guide/manage/mmctl-command-line-tool>`.

This page describes how to manage the plugin lifecycle. For a conceptual overview of pre-built and custom plugins, see the :doc:`plugins </integrations-guide/plugins>` documentation. For the complete list of plugin configuration options, see the :doc:`plugins configuration settings </administration-guide/configure/plugins-configuration-settings>` documentation. To build your own plugin, see the `Mattermost plugin developer <https://developers.mattermost.com/integrate/plugins/>`__ documentation.

.. note::

  You must be a system admin to install and manage plugins. Plugins are managed at the server level and apply to your entire Mattermost deployment.

Before you begin
----------------

Plugin availability and the actions you can take depend on a few configuration settings found in the System Console under **Plugins > Plugin Management**. Review these settings before installing or updating plugins:

- **Enable plugins** must be set to **true** (the default) for the plugin system to work. When disabled, all plugins are turned off.
- **Enable Marketplace** must be set to **true** (the default) to install plugins from the in-product Marketplace.
- **Enable remote Marketplace** must be set to **true** (the default) for the Marketplace to connect to the remote endpoint and list community and Mattermost-provided plugins. Set this to **false** for servers that can't reach the internet; the Marketplace then shows only pre-packaged and installed plugins.
- **Upload Plugin** (``EnableUploads``) must be set to **true** to upload plugin bundles from your local computer. This setting applies to self-hosted deployments only.
- **Require plugin signature**, when enabled, validates plugin signatures and **disables plugin file uploads** in the System Console. With this setting enabled, install plugins from the Marketplace or as pre-packaged plugins instead.

.. note::

  If you receive a ``Received invalid response from the server`` error when uploading a plugin, the :ref:`maximum file size <administration-guide/configure/environment-configuration-settings:maximum file size>` configuration setting is likely too small for the plugin bundle. Increase it, and update any proxy settings as needed.

See the :doc:`plugins configuration settings </administration-guide/configure/plugins-configuration-settings>` documentation for details on each of these settings, including their ``config.json`` paths and environment variables.

Install a plugin
----------------

You can install a plugin from the in-product Marketplace, by uploading a plugin bundle, or by using mmctl. Pre-packaged plugins that ship with the Mattermost Server are installed and upgraded automatically when **Automatic prepackaged plugins** is enabled (the default).

From the Marketplace
~~~~~~~~~~~~~~~~~~~~~

Installing from the Marketplace is the recommended method for pre-built plugins. The Marketplace always installs the latest compatible version, and plugins downloaded from the Marketplace are signature-validated.

1. In Mattermost, from the Product menu |product-list|, select **App Marketplace**.
2. Search for or scroll to the plugin you want, and then select **Install**.
3. Once the plugin is installed, select **Configure** to open its settings in the System Console, or **Enable** to turn it on with the default configuration.

.. tip::

  The `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ website offers an expanded selection of community-supported integrations.

By uploading a plugin bundle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload a plugin bundle when you're installing a custom or third-party plugin that isn't in the Marketplace, or when your server runs in an air-gapped or restricted environment. Uploading requires the **Upload Plugin** setting to be enabled and the **Require plugin signature** setting to be disabled.

1. Download the plugin bundle. Mattermost plugins are distributed as ``.tar.gz`` files, typically from the plugin's GitHub releases page.
2. Log in to your Mattermost System Console as a system admin.
3. Go to **Plugins > Plugin Management**.
4. In the **Upload Plugin** section, select **Choose File**, select the plugin bundle you downloaded, and then select **Upload**.
5. The plugin appears in the **Installed Plugins** list. Select **Enable** to turn it on.

Using mmctl
~~~~~~~~~~~

The :doc:`mmctl command line tool </administration-guide/manage/mmctl-command-line-tool>` is useful for scripted or remote plugin management. Plugins must be enabled in the server configuration first.

- Install the latest version from the Marketplace by plugin ID:

  .. code-block:: sh

     mmctl plugin marketplace install <id>

- Install a plugin bundle from your local computer:

  .. code-block:: sh

     mmctl plugin add myplugin.tar.gz

- Install a plugin bundle from a URL:

  .. code-block:: sh

     mmctl plugin install-url https://example.com/myplugin.tar.gz

After installing, enable the plugin by its ID:

.. code-block:: sh

   mmctl plugin enable <id>

Enable or disable a plugin
--------------------------

Installing a plugin doesn't turn it on automatically. Enable a plugin to make it available to users, and disable it to remove it from the user interface without uninstalling it.

To enable or disable a plugin in the System Console:

1. Go to **Plugins > Plugin Management**.
2. In the **Installed Plugins** list, locate the plugin.
3. Select **Enable** or **Disable**.

To enable or disable a plugin with mmctl:

.. code-block:: sh

   mmctl plugin enable <id>
   mmctl plugin disable <id>

.. note::

  Disabling a plugin immediately removes it from the user interface and logs it out of all sessions. The plugin remains installed and can be re-enabled at any time.

Configure a plugin
------------------

Most plugins have their own settings page. After a plugin is installed, go to **Plugins** in the System Console and select the plugin by name to configure it, then select **Save**. Refer to the documentation for each plugin for details on its available settings.

Update a plugin
---------------

We recommend keeping plugins up to date as new versions are released. Updates are generally seamless and don't interrupt the user experience, but you should review each plugin's release notes for compatibility considerations, and test updates in a staging environment before applying them in production.

You can update a plugin using any of the following methods:

- **Pre-packaged plugins** are upgraded automatically when the **Automatic prepackaged plugins** setting is enabled (the default). If a newer version is already installed, no change is made.
- **Marketplace plugins** show an **Update** option in the App Marketplace when a newer version is available. Select it to install the latest version.
- **Uploaded plugins** are updated by uploading a newer bundle with the same plugin ID through **Plugins > Plugin Management**. The new version overwrites the existing one.
- **mmctl** updates an installed plugin when you add a bundle that has the same plugin ID. Use the ``--force`` (``-f``) flag to overwrite the existing version:

  .. code-block:: sh

     mmctl plugin add myplugin.tar.gz --force
     mmctl plugin install-url https://example.com/myplugin.tar.gz --force

  You can also reinstall the latest Marketplace version with ``mmctl plugin marketplace install <id>``.

.. tip::

  To confirm the version currently installed, go to **Plugins > Plugin Management** and review the **Installed Plugins** list, or run ``mmctl plugin list``.

Remove a plugin
---------------

Removing a plugin disables it and uninstalls it from the server.

To remove a plugin in the System Console:

1. Go to **Plugins > Plugin Management**.
2. In the **Installed Plugins** list, locate the plugin.
3. Select **Remove**.

To remove a plugin with mmctl:

.. code-block:: sh

   mmctl plugin delete <id>

Air-gapped and restricted environments
---------------------------------------

For deployments without internet access, set **Enable remote Marketplace** to **false** so the Marketplace shows only pre-packaged and installed plugins, and install plugins by uploading the bundle directly through the System Console. See the :doc:`air-gapped deployment </deployment-guide/reference-architecture/deployment-scenarios/air-gapped-deployment>` documentation for details.

Related documentation
----------------------

- :doc:`Plugins overview </integrations-guide/plugins>` - Learn about pre-built and custom plugins.
- :doc:`Popular pre-built integrations </integrations-guide/popular-integrations>` - Browse available pre-built plugins and how to get them.
- :doc:`Plugins configuration settings </administration-guide/configure/plugins-configuration-settings>` - Review every plugin configuration setting.
- :doc:`mmctl command line tool </administration-guide/manage/mmctl-command-line-tool>` - Manage plugins from the command line.
