Installing Ubuntu Server 14.04 LTS
==================================

Install Ubuntu Server on each machine that hosts one or more of the components. In most cases you need the 64-bit version.

You can use the 32-bit version on a machine that hosts the database and proxy server, but the Mattermost server requires 64-bit.

**To install Ubuntu Server:**

1. Download the appropriate ISO image from http://releases.ubuntu.com/14.04.5/ and burn it to a CD-ROM.

2. Boot the system from the CD-ROM drive and follow the on-screen prompts.

3. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

   -  ``sudo apt-get update``
   -  ``sudo apt-get upgrade``

**What to do next**

Install a database. You can install either MySQL 5.6 or PostgreSQL version 9.3 or later.

**Related links**
  - :ref:`install-ubuntu-1404-mysql`
  - :ref:`install-ubuntu-1404-postgresql`
