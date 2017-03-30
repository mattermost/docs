.. _dev-setup:

=======================
Developer Machine Setup
=======================

For developing and contributing to Mattermost, make sure that you install and use the Docker container. The container has an Inbucket email server and both MySQL and PostgreSQL databases. Both databases are pre-populated with teams, channels, and users, and are required for running the built-in unit tests.

If you don't plan on contributing code to the Mattermost open source project, then you don't need to install Docker. If you're not installing Docker, you can safely skip the Docker installation parts of the setup instructions. However, the ``make run`` and ``make test`` commands won't work.

Set up instructions are available for the following operating systems:

  .. toctree::

    Setting up Ubuntu 16.04 <dev-setup-ubuntu-1604.rst>
    Setting up Mac OS X <dev-setup-osx.rst>
    Setting up Archlinux <dev-setup-archlinux.rst>
    Setting up Windows <dev-setup-windows.rst>
    dev-setup-compiling.rst
    dev-setup-troubleshooting.rst
