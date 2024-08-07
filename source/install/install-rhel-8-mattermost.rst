:orphan: :nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Install Mattermost server
--------------------------

Install Mattermost Server on a 64-bit machine. Assume that the IP address of this server is ``10.10.10.2``.

1. Log in to the server that will host Mattermost Server and open a terminal window.

2. Download `the latest version of the Mattermost Server <https://mattermost.com/deploy/>`__. In the following command, replace ``X.X.X`` with the version that you want to download:

  .. code-block:: sh
  
    wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

3. Extract the Mattermost Server files.

  .. code-block:: sh
  
    tar -xvzf *.gz

4. Move the extracted file to the ``/opt`` directory.

  .. code-block:: sh
  
    sudo mv mattermost /opt

5. Create the storage directory for files.

  .. code-block:: sh
  
    sudo mkdir /opt/mattermost/data

.. note::
  
  The storage directory will contain all the files and images that your users post to Mattermost, so you need to make sure that the drive is large enough to hold the anticipated number of uploaded files and images.

6. Set up a system user and group called ``mattermost`` that will run this service, and set the ownership and permissions.

  .. code-block:: sh

    sudo useradd --system --user-group mattermost
    sudo chown -R mattermost:mattermost /opt/mattermost
    sudo chmod -R g+w /opt/mattermost
    sudo restorecon -R /opt/mattermost

7. Set up the database driver in the file ``/opt/mattermost/config/config.json``. Open the file as *root* in a text editor and make the following changes:

  -  If you are using PostgreSQL:

    a.  Set ``"DriverName"`` to ``"postgres"``
    b.  Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>`` and ``<host-name-or-IP>`` with the appropriate values:

      .. code-block:: text

        "postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"
  
  -  If you are using MySQL:

    a.  Set ``"DriverName"`` to ``"mysql"``
    b.  Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>`` and ``<host-name-or-IP>`` with the appropriate values. Also make sure that the database name is ``mattermost`` instead of ``mattermost_test``:

      .. code-block:: text
      
        "mmuser:<mmuser-password>@tcp(<host-name-or-IP>:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s"
    
    .. note::

      For a same-machine installation, replace ``<host-name-or-IP>`` above with ``localhost`` or ``127.0.0.1``.

8. Also set ``"SiteURL"`` to the full base URL of the site (e.g. ``"https://mattermost.example.com"``).

9. Test the Mattermost server to make sure everything works.

    a. Change to the ``mattermost`` directory:

    .. code-block:: sh

      cd /opt/mattermost

    b. Start the Mattermost server as the user *mattermost*:

    .. code-block:: sh

      sudo -u mattermost ./bin/mattermost

  When the server starts, it shows some log information and the text ``Server is listening on :8065``. You can stop the server by pressing pressing :kbd:`Ctrl` :kbd:`C` on Windows or Linux, or :kbd:`⌘` :kbd:`C` on Mac, in the terminal window.

10. Set up Mattermost to use the ``systemd init`` daemon which handles supervision of the Mattermost process.

  a. Create the Mattermost configuration file:

    .. code-block:: sh

      sudo touch /etc/systemd/system/mattermost.service

  b. Open the configuration file in a text editor, and copy the following lines into the file:

    .. code-block:: text

      [Unit]
      Description=Mattermost
      After=syslog.target network.target postgresql.service

      [Service]
      Type=notify
      WorkingDirectory=/opt/mattermost
      User=mattermost
      ExecStart=/opt/mattermost/bin/mattermost
      PIDFile=/var/spool/mattermost/pid/master.pid
      TimeoutStartSec=3600
      KillMode=mixed
      LimitNOFILE=49152

      [Install]
      WantedBy=multi-user.target

    .. note::
      If you are using MySQL, replace ``postgresql.service`` with ``mysqld.service`` in the ``[unit]`` section.

  c. Set the service file permissions.

    .. code-block:: sh

      sudo chmod 644 /etc/systemd/system/mattermost.service

  d. Reload the systemd services.

    .. code-block:: sh
    
      sudo systemctl daemon-reload

  e. Set Mattermost to start on boot.

    .. code-block:: sh

      sudo systemctl enable mattermost  

11. Start the Mattermost server.

    .. code-block:: sh

    sudo systemctl start mattermost

12. Verify that Mattermost is running.

    .. code-block:: sh

      curl http://localhost:8065

  You should see the HTML that's returned by the Mattermost server.

Now that Mattermost is installed and running, it's time to create the admin user and configure Mattermost for use.
