:orphan:
:nosearch:

Before you start the Mattermost Server, you need to edit the configuration file. A default configuration file is located at ``/opt/mattermost/config/config.json``. 

We recommend taking a backup of this default config ahead of making changes:

.. code-block:: none
  :class: mm-code-block 
        
    sudo cp /opt/mattermost/config/config.json /opt/mattermost/config/config.defaults.json 

Configure the following properties in this file:

* Set ``DriverName`` to ``"postgres"``. This is the default and recommended database for all Mattermost installations.
* Set ``DataSource`` to ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"`` replacing ``mmuser``, ``<mmuser-password>``, ``<host-name-or-IP>``, and ``mattermost`` with your database name.
* Set your ``"SiteURL"``: The domain name for the Mattermost application (e.g. ``https://mattermost.example.com``).

After modifying the ``config.json`` configuration file, you can now start the Mattermost server:
	
.. code-block:: none
  :class: mm-code-block 

    sudo systemctl start mattermost

Verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that’s returned by the Mattermost Server.

The final step, depending on your requirements, is to run sudo ``systemctl enable mattermost.service`` so that Mattermost will start on system boot. 