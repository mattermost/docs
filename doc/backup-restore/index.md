# Backup and restore a GitLab instance

GitLab Helm chart provides a specific pod named `task-runner` that acts as an interface for the purpose of backing up and restoring GitLab instances. It is equipped with a `backup-utility` executable which interacts with other necessary pods for this task.
Technical details for how the utility works can be found in the [architecture documentation](../architecture/backup-restore.md).

## Prerequisites

- Backup and Restore procedures described here have only been tested with S3 compatible APIs. Support for other object storage services, like Google Cloud Storage, will be tested in future revisions.

- During restoration, the backup tarball needs to be extracted to disk. This means the `task-runner` pod should have disk of necessary size available.

- This chart relies on the use of [object storage](#object-storage) for `artifacts`, `uploads`, `packages`, `registry` and `lfs` objects, and does not currently migrate these for you during restore. If you are restoring a backup taken from another instance, you must migrate your existing instance to using object storage before taking the backup. See [issue 646](https://gitlab.com/gitlab-org/charts/gitlab/issues/646).

## Object storage

We provide a MinIO instance out of the box when using this charts unless an [external object storage](../advanced/external-object-storage/index.md) is specified. The default behavior of the task-runner pod defaults to connect to our MinIO unless specific settings are given. The task-runner can also be configured to back up to Amazon S3 or Google Cloud Storage (GCS).

### Backups to S3

The task-runner uses `s3cmd` to connect to object storage. In order to configure connectivity to external object storage `gitlab.task-runner.backups.objectStorage.config.secret` should be specified which points to a Kubernetes secret containing a `.s3cfg` file. `gitlab.task-runner.backups.objectStorage.config.key` should be specified if different from the default of `config`. This points to the key containing the contents of a .s3cfg file.

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

### Backups to Google Cloud Storage (GCS)

To backup to GCS you must set `gitlab.task-runner.backups.objectStorage.backend` to `gcs`. This ensures that the task-runner uses the `gsutil` CLI when storing and retrieving
objects. Additionally you must set `gitlab.task-runner.backups.objectStorage.config.gcpProject` to the project ID of the GCP project that contains your storage buckets.
You must create a Kubernetes secret with the contents of an active service account JSON key where the service account has the `storage.admin` role for the buckets
you will use for backup. Below is an example of using the `gcloud` and `kubectl` to create the secret.

```shell
export PROJECT_ID=$(gcloud config get-value project)
gcloud iam service-accounts create gitlab-gcs --display-name "Gitlab Cloud Storage"
gcloud projects add-iam-policy-binding --role roles/storage.admin ${PROJECT_ID} --member=serviceAccount:gitlab-gcs@${PROJECT_ID}.iam.gserviceaccount.com
gcloud iam service-accounts keys create --iam-account gitlab-gcs@${PROJECT_ID}.iam.gserviceaccount.com storage.config
kubectl create secret generic storage-config --from-file=config=storage.config
```

Configure your Helm chart as follows to use the service account key to authenticate to GCS for backups:

```sh
helm install gitlab . \
  --set gitlab.task-runner.backups.objectStorage.config.secret=storage-config \
  --set gitlab.task-runner.backups.objectStorage.config.key=config \
  --set gitlab.task-runner.backups.objectStorage.config.gcpProject=my-gcp-project-id \
  --set gitlab.task-runner.backups.objectStorage.backend=gcs
```

In addition, two bucket locations need to be configured, one for storing the backups, and one temporary bucket that is used
when restoring a backup.

```
--set global.appConfig.backups.bucket=gitlab-backup-storage
--set global.appConfig.backups.tmpBucket=gitlab-tmp-storage
```

## Backup and Restoring procedures

- [Backing up a GitLab installation](backup.md)
- [Restoring a GitLab installation](restore.md)

## Troubleshooting

### Pod eviction issues

As the backups are assembled locally outside of the object storage target, temporary disk space is needed. The required space might exceed the size of the actual backup archive.
The default configuration will use the task-runner pod's file system to store the temporary data. If you find pod being evicted due to low resources, you should attach a persistent volume to the pod to hold the temporary data.
On GKE, add the following settings to your Helm command:

```
--set gitlab.task-runner.persistence.enabled=true
```

If your backups are being run as part of the included backup cron job, then you will want to enable persistence for the cron job as well:

```
-- set gitlab.task-runner.backups.cron.persistence.enabled=true
```

For other providers, you may need to create a persistent volume. See our [Storage documentation](../installation/storage.md) for possible examples on how to do this.
