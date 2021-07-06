:orphan:

..  _docker-local-machine:

Deploy Mattermost on Docker
============================

.. important:: 

   This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. Community testing, feedback and improvements are welcome and greatly appreciated. You can `edit this page on GitHub <https://github.com/mattermost/docs/blob/master/source/install/prod-docker.rst>`__.

Deploy Mattermost using a multi-node configuration with `Docker Compose <https://docs.docker.com/compose/>`__. Experience with Docker Compose is recommended.

For a single-node preview of Mattermost (without email) see `Local Machine Setup using Docker <https://docs.mattermost.com/install/docker-local-machine.html>`__.

If you have any problems installing, see the `troubleshooting guide <https://mattermost.org/troubleshoot/>`__. To submit an improvement or correction, click **Edit** at the top of this page.

Docker Setup on Ubuntu
-----------------------

1. **Install Docker** using `the Ubuntu online guide <https://docs.docker.com/installation/ubuntulinux/>`__ or these instructions:

   .. code:: bash

       sudo apt-get update
       sudo apt-get install wget
       wget -qO- https://get.docker.com/ | sh
       sudo usermod -aG docker <username>
       sudo service docker start
       newgrp docker

2. **Install Docker Compose** using `the online guide <https://docs.docker.com/compose/install/>`__. You have to download the latest release from the `Docker Compose Github page <https://github.com/docker/compose/releases/>`__ and put the binary on your :code:`/usr/local/bin` folder. Usually, you can use the following command, replacing :code:`$dockerComposeVersion` with the Docker Compose version to install:

   .. code:: bash
   
      sudo curl -L "https://github.com/docker/compose/releases/download/$dockerComposeVersion/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      sudo chmod +x /usr/local/bin/docker-compose

3. **Deploy the Mattermost Docker** 

You can get the :code:`uid` (user ID) and :code:`gid` (group ID) of the Docker user by running:

.. code:: bash
   
   id <username>

Replace :code:`<username>` with the actual username. The following setup assumes the result above is :code:`uid=1000` and :code:`gid=1000`.

Set up using:

.. code:: bash
   
   sudo apt-get install git
   git clone https://github.com/mattermost/mattermost-docker.git
   cd mattermost-docker
   docker-compose build
   mkdir -pv ./volumes/app/mattermost/{data,logs,config,plugins,client-plugins}
   sudo chown -R 1000:1000 ./volumes/app/mattermost/
   docker-compose up -d

The ``docker-compose`` network that is created defaults to 172.18.0.0/16.  If you need to change the default network this `link <https://success.docker.com/article/how-do-i-configure-the-default-bridge-docker0-network-for-docker-engine-to-a-different-subnet>`__ provides guidelines on how to do that. If the network is already set up with the default, you need to run the following command to remove it. Then, run the command again to regenerate the default network to include the new network setting.
   
.. code:: bash
 
   docker network rm mattermost-server_mm-test
	   
To verify the current Docker network use the following command to list it (you can access information about the options `here <https://docs.docker.com/engine/reference/commandline/network_ls/>`__):
   
.. code:: bash
   
   docker network ls [OPTIONS]

4. **Configure TLS** by following `the instructions <https://github.com/mattermost/mattermost-docker#install-with-ssl-certificate>`__.

5. **Configure Email** by following the `SMTP email setup guide <https://docs.mattermost.com/install/smtp-email-setup.html>`__.

6. (Optional) To enable enterprise features, go to **System Console > Edition and License** and select **Start trial**.

7. **Configure your Server** based on the `configuration settings documentation <https://docs.mattermost.com/administration/config-settings.html>`__.

Once you've saved your configurations, start an Enterprise E20 trial via **Main Menu > System Console > Edition and License > Start trial**.

Additional guides:

- **Start, Stop, and Remove Containers** using `management instructions. <https://github.com/mattermost/mattermost-docker/#startingstopping-docker>`__

- **Setup Database Backup** following the `database backup instructions. <https://github.com/mattermost/mattermost-docker#aws>`__

Docker Setup on Arch Linux
--------------------------

To install on Arch Linux, see the `installation guide <https://wiki.archlinux.org/index.php/Mattermost>`__ on the Arch Linux wiki.

Docker Setup on macOS
---------------------

You can run a deployment on macOS by `installing Docker Compose using the online guide <https://docs.docker.com/docker-for-mac/>`__ then following the above instructions.

Other Options
--------------

To install Mattermost Team Edition instead of Mattermost Enterprise Edition, open ``docker-compose.yaml`` and uncomment the following lines:

.. code-block:: text

   # args:
   #   - edition=team
