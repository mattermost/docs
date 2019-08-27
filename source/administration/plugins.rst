Plugins (Beta)
===============

.. note::
  This is the admin documentation for plugins. If you're a developer looking to build a plugin, see `our developer documentation <https://developers.mattermost.com/extend/plugins>`__.

Mattermost supports plugins to customize and extend the platform. See our `demo plugin <https://github.com/mattermost/mattermost-plugin-demo>`__ that illustrates the potential for a Mattermost plugin. To start writing your own plugin, consult our `starter template <https://github.com/mattermost/mattermost-plugin-starter-template>`__.

Consider using a plugin in the following scenarios:

 - When you want to customize the Mattermost user interface
 - When you want to extend Mattermost functionality to meet a specific, complex requirement
 - When you want to build integrations that are managed by your Mattermost server

Plugins are fully supported by both Team and Enterprise Editions. Plugins may have one or both of the following parts:

 - **Webapp plugins (Beta)**: Customize the Mattermost user interface by adding to the channel header, overriding the ``RHS``, or even rendering a custom post type. All this is possible without having to fork the source code and rebase on every Mattermost release. For a sample plugin, see `our Zoom plugin <https://github.com/mattermost/mattermost-plugin-zoom>`__.
 - **Server plugins (Release Candidate)**: Run a Go process alongside the server, filtering messages or integrating with third-party systems such as Jira, GitLab or Jenkins. For a sample plugin, see `our Jira plugin <https://github.com/mattermost/mattermost-plugin-jira>`__.

Browse available plugins at `https://integrations.mattermost.com/ <https://integrations.mattermost.com/>`__.

Security
--------
Plugins are intentionally powerful and not artificially sandboxed in any way. Server plugins can execute arbitrary code alongside your server. Webapp plugins can deploy arbitrary code in client browsers. Plugins effectively become part of the Mattermost server.

While this power enables deep customization and integration, it can be abused in the wrong hands. Plugins have full access to your server configuration and thus also to your Mattermost database. Plugins can read any message in any channel, or perform any action on behalf of any user in the webapp.

You should only install custom plugins from sources you trust to avoid compromising the security of your installation.

Set Up Guide
------------

To manage plugins, go to **System Console > Plugins > Plugin Management**. From here, you can:

 - Enable or disable pre-packaged plugins
 - Install and manage custom plugins

.. note::
  In prior versions, go to **System Console > Plugins (Beta) > Configuration**.


Pre-packaged Plugins
~~~~~~~~~~~~~~~~~~~
Mattermost ships with a number of pre-packaged plugins written and maintained by Mattermost. Instead of building these features directly into the product, you can selectively enable the functionality your installation requires. Pre-packaged plugins cannot be removed via the System Console, but can be customized by modifying the ``prepackaged_plugins`` directory in your Mattermost installation.

Custom Plugins
~~~~~~~~~~~~~~
As noted above, installing a custom plugin introduces some risk. As a result, plugin uploads are disabled by default and cannot be enabled via the System Console or REST API.

To enable plugin uploads, manually set **PluginSettings > EnableUploads** to ``true`` in your configuration and restart your server. You can disable plugin uploads at any time without affecting previously uploaded plugins.

With plugin uploads enabled, navigate to **System Console > Plugins > Management** and upload a plugin bundle. Plugin bundles are ``*.tar.gz`` files containing the server executables and webapp resources for the plugin. You may also specify a URL to install a plugin bundle from a remote source.

Custom plugins may also be installed via the `command line interface <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-plugin>`__.

While no longer recommended, plugins may also be installed manually by unpacking the plugin bundle inside the `plugins` directory of a Mattermost installation.

Plugin Uploads in High Availability Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prior to Mattermost 5.14, Mattermost servers configured for `High Availability mode <https://docs.mattermost.com/deployment/cluster.html>`_ required plugins to be installed manually. As of Mattermost 5.14, plugins uploaded via the System Console or the command line interface are persisted to the configured file store and automatically installed on all servers that join the cluster. 

Manually installed plugins remain supported, but must be installed on each server in the cluster.

Frequently Asked Questions (FAQ)
---------------------------------

Where can I share feedback on plugins?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Join our community server discussion in the `Toolkit channel <https://community.mattermost.com/core/channels/developer-toolkit>`__.

Troubleshooting
-----------------

Plugin uploads fail even though uploads are enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If plugin uploads fail and you see "permissions denied" errors in **System Console > Logs**  such as 

.. code-block:: text

  [2017/11/13 20:42:18 UTC] [EROR] failed to start up plugins: mkdir /home/ubuntu/mattermost/client/plugins: permission denied

the Mattermost server doesn't have the necessary permissions for uploading plugins. Ensure the Mattermost server has write access to the ``mattermost/client`` directory.

It may also be the case that the working directory for the service running Mattermost is not correct. On Ubuntu you might see

.. code-block:: text

    [2018/01/03 08:34:47 EST] [EROR] failed to start up plugins: mkdir ./client/plugins: no such file or directory

This can be fixed on Ubuntu 16.04 and RHEL by opening the service configuration file and setting WorkingDirectory to the path to Mattermost, often ``/opt/mattermost``.

A similar problem can occur on Windows:

.. code-block:: text

    [EROR] failed to start up plugins: mkdir ./client/plugins: The system cannot find the path specified.

To fix this, set the AppDirectory of your service using ``nssm set mattermost AppDirectory c:\mattermost``.

``x509: certificate signed by unknown authority``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are seeing ``x509: certificate signed by unknown authority`` in your server logs, it usually means that your self-signed certificate hasn't been added to your local trusted CA of the Mattermost server.

You can add one in Linux `following instructions in this StackExchange article <https://unix.stackexchange.com/questions/90450/adding-a-self-signed-certificate-to-the-trusted-list>`_, or set up a load balancer like NGINX per :doc:`production install guide <config-ssl-http2-nginx>` to resolve the issue.
