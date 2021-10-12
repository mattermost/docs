..  _install-rhel-6-server:

Installing Red Hat Enterprise Linux 6
=======================================

Install the 64-bit version of RHEL 6 on each machine that hosts one or more of the components.

**To install RHEL 6 Server:**

1. To install RHEL 6, see the `RedHat Installation Instructions <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/pdf/Installation_Guide/Red_Hat_Enterprise_Linux-6-Installation_Guide-en-US.pdf>`__.

2. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

  ``sudo yum update``
  
  ``sudo yum upgrade``

Now that the system is up to date, you can start installing the components that make up a Mattermost system.
