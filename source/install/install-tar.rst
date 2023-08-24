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

.. contents:: On this page:
  :backlinks: top
  :local:
  :depth: 1

Deployment includes 3 steps: `download <#download>`__, `install <#install>`__, and `setup <#setup>`__.

Download
--------

In a terminal window, ssh onto the system that will host the Mattermost Server. 

Using ``wget``, download the Mattermost Server release you want to install.

.. tabs::

  .. tab:: Latest release

    .. raw:: html

      <div class="mm-code-copy mm-code-copy--long" data-click-method="Tarball" data-click-command="Download the latest release">

        <div class="mm-code-copy__wrapper">
          <code class="mm-code-copy__text mm-code-copy__trigger" data-click-el="Snippet">
          wget https://releases.mattermost.com/8.0.2/mattermost-8.0.2-linux-amd64.tar.gz
          </code>
          <span class="mm-code-copy__copied-notice">Copied to clipboard</span>
        </div>

        <button class="mm-button mm-code-copy__trigger" data-click-el="Button">
        <svg aria-hidden="true" width="17" height="18" viewBox="0 0 17 18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="0.5" y="0.5" width="10.2972" height="10.8284" rx="0.5" stroke="white"/><rect x="6.1489" y="6.41418" width="10.2972" height="10.8284" rx="0.5" stroke="white"/></svg>
          <span>Copy to clipboard<span>
        </button>

      </div>

  .. tab:: Current ESR

    .. raw:: html

      <div class="mm-code-copy mm-code-copy--long" data-click-method="Tarball" data-click-command="Download the current ESR">

        <div class="mm-code-copy__wrapper">
          <code class="mm-code-copy__text mm-code-copy__trigger" data-click-el="Snippet">
            wget https://releases.mattermost.com/7.8.9/mattermost-7.8.9-linux-amd64.tar.gz
          </code>
          <span class="mm-code-copy__copied-notice">Copied to clipboard</span>
        </div>

        <button class="mm-button mm-code-copy__trigger" data-click-el="Button">
          <svg aria-hidden="true" width="17" height="18" viewBox="0 0 17 18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="0.5" y="0.5" width="10.2972" height="10.8284" rx="0.5" stroke="white"/><rect x="6.1489" y="6.41418" width="10.2972" height="10.8284" rx="0.5" stroke="white"/></svg>
          <span>Copy to clipboard<span>
        </button>

      </div>

  .. tab:: Older releases

    If you are looking for an older release, these can be found in our `version archive </upgrade/version-archive.html>`__ documentation.

    - `Enterprise Edition releases </upgrade/version-archive.html#mattermost-enterprise-edition>`__
    - `Team Edition releases </upgrade/version-archive.html#mattermost-team-edition>`__
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

.. tip::
	
	We recommend the `Mattermost Omnibus install method </install/installing-mattermost-omnibus.html>`__ over the tarball if you are running the Mattermost Server and database a single system as this greatly reduces setup and ongoing maintenance.
