# External object stoarge

Gitlab relies on object storage in Kubernetes highly-available persisted data.
By default, an S3-compatible storage solution named `minio` is deployed with the
chart, but for production quality deployments, we recommend using a hosted
object storage solution like Google Cloud Storage or AWS S3.

To disable minio, set these options and then follow the directions for your
specific cloud provider in each section below:
```
--set global.minio.enabled=false
--set registry.minio.enabled=false
--set gitlab.unicorn.minio.enabled=false
--set gitlab.sidekiq.minio.enabled=false
```

## Docker Registry images

### AWS S3

To use AWS S3 to store Docker images, include these options in your helm
install command:

```
--set registry.storage.s3.region=<AWS_REGION>
--set registry.storage.s3.bucket=my-registry-bucket
--set registry.storage.s3.accesskey=<AWS_ACCESS_KEY_ID>
--set registry.storage.s3.secretkey=<AWS_SECRET_ACCESS_KEY>
```

### Google Cloud Storage

TBD

## Artifacts from CI

### AWS S3

To use AWS S3 to store artifacts from CI, include these options in your helm
install command:

```
--set gitlab.unicorn.artifacts.connection.aws_access_key_id=<AWS_ACCESS_KEY_ID>
--set gitlab.unicorn.artifacts.connection.aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
--set gitlab.unicorn.artifacts.connection.region=<AWS_REGION>
--set gitlab.unicorn.artifacts.connection.provider=AWS
--set gitlab.unicorn.artifacts.bucket=my-artifacts-bucket
--set gitlab.sidekiq.artifacts.connection.aws_access_key_id=<AWS_ACCESS_KEY_ID>
--set gitlab.sidekiq.artifacts.connection.aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
--set gitlab.sidekiq.artifacts.connection.region=<AWS_REGION>
--set gitlab.sidekiq.artifacts.connection.provider=AWS
--set gitlab.sidekiq.artifacts.bucket=my-artifacts-bucket
```

### Google Cloud Storage

TBD

## Large file storage in git repositories

### AWS S3

To use AWS S3 for large file support in git repositories, include these options
in your helm install command:

```
--set gitlab.unicorn.lfs.connection.aws_access_key_id=<AWS_ACCESS_KEY_ID>
--set gitlab.unicorn.lfs.connection.aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
--set gitlab.unicorn.lfs.connection.region=<AWS_REGION>
--set gitlab.unicorn.lfs.connection.provider=AWS
--set gitlab.unicorn.lfs.bucket=my-lfs-bucket
--set gitlab.sidekiq.lfs.connection.aws_access_key_id=<AWS_ACCESS_KEY_ID>
--set gitlab.sidekiq.lfs.connection.aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
--set gitlab.sidekiq.lfs.connection.region=<AWS_REGION>
--set gitlab.sidekiq.lfs.connection.provider=AWS
--set gitlab.sidekiq.lfs.bucket=my-lfs-bucket
```

### Google Cloud Storage

TBD

## Attachments and other uploads

### AWS S3

To use AWS S3 to store issue attachments and other uploads, include these
options in your helm install command:

```
--set gitlab.unicorn.uploads.connection.aws_access_key_id=<AWS_ACCESS_KEY_ID>
--set gitlab.unicorn.uploads.connection.aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
--set gitlab.unicorn.uploads.connection.region=<AWS_REGION>
--set gitlab.unicorn.uploads.connection.provider=AWS
--set gitlab.unicorn.uploads.bucket=my-uploads-bucket
--set gitlab.sidekiq.uploads.connection.aws_access_key_id=<AWS_ACCESS_KEY_ID>
--set gitlab.sidekiq.uploads.connection.aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
--set gitlab.sidekiq.uploads.connection.region=<AWS_REGION>
--set gitlab.sidekiq.uploads.connection.provider=AWS
--set gitlab.sidekiq.uploads.bucket=my-uploads-bucket
```

### Google Cloud Storage
