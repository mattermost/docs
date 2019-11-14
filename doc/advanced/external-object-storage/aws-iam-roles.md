# IAM roles for AWS

The default configuration for external object storage in the charts is to use access and secret keys.
It is also possible to use IAM roles in combination with [kube2iam](https://github.com/jtblin/kube2iam) or [kiam](https://github.com/uswitch/kiam).

## IAM role

The IAM role will need read, write and list permissions on the S3 buckets. You can choose to have a role per bucket or combine them.

## Chart configuration

IAM roles can be specified by adding annotations and changing the secrets, as specified below:

### Registry

An IAM role can be specified via the annotations key:

```
--set registry.annotations."iam\.amazonaws\.com/role"=<role name>
```

When creating the [registry-storage.yaml](../../charts/registry/index.md#storage) secret, omit the access and secret key:

```yaml
s3:
  bucket: gitlab-registry
  v4auth: true
  region: us-east-1
```

*Note*: If you provide the keypair, IAM role will be ignored. See [AWS documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default) for more details.

### LFS, Artifacts, Uploads, Packages, Pseudonymizer

For LFS, artifacts, uploads, packages and pseudonymizer an IAM role can be specified via the annotations key in the `unicorn` and `sidekiq` configuration:

```
--set gitlab.sidekiq.annotations."iam\.amazonaws\.com/role"=<role name>
--set gitlab.unicorn.annotations."iam\.amazonaws\.com/role"=<role name>
```

For the [object-storage.yaml](../../charts/globals.md#connection) secret, omit the access and secret key.
As Unicorn uses Fog for S3 storage, the [use_iam_profile](https://docs.gitlab.com/ee/administration/job_artifacts.html#s3-compatible-connection-settings) key should be added for Fog to use the role:

```yaml
provider: AWS
use_iam_profile: true
region: us-east-1
```

### Backups

The `task-runner` configuration allows for annotations to be set to upload backups to S3:

```
--set gitlab.task-runner.annotations."iam\.amazonaws\.com/role"=<role name>
```

The [s3cmd.config](./index.md#backups-storage-example) secret is to be created without the access and secret keys:

```
[default]
bucket_location = us-east-1
```
