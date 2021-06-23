..  _install-rhel-8-server:

Installing Red Hat Enterprise Linux 8
-------------------------------------

Install the 64-bit version of RHEL 8 on each machine that hosts one or more of the components.

**To install RHEL 8 Server:**

1. To install RHEL 8, see the `RedHat Installation Instructions <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/performing_a_standard_rhel_installation/index>`__.


2. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

  ``sudo yum update``
  
  ``sudo yum upgrade``

Now that the system is up to date, you can start installing the components that make up a Mattermost system.

.. note:: 

  Ensure that the ``mailcap`` package is installed as it includes the ``mime.types`` file which is needed for the Mobile App to work correctly.
