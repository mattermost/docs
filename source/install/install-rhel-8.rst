.. _install-rhel-8:

Install Mattermost on RHEL
==========================

.. raw:: html

    <div class="mm-badge mm-badge--combo">

    <div class="mm-badge__plan-deploy">
      <p>
        <img src="../_static/images/badges/flag_icon.svg" alt="" />
        <span>Available on <a href="https://mattermost.com/pricing/">all plans</a></span>
      </p>
      <p>
        <img src="../_static/images/badges/deployment_icon.svg" alt="" />
        <span><a href="https://mattermost.com/download/">Self-hosted</a> deployments</span>
      </p>
    </div>

    <div class="mm-badge__reqs">
      <h3>Minimum system requirements:</h3>
      <ul>
        <li>Operating System: Enterprise Linux 7+, Oracle Linux  6+, Oracle Linux 7+
        <li>Hardware: 1 vCPU/core with 2GB RAM (support for up to 1,000 users)</li>
        <li>Database: PostgreSQL v11+</li>
        <li>Network:
          <ul>
            <li>Application 80/443, TLS, TCP Inbound</li>
            <li>Administrator Console 8065, TLS, TCP Inbound</li>
            <li>SMTP port 10025, TCP/UDP Outbound</li>
          </ul>
        </li>
      </ul>
    </div>

  </div>

.. tip::

  If you are running the Mattermost Server and database on a single system, we recommend the `Mattermost Omnibus install method </install/installing-mattermost-omnibus.html>`__ as this greatly reduces setup and ongoing maintenance.

.. contents:: On this page
  :backlinks: top
  :local:
  :depth: 1

.. note::
  
  You need a PostgreSQL database. See the `database preparation </install/prepare-mattermost-database.html>`__ documentation for details on this prerequisite.

A Mattermost deployment includes 4 steps: `download <#download>`__, `install <#install>`__, `setup <#setup>`__, and `update <#updates>`__.

Download the latest Mattermost Server tarball
---------------------------------------------

.. include:: download-latest-tarball.rst
    :start-after: :nosearch:

Install
-------

Ahead of installing the Mattermost Server, it’s good practice to update all your repositories and, where required, update existing packages by running the following commands:

.. code-block:: none
  :class: mm-code-block 

    sudo dnf update

.. code-block:: none
  :class: mm-code-block 
    
    sudo dnf upgrade

After any updates, and any system reboots, are complete, install the Mattermost Server.

.. include:: install-mattermost-server-tarball.rst
    :start-after: :nosearch:

Setup
-----

.. include:: setup-mattermost-server.rst
    :start-after: :nosearch:

Updates
-------

Updating your Mattermost Server installation when using the tarball requires several manual steps. See the `upgrade Mattermost Server </upgrade/upgrading-mattermost-server.html>`__ documentation for details. 

Remove Mattermost
------------------

If you wish to remove the Mattermost Server for any reason, you must stop the Mattermost Server, back up all important files, and then run this command:

.. code-block:: none
  :class: mm-code-block 

   sudo rm /opt/mattermost

.. note::

	Depending on your configuration, there are several important folders in ``/opt/mattermost`` to backup. These are ``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data``. We strongly recommend you back up these locations before running the ``rm`` command.

You may also remove the Mattermost systemd unit file and the user/group created for running the application.