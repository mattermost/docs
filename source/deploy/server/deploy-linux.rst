Deploy Mattermost on Linux
==========================

Mattermost can be deployed on various Linux distributions, providing a flexible and robust platform for your team communication needs. This guide covers deployment options for major Linux distributions and installation methods.

Choose your preferred platform below for specific deployment instructions:

.. note::

  - If you are running the Mattermost Server and database on a single system, we recommend the **Omnibus Package** method as it greatly reduces setup and ongoing maintenance.
  - You need a PostgreSQL database. See the :ref:`database preparation <deploy/server/preparations:database preparation>` documentation for details on this prerequisite.
  - See the :doc:`deployment troubleshooting </guides/deployment-troubleshooting>` documentation for resolutions to common deployment issues.

.. tab:: Ubuntu

  .. include:: linux/deploy-ubuntu.rst

.. tab:: RHEL/CentOS

  .. include:: linux/deploy-rhel.rst

.. tab:: Generic Linux

  .. include:: linux/deploy-tar.rst

.. tab:: Omnibus Package

  .. include:: linux/deploy-omnibus.rst