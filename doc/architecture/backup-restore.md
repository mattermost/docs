# Backup and restore

This document explains the technical implementation of the backup and restore into/from CNG.

## Task runner pod

The [task runner chart](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/charts/gitlab/charts/task-runner) deploys a pod into the cluster. This pod will act as an entry point for interaction with other containers in the cluster.

Using this pod user can run commands using `kubectl exec -it <pod name> -- <arbitrary command>`

The task runner runs a container from the [task-runner image](https://gitlab.com/gitlab-org/build/CNG/tree/master/gitlab-task-runner).

The image contains some custom scripts that are to be called as commands by the user, these scripts can be found [here](https://gitlab.com/gitlab-org/build/CNG/tree/master/gitlab-task-runner/scripts). These scripts are for running rake tasks, backup, restore, and some helper scripts for interacting with object storage.

## Backup utility

[Backup utility](https://gitlab.com/gitlab-org/build/CNG/blob/master/gitlab-task-runner/scripts/bin/backup-utility) is one of the scripts
in the task runner container and as the name suggests it is a script used for doing backups but also handles restoring of an existing backup.

### Backups

The backup utility script when run without any arguments creates a backup tar and uploads it to object storage.
You can skip parts of the backup process by using `--skip <component>` for every component that you want to skip in the backup process. Skippable components are the database (`db`), repositories (`repositories`), and any of the object storages (`artifacts`, `lfs`, `packages`, `registry` and `uploads`).
There is also an option to manually set a part of the name of the generated backup tar via the `-t <backup-name>` command line flag, which will result in the backup file `<backup-name>_gitlab_backup.tar` to be created.

The sequence of execution is:

1. Backup the database (if not skipped) using the [GitLab backup rake task](https://gitlab.com/gitlab-org/build/CNG/blob/74dc35d4b481e86330bf6b244f88e5dd8876cc0c/gitlab-task-runner/scripts/bin/backup-utility#L120)
1. Backup the repositories (if not skipped) using the [GitLab backup rake task](https://gitlab.com/gitlab-org/build/CNG/blob/74dc35d4b481e86330bf6b244f88e5dd8876cc0c/gitlab-task-runner/scripts/bin/backup-utility#L123)
1. For each of the object storage backends
   1. If the object storage backend is marked for skipping, skip this storage backend.
   1. Tar the existing data in the corresponding object storage bucket naming it `<bucket-name>.tar`
   1. Move the tar to the backup location on disk
1. Write a `backup_information.yml` file which contains some metadata identifying the version of GitLab, the time of the backup and the skipped items.
1. Create a tar file containing individual tar files along with `backup_information.yml`
1. Upload the resulting tar file to object storage `gitlab-backups` bucket.

#### GitLab backup bucket

The default name of the bucket that will be used to store backups is `gitlab-backups`. This is configurable
using the `BACKUP_BUCKET_NAME` environment variable.

#### Backing up to Google Cloud Storage

By default, the backup utility uses `s3cmd` to upload and download artifacts from object storage. While this can work with Google Cloud Storage (GCS),
it requires using the Interoperability API which makes undesireable compromises to authentication and authorization. When using Google Cloud Storage
for backups you can configure the backup utility script to use the Cloud Storage native CLI, `gsutil`, to do the upload and download
of your artifacts by setting the `BACKUP_BACKEND` environment variable to `gcs`.

### Restore

The backup utility when given an argument `--restore` attempts to restore from an existing backup to the running instance. This
backup can be from either an Omnibus GitLab or a CNG Helm chart installation given that both the instance that was
backed up and the running instance runs the same version of GitLab. The restore expects a file in backup bucket using `-t <backup-name>` or a remote url using `-f <url>`.

When given a `-t` parameter it looks into backup bucket in object storage for a backup tar with such name. When
given a `-f` parameter it expects that the given url is a valid uri of a backup tar in a location accessible from the container.

After fetching the backup tar the sequence of execution is:

1. For repositories and database run the [GitLab backup rake task](https://gitlab.com/gitlab-org/gitlab-foss/tree/master/lib/tasks/gitlab/backup.rake)
1. For each of object storage backends:
   - tar the existing data in the corresponding object storage bucket naming it `<backup-name>.tar`
   - upload it to `tmp` bucket in object storage
   - clean up the corresponding bucket
   - restore the backup content into the corresponding bucket

> Note:  If the restore fails, user will need to revert to previous backup using data in `tmp` directory of the the backup bucket. This is currently a manual process.
