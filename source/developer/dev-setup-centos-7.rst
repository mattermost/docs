.. _dev-setup-centos-7:

Installing Developer Components on CentOS 7
===========================================

Set up your development environment for building, running, and testing Mattermost.

1. If you are developing with the Docker container, install and configure Docker CE:

  a. Follow the Docker installation instructions at https://docs.docker.com/engine/installation/linux/docker-ce/centos/.

  b. Edit your ``/etc/hosts`` file to include the following line:

    ``127.0.0.1     dockerhost``

  c. Add your username to the *docker* group so that you can run Docker without using sudo. Replace *{username}* with your username.

    ``sudo gpasswd -a {username} docker``

  d. Restart the Docker daemon.

    ``sudo systemctl restart docker``

  e. Change your current group ID to the *docker* group.

    ``newgrp docker``

2. Install the development tools package, wget and libpng12 required by pngquant(a library used by Mattermost).

    a. ``sudo yum group install "Development Tools"``

    b. ``sudo yum install -y wget libpng12``

3. Download and install Go 1.9 for Linux:

    a. Download the Go binary.

       ``wget https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz``

    b. Install the Go binary.

       ``sudo tar -C /usr/local -xzf go1.9.2.linux-amd64.tar.gz``

4. Set up your Go workspace:

  a. ``mkdir ~/go``

  b. Add the following lines to your ``~/.bashrc`` file:

    .. code-block:: bash

      export GOPATH=$HOME/go
      export PATH=$PATH:$GOPATH/bin
      export PATH=$PATH:/usr/local/go/bin

  c. Reload your bash configuration.

      source ~/.bashrc

  d. Since you cannot run ``ulimit -n 8096`` with a regular user, we have to edit the file ``sudo nano /etc/security/limits.conf`` to include the following 2 lines at the end of it:

    .. code-block:: bash
    
      {username} soft nofile 8096
      {username} hard nofile 10000

  e. After doing the above simple logout then log back in and it should accept the changes.


5. Install Node.js:

    a. Add the Node.js repository to your repository list.

      ``curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -``

    b. Install Node.js

      ``sudo yum install -y nodejs``

6. Install Yarn. Go to https://yarnpkg.com/en/docs/install and follow the installation instructions.

7. Fork Mattermost server on GitHub from https://github.com/mattermost/mattermost-server.

8. Fork Mattermost webapp on GitHub from https://github.com/mattermost/mattermost-webapp.

9. Download the Mattermost code from your forked repositories:

  a. Create the directory for the code.

    ``mkdir -p ~/go/src/github.com/mattermost``

  b. Change to the directory that you created.

    ``cd ~/go/src/github.com/mattermost``

  c. Clone your Mattermost server fork. In the following command, replace *{username}* with your GitHub username.

    ``git clone https://github.com/{username}/mattermost-server.git``

  d. Clone your Mattermost webapp fork. In the following command, replace *{username}* with your GitHub username.

    ``git clone https://github.com/{username}/mattermost-webapp.git``

Now that everything is set up, you are ready to compile and run Mattermost. See :doc:`dev-setup-compiling`.
