# Backup and restore

This document explains the technical implementation of the backup and restore into/from CNG.

## Task runner pod
The [task runner chart](../../charts/gitlab/charts/task-runner) deploys a pod into the cluster. This pod will act as an entry point for interaction with other containers in the cluster.

Using this pod user can run commands using `kubectl exec -it <pod name> -- <arbitrary command>`

The task runner runs a container from the [task-runner image](https://gitlab.com/gitlab-org/build/CNG/tree/master/gitlab-task-runner).

The image contains some custom scripts that are to be called as commands by the user, these scripts can be found [here](https://gitlab.com/gitlab-org/build/CNG/tree/master/gitlab-task-runner/scripts). These scripts are for running rake tasks, backup, restore, and some helper scripts for interacting with object storage.

## Backup utility

[Backup utility](https://gitlab.com/gitlab-org/build/CNG/blob/master/gitlab-task-runner/scripts/bin/backup-utility) is one of the scripts
in the task runner container and as the name suggests it is a script used for doing backups but also handles restoring of an existing backup.

### Backups

The backup utility script when run without any arguments creates a backup tar and uploads it to object storage. The sequence of execution is:
1. Backup the repositories and database using the [GitLab backup rake task](https://gitlab.com/gitlab-org/build/CNG/blob/master/gitlab-task-runner/scripts/bin/backup-utility#L121)
2. For each of object storage backends
   - tar the existing data in the corresponding object storage bucket naming it `<bucket-name>.tar`
   - Move the tar to the backup location on disk
3. Write a `backup_information.yml` file which contains some metadata identifying the version of gitlab, the time of the backup and the skipped items if any.
4. Create a tar file containing individual tar files along with `backup_information.yml`
5. Upload the resulting tar file to object storage `gitlab-backups` bucket.

#### GitLab backup bucket

The default name of the bucket that will be used to store backups is `gitlab-backups`. This is configurable
using the `BACKUP_BUCKET_NAME` environment variable.

### Restore

The backup utility when given an argument `--restore` attempts to restore from an existing backup to the running instance. This
backup can be from either an omnibus-gitlab or a CNG Helm chart installation given that both the instance that was
backed up and the running instance runs the same version of gitlab. The restore expects a file in backup bucket using `-t <backup-name>` or a remote url using `-f <url>`.

When given a `-t` parameter it looks into backup bucket in object storage for a backup tar with such name. When
given a `-f` parameter it expects that the given url is a valid uri of a backup tar in a location accessible from the container.

After fetching the backup tar the sequence of execution is:
1. For repositories and database run the [GitLab backup rake task](https://gitlab.com/gitlab-org/gitlab-ce/tree/master/lib/tasks/gitlab/backup.rb)
2. For each of object storage backends
   - tar the existing data in the corresponding object storage bucket naming it `<backup-name>.tar`
   - upload it to `tmp` bucket in object storage
   - clean up the corresponding bucket
   - restore the backup content into the corresponding bucket

> Note:  If the restore fails, user will need to revert to previous backup using data in `tmp` directory of the the backup bucket. This is currently a manual process.
