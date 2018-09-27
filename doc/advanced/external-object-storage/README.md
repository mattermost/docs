# External object storage

Gitlab relies on object storage for highly-available persistent data in Kubernetes.
By default, an S3-compatible storage solution named `minio` is deployed with the
chart, but for production quality deployments, we recommend using a hosted
object storage solution like Google Cloud Storage or AWS S3.

To disable minio, set this option and then follow the related documentation below:

```
--set global.minio.enabled=false
```

You can see an [example of the full configuration](https://gitlab.com/charts/gitlab/blob/master/examples/values-external-objectstroage.yaml)
in the [examples documentation](https://gitlab.com/charts/gitlab/tree/master/examples).

## Docker Registry images

Configuration of object storage for the `registry` chart is done via the `registry.storage` key, and the `global.registry.bucket` key.

```
--set registry.storage.secret=registry-storage
--set registry.storage.key=config
--set global.registry.bucket=bucket-name
```

> **Note**: The bucket name needs to be set both in the secret, and in `global.registry.bucket`. The secret is used in the registry server, and
the global is used by GitLab backups.

Create the secret using yaml config per documentation, then configure the chart to make use of this secret.
See the [registry chart documentation on storage](../../charts/registry/README.md#storage) for full details.

### Registry example

**registry-storage.yaml**

```yaml
s3:
  accesskey: BOGUS_ACCESS_KEY
  secretkey: BOGUS_SECRET_KEY
  bucket: gitlab-registry
  v4auth: true
  region: us-east-1
```

```bash
kubectl create secret generic registry-storage --from-file=config=registry-storage.yaml
```

## LFS, Artifacts, Uploads

Configuration of object storage for LFS, artifacts, and uploads is done via the `global.appConfig.lfs`, `global.appConfig.artifacts`, and `global.appConfig.uploads` keys.

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
````

> **Note**: Currently you need to use a different bucket for each, otherwise performing a restore from backup will not properly function.

See the [charts/globals documentaion on appConfig](../../charts/globals.md#configure-appconfig-settings) for full details.

Create the secret(s) using yaml config per the documentation, and then configure the chart to use the provided secrets. Note, you can use the same secret for all 3 if you so chose. See the [connection details documentation](../../charts/globals.md#connection).

### Object storage example

**object-storage.yaml**

```yaml
provider: AWS
aws_access_key_id: BOGUS_ACCESS_KEY
aws_secret_access_key: BOGUS_SECRET_KEY
region: us-east-1
```

```bash
kubectl create secret generic object-storage --from-file=connection=object-storage.yaml
```

## Backups

Backups are also stored in object storage, and need to be configured to point
externally rather than the included minio service. The backup/restore procedure makes
use of two separate buckets. A bucket for storing your backups (`global.appConfig.backups.bucket`),
and a tmp bucket for preserving existing data during the restore process (`global.appConfig.backups.tmpBucket`).
You also need to provide connection configuration through the `gitlab.task-runner.backups.objectStorage.config` key.

```
--set global.appConfig.backups.bucket=gitlab-backup-storage
--set global.appConfig.backups.tmpBucket=gitlab-tmp-storage
--set gitlab.task-runner.backups.objectStorage.config.secret=s3cmd-config
--set gitlab.task-runner.backups.objectStorage.config.key=config
```

See the [backup/restore object storage documentation](../../backup-restore/README.md#object-storage) for full details.

Create the secret using the [s3cmd config file format](https://s3tools.org/kb/item14.htm) per the documentation.

> **Note**: In order to backup/restore files from the other object storage locations, the s3cmd config file needs to be
> configured to authenticate as a user with sufficient access to read/write to all your GitLab buckets.

### Backups storage example

**s3cmd.config**

```
[default]
access_key = BOGUS_ACCESS_KEY
secret_key = BOGUS_SECRET_KEY
bucket_location = us-east-1
```

```bash
kubectl create secret generic s3cmd-config --from-file=config=s3cmd.config
```
