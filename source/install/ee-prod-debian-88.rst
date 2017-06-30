.. _install-debian-88:

=========================================================
Installing Mattermost Enterprise Edition on Debian Jessie
=========================================================

Install a production-ready Mattermost system on 1 to 3 machines.

.. include:: install-common-intro.rst

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-debian-88-server.rst
.. include:: install-debian-88-mysql.rst
.. include:: install-debian-88-postgresql.rst
.. include:: install-debian-88-mattermost.rst
.. include:: config-mattermost-server.rst
.. include:: config-tls-mattermost.rst
.. include:: install-nginx.rst
.. include:: config-proxy-nginx.rst
.. include:: config-ssl-http2-nginx.rst
