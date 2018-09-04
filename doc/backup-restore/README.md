
GitLab Helm chart provides a specific pod named `task-runner` that acts as an interface for the purpose of backing up and restoring GitLab instances. It is equipped with a `backup-utility` executable which interacts with other necessary pods for this task.
Technical details for how the utility works can be found in the [architecture documentation](../architecture/backup-restore.md).

## Prerequisites

- Backup and Restore procedures described here have only been tested with S3 compatible APIs. Support for other object storage services, like Google Cloud Storage, will be tested in future revisions.

- During restoration, the backup tarball needs to be extracted to disk. This means the `task-runner` pod should have disk of necessary size available.

- This chart relies on the use of [object storage](#object-storage) for `artifacts`, `uploads`, and `lfs objects`, and does not currently migrate these for you during restore. If you are restoring a backup taken from another instance, you must migrate your existing instance to using object storage before taking the backup. See [issue 646](https://gitlab.com/charts/gitlab/issues/646).

## Object storage

We provide a minio instance out of the box when using this charts unless an [external object storage](../advanced/external-object-storage/README.md) is specified. The default behavior of the task-runner pod defaults to connect to our minio unless specific settings are given.

The task-runner uses `s3cmd` to connect to object storage. In order to configure connectivity to external object storage `gitlab.task-runner.backups.objectStorage.config.secret` should be specified which points to a kubernetes secret containing a `.s3cfg` file. `gitlab.task-runner.backups.objectStorage.config.key` should be specified if different from the default of `config`. This points to the key containing the contents of a .s3cfg file.

It should look like this:

```sh
helm install gitlab \
  --set gitlab.task-runner.backups.objectStorage.config.secret=my-s3cfg \
  --set gitlab.task-runner.backups.objectStorage.config.key=config .
```

s3cmd `.s3cfg` file documentation can be found [here](https://s3tools.org/kb/item14.htm)

In addition, two bucket locations need to be configured, one for storing the backups, and one temporary bucket that is used
when restoring a backup.

```
--set global.appConfig.backups.bucket=gitlab-backup-storage
--set global.appConfig.backups.tmpBucket=gitlab-tmp-storage
```

## Backup and Restoring procedures

- [Backing up a GitLab installation](backup.md)
- [Restoring a GitLab installation](restore.md)
