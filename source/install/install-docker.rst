Deploy Mattermost via Docker
==============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Install Docker
---------------

If you don't have Docker installed, follow the instructions below based on your operating system:

.. tab:: macOS

  Install `Docker for Mac <https://docs.docker.com/desktop/setup/install/mac-install/>`_.

.. tab:: Windows 10

  Install `Docker for Windows <https://docs.docker.com/desktop/setup/install/windows-install/>`_.

.. tab:: Ubuntu

  Follow the `Install Docker Engine on Ubuntu <https://docs.docker.com/engine/install/ubuntu/>`_ documentation, or you can use the Docker package from the Ubuntu repositories:

  .. code-block:: sh

    sudo apt update
    sudo apt install docker.io
    sudo systemctl start docker

.. tab:: Fedora

  Follow the `Install Docker Engine on Fedora <https://docs.docker.com/engine/install/fedora/>`_ documentation, or you can use the Moby package (Moby is the FOSS upstream project to Docker) from the Fedora repositories:

  .. code-block:: sh

    sudo dnf install moby-engine
    sudo systemctl start docker

.. _Deploy Mattermost on Docker:

Deploy Mattermost on Docker for production use
----------------------------------------------

You'll need `Docker Engine <https://docs.docker.com/engine/install/>`__ and `Docker Compose <https://docs.docker.com/compose/install/>`_ (release 1.28 or later).

.. important::

   - The production configuration results in two separate containers: one for the database and one for the application. An optional third container results when using NGINX for reverse proxy.
   - Encountering issues with your Docker deployment? See the :ref:`Docker deployment troubleshooting <install/troubleshooting:docker deployments>` documentation for details.

To deploy Mattermost on Docker:

1. In a terminal window, clone the repository and enter the directory.

   .. code-block:: sh
        
      git clone https://github.com/mattermost/docker
      cd docker

2. Create your ``.env`` file by copying and adjusting the ``env.example`` file.

   .. code-block:: sh
        
      cp env.example .env

.. important::
    
      At a minimum, you must edit the ``DOMAIN`` value in the ``.env`` file to correspond to the domain for your Mattermost server.

3. Create the required directories and set their permissions.

   .. code-block:: sh
        
      mkdir -p ./volumes/app/mattermost/{config,data,logs,plugins,client/plugins,bleve-indexes}
      sudo chown -R 2000:2000 ./volumes/app/mattermost

4. Configure TLS for NGINX *(optional)*. If you're not using the included NGINX reverse proxy, you can skip this step.

   **If creating a new certificate and key:**

   .. code-block:: sh
  
      bash scripts/issue-certificate.sh -d <YOUR_MM_DOMAIN> -o ${PWD}/certs

   To include the certificate and key, uncomment the following lines in your ``.env`` file and ensure they point to the appropriate files.

   .. code-block:: sh
  
      #CERT_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/fullchain.pem
      #KEY_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/privkey.pem

   **If using a pre-existing certificate and key:**

   .. code-block:: sh
  
            mkdir -p ./volumes/web/cert
            cp <PATH-TO-PRE-EXISTING-CERT>.pem ./volumes/web/cert/cert.pem
            cp <PATH-TO-PRE-EXISTING-KEY>.pem ./volumes/web/cert/key-no-password.pem

   To include the certificate and key, ensure the following lines in your ``.env`` file points to the appropriate files.

   .. code-block:: sh
  
            CERT_PATH=./volumes/web/cert/cert.pem
            KEY_PATH=./volumes/web/cert/key-no-password.pem

5. Configure SSO with GitLab *(optional)*. If you want to use SSO with GitLab, and you're using a self-signed certificate, you have to add the PKI chain for your authority. This is required to avoid the ``Token request failed: certificate signed by unknown authority`` error.
      
   To add the PKI chain, uncomment this line in your ``.env`` file, and ensure it points to your ``pki_chain.pem`` file:

   .. code-block:: sh
  
      #GITLAB_PKI_CHAIN_PATH=<path_to_your_gitlab_pki>/pki_chain.pem
        
   Then uncomment this line in your ``docker-compose.yml`` file, and ensure it points to the same ``pki_chain.pem`` file:

   .. code-block:: sh

      # - ${GITLAB_PKI_CHAIN_PATH}:/etc/ssl/certs/pki_chain.pem:ro

6. Deploy Mattermost.

   **Without using the included NGINX:**

   .. code-block:: sh
  
      sudo docker compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d

   To access your new Mattermost deployment, navigate to ``http://<YOUR_MM_DOMAIN>:8065/`` in your browser.

   To shut down your deployment:

   .. code-block:: sh
  
      sudo docker compose -f docker-compose.yml -f docker-compose.without-nginx.yml down

   **Using the included NGINX:**

   .. code-block:: sh
  
      sudo docker compose -f docker-compose.yml -f docker-compose.nginx.yml up -d

   To access your new Mattermost deployment via HTTPS, navigate to ``https://<YOUR_MM_DOMAIN>/`` in your browser.

   To shut down your deployment:

   .. code-block:: sh
  
      sudo docker compose -f docker-compose.yml -f docker-compose.nginx.yml down
      
7. Create your first Mattermost system admin user, :doc:`invite more users </collaborate/manage-channel-members>`, and explore the Mattermost platform. 

Upgrade from ``mattermost-docker``
-----------------------------------

The `mattermost-docker <https://github.com/mattermost/mattermost-docker>`__ GitHub repository is deprecated. Visit the `mattermost/docker <https://github.com/mattermost/docker>`_ GitHub repository to access the official Docker deployment solution for Mattermost.

To migrate from an existing ``mattermost/mattermost-prod-app`` image, we recommend migrating to either ``mattermost/mattermost-enterprise-edition`` or ``mattermost/mattermost-team-edition`` images, which are the official images supported by Mattermost. These images support PostgreSQL 11+ databases, which we know has been a long-running challenge for the community, and you will not lose any features or functionality by moving to these new images.

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

.. code-block:: sh

  sudo chown -R 2000:2000 ./volumes/app/mattermost

If having issues deploying on Docker generally, ensure the docker daemon is enabled and running:

.. code-block:: sh

  sudo systemctl enable --now docker

To remove all data and settings for your Mattermost deployment:

.. code-block:: sh

  sudo rm -rf ./volumes

PostgreSQL
~~~~~~~~~~~

You can change the Postgres username and/or password (recommended) in the ``.env`` file.

TLS & NGINX
~~~~~~~~~~~~

For an in-depth guide to configuring the TLS certificate and key for Nginx, please refer to `this document in the repository <https://github.com/mattermost/docker/blob/main/docs/issuing-letsencrypt-certificate.md>`__.

Further help
~~~~~~~~~~~~~

If you encounter other problems while installing Mattermost, please refer to our :doc:`troubleshooting guide </install/troubleshooting>`.

Trial Mattermost using Docker Preview
--------------------------------------

Looking to a way to evaluate Mattermost in a non-production environment using Docker? We recommend using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`_ to install Mattermost in Preview Mode. 

See the :doc:`trial Mattermost using Docker </install/trial-mattermost-using-docker>` documentation for details.