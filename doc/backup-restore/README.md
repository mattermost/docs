# Backuping up and Restoring GitLab instances

GitLab Helm chart provides a specific pod named `task-runner` that acts as an interface for the purpose of backing up and restoring GitLab instances. It is equipped with a `backup-utility` executable which interacts with other necessary pods for this task.
Technical details for how the utility works can be found in the [architecture documentation](../architecture/backup-restore.md).

## Prerequisites

1. Backup and Restore procedures described here have only been tested with S3 compatible APIs. Support for other object storage services, like Google Cloud Storage, will be tested in future revisions.
1. During restoration, the backup tarball needs to be extracted to disk. This means the `task-runner` pod should have disk of necessary size available.
1. This chart relies on the use of [object storage](#object-storage) for `artifacts`, `uploads`, and `lfs objects`, and does not currently migrate these for you during restore. If you are restoring a backup taken from another instance, you must migrate your existing instance to using object storage before taking the backup. See [issue 646](https://gitlab.com/charts/gitlab/issues/646).
1. Restoration process does not update the `gitlab-initial-root-password` secret with the value from backup. For logging in as `root`, use the original password included in the backup.. In case the password is no longer accessible, follow the steps below to reset it.
    1. Attach to the unicorn pod by executing the command

        ```bash
        $ kubectl exec <unicorn pod name> -it bash
        ```
    1. Run the following command to reset the password of `root` user. Replace `#{password}` with a password of your choice
        ```bash
        $ /srv/gitlab/bin/rails runner "user = User.first; user.password='#{password}'; user.password_confirmation='#{password}'; user.save!"
        ```

## Object storage

We provide a minio instance out of the box when using this charts unless an [external object storage](../advanced/external-object-storage/README.md) is specified. The default behavior of the task-runner pod defaults to connect to our minio unless specific settings are given.

The task-runner uses `s3cmd` to connect to object storage. In order to configure connectivity to external object storage `gitlab.task-runner.backups.objectStorage.config.secret` should be specified which points to a kubernetes secret containing a `.s3cfg` file. `gitlab.task-runner.backups.objectStorage.config.key` should be specified if different from the default of `config`. This points to the key containing the contents of a .s3cfg file.

It should look like this:

`helm install gitlab \
  --set gitlab.task-runner.backups.objectStorage.config.secret=my-s3cfg \
  --set gitlab.task-runner.backups.objectStorage.config.key=config .`

s3cmd `.s3cfg` file documentation can be found [here](https://s3tools.org/kb/item14.htm)

In addition, two bucket locations need to be configured, one for storing the backups, and one temporary bucket that is used
when restoring a backup.

```
--set global.appConfig.backups.bucket=gitlab-backup-storage
--set global.appConfig.backups.tmpBucket=gitlab-tmp-storage
```

## Backing up a GitLab installation

Follow the steps for backing up a GitLab Helm chart based installation

### Create the backup

1. Ensure the task runner pod is running, by executing the following command

    ```
    $ kubectl get pods --all-namespaces | grep task-runner
    ```
1. Run the backup utility
    ```
    $ kubectl exec <task-runner pod name> -it backup-utility
    ```

1. Visit the `gitlab-backups` bucket in the object storage service and ensure a tarball has been added. It will be named in `<timestamp>_<version>_gitlab_backup.tar` format.

1. This tarball is required for restoration.

### Backup the secrets

You should also save a copy of the rails secrets. (These are not included in the backup as a security precaution. We recommend keeping your full backup that includes the database separate from the copy of the secrets.)

1. Find the object name for the rails secrets

  ```
  $ kubectl get secrets | grep rails-secret
  ```

1. Save a copy of the rails secrets

  ```
  $ kubectl get secrets <rails-secret-name> -o "jsonpath={.data['secrets\.yml']}" | base64 --decode > secrets.yaml
  ```

1. Store `secrets.yml` in a secure location, you may need it to fully restore your backups.

## Restoring a GitLab installation

> To obtain a backup tarball of an existing GitLab instance that used other installation methods like an omnibus-gitlab package or GitLab-Omnibus helm chart, follow the instructions [given in documentation](https://docs.gitlab.com/ee/raketasks/backup_restore.html#creating-a-backup-of-the-gitlab-system)
>
> **Note**: If you are restoring a backup taken from another instance, you must migrate your existing instance to using object storage before taking the backup. See [issue 646](https://gitlab.com/charts/gitlab/issues/646)

Backup utility provided by GitLab Helm chart supports restoring a tarball from any of the following locations

1. The `gitlab-backups` bucket in the object storage service associated to the instance. This is the default scenario.
1. A public URL that can be accessed from the pod.
1. A local file that you can copy to the `task-runner` pod using `kubectl cp`

### Restoring the backup file

The steps for restoring a GitLab installation are

1. Make sure you have a running GitLab instance by deploying the charts. Ensure the `task-runner` pod is enabled and running.
1. Get the tarball ready in any of the above locations. Make sure it is named in the `<timestamp>_<version>_gitlab_backup.tar` format.
1. Run the backup utility to restore the tarball

    ```
    $ kubectl exec <task-runner pod name> -it -- backup-utility --restore -t <timestamp>_<version>
    ```
   Here, `<timestamp>_<version>` is from the name of the tarball stored in `gitlab-backups` bucket. In case you want to provide a public URL, use the following command
    ```
    $ kubectl exec <task-runner pod name> -it -- backup-utility --restore -f <URL>
    ```

    You can provide a local path as a URL as long as it's in the format: `file://<path>`

1. This process will take time depending on the size of the tarball.
1. The restoration process will erase the existing contents of database, move existing repositories to temporary locations and extract the contents of the tarball. Repositories will be moved to their corresponding locations on the disk and other data, like artifacts, uploads, LFS etc. will be uploaded to corresponding buckets in Object Storage.

### Restoring the secrets

#### Restore the rails secrets

The GitLab chart expects rails secrets to be provided as a Kubernetes Secret with content in yaml. Create a local file with the following content:

```yaml
production:
  db_key_base: <your key base value>
  secret_key_base: <your secret key base value>
  otp_key_base: <your otp key base value>
  openid_connect_signing_key: <your openid signing key>
```

The values should be replaced with matching values from your backup instances rails secrets. For omnibus install they were found in the `/etc/gitlab/gitlab-secrets.json` file, and for other install types you should have a `secrets.yml` file that contains them.

Once you have the secrets created as a local yaml file:

1. Find the object name for the rails secrets

  ```
  $ kubectl get secrets | grep rails-secret
  ```

1. Delete the existing secret

  ```
  $ kubectl delete secret <rails-secret-name>
  ```

1. Create the new secret using the same name as the old, and passing in your local yaml file

  ```
  $ kubectl create secret generic <rails-secret-name> --from-file=secrets.yml=<local-yaml-filepath>
  ```

#### Restore the runner registration token

After restoring, the included runner will not be able to register to the instance because it no longer has the correct registration token.
Follow these [troubleshooting steps](../troubleshooting/README.md#included-gitlab-runner-failing-to-register) to get it updated.

### Restart the pods

In order to use the new changes, the `unicorn` and `sidekiq` pods need to be restarted. The easiest way to restart everything is to run:

```
$ helm upgrade gitlab gitlab/gitlab \
  --timeout 600 \
  --reuse-values \
  --recreate-pods
```

where the first `gitlab` is the release name you used when installing.
