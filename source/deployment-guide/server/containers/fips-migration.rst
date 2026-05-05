Migrate an existing deployment to FIPS-compliant containers
============================================================

.. include:: ../../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

From Mattermost v11, each release ships in two image variants: a standard Enterprise build (``mattermost/mattermost-enterprise-edition``) and a FIPS-compliant build (``mattermost/mattermost-enterprise-fips-edition``). Migrating an existing deployment to the FIPS image is primarily a matter of replacing the image and restarting Mattermost. No data migration is required, and rollback is symmetric.

This guide covers migrating an existing Mattermost Server deployment running on Docker or Kubernetes. FIPS images are only supported for Docker- and Kubernetes-based deployments; Linux package and tarball installations can't be migrated to FIPS in place.

Mattermost's FIPS offering also covers the Mattermost Operator and a self-hosted Push Proxy. Migrating those components is out of scope for this guide.

For background on what the FIPS build is and how it's constructed, see the :doc:`FIPS overview </deployment-guide/server/deploy-containers>`.

Before you begin
----------------

1. **Back up your database and configuration.** Always take a full backup before changing the image. See the :doc:`backup and disaster recovery </deployment-guide/backup-disaster-recovery>` documentation.

2. **Confirm your deployment type.** FIPS images are supported on Docker, Docker Compose, and Kubernetes only. If you're running Mattermost from a Linux package or tarball, you can't migrate in place.

3. **Check your Mattermost version.** FIPS images are available from v11.0 onward and use the same release tags as the standard Enterprise images. Plan to migrate to the matching FIPS tag for your current version.

4. **Plan for additional plugins.** The FIPS image includes Boards, Playbooks, and Agents prepackaged and running in FIPS mode. Any additional plugins you've installed will continue to run inside the FIPS image, but they run in non-FIPS mode. This is expected behavior, not a configuration error.

5. **PostgreSQL password length.** Beginning with Mattermost v11.7, the Postgres password used by the Mattermost server must be at least 14 characters when running the FIPS image. If your current password is shorter, rotate it and update the connection string in your Mattermost configuration before migrating.

6. **Plan for downtime.** The migration requires pulling the new image and restarting the Mattermost container or pod.

Migrate a Kubernetes deployment
-------------------------------

These steps assume your deployment is managed by the Mattermost Operator using a ``Mattermost`` custom resource.

1. Edit the ``Mattermost`` custom resource to point at the FIPS image. You can edit the live resource directly:

   .. code-block:: sh

      kubectl edit mattermost <installation-name>

   Or update your manifest file and re-apply it.

2. In ``spec.image``, change the value from ``mattermost/mattermost-enterprise-edition`` to ``mattermost/mattermost-enterprise-fips-edition``. Keep ``spec.version`` aligned with your current release tag. For example:

   .. code-block:: yaml

      spec:
        image: mattermost/mattermost-enterprise-fips-edition
        version: 11.6.1

3. If you edited a manifest file, apply it:

   .. code-block:: sh

      kubectl apply -f <your-mattermost-manifest>.yaml

4. Watch the rollout to confirm the new pods come up healthy:

   .. code-block:: sh

      kubectl rollout status deployment/<installation-name>

5. Verify the running pods are using the FIPS image:

   .. code-block:: sh

      kubectl describe pod <pod-name> | grep Image

Migrate a Docker or Docker Compose deployment
---------------------------------------------

These steps are written for the official `Mattermost Docker deployment <https://github.com/mattermost/docker>`_. If you're using a custom Docker setup, adapt the container and service names accordingly.

1. Stop the Mattermost container:

   .. code-block:: sh

      docker compose stop mattermost

2. Edit ``docker-compose.yml``. In the ``mattermost`` service, change the ``image:`` value from ``mattermost/mattermost-enterprise-edition:<tag>`` to ``mattermost/mattermost-enterprise-fips-edition:<tag>``. Keep the same release tag. For example:

   .. code-block:: yaml

      services:
        mattermost:
          image: mattermost/mattermost-enterprise-fips-edition:11.6.1

3. Pull the FIPS image:

   .. code-block:: sh

      docker compose pull mattermost

4. Recreate the Mattermost container so the new image is applied:

   .. code-block:: sh

      docker compose up -d mattermost

5. Verify the running container is using the FIPS image:

   .. code-block:: sh

      docker inspect mattermost --format '{{.Config.Image}}'

After migration
---------------

1. Confirm Mattermost starts cleanly. Tail the logs and watch for startup errors:

   .. code-block:: sh

      kubectl logs -f deployment/<installation-name>

   Or, on Docker:

   .. code-block:: sh

      docker compose logs -f mattermost

2. Sign in and verify core functionality (sending messages, file uploads, search).

3. Confirm the prepackaged plugins (Boards, Playbooks, Agents) load successfully. In the System Console, go to **Plugins > Plugin Management** and confirm they're enabled and healthy.

4. If you have additional plugins installed, confirm they still load. They'll run in non-FIPS mode inside the FIPS image — this is expected.

Roll back
---------

If the migration doesn't go as planned, rolling back is symmetric: revert the image reference and redeploy. No data migration is involved.

- **Kubernetes:** Edit the ``Mattermost`` custom resource and change ``spec.image`` back to ``mattermost/mattermost-enterprise-edition``. Re-apply or save, and watch the rollout.
- **Docker / Docker Compose:** Restore the original ``image:`` value in ``docker-compose.yml`` and run ``docker compose pull mattermost`` followed by ``docker compose up -d mattermost``.
