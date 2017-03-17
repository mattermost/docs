.. _install-ubuntu-1404:

=========================================
Installing Mattermost on Ubuntu 14.04 LTS
=========================================

Install a production-ready Mattermost system on 1 to 3 machines.

.. include:: install-common-intro.rst

.. contents:: Install and configure the components in the following order. Note that you need only one database, either MySQL or PostgreSQL.
  :backlinks: top
  :local:
  
.. attention:: If you have any issues with these installation instructions, `please see consult our troubleshooting forum. <https://www.mattermost.org/troubleshoot/>`_ To submit and improvement or correction, use the "Edit" button at the top of this page. 
 
.. include:: install-ubuntu-1404-server.rst
.. include:: install-ubuntu-1404-mysql.rst
.. include:: install-ubuntu-1404-postgresql.rst
.. include:: install-ubuntu-1404-mattermost.rst
.. include:: config-mattermost-server.rst
.. include:: config-tls-mattermost.rst
.. include:: install-nginx.rst
.. include:: config-proxy-nginx.rst
.. include:: config-ssl-http2-nginx.rst
