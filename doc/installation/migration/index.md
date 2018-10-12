# Migrating from Omnibus-GitLab package based installation

## Prerequisites

* Deployment using omnibus-gitlab package needs to be running. Run `gitlab-ctl
  status` and confirm no services report a `down` state.

* `/etc/gitlab/gitlab-secrets.json` file from package based installation.

* A Helm charts based deployment running the same GitLab version as the
  omnibus-gitlab package based installation.

* Object storage service which the Helm chart based deployment is configured to
  use. For production use, we recommend you use an [external object storage] and
  have the login credentials to access it ready. If you are using the built-in
  Minio service, [read the docs](minio.md) on how to grab the login credentials
  from it.

## Migration Steps

1. Migrate existing files (uploads, artifacts, lfs objects) from package based
   installation to object storage.
    1. Modify `/etc/gitlab/gitlab.rb` file and configure object storage for
       [uploads](https://docs.gitlab.com/ee/administration/uploads.html#s3-compatible-connection-settings),
       [artifacts](https://docs.gitlab.com/ee/administration/job_artifacts.html#s3-compatible-connection-settings)
       and
       [LFS](https://docs.gitlab.com/ee/workflow/lfs/lfs_administration.html#s3-for-omnibus-installations).

       **`Note:`** This **must** be the same object storage service that the
       Helm charts based deployment is connected to.

    1. Run reconfigure to apply the changes
        ```
        $ sudo gitlab-ctl reconfigure
        ```

    1. Migrate existing artifacts to object storage
        ```
        $ sudo gitlab-rake gitlab:artifacts:migrate
        ```

    1. Migrate existing LFS objects to object storage
        ```
        $ sudo gitlab-rake gitlab:lfs:migrate
        ```

    1. Migrate existing uploads to object storage
        ```
        $ sudo gitlab-rake gitlab:uploads:migrate:all
        ```        
        Docs: https://docs.gitlab.com/ee/administration/raketasks/uploads/migrate.html#migrate-to-object-storage

    1. Visit the omnibus-gitlab package based GitLab instance and make sure the
       uploads are available. For example check if user, group and project
       avatars are rendered fine, image and other files added to issues load
       correctly, etc.

    1. Delete or move the uploaded files from their current location so that
       they won't end up in the tarball. The default locations are
        * uploads: `/var/opt/gitlab/gitlab-rails/uploads/`
        * lfs: `/var/opt/gitlab/gitlab-rails/shared/lfs-objects`
        * artifacts: `/var/opt/gitlab/gitlab-rails/shared/artifacts`

        ```
        $ sudo mv /var/opt/gitlab/gitlab-rails/uploads{,.bak}
        $ sudo mv /var/opt/gitlab/gitlab-rails/shared/lfs-objects{,.bak}
        $ sudo mv /var/opt/gitlab/gitlab-rails/shared/artifacts{,.bak}
        ```

    1. Run reconfigure to recreate empty directories in place, so backup task
       won't fail.
        ```
        $ sudo gitlab-ctl reconfigure
        ```

1. [Create backup tarball](https://docs.gitlab.com/ee/raketasks/backup_restore.html#creating-a-backup-of-the-gitlab-system)
    ```
    $ sudo gitlab-rake gitlab:backup:create
    ```
   The backup file will be stored in `/var/opt/gitlab/backups` directory, unless
   [explicitly changed](https://docs.gitlab.com/omnibus/settings/backups.html#manually-manage-backup-directory)
   in `gitlab.rb`.

1. [Restore backup tarball to Helm chart based deployment](../..//backup-restore/restore.md)

1. Follow [official documentation](../../backup-restore/restore.md#restoring-the-secrets)
   on how to restore the secrets from package based installation.

1. Restart the pods to make sure changes are applied
    ```
    $ helm upgrade <deployment name> gitlab/gitlab \
      --timeout 600 \
      --reuse-values \
      --recreate-pods
    ```

1. Visit the Helm based deployment and confirm projects, groups, users, issues
   etc. that existed in omnibus-gitlab package based installation are restored.
   Also verify if the uploaded files (avatars, files uploaded to issues, etc.)
   are loaded fine.

[external object storage]: ../../advanced/external-object-storage/README.md
