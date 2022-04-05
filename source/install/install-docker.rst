..  _docker-local-machine:

Install Mattermost via Docker
================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Prerequisites
-------------

If you don't have Docker installed, follow the instructions below based on your operating system:

.. tabs::

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

Preview Mattermost on Docker
----------------------------
.. important::
  Follow the `preview instructions <#preview-mattermost>`__ to deploy Mattermost on Docker in **Preview Mode** using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__. **Preview Mode** is for exploring product functionality on a single local machine. This configuration shouldn't be used in production, as it uses a known password string, contains other non-production configuration settings, keeps no persistent data (all data lives inside the container), and doesn't support upgrades.
  
  **When you're ready to use Mattermost, follow the** `production instructions <#deploy-mattermost>`__ **to deploy Mattermost on Docker in your production environment.**

After you install Docker, you can preview Mattermost with one command:

.. code:: bash

  docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

When Docker is done fetching the image, navigate to http://localhost:8065/ in your browser to preview Mattermost.

Troubleshooting
^^^^^^^^^^^^^^^

The **Preview Mode** Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. See the `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to customize your deployment.

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

Deploy Mattermost on Docker For production use
----------------------------------------------

.. important::
  To deploy Mattermost for production, `docker-compose >= 1.28 <https://docs.docker.com/compose/install/>`__ needs to be installed.

1. Clone the repository and enter the directory:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

  git clone https://github.com/mattermost/docker
  cd docker

2. Create your ``.env`` file by copying and adjusting the ``env.example`` file:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

  cp env.example .env

.. important::
  At a minimum, you must edit the ``DOMAIN`` value in the ``.env`` file to correspond to the domain for your Mattermost server.

3. Create the required directories and set their permissions:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

  mkdir -p ./volumes/app/mattermost/{config,data,logs,plugins,client/plugins,bleve-indexes}
  sudo chown -R 2000:2000 ./volumes/app/mattermost

4. Configure TLS for Nginx *(optional)*:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::
  If you're not using the included Nginx reverse proxy, skip this step.

If creating a new certificate and key:
""""""""""""""""""""""""""""""""""""""

.. code:: bash

  bash scripts/issue-certificate.sh -d <YOUR_MM_DOMAIN> -o ${PWD}/certs

To include the certificate and key, uncomment these lines in your ``.env`` file and ensure they point to the appropriate files:

.. code:: bash

  #CERT_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/fullchain.pem
  #KEY_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/privkey.pem

If using a pre-existing certificate and key:
""""""""""""""""""""""""""""""""""""""""""""

.. code:: bash

  mkdir -p ./volumes/web/cert
  cp <PATH-TO-PRE-EXISTING-CERT>.pem ./volumes/web/cert/cert.pem
  cp <PATH-TO-PRE-EXISTING-KEY>.pem ./volumes/web/cert/key-no-password.pem

To include the certificate and key, ensure these lines in your ``.env`` file points to the appropriate files:

.. code:: bash

  CERT_PATH=./volumes/web/cert/cert.pem
  KEY_PATH=./volumes/web/cert/key-no-password.pem

4. Configure SSO with GitLab *(optional)*:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to use SSO with GitLab and you're using a self-signed certificate, you have to add the PKI chain for your authority. This is required to avoid the ``Token request failed: certificate signed by unknown authority`` error.

To add the PKI chain, uncomment this line in your ``.env`` file and ensure it points to your ``pki_chain.pem`` file:

.. code:: bash

  # - ${GITLAB_PKI_CHAIN_PATH}:/etc/ssl/certs/pki_chain.pem:ro


5. Deploy
^^^^^^^^^

Without using the included Nginx:
"""""""""""""""""""""""""""""""""

.. code:: bash

  sudo docker-compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d

To access your new Mattermost deploy, navigate to ``http://<YOUR_MM_DOMAIN>:8065/`` in your browser.

To shut down your deployment:

.. code:: bash

  sudo docker-compose -f docker-compose.yml -f docker-compose.without-nginx.yml down

Using the included Nginx:
"""""""""""""""""""""""""

.. code:: bash

  sudo docker-compose -f docker-compose.yml -f docker-compose.nginx.yml up -d

To access your new Mattermost deploy via HTTPS, navigate to ``https://<YOUR_MM_DOMAIN>/`` in your browser.

To shut down your deployment:

.. code:: bash

  sudo docker-compose -f docker-compose.yml -f docker-compose.nginx.yml down

Troubleshooting
^^^^^^^^^^^^^^^

Docker
""""""

If deploying on an M1 Mac and encountering permission issues in the Docker container, `redo the third step <#create-the-required-directores-and-set-their-permissions>`__ and skip this command:

.. code:: bash

  sudo chown -R 2000:2000 ./volumes/app/mattermost

If having issues deploying on Docker generally, ensure the docker daemon is enabled and running:

.. code:: bash

  sudo systemctl enable --now docker

To remove all data and settings for your Mattermost deployment:

.. code:: bash

  sudo rm -rf ./volumes

Postgres
""""""""

You can change the Postgres username and/or password (recommended) in the ``.env`` file.

TLS & Nginx
"""""""""""

For an in-depth guide to configuring the TLS certificate and key for Nginx, please refer to `this document in the repository <https://github.com/mattermost/docker/blob/main/docs/issuing-letsencrypt-certificate.md>`__.

Installing a different version of Mattermost
""""""""""""""""""""""""""""""""""""""""""""

1. `Follow the appropriate step <#deploy>`__ to shut down your deployment.

2. Run ``git pull`` to fetch any recent changes to the repository, paying attention to any potential ``env.example`` changes.

3. Adjust the ``MATTERMOST_IMAGE_TAG`` in the ``.env`` file to point your desired `enterprise <(https://hub.docker.com/r/mattermost/mattermost-enterprise-edition/tags?page=1&ordering=last_updated>`__ or `team <https://hub.docker.com/r/mattermost/mattermost-team-edition/tags?page=1&ordering=last_updated>`__ image version.

4. `Follow the appropriate step <#deploy>`__ to redeploy Mattermost.

Upgrading from ``mattermost-docker``
""""""""""""""""""""""""""""""""""""

For an in-depth guide to upgrading from the deprecated `mattermost-docker repository <https://github.com/mattermost/mattermost-docker>`__, please refer to `this document <https://github.com/mattermost/docker/blob/main/scripts/UPGRADE.md>`__. For additional help pr questions, please refer to `this issue <https://github.com/mattermost/mattermost-docker/issues/489>`__.

Further help
""""""""""""

If you encounter other problems while installing Mattermost, please refer to our `troubleshooting guide <https://docs.mattermost.com/install/troubleshooting.html>`__. 
