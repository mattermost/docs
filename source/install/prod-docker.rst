..  _docker-local-machine:

Production Docker Deployment
==============================

Deploy Mattermost using a multi-node production configuration using `Docker Compose <https://docs.docker.com/compose/>`_. Docker Compose experience recommended.

For a single-node preview of Mattermost (without email) see `Local Machine Setup using Docker <http://docs.mattermost.com/install/docker-local-machine.html>`_.

If you have any problems installing, see the `troubleshooting guide <https://www.mattermost.org/troubleshoot/>`_. To submit an improvement or correction, click Edit at the top of this page.

Production Docker Setup on Ubuntu
----------------------------------------------------

1. **Install Docker Compose** using `the Ubuntu online guide <https://docs.docker.com/installation/ubuntulinux/>`_ or these instructions:

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
       docker-compose build
       docker-compose up -d

3. **Configure TLS** by following `the instructions <https://github.com/mattermost/mattermost-docker#install-with-ssl-certificate>`_

4. **Configure Email** by following the `SMTP email setup guide <http://docs.mattermost.com/install/smtp-email-setup.html>`_

5. (Optional) to enable enterprise features under **System Console** > **Edition and License** upload your `trial license <https://about.mattermost.com/trial/>`_ or `subscription license file <https://about.mattermost.com/pricing/>`_ received via email.

6. **Configure your server** based on `configuration settings documentation <http://docs.mattermost.com/administration/config-settings.html>`_

Additional Guides:

- **Start, stop and remove containers** using `management instructions. <https://github.com/mattermost/mattermost-docker/#startingstopping>`_

- **Setup Database Backup** following the `database backup instructions. <https://github.com/mattermost/mattermost-docker/#database-backup>`_

Production Docker Setup on Mac OS X
------------------------------------------------------------

You can run a test deployment on Mac OS X by `installing Docker Compose using the online guide <http://docs.docker.com/installation/mac/>`_ then following the above instructions.

**Other options:** To install a feature-equivalent version of Mattermost that does not upgrade to enterprise features using a license key, Mattermost Team Edition, repeat steps above excluding ``-b enterprise`` from ``git clone`` command.
