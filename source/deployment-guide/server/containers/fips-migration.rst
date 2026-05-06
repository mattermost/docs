Migrate an existing deployment to FIPS-compliant containers
============================================================

.. include:: ../../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

From Mattermost v11, each release ships in two image variants: a standard Enterprise build (``mattermost/mattermost-enterprise-edition``) and a FIPS-compliant build (``mattermost/mattermost-enterprise-fips-edition``). Migrating an existing deployment to the FIPS image is primarily a matter of replacing the image and restarting Mattermost. No data migration is required, and rollback is symmetric.

This guide covers migrating an existing Mattermost Server deployment running on Docker or Kubernetes. FIPS images are only supported for Docker- and Kubernetes-based deployments; Linux package and tarball installations can't be migrated to FIPS in place.

Mattermost's FIPS offering also covers the Mattermost Operator and a self-hosted Push Proxy. Migrating those components is out of scope for this guide.

For background on what the FIPS build is and how it's constructed, see the **FIPS/STIG** tab on :doc:`Deploy Mattermost using Containers </deployment-guide/server/deploy-containers>`.

Before you begin
----------------

1. **Back up your database and configuration.** Always take a full backup before changing the image. See the :doc:`backup and disaster recovery </deployment-guide/backup-disaster-recovery>` documentation.

2. **Confirm your deployment type.** FIPS images are supported on Docker, Docker Compose, and Kubernetes only. If you're running Mattermost from a Linux package or tarball, you can't migrate in place.

3. **Check your Mattermost version.** FIPS images are available from v11.0 onward and use the same release tags as the standard Enterprise images. Plan to migrate to the matching FIPS tag for your current version.

4. **Plan for additional plugins.** The FIPS image includes Boards, Playbooks, and Agents prepackaged and running in FIPS mode. Any additional plugins you've installed will continue to run inside the FIPS image, but they run in non-FIPS mode. This is expected behavior, not a configuration error.

5. **PostgreSQL password length.** Beginning with Mattermost v11.7, the Postgres password used by the Mattermost server must be at least 14 characters when running the FIPS image. If your current password is shorter, rotate it in PostgreSQL first, then update wherever your deployment stores the password before migrating: in the official Docker deployment, the ``POSTGRES_PASSWORD`` value in ``.env``; in Operator-managed Kubernetes deployments, the database Secret referenced by your ``Mattermost`` custom resource (commonly under ``spec.database.external.secret``). Restart Mattermost so the new credentials take effect — the migration itself recreates the container, so this can happen as part of the image swap rather than as a separate restart.

6. **Plan for downtime.** The migration requires pulling the new image and restarting the Mattermost container or pod.

Migrate a Kubernetes deployment
-------------------------------

These steps assume your deployment is managed by the Mattermost Operator using a ``Mattermost`` custom resource.

In the steps below, replace ``[namespace]`` with the namespace your Mattermost installation runs in. If you omit ``-n [namespace]``, ``kubectl`` uses your current context's default namespace.

1. Find the name of your Mattermost custom resource:

   .. code-block:: sh

      kubectl -n [namespace] get mattermost

2. Edit the ``Mattermost`` custom resource to point at the FIPS image. You can edit the live resource directly:

   .. code-block:: sh

      kubectl -n [namespace] edit mattermost [installation-name]

   Or update your manifest file and re-apply it.

3. In ``spec.image``, change the value from ``mattermost/mattermost-enterprise-edition`` to ``mattermost/mattermost-enterprise-fips-edition``. Keep ``spec.version`` aligned with your current release tag. For example:

   .. code-block:: yaml

      spec:
        image: mattermost/mattermost-enterprise-fips-edition
        version: 11.6.1

4. If you edited a manifest file, apply it:

   .. code-block:: sh

      kubectl -n [namespace] apply -f <your-mattermost-manifest>.yaml

5. Watch the Mattermost pods until the new ones reach ``Running`` and the old ones terminate:

   .. code-block:: sh

      kubectl -n [namespace] get pods -w

6. Verify the running pods are using the FIPS image:

   .. code-block:: sh

      kubectl -n [namespace] get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.containers[*].image}{"\n"}{end}'

Migrate a Docker or Docker Compose deployment
---------------------------------------------

These steps are written for the official `Mattermost Docker deployment <https://github.com/mattermost/docker>`_, which selects the Mattermost image and tag through ``.env`` variables (``MATTERMOST_IMAGE`` and ``MATTERMOST_IMAGE_TAG``) referenced from ``docker-compose.yml`` as ``mattermost/${MATTERMOST_IMAGE}:${MATTERMOST_IMAGE_TAG}``. If you're using a custom Docker setup that hardcodes the image in ``docker-compose.yml`` or uses different variable names, adapt these steps accordingly.

1. Stop the Mattermost container:

   .. code-block:: sh

      docker compose stop mattermost

2. Edit your ``.env`` file. Change ``MATTERMOST_IMAGE`` from ``mattermost-enterprise-edition`` to ``mattermost-enterprise-fips-edition``. Leave ``MATTERMOST_IMAGE_TAG`` set to your current release tag — FIPS images are published under the same tags as the standard Enterprise images.

   .. code-block:: text

      MATTERMOST_IMAGE=mattermost-enterprise-fips-edition
      MATTERMOST_IMAGE_TAG=<tag>

3. Pull the FIPS image:

   .. code-block:: sh

      docker compose pull mattermost

4. Recreate the Mattermost container so the new ``.env`` values are applied:

   .. code-block:: sh

      docker compose up -d --force-recreate mattermost

5. Verify the running container is using the FIPS image:

   .. code-block:: sh

      docker inspect mattermost --format '{{.Config.Image}}'

After migration
---------------

1. Confirm Mattermost starts cleanly. Tail the logs and watch for startup errors. On Kubernetes, target a specific Mattermost pod:

   .. code-block:: sh

      kubectl -n [namespace] logs -f [pod-name]

   On Docker:

   .. code-block:: sh

      docker compose logs -f mattermost

2. Sign in and verify core functionality (sending messages, file uploads, search).

3. Confirm the prepackaged plugins (Boards, Playbooks, Agents) load successfully. In the System Console, go to **Plugins > Plugin Management** and confirm they're enabled and healthy.

4. If you have additional plugins installed, confirm they still load. They'll run in non-FIPS mode inside the FIPS image — this is expected.

Roll back
---------

If the migration doesn't go as planned, rolling back is symmetric: revert the image reference and redeploy. No data migration is involved.

- **Kubernetes:** Edit the ``Mattermost`` custom resource and change ``spec.image`` back to ``mattermost/mattermost-enterprise-edition``. Re-apply or save, and watch the rollout.
- **Docker / Docker Compose:** Restore the original ``MATTERMOST_IMAGE`` value in ``.env`` (``mattermost-enterprise-edition``) and run ``docker compose pull mattermost`` followed by ``docker compose up -d --force-recreate mattermost``.
