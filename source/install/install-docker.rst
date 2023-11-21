Install Mattermost via Docker
==============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Install Docker
---------------

If you don't have Docker installed, follow the instructions below based on your operating system:

.. tab:: macOS

  Install `Docker for Mac <https://docs.docker.com/installation/mac/>`__.

.. tab:: Windows 10

  Install `Docker for Windows <https://docs.docker.com/installation/windows/>`__.

.. tab:: Ubuntu

  Follow the `Install Docker Engine on Ubuntu <https://docs.docker.com/engine/install/ubuntu/>`__ documentation, or you can use the Docker package from the Ubuntu repositories:

  .. code:: bash

    sudo apt update
    sudo apt install docker.io
    sudo systemctl start docker

.. tab:: Fedora

  Follow the `Install Docker Engine on Fedora <https://docs.docker.com/engine/installation/linux/fedora/>`__ documentation, or you can use the Moby package (Moby is the FOSS upstream project to Docker) from the Fedora repositories:

  .. code:: bash

    sudo dnf install moby-engine
    sudo systemctl start docker

.. _Preview Mattermost on Docker:

.. include:: common-local-deploy-docker.rst
  :start-after: :nosearch:

Troubleshooting your preview deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Preview Mode** Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. See the `Configuration Settings </configure/configuration-settings.html>`__ documentation to customize your deployment.

To update your Mattermost preview image and container, you must first stop and delete your existing **mattermost-preview** container by running the following commands:

.. code:: bash

  docker pull mattermost/mattermost-preview
  docker stop mattermost-preview
  docker rm mattermost-preview

Once the new image is pulled and the container is stopped and deleted you need to run the ``docker run`` command from above.

.. important::
  On Linux, include ``sudo`` in front of all ``docker`` commands.

To access a shell inside the container, run the following command:

.. code:: bash

   docker exec -ti mattermost-preview /bin/bash

.. _Deploy Mattermost on Docker:

Deploy Mattermost on Docker for production use
----------------------------------------------

.. include:: common-prod-deploy-docker.rst
  :start-after: :nosearch:

Upgrade from ``mattermost-docker``
-----------------------------------

The `mattermost-docker <https://github.com/mattermost/mattermost-docker>`__ repository is deprecated. To migrate from the ``mattermost/mattermost-prod-app`` image, we recommend migrating to either ``mattermost/mattermost-enterprise-edition`` or ``mattermost/mattermost-team-edition`` images, which are the official images supported by Mattermost. These images support PostgreSQL 11+ databases, which we know has been a long-running challenge for the community, and you will not lose any features or functionality by moving to these new images.

For additional help or questions, please refer to `this issue <https://github.com/mattermost/mattermost-docker/issues/489>`__.

Installing a different version of Mattermost
--------------------------------------------

1. Shut down your deployment.

2. Run ``git pull`` to fetch any recent changes to the repository, paying attention to any potential ``env.example`` changes.

3. Adjust the ``MATTERMOST_IMAGE_TAG`` in the ``.env`` file to point your desired `enterprise <https://hub.docker.com/r/mattermost/mattermost-enterprise-edition/tags?page=1&ordering=last_updated>`__ or `team <https://hub.docker.com/r/mattermost/mattermost-team-edition/tags?page=1&ordering=last_updated>`__ image version.

4. Redeploy Mattermost.

Troubleshooting your production deployment
-------------------------------------------

Docker
~~~~~~

If deploying on an M1 Mac and encountering permission issues in the Docker container, `redo the third step <#create-the-required-directores-and-set-their-permissions>`__ and skip this command:

.. code:: bash

  sudo chown -R 2000:2000 ./volumes/app/mattermost

If having issues deploying on Docker generally, ensure the docker daemon is enabled and running:

.. code:: bash

  sudo systemctl enable --now docker

To remove all data and settings for your Mattermost deployment:

.. code:: bash

  sudo rm -rf ./volumes

PostgreSQL
~~~~~~~~~~~

You can change the Postgres username and/or password (recommended) in the ``.env`` file.

TLS & NGINX
~~~~~~~~~~~~

For an in-depth guide to configuring the TLS certificate and key for Nginx, please refer to `this document in the repository <https://github.com/mattermost/docker/blob/main/docs/issuing-letsencrypt-certificate.md>`__.

Further help
~~~~~~~~~~~~~

If you encounter other problems while installing Mattermost, please refer to our `troubleshooting guide </install/troubleshooting.html>`__. 
