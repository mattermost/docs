.. _install-rhel-7:

Installing Mattermost on RHEL 7
=================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

You can also use these instructions to install Mattermost on CentOS 7, Oracle Linux 7, or Scientific Linux 7. With the exception of the operating system that you install, the process is identical.

.. include:: install-common-intro.rst
  :start-after: :nosearch:

.. contents:: Install and configure the components in the following order. Note that you need only one database, either PostgreSQL or MySQL.
  :backlinks: top
  :local:

.. include:: install-rhel-7-server.rst
  :start-after: :nosearch:

.. include:: install-rhel-7-mysql.rst
  :start-after: :nosearch:

.. include:: install-rhel-7-postgresql.rst
  :start-after: :nosearch:

.. include:: install-rhel-7-mattermost.rst
  :start-after: :nosearch:

.. include:: config-mattermost-server.rst
  :start-after: :nosearch:

.. include:: config-tls-mattermost.rst
  :start-after: :nosearch:

.. include:: install-rhel-nginx.rst
  :start-after: :nosearch:

.. include:: config-proxy-nginx.rst
  :start-after: :nosearch:

.. include:: config-ssl-http2-nginx.rst
  :start-after: :nosearch:
  
