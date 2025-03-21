Preparing Your Mattermost Server Environment
=========================================

This guide outlines the key preparation steps required before installing Mattermost Server, focusing on setting up your database and file storage systems.

Database Preparation
------------------

Mattermost requires a PostgreSQL database (version 12 or higher). While MySQL was previously supported, PostgreSQL is now the recommended and preferred database.

.. important::

    PostgreSQL v12+ is required for Mattermost server installations. MySQL support is being deprecated starting with Mattermost v11.


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

   .. tab:: Red Hat/CentOS
   
      .. code-block:: sh

         sudo dnf install postgresql-server
         sudo postgresql-setup --initdb

2. Create the Mattermost database and user:

   a. Access PostgreSQL by running:

      .. code-block:: sh

         sudo -u postgres psql

   b. Create the database:

      .. code-block:: sql

         CREATE DATABASE mattermost;

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

   a. Edit postgresql.conf to allow remote connections:
      
      .. tab:: Ubuntu/Debian
      
         Edit ``/etc/postgresql/{version}/main/postgresql.conf``:
         
         .. code-block:: text

            listen_addresses = '*'

      .. tab:: Red Hat/CentOS
      
         Edit ``/var/lib/pgsql/{version}/data/postgresql.conf``:
         
         .. code-block:: text

            listen_addresses = '*'

   b. Configure client authentication by editing pg_hba.conf:
      
      Add the following line, replacing {mattermost-server-IP}:
      
      .. code-block:: text

         host all all {mattermost-server-IP}/32 md5

File Storage Preparation
----------------------

Mattermost requires a file storage system for storing user files, images, and attachments. You have several options:

Local File Storage
~~~~~~~~~~~~~~~~

For simple deployments, you can use local file storage. However, this is not recommended for production environments or multi-node deployments.

1. Create a directory for file storage:

   .. code-block:: sh

      sudo mkdir -p /opt/mattermost/data

2. Set appropriate permissions:

   .. code-block:: sh

      sudo chown -R mattermost:mattermost /opt/mattermost/data

S3-Compatible Object Storage (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Network Preparation
-----------------

Ensure the following ports are available:

- Application ports: 80/443 (TCP) for HTTP/HTTPS
- Database port: 5432 (TCP) for PostgreSQL
- SMTP port: 10025 (TCP/UDP) for outbound email

System Requirements
-----------------

Ensure your system meets these minimum requirements:

- Operating System: 64-bit Linux distribution
- Hardware: 1 vCPU/core with 2GB RAM (supports up to 1,000 users)
- Storage: Minimum 10GB available space
- Database: PostgreSQL v12+
- Network: Reliable internet connection with sufficient bandwidth

Next Steps
---------

Once you've completed these preparation steps, you can proceed with installing the Mattermost server. Choose your preferred installation method:

- :doc:`Install using Docker </deploy/server/containers/install-docker>`
- :doc:`Install on Ubuntu </deploy/server/virtual-machines/install-ubuntu>`
- :doc:`Install on RHEL </deploy/server/virtual-machines/install-rhel>`
- :doc:`Install using Kubernetes </deploy/server/kubernetes/install-kubernetes>` 