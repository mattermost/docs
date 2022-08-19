.. _install-ubuntu-2004:

Install Mattermost on Ubuntu 20.04 LTS
======================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Install a production-ready Mattermost system on up to three machines.

.. include:: install-common-intro.rst
  :start-after: :nosearch:

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-ubuntu-2004-server.rst
  :start-after: :nosearch:

.. include:: install-ubuntu-2004-mysql.rst
  :start-after: :nosearch:

.. include:: install-ubuntu-2004-postgresql.rst
  :start-after: :nosearch:

.. include:: install-ubuntu-2004-mattermost.rst
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
