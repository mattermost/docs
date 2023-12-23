:orphan:
:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

You'll need `Docker Engine <https://docs.docker.com/engine/install/>`__ and `Docker Compose <https://docs.docker.com/compose/install/>`__ (release 1.28 or later) Follow the steps in the `Mattermost Docker Setup README <https://github.com/mattermost/docker#mattermost-docker-setup>`__ or follow the steps below.

.. important::

   - The production configuration results in two separate containers: one for the database and one for the application. An optional third container results when using NGINX for reverse proxy.
   - Encountering issues with your Docker deployment? See the `Docker deployment troubleshooting </install/troubleshooting.html#docker-deployments>`__ documentation for details.
      
1. In a terminal window, clone the repository and enter the directory.

   .. code:: bash
        
      git clone https://github.com/mattermost/docker
      cd docker

2. Create your ``.env`` file by copying and adjusting the ``env.example`` file.

   .. code:: bash
        
      cp env.example .env

.. important::
    
      At a minimum, you must edit the ``DOMAIN`` value in the ``.env`` file to correspond to the domain for your Mattermost server.

3. Create the required directories and set their permissions.

   .. code:: bash
        
      mkdir -p ./volumes/app/mattermost/{config,data,logs,plugins,client/plugins,bleve-indexes}
      sudo chown -R 2000:2000 ./volumes/app/mattermost

4. Configure TLS for NGINX *(optional)*. If you're not using the included NGINX reverse proxy, you can skip this step.

   **If creating a new certificate and key:**

   .. code:: bash
  
      bash scripts/issue-certificate.sh -d <YOUR_MM_DOMAIN> -o ${PWD}/certs

   To include the certificate and key, uncomment the following lines in your ``.env`` file and ensure they point to the appropriate files.

   .. code:: bash
  
      #CERT_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/fullchain.pem
      #KEY_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/privkey.pem

   **If using a pre-existing certificate and key:**

   .. code:: bash
  
            mkdir -p ./volumes/web/cert
            cp <PATH-TO-PRE-EXISTING-CERT>.pem ./volumes/web/cert/cert.pem
            cp <PATH-TO-PRE-EXISTING-KEY>.pem ./volumes/web/cert/key-no-password.pem

   To include the certificate and key, ensure the following lines in your ``.env`` file points to the appropriate files.

   .. code:: bash
  
            CERT_PATH=./volumes/web/cert/cert.pem
            KEY_PATH=./volumes/web/cert/key-no-password.pem

5. Configure SSO with GitLab *(optional)*. If you want to use SSO with GitLab, and you're using a self-signed certificate, you have to add the PKI chain for your authority. This is required to avoid the ``Token request failed: certificate signed by unknown authority`` error.
      
   To add the PKI chain, uncomment this line in your ``.env`` file, and ensure it points to your ``pki_chain.pem`` file:

   .. code:: bash
  
      #GITLAB_PKI_CHAIN_PATH=<path_to_your_gitlab_pki>/pki_chain.pem
        
   Then uncomment this line in your ``docker-compose.yml`` file, and ensure it points to the same ``pki_chain.pem`` file:

   .. code:: bash

      # - ${GITLAB_PKI_CHAIN_PATH}:/etc/ssl/certs/pki_chain.pem:ro

6. Deploy Mattermost.

   **Without using the included NGINX:**

   .. code:: bash
  
      sudo docker compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d

   To access your new Mattermost deployment, navigate to ``http://<YOUR_MM_DOMAIN>:8065/`` in your browser.

   To shut down your deployment:

   .. code:: bash
  
      sudo docker compose -f docker-compose.yml -f docker-compose.without-nginx.yml down

   **Using the included NGINX:**

   .. code:: bash
  
      sudo docker compose -f docker-compose.yml -f docker-compose.nginx.yml up -d

   To access your new Mattermost deployment via HTTPS, navigate to ``https://<YOUR_MM_DOMAIN>/`` in your browser.

   To shut down your deployment:

   .. code:: bash
  
      sudo docker compose -f docker-compose.yml -f docker-compose.nginx.yml down
      
7. Create your first Mattermost System Admin user, `invite more users </collaborate/manage-channel-members.html>`__, and explore the Mattermost platform. 