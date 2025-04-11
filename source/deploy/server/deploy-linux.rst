Deploy Mattermost on Linux
==========================

Mattermost Server can be deployed on various Linux distributions, providing a flexible and robust platform for smaller teams and non-commercial customers. We don't recommend deploying Mattermost Server and database on a single system for production use, but it is a good option for development and testing purposes.

This page covers deployment options for major Linux distributions and installation methods. Choose your preferred platform below for specific deployment instructions:

.. tab:: Ubuntu

  .. include:: linux/deploy-ubuntu.rst
    :start-after: :nosearch:

.. tab:: RHEL/CentOS

  .. include:: linux/deploy-rhel.rst
    :start-after: :nosearch:

.. tab:: Generic Linux

  .. include:: linux/deploy-tar.rst
    :start-after: :nosearch:

.. tab:: Omnibus Package

  .. include:: linux/deploy-omnibus.rst
    :start-after: :nosearch:

Secure your Mattermost deployment
---------------------------------

Configuring TLS and setting up an NGINX proxy ensures secure communication between clients and your Mattermost server. This setup allows you to serve HTTPS traffic while proxying requests to Mattermost. You don’t need TLS enabled within Mattermost itself as NGINX will handle HTTPS traffic.

1. Install NGINX on the host server. See the :doc:`set up NGINX proxy </deploy/server/setup-nginx-proxy>` documentation for details.
2. Obtain a TLS certificate from a trusted certificate authority (CA) or use a self-signed certificate for testing purposes.
3. Configure NGINX with TLS certificates to serve HTTPS traffic. NGINX serves as a proxy, forwarding requests to the Mattermost application running locally or on a separate server.

.. note::

  - Your Mattermost Server deployments requires a PostgreSQL database. See the :ref:`database preparation <deploy/server/preparations:database preparation>` documentation for details on this prerequisite.
  - See the :doc:`deployment troubleshooting </guides/deployment-troubleshooting>` documentation for resolutions to common deployment issues.