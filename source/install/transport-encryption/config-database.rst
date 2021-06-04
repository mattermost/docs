=============================================
Configuring Database Transport Encryption
=============================================

Mattermost is able to encrypt the traffic between the database and the application
using TLS. This guide describes the setup steps for a single, separate MySQL
server.

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Operational Mattermost server or cluster
- Operational MySQL server
- Confirmed connectivity between Mattermost and MySQL server
- Authentication credentials for Mattermost user on MySQL server

Example Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In this scenario there is one Mattermost application server and one MySQL server,
both running Ubuntu 18.04, with the following IPs:

- **transport-encryption-mattermost1:** 10.10.250.146
- **transport-encryption-mysql1:** 10.10.250.148

Configuring MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a first step, connect to both servers with a sudo or root user.

Execute the following command to prepare the server for SSL connections:

``sudo mysql_ssl_rsa_setup --uid=mysql``

This generates self-signed certificates in ``/var/lib/mysql/`` that the MySQL
server uses to encrypt the connection. If you would like to use certificates
from your company CA, please follow the MySQL documentation for configuration steps.

**Note:** Optionally, it can be enforced that all connections must be made via a local
socket connection or TLS. To do this, open ``/etc/mysql/mysql.conf.d/mysqld.cnf``
and append the following line to the file:

``require_secure_transport = ON``

Any connection to the MySQL server must now be made with secure transport enabled.

Last but not least, restart the server and confirm it is up and running:

  .. code-block:: none

    root@transport-encryption-mysql1:~# systemctl restart mysql
    root@transport-encryption-mysql1:~# systemctl status mysql
    ● mysql.service - MySQL Community Server
       Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
       Active: active (running) since Fri 2019-10-18 16:41:25 UTC; 2s ago
      Process: 8380 ExecStart=/usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid (code=exited, status=0/SUCCESS)
      Process: 8360 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exited, status=0/SUCCESS)
     Main PID: 8382 (mysqld)
        Tasks: 27 (limit: 2361)
       CGroup: /system.slice/mysql.service
               └─8382 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid

    Oct 18 16:41:25 transport-encryption-mysql1 systemd[1]: Stopped MySQL Community Server.
    Oct 18 16:41:25 transport-encryption-mysql1 systemd[1]: Starting MySQL Community Server...
    Oct 18 16:41:25 transport-encryption-mysql1 systemd[1]: Started MySQL Community Server.


Configuring Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
On the Mattermost server, open the file ``config.json`` and look for the ``DataSource``
value in the ``SqlSettings`` section. It should look similar to this:

``"DataSource": "mmuser:sad09zusaopdhsad123@tcp(10.10.250.148:3306)/mattermost?charset=utf8mb4,utf8\u0026writeTimeout=30s",``

At the end of the line, we can configure that TLS must be turned on with the ``tls`` flag
which supports the following values:

- true (Require TLS + a trusted certificate)
- false
- skip-verify (Require TLS + accept self-signed)
- preferred (Try TLS, fallback to unencrypted)

In our case we need to use ``skip-verify`` since we use a self-signed certificate.
The configuration setting will now look like this:

``"DataSource": "mmuser:sad09zusaopdhsad123@tcp(10.10.250.148:3306)/mattermost?charset=utf8mb4,utf8\u0026\u0026writeTimeout=30s&tls=skip-verify",``

If you are running Mattermost in a cluster, be sure to update the value on each node
of the cluster. If you are using configuration in the database, be sure to update the
``systemd`` unit file and enable TLS for the configuration store.

Once complete, restart the Mattermost server and ensure the system is operational:

.. code-block:: none

  ubuntu@transport-encryption-mattermost1:~$ sudo systemctl restart mattermost
  ubuntu@transport-encryption-mattermost1:~$ systemctl status mattermost
  ● mattermost.service - Mattermost
     Loaded: loaded (/lib/systemd/system/mattermost.service; static; vendor preset: enabled)
     Active: active (running) since Fri 2019-10-18 16:47:08 UTC; 3s ago
    Process: 3424 ExecStartPre=/opt/mattermost/bin/pre_start.sh (code=exited, status=0/SUCCESS)
   Main PID: 3443 (mattermost)
      Tasks: 20 (limit: 2361)
     CGroup: /system.slice/mattermost.service
             ├─3443 /opt/mattermost/bin/mattermost --config=mysql://mmuser:sad09zusaopdhsad123@tcp(10.10.250.148:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s&tls=skip-verify
             └─3459 plugins/com.mattermost.nps/server/dist/plugin-linux-amd64

  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8637397,"caller":"scheduler/worker.go:36","msg":"Worker started","worker":"Plugins"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8639545,"caller":"jobs/jobs_watcher.go:38","msg":"Watcher Started"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"info","ts":1571417228.8641603,"caller":"jobs/schedulers.go:72","msg":"Starting schedulers."}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8645394,"caller":"app/web_hub.go:436","msg":"Hub for index 0 is starting with goroutine 3923"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8648505,"caller":"app/web_hub.go:436","msg":"Hub for index 1 is starting with goroutine 3924"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8656101,"caller":"web/static.go:31","msg":"Using client directory at /opt/mattermost/client"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"info","ts":1571417228.8681324,"caller":"commands/server.go:105","msg":"Sending systemd READY notification."}
  Oct 18 16:47:08 transport-encryption-mattermost1 systemd[1]: Started Mattermost.
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.9003174,"caller":"jobs/schedulers.go:166","msg":"Next run time for scheduler","scheduler_name":"MigrationsSched
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.9025588,"caller":"jobs/schedulers.go:166","msg":"Next run time for scheduler","scheduler_name":"PluginsSchedule
