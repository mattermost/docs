..  _docker-local-machine:

Production Docker Deployment 
==============================

This guide walks through deploying a multi-node production configuration using Docker compose. Experience setting up production Docker environments using Docker-Compose is recommended. 

If you're looking for a quick "Preview Mode" setup of Mattermost on a local machine using Docker on a single node, please see the guide for `Local Machine Setup using Docker <http://docs.mattermost.com/install/docker-local-machine.html>`_. 

Production Docker on Ubuntu with Team Edition 
------

1. **Setup Docker Compose** using `the Ubuntu online guide <https://docs.docker.com/installation/ubuntulinux/>`_ or these instructions: 

   .. code:: bash

       sudo apt-get update
       sudo apt-get install wget
       wget -qO- https://get.docker.com/ | sh
       sudo usermod -aG docker <username>
       sudo service docker start
       newgrp docker

2. **Deploy the Mattermost Production Docker** setup by running: 

   .. code:: bash

       git clone https://github.com/mattermost/mattermost-docker.git
       cd mattermost-docker
       ln -s docker-compose-nossl.yml docker-compose.yml
       docker-compose up -d

3. **Setup Email** by following the `SMTP email setup guide <http://docs.mattermost.com/install/smtp-email-setup.html>`_ 

4. **Configure your server** based on `configuration settings documentation <http://docs.mattermost.com/administration/config-settings.html>`_

Production Docker on Ubuntu with Enterprise Edition 
------

1. **Setup Docker Compose** using `the Ubuntu online guide <https://docs.docker.com/installation/ubuntulinux/>`_ or these instructions: 

   .. code:: bash

       sudo apt-get update
       sudo apt-get install wget
       wget -qO- https://get.docker.com/ | sh
       sudo usermod -aG docker <username>
       sudo service docker start
       newgrp docker

2. **Deploy the Mattermost Production Docker** setup by running: 

   .. code:: bash

       git clone https://github.com/mattermost/mattermost-docker.git
       get checkout enterprise
       cd mattermost-docker
       ln -s docker-compose-nossl.yml docker-compose.yml
       docker-compose up -d

3. **Setup Email** by following the `SMTP email setup guide <http://docs.mattermost.com/install/smtp-email-setup.html>`_ 

4. **Configure your server** based on `configuration settings documentation <http://docs.mattermost.com/administration/config-settings.html>`_

5. Under **System Console** > **Edition and License** upload your `license file received in email with purchase. <https://about.mattermost.com/pricing/>`_

Production Docker on Mac OS X 
------

You can run a test deployment on Mac OS X by `installing Docker Compose using the online guide <http://docs.docker.com/installation/mac/>`_ then following the above instructions. 
