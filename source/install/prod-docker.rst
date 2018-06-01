..  _docker-local-machine:

Production Docker Deployment
==============================

Deploy Mattermost using a multi-node production configuration using `Docker Compose <https://docs.docker.com/compose/>`_. Docker Compose experience recommended.

For a single-node preview of Mattermost (without email) see `Local Machine Setup using Docker <http://docs.mattermost.com/install/docker-local-machine.html>`_.

If you have any problems installing, see the `troubleshooting guide <https://www.mattermost.org/troubleshoot/>`_. To submit an improvement or correction, click Edit at the top of this page.

Production Docker Setup on Ubuntu
----------------------------------------------------

1. **Install Docker** using `the Ubuntu online guide <https://docs.docker.com/installation/ubuntulinux/>`_ or these instructions:

   .. code:: bash

       sudo apt-get update
       sudo apt-get install wget
       wget -qO- https://get.docker.com/ | sh
       sudo usermod -aG docker <username>
       sudo service docker start
       newgrp docker

2. **Install Docker Compose** using `the online guide <https://docs.docker.com/compose/install/>`_. You have to download the latest release from `Docker Compose Github's page <https://github.com/docker/compose/releases/>`_ and put the binary on your :code:`/usr/local/bin` folder. Usually, you can use the following command, replacing :code:`$dockerComposeVersion` by the Docker Compose version to install :

   .. code:: bash
   
      curl -L https://github.com/docker/compose/releases/download/$dockerComposeVersion/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
      sudo chmod +x /usr/local/bin/docker-compose

3. **Deploy the Mattermost Production Docker** setup by running:

   .. code:: bash

       git clone https://github.com/mattermost/mattermost-docker.git
       cd mattermost-docker
       docker-compose build
       mkdir -pv ./volumes/app/mattermost/{data,logs,config}
       chown -R 2000:2000 ./volumes/app/mattermost/
       docker-compose up -d

4. **Configure TLS** by following `the instructions <https://github.com/mattermost/mattermost-docker#install-with-ssl-certificate>`_

5. **Configure Email** by following the `SMTP email setup guide <http://docs.mattermost.com/install/smtp-email-setup.html>`_

6. (Optional) to enable enterprise features under **System Console** > **Edition and License** upload your `trial license <https://about.mattermost.com/trial/>`_ or `subscription license file <https://about.mattermost.com/pricing/>`_ received via email.

7. **Configure your server** based on `configuration settings documentation <http://docs.mattermost.com/administration/config-settings.html>`_

Additional Guides:

- **Start, stop and remove containers** using `management instructions. <https://github.com/mattermost/mattermost-docker/#startingstopping-docker>`_

- **Setup Database Backup** following the `database backup instructions. <https://github.com/mattermost/mattermost-docker#aws>`_


Production Docker Setup on Arch Linux
------------------------------------------------------------

To install on Arch Linux, see the `installation guide <https://wiki.archlinux.org/index.php/Mattermost>`_ on the Arch Linux wiki.


Production Docker Setup on macOS
------------------------------------------------------------

You can run a production deployment on macOS by `installing Docker Compose using the online guide <https://docs.docker.com/docker-for-mac/>`_ then following the above instructions.

Other options:
--------------

To install Mattermost Team Edition instead of Mattermost Enterprise Edition, open ``docker-compose.yaml`` and comment out the following line:

  .. code-block:: text

    dockerfile: Dockerfile-enterprise
