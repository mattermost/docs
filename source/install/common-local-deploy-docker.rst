Preview Mattermost using Docker
===============================

You can install Mattermost server in **Preview Mode** using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__ image to explore Mattermost product functionality on a single local machine.

.. important::

    This local image is self-contained (i.e., it has an internal database and works out of the box). Dropping a container using this image removes data and configuration as expected. You can see the `configuration settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to learn more about customizing your preview deployment.
    
    However, **Preview Mode** shouldn't be used in a production environment, as it uses a known password string, contains other non-production configuration settings, has email disabled, keeps no persistent data (all data lives inside the container), and doesn't support upgrades. 

1. Install `Docker <https://www.docker.com/get-started/>`__.

2. Once you have Docker, run the following command in a terminal window:

  .. code:: bash

    docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

3. When Docker is done fetching the image, navigate to ``http://localhost:8065/`` in your browser to preview Mattermost.

Troubleshooting your preview deployment
---------------------------------------

The **Preview Mode** Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. See the `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to customize your deployment.

To update your Mattermost preview image and container, you must first stop and delete your existing **mattermost-preview** container by running the following commands:

.. code:: bash

  docker pull mattermost/mattermost-preview
  docker stop mattermost-preview
  docker rm mattermost-preview

Once the new image is pulled and the container is stopped and deleted you need to run the ``docker run`` command from above.

.. important::
  On Linux, include ``sudo`` in front of all ``docker`` commands.

To access a shell inside the container, run the following command:

.. code:: bash

   docker exec -ti mattermost-preview /bin/bash
