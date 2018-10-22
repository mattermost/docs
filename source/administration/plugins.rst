Plugins (Beta)
===============

.. note::
  This is the admin documentation for plugins. If you're a developer looking to build a plugin, see `our developer documentation <https://developers.mattermost.com/extend/plugins>`_.

Mattermost supports plugins, which allow users to customize and extend the platform by adding specific features. See our `demo plugin <https://github.com/mattermost/mattermost-plugin-demo>`_ that demonstrates the capabilities of a Mattermost plugin. For a starting point to write a Mattermost plugin, see our `sample plugin <https://github.com/mattermost/mattermost-plugin-sample>`_.

There are three scenarios in which you would consider using a plugin:

 - When you want to customize the Mattermost user interface
 - When you want to extend Mattermost functionality to meet a specific, complex requirement
 - When you want to build integrations that are managed by your Mattermost server

There are two main types of plugins, both of which are supported in Team and Enterprise Editions:

 - **Webapp plugins (Beta)**: Allows you to customize the Mattermost user interface, by overriding elements such as the profile popover, channel header or the sidebar. For a sample plugin, see `our zoom plugin <https://github.com/mattermost/mattermost-plugin-zoom>`_.
 - **Server plugins (Release Candidate)**: Makes it easier to integrate with third-party systems such as JIRA, GitLab or Jenkins. A sample plugin for a video and audio call system with Zoom `is available here <https://github.com/mattermost/mattermost-plugin-zoom>`_. A sample plugin that auto-censors restricted words and intercepts them `is described here <https://forum.mattermost.org/t/coming-soon-apiv4-mattermost-post-intercept/4982>`_.

Later in upcoming releases, the `Enterprise Edition <https://about.mattermost.com/pricing>`_ will also support plugins that enable you to extend Mattermost functionality to meet a specific, complex requirement such as profiling performance metrics, and to implement highly customized compliance rules for `information barriers <http://www.17a-4.com/supervision-information-barriers/>`_.

For a list of available plugins, including those for auto-linking, auto-censoring and anti-virus scanning, as well as third-party plugins with JIRA, Zoom, GitHub and more, see the `Mattermost plugins repo <https://github.com/mattermost/mattermost-plugins>`_. 

Security
--------
Plugins are powerful. You should only install plugins that you've thoroughly reviewed as they have the potential to compromise the security of your installation.

Server Considerations
~~~~~~~~~~~~~~~~~~~~~
Plugins have the ability to execute arbitrary code on your server. They can do just about *anything*. For example, they could read your config file to get your database password, connect to your database, then exfiltrate sensitive user information.

Web App Considerations
~~~~~~~~~~~~~~~~~~~~~~
Plugins have the ability to execute arbitrary code in client browsers. They have the ability to perform nearly any action on behalf of anyone using the web app.

Set Up Guide
--------------

To enable plugins, follow these two simple steps.

1) Go to **System Console > Plugins (Beta) > Configuration**. Here you can enable plugins.
2) Go to **System Console > Plugins (Beta) > Management** to manage your plugins, including:

 - Activating or deactivating pre-packaged Mattermost plugins.
 - Upload and install a plugin for your Mattermost server, or remove them.

For more information on building your own plugin, see our `developer documentation <https://developers.mattermost.com/extend/plugins/>`_.

Plugin Uploads
~~~~~~~~~~~~~~~~~~

Mattermost supports plugin uploads by System Admins, which allow you to customize and extend the platform in ways that would otherwise not be available. These plugins are not pre-packaged in Mattermost, and have either been developed by the community or by a Mattermost staff member.

By default, plugin uploads are disabled on your server. To enable them, set **PluginSettings > EnableUploads** to ``true`` in your ``config.json`` file. You can disable plugin uploads anytime to control which plugins are installed on your server. This action won't disable plugins already installed on your server.

Once enabled, install plugins in one of the following ways:

1) Through System Console UI:
 - Log in to Mattermost as a System Admin.
 - Navigate to **Plugins > Management** and upload the `plugin.tar.gz` you generated above.
 - Click "Activate" under the plugin after it has uploaded.

2) Manually:
 - Extract `plugin.tar.gz` to a folder with the same name as the plugin id you specified in ``plugin.json/plugin.json``.
 - Add the plugin to the directory set by **PluginSettings > Directory** in your ``config.json`` file. If none is set, defaults to ``./plugins``.
 - Restart the Mattermost server.

If you run your Mattermost server in `High Availability mode <https://docs.mattermost.com/deployment/cluster.html>`_, plugins need to be uploaded on all app servers manually.

Once installed, your plugins directory should look similar to:

.. code-block:: none

  plugins
  ├── com.mattermost.demo-plugin
  │   ├── plugin.json
  │   ├── server
  │   │   ├── plugin-darwin-amd64
  │   │   ├── plugin-linux-amd64
  │   │   └── plugin-windows-amd64.exe
  │   └── webapp
  │       └── main.js
  ├── jira
  │   ├── plugin.exe
  │   └── plugin.yaml
  ├── zoom
  │   ├── plugin.json
  │   ├── server
  │   │   └── plugin.exe
  │   └── webapp
  │       └── zoom_bundle.js

It is recommended that you automate plugin deployment as part of your Mattermost deployment jobs.

Frequently Asked Questions (FAQ)
---------------------------------

Where can I share feedback on plugins?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can share feedback in our `forums <https://forum.mattermost.org>`_ by creating a new forum post or by replying to `our open issue <https://forum.mattermost.org/t/mattermost-plugins-in-beta/4123>`_.

All feedback is highly welcome!

Troubleshooting
-----------------

Plugin uploads fail even though uploads are enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If plugin uploads fail and you see "permissions denied" errors in **System Console > Logs**  such as 

.. code-block:: text

  [2017/11/13 20:42:18 UTC] [EROR] failed to start up plugins: mkdir /home/ubuntu/mattermost/client/plugins: permission denied

you don't have proper permissions for uploading plugins. To resolve it, apply write access to the ``mattermost/client`` directory.

Another potential cause is that the working directory for the service running Mattermost is not correct. On Ubuntu you might see

.. code-block:: text

    [2018/01/03 08:34:47 EST] [EROR] failed to start up plugins: mkdir ./client/plugins: no such file or directory

This can be fixed on Ubuntu 16.04 and RHEL by opening the service configuration file and setting WorkingDirectory to the path to Mattermost, often ``/opt/mattermost``.

Or on Windows

.. code-block:: text

    [EROR] failed to start up plugins: mkdir ./client/plugins: The system cannot find the path specified.

To fix this, set the AppDirectory of your service using ``nssm set mattermost AppDirectory c:\mattermost``.

