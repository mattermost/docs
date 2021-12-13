..  _docker-local-machine:

Local Machine Setup using Docker
================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The following instructions use Docker to install Mattermost in *Preview Mode* using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__ for exploring product functionality on a single local machine.

.. important::
  This configuration shouldn't be used in production, as it uses a known password string, contains other non-production configuration settings, keeps no persitent data (all data lives inside the container) and doesn't support upgrades. For a production installation with Docker, see the `Mattermost Docker Setup README <https://github.com/mattermost/docker#mattermost-docker-setup>`__.

.. note::
  If you have problems installing Mattermost, see
  the `troubleshooting guide <https://docs.mattermost.com/install/troubleshooting.html>`__. For help with inviting users to your system, see `inviting team members <https://docs.mattermost.com/messaging/managing-members.html>`__ and additional `getting started information for Channels <https://docs.mattermost.com/guides/channels.htmld>`__.

One-line Docker install
-----------------------

If you have Docker set up, Mattermost installs in one line:

.. code:: bash

  docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

When Docker is done fetching the image, open http://localhost:8065/ in your browser.

If you don't have Docker installed, follow the step-by-step instructions below based on your operating system.

.. tabs::

  .. tab:: macOS

    1. Install `Docker for Mac <https://docs.docker.com/installation/mac/>`__

    2. Start the Mattermost container:

    .. code:: bash

      docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

    3. When Docker is done fetching the image and starting the container, open ``http://localhost:8065/`` in your browser.

  .. tab:: Windows 10

    1. Install `Docker for Windows <https://docs.docker.com/installation/windows/>`__

    2. Start the Mattermost container:

    .. code:: bash

      docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

    3. When Docker is done fetching the image and starting the container, open ``http://localhost:8065/`` in your browser.

  .. tab:: Ubuntu

    1. Follow the `Install Docker Engine on Ubuntu <https://docs.docker.com/engine/install/ubuntu/>`__ documentation, or you can use the Docker package from the Ubuntu repositories:

    .. code:: bash

      sudo apt update
      sudo apt install docker.io
      sudo systemctl start docker

    2. Start the Mattermost container:

    .. code:: bash

      sudo docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

    3. When Docker is done fetching the image and starting the container, open ``http://localhost:8065/`` in your browser.

  .. tab:: Fedora

    1. Follow the `Install Docker Engine on Fedora <https://docs.docker.com/engine/installation/linux/fedora/>`__ documentation, or you can use the Moby package (Moby is the FOSS upstream project to Docker) from the Fedora repositories:

    .. code:: bash

      sudo dnf install moby-engine
      sudo systemctl start docker

    2. Start the Mattermost container:

    .. code:: bash

      sudo docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

    3. When Docker is done fetching the image and starting the container, open ``http://localhost:8065/`` in your browser.

Setting up SMTP email (Recommended)
-----------------------------------

The default single-container Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. 

Configuration Settings
----------------------

See the `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to customize your deployment.

Updating Mattermost Preview
---------------------------

To update your Mattermost preview image and container, you must first stop and delete your existing **mattermost-preview** container by running the following commands:

.. code:: bash

  docker pull mattermost/mattermost-preview
  docker stop mattermost-preview
  docker rm mattermost-preview

Once the new image is pulled and the container is stopped and deleted you need to run the ``docker run`` command from above.

.. note::
  On Linux add a ``sudo`` in front of the ``docker`` commands.

Accessing Your Container
------------------------

To access a shell inside the container, run the following command:

.. code:: bash

   docker exec -ti mattermost-preview /bin/bash
