# IAM roles for AWS

The default configuration for external object storage in the charts is to use access and secret keys. 
It is also possible to use IAM roles instead in combination with [kube2iam](https://github.com/jtblin/kube2iam) or [kiam](https://github.com/uswitch/kiam). 

## IAM role

The IAM role will need read, write and list permissions on the S3 buckets. You can choose to have a role per bucket or combine them.

## Chart configuration

IAM roles can be specified by adding annotations and changing the secrets, as specified below:

### Registry

An IAM role can be specified via the annotations key:

```
--set registry.annotations."iam\.amazonaws\.com/role"=gitlab-registry
```

The `registry-storage.yaml` secret can be specified without access and secret key:

```yaml
s3:
  bucket: gitlab-registry
  v4auth: true
  region: us-east-1
```

### LFS, Artifacts, Uploads

For LFS, artifacts and uploads an IAM role can be specified via the annotations key in the `unicorn` and `sidekiq` configuration:

```
--set gitlab.sidekiq.annotations."iam\.amazonaws\.com/role"=gitlab-storage
--set gitlab.unicorn.annotations."iam\.amazonaws\.com/role"=gitlab-storage
```

The `object-storage.yaml` can also be specified without access and secret keys, but it is necessary to add the `use_iam_profile` key:

```yaml
provider: AWS
use_iam_profile: true
region: us-east-1
```

### Backups

The `task-runner` configuration also allows for annotations to be set to upload backups to S3:

```
--set gitlab.task-runner.annotations."iam\.amazonaws\.com/role"=gitlab-backups
```

The `s3cmd.config` secret can simply be changed to not include the access and secret keys:

```
[default]
bucket_location = us-east-1
```