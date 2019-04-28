..  _docker-local-machine:

Production Docker Deployment
==============================

Deploy Mattermost using a multi-container production configuration. Docker experience recommended.

For a single-container preview of Mattermost (without email) see `Local Machine Setup using Docker <http://docs.mattermost.com/install/docker-local-machine.html>`__.

If you have any problems installing, see the `troubleshooting guide <https://www.mattermost.org/troubleshoot/>`__. To submit an improvement or correction, click Edit at the top of this page.

Install Docker
----------------------------------------------------

First ensure you have Docker installed on your server (try to run ``docker version``). If not you should follow the Docker documentation to install it :

- `Debian <https://docs.docker.com/install/linux/docker-ce/debian/>`__
- `Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`__
- `CentOS <https://docs.docker.com/install/linux/docker-ce/centos/>`__
- `Fedora <https://docs.docker.com/install/linux/docker-ce/fedora/>`__
- `MacOS <https://docs.docker.com/docker-for-mac/>`__

Docker images
----------------------------------------------------

To run a Mattermost server, you will need 2 Docker images :

- one for the application itself
- one for the database (this is optionnal if you want to use an existing PostgreSQL database)

Those images are available on `Docker Hub <https://hub.docker.com/u/mattermost>`__. If you prefer to build them yourself, you can follow the `instructions on Github <https://github.com/mattermost/mattermost-docker#docker-images>`__. Docker Hub images are :

- `mattemost/mattermost-team-edition <https://hub.docker.com/r/mattermost/mattermost-team-edition>`__ for the application if you want to use Mattermost Team Edition
- `mattemost/mattermost-enterprise-edition <https://hub.docker.com/r/mattermost/mattermost-enterprise-edition>`__ for the application if you want to use Mattermost Enterprise Edition
- `mattermost/mattermost-prod-db <https://hub.docker.com/r/mattermost/mattermost-prod-db>`__ for the database

All images have tags corresponding to the Mattermost version. For example, ``mattemost/mattermost-team-edition:5.7.3`` is Mattermost 5.7.3 Team Edition.


Prepare environment
----------------------------------------------------

The ``app`` container need to communicate with the ``db`` container. In order to do this, we use a custom Docker network to connect both containers.

  .. code-block:: bash

    docker network create mattermost-net

Also, Mattermost application and database need to persists data to disk (database, uploaded files, configuration, etc.). You can use Docker bind-mounts to mount persistent folderq inside the containers. Because the Mattermost application is running with a user having UID and GID ``2000``, you need to prepare the folders before running your images :

  .. code-block:: bash

    mkdir -p /docker/volumes/mattermost/app/{data,logs,config,plugins}
    chown -R 2000:2000 /docker/volumes/mattermost/app

Then you need to choose a database name, user and password. Those values will be transmitted as environment variables to the database and the application.

.. code-block:: bash

  MATTERMOST_DB_USER=mattermost
  MATTERMOST_DB_PASSWORD=tb8Bs64oydFuOvvILGsiEGjnhDA0q4cz
  MATTERMOST_DATABASE=mattermost

**Use custom values here and backup them. If you lost your database credentials, it will require some manual intervention to recover.**

Run Docker containers
----------------------------------------------------

Then you are ready to deploy your Mattermost containers. Because every infrastructure is different, we just provide `docker run` command examples to run the containers. It will give you the information about environment variables and mount points required by the containers, so you will be able to adapt it to your deployment tool (Docker Compose, Docker Swarm, Kubernetes, etc.). If you want deeper information about the images, and other deployment examples, you should check the `Github repository for Mattermost Docker images <https://github.com/mattermost/mattermost-docker>`__.


To deploy the database container, run :

.. code-block:: bash

  docker run -d --name mattermost-db --net mattermost-net --network-alias db \
  -e POSTGRES_USER=$MATTERMOST_DB_USER -e POSTGRES_PASSWORD=$MATTERMOST_DB_PASSWORD -e POSTGRES_DB=$MATTERMOST_DATABASE \
  -v /docker/volumes/mattermost/db/data:/var/lib/postgresql/data -v /etc/localtime:/etc/localtime:ro \
  mattermost/mattermost-prod-db

Then run the application container :

.. code-block:: bash

  docker run -d --name mattermost-app --net mattermost-net \
  -e MM_USERNAME=$MATTERMOST_DB_USER -e MM_PASSWORD=$MATTERMOST_DB_PASSWORD -e MM_DBNAME=$MATTERMOST_DATABASE \
  -v /docker/volumes/mattermost/app/config:/mattermost/config \
  -v /docker/volumes/mattermost/app/data:/mattermost/data \
  -v /docker/volumes/mattermost/app/logs:/mattermost/logs \
  -v /docker/volumes/mattermost/app/plugins:/mattermost/plugins \
  -v /docker/volumes/mattermost/app/client-plugins:/mattermost/client/plugins \
  -v /etc/localtime:/etc/localtime:ro \
  mattermost/mattermost-prod-app

The application is running, you just need to expose it to the outside world now. The ``app`` container serve the Mattermost application on its port ``8000``.

Expose application
----------------------------------------------------

There are a lot of different ways to expose your server : with a reverse-proxy or not, enabling TLS or not (using Let's Encrypt or not), etc. This choice is yours because it depends a lot on your needs and your infrastructure. The only think you need to do is to expose the port ``8000`` of the ``app`` container, by direct binding to the host network, or using a reverse-proxy.
