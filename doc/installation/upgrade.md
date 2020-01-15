# Upgrade Guide

Before upgrading your GitLab installation, you need to check the
[changelog](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/CHANGELOG.md)
corresponding to the specific release you want to upgrade to and look for any
[release notes](../releases/index.md) that might pertain to the new GitLab chart
version.

Warning: **Warning:**
If you are upgrading from the `2.x` version of the chart to the latest 3.0 release, you need
to first update to the latest `2.6.x` patch release in order for the upgrade to work.
The [3.0 release notes](../releases/3_0.md) describe the supported upgrade path.

We also recommend that you take a [backup](../backup-restore/index.md) first.
Also note that you need to provide all values using `helm upgrade --set key=value` syntax or `-f values.yml` instead of using `--reuse-values` because some of the current values might be deprecated.

NOTE: **Note:**
You can retrieve your previous `--set` arguments cleanly, with
`helm get values <release name>`. If you direct this into a file
(`helm get values <release name> > gitlab.yaml`), you can safely pass this
file via `-f`. Thus `helm upgrade gitlab gitlab/gitlab -f gitlab.yaml`.
This safely replaces the behavior of `--reuse-values`

Mappings between chart versioning and GitLab versioning can be found [here](../index.md#gitlab-version-mappings).

## Steps

The following are the steps to upgrade GitLab to a newer version:

1. Check the [change log](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/CHANGELOG.md) for the specific version you would like to upgrade to
1. Go through [deployment documentation](./deployment.md) step by step
1. Extract your previous `--set` arguments with

   ```
   helm get values gitlab > gitlab.yaml
   ```

1. Decide on all the values you need to set
1. If you would like to use the GitLab Operator go through the steps outlined in [Operator installation](./operator.md)
1. Perform the upgrade, with all `--set` arguments extracted in step 4

   ```
   helm upgrade gitlab gitlab/gitlab \
     --version <new version> \
     -f gitlab.yaml \
     --set ...
   ```

## Upgrade the bundled PostgreSQL chart

As part of the `3.0.0` release of this chart, we upgraded the bundled [PostgreSQL chart](https://github.com/helm/charts/tree/master/stable/postgresql) from 0.11.0 to 7.7.0. This is not a drop in replacement. Manual steps need to be performed to upgrade the database.

NOTE: **Note:** If you are not using the bundled PostgreSQL chart (`postgresql.enabled` is false), you do not need to perform these steps.

### Steps

If you are using the bundled PostgreSQL, the best way to perform this upgrade is to backup your old database, and restore into a new database instance. We've automated some of the steps, as an alternative, you can perform the steps manually.

NOTE: **Note:** Failure to perform these steps as documented **may** result in the loss of your database.

NOTE: **Note:** If you have multiple charts installed in the same namespace. It may be necessary to pass the Helm release name to the database-upgrade script as well. Replace `bash -s STAGE` with `bash -s -- -r RELEASE STAGE` in the example commands provided later.

1. Prepare the existing database

   The pre stage will create a backup of your database using the backup-utility script in the task-runner pod, which gets saved to the configured s3 bucket (MinIO by default).

   ```shell
   # GITLAB_RELEASE should be the version of the chart you are installing
   curl -s https://gitlab.com/gitlab-org/charts/gitlab/raw/${GITLAB_RELEASE}/scripts/database-upgrade | bash -s pre
   ```

1. Prepare the cluster database secrets

   The secret key for the application database key is changing from `postgres-password`, to `postgresql-password`.

   1. If you'd to use an auto-generated PostgreSQL password, delete the existing secret to allow the upgrade to generate a new password for you. RELEASE-NAME should be the name of the GitLab release from `helm list`

      ```shell
      kubectl delete secret RELEASE-NAME-postgresql-password
      ```

   1. If you want to use the same password, edit the secret, and change the key from `postgres-password` to `postgresql-password`. Additionally, we need a secret for the superuser account. Add a key for that user `postgresql-postgres-password`

      ```shell
      # Encode the superuser password into base64
      echo SUPERUSER_PASSWORD | base64
      kubectl edit RELEASE-NAME-postgresql-password
      # Make the appropriate changes in your EDITOR window
      ```

1. Upgrade GitLab following our [standard procedure](#upgrade-guide), with the addition of:

   1. `gitlab.migrations.enabled` should be set to false

1. After the upgrade is complete, run the post steps

   This step will do the following:
       1. Set replicas to 0 for the `unicorn`, `sidekiq`, and `gitlab-exporter` deployments. This will prevent any other application from altering the database while the backup is being restored.
       1. Restore the database from the backup created in the pre stage.
       1. Run database migrations for the new version
       1. Unpause the deployments from the first step

   ```shell
   # RELEASE should be the version of the chart you are installing
   curl -s https://gitlab.com/gitlab-org/charts/gitlab/raw/${RELEASE}/scripts/database-upgrade | bash -s post
   ```
