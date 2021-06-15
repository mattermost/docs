Installing Mattermost Omnibus
=============================

Overview
---------

Mattermost Omnibus is a Debian package that packages the individual components of a Mattermost deployment into a single installation process. The package leverages the ``apt`` package manager to install and keep the components of the platform updated, using a custom CLI and ansible recipes to link those components together and configure them.

Mattermost Omnibus currently supports Ubuntu's ``bionic`` and ``focal`` distributions. Support for RedHat/CentOS distributions will be available in future versions. The package bundles the free, unlicensed Mattermost Enterprise Edition.

Prerequisites
-------------

- A clean Ubuntu server (18.04 or 20.04)
- A domain name pointing to that server
- Root level access to the server

Configuring Mattermost Omnibus Repositories
-------------------------------------------

The Omnibus repositories are configured using a cURL command:

``curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash``

This command configures the repositories needed for a ``PostgreSQL`` database, an ``nginx`` web server to act as a proxy, and ``certbot`` to issue and renew the SSL certificate. It also configures the Mattermost Omnibus repository so that you can run the install command.

Installing Mattermost Omnibus
-----------------------------

If you're installing Omnibus, and have a domain and SSL use:

``sudo apt install mattermost-omnibus -y``

In order to issue that certificate, the installer requests a domain name and an email address from you. These are used to generate the certificate and deliver any related communications respectively.

After all the packages are installed, Omnibus runs the ansible scripts that configure all the platform components and starts the server. To access Mattermost, open a browser, navigate to your domain, and create the System Admin user to start using the platform.

Updating Mattermost Omnibus
---------------------------

Mattermost Omnibus is integrated with the ``apt`` package manager. When a new Mattermost version is released, run:

``sudo apt update && sudo apt upgrade``

This downloads the latest version of Mattermost and updates your Mattermost platform.

Configuring Mattermost Omnibus
-------------------------------

.. note::
  
  Plugin uploads, local mode, and HTTPS are enabled by default. These settings are modified in the ``yaml`` file as described below.

With Mattermost Omnibus, the ``config.json`` file is no longer used as `Omnibus stores the Mattermost configuration in the database <https://docs.mattermost.com/administration/config-in-database.html>`__. The Omnibus platform itself requires of a configuration of its own, that is stored in ``/etc/mattermost/mmomni.yml``. This file contains the data that Omnibus needs to configure the platform and connect all the services together. So you’ll need to use mmctl to make changes to your Mattermost server configuration using ``mmctl --local config edit``.

For Omnibus to work properly, there are some configuration parameters that are fixed and cannot be changed through the web interface - for example, the port that Mattermost uses to run. Other parameters need to be configured directly in the ``mmomni.yml`` file instead of in the Mattermost web interface or the ``config.json`` file.

The properties that you can configure in this file are:

- ``db_user``: The PostgreSQL database user. This value is generated during the Omnibus installation and should not be changed.
- ``db_password``: The PostgreSQL database password. This value is generated during the Omnibus installation and should not be changed.
- ``fqdn``: The domain name for the Mattermost application. This is the value that is asked during the install process, and it’s used to populate the ``ServiceSettings.SiteURL`` Mattermost configuration property, as well as to retrieve and configure the SSL certificate for the server.
- ``email``: The email address used for certificate communications. This is the value that is asked during the install process, and it will not be used if HTTPS is disabled.
- ``https``: This indicates whether the platform should be configured to use HTTPS or HTTP with values ``true`` or ``false``. The recommended way to install Mattermost is to use HTTPS, but you can disable it if required.
- ``data_directory``: This is the directory where Mattermost stores its data.
- ``enable_plugin_uploads``: This setting can be ``true`` or ``false`` and is used to configure the ``PluginSettings.EnableUploads`` Mattermost configuration property.
- ``enable_local_mode``: This setting can be ``true`` or ``false`` and is used to configure the ``ServiceSettings.EnableLocalMode`` Mattermost configuration property.
- ``nginx_template``: Optional path to a custom NGINX template.

After modifying the ``mmomni.yml`` configuration file, you need to run ``mmomni reconfigure`` for Omnibus to apply the changes and restart Mattermost.

Using a custom NGINX template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Omnibus generates an ``nginx`` configuration depending on how the different properties of the ``mmomni.yml`` file are set. However, you may need to customize the configuration further to support other use cases, such as using custom SSL certificates. For those cases, Omnibus supports using a custom ``nginx`` template to generate its configuration. 

To use this feature, you need to copy and modify the original template located at ``/opt/mattermost/mmomni/ansible/playbooks/mattermost.conf`` to a new location. Then, you can either use the variables and internal logic already bundled in the template and modify the parts that you need, or use a fully static configuration instead.

After the template has been customized, add an ``nginx_template`` property to the ``/etc/mattermost/mmomni.yml`` configuration file, and then run ``mmomni reconfigure``. The reconfigure process will use the new template to generate the NGINX final configuration. You can check the contents of the ``/etc/nginx/conf.d/mattermost.conf`` file to validate that the changes were applied successfully.

Please be careful when using this feature, as making changes to the custom template can cause the reconfigure process to fail, or the generated NGINX configuration to be invalid.

This feature is available from Mattermost Omnibus version 5.32.0.

Removing Mattermost Omnibus
---------------------------

If you wish to remove Mattermost and Mattermost Omnibus completely for any reason, you can run this command:

``sudo apt remove --purge mattermost mattermost-omnibus``

Backup and Restore using the Mattermost Omnibus CLI
---------------------------------------------------

Mattermost Omnibus includes a CLI tool: ``mmomni``, which is used to manage configuration.

Server and domain migration as well as backup and restore is now much easier - you can take snapshots of all content in your Mattermost server. This includes all content, users, plugins, configurations, and databases. You can restore on the same server or move to another server at any time.

Backup example:

``mmomni backup -o /tmp/Aug27-2020.tgz``

Restore example:

``mmomni restore /tmp/Aug27-2020.tgz`` and ``mmomni reconfigure``

Future releases may include automation for snapshot management.

Frequently Asked Questions (FAQs)
---------------------------------

What are the ``mmomni`` commands and what do they do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``mmomni backup``: Takes a complete snapshot of your Mattermost server and places the backup file in a specified file location.
- ``mmomni restore``: Restores specified backup file to your Mattermost server.
- ``mmomni reconfigure``: Reruns the process that changes domain, SSL, or any Omnibus-specified restrictions such as the ability to upload plugins. It also applies any changes made to the ``mmomni.yml`` configuration file.
- ``mmomni status``: Shows current status of all Omnibus components.
- ``mmomni tail``: Runs a join tail of logs of all Omnibus components.

Can I install without a domain?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although the recommended way to install and configure Omnibus is with SSL enabled, if you want to use or test without it, you can run:

``sudo MMO_HTTPS=false apt install mattermost-omnibus``

What happened to ``config.json``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Omnibus `stores the configuration of the Mattermost server into the database <https://docs.mattermost.com/administration/config-in-database.html>`__. You can edit your config by running the following mmctl command after connecting mmctl to the instance: ``mmctl config edit``. If you're logged into the machine as the ``mattermost`` user, you can use ``mmctl --local config edit`` as well.

Are there plans to add other packages to the Omnibus?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! We are planning several packages and currently seeking feedback to help us prioritize these.

Are there plans to support other OS distros?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! We are currently seeking feedback to help us prioritize these.

Can I use MySQL instead of PostgreSQL?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MySQL is not supported. Omnibus is architected to run with PostgreSQL.

Can I use a license with Omnibus?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Mattermost Omnibus bundles the free, unlicensed Mattermost Enterprise Edition, and Enterprise features are unlocked when you purchase and upload a license.

Can I use an Omnibus server as part of a cluster?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, Omnibus is designed to be a self-contained Mattermost platform, so it expects all the necessary components to be in the same server.

Where can I get help?
~~~~~~~~~~~~~~~~~~~~~

If you have any problems installing Mattermost Omnibus, see the `troubleshooting guide <https://docs.mattermost.com/install/troubleshooting.html>`__ for common error messages, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`_.
