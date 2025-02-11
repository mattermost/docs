Install Mattermost Server on Ubuntu
===================================

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
        <li>Operating System: 20.04 LTS, 22.04 LTS, 24.04 LTS
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

You can install the Mattermost Server using our ``.deb`` signed packages using the Mattermost PPA (Personal Package Archive). Using the Mattermost Personal Package Archive (PPA) not only provides the quickest way to install a Mattermost Server, but also provides automatic updates. This install method is used for both single and clustered installations.

.. include:: common-omnibus-tip.rst
  :start-after: :nosearch:

.. include:: common-postgres-database-important.rst
  :start-after: :nosearch:

This Mattermost deployment includes 4 steps: `add the PPA repository <#add-the-mattermost-server-ppa-repository>`__, `install <#install>`__, `setup <#setup>`__, and `update <#updates>`__.

Add the Mattermost Server PPA repository
----------------------------------------

.. include:: common-gpg-public-key-changed.rst
  :start-after: :nosearch:

In a terminal window, run the following repository setup command to add the Mattermost Server repositories:

.. code-block:: sh

  curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash -s mattermost

This command configures the repositories needed for a PostgreSQL database, configures an NGINX web server to act as a proxy, configures certbot to issue and renew the SSL certificate, and configures the Mattermost Omnibus repository so that you can run the install command.

Install
-------

Ahead of installing the Mattermost Server, it's good practice to update all your repositories and, where required, update existing packages by running the following command:

.. code-block:: sh

    sudo apt update

After any updates and system reboots are complete, you can install the Mattermost Server by running:

.. code-block:: sh

  sudo apt install mattermost -y

You now have the latest Mattermost Server version installed on your system.

The installation path is ``/opt/mattermost``. The package will have added a user and group named ``mattermost``. The required systemd unit file has also been created but will not be set to active.

.. note::

	Since the signed package from the Mattermost repository is used for mulitple installation types, we don't add any dependencies in the systemd unit file. If you are installing the Mattermost server on the same system as your database, you may want to add both ``After=postgresql.service`` and ``BindsTo=postgresql.service`` to the ``[Unit]`` section of the systemd unit file.

Setup
-----

Before you start the Mattermost Server, you need to edit the configuration file. A sample configuration file is located at ``/opt/mattermost/config/config.defaults.json``.

Rename this configuration file with correct permissions:

.. code-block:: sh

  sudo install -C -m 600 -o mattermost -g mattermost /opt/mattermost/config/config.defaults.json /opt/mattermost/config/config.json

.. include:: common-default-config-changes.rst
  :start-after: :nosearch:

.. include:: common-configure-support-email.rst
  :start-after: :nosearch:

After modifying the ``config.json`` configuration file, you can now start the Mattermost Server:

.. code-block:: sh

  sudo systemctl start mattermost

Verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that’s returned by the Mattermost Server.

The final step, depending on your requirements, is to run ``sudo systemctl enable mattermost.service`` so that Mattermost will start on system boot.

.. note::

	The value of the ``sslmode`` property in the ``DataSource`` configuration is entirely dependent on your native environment. Please consult the native environment setup documentation for guidance on its value. The available options for ``sslmode`` are ``disable`` or ``require``. For example, if you are using Amazon Lightsail as your data source, you must set ``sslmode`` to ``require`` to successfully connect to the database.

Updates
-------

When a new Mattermost version is released, run: ``sudo apt update && sudo apt upgrade`` to download and update your Mattermost instance.

.. note::

	When you run the ``sudo apt upgrade`` command, ``mattermost-server`` will be updated along with any other packages. We strongly recommend you stop the Mattermost Server before running the ``apt`` command using ``sudo systemctl stop mattermost``.

Remove Mattermost
------------------

If you wish to remove the Mattermost Server for any reason, you can run this command:

.. code-block:: sh

    sudo apt remove --purge mattermost

Frequently asked questions
--------------------------

.. include:: common-deploy-faq.rst
  :start-after: :nosearch:
