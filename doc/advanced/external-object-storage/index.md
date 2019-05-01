# External object storage

Gitlab relies on object storage for highly-available persistent data in Kubernetes.
By default, an S3-compatible storage solution named `minio` is deployed with the
chart, but for production quality deployments, we recommend using a hosted
object storage solution like Google Cloud Storage or AWS S3.

To disable minio, set this option and then follow the related documentation below:

```
--set global.minio.enabled=false
```

An [example of the full configuration](https://gitlab.com/charts/gitlab/blob/master/examples/values-external-objectstorage.yaml)
has been provided in the [examples](https://gitlab.com/charts/gitlab/tree/master/examples).

This documentation specifies usage of access and secret keys for AWS. It is also possible to use [IAM roles](./aws-iam-roles.md).

## Azure Blob Storage

GitLab uses [fog](https://github.com/fog/fog), but [doesn't currently support fog-azure](https://gitlab.com/gitlab-org/gitlab-ce/issues/55624). To make use Azure Blob Storage, you will have to setup a [minio-azure gateway](./minio-azure-gateway.md).

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

Examples for [S3][storage-s3](any s3 compatible), [Azure][storage-azure] and [GCS][storage-gcs] drivers can be found in
[examples/objectstorage](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage).
- [registry.s3.yaml](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage/registry.s3.yaml)
- [registry.gcs.yaml](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage/registry.gcs.yaml)
- [registry.azure.yaml](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage/registry.azure.yaml)

[storage-s3]: https://docs.docker.com/registry/storage-drivers/s3
[storage-gcs]: https://docs.docker.com/registry/storage-drivers/gcs
[storage-azure]: https://docs.docker.com/registry/storage-drivers/azure

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
````

> **Note**: Currently a different bucket is needed for each, otherwise performing a restore from backup will not properly function.

> **Note**: Storing MR diffs on external storage is not enabled by default. So,
> for the object storage settings for `externalDiffs` to take effect,
> `global.appConfig.externalDiffs.enabled` key should have a `true` value.

See the [charts/globals documentaion on appConfig](../../charts/globals.md#configure-appconfig-settings) for full details.

Create the secret(s) per the [connection details documentation](../../charts/globals.md#connection), and then configure the chart to use the provided secrets. Note, the same secret can be used for all of them.

Examples for [AWS][fog-aws](any S3 compatible like [Azure using Minio][minio-azure] ) and [Google][fog-gcs] providers can be found in
[examples/objectstorage](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage).
- [rails.s3.yaml](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage/rails.s3.yaml)
- [rails.gcs.yaml](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage/rails.gcs.yaml)
- [rails.azure.yaml](https://gitlab.com/charts/gitlab/tree/master/examples/objectstorage/rails.azure.yaml)

[fog-aws]: https://fog.io/storage/#using-amazon-s3-and-fog
[fog-gcs]: https://fog.io/storage/#google-cloud-storage
[minio-azure]: ./aws-iam-roles.md

### appConfig configuration

1. Decide on which storage service to use.
1. Copy appropriate file to `rails.yaml`.
1. Edit with the correct values for the environment.
1. Follow [connection details documentation](../../charts/globals.md#connection) for creating the secret.
1. Configure the chart as documented.

## Backups

Backups are also stored in object storage, and need to be configured to point
externally rather than the included minio service. The backup/restore procedure makes
use of two separate buckets. A bucket for storing backups (`global.appConfig.backups.bucket`),
and a tmp bucket for preserving existing data during the restore process (`global.appConfig.backups.tmpBucket`).
A connection configuration through the `gitlab.task-runner.backups.objectStorage.config` key must also be provided.

```
--set global.appConfig.backups.bucket=gitlab-backup-storage
--set global.appConfig.backups.tmpBucket=gitlab-tmp-storage
--set gitlab.task-runner.backups.objectStorage.config.secret=s3cmd-config
--set gitlab.task-runner.backups.objectStorage.config.key=config
```

See the [backup/restore object storage documentation](../../backup-restore/index.md#object-storage) for full details.

Create the secret using the [s3cmd config file format](https://s3tools.org/kb/item14.htm) per the documentation.

> **Note**: In order to backup/restore files from the other object storage locations, the s3cmd config file needs to be
> configured to authenticate as a user with sufficient access to read/write to all GitLab buckets.

### Backups storage example

1. Create a file called `s3cmd.config` containing:

    * On Amazon S3

    ```
    [default]
    access_key = BOGUS_ACCESS_KEY
    secret_key = BOGUS_SECRET_KEY
    bucket_location = us-east-1
    ```

    * On Google Cloud Storage

    ```
    [default]
    host_base = storage.googleapis.com
    host_bucket = storage.googleapis.com
    use_https = True
    signature_v2 = True

    # Access and secret key can be generated in the interoperability
    # https://console.cloud.google.com/storage/settings
    # See Docs: https://cloud.google.com/storage/docs/interoperability
    access_key = BOGUS_ACCESS_KEY
    secret_key = BOGUS_SECRET_KEY

    # Multipart needs to be disabled for GCS !
    enable_multipart = False
    ```

    * On Azure Storage

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
    kubectl create secret generic s3cmd-config --from-file=config=s3cmd.config
    ```
