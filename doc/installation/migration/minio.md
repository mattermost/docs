# [Migrating from Omnibus-Gitlab package based installation](./index.md)

## Using built-in Minio service for object storage

**`Note:`** Users are advised to setup an [external object storage] service for
production use.

The easiest way to figure out the access details to built-in minio cluster is to
look at the `gitlab.yml` file that is generated in sidekiq, unicorn and
task-runner pods. Follow the steps to grab it from the sidekiq pod

1. Find out the name of the sidekiq pod
    ```bash
    $ kubectl get pods -lapp=sidekiq
    ```

1. Grab the `gitlab.yml` file from sidekiq pod
    ```bash
    $ kubectl exec <sidekiq pod name> -- cat /srv/gitlab/config/gitlab.yml
    ```

1. In the gitlab.yml file, there will be a section for uploads with details of
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
   file of omnibus-gitlab package based deployment, as detailed in the [docs](https://docs.gitlab.com/ee/administration/uploads.html#s3-compatible-connection-settings).

   **Note:** For connecting to the Minio service from outside the cluster, the
   Minio host URL alone is enough. Helm charts based installations are
   configured to redirect requests coming to that URL automatically to the
   corresponding endpoint. So, you need not set `endpoint` value in your
   connection settings in `gitlab.rb` file.

[external object storage]: ../../advanced/external-object-storage/README.md
