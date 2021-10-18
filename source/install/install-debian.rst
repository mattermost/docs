.. _install-debian:

Installing Mattermost on Debian Buster
=========================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Install a production-ready Mattermost system on 1 to 3 machines.

.. include:: install-common-intro.rst

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-debian-server.rst
.. include:: install-debian-mysql.rst
.. include:: install-debian-postgresql.rst
.. include:: install-debian-mattermost.rst
.. include:: config-mattermost-server.rst
.. include:: config-tls-mattermost.rst
.. include:: install-nginx.rst
.. include:: config-proxy-nginx.rst
.. include:: config-ssl-http2-nginx.rst
