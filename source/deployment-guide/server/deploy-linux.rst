Deploy Mattermost on Linux
==========================

Mattermost Server can be deployed on Linux in two broad ways: as a package-based install on a host you manage, or as a managed cloud marketplace deployment that provisions a production-ready stack in your own cloud account.

For package-based installs (Manual Install, Ubuntu, RHEL/CentOS), we don't recommend deploying Mattermost Server and the database on the same system in production. These options are best suited to development and testing. The cloud marketplace options provision a separated production stack designed to scale.

Choose your preferred option below for specific deployment instructions:

.. tab:: Manual Install
  :parse-titles:

  .. include:: linux/deploy-tar.rst
    :start-after: :nosearch:

.. tab:: Ubuntu
  :parse-titles:

  .. include:: linux/deploy-ubuntu.rst
    :start-after: :nosearch:

.. tab:: RHEL/CentOS
  :parse-titles:

  .. include:: linux/deploy-rhel.rst
    :start-after: :nosearch:

.. tab:: Azure
  :parse-titles:

  .. include:: linux/deploy-azure-native-vm.rst
    :start-after: :nosearch:

Secure your Mattermost deployment
---------------------------------

Configuring TLS and setting up an NGINX proxy ensures secure communication between clients and your Mattermost server. This setup allows you to serve HTTPS traffic while proxying requests to Mattermost. You don’t need TLS enabled within Mattermost itself as NGINX will handle HTTPS traffic.

1. Install NGINX on the host server. See the :doc:`set up NGINX proxy </deployment-guide/server/setup-nginx-proxy>` documentation for details.
2. Obtain a TLS certificate from a trusted certificate authority (CA) or use a self-signed certificate for testing purposes.
3. Configure NGINX with TLS certificates to serve HTTPS traffic. NGINX serves as a proxy, forwarding requests to the Mattermost application running locally or on a separate server.

.. note::

  See the :doc:`deployment troubleshooting </deployment-guide/deployment-troubleshooting>` documentation for resolutions to common deployment issues.
