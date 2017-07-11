.. _install-debian-88-server:

Installing Debian Jessie
========================

Install the 64-bit version of Debian on each machine that hosts one or more of the components.

**To install Debian Jessie:**

1. To install Debian Jessie, see the `Debian Installation Guide (PDF). <https://www.debian.org/releases/stable/amd64/install.pdf>`_

2. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands as root:

  ``apt-get update``

  ``apt-get upgrade``

3. Let's install *sudo* and *curl* for use later in the installation:

  ``apt-get install sudo curl``

4. Let's add our non-root user to the sudo group so we don't have to be logged in as the root user.

  ``usermod -a -G sudo myuser``

Now that the system is up to date and our user is in the sudo group, you can start installing the components that make up a Mattermost system.
