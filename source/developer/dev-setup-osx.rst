.. _dev-setup-osx:

Installing Developer Components on macOS
===========================================

Set up your development environment for building, running, and testing Mattermost.

1. If you are developing with the Docker container, install and configure Docker CE:

  a. Follow the Docker installation instructions at https://docs.docker.com/docker-for-mac/.

  b. Edit your ``/etc/hosts`` file to include the following line:

    ``127.0.0.1     dockerhost``

2. Download and install Brew, which you'll use for installing dependencies. Follow the Brew installation instructions at https://brew.sh/

3. Install Node.js, Yarn, libpng, and Go:

  ``brew install node yarn libpng go``

4. Set up your Go workspace:

  a. ``mkdir ~/go``

  b. Add the following lines to your ``~/.bash_profile`` file:

    .. code-block:: bash

      export GOPATH=$HOME/go
      export PATH=$PATH:$GOPATH/bin
      export PATH=$PATH:/usr/local/go/bin
      ulimit -n 8096

  c. Reload your bash configuration.

    ``source ~/.bash_profile``

5. Fork Mattermost server on GitHub from https://github.com/mattermost/mattermost-server.

6. Fork Mattermost webapp on GitHub from https://github.com/mattermost/mattermost-webapp.

6. Download the Mattermost code from your forked repositories:

  a. Create the directory for the code.

    ``mkdir -p ~/go/src/github.com/mattermost``

  b. Change to the directory that you created.

    ``cd ~/go/src/github.com/mattermost``

  c. Clone your Mattermost server fork. In the following command, replace *{username}* with your GitHub username.

    ``git clone https://github.com/{username}/mattermost-server.git``

  d. Clone your Mattermost webapp fork. In the following command, replace *{username}* with your GitHub username.

    ``git clone https://github.com/{username}/mattermost-webapp.git``

Now that everything is set up, you are ready to compile and run Mattermost. See :doc:`dev-setup-compiling`.
