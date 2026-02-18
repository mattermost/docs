:orphan:
:nosearch:

.. raw:: html

  <div class="mm-badge mm-badge--combo">
    <div class="mm-badge__reqs">
      <h3>Minimum system requirements:</h3>
      <ul>
        <li>Operating System: Enterprise Linux 7+, Oracle Linux  6+, Oracle Linux 7+</li>
        <li>Hardware: 1 vCPU/core with 2GB RAM (support for up to 1,000 users)</li>
        <li>Database: <a href="https://docs.mattermost.com/deployment-guide/postgres-migration.html">PostgreSQL v14+</a></li>
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

This Mattermost deployment includes the following steps: install PostgreSQL database, prepare the database, download the Mattermost server, install the server, set up the server, and update the server.

Step 1: Install PostgreSQL database or get database connection credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Install PostgreSQL locally on the same server by following the `PostgreSQL installation <https://www.postgresql.org/download/>`_ documentation.
- Use an external PostgreSQL database server. Ensure you have connection credentials, including hostname, port, database name, username, and password available.
- Use a managed database service.

Step 2: Prepare the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the :ref:`database preparation <deployment-guide/server/preparations:database preparation>` documentation to set up your PostgreSQL database for Mattermost.

Step 3: Download the latest Mattermost Server tarball
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a terminal window, ssh onto the system that will host the Mattermost Server. Using ``wget``, download the Mattermost Server release you want to install using one of the following commands. Replace ``amd64`` with the appropriate architecture (e.g., ``arm64`` for ARM-based systems) in the link as needed.

.. tab:: Latest release

  .. code-block:: sh

    wget https://releases.mattermost.com/11.4.0/mattermost-11.4.0-linux-amd64.tar.gz

.. tab:: Current ESR

  .. code-block:: sh

    wget https://releases.mattermost.com/10.11.11/mattermost-10.11.11-linux-amd64.tar.gz

.. tab:: Older releases

  If you are looking for an older release, Enterprise and Team Edition releases can be found in our :doc:`version archive </product-overview/version-archive>` documentation.

Step 4: Install Mattermost server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ahead of installing the Mattermost Server, we recommend updating all your repositories and, where required, update existing packages by running the following commands:

  .. code-block:: sh

      sudo dnf update
      sudo dnf upgrade

2. After any updates, and any system reboots, are complete, install the Mattermost Server by extracting the tarball, creating users and groups, and setting file/folder permissions.

  a. First extract the tarball:

    .. code-block:: sh

        tar -xvzf mattermost*.gz

  b. Now move the entire folder to the ``/opt`` directory (or whatever path you require):

    .. code-block:: sh

        sudo mv mattermost /opt

  c. Create the default storage folder. By default the Mattermost Server uses ``/opt/mattermost/data`` as the folder for files. This can be changed in the System Console during setup (even using alternative storage such as S3):

    .. code-block:: sh

        sudo mkdir /opt/mattermost/data

.. note::

  If you choose a custom path, ensure this alternate path is used in all steps that follow.`

3. Set up a user and group called ``mattermost``:

  .. code-block:: sh

    sudo useradd --system --user-group mattermost

.. note::

  If you choose a custom user and group name, ensure it is used in all the steps that follow.

4. Set the file and folder permissions for your installation:

  .. code-block:: sh

    sudo chown -R mattermost:mattermost /opt/mattermost

5. Give the ``mattermost`` group write permissions to the application folder:

  .. code-block:: sh

    sudo chmod -R g+w /opt/mattermost

  You will now have the latest Mattermost Server version installed on your system. Starting and stopping the Mattermost Server is done using ``systemd``.

6. Create the systemd unit file:

  .. code-block:: sh

    sudo touch /lib/systemd/system/mattermost.service

7. As root, edit the systemd unit file at ``/lib/systemd/system/mattermost.service`` to add the following lines:

  .. code-block:: text

    [Unit]
    Description=Mattermost
    After=network.target

    [Service]
    Type=notify
    ExecStart=/opt/mattermost/bin/mattermost
    TimeoutStartSec=3600
    KillMode=mixed
    Restart=always
    RestartSec=10
    WorkingDirectory=/opt/mattermost
    User=mattermost
    Group=mattermost
    LimitNOFILE=49152

    [Install]
    WantedBy=multi-user.target

8. Save the file and reload systemd using ``sudo systemctl daemon-reload``. Mattermost Server is now installed and is ready for setup.

Step 5: Set up the server
~~~~~~~~~~~~~~~~~~~~~~~~~

Before you start the Mattermost Server, you need to edit the configuration file. A default configuration file is located at ``/opt/mattermost/config/config.json``. We recommend taking a backup of this default config ahead of making changes:

.. code-block:: sh

  sudo cp /opt/mattermost/config/config.json /opt/mattermost/config/config.defaults.json

Configure the following properties in this file:

* Under ``SqlSettings``, set ``DriverName`` to ``"postgres"``. This is the default and recommended database for all Mattermost installations.
* Under ``SqlSettings``, set ``DataSource`` to ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"`` replacing ``mmuser``, ``<mmuser-password>``, ``<host-name-or-IP>`` and ``mattermost`` with your database name.
* Under ``ServiceSettings``, set ``"SiteURL"``: The domain name for the Mattermost application (e.g. ``https://mattermost.example.com``).

.. note::

  We recommend configuring the :ref:`Support Email <administration-guide/configure/site-configuration-settings:support email address>` under ``SupportSettings``, set ``"SupportEmail"``. This is the email address your users will contact when they need help.

After modifying the ``config.json`` configuration file, you can now start the Mattermost server:

.. code-block:: sh

  sudo systemctl start mattermost

Verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that’s returned by the Mattermost Server.

The final step, depending on your requirements, is to run sudo ``systemctl enable mattermost.service`` so that Mattermost will start on system boot. If you don't receive an error when starting Mattermost after the previous step, you are good to go. If you did receive an error, continue on.

.. important::

  **Modify SELinux settings**: When deploying Mattermost from RHEL9, which has SELinux running with enforceing mode enabled by default, additional configuration is required.

  - SELinux is a security module that provides access control security policies. It's enabled by default on RHEL and CentOS systems. SELinux can block access to files, directories, and ports, which can cause issues when starting Mattermost. To resolve these issues, you'll need to set the appropriate SELinux contexts for the Mattermost binaries and directories, and allow Mattermost to bind to ports.
  - Ensure that SELinux is enabled and in enforcing mode by running the ``sestatus`` command. If it's ``enforcing``, you'll need to configure it properly.
  - Set bin contexts for ``/opt/mattermost/bin``: SELinux enforces security contexts for binaries. To label the Mattermost binaries as safe, you'll need to set them to the below SELinux context.

    .. code-block:: sh

      sudo semanage fcontext -a -t bin_t "/opt/mattermost/bin(/.*)?"
      sudo restorecon -RF /opt/mattermost/bin

    Now, try starting Mattermost again with

    .. code-block:: sh

      sudo systemctl start mattermost

    If you don't receive an error, verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that's returned by the Mattermost Server. You're all set!

    If on starting Mattermost you receive an error, before moving on, check for the existence of a file in ``/opt/mattermost/logs`` - if ``mattermost.log`` exists in that directory, it's more likely you're dealing with a configuration issue in  ``config.json``. Double check the previous steps before continuing

    Try different contexts for ``/opt/mattermost``: SELinux enforces security contexts for files and directories. To label your Mattermost directory as safe, you'll need to set an appropriate SELinux context.

      1. Check current context by running ``ls -Z /opt/mattermost``. When you see something like ``drwxr-xr-x. root root unconfined_u:object_r:default_t:s0 mattermost`` returned, the ``default_t`` indicates that SELinux doesn't know what this directory is for.
      2. Set a safe context by assigning a SELinux type that's compatible with web services or applications by running ``sudo semanage fcontext -a -t httpd_sys_content_t "/opt/mattermost(/.*)?"``. A common one is ``httpd_sys_content_t``, used for serving files. Ensure you match the directory and its contents recursively. Run the ``sudo restorecon -R /opt/mattermost`` to apply the changes.

    Allow Mattermost to bind to ports: When Mattermost needs specific ports (e.g., 8065), ensure that SELinux allows it by allowing Mattermost to bind to ports. Run the ``sudo semanage port -l | grep 8065`` command, and if the port's not listed, you'll need to add it by running ``sudo semanage port -a -t http_port_t -p tcp 8065``, replacing the ``8065`` with the required port.

    Handle custom policies: If Mattermost requires actions that SELinux blocks, you'll need to generate a custom policy.

      1. Check for SELinux denials first in the logs by running ``sudo ausearch -m avc -ts recent``, or by checking the audit log: ``sudo cat /var/log/audit/audit.log | grep denied``.

      2. If needed, generate a policy module by installing ``audit2allow`` to generate policies automatically.

        .. code-block:: sh

          sudo yum install -y policycoreutils-python-utils
          sudo grep mattermost /var/log/audit/audit.log | audit2allow -M mattermost_policy
          sudo semodule -i mattermost_policy.pp

    Test the configuration: Restart Mattermost to confirm the configuation works as expected by running ``sudo systemctl restart mattermost``. In the case of failures, revisit the logs to identify other SELinux-related issues.

    Need Mattermost working quickly for testing purposes?

    - You can change SELinux to permissive mode by running the ``sudo setenforce 0``. command where policies aren't enforced, only logged.
    - This command changes the SELinux mode to "permissive". While in permissive mode, policies aren't enforced, and violations are logged instead of being blocked. This can be helpful for debugging and troubleshooting issues related to SELinux policies.
    - Ensure you re-enable enforcing mode once context is working as needed by running the ``sudo setenforce 1`` command.

    See the following SELinux resources for additional details:

      - `SELinux User's and Administrator's Guide <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index>`_
      - `SELinux Project Wiki <https://github.com/SELinuxProject/selinux>`_
      - `Introduction to SELinux <https://github.blog/developer-skills/programming-languages-and-frameworks/introduction-to-selinux/>`_
      - `A Sysadmin's Guide to SELinux: 42 Answers to the Big Questions <https://opensource.com/article/18/7/sysadmin-guide-selinux>`_
      - `Mastering SELinux: A Comprehensive Guide to Linux Security <https://srivastavayushmaan1347.medium.com/mastering-selinux-a-comprehensive-guide-to-linux-security-8bed9976da88>`_

Step 6: Update the server
~~~~~~~~~~~~~~~~~~~~~~~~~

Updating your Mattermost Server installation when using the tarball requires several manual steps. See the :doc:`upgrade Mattermost Server </administration-guide/upgrade/upgrading-mattermost-server>` documentation for details.

Remove Mattermost
-----------------

To remove the Mattermost Server, you must stop the Mattermost Server, back up all important files, and then run this command:

.. code-block:: sh

   sudo rm /opt/mattermost

.. note::

  Depending on your configuration, there are several important folders in ``/opt/mattermost`` to backup. These are ``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data``. We strongly recommend you back up these locations before running the ``rm`` command.

You may also remove the Mattermost systemd unit file and the user/group created for running the application.
