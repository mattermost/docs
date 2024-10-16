Install Mattermost Server using the tarball
===========================================

.. raw:: html

  <div class="mm-badge mm-badge--combo">

    <div class="mm-plans-badge block">
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
        <li>Database: <a href="https://docs.mattermost.com/deploy/postgres-migration.html">PostgreSQL v12+</a></li>
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

.. include:: ../_static/badges/academy-tarball-deployment.rst
  :start-after: :nosearch:

.. tip::

  If you are running the Mattermost Server and database on a single system, we recommend the :doc:`Mattermost Omnibus install method </install/installing-mattermost-omnibus>` as this greatly reduces setup and ongoing maintenance, and uses the Mattermost PPA for updates. More modern installation methods such as the Mattermost Helm Chart or Kubernetes Operator are available and are highly recommended.

.. note::

  You need a PostgreSQL database. See the :doc:`database preparation </install/prepare-mattermost-database>` documentation for details on this prerequisite.

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

Updating your Mattermost Server installation when using the tarball requires several manual steps. See the :doc:`upgrade Mattermost Server </upgrade/upgrading-mattermost-server>` documentation for details.

Remove Mattermost
------------------

If you wish to remove the Mattermost Server for any reason, you must stop the Mattermost Server, back up all important files, and then run this command:

.. code-block:: sh

   sudo rm /opt/mattermost

.. note::

	Depending on your configuration, there are several important folders in ``/opt/mattermost`` to backup. These are ``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data``. We strongly recommend you back up these locations before running the ``rm`` command.

You may also remove the Mattermost systemd unit file and the user/group created for running the application.

Frequently asked questions
--------------------------

.. include:: common-deploy-faq.rst
  :start-after: :nosearch:
