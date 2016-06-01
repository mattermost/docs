..  _docker-local-machine:

Local Machine Setup using Docker 
===============================

The following instructions use Docker to install Mattermost in *Preview Mode* for exploring product functionality on a single machine using Docker. This configuration should not be used in production, as it's using a known password string and contains other non-production configuration settings, and it does not support upgrade. 

If you're looking for a production installation with Docker, please see the `Mattermost Production Docker Deployment Guide <https://http://docs.mattermost.com/install/prod-docker.html>`_.

One-line Docker Install
-----------------------

If you have Docker set up, Mattermost installs in one-line:

   .. code:: bash

       docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

Otherwise, see step-by-step instructions:

Mac OSX
-------

1. Install Docker Toolbox using instructions at:
   http://docs.docker.com/installation/mac/

   1. Start Docker Toolbox from the command line and run:
      ``docker-machine create -d virtualbox dev``

2. Get your Docker IP address with: ``docker-machine ip dev``
3. Use ``sudo nano /etc/hosts`` to add ``<Docker IP> dockerhost`` to
   your /etc/hosts file
4. Run: ``docker-machine env dev`` and copy the export statements to
   your ~/.bash\_profile by running ``sudo nano ~/.bash_profile``. Then
   run: ``source ~/.bash_profile``
5. Run:
   ``docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview``
6. When docker is done fetching the image, open http://dockerhost:8065/
   in your browser.

Ubuntu
------

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

2. Start docker container:

   .. code:: bash

       docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

3. When docker is done fetching the image, open http://localhost:8065/
   in your browser.

Arch
----

1. Install Docker using the following commands:

   .. code:: bash

       pacman -S docker
       systemctl enable docker.service
       systemctl start docker.service
       gpasswd -a <username> docker
       newgrp docker

2. Start Docker container:

   .. code:: bash

       docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

3. When Docker is done fetching the image, open http://localhost:8065/
   in your browser.

Additional Notes
----------------

-  Instructions on how to update your Docker image are found below.

-  If you wish to remove mattermost-dev use:

   .. code:: bash

       docker stop mattermost-dev
       docker rm -v mattermost-dev

-  If you wish to gain access to a shell on the container use:

   .. code:: bash

       docker exec -ti mattermost-dev /bin/bash

Configuration Settings
----------------------

See `Configuration Settings <http://docs.mattermost.com/administration/config-settings.html>`__
documentation to customize your deployment.

(Recommended) Enable Email
-----

The default single-container Docker instance for Mattermost is designed
for product evaluation, and sets ``SendEmailNotifications=false`` so the
product can function without enabling email. To see the product's full
functionality, enabling SMTP email is recommended.

.. include:: smtp-email-setup.rst 
  :start-after: How to Enable Email
