Prepare your Mattermost Server environment
===========================================

This guide outlines the key preparation steps required before installing the Mattermost Server, focusing on setting up the database and file storage systems.

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    Review software and hardware requirements </deployment-guide/software-hardware-requirements>
    Set up an NGINX proxy </deployment-guide/server/setup-nginx-proxy>
    Configure Mattermost Calls </administration-guide/configure/calls-deployment>
    Set up TLS </deployment-guide/server/setup-tls>
    Use an image proxy </deployment-guide/server/image-proxy>

Before installing Mattermost Server, review the following preparation requirements:

* :doc:`Review software and hardware requirements </deployment-guide/software-hardware-requirements>` - Ensure your system meets the minimum requirements for Mattermost deployment.
* :doc:`Set up an NGINX proxy </deployment-guide/server/setup-nginx-proxy>` - Configure NGINX as a reverse proxy for enhanced security and performance.
* :doc:`Configure Mattermost Calls </administration-guide/configure/calls-deployment>` - Set up real-time communication capabilities for voice and video calls.
* :doc:`Set up TLS </deployment-guide/server/setup-tls>` - Enable secure communication with SSL/TLS encryption.
* :doc:`Use an image proxy </deployment-guide/server/image-proxy>` - Configure image proxy for enhanced privacy and security.

Database preparation
--------------------

PostgreSQL v14+ is required for Mattermost server installations. :doc:`MySQL database support </deployment-guide/server/prepare-mattermost-mysql-database>` is being deprecated starting with Mattermost v11. See the :doc:`PostgreSQL migration </deployment-guide/postgres-migration>` documentation for guidance on migrating from MySQL to PostgreSQL.

1. Create an PostgreSQL server instance. See the `PostgreSQL documentation <https://www.postgresql.org/download/>`_ for details. When the installation is complete, the PostgreSQL server is running, and a Linux user account called postgres has been created.

2. Create the Mattermost database and user:

   a. Access PostgreSQL by running:

      .. code-block:: sh

         sudo -u postgres psql

   b. Create the database:

      .. code-block:: sql

         CREATE DATABASE mattermost WITH ENCODING 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' TEMPLATE=template0;

   If this steps fails with an error message like ``invalid LC_COLLATE locale name: "en_US.UTF-8"``, you need to generate the locale first using ``locale-gen en_US.UTF-8``.

   c. Create the Mattermost user with a secure password:

      .. code-block:: sql

         CREATE USER mmuser WITH PASSWORD 'mmuser-password';

   d. Grant database access to the user:

      .. code-block:: sql

         GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;

   e. If using PostgreSQL v15.x or later, additional grants are required:

      .. code-block:: sql

         ALTER DATABASE mattermost OWNER TO mmuser;
         ALTER SCHEMA public OWNER TO mmuser;
         GRANT USAGE, CREATE ON SCHEMA public TO mmuser;

3. Configure PostgreSQL for remote connections (if database is on a separate server):

   a. Edit ``postgresql.conf`` to allow remote connections:

      .. tab:: Ubuntu/Debian

         Edit ``/etc/postgresql/{version}/main/postgresql.conf``:

         .. code-block:: text

            listen_addresses = '*'

      .. tab:: RHEL/CentOS

         Edit ``/var/lib/pgsql/{version}/data/postgresql.conf``:

         .. code-block:: text

            listen_addresses = '*'

   b. Configure client authentication by editing ``pg_hba.conf``:

      Add the following line, replacing ``{mattermost-server-IP}``:

      .. code-block:: text

         host all all {mattermost-server-IP}/32 md5

4. Restart the PostgreSQL service to apply the configuration changes:

   .. tab:: Ubuntu/Debian

      .. code-block:: sh

         sudo systemctl restart postgresql

   .. tab:: RHEL/CentOS

      .. code-block:: sh

         sudo systemctl restart postgresql

.. important::

  If you are upgrading a major version of Postgres, ensure that ``ANALYZE VERBOSE`` is run on the database post upgrade. This is required to re-populate the ``pg_statistics`` table used to generate optimal query plans. Database performance may suffer if this step is skipped.

Once you've completed the database preparation, return to the :doc:`Linux deployment </deployment-guide/server/deploy-linux>` documentation to continue with your Mattermost server installation.

File storage preparation
-------------------------

Mattermost requires a file storage system for storing user files, images, and attachments. You have several options, including:

- S3-compatibile object storage (recommended)
- Network file storage
- Local file storage

S3-compatible object storage (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For production environments, we recommend using S3-compatible object storage such as:

- Amazon S3
- Digital Ocean Spaces
- Other S3-compatible services

When using S3 storage, you'll need:

1. A bucket created specifically for Mattermost
2. Access credentials (Access Key and Secret Key)
3. Appropriate bucket policies configured
4. The following information for configuration:

   - Bucket name
   - Region (if applicable)
   - Access Key
   - Secret Key
   - Endpoint URL (for non-AWS S3 services)

Network file storage
~~~~~~~~~~~~~~~~~~~~~

For production environments that cannot use S3-compatible object storage, we recommend using a Network Addressable Storage (NAS) solution with Network File System (NFS).

You'll need to prepare an NFS server with a dedicated share for Mattermost (e.g. `/mnt/mattermost_data`) and mount it on all servers that will be running Mattermost.


Local file storage
~~~~~~~~~~~~~~~~~~

For simple deployments, you can use local file storage. However, we don't recommend this for production environments or multi-node deployments.

1. Create a directory for file storage:

   .. code-block:: sh

         sudo mkdir -p /opt/mattermost/data

2. Set appropriate permissions:

   .. code-block:: sh

         sudo chown -R mattermost:mattermost /opt/mattermost/data

(Optional) Use an image proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using an :doc:`image proxy </deployment-guide/server/image-proxy>` means that all requests for images made by Mattermost clients will go through the proxy instead of contacting third-party servers directly. This helps protect user privacy by preventing third-party servers from tracking who views an image. This also prevents the use of tracking pixels (invisible images that do the same thing without the user even seeing an image).

Certain proxy servers also provide a layer of caching which can make loading images faster and more reliable. This caching also helps preserve posts by protecting them from dead images.

Network preparation
--------------------

The following table outlines the network ports and protocols required for Mattermost server:

+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Service Name                                                | Config Setting                        | Port (default)                    | Protocol  | Direction  | Info                                                          |
+=============================================================+=======================================+===================================+===========+============+===============================================================+
| HTTP/Websocket                                              | ServiceSettings.ListenAddress         | 8065/80/443 (TLS)                 | TCP       | Inbound    | External (no proxy) / Internal (with proxy)                   |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+ Usually this requires port 80 and 443 when running HTTPS.     |
|                                                             |                                       |                                   |           |            |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Cluster                                                     | ClusterSettings.GossipPort            | 8074                              | TCP/UDP   | Inbound    | Internal                                                      |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Metrics                                                     | MetricsSettings.ListenAddress         | 8067                              | TCP       | Inbound    | External (no proxy) / Internal (with proxy)                   |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Database                                                    | SqlSettings.DataSource                | 5432 (PostgreSQL) / 3306 (MySQL)  | TCP       | Outbound   | Usually internal (recommended)                                |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| LDAP                                                        | LdapSettings.LdapPort                 | 389                               | TCP/UDP   | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| S3 Storage                                                  | FileSettings.AmazonS3Endpoint         | 443 (TLS)                         | TCP       | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| SMTP                                                        | EmailSettings.SMTPPort                | 10025                             | TCP/UDP   | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Push Notifications                                          | EmailSettings.PushNotificationServer  | 443 (TLS)                         | TCP       | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+

.. note::

   - All outbound ports may vary based on your specific configuration
   - Mattermost can be configured to use an outbound proxy for any HTTP/HTTPS traffic (see below)
   - Calls service may require additional ports

Outbound proxy configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your deployment requires using an outbound proxy, you can configure Mattermost using environment variables:

1. Configure the proxy settings in your service configuration:

   .. code-block:: text

      Environment=HTTP_PROXY=http://proxy.example.com:3128
      Environment=HTTPS_PROXY=https://proxy.example.com:3128
      Environment=NO_PROXY=localhost,127.0.0.1,.internal.example.com

2. For authenticated proxies, include credentials in the URL:

   .. code-block:: text

      Environment=HTTP_PROXY=http://username:password@proxy.example.com:3128
      Environment=HTTPS_PROXY=https://username:password@proxy.example.com:3128

3. The ``NO_PROXY`` variable can include:
   - IP addresses (e.g., ``1.2.3.4``)
   - CIDR ranges (e.g., ``1.2.3.4/8``)
   - Domain names (e.g., ``example.com``)
   - Subdomains (e.g., ``.example.com``)

.. note::

   When using an HTTPS proxy, ensure your Mattermost server has the proxy's root certificate configured to avoid connection issues.

   Example systemd Service Configuration

   .. code-block:: ini

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

      # Configure proxy settings if needed
      #Environment=HTTP_PROXY=http://proxy.example.com:3128
      #Environment=HTTPS_PROXY=https://proxy.example.com:3128
      #Environment=NO_PROXY=localhost,127.0.0.1,.internal.example.com

      # Recommended security options
      ProtectSystem=full
      PrivateTmp=true
      NoNewPrivileges=true

      [Install]
      WantedBy=postgresql.service

System requirements
--------------------

Ensure your system meets these minimum requirements:

- Operating System: 64-bit Linux distribution
- Hardware: 1 vCPU/core with 2GB RAM (supports up to 1,000 users)
- Storage: Minimum 10GB available space
- Database: PostgreSQL v14+
- Network: Reliable internet connection with sufficient bandwidth

See the :doc:`software and hardware requirements </deployment-guide/software-hardware-requirements>` documentation for additional requirements.

Next steps
-----------

Once you've completed these preparation steps, you can proceed with installing the Mattermost server. Choose your preferred installation method:

- :doc:`Deploy with Kubernetes </deployment-guide/server/deploy-kubernetes>`
- :doc:`Deploy on Linux </deployment-guide/server/deploy-linux>`
- :doc:`Deploy with Containers </deployment-guide/server/deploy-containers>`
