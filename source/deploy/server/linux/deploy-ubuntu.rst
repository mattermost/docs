:orphan:
:nosearch:

.. raw:: html

    <div class="mm-badge mm-badge--combo">

    <div class="mm-badge__reqs">
      <h3>Minimum system requirements:</h3>
      <ul>
        <li>Operating System: 20.04 LTS, 22.04 LTS, 24.04 LTS
        <li>Hardware: 1 vCPU/core with 2GB RAM (support for up to 1,000 users)</li>
        <li>Database: <a href="https://docs.mattermost.com/deploy/postgres-migration.html">PostgreSQL v13+</a></li>
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

You can deploy Mattermost server using our ``.deb`` signed packages using the Mattermost PPA (Personal Package Archive). This is the quickest way to install a Mattermost Server that provides automatic updates. This install method is used for both single and clustered installations, as you can tools like Packer for a clustered deployment.

.. tip::

  Alternatively, an **Omnibus Package** deployment bundles together all required components to greatly reduce setup and ongoing maintenance, including Mattermost Server, a PostgreSQL database, NGINX as the application proxy, a custom CLI, and ansible recipes to configure and connect these components.

This Mattermost deployment includes 4 steps: add the PPA repository, install Mattermost server, configure the server, and update the server.

Step 1: Add the Mattermost Server PPA repository
-------------------------------------------------

.. important::

  The GPG public key has changed. You can `import the new public key <https://deb.packages.mattermost.com/pubkey.gpg>`_ or run the automatic Mattermost PPA repository setup script provided below. Depending on your setup, additional steps may also be required, particularly for installations that didn't rely on the repository setup script. We recommend deleting the old key from ``/etc/apt/trusted.gpg.d`` before adding the apt repository.

  - For Ubuntu Focal - 20.04 LTS:

    ``sudo apt-key del A1B31D46F0F3A10B02CF2D44F8F2C31744774B28``

    ``curl -sL -o- https://deb.packages.mattermost.com/pubkey.gpg | gpg --dearmor | sudo apt-key add``

  - For Ubuntu Jammy - 22.04 LTS and Ubuntu Noble - 24.04 LTS:

    ``sudo rm /usr/share/keyrings/mattermost-archive-keyring.gpg``

    ``curl -sL -o- https://deb.packages.mattermost.com/pubkey.gpg |  gpg --dearmor | sudo tee /usr/share/keyrings/mattermost-archive-keyring.gpg > /dev/null``

In a terminal window, run the following repository setup command to add the Mattermost Server repositories:

.. code-block:: sh

  curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash -s mattermost

This command configures the repositories needed for a PostgreSQL database, configures an NGINX web server to act as a proxy, configures certbot to issue and renew the SSL certificate, and configures the Mattermost Omnibus repository so that you can run the install command.

Step 2: Instal Mattermost server
--------------------------------

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

Step 3: Configure the server
----------------------------

Before you start the Mattermost Server, you need to edit the configuration file. A sample configuration file is located at ``/opt/mattermost/config/config.defaults.json``.

Rename this configuration file with correct permissions:

.. code-block:: sh

  sudo install -C -m 600 -o mattermost -g mattermost /opt/mattermost/config/config.defaults.json /opt/mattermost/config/config.json

Configure the following properties in this file:

* Under ``SqlSettings``, set ``DriverName`` to ``"postgres"``. This is the default and recommended database for all Mattermost installations.
* Under ``SqlSettings``, set ``DataSource`` to ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"`` replacing ``mmuser``, ``<mmuser-password>``, ``<host-name-or-IP>`` and ``mattermost`` with your database name.
* Under ``ServiceSettings``, set ``"SiteURL"``: The domain name for the Mattermost application (e.g. ``https://mattermost.example.com``).

We recommend configuring the `Support Email <https://docs.mattermost.com/administration/config-settings.html#support-email>`_ under ``SupportSettings``, set ``"SupportEmail"``. This is the email address your users will contact when they need help.

After modifying the ``config.json`` configuration file, you can now start the Mattermost Server:

.. code-block:: sh

  sudo systemctl start mattermost

Verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that's returned by the Mattermost Server.

The final step, depending on your requirements, is to run ``sudo systemctl enable mattermost.service`` so that Mattermost will start on system boot.

.. note::

	The value of the ``sslmode`` property in the ``DataSource`` configuration is entirely dependent on your native environment. Please consult the native environment setup documentation for guidance on its value. The available options for ``sslmode`` are ``disable`` or ``require``. For example, if you are using Amazon Lightsail as your data source, you must set ``sslmode`` to ``require`` to successfully connect to the database.

Step 4: Update the server
-------------------------

When a new Mattermost version is released, run: ``sudo apt update && sudo apt upgrade`` to download and update your Mattermost instance.

.. note::

  When you run the ``sudo apt upgrade`` command, ``mattermost-server`` will be updated along with any other packages. We strongly recommend you stop the Mattermost Server before running the ``apt`` command using ``sudo systemctl stop mattermost``.

Remove Mattermost
-----------------

Run the following command to remove the Mattermost Server:

.. code-block:: sh

  sudo apt remove --purge mattermost