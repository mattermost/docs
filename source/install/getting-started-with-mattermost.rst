Getting Started with Mattermost is Easy
=======================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost is a secure collaboration platform that is open, flexible, and deeply integrated with the tools you love. Use Mattermost to bring your people and your processes together. Get started with Mattermost quickly by installing Mattermost using Docker or Omnibus.

.. tabs::

    .. tab:: Using Docker

        **Install Mattermost using Docker**

        You'll need `Docker Engine <https://docs.docker.com/engine/install/>`__ and `Docker Compose <https://docs.docker.com/compose/install/>`__ (release 1.28 or later).

        1. Follow the steps in the `Mattermost Docker Setup README <https://github.com/mattermost/docker#mattermost-docker-setup>`__ to install Mattermost in a production environment using Docker. 
        
        2. When Docker is done fetching the image, open ``http://localhost:8065/`` in your browser. 
        
        3. Create your first Mattermost System Admin user, `invite more users <https://docs.mattermost.com/messaging/managing-members.html>`__, and explore the Mattermost platform. 

        **Looking to explore Mattermost product functionality on a local machine instead?**
    
        You can install Mattermost in Preview Mode using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__. This Docker image installs the free, unlicensed Mattermost Enterprise version of Mattermost using the following 1-line command: 
    
        .. code-block:: none

            docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

        .. important:: 
        
            Don't use the Mattermost Docker Preview image in production environments. It uses a known password string, contains other non-production configuration settings, keeps no persistent data (all data lives inside the container), and doesn't support upgrades. 

    .. tab:: Using Omnibus

        Mattermost Omnibus is a `Debian <https://www.debian.org/>`__ package that bundles the  components of a Mattermost deployment into a single installation. The package leverages the `apt package manager <https://ubuntu.com/server/docs/package-management>`__ to install and update the platform components, and uses a custom CLI and ansible recipes to link the components together and configure them.

        Mattermost Omnibus currently supports Ubuntu's ``bionic`` and ``focal`` distributions. The package bundles the free, unlicensed Mattermost Enterprise version of Mattermost.

        **Install Mattermost using Mattermost Omnibus**

        1. Run the following command in a terminal window to configure the repositories needed for a PostgreSQL database, configure an NGINX web server to act as a proxy, configure certbot to issue and renew the SSL certificate, and configure the Mattermost Omnibus repository so that you can run the install command:

        .. code-block:: none

            curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash

        2. Run the following command to install the Omnibus package:

        .. code-block:: none

            sudo apt install mattermost-omnibus -y

        To issue the certificate, the installer requests a domain name and an email address from you. These are used to generate the certificate and deliver any related communications. After all the packages are installed, Omnibus runs ansible scripts that configure all the platform components and starts the server. 

        3. Open a browser, navigate to your Mattermost domain by domain name (e.g. ``mymattermostserver.com``), or by the server's IP address if you're not using a domain name. 

        4. Create your first Mattermost user, `invite more users <https://docs.mattermost.com/messaging/managing-members.html>`__, and explore the Mattermost platform. 

        .. note:: 
        
            We recommend installing and configuring Omnibus with SSL enabled; however, you can run the following command to disable SSL: ``sudo MMO_HTTPS=false apt install mattermost-omnibus``.

        **Update Mattermost Omnibus**

        Mattermost Omnibus is integrated with the apt package manager. When a new Mattermost version is released, run: ``sudo apt update && sudo apt upgrade`` to download and update your Mattermost instance.

Getting help
------------

If you encounter issues during your Mattermost installation, see the `Troubleshooting Mattermost Issues <https://docs.mattermost.com/install/troubleshooting.html>`__ product documentation or `join the Mattermost User Community <https://mattermost.com/community/>`__ where you can connect with thousands of contributors, customers, and users to build, share, and learn together.

Apply your license key
-----------------------

When you start a free Mattermost Enterprise trial, you'll receive a Mattermost license key by email. You can apply that license key using the System Console, using mmctl, or using the CLI.

.. note:: 
    
    You must be a Mattermost System Admin to apply the license key to your Mattermost instance. If you're not a System Admin, contact your organization's Mattermost System Admin for assistance.

.. tabs::

    .. tab:: Using System Console

        1. Go go **System Console > About > Edition and License**.
        2. Upload your license key.

        Once the key is uploaded and installed, the details of your license are displayed.

    .. tab:: Using mmctl

        Use the `mmctl license upload <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-license-upload>`__ command to upload the license key, or to replace an existing license key with a new one. 

        .. code-block:: none

            mmctl license upload [license] [flags]
        
        When complete, restart the Mattermost server. If you're running in a `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ environment, the license key must be updated to every node.

    .. tab:: Using the CLI

        .. note::

          The legacy `CLI <https://docs.mattermost.com/manage/command-line-tools.html>`__ is available for Mattermost v5.39 and earlier.
        
        Use the `mattermost license upload <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-license-upload>`__ command to to upload a new license key, or to replace an existing license key with a new one. 

        .. code-block:: none

            mattermost license upload {license}
        
        When complete, restart the Mattermost server. If you're running in a `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ environment, the new license key must be updated to every node.

Once your license key is uploaded to your Mattermost server, it's stored in your SQL database at ``mattermost.Licenses``. Verify what keys are on your server by running: ``select * from mattermost.Licenses;``.
