.. _dev-setup-archlinux:

Installing Developer Components on Archlinux
============================================

Set up your development environment for building, running, and testing Mattermost.

1. If you are developing with the Docker container, install and configure Docker CE:

  a. ``pacman -S docker``
  b. ``gpasswd -a user docker``
  c. ``systemctl enable docker.service``
  d. ``systemctl start docker.service``
  e. ``newgrp docker``
  f. Edit your ``/etc/hosts`` file to include the following line:

    ``127.0.0.1 dockerhost``

2. Install Go 1.8.

  ``pacman -S go``

3. Set up your Go workspace:

  a. ``mkdir ~/go``

  b. Add the following lines to your ``~/.bashrc`` file:

    .. code-block:: bash

      export GOPATH=$HOME/go
      export PATH=$PATH:$GOPATH/bin
      export PATH=$PATH:/usr/local/go/bin

  c. Reload your bash configuration.

    ``source ~/.bashrc``

4. Increase the file handle limit. Edit ``/etc/security/limits.conf`` and add the following lines (replace *{username}* with your user):

  .. code-block:: text

    {username}  soft  nofile  8096
    {username}  hard  nofile  8096

  You must reboot for these changes to take effect.

5. Install Node.js.

  ``pacman -S nodejs npm``

6. Fork Mattermost on GitHub.com from https://github.com/mattermost/platform.

7. Download the Mattermost code from your forked repository:

  a. Create the directory for the code.

    ``mkdir -p ~/go/src/github.com/mattermost``

  b. Change to the directory that you created.

    ``cd ~/go/src/github.com/mattermost``

  c. Clone your Mattermost fork. In the following command, replace *{username}* with your GitHub username.

    ``git clone https://github.com/{username}/platform.git``

Now that everything is set up, you are ready to compile and run Mattermost. See :doc:`dev-setup-compiling`.
