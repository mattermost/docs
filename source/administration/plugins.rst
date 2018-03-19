Plugins (Beta)
===============

Mattermost supports plugins, which allow users to customize and extend the platform by adding specific features.

There are three scenarios in which you would consider using a plugin:

 - When you want to customize the Mattermost user interface
 - When you want to extend Mattermost functionality to meet a specific, complex requirement
 - When you want to build integrations that are managed by your Mattermost server

There are two main types of plugins, both of which are supported in Team and Enterprise Editions:

 - **Client plugins**: Allows you to customize the Mattermost user interface, by overriding elements such as the profile popover, channel header or the sidebar. For a sample plugin, see `hovercardexample <https://github.com/jwilander/hovercardexample>`_.
 - **Server plugins**: Makes it easier to integrate with third-party systems such as JIRA, GitLab or Jenkins. A sample plugin for a video and audio call system such as Zoom and Skype for Business is currently in progress.

Later in upcoming releases, the `Enterprise Edition <https://about.mattermost.com/pricing>`_ will also support plugins that enable you to extend Mattermost functionality to meet a specific, complex requirement such as profiling performance metrics, and to implement highly customized compliance rules for `information barriers <http://www.17a-4.com/supervision-information-barriers/>`_.

Set Up Guide
--------------

To enable plugins, follow these two simple steps.

1) Go to **System Console > Plugins (Beta) > Configuration**. Here you can enable plugins and plugin uploads. If you do not plan to upload a plugin, set **Enable Plugin Uploads** to ``false`` to control which plugins are installed on your server. 
2) Go to **System Console > Plugins (Beta) > Management** to manage your plugins, including:

 - Activating or deactivating pre-packaged Mattermost plugins.
 - Upload and install a plugin for your Mattermost server, or remove them.

For more information on building your own plugin, see our `developer documentation <https://developers.mattermost.com/extend/plugins/>`_.

Plugin Uploads
~~~~~~~~~~~~~~~~~~

Mattermost supports plugin uploads by System Admins, which allow you to customize and extend the platform that would otherwise not be available. These plugins are not pre-packaged in Mattermost, and have either been developed by the community or by a Mattermost staff member.

If you don't plan to upload plugins on your server, you can disable plugin uploads anytime in **System Console > Plugins (Beta) > Configuration**. Note that disabling uploads will not disable plugins already installed on your server.

If you run your Mattermost server in `High Availability mode <https://docs.mattermost.com/deployment/cluster.html>`_, plugins need to be uploaded on all app servers.

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

