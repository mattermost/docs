Install Mattermost on RHEL
==========================

.. raw:: html

    <div class="mm-badge mm-badge--combo">

    <div class="mm-plans-badge block">
      <p>
        <img src="../_static/images/badges/flag_icon.svg" alt="" />
        <span>Available on <a href="https://mattermost.com/pricing/">all plans</a></span>
      </p>
      <p>
        <img src="../_static/images/badges/deployment_icon.svg" alt="" />
        <span><a href="https://mattermost.com/download/">Self-hosted</a> deployments</span>
      </p>
    </div>

    <div class="mm-badge__reqs">
      <h3>Minimum system requirements:</h3>
      <ul>
        <li>Operating System: Enterprise Linux 7+, Oracle Linux  6+, Oracle Linux 7+
        <li>Hardware: 1 vCPU/core with 2GB RAM (support for up to 1,000 users)</li>
        <li>Database: <a href="https://docs.mattermost.com/deploy/postgres-migration.html">PostgreSQL v12+</a></li>
        <li>Network:
          <ul>
            <li>Application 80/443, TLS, TCP Inbound</li>
            <li>Administrator Console 8065, TLS, TCP Inbound</li>
            <li>SMTP port 10025, TCP/UDP Outbound</li>
          </ul>
        </li>
      </ul>
    </div>

  </div>

.. note::

  You need a PostgreSQL database. See the :doc:`database preparation </install/prepare-mattermost-database>` documentation for details on this prerequisite.

A Mattermost deployment includes 4 steps: `download <#download>`__, `install <#install>`__, `setup <#setup>`__, and `update <#updates>`__.

Download the latest Mattermost Server tarball
---------------------------------------------

.. include:: download-latest-tarball.rst
    :start-after: :nosearch:

Install
-------

Ahead of installing the Mattermost Server, it’s good practice to update all your repositories and, where required, update existing packages by running the following commands:

.. code-block:: sh

    sudo dnf update
    sudo dnf upgrade

After any updates, and any system reboots, are complete, install the Mattermost Server.

.. include:: install-mattermost-server-tarball.rst
    :start-after: :nosearch:

Setup
-----

.. include:: setup-mattermost-server.rst
    :start-after: :nosearch:
  
.. important::
  If you don't receive an error when starting Mattermost after the previous step, you are good to go. If you did receive an error, continue on

Modify SELinux settings
-----------------------

When deploying Mattermost from RHEL9, which has SELinux running with enforceing mode enabled by default, additional configuration is required the SELinux policy is being enforced and denies access based on SELinux policy rules.

First, ensure that SELinux is enabled and in enforcing mode by running the ``sestatus`` command. If it's ``enforcing``, you'll need to configure it properly.

Set bin contexts for ``/opt/mattermost/bin``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SELinux enforces security contexts for binaries. To label the Mattermost binaries as safe, you'll need to set them to the below SELinux context.

.. code-block:: sh

  sudo semanage fcontext -a -t bin_t "/opt/mattermost/bin(/.*)?"
  sudo restorecon -RF /opt/mattermost/bin

Now, try starting Mattermost again with 

.. code-block:: sh

  sudo systemctl start mattermost

If you don't receive an error, verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that's returned by the Mattermost Server. You're all set!

.. important::
  If on starting Mattermost you receive an error, before moving on, check for the existence of a file in ``/opt/mattermost/logs`` - if ``mattermost.log`` exists in that directory, it's more likely you're dealing with a configuration issue in  ``config.json``. Double check the previous steps before continuing

Try different contexts for ``/opt/mattermost``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SELinux enforces security contexts for files and directories. To label your Mattermost directory as safe, you'll need to set an appropriate SELinux context.

1. Check current context by running ``ls -Z /opt/mattermost``. When you see something like ``drwxr-xr-x. root root unconfined_u:object_r:default_t:s0 mattermost`` returned, the ``default_t`` indicates that SELinux doesn't know what this directory is for.
2. Set a safe context by assigning a SELinux type that's compatible with web services or applications by running ``sudo semanage fcontext -a -t httpd_sys_content_t "/opt/mattermost(/.*)?"``. A common one is ``httpd_sys_content_t``, used for serving files. Ensure you match the directory and its contents recursively. Run the ``sudo restorecon -R /opt/mattermost`` to apply the changes.

Allow Mattermost to bind to ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Mattermost needs specific ports (e.g., 8065), ensure that SELinux allows it by allowing Mattermost to bind to ports. Run the ``sudo semanage port -l | grep 8065`` command, and if the port's not listed, you'll need to add it by running ``sudo semanage port -a -t http_port_t -p tcp 8065``, replacing the ``8065`` with the required port.

Handle custom policies
~~~~~~~~~~~~~~~~~~~~~~~

If Mattermost requires actions that SELinux blocks, you'll need to generate a custom policy. 

1. Check for SELinux denials first in the logs by running ``sudo ausearch -m avc -ts recent``, or by checking the audit log: ``sudo cat /var/log/audit/audit.log | grep denied``.

2. If needed, generate a policy module by installing ``audit2allow`` to generate policies automatically.

.. code-block:: sh

  sudo yum install -y policycoreutils-python-utils
  sudo grep mattermost /var/log/audit/audit.log | audit2allow -M mattermost_policy
  sudo semodule -i mattermost_policy.pp

Test the configuration
~~~~~~~~~~~~~~~~~~~~~~

Restart Mattermost to confirm the configuation works as expected by running ``sudo systemctl restart mattermost``. In the case of failures, revisit the logs to identify other SELinux-related issues.

.. tip::

  Need Mattermost working quickly for testing purposes? You can change SELinux to permissive mode by running the ``sudo setenforce 0``. command where policies aren't enforced, only logged. This command changes the SELinux mode to "permissive". While in permissive mode, policies aren't enforced, and violations are logged instead of being blocked. This can be helpful for debugging and troubleshooting issues related to SELinux policies. Ensure you re-enable enforcing mode once context is working as needed by running the ``sudo setenforce 1`` command.

See the following SELinux resources for additional details:

- `SELinux User’s and Administrator’s Guide <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index>`_
- `SELinux Project Wiki <https://selinuxproject.org/page/Main_Page>`_
- `Introduction to SELinux <https://github.blog/developer-skills/programming-languages-and-frameworks/introduction-to-selinux/>`_
- `A Sysadmin’s Guide to SELinux: 42 Answers to the Big Questions <https://opensource.com/article/18/7/sysadmin-guide-selinux>`_
- `Mastering SELinux: A Comprehensive Guide to Linux Security <https://srivastavayushmaan1347.medium.com/mastering-selinux-a-comprehensive-guide-to-linux-security-8bed9976da88>`_

Updates
-------

Updating your Mattermost Server installation when using the tarball requires several manual steps. See the :doc:`upgrade Mattermost Server </upgrade/upgrading-mattermost-server>` documentation for details.

Remove Mattermost
------------------

If you wish to remove the Mattermost Server for any reason, you must stop the Mattermost Server, back up all important files, and then run this command:

.. code-block:: sh

   sudo rm /opt/mattermost

.. note::

	Depending on your configuration, there are several important folders in ``/opt/mattermost`` to backup. These are ``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data``. We strongly recommend you back up these locations before running the ``rm`` command.

You may also remove the Mattermost systemd unit file and the user/group created for running the application.

Frequently asked questions
--------------------------

.. include:: common-deploy-faq.rst
  :start-after: :nosearch:
