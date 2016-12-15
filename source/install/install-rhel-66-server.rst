..  _install-rhel-66-server:

Installing Red Hat Enterprise Linux 6.6
=======================================

Install the 64-bit version of RHEL 6.6 on each machine that hosts one or more of the components.

**To install RHEL 6.6 Server:**

1. Download the appropriate ISO image from RedHat and burn it to a CD-ROM.

2. Boot the system from the CD-ROM drive and follow the on-screen prompts.

3. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

   -  ``sudo yum update``
   -  ``sudo yum upgrade``

Now that the system is up to date, you can start installing the components that make up a Mattermost system.
