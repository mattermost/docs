.. _install-ubuntu-1404-server:

Installing Ubuntu Server 14.04 LTS
==================================

Install the 64-bit version of Ubuntu Server on each machine that hosts one or more of the components.

**To install Ubuntu Server 14.04:**

1. Download the appropriate server install image from http://releases.ubuntu.com/14.04.5/ and burn it to a CD-ROM.

2. Boot the system from the CD-ROM drive and follow the on-screen prompts.

  .. note::
    If you need help with installing, see the `Ubuntu Installation Guide. <https://help.ubuntu.com/14.04/installation-guide/amd64/index.html>`_

3. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

  ``sudo apt-get update``
  
  ``sudo apt-get upgrade``

Now that the system is up to date, you can start installing the components that make up a Mattermost system.
