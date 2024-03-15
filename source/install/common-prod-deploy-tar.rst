:orphan:
:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's being phased out in favor of a dedicated Tarball deploy page linked to the /download page of the website.

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

These instructions outline how to install Mattermost Server on a 64-bit Linux host from a compressed tarball, and assume the IP address of the Mattermost server is 10.10.10.2.

**Minimum system requirements**

- Hardware: 2 vCPUs/cores with 4GB RAM (support for 1,000-2,000 users)
- Database: PostgreSQL v12+ or MySQL v8+
- Network ports required:

   - Application ports 80/443, TLS, TCP Inbound
   - Administrator Console port 8065, TLS, TCP Inbound
   - SMTP port 10025, TCP/UDP Outbound

**Deploy Generic Linux**

1. Install and configure a PostgreSQL or MySQL database. See the following guides for details:

 - :doc:`Prepare your Mattermost PostgreSQL database </install/prepare-mattermost-database>`
 - :doc:`Prepare your Mattermost MySQL database </install/prepare-mattermost-mysql-database>`

2. Log in to the server that will host Mattermost Server and open a terminal window.

3. Download :doc:`the latest version of the Mattermost Server </upgrade/version-archive>`. In the following command, replace ``X.X.X`` with the version that you want to download:
  
   .. code:: bash

    # Enterprise Edition
    wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

    # Team Edition
    wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz

4. Extract the Mattermost Server files.
  
   .. code:: bash
            
    tar -xvzf mattermost*.gz

5. Move the extracted file to the ``/opt`` directory.
  
   .. code:: bash
            
    sudo mv mattermost /opt

6. Create the storage directory for files.

   .. code:: bash
            
    sudo mkdir /opt/mattermost/data
  
.. note::
    
  The storage directory will contain all the files and images that your users post to Mattermost, so you need to make sure that the drive is large enough to hold the anticipated number of uploaded files and images.

7. Set up a system user and group called ``mattermost`` that will run this service, and set the ownership and permissions.
  
  a. Create the Mattermost user and group.
        
     .. code:: bash

        sudo useradd --system --user-group mattermost
  
  b. Set the user and group *mattermost* as the owner of the Mattermost files.
    
     .. code:: bash
            
        sudo chown -R mattermost:mattermost /opt/mattermost
  
  c. Give write permissions to the *mattermost* group.
        
     .. code:: bash
            
        sudo chmod -R g+w /opt/mattermost

8. Set up the database driver in the file ``/opt/mattermost/config/config.json``. Open the file in a text editor and make the following changes:
  
   **If you're using PostgreSQL:**

   Set ``"DriverName"`` to ``"postgres"``
   Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values: ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10",``
  
   **If you're using MySQL:**

   Set ``"DriverName"`` to ``"mysql"``
   Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values. Also make sure that the database name is ``mattermost`` instead of ``mattermost_test``: ``"mmuser:<mmuser-password>@tcp(<host-name-or-IP>:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s"``

9. Test the Mattermost server to make sure everything works.
    
  a. Change to the Mattermost directory.
            
     .. code:: bash
            
      cd /opt/mattermost
            
  b. Start the Mattermost server as the user mattermost.
            
     .. code:: bash
            
      sudo -u mattermost bin/mattermost
  
    When the server starts, it shows some log information and the text ``Server is listening on :8065``. You can stop the server by pressing :kbd:`Ctrl` :kbd:`C` on Windows or Linux, or :kbd:`⌘` :kbd:`C` on Mac, in the terminal window.

10. Set up Mattermost to use *systemd* for starting and stopping.
  
  a. Create a *systemd* unit file.
    
     .. code:: bash
            
      sudo touch /lib/systemd/system/mattermost.service
  
  b. Open the unit file as *root* in a text editor, and copy the following lines into the file.
  
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
    
      * If you're using MySQL, replace ``postgresql.service`` with ``mysql.service`` in two places in the ``[Unit]`` section.
      * If you've installed PostgreSQL or MySQL on a dedicated server, you need to remove the ``After=postgresql.service`` and ``BindsTo=postgresql.service`` or ``After=mysql.service`` and ``BindsTo=mysql.service`` lines in the ``[Unit]`` section or the Mattermost service won't start.
    
  c. Make systemd load the new unit.
    
     .. code:: bash
            
      sudo systemctl daemon-reload
  
  d. Check to make sure that the unit was loaded.
    
     .. code:: bash
            
      sudo systemctl status mattermost.service
    
  You should see an output similar to the following:
    
  .. code-block:: none
                
    mattermost.service - Mattermost
    Loaded: loaded (/lib/systemd/system/mattermost.service; disabled; vendor preset: enabled)
    Active: inactive (dead)
  
  e. Start the service.
    
     .. code:: bash
            
      sudo systemctl start mattermost.service
  
  f. Verify that Mattermost is running.
    
     .. code:: bash
            
      curl http://localhost:8065
    
  You should see the HTML that's returned by the Mattermost server. If a firewall is used, external requests to port 8065 may be blocked. Use ``sudo ufw allow 8065`` to open port 8065.
  
  g. Set Mattermost to start on machine start up.

     .. code:: bash
            
      sudo systemctl enable mattermost.service

Once your Mattermost server is up and running, create your first Mattermost user, :doc:`invite more users </collaborate/manage-channel-members>`, and explore the Mattermost platform. 
