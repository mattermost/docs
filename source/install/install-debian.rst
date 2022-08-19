.. _install-debian:

Installing Mattermost on Debian Buster
=========================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Install a production-ready Mattermost system on 1 to 3 machines.

.. include:: install-common-intro.rst
  :start-after: :nosearch:

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-tar.rst
  :start-after: :nosearch:

.. include:: install-debian-mysql.rst
  :start-after: :nosearch:

.. include:: install-debian-postgresql.rst
  :start-after: :nosearch:

.. include:: config-mattermost-server.rst
  :start-after: :nosearch:

.. include:: config-tls-mattermost.rst
  :start-after: :nosearch:

.. include:: install-nginx.rst
  :start-after: :nosearch:

.. include:: config-proxy-nginx.rst
  :start-after: :nosearch:

.. include:: config-ssl-http2-nginx.rst
  :start-after: :nosearch: