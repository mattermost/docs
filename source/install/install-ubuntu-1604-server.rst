.. _install-ubuntu-1604-server:

Installing Ubuntu Server 16.04 LTS
==================================

Install the 64-bit version of Ubuntu Server on each machine that hosts one or more of the components.

**To install Ubuntu Server 16.04:**

1. Download the appropriate ISO image from http://releases.ubuntu.com/16.04/ and burn it to a CD-ROM.

2. Boot the system from the CD-ROM drive and follow the on-screen prompts.

3. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

   -  ``sudo apt-get update``
   -  ``sudo apt-get upgrade``

Now that the system is up to date, you can start installing the components that make up a Mattermost system.
