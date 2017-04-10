.. _dev-setup-ubuntu-1604:

Installing Developer Components on Ubuntu 16.04
===============================================

Set up your development environment for building, running, and testing Mattermost.

1. If you are developing with the Docker container, install and configure Docker CE:

  a. Follow the Docker installation instructions at https://docs.docker.com/engine/installation/linux/ubuntu/#install-using-the-repository.

  b. Edit your ``/etc/hosts`` file to include the following line:

    ``127.0.0.1     dockerhost``

  c. Add your username to the *docker* group so that you can run Docker without using sudo. Replace *{username}* with your username.

    ``sudo gpasswd -a {username} docker``

  d. Restart the Docker daemon.

    ``sudo service docker restart``

  e. Change your current group ID to the *docker* group.

    ``newgrp docker``

2. Install the build-essential package.

  ``sudo apt-get install build-essential``

3. Download and install Go 1.8 for Linux:

    a. Download the Go binary.

       ``wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz``

    b. Install the Go binary.

       ``sudo tar -C /usr/local -xzf go1.8.linux-amd64.tar.gz``

    c. Modify permissions on ``/usr/local/go``. Replace *{user}* and *{group}* with the user and group that you are logged in with.

      ``sudo chown -R {user}.{group} /usr/local/go``

4. Set up your Go workspace:

  a. ``mkdir ~/go``

  b. Add the following lines to your ``~/.bashrc`` file:

    .. code-block:: bash

      export GOPATH=$HOME/go
      export PATH=$PATH:$GOPATH/bin
      export PATH=$PATH:/usr/local/go/bin
      ulimit -n 8096

  c. Reload your bash configuration.

    ``source ~/.bashrc``

5. Install Node.js:

    a. Add the Node.js repository to your repository list.

      ``curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -``

    b. Install Node.js

      ``sudo apt-get install -y nodejs``

6. Fork Mattermost on GitHub from https://github.com/mattermost/platform.

7. Download the Mattermost code from your forked repository:

  a. Create the directory for the code.

    ``mkdir -p ~/go/src/github.com/mattermost``

  b. Change to the directory that you created.

    ``cd ~/go/src/github.com/mattermost``

  c. Clone your Mattermost fork. In the following command, replace *{username}* with your GitHub username.

    ``git clone https://github.com/{username}/platform.git``

Now that everything is set up, you are ready to compile and run Mattermost. See :doc:`dev-setup-compiling`.
