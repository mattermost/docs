# External object storage

GitLab relies on object storage for highly-available persistent data in Kubernetes.
By default, an S3-compatible storage solution named `minio` is deployed with the
chart, but for production quality deployments, we recommend using a hosted
object storage solution like Google Cloud Storage or AWS S3.

To disable MinIO, set this option and then follow the related documentation below:

```
--set global.minio.enabled=false
```

An [example of the full configuration](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/values-external-objectstorage.yaml)
has been provided in the [examples](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples).

This documentation specifies usage of access and secret keys for AWS. It is also possible to use [IAM roles](./aws-iam-roles.md).

## Azure Blob Storage

GitLab uses [fog](https://github.com/fog/fog), but [doesn't currently support Fog Azure](https://gitlab.com/gitlab-org/gitlab-foss/issues/55624). To make use Azure Blob Storage, you will have to set up an [Azure MinIO gateway](azure-minio-gateway.md).

## Docker Registry images

Configuration of object storage for the `registry` chart is done via the `registry.storage` key, and the `global.registry.bucket` key.

```
--set registry.storage.secret=registry-storage
--set registry.storage.key=config
--set global.registry.bucket=bucket-name
```

> **Note**: The bucket name needs to be set both in the secret, and in `global.registry.bucket`. The secret is used in the registry server, and
the global is used by GitLab backups.

Create the secret per [registry chart documentation on storage](../../charts/registry/index.md#storage), then configure the chart to make use of this secret.

Examples for [S3](https://docs.docker.com/registry/storage-drivers/s3/)(any s3 compatible), [Azure](https://docs.docker.com/registry/storage-drivers/azure/) and [GCS](https://docs.docker.com/registry/storage-drivers/gcs/) drivers can be found in
[examples/objectstorage](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage).

- [`registry.s3.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/registry.s3.yaml)
- [`registry.gcs.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/registry.gcs.yaml)
- [`registry.azure.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/registry.azure.yaml)

### Registry configuration

1. Decide on which storage service to use.
1. Copy appropriate file to `registry-storage.yaml`.
1. Edit with the correct values for the environment.
1. Follow [registry chart documentation on storage](../../charts/registry/index.md#storage) for creating the secret.
1. Configure the chart as documented.

## LFS, Artifacts, Uploads, Packages, External Diffs, Pseudonymizer

Configuration of object storage for LFS, artifacts, uploads, packages, external
diffs, and pseudonymizer is done via the `global.appConfig.lfs`,
`global.appConfig.artifacts`, `global.appConfig.uploads`,
`global.appConfig.packages`, `global.appConfig.externalDiffs` and `global.appConfig.pseudonymizer` keys.

```
--set global.appConfig.lfs.bucket=gitlab-lfs-storage
--set global.appConfig.lfs.connection.secret=object-storage
--set global.appConfig.lfs.connection.key=connection

--set global.appConfig.artifacts.bucket=gitlab-artifacts-storage
--set global.appConfig.artifacts.connection.secret=object-storage
--set global.appConfig.artifacts.connection.key=connection

--set global.appConfig.uploads.bucket=gitlab-uploads-storage
--set global.appConfig.uploads.connection.secret=object-storage
--set global.appConfig.uploads.connection.key=connection

--set global.appConfig.packages.bucket=gitlab-packages-storage
--set global.appConfig.packages.connection.secret=object-storage
--set global.appConfig.packages.connection.key=connection

--set global.appConfig.externalDiffs.bucket=gitlab-externaldiffs-storage
--set global.appConfig.externalDiffs.connection.secret=object-storage
--set global.appConfig.externalDiffs.connection.key=connection

--set global.appConfig.pseudonymizer.bucket=gitlab-pseudonymizer-storage
--set global.appConfig.pseudonymizer.connection.secret=object-storage
--set global.appConfig.pseudonymizer.connection.key=connection
```

NOTE: **Note:**
Currently a different bucket is needed for each, otherwise performing a restore from backup will not properly function.

NOTE: **Note:**
Storing MR diffs on external storage is not enabled by default. So,
for the object storage settings for `externalDiffs` to take effect,
`global.appConfig.externalDiffs.enabled` key should have a `true` value.

See the [charts/globals documentaion on appConfig](../../charts/globals.md#configure-appconfig-settings) for full details.

Create the secret(s) per the [connection details documentation](../../charts/globals.md#connection), and then configure the chart to use the provided secrets. Note, the same secret can be used for all of them.

Examples for [AWS][fog-aws](any S3 compatible like [Azure using MinIO][minio-azure] ) and [Google][fog-gcs] providers can be found in
[examples/objectstorage](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage).

- [`rails.s3.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/rails.s3.yaml)
- [`rails.gcs.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/rails.gcs.yaml)
- [`rails.azure.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/rails.azure.yaml)

[fog-aws]: https://fog.io/storage/#using-amazon-s3-and-fog
[fog-gcs]: https://fog.io/storage/#google-cloud-storage
[minio-azure]: ./azure-minio-gateway.md

### appConfig configuration

1. Decide on which storage service to use.
1. Copy appropriate file to `rails.yaml`.
1. Edit with the correct values for the environment.
1. Follow [connection details documentation](../../charts/globals.md#connection) for creating the secret.
1. Configure the chart as documented.

## Backups

Backups are also stored in object storage, and need to be configured to point
externally rather than the included MinIO service. The backup/restore procedure makes
use of two separate buckets. A bucket for storing backups (`global.appConfig.backups.bucket`)
and a tmp bucket for preserving existing data during the restore process (`global.appConfig.backups.tmpBucket`).
Currently AWS S3-compatible object storage systems and Google Cloud Storage are supported backends
The backend type is configurable by setting `global.appConfig.backups.objectStorage.backend` to `s3` and `gcs` respectively.
A connection configuration through the `gitlab.task-runner.backups.objectStorage.config` key must also be provided.
When using Google Cloud Storage, the GCP project must be set with the `global.appConfig.backups.objectStorage.config.gcpProject` value.

For S3-compatible storage:

```
--set global.appConfig.backups.bucket=gitlab-backup-storage
--set global.appConfig.backups.tmpBucket=gitlab-tmp-storage
--set gitlab.task-runner.backups.objectStorage.config.secret=storage-config
--set gitlab.task-runner.backups.objectStorage.config.key=config
```

For Google Cloud Storage (GCS):

```
--set global.appConfig.backups.bucket=gitlab-backup-storage
--set global.appConfig.backups.tmpBucket=gitlab-tmp-storage
--set gitlab.task-runner.backups.objectStorage.backend=gcs
--set gitlab.task-runner.backups.objectStorage.config.gcpProject=my-gcp-project-id
--set gitlab.task-runner.backups.objectStorage.config.secret=storage-config
--set gitlab.task-runner.backups.objectStorage.config.key=config
```

See the [backup/restore object storage documentation](../../backup-restore/index.md#object-storage) for full details.

> **Note**: In order to backup/restore files from the other object storage locations, the config file needs to be
> configured to authenticate as a user with sufficient access to read/write to all GitLab buckets.

### Backups storage example

1. Create the `storage.config` file:

    - On Amazon S3, the contents should be in the [s3cmd config file format](https://s3tools.org/kb/item14.htm)

    ```
    [default]
    access_key = BOGUS_ACCESS_KEY
    secret_key = BOGUS_SECRET_KEY
    bucket_location = us-east-1
    ```

    - On Google Cloud Storage, you can create the file by creating a service account
      with the storage.admin role and then
      [creating a service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys).
      Below is an example of using the `gcloud` CLI to create the file.

    ```shell
    export PROJECT_ID=$(gcloud config get-value project)
    gcloud iam service-accounts create gitlab-gcs --display-name "Gitlab Cloud Storage"
    gcloud projects add-iam-policy-binding --role roles/storage.admin ${PROJECT_ID} --member=serviceAccount:gitlab-gcs@${PROJECT_ID}.iam.gserviceaccount.com
    gcloud iam service-accounts keys create --iam-account gitlab-gcs@${PROJECT_ID}.iam.gserviceaccount.com storage.config
    ```

    - On Azure Storage

    ```
    [default]
    # Setup endpoint: hostname of the Web App
    host_base = https://your_minio_setup.azurewebsites.net
    host_bucket = https://your_minio_setup.azurewebsites.net
    # Leave as default
    bucket_location = us-west-1
    use_https = True

    # Setup access keys
    # Access Key = Azure Storage Account name
    access_key =  BOGUS_ACCOUNT_NAME
    # Secret Key = Azure Storage Account Key
    secret_key = BOGUS_KEY

    # Use S3 v4 signature APIs
    signature_v2 = False
    ```

1. Create the secret

    ```bash
    kubectl create secret generic storage-config --from-file=config=storage.config
    ```
