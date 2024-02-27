Install Mattermost Omnibus
==========================

.. raw:: html

  <div class="mm-badge mm-badge--combo">

    <div class="mm-plans-badge block">
      <p>
        <img src="../_static/images/badges/flag_icon.svg" alt="" />
        <span>Available on <a href="https://mattermost.com/pricing/">all plans</a></span>
      </p>
      <p>
        <img src="../_static/images/badges/deployment_icon.svg" alt="" />
        <span><a href="https://mattermost.com/download/">Self-hosted</a> deployments</span>
      </p>
    </div>

    <div class="mm-badge__reqs">
      <h3>Minimum system requirements:</h3>
      <ul>
        <li>Hardware: 1 vCPU/core with 2GB RAM (support for up to 1,000 users)</li>
	<li>Operating System: Ubuntu 18.04 or greater</li>
        <li>Database: PostgreSQL v11+</li>
        <li>Network ports required:
          <ul>
            <li>Application ports 80/443, TLS, TCP Inbound</li>
            <li>Administrator Console port 8065, TLS, TCP Inbound</li>
            <li>SMTP port 10025, TCP/UDP Outbound</li>
          </ul>
        </li>
      </ul>
    </div>

  </div>

.. note::

 Omnibus supports Ubuntu distributions only.

Mattermost Omnibus packages the free, unlicensed Mattermost Enterprise version of Mattermost, a PostgreSQL database, and when required, NGINX as the application proxy. A custom CLI (``mmomni``) and ansible recipes link the components together and configures them. Mattermost Omnibus is only supported on Ubuntu distributions.

Add the Mattermost PPA repositories
-----------------------------------

In a terminal window, run the following command

.. raw:: html

  <div class="mm-code-copy mm-code-copy--long" data-click-method="Omnibus" data-click-command="Add the Mattermost PPA repositories">

    <div class="mm-code-copy__wrapper">
      <code class="mm-code-copy__text mm-code-copy__trigger" data-click-el="Snippet">
        curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash
      </code>
      <span class="mm-code-copy__copied-notice">Copied to clipboard</span>
    </div>

    <button class="mm-button mm-code-copy__trigger" data-click-el="Button">
      <svg aria-hidden="true" width="17" height="18" viewBox="0 0 17 18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="0.5" y="0.5" width="10.2972" height="10.8284" rx="0.5" stroke="white"/><rect x="6.1489" y="6.41418" width="10.2972" height="10.8284" rx="0.5" stroke="white"/></svg>
      <span>Copy to clipboard<span>
    </button>

  </div>

This command configures the repositories needed for a PostgreSQL database, configures an NGINX web server to act as a proxy, configures certbot to issue and renew the SSL certificate, and configures the Mattermost Omnibus repository so that you can run the install command.

Install Mattermost Omnibus
---------------------------

In a terminal window, run the following command to install Omnibus.

.. raw:: html

  <div class="mm-code-copy" data-click-method="Omnibus" data-click-command="Install Mattermost Omnibus">

    <div class="mm-code-copy__wrapper">
      <code class="mm-code-copy__text mm-code-copy__trigger" data-click-el="Snippet">
        sudo apt install mattermost-omnibus -y
      </code>
      <span class="mm-code-copy__copied-notice">Copied to clipboard</span>
    </div>

    <button class="mm-button mm-code-copy__trigger" data-click-el="Button">
      <svg aria-hidden="true" width="17" height="18" viewBox="0 0 17 18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="0.5" y="0.5" width="10.2972" height="10.8284" rx="0.5" stroke="white"/><rect x="6.1489" y="6.41418" width="10.2972" height="10.8284" rx="0.5" stroke="white"/></svg>
      <span>Copy to clipboard<span>
    </button>

  </div>

.. note::

  We recommend installing and configuring Omnibus with SSL enabled; however, you can run the following command to disable SSL: ``sudo MMO_HTTPS=false apt install mattermost-omnibus``.

You're prompted to specify a domain name and email address to issue the certificate. This information is used to generate the certificate and deliver any related communications. After all the packages are installed, Omnibus runs ansible scripts that configure all the platform components and starts the server.

Next steps:

1. Open a browser and navigate to your Mattermost domain either by domain name (e.g. ``mymattermostserver.com``), or by the server’s IP address if you’re not using a domain name.

2. Create your first Mattermost user, invite more users, and explore the Mattermost platform.

Configure Mattermost Omnibus
-----------------------------

.. note::

  Plugin uploads, local mode, and HTTPS are enabled by default. These settings are modified in the ``yaml`` file as described below.

With Mattermost Omnibus, the Mattermost ``config.json`` file isn't used because Omnibus stores configuration in the database. The Omnibus platform itself requires a configuration of its own stored in ``/etc/mattermost/mmomni.yml``. This file contains the data that Omnibus needs to configure the platform, and connect all the services together.

You’ll need to use ``mmctl`` to make changes to your Mattermost server configuration using ``mmctl --local config edit``. See the `mmctl </manage/mmctl-command-line-tool.html#mmctl-config-edit>`__ documentation for additional command details.

For Omnibus to work properly, some configuration parameters must remain unchanged, such as the port that Mattermost uses to run.

The following parameters must be configured directly using the ``mmomni.yml`` file:

* ``db_user``: The PostgreSQL database user. This value is generated during the Omnibus installation and should not be changed.
* ``db_password``: The PostgreSQL database password. This value is generated during the Omnibus installation and should not be changed.
* ``fqdn``: The domain name for the Mattermost application. This is the value you're prompted for during the install process, and it’s used to populate the ``ServiceSettings.SiteURL`` Mattermost configuration property, as well as to retrieve and configure the SSL certificate for the server.
* ``email``: The email address used for certificate communications. This is the value you're prompted for during the install process, and it won't used if HTTPS is disabled.
* ``https``: This indicates whether the platform should be configured to use HTTPS or HTTP with values ``true`` or ``false``. The recommended way to install Mattermost is to use HTTPS, but you can disable it if necessary.
* ``data_directory``: This is the directory where Mattermost stores its data.
* ``enable_plugin_uploads``: This setting can be ``true`` or ``false``, and is used to configure the ``PluginSettings.EnableUploads`` Mattermost configuration property.
* ``enable_local_mode``: This setting can be ``true`` or ``false`` and is used to configure the ``ServiceSettings.EnableLocalMode`` Mattermost configuration property.
* ``nginx_template``: Optional path to a custom NGINX template.

After modifying the ``mmomni.yml`` configuration file, you need to run ``mmomni reconfigure`` for Omnibus to apply the changes, and then you need to restart the Mattermost server.

Update Mattermost Omnibus
-------------------------

Mattermost Omnibus is integrated with the apt package manager. When a new Mattermost version is released, run the following command to download and update your Mattermost instance:

.. raw:: html

  <div class="mm-code-copy" data-click-method="Omnibus" data-click-command="Update Mattermost Omnibus">

    <div class="mm-code-copy__wrapper">
      <code class="mm-code-copy__text mm-code-copy__trigger" data-click-el="Snippet">
        sudo apt update && sudo apt upgrade
      </code>
      <span class="mm-code-copy__copied-notice">Copied to clipboard</span>
    </div>

    <button class="mm-button mm-code-copy__trigger" data-click-el="Button">
      <svg aria-hidden="true" width="17" height="18" viewBox="0 0 17 18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="0.5" y="0.5" width="10.2972" height="10.8284" rx="0.5" stroke="white"/><rect x="6.1489" y="6.41418" width="10.2972" height="10.8284" rx="0.5" stroke="white"/></svg>
      <span>Copy to clipboard<span>
    </button>

  </div>

.. note::

  When you run the ``sudo apt upgrade`` command, mattermost-server will be updated along with any other packages. Before running the ``apt`` command, we strongly recommend stopping the Mattermost server by running the command ``sudo systemctl stop mattermost-server``.

Backup and restore
------------------

The Mattermost Omnibus CLI tool ``mmomni`` is used for both backups and restores. Server and domain migration, as well as backup and restore, is now much easier. You can take snapshots of all content in your Mattermost server. This includes all content, users, plugins, configurations, and databases. You can restore on the same server, or move to another server at any time.

To back up the contents of your Mattermost server, run the following command:

.. code-block:: sh
  :class: mm-code-block

  mmomni backup -o /tmp/mm_backup_datetime.tgz

To restore the contents of your Mattermost server, run the following two commands:

.. code-block:: sh
  :class: mm-code-block

  mmomni restore /tmp/mm_backup_datetime.tgz
  mmomni reconfigure

Remove Mattermost Omnibus
-------------------------

If you want to remove Mattermost and Mattermost Omnibus completely for any reason, you can run the following command:

.. code-block:: sh
  :class: mm-code-block

  sudo apt remove --purge mattermost mattermost-omnibus

Frequently asked questions
--------------------------

Can I use a license with Omnibus?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Mattermost Omnibus bundles the free, unlicensed Mattermost Enterprise Edition, and Enterprise features are unlocked when you purchase and upload a license.

Can I use an Omnibus server as part of a cluster?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, Omnibus is designed to be a self-contained single server Mattermost platform. It expects all the necessary components to be on the same server.

Does the SSL Certificate automatically renew?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. The SSL certificate automatically updated and renewed. Omnibus installs the certbot package to manage the certificate, and it comes with a cron job that you can find at /etc/cron.d/certbot that automatically launches the renewal process.

How do I fix an EXPKEYSIG error on upgrades?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the rare case that you encounter an ``EXPKEYSIG`` error when upgrading, this indicates that your certificate is expired. To obtain a new certificate, run the following commands:

.. code-block:: sh
  :class: mm-code-block

  sudo apt-key remove 44774B28
  sudo curl -o- https://deb.packages.mattermost.com/pubkey.gpg | sudo apt-key add -
  sudo apt update

Can I use a custom NGINX template?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Mattermost Omnibus supports using a custom NGINX template to generate its configuration.

To use this feature, you need to copy and modify the original template located at ``/opt/mattermost/mmomni/ansible/playbooks/mattermost.conf`` to a new location. Then, you can either use the variables and internal logic already bundled in the template and modify the parts that you need, or use a fully static configuration instead.

After the template has been customized, add an ``nginx_template`` property to the ``/etc/mattermost/mmomni.yml`` configuration file, and then run ``mmomni reconfigure``. The reconfigure process will use the new template to generate the NGINX final configuration. You can check the contents of the ``/etc/nginx/conf.d/mattermost.conf`` file to validate that the changes were applied successfully.

.. note::

  Please use caution when using this feature. Making changes to the custom template can cause the reconfigure process to fail, or the generated NGINX configuration to be invalid.

What ``mmomni`` commands are available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``mmomni backup``: Takes a complete snapshot of your Mattermost server and places the backup file in a specified file location.

- ``mmomni restore``: Restores specified backup file to your Mattermost server.

- ``mmomni reconfigure``: Reruns the process that changes domain, SSL, or any Omnibus-specified restrictions such as the ability to upload plugins. It also applies any changes made to the mmomni.yml configuration file.

- ``mmomni status``: Shows current status of all Omnibus components.

- ``mmomni tail``: Runs a join tail of logs of all Omnibus components.

Where can I get help?
~~~~~~~~~~~~~~~~~~~~~

If you have any problems installing Mattermost Omnibus, see the `troubleshooting guide </install/troubleshooting.html>`__ for common error messages, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`__.
