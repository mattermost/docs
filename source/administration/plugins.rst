Plugins (Beta)
===============

.. note::
  This is the admin documentation for plugins. If you're a developer looking to build a plugin, see `our developer documentation <https://developers.mattermost.com/extend/plugins/>`__.

Mattermost supports plugins to customize and extend the platform. See our `demo plugin <https://github.com/mattermost/mattermost-plugin-demo>`__ that illustrates the potential for a Mattermost plugin. To start writing your own plugin, consult our `starter template <https://github.com/mattermost/mattermost-plugin-starter-template>`__.

Consider using a plugin in the following scenarios:

 - When you want to customize the Mattermost user interface.
 - When you want to extend Mattermost functionality to meet a specific, complex requirement.
 - When you want to build integrations that are managed by your Mattermost server.

Plugins are fully supported in both Team Edition and Enterprise Edition.

Plugin Marketplace
------------------

The Plugin Marketplace is a collection of plugins that can greatly increase the value and capabilities of your Mattermost deployment. End users can see increased productivity through quick access to systems such as Jira, Zoom, Webex, and GitHub. Mattermost Admins can discover new plugins and quickly deploy them to their servers, including High Availability clusters. 

The Plugin Marketplace is available from v5.16 and is accessed via **Main Menu > Plugin Marketplace**. More listings will be added as we add new features and plugins that our customers request.

.. image:: https://user-images.githubusercontent.com/915956/66891467-1b18eb80-ef9e-11e9-9de3-37a3c5899bd8.png

Plugin labels
~~~~~~~~~~~~~

Plugins in the Plugin Marketplace are labeled to make it easier for administrators to choose plugins that fit their company's security and risk policies if they do not allow for community plugins to be used.

**Community Plugins**

Plugins identified as "Community" are produced by the open-source community or partners and the features/roadmap are not controlled directly by Mattermost. Prior to being listed on the Plugin Marketplace, they are reviewed by the Mattermost development team and code-signed to ensure the code Mattermost reviewed, is delivered. Mattermost does not directly support these plugins in production environments.

**Beta Plugins**

Plugins may be labeled as "Beta" if they're released to the Plugin Marketplace early for customer previews. We do not recommend running Beta plugins on production servers.

Installing a plugin
~~~~~~~~~~~~~~~~~~~

When a new plugin becomes available on the Plugin Marketplace, it's listed with an option to **Install**. Select **Install** to download and install the latest plugin binary from its respective GitHub repository. If there's a cluster present, the plugin will be distributed to each server automatically.

Configuring and enabling a plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once a plugin is installed (or pre-installed if shipped with Mattermost binary release):

1. Select **Configure** to open the **Settings** menu.
2. Enter the plugin settings as required.
3. Set **Enable Plugin** setting to ``True``. If this flag is not enabled, the plugin will not become active.
4. Test out the plugin as needed.

Upgrading plugins
~~~~~~~~~~~~~~~~~

Upgrade a plugin on demand when a new version becomes available. New versions of plugins that you have already installed will display a link to easily install the upgraded plugins. Some plugin versions may have breaking changes; please check the release notes if you are performing a major version change.

Upgrading plugins (prior to v5.18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In v5.16 and v5.17 the Plugin Marketplace only supports the installation of new plugins. To upgrade a plugin, you need to manually update it by downloading the binary file from the GitHub repository and then upload it in **System Console > Plugin Management**.

Marketplace server
------------------

There are two settings in **System Console > Plugin Management**:

.. image:: https://user-images.githubusercontent.com/915956/66892854-94660d80-efa1-11e9-805c-a85223d43a07.png

- **Enable Marketplace:** Turns the Plugin Marketplace user interface on or off for System Administrators (end users cannot see the Plugin Marketplace).
- **Marketplace URL:** The location of the Marketplace server to query for new plugins. Mattermost hosts a Plugin Marketplace for the community and this is the default value for this field. You can also set up your own Marketplace server.

When you first access the Marketplace, your Mattermost server will attempt to contact the Mattermost Plugin Marketplace server and return a list of available plugins that are appropriate based on the server version that is currently running. Only your server version and search query is passed over to the Mattermost Plugin Marketplace; we retain an anonymized record for product analytics whenever a new plugin is installed, unless you have opted out of `Telemetry <https://docs.mattermost.com/administration/telemetry.html>`__.

The `Plugin Marketplace server code <https://github.com/mattermost/mattermost-marketplace>`__ is available as an open source project and can be used to set up your own private Marketplace if desired.

Mattermost Marketplace
~~~~~~~~~~~~~~~~~~~~~~~

The `Mattermost Plugin Marketplace <https://github.com/mattermost/mattermost-marketplace>`__ is a service run by Mattermost that contains listings of plugins that we have reviewed and, in many cases, built. In the future, we plan to include community-developed plugins that will be labeled separately to Mattermost-developed plugins. as well as settings that would restrict which types of plugins you can install. Comments in our forum are welcome as we develop this feature further.

Mattermost integration directory
--------------------------------

There are many ways to integrate Mattermost aside from plugins, and we have created a directory of integration "recipes", some of which are scripts, plugins, or instructions on how to connect Mattermost with your Enterprise systems. Many are sourced from our community of customers. You can browse the directory at `https://integrations.mattermost.com/ <https://integrations.mattermost.com/>`__.

About plugins
-------------

Plugins may have one or both of the following parts:

 - **Web App plugins:** Customize the Mattermost user interface by adding buttons to the channel header, overriding the ``RHS``, or even rendering a custom post type within the center channel. All this is possible without having to fork the source code and rebase on every Mattermost release. For a sample plugin, see `our Zoom plugin <https://github.com/mattermost/mattermost-plugin-zoom>`__.
 - **Server plugins:** Run a Go process alongside the server, filtering messages, or integrating with third-party systems such as Jira, GitLab, or Jenkins. For a sample plugin, see `our Jira plugin <https://github.com/mattermost/mattermost-plugin-jira>`__.

Security
--------

Plugins are intentionally powerful and not artificially sandboxed in any way and effectively become part of the Mattermost server. Server plugins can execute arbitrary code alongside your server and webapp plugins can deploy arbitrary code in client browsers.

While this power enables deep customization and integration, it can be abused in the wrong hands. Plugins have full access to your server configuration and thus also to your Mattermost database. Plugins can read any message in any channel, or perform any action on behalf of any user in the Web App.

You should only install custom plugins from sources you trust to avoid compromising the security of your installation.

Plugin signing
--------------

The Plugin Marketplace allows system administrators to download and install plugins from a central repository. Plugins installed via the Plugin Marketplace must be signed by a public key certificate trusted by the local Mattermost server.

While the server ships with a default certificate used to verify plugins from the default Mattermost Plugin Marketplace, the server can be configured to trust different certificates and point at a different plugin marketplace. This document outlines the steps for generating a public key certificate and signing plugins for use with a custom plugin marketplace. It assumes access to the `GNU Privacy Guard (GPG) <https://gnupg.org>`__ tool.

Configuration
~~~~~~~~~~~~~

Configuring plugin signatures allows finer control over the verification process:

.. code-block:: sh

   PluginSettings.RequirePluginSignature = true

This is used to enforce plugin signature verification. With flag on, only Marketplace plugins will be installed and verified. With flag off, customers will be able to install plugins manually without signature verification.

Note that the Marketplace plugins will still be verified even if the flag is off.

Key generation
~~~~~~~~~~~~~~~

Public and private key pairs are needed to sign and verify plugins. The private key is used for signing and should be kept in a secure location. The public key is used for verification and can be distributed freely. To generate a key pair, run the following command:

.. code-block:: sh

   gpg --full-generate-key

.. code-block:: text

  Please select what kind of key you want:
    (1) RSA and RSA (default)
    (2) DSA and Elgamal
    (3) DSA (sign only)
    (4) RSA (sign only)
  Your selection? 1

  RSA keys may be between 1024 and 4096 bits long.
  What keysize do you want? (2048) 3072

  Requested keysize is 3072 bits

  Please specify how long the key should be valid.
        0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
  Key is valid for? (0) 0

  Key expires at ...

  Is this correct? (y/N) y

  GnuPG needs to construct a user ID to identify your key.
  Real name: Mattermost Inc

  Email address: info@mattermost.com
  Comment:

  You selected this USER-ID:
      "Mattermost Inc <info@mattermost.com>"
  Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O

.. note::

 Key size should be at least 3072 bits.

Exporting the private key
~~~~~~~~~~~~~~~~~~~~~~~~~

Find the ID of your private key first. The ID is a hexadecimal number.

.. code-block:: sh

  gpg --list-secret-keys

This is your private key and should be kept secret. Your hexadecimal key ID will, of course, be different.

.. code-block:: sh

  gpg --export-secret-keys F3FACE45E0DE642C8BD6A8E64C7C6562C192CC1F > ./my-priv-key

Exporting the public key
~~~~~~~~~~~~~~~~~~~~~~~~

Find the ID of your public key first. The ID is a hexadecimal number.

.. code-block:: sh

  gpg --list-keys

.. code-block:: sh

  gpg --export F3FACE45E0DE642C8BD6A8E64C7C6562C192CC1F > ./my-pub-key

Importing the key
~~~~~~~~~~~~~~~~~

If you already have a public and private key pair, you can import them to the GPG.

.. code-block:: sh

 gpg --import ./my-priv-gpg-key

 gpg --import ./my-pub-gpg-key

Running plugin signing
^^^^^^^^^^^^^^^^^^^^^^

For plugin signing, you have to know the hexadecimal ID of the private key. Let's assume you want to sign ``com.mattermost.demo-plugin-0.1.0.tar.gz`` file, run:

.. code-block:: sh

  gpg -u F3FACE45E0DE642C8BD6A8E64C7C6562C192CC1F --verbose --personal-digest-preferences SHA256 --detach-sign com.mattermost.demo-plugin-0.1.0.tar.gz

This command will generate ``com.mattermost.demo-plugin-0.1.0.tar.gz.sig``, which is the signature of your plugin.

Plugin verification
^^^^^^^^^^^^^^^^^^^

Mattermost server will verify plugin signatures downloaded from the Plugin Marketplace. To add custom public keys, run the following command on the Mattermost server:

.. code-block:: sh

  mattermost plugin add key my-pub-key

Multiple public keys can be added to the Mattermost server:

.. code-block:: sh

  mattermost plugin add key my-pk-file1 my-pk-file2

To list the names of all public keys installed on your Mattermost server, use:

.. code-block:: sh

  mattermost plugin keys

To delete public key(s) from your Mattermost server, use:

.. code-block:: sh

  mattermost plugin delete key my-pk-file1 my-pk-file2

Implementation
~~~~~~~~~~~~~~

See the `implementation document <https://docs.google.com/document/d/1qABE7VEx4k_ZAeh6Ydn4pGbu6BQfZt65x68i2s65MOQ>`__ for more information.

Set up guide
------------

To manage plugins, go to **System Console > Plugins > Plugin Management**. From here, you can:

 - Enable or disable pre-packaged plugins.
 - Install and manage custom plugins.

.. note::

  In versions prior to 5.16, go to **System Console > Plugins (Beta) > Configuration**.

Pre-packaged plugins
~~~~~~~~~~~~~~~~~~~~

Mattermost ships with a number of pre-packaged plugins written and maintained by Mattermost. Instead of building these features directly into the product, you can selectively enable the functionality your installation requires. Install pre-packaged plugins from the Plugin Marketplace, even if your system cannot directly connect to the internet.

Prior to v5.20, pre-packaged plugins were installed by default and could not be uninstalled without manually modifying the ``prepackaged_plugins`` directory. Any pre-packaged plugins installed prior to v5.20 and left enabled on upgrade will remain installed, but can now be uninstalled.

Custom plugins
~~~~~~~~~~~~~~

Installing a custom plugin introduces some risk. As a result, plugin uploads are disabled by default and cannot be enabled via the System Console or REST API.

To enable plugin uploads, manually set ``PluginSettings > EnableUploads`` to ``true`` in your ``config.json`` file and restart your server. You can disable plugin uploads at any time without affecting previously uploaded plugins.

With plugin uploads enabled, navigate to **System Console > Plugins > Management** and upload a plugin bundle. Plugin bundles are ``*.tar.gz`` files containing the server executables and web app resources for the plugin. You can also specify a URL to install a plugin bundle from a remote source.

.. note:: 

  When ``RequirePluginSignature`` is ``true``, plugin uploads cannot be enabled, and may only be installed via the Plugin Marketplace (which verifies Plugin Code Signatures).

Custom plugins may also be installed via the `command line interface <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-plugin>`__.

While no longer recommended, plugins may also be installed manually by unpacking the plugin bundle inside the ``plugins`` directory of a Mattermost installation.

Plugin uploads in High Availability mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior to Mattermost 5.14, Mattermost servers configured for `High Availability mode <https://docs.mattermost.com/deployment/cluster.html>`_ required plugins to be installed manually. As of Mattermost 5.14, plugins uploaded via the System Console or the command line interface are persisted to the configured file store and automatically installed on all servers that join the cluster.

Manually installed plugins remain supported, but must be individually installed on each server in the cluster.

Frequently Asked Questions (FAQs)
---------------------------------

Where can I share feedback on plugins?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Join our community server discussion in the `Toolkit channel <https://community.mattermost.com/core/channels/developer-toolkit>`__.

Troubleshooting
---------------

Please see common questions below. For further assistance, review the `Troubleshooting forum <https://forum.mattermost.org/c/trouble-shoot>`__ for previously reported errors, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`_.

Plugin uploads fail even though uploads are enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If plugin uploads fail and you see ``permission denied`` errors in **System Console > Logs** such as:

.. code-block:: text

  [2017/11/13 20:42:18 UTC] [EROR] failed to start up plugins: mkdir /home/ubuntu/mattermost/client/plugins: permission denied

It's likely that the Mattermost server doesn't have the necessary permissions for uploading plugins. Ensure the Mattermost server has write access to the ``mattermost/client`` directory.

It may also be that the working directory for the service running Mattermost is not correct. On Ubuntu you might see:

.. code-block:: text

    [2018/01/03 08:34:47 EST] [EROR] failed to start up plugins: mkdir ./client/plugins: no such file or directory

This can be fixed on Ubuntu 16.04 and RHEL by opening the service configuration file and setting ``WorkingDirectory`` to the path to Mattermost (generally it's ``/opt/mattermost``).

A similar problem can occur on Windows:

.. code-block:: text

    [EROR] failed to start up plugins: mkdir ./client/plugins: The system cannot find the path specified.

To fix this, set the ``AppDirectory`` of your service using ``nssm set mattermost AppDirectory c:\mattermost``.

``x509: certificate signed by unknown authority``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're seeing ``x509: certificate signed by unknown authority`` in your server logs, it usually means that the CA for a self-signed certificate for a server your plugin is trying to access has not been added to your local trust store of the machine the Mattermost server is running on.

You can add one in Linux `following instructions in this StackExchange article <https://unix.stackexchange.com/questions/90450/adding-a-self-signed-certificate-to-the-trusted-list>`_, or set up a load balancer like NGINX per :doc:`production install guide <config-ssl-http2-nginx>` to resolve the issue.
