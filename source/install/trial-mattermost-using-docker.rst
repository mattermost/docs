Trial Mattermost using Docker
=============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. tip::

  Looking to deploy Mattermost in a production environment? See the :doc:`Docker deployment </install/install-docker>` documentation for details.

.. _Preview Mattermost on Docker:

.. include:: common-local-deploy-docker.rst
  :start-after: :nosearch:

Troubleshooting your preview deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Preview Mode** Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. See the :doc:`Configuration Settings </configure/configuration-settings>` documentation to customize your deployment.

To update your Mattermost preview image and container, you must first stop and delete your existing **mattermost-preview** container by running the following commands:

.. code-block:: bash

  docker pull mattermost/mattermost-preview
  docker stop mattermost-preview
  docker rm mattermost-preview

Once the new image is pulled and the container is stopped and deleted you need to run the ``docker run`` command from above.

.. important::
  On Linux, include ``sudo`` in front of all ``docker`` commands.

To access a shell inside the container, run the following command:

.. code-block:: bash

   docker exec -ti mattermost-preview /bin/bash