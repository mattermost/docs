.. _dev-compiling:

tl;dr
-----

.. code-block:: bash

  # Start the API server (required)
  cd ~/go/src/github.com/mattermost/mattermost-server
  make run

  # Start the web app (optional)
  cd $WEBAPP_DIR
  make help

  # Make docs from either repo
  make help
  

Compiling Mattermost
====================

Before compiling Mattermost, make sure to set up your developer machine according to the instructions for your platform.

Instructions are available for the following platforms:

  - :doc:`Ubuntu 16.04 <dev-setup-ubuntu-1604>`
  - :doc:`Mac OS X <dev-setup-osx>`
  - :doc:`Archlinux <dev-setup-archlinux>`
  - :doc:`Windows <dev-setup-windows>`

Mattermost uses `GNU Make <https://www.gnu.org/software/make/>`_ to control the generation of builds, to run the test suite, and to manage the build environment. You must run the ``make`` command from within the source directory. If you set up your developer machine according to the instructions, you can change to the source directory with the following command:

  ``cd ~/go/src/github.com/mattermost/mattermost-server``

The first time that you use the ``make run`` command can take a substantial amount of time depending on your machine's processor speed and memory size, and on the speed of your network. If you are developing in a VM, make sure that the VM has at least 2G of memory assigned to it.

To start contributing to Mattermost, see :doc:`Developer Flow <developer-flow>`.


Make Commands
-------------

``make help``:
  Displays all of the make commands.

``make package`` additional notes:
  Creates packages for distributing your builds and puts them in the ``~/go/src/github.com/mattermost/mattermost-server/dist`` directory. If you want to make packages for targets other than your build machine, you must run the following commands first:

  1. Modify permissions on ``/usr/local/go``. Replace *{user}* and *{group}* with the user and group that you are logged in with.

     ``sudo chown -R {user}.{group} /usr/local/go``

  2. If you are not developing on OS X, set up your environment to cross-compile Apple OS X binaries:

     ``env GOOS=darwin GOARCH=amd64 go install std``

  3. If you are not developing on Windows, set up your environment to cross-compile Windows binaries:

     a. ``env GOOS=windows GOARCH=amd64 go install std``
     b. ``sudo apt-get install zip``

  4. If you are not developing on Linux, set up your environment to cross-compile Linux binaries:

    ``env GOOS=linux GOARCH=amd64 go install std``
