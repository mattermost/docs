.. _install-ubuntu-1604:

Installing Mattermost on Ubuntu 16.04 LTS
=========================================

Install a production-ready Mattermost system on 1 to 3 machines.

.. include:: install-common-intro.rst

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-ubuntu-1604-server.rst
.. include:: install-ubuntu-1604-mysql.rst
.. include:: install-ubuntu-1604-postgresql.rst
.. include:: install-ubuntu-1604-mattermost.rst
.. include:: config-mattermost-server.rst
.. include:: config-tls-mattermost.rst
.. include:: install-nginx.rst
.. include:: config-proxy-nginx.rst
.. include:: config-ssl-http2-nginx.rst
