:orphan:
:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Before you start the Mattermost Server, you need to edit the configuration file. A default configuration file is located at ``/opt/mattermost/config/config.json``. 

We recommend taking a backup of this default config ahead of making changes:

.. code-block:: sh
        
    sudo cp /opt/mattermost/config/config.json /opt/mattermost/config/config.defaults.json 

.. include:: common-default-config-changes.rst
  :start-after: :nosearch:

.. include:: common-configure-support-email.rst
  :start-after: :nosearch:

After modifying the ``config.json`` configuration file, you can now start the Mattermost server:
	
.. code-block:: sh

    sudo systemctl start mattermost

Verify that Mattermost is running: curl ``http://localhost:8065``. You should see the HTML that’s returned by the Mattermost Server.

The final step, depending on your requirements, is to run sudo ``systemctl enable mattermost.service`` so that Mattermost will start on system boot. 
