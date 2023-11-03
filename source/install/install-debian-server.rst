:orphan:
:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Install Debian Buster
----------------------

Install the 64-bit version of Debian on each machine that hosts one or more of the components.

**To install Debian Buster:**

1. To install Debian Buster, see `Debian Installation documentation <https://www.debian.org/releases/buster/installmanual>`__ for details.

2. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands as root:

  ``apt-get update``

  ``apt-get upgrade``

3. Install *sudo* and *curl* for use later in the installation: ``apt-get install sudo curl gnupg``.

4. Add your username to the sudo group. In the following command, replace {username} with your own username: ``usermod -a -G sudo {username}``.

Now that the system is up to date and your user is in the sudo group, you can start installing the components that make up a Mattermost system.
