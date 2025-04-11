Prepare your Mattermost Server environment
===========================================

This guide outlines the key preparation steps required before installing the Mattermost Server, focusing on setting up the database and file storage systems.

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

   Review software and hardware requirements </deploy/software-hardware-requirements>
   (Recommended) Set up an NGINX proxy </deploy/server/setup-nginx-proxy>
   (Recommended) Configure Mattermost Calls </configure/calls-deployment>
   (Optional) Set up TLS </deploy/server/setup-tls>
   (Optional) Use an image proxy </deploy/server/image-proxy>
   (Optional) Configure CloudFront to host Mattermost static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>
   (Optional) Use an outbound proxy </configure/using-outbound-proxy>
   (Optional) Use sockets to set up the database </deploy/server/setting-up-socket-based-mattermost-database>

Database preparation
--------------------

Mattermost requires a PostgreSQL database (version 13 or higher). While MySQL was previously supported, PostgreSQL is now the recommended and preferred database.

.. important::

   - PostgreSQL v13+ is required for Mattermost server installations. :doc:`MySQL database support </deploy/server/prepare-mattermost-mysql-database>` is being deprecated starting with Mattermost v11. See the :doc:`PostgreSQL migration </deploy/postgres-migration>` documentation for guidance on migrating from MySQL to PostgreSQL.
   - Learn how to :doc:`use sockets to set up the database </deploy/server/setting-up-socket-based-mattermost-database>`.

1. Create an PostgreSQL server instance:

   .. tab:: AWS

      .. code-block:: sh

         sudo apt update
         sudo apt install postgresql
    
   .. tab:: Azure

      .. code-block:: sh

         sudo apt update
         sudo apt install postgresql

   .. tab:: Ubuntu/Debian

      .. code-block:: sh

         sudo apt update
         sudo apt install postgresql

   .. tab:: RHEL/CentOS

      .. code-block:: sh

         sudo dnf install postgresql-server
         sudo postgresql-setup --initdb

2. Create the Mattermost database and user:

   a. Access PostgreSQL by running:

      .. code-block:: sh

         sudo -u postgres psql

   b. Create the database:

      .. code-block:: sql

         CREATE DATABASE mattermost WITH ENCODING 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' TEMPLATE=template0;

   c. Create the Mattermost user with a secure password:

      .. code-block:: sql

         CREATE USER mmuser WITH PASSWORD 'mmuser-password';

   d. Grant database access to the user:

      .. code-block:: sql

         GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;

   e. If using PostgreSQL v15.x or later, additional grants are required:

      .. code-block:: sql

         ALTER DATABASE mattermost OWNER TO mmuser;
         GRANT USAGE, CREATE ON SCHEMA PUBLIC TO mmuser;

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

.. important::

  If you are upgrading a major version of Postgres, ensure that ``ANALYZE VERBOSE`` is run on the database post upgrade. This is required to re-populate the ``pg_statistics`` table used to generate optimal query plans. Database performance may suffer if this step is skipped.

File storage preparation
-------------------------

Mattermost requires a file storage system for storing user files, images, and attachments. You have several options, including:

- S3-compatibile object storage (recommended)
- local file storage

S3-compatible object storage (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For production environments, we recommend using S3-compatible object storage such as:

- Amazon S3
- MinIO
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

Using an :doc:`image proxy </deploy/server/image-proxy>` means that all requests for images made by Mattermost clients will go through the proxy instead of contacting third-party servers directly. This helps protect user privacy by preventing third-party servers from tracking who views an image. This also prevents the use of tracking pixels (invisible images that do the same thing without the user even seeing an image).

Certain proxy servers also provide a layer of caching which can make loading images faster and more reliable. This caching also helps preserve posts by protecting them from dead images.

Network preparation
--------------------

Ensure the following ports are available:

- Application ports: 80/443 (TCP) for HTTP/HTTPS
- Database port: 5432 (TCP) for PostgreSQL
- SMTP port: 10025 (TCP/UDP) for outbound email

System requirements
--------------------

Ensure your system meets these minimum requirements:

- Operating System: 64-bit Linux distribution
- Hardware: 1 vCPU/core with 2GB RAM (supports up to 1,000 users)
- Storage: Minimum 10GB available space
- Database: PostgreSQL v13+
- Network: Reliable internet connection with sufficient bandwidth

See the :doc:`software and hardware requirements </deploy/software-hardware-requirements>` documentation for additional requirements.

Next steps
-----------

Once you've completed these preparation steps, you can proceed with installing the Mattermost server. Choose your preferred installation method:

- :doc:`Deploy with Kubernetes </deploy/server/deploy-kubernetes>`
- :doc:`Deploy with Containers </deploy/server/deploy-containers>`
- :doc:`Deploy on Linux </deploy/server/deploy-linux>`