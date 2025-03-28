Deploy Mattermost on Linux
==========================

Mattermost Server can be deployed on various Linux distributions, providing a flexible and robust platform for smaller teams and non-commercial customers. We don't recommend deploying Mattermost Server and database on a single system for production use, but it is a good option for development and testing purposes.

This page covers deployment options for major Linux distributions and installation methods. Choose your preferred platform below for specific deployment instructions:

.. tab:: Ubuntu

  .. include:: linux/deploy-ubuntu.rst

.. tab:: RHEL/CentOS

  .. include:: linux/deploy-rhel.rst

.. tab:: Generic Linux

  .. include:: linux/deploy-tar.rst

.. tab:: Omnibus Package

  .. include:: linux/deploy-omnibus.rst

.. note::

  - Your Mattermost Server deployments requires a PostgreSQL database. See the :ref:`database preparation <deploy/server/preparations:database preparation>` documentation for details on this prerequisite.
  - See the :doc:`deployment troubleshooting </guides/deployment-troubleshooting>` documentation for resolutions to common deployment issues.