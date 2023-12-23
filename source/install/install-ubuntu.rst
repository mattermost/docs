Install Mattermost Server on Ubuntu
===================================

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
        <li>Operating System: 18.04 LTS, 20.04 LTS, 22.04 LTS
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

You can install the Mattermost Server using our ``.deb`` signed packages using the Mattermost PPA (Personal Package Archive). Using the Mattermost Personal Package Archive (PPA) not only provides the quickest way to install a Mattermost Server, but also provides automatic updates. This install method is used for both single and clustered installations.

.. tip::

  If you are running the Mattermost Server and database on a single system, we recommend the `Mattermost Omnibus install method </install/installing-mattermost-omnibus.html>`__ as this greatly reduces setup and ongoing maintenance.

.. note::
  
  You need a PostgreSQL database. See the `database preparation </install/prepare-mattermost-database.html>`__ documentation for details on this prerequisite.

A Mattermost deployment includes 4 steps: `add the PPA repository <#add-the-mattermost-server-ppa-repository>`__, `install <#install>`__, `setup <#setup>`__, and `update <#updates>`__.

Add the Mattermost Server PPA repository
----------------------------------------

In a terminal window, run the following command to add the Mattermost Server repositories:

.. raw:: html

  <div class="mm-code-copy mm-code-copy--long" data-click-method="Ubuntu" data-click-command="Add the Mattermost Server PPA repository">

    <div class="mm-code-copy__wrapper">
      <code class="mm-code-copy__text mm-code-copy__trigger" data-click-el="Snippet">
        curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash -s mattermost
      </code>
      <span class="mm-code-copy__copied-notice">Copied to clipboard</span>
    </div>

    <button class="mm-button mm-code-copy__trigger" data-click-el="Button">
      <svg aria-hidden="true" width="17" height="18" viewBox="0 0 17 18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="0.5" y="0.5" width="10.2972" height="10.8284" rx="0.5" stroke="white"/><rect x="6.1489" y="6.41418" width="10.2972" height="10.8284" rx="0.5" stroke="white"/></svg>
      <span>Copy to clipboard<span>
    </button>

  </div>

Install
-------

Ahead of installing the Mattermost Server, it's good practice to update all your repositories and, where required, update existing packages by running the following command:

.. code-block:: none
  :class: mm-code-block 

    sudo apt update

After any updates, and any system reboots, are complete, installing the Mattermost Server is now a single command:

.. raw:: html

  <div class="mm-code-copy mm-code-copy--long" data-click-method="Ubuntu" data-click-command="Install - sudo apt install">

    <div class="mm-code-copy__wrapper">
      <code class="mm-code-copy__text mm-code-copy__trigger" data-click-el="Snippet">
        sudo apt install mattermost -y
      </code>
      <span class="mm-code-copy__copied-notice">Copied to clipboard</span>
    </div>

    <button class="mm-button mm-code-copy__trigger" data-click-el="Button">
      <svg aria-hidden="true" width="17" height="18" viewBox="0 0 17 18" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="0.5" y="0.5" width="10.2972" height="10.8284" rx="0.5" stroke="white"/><rect x="6.1489" y="6.41418" width="10.2972" height="10.8284" rx="0.5" stroke="white"/></svg>
      <span>Copy to clipboard<span>
    </button>

  </div>

You now have the latest Mattermost Server version installed on your system.

The installation path is ``/opt/mattermost``. The package will have added a user and group named ``mattermost``. The required systemd unit file has also been created but will not be set to active.

.. note::
	
	Since the signed package from the Mattermost repository is used for mulitple installation types, we don't add any dependencies in the systemd unit file. If you are installing the Mattermost server on the same system as your database, you may want to add both ``After=postgresql.service`` and ``BindsTo=postgresql.service`` to the ``[Unit]`` section of the systemd unit file.

Setup
-----

Before you start the Mattermost Server, you need to edit the configuration file. A sample configuration file is located at ``/opt/mattermost/config/config.defaults.json``. 

Rename this configuration file with correct permissions:

.. code-block:: none
  :class: mm-code-block 

  sudo install -C -m 600 -o mattermost -g mattermost /opt/mattermost/config/config.defaults.json /opt/mattermost/config/config.json

Configure the following properties in this file:

* Set ``DriverName`` to ``"postgres"``. This is the default and recommended database for all Mattermost installations.
* Set ``DataSource`` to ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"`` replacing ``mmuser``, ``<mmuser-password>``, ``<host-name-or-IP>`` and ``mattermost`` with your database name.
* Set ``"SiteURL"``: The domain name for the Mattermost application (e.g. ``https://mattermost.example.com``).

After modifying the ``config.json`` configuration file, you can now start the Mattermost Server:
	
.. code-block:: none
  :class: mm-code-block 

  sudo systemctl start mattermost

Verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that’s returned by the Mattermost Server.

The final step, depending on your requirements, is to run ``sudo systemctl enable mattermost.service`` so that Mattermost will start on system boot. 

Updates
-------

When a new Mattermost version is released, run: ``sudo apt update && sudo apt upgrade`` to download and update your Mattermost instance.

.. note::
	
	When you run the ``sudo apt uprade`` command, ``mattermost-server`` will be updated along with any other packages. We strongly recommend you stop the Mattermost Server before running the ``apt`` command using ``sudo systemctl stop mattermost-server``.

Remove Mattermost
------------------

If you wish to remove the Mattermost Server for any reason, you can run this command:

.. code-block:: none
  :class: mm-code-block 

    sudo apt remove --purge mattermost

Frequently asked questions
--------------------------

.. include:: common-deploy-faq.rst
  :start-after: :nosearch: