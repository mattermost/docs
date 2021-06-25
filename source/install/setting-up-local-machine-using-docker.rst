..  _docker-local-machine:

Local Machine Setup using Docker 
================================

The following instructions use Docker to install Mattermost in *Preview Mode* for exploring product functionality on a single machine. 

**Note:** This configuration should not be used in production, as it uses a known password string, contains other non-production configuration settings, and does not support upgrade. 

If you're looking for a production installation with Docker, please see the `Mattermost Production Docker Deployment Guide <https://docs.mattermost.com/install/prod-docker.html>`__.

.. note::
  If you have any problems installing Mattermost, see
  the `troubleshooting guide <https://docs.mattermost.com/install/troubleshooting.html>`__. For help with inviting users to your system, see `inviting team members <https://docs.mattermost.com/help/getting-started/managing-members.html#inviting-team-members>`__ and other `getting started information <https://docs.mattermost.com/guides/user.html#getting-started>`__. To submit an improvement or correction, click  **Edit** at the top of this page.
  
One-line Docker Install
-----------------------

If you have Docker set up, Mattermost installs in one-line:

   .. code:: bash

       docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview
 
When Docker is done fetching the image, open http://localhost:8065/ in your browser.

Otherwise, follow the step-by-step instructions:

macOS
~~~~~

1. Install `Docker for Mac <https://docs.docker.com/installation/mac/>`__ 

2. Run:
   ``docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview``

3. When Docker is done fetching the image, open ``http://localhost:8065/``
   in your browser.


Windows 10
~~~~~~~~~~

1. Install `Docker for Windows <https://docs.docker.com/installation/windows/>`__

2. Run:
   ``docker run --name mattermost-preview -d --publish 8065:8065 --add-host dockerhost:127.0.0.1 mattermost/mattermost-preview``

3. When Docker is done fetching the image, open ``http://localhost:8065/``
   in your browser.

Ubuntu
~~~~~~

1. Follow the instructions at
   https://docs.docker.com/installation/ubuntulinux/ or use the summary
   below:

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

3. When Docker is done fetching the image, open ``http://localhost:8065/``
   in your browser.

Fedora
~~~~~~

1. Follow the instructions at https://docs.docker.com/engine/installation/linux/fedora/ or use the summary below:

   ..  code:: bash
      
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

Arch Linux
~~~~~~~~~~

To install the preview on Arch Linux, see the `installation guide <https://wiki.archlinux.org/index.php/Mattermost#With_Docker>`__ on the Arch Linux wiki.

Setting up SMTP Email (Recommended) 
-----------------------------------

The default single-container Docker instance for Mattermost is designed
for product evaluation, and sets ``SendEmailNotifications=false`` so the
product can function without enabling email. To see the product's full
functionality, enabling SMTP email is recommended.

.. include:: smtp-email-setup.rst 
  :start-after: How to Enable Email

Configuration Settings
----------------------

See `Configuration Settings <https://docs.mattermost.com/administration/config-settings.html>`__
documentation to customize your deployment.

Updating Docker Preview
-----------------------

To delete your existing Docker preview and run a new version use: 

   .. code:: bash

       docker stop mattermost-preview
       docker rm -v mattermost-preview

Accessing Your Container
------------------------

-  If you wish to gain access to a shell on the container use:

   .. code:: bash

       docker exec -ti mattermost-preview /bin/bash
