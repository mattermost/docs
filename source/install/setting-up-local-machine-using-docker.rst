..  _docker-local-machine:

Local Machine Setup using Docker 
================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The following instructions use Docker to install Mattermost in *Preview Mode* using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__ for exploring product functionality on a single local machine. 

.. important::

  This configuration shouldn't be used in production, as it uses a known password string, contains other non-production configuration settings, and doesn't support upgrades. For a production installation with Docker, see the `Mattermost Docker Setup README <https://github.com/mattermost/docker#mattermost-docker-setup>`__.

.. note::
  If you have problems installing Mattermost, see
  the `troubleshooting guide <https://docs.mattermost.com/install/troubleshooting.html>`__. For help with inviting users to your system, see `inviting team members <https://docs.mattermost.com/messaging/managing-members.html>`__ and additional `getting started information for Channels <https://docs.mattermost.com/guides/channels.htmld>`__. 
  
One-line Docker install
-----------------------

If you have Docker set up, Mattermost installs in one line:

.. code:: bash

   docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview
 
When Docker is done fetching the image, open http://localhost:8065/ in your browser.

If you don't have Docker installed, follow the step-by-step instructions below based on your operating system.

.. tabs::

  .. tab:: macOS
  
    1. Install `Docker for Mac <https://docs.docker.com/installation/mac/>`__ 

    2. Run:

      .. code:: bash

         docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview

    3. When Docker is done fetching the image, open ``http://localhost:8065/`` in your browser.
  
  .. tab:: Windows 10
  
    1. Install `Docker for Windows <https://docs.docker.com/installation/windows/>`__

    2. Run:

      .. code:: bash

         docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview

    3. When Docker is done fetching the image, open ``http://localhost:8065/`` in your browser.
  
  .. tab:: Ubuntu
  
    1. Follow the `Install Docker Engine on Ubuntu <https://docs.docker.com/installation/ubuntulinux/>`__ documentation, or follow the summary steps below:

      .. code:: bash

         sudo apt-get update
         sudo apt-get install wget
         wget -qO- https://get.docker.com/ | sh
         sudo usermod -aG docker <username>
         sudo service docker start
         newgrp docker

    2. Start Docker container:

      .. code:: bash

         docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview

    3. When Docker is done fetching the image, open ``http://localhost:8065/`` in your browser.
  
  .. tab:: Fedora
  
    1. Follow the `Install Docker Engine on Fedora <https://docs.docker.com/engine/installation/linux/fedora/>`__ documentation, or follow the summary steps below:

      .. code:: bash
      
         sudo dnf -y install dnf-plugins-core
         sudo dnf config-manager \
         --add-repo \
         https://download.docker.com/linux/fedora/docker-ce.repo
         sudo dnf install docker-ce docker-compose git # Accepting the new docker repository key
         sudo usermod -aG docker <username>
         sudo systemctl start docker
 
    2. Start Docker container: 

      .. code:: bash
      
         docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview
       
    3. When Docker is done fetching the image, open http://localhost:8065/ in your browser.
  
  .. tab:: Arch Linux
  
    To install the preview on Arch Linux, see the `installation steps <https://wiki.archlinux.org/index.php/Mattermost#With_Docker>`__ on the Arch Linux wiki.

Setting up SMTP email (Recommended) 
-----------------------------------

The default single-container Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. To see the product's full functionality, we recommend enabling SMTP email. See the `SMTP Email Setup <https://docs.mattermost.com/configure/smtp-email.html>`__ documentation for details.

Configuration Settings
----------------------

See the `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to customize your deployment.

Updating Docker Preview
-----------------------

To delete your existing Docker preview and run a new version, run the following commands: 

.. code:: bash

   docker stop mattermost-preview
   docker rm -v mattermost-preview

Accessing Your Container
------------------------

To access a shell on the container, run the following command:

.. code:: bash

   docker exec -ti mattermost-preview /bin/bash
