:orphan:
:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Preview Mattermost using Docker
-------------------------------

Using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__ is the fastest way to trial Mattermost in **Preview Mode**, and explore product functionality on a single local machine.

.. important::

    This local image is self-contained (i.e., it has an internal database and works out of the box). Dropping a container using this image removes data and configuration as expected. You can see the :doc:`configuration settings </configure/configuration-settings>` documentation to learn more about customizing your trial deployment.
    
    **Preview Mode** shouldn't be used in a production environment, as it uses a known password string, contains other non-production configuration settings, has email disabled, keeps no persistent data (all data lives inside the container), and doesn't support upgrades. 

    If you are planning to use the calling functionality in **Preview Mode** on a non-local environment, you should ensure that the server is running on a secure (HTTPs) connection and that the :ref:`network requirements <configure/calls-deployment:network>` to run calls are met.

1. Install `Docker <https://www.docker.com/get-started/>`__.

2. Once you have Docker, run the following command in a terminal window:

  .. code-block:: bash

    docker run --name mattermost-preview -d --publish 8065:8065 --publish 8443:8443 mattermost/mattermost-preview

3. When Docker is done fetching the image, navigate to ``http://localhost:8065/`` in your browser to preview Mattermost.
4. Select **Don't have an account** in the top right corner of the screen to create an account for your preview instance. If you don't see this option, ensure that the :ref:`Enable open server <configure/authentication-configuration-settings:enable open server>` configuration setting is enabled. This setting is disabled for self-hosted Mattermost deployments by default.
5. Log in to your preview instance with your user credentials.
