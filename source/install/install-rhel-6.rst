:orphan:

.. _install-rhel-6:

Installing Mattermost on RHEL 6
=================================

.. warning::
  RHEL 6 has approached its End of Life in December 2020.
  Because of this, we don't recommend installing new instances of Mattermost on RHEL 6.

You can use these instructions to install Mattermost on CentOS 6, Oracle Linux 6, or Scientific Linux 6. With the exception of the operating system that you install, the process is identical.

.. include:: install-common-intro.rst

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-rhel-6-server.rst
.. include:: install-rhel-6-mysql.rst
.. include:: install-rhel-6-postgresql.rst
.. include:: install-rhel-6-mattermost.rst
.. include:: config-mattermost-server.rst
.. include:: config-tls-mattermost.rst
.. include:: install-rhel-nginx.rst
.. include:: config-proxy-nginx.rst
.. include:: config-ssl-http2-nginx.rst
