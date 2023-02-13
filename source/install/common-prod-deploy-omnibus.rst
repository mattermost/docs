:orphan:
:nosearch:
.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Mattermost bundles the components of a Mattermost deployment into a single installation, called **Omnibus**. Mattermost Omnibus currently supports Ubuntu's ``bionic`` (18.04), ``focal`` (20.04) and ``jammy`` (22.04) distributions. The package bundles the free, unlicensed Mattermost Enterprise version of Mattermost, and leverages the `apt package manager <https://ubuntu.com/server/docs/package-management>`__ to install and update the platform components. A custom CLI and ansible recipes link the components together and configures them.

**Minimum system requirements**

- Hardware: 2 vCPUs/cores with 4GB RAM (support for 1,000-2,000 users)
- Database: MySQL v8+ or PostgreSQL v12+
- Network ports required: 

  - Application ports 80/443, TLS, TCP Inbound
  - Administrator Console port 8065, TLS, TCP Inbound
  - SMTP port 10025, TCP/UDP Outbound

**Deploy Omnibus**

1. In a terminal window, run the following command to configure the repositories needed for a PostgreSQL database, configure an NGINX web server to act as a proxy, configure certbot to issue and renew the SSL certificate, and configure the Mattermost Omnibus repository so that you can run the install command.

   .. code-block:: none

    curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash

2. Install the Omnibus package.

   .. code-block:: none

    sudo apt install mattermost-omnibus -y

  To issue the certificate, the installer requests a domain name and an email address from you. These are used to generate the certificate and deliver any related communications. After all the packages are installed, Omnibus runs ansible scripts that configure all the platform components and starts the server. 

    .. note::

      If you encounter ``EXPKEYSIG``, this indicates that the certificate is expired. To obtain a new certificate, run the following commands:

       .. code-block:: none

        sudo apt-key remove 44774B28
        sudo curl -o- https://deb.packages.mattermost.com/pubkey.gpg | sudo apt-key add -
        sudo apt update

3. Open a browser and navigate to your Mattermost domain either by domain name (e.g. ``mymattermostserver.com``), or by the server's IP address if you're not using a domain name. 

4. Create your first Mattermost user, `invite more users </channels/manage-channel-members.html>`__, and explore the Mattermost platform. 

   .. note:: 

    We recommend installing and configuring Omnibus with SSL enabled; however, you can run the following command to disable SSL: ``sudo MMO_HTTPS=false apt install mattermost-omnibus``.

Update Mattermost Omnibus
-------------------------

Mattermost Omnibus is integrated with the apt package manager. When a new Mattermost version is released, run: ``sudo apt update && sudo apt upgrade`` to download and update your Mattermost instance.
