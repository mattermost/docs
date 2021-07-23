Installing Mattermost Server
----------------------------

Install Mattermost Server on a 64-bit machine.

Assume that the IP address of this server is 10.10.10.2.

**To install Mattermost Server on Ubuntu**

1. Log in to the server that will host Mattermost Server and open a terminal window.
2. Download `the latest version of the Mattermost Server <https://mattermost.com/download/>`__. In the following command, replace ``X.X.X`` with the version that you want to download:
  ``wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz``
3. Extract the Mattermost Server files.
  ``tar -xvzf mattermost*.gz``
4. Move the extracted file to the ``/opt`` directory.
  ``sudo mv mattermost /opt``
5. Create the storage directory for files.
  ``sudo mkdir /opt/mattermost/data``
  .. note::
    The storage directory will contain all the files and images that your users post to Mattermost, so you need to make sure that the drive is large enough to hold the anticipated number of uploaded files and images.
6. Set up a system user and group called ``mattermost`` that will run this service, and set the ownership and permissions.
  a. Create the Mattermost user and group:
    ``sudo useradd --system --user-group mattermost``
  b. Set the user and group *mattermost* as the owner of the Mattermost files:
    ``sudo chown -R mattermost:mattermost /opt/mattermost``
  c. Give write permissions to the *mattermost* group:
    ``sudo chmod -R g+w /opt/mattermost``
7. Set up the database driver in the file ``/opt/mattermost/config/config.json``. Open the file in a text editor and make the following changes:
  -  If you are using PostgreSQL:
    a.  Set ``"DriverName"`` to ``"postgres"``
    b.  Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values:
     ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"``.
  -  If you are using MySQL:
    a.  Set ``"DriverName"`` to ``"mysql"``
    2.  Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values. Also make sure that the database name is ``mattermost`` instead of ``mattermost_test``:
      ``"mmuser:<mmuser-password>@tcp(<host-name-or-IP>:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s"``
8. Also set ``"SiteURL"`` to the full base URL of the site (e.g. ``"https://mattermost.example.com"``).
9. Test the Mattermost server to make sure everything works.
    a. Change to the ``mattermost`` directory:
      ``cd /opt/mattermost``
    b. Start the Mattermost server as the user mattermost:
      ``sudo -u mattermost ./bin/mattermost``
  When the server starts, it shows some log information and the text ``Server is listening on :8065``. You can stop the server by pressing CTRL+C in the terminal window.
10. Setup Mattermost to use *systemd* for starting and stopping.
  a. Create a *systemd* unit file:
    ``sudo touch /lib/systemd/system/mattermost.service``
  b. Open the unit file as root in a text editor, and copy the following lines into the file:
  .. code-block:: none
    [Unit]
    Description=Mattermost
    After=network.target
    After=postgresql.service
    BindsTo=postgresql.service
    [Service]
    Type=notify
    ExecStart=/opt/mattermost/bin/mattermost
    TimeoutStartSec=3600
    Restart=always
    RestartSec=10
    WorkingDirectory=/opt/mattermost
    User=mattermost
    Group=mattermost
    LimitNOFILE=49152
    [Install]
    WantedBy=postgresql.service
  .. note::
    If you are using MySQL, replace ``postgresql.service`` with ``mysql.service`` in 2 places in the ``[Unit]`` section and 1 place in the ``[Install]`` section.
  .. note::
    If you have installed MySQL or PostgreSQL on a dedicated server, then you need to
      - remove ``After=postgresql.service`` and ``BindsTo=postgresql.service`` or ``After=mysql.service`` and ``BindsTo=mysql.service`` lines in the ``[Unit]`` section, and
      - replace the ``WantedBy=postgresql.service`` or ``WantedBy=mysql.service`` line in the ``[Install]`` section with ``WantedBy=multi-user.target``
    or the Mattermost service will not start.
  .. note::
    Setting ``WantedBy`` to your local database service ensures that whenever the database service is started, the Mattermost server starts too. This prevents the Mattermost server from stopping to work after an automatic update of the database.
  c. Make systemd load the new unit.
    ``sudo systemctl daemon-reload``
  d. Check to make sure that the unit was loaded.
    ``sudo systemctl status mattermost.service``
    You should see an output similar to the following:
    .. code-block:: none
      ● mattermost.service - Mattermost
        Loaded: loaded (/lib/systemd/system/mattermost.service; disabled; vendor preset: enabled)
        Active: inactive (dead)
  e. Start the service.
    ``sudo systemctl start mattermost.service``
  f. Verify that Mattermost is running.
    ``curl http://localhost:8065``
    You should see the HTML that's returned by the Mattermost server.
  g. Set Mattermost to start on machine start up.
    ``sudo systemctl enable mattermost.service``
Now that the Mattermost server is up and running, you can do some initial configuration and setup.
