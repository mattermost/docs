# [Migrating from Omnibus GitLab package-based installation](index.md)

## Using built-in MinIO service for object storage

NOTE: **Note:**
Users are advised to setup an [external object storage](../../advanced/external-object-storage/index.md)
service for production use.

The easiest way to figure out the access details to built-in MinIO cluster is to
look at the `gitlab.yml` file that is generated in Sidekiq, Unicorn and
task-runner pods. Follow the steps to grab it from the Sidekiq pod

1. Find out the name of the Sidekiq pod

   ```bash
   kubectl get pods -lapp=sidekiq
   ```

1. Grab the `gitlab.yml` file from Sidekiq pod

   ```bash
   kubectl exec <sidekiq pod name> -- cat /srv/gitlab/config/gitlab.yml
   ```

1. In the `gitlab.yml` file, there will be a section for uploads with details of
   object storage connection. Something similar to the following

   ```yaml
   uploads:
     enabled: true
     object_store:
     enabled: true
     remote_directory: gitlab-uploads
     direct_upload: true
     background_upload: false
     proxy_download: true
     connection:
       provider: AWS
       region: <S3 region>
       aws_access_key_id: "<access key>"
       aws_secret_access_key: "<secret access key>"
       host: <Minio host>
       endpoint: <Minio endpoint>
       path_style: true
   ```

1. Use this information to configure object storage in `/etc/gitlab/gitlab.rb`
   file of Omnibus GitLab package-based deployment, as detailed in the [docs](https://docs.gitlab.com/ee/administration/uploads.html#s3-compatible-connection-settings).

   **Note:** For connecting to the MinIO service from outside the cluster, the
   MinIO host URL alone is enough. Helm charts based installations are
   configured to redirect requests coming to that URL automatically to the
   corresponding endpoint. So, you need not set `endpoint` value in your
   connection settings in `gitlab.rb` file.
