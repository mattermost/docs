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

   .. important::

      **For production environments**, we recommend using specific version tags such as ``MATTERMOST_IMAGE_TAG=release-10.5`` rather than generic tags like ``MATTERMOST_IMAGE_TAG=release-10``. Generic ``release-x`` tags are intended for development use only and do not automatically receive new patch releases within that major version. Using specific version tags ensures a more reproducible and deterministic environment for your production deployment.

4. Redeploy Mattermost.

Unintentional version downgrades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you experience an unintentional downgrade when using generic ``MATTERMOST_IMAGE_TAG=release-x`` tags, this is because these tags are designed for development use and may not point to the latest patch release within that major version.

**Solution**: Use a more specific version tag for your Docker image, such as ``MATTERMOST_IMAGE_TAG=release-10.5``, to avoid unexpected version changes and ensure consistent deployments.

.. note::

   A `pipeline improvement <https://github.com/mattermost/mattermost/issues/30656>`__ is in progress to ensure that generic ``release-x`` tags are updated to the latest version from the corresponding release branch. Once this improvement is implemented, the behavior of these tags will be more predictable.

Upgrading from ``mattermost-docker``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For an in-depth guide to upgrading from the deprecated `mattermost-docker repository <https://github.com/mattermost/mattermost-docker>`__, please refer to `this document <https://github.com/mattermost/docker/blob/main/scripts/UPGRADE.md>`__. For additional help, please refer to `this issue <https://github.com/mattermost/mattermost-docker/issues/489>`__.