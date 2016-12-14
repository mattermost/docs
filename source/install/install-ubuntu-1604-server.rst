Installing Ubuntu Server 16.04 LTS
==================================

Install Ubuntu Server on each machine that hosts one or more of the components. In most cases you need the 64-bit version.

You can use the 32-bit version on a machine that hosts the database and proxy server, but the Mattermost server requires 64-bit.

**To install Ubuntu Server:**

1. Download the appropriate ISO image from http://releases.ubuntu.com/16.04/ and burn it to a CD-ROM.

2. Boot the system from the CD-ROM drive and follow the on-screen prompts.

3. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

   -  ``sudo apt-get update``
   -  ``sudo apt-get upgrade``

Now that the system is up to date, you can install the database.
