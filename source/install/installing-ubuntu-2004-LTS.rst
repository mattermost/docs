.. _install-ubuntu-2004:

Installing Mattermost on Ubuntu 20.04 LTS
=========================================

Install a production-ready Mattermost system on up to three machines.

.. include:: install-common-intro.rst

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-ubuntu-2004-server.rst
.. include:: install-ubuntu-2004-mysql.rst
.. include:: install-ubuntu-2004-postgresql.rst
.. include:: install-ubuntu-1604-mattermost.rst
.. include:: config-mattermost-server.rst
.. include:: config-tls-mattermost.rst
.. include:: install-nginx.rst
.. include:: config-proxy-nginx.rst
.. include:: config-ssl-http2-nginx.rst
