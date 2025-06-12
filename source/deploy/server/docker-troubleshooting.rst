Docker deployment troubleshooting
====================================

Permission issues on M1 Mac
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're deploying the Mattermost server using Docker on an M1 Mac and encountering permission issues in the Docker container, re-create the required directories and set their permissions, then skip the following command because it causes the deploy to stop working.

.. code-block:: sh

   sudo chown -R 2000:2000 ./volumes/app/mattermost

If you're experiencing issues deploying on Docker generally, ensure the docker daemon is enabled and running:

.. code-block:: sh
  
   sudo systemctl enable --now docker

To remove all data and settings for your Mattermost deployment:

.. code-block:: sh

   sudo rm -rf ./volumes

TLS and NGINX issues
~~~~~~~~~~~~~~~~~~~~

For an in-depth guide to configuring the TLS certificate and key for NGINX, please refer to `this document in the repository <https://github.com/mattermost/docker/blob/main/docs/issuing-letsencrypt-certificate.md>`__.

Install a different version of Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Shut down your deployment.

2. Run ``git pull`` to fetch any recent changes to the repository, paying attention to any potential ``env.example`` changes.

3. Adjust the ``MATTERMOST_IMAGE_TAG`` in the ``.env`` file to point your desired `enterprise <https://hub.docker.com/r/mattermost/mattermost-enterprise-edition/tags?page=1&ordering=last_updated>`__ or `team <https://hub.docker.com/r/mattermost/mattermost-team-edition/tags?page=1&ordering=last_updated>`__ image version.

4. Redeploy Mattermost.

Upgrading from ``mattermost-docker``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For an in-depth guide to upgrading from the deprecated `mattermost-docker repository <https://github.com/mattermost/mattermost-docker>`__, please refer to `this document <https://github.com/mattermost/docker/blob/main/scripts/UPGRADE.md>`__. For additional help, please refer to `this issue <https://github.com/mattermost/mattermost-docker/issues/489>`__.