:orphan:
:nosearch:

.. raw:: html

  <div class="mm-badge mm-badge--combo">
    <div class="mm-badge__reqs">
      <h3>Minimum system requirements:</h3>
      <ul>
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

You can install the Mattermost Server on any 64-bit Linux system using the tarball. This is the most flexible installation method, but it comes with the highest effort, typically favored by advanced system administrators.

This Mattermost deployment includes the following steps: install PostgreSQL database, prepare the database, download the Mattermost server, install the server, and set up the server.

Step 1: Install PostgreSQL database or get database connection credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Install PostgreSQL locally on the same server by following the `PostgreSQL installation <https://www.postgresql.org/download/>`_ documentation.
- Use an external PostgreSQL database server. Ensure you have connection credentials, including hostname, port, database name, username, and password available.
- Use a managed database service.

Step 2: Prepare the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the :ref:`database preparation <deployment-guide/server/preparations:database preparation>` documentation to set up your PostgreSQL database for Mattermost.

Step 3: Download
~~~~~~~~~~~~~~~~~

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

Install the Mattermost Server by extracting the tarball, creating users and groups, and setting file/folder permissions.

1. First extract the tarball:

  .. code-block:: sh

      tar -xvzf mattermost*.gz

2. Move the entire folder to the ``/opt`` directory (or whatever path you require):

  .. code-block:: sh

      sudo mv mattermost /opt

3. Create the default storage folder. By default the Mattermost Server uses ``/opt/mattermost/data`` as the folder for files. This can be changed in the System Console during setup (even using alternative storage such as S3):

  .. code-block:: sh

      sudo mkdir /opt/mattermost/data

.. note::

	If you choose a custom path, ensure this alternate path is used in all steps that follow.

4. Set up a user and group called ``mattermost``:

  .. code-block:: sh

    sudo useradd --system --user-group mattermost

.. note::

	If you choose a custom user and group name, ensure it is used in all the steps that follow.

5. Set the file and folder permissions for your installation:

  .. code-block:: sh

    sudo chown -R mattermost:mattermost /opt/mattermost

6. Give the ``mattermost`` group write permissions to the application folder:

  .. code-block:: sh

    sudo chmod -R g+w /opt/mattermost

  You will now have the latest Mattermost Server version installed on your system. Starting and stopping the Mattermost Server is done using ``systemd``.

7. Create the systemd unit file:

  .. code-block:: sh

    sudo touch /lib/systemd/system/mattermost.service

8. As root, edit the systemd unit file at ``/lib/systemd/system/mattermost.service`` to add the following lines:

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

  .. note::

    If you are installing the Mattermost server on the same system as your database, you may want to add both ``After=postgresql.service`` and ``BindsTo=postgresql.service`` to the ``[Unit]`` section of the systemd unit file.

9. Save the file and reload systemd using ``sudo systemctl daemon-reload``. Mattermost Server is now installed and is ready for setup.

Step 5: Set up the server
~~~~~~~~~~~~~~~~~~~~~~~~~

Before you start the Mattermost Server, you need to edit the configuration file. A default configuration file is located at ``/opt/mattermost/config/config.json``. We recommend taking a backup of this default config ahead of making changes:

.. code-block:: sh

  sudo cp /opt/mattermost/config/config.json /opt/mattermost/config/config.defaults.json

Configure the following properties in this file:

* Under ``SqlSettings``, set ``DriverName`` to ``"postgres"``. This is the default and recommended database for all Mattermost installations.
* Under ``SqlSettings``, set ``DataSource`` to ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"`` replacing ``mmuser``, ``<mmuser-password>``, ``<host-name-or-IP>`` and ``mattermost`` with your database name.
* Under ``ServiceSettings``, set ``"SiteURL"``: The domain name for the Mattermost application (e.g. ``https://mattermost.example.com``).

We recommend configuring the :ref:`Support Email <administration-guide/configure/site-configuration-settings:support email address>` under ``SupportSettings``, set ``"SupportEmail"``. This is the email address your users will contact when they need help.

After modifying the ``config.json`` configuration file, you can now start the Mattermost server:

.. code-block:: sh

  sudo systemctl start mattermost

Verify that Mattermost is running: ``curl http://localhost:8065``. You should see the HTML that’s returned by the Mattermost Server.

The final step, depending on your requirements, is to run sudo ``systemctl enable mattermost.service`` so that Mattermost will start on system boot.

Step 6: Update the server
~~~~~~~~~~~~~~~~~~~~~~~~~~

Updating your Mattermost Server installation when using the tarball requires several manual steps. See the :doc:`upgrade Mattermost Server </administration-guide/upgrade/upgrading-mattermost-server>` documentation for details.

Remove Mattermost
-----------------

To remove the Mattermost Server for any reason, you must stop the Mattermost Server, back up all important files, and then run this command:

.. code-block:: sh

  sudo rm - rf /opt/mattermost

.. note::

  Depending on your configuration, there are several important folders in ``/opt/mattermost`` to backup. These are ``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data``. We strongly recommend you back up these locations before running the ``rm`` command.

You may also remove the Mattermost systemd unit file and the user/group created for running the application.
