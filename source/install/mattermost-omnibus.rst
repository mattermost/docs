Installing Mattermost Omnibus
============================

Overview
---------

Mattermost Omnibus is a Debian package that packages the individual components of a Mattermost deployment into a single installation process. The package leverages the ``apt`` package manager to install and keep the components of the platform updated, using a custom CLI and ansible recipes to link those components together and configure them.

Mattermost Omnibus currently supports Ubuntu's ``bionic`` and ``focal`` distributions. Support for RedHat/CentOS distributions will be available in future versions. 

Prerequisites
-------------

- A clean Ubuntu server (18.04. Or 20.04)
- A domain name pointing to that server
- Root level access to the server

.. note:: 

  With Mattermost Omnibus, the ``config.json`` file no longer exists. So you’ll need to use mmctl to make changes to your Mattermost server configuration using ``mmctl config edit``. If you wish to manage your server locally, you may want to enable local mode for mmctl.

Installing Mattermost Omnibus
------------------------------

During installation you can provide an existing domain name that points to the Ubuntu server or, if you don't have one available, you can log in using the server's IP address.

.. note::
  Plugin uploads and HTTPS are enabled by default. These settings are modified in the ``yaml`` file using `mmctl config edit <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-config-edit>`__. 

The Omnibus repositories are configured using a cURL command: 

``curl -o- deb.packages.mattermost.com/repo-setup.sh | sudo bash``

This command installs and configures a ``PostgreSQL`` database, an ``nginx`` web server to act as a proxy, and ``certbot`` to issue and renew the SSL certificate. 

In order to issue that certificate, the installer requests a domain name and an email address from us. These are used to generate the certificate and deliver any related communications respectively.

Installing Omnibus Package and Mattermost Server
------------------------------------------------

If you're installing Omnibus, and have a domain and SSL use: 

``sudo apt install mattermost-omnibus``.

After all the packages are installed, Omnibus runs the ansible scripts that configure all the platform components and starts the server. To access Mattermost, open a browser, navigate to your domain, and create the System Admin user to start using the platform. 

You can also install Mattermost without a domain name or SSL (not recommended). To do this use: 

``sudo MMO_HTTPS=false apt install mattermost-omnibus``

Updating Mattermost Omnibus
-----------------------------

Mattermost Omnibus is integrated with Ubuntu’s OS's package manager. When a new Mattermost version is released, run:

``sudo apt update && sudo apt upgrade``

This downloads the latest version of Mattermost and updates your Mattermost platform. 

Removing Mattermost Omnibus
---------------------------

If you wish to remove Mattermost and Mattermost Omnibus completely for any reason, you can run this command: ``sudo apt remove --purge mattermost mattermost-omnibus``

Backup and Restore using the Mattermost Omnibus CLI
--------------------------------------------------

Mattermost Omnibus includes a CLI tool: ``mmomni``, which is used to manage configuration. 

Server and domain migration as well as backup and restore is now much easier - you can take snapshots of all content in your Mattermost server. This includes all content, users, plugins, configurations, and databases. You can restore on the same server or move to another server at any time.

Backup example:

``mmomni backup -o /tmp/Aug27-2020.tgz``

Restore example:

``mmomni restore /tmp/Aug27-2020.tgz`` and ``mmomni reconfigure``

Future releases may include automation for snapshot management.

Frequently Asked Questions (FAQs)
----------------------------------

What are the ``mmomni`` commands and what do they do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``mmomni backup``: Takes a complete snapshot of your Mattermost server and places the backup file in a specified file location.
``mmomni restore``: Restores specified backup file to your Mattermost server.
``mmomni reconfigure``: Reruns the process that changes domain, SSL, or any Omnibus-specified restrictions such as the ability to upload plugins.
``mmomni status``: Shows current status of all Omnibus components.
``mmomni tail``: Runs a join tail of logs of all Omnibus components.

Can I install without a domain?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although the recommended way to install and configure Omnibus is with SSL enabled, if you want to use or test without it, you can run: 
``sudo MMO_HTTPS=false apt install mattermost-omnibus``

What happened to ``config.json``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Omnibus does not use a file for managing server configuration settings. You can edit your config by running the following mmctl command after connecting mmctl to the instance: ``mmctl config edit``. If you are logged into the machine as the ``mattermost`` user, you can use ``mmctl --local config edit`` as well.

Are there plans to add other packages to the Omnibus?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes! We are planning several packages and currently seeking feedback to help us prioritize these.

Are there plans to support other OS distros?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes! We are currently seeking feedback to help us prioritize these.

Can I use MySQL instead of PostgreSQL?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MySQL is not supported. Omnibus is architected to run with PostgreSQL.
