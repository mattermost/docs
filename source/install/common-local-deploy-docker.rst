:nosearch:
.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Preview Mattermost using Docker
-------------------------------

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

You can install Mattermost server in **Preview Mode** using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__ image to explore Mattermost product functionality on a single local machine.

.. important::

    This local image is self-contained (i.e., it has an internal database and works out of the box). Dropping a container using this image removes data and configuration as expected. You can see the `configuration settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to learn more about customizing your preview deployment.
    
    However, **Preview Mode** shouldn't be used in a production environment, as it uses a known password string, contains other non-production configuration settings, has email disabled, keeps no persistent data (all data lives inside the container), and doesn't support upgrades. 

1. Install `Docker <https://www.docker.com/get-started/>`__.

2. Once you have Docker, run the following command in a terminal window:

  .. code:: bash

    docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

3. When Docker is done fetching the image, navigate to ``http://localhost:8065/`` in your browser to preview Mattermost.