.. _install-rhel-71:

=================================
Installing Mattermost on RHEL 7.1
=================================

You can also use these instructions to install Mattermost on CentOS 7, Oracle Linux 7, or Scientific Linux 7. With the exception of the operating system that you install, the process is identical.

.. include:: install-common-intro.rst

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:

.. include:: install-rhel-71-server.rst
.. include:: install-rhel-71-mysql.rst
.. include:: install-rhel-71-postgresql.rst
.. include:: install-rhel-71-mattermost.rst
.. include:: config-mattermost-server.rst
.. include:: config-tls-mattermost.rst
.. include:: install-rhel-nginx.rst
.. include:: config-proxy-nginx.rst
.. include:: config-ssl-http2-nginx.rst
