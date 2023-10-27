Install Mattermost Server using the tarball
===========================================

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

You can install the Mattermost Server on any 64-bit Linux system using the tarball. This is the most flexible installation method, but it comes with the highest effort, normally favored by advanced system administrators. 

.. tip::

  If you are running the Mattermost Server and database on a single system, we recommend the `Mattermost Omnibus install method </install/installing-mattermost-omnibus.html>`__ as this greatly reduces setup and ongoing maintenance, and uses the Mattermost PPA for updates. More modern installation methods such as the Mattermost Helm Chart or Kubernetes Operator are available and are highly recommended.

.. contents:: On this page
  :backlinks: top
  :local:
  :depth: 1

.. note::

  You need a PostgreSQL database. See the `database preparation </install/prepare-mattermost-database.html>`__ documentation for details on this prerequisite.

A Mattermost deployment includes 3 steps: `download <#download>`__, `install <#install>`__, and `setup <#setup>`__.

Download
--------

.. include:: download-latest-tarball.rst
    :start-after: :nosearch:

Install
-------

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

Frequently asked questions
--------------------------

Why doesn't Mattermost start at system boot?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To have the Mattermost Server start at system boot, the systemd until file needs to be enabled. Run the following command:

.. code-block:: none
  :class: mm-code-block 

    sudo systemctl enable mattermost.service

Why does Mattermost fail to start at system boot?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your database is on the same system as your Mattermost Server, we recommend editing the default ``/lib/systemd/system/mattermost.service`` systemd unit file to add ``After=postgresql.service`` and ``BindsTo=postgresql.service`` to the ``[Unit]`` section.

Can I run Mattermost without a proxy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. However, like NGINX, in place, Mattermost binds to 443 instead of 8065. The Mattermost binary requires the correct permissions to do that binding. You must activate the ``CAP_NET_BIND_SERVICE`` capability to allow the new Mattermost binary to bind to ports lower than 1024 by running the following command:

.. code-block:: none
  :class: mm-code-block 

    sudo setcap cap_net_bind_service=+ep ./mattermost/bin/mattermost

.. note::
  
  - We don't recommend deploying Mattermost on a single server unless you have fewer than 200 users.
  - We recommend the `Mattermost Omnibus install method </install/installing-mattermost-omnibus.html>`__ over the tarball if you are running the Mattermost Server and database a single system as this greatly reduces setup and ongoing maintenance.