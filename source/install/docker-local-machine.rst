..  _docker-local-machine:

Local Machine Setup and Upgrade
===============================

The following instructions use Docker to install Mattermost in *Preview
Mode* for exploring product functionality. This configuration should not
be used in production. Knowledge of Docker and Docker-Compose is required
to setup a production docker environments.

Docker Install
-----------------------

| If you have Docker Compose set up, follow these instructions:
| ``git clone https://github.com/mattermost/mattermost-docker.git``
| ``cd mattermost-docker``
| ``ln -s docker-compose-nossl.yml docker-compose.yml``
| ``docker-compose up -d``

Otherwise, see step-by-step docker setup available:

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

Arch
----

1. Install Docker using the following commands:

   .. code:: bash

       pacman -S docker
       systemctl enable docker.service
       systemctl start docker.service
       gpasswd -a <username> docker
       newgrp docker

Configuration Settings
----------------------

See `Configuration Settings <http://docs.mattermost.com/administration/config-settings.html>`__
documentation to customize your deployment.

(Recommended) Enable Email
-----

The default Docker instance for Mattermost is designed
for product evaluation, and sets ``SendEmailNotifications=false`` so the
product can function without enabling email. To see the product's full
functionality, enabling SMTP email is recommended.

.. include:: smtp-email-setup.rst 
  :start-after: How to Enable Email

