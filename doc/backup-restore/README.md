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

We provide a minio instance out of the box when using this charts unless an [external object storage](../../external-object-storage/README.md) is specified. The default behavior of the task-runner pod is consistent with this behavior such that it defaults to connect to our minio unless specific settings are given. The task-runner uses `s3cmd` to connect to object storage. In order to configure connectivity to external object storage `gitlab.task-runner.backups.objectStorage.config.secret` should be specified which points to a kubernetes secret containing a `.s3cfg` file. `gitlab.task-runner.backups.objectStorage.config.key` should be specified if different from the default of `config`. This points to the key containing the contents of a .s3cfg file.

It should look like this:

`helm install gitlab \
  --set gitlab.task-runner.backups.objectStorage.config.secret=my-s3cfg \
  --set gitlab.task-runner.backups.objectStorage.config.key=config .`

s3cmd `.s3cfg` file documentation can be found [here](https://s3tools.org/kb/item14.htm)

## Backing up a GitLab installation

Follow the steps for backing up a GitLab Helm chart based installation

1. Ensure the task runner pod is running, by executing the following command

    ```
    $ kubectl get pods --all-namespaces
    ```
1. Run the backup utility
    ```
    $ kubectl exec <task-runner pod name> -it backup-utility
    ```

1. Visit the `gitlab-backups` bucket in the object storage service and ensure a tarball has been added. It will be named in `<timestamp>_<version>_gitlab_backup.tar` format.

1. This tarball is required for restoration.

## Restoring a GitLab installation

> To obtain a backup tarball of an existing GitLab instance that used other installation methods like an omnibus-gitlab package or GitLab-Omnibus helm chart, follow the instructions [given in documentation](https://docs.gitlab.com/ee/raketasks/backup_restore.html#creating-a-backup-of-the-gitlab-system)
>
> **Note**: If you are restoring a backup taken from another instance, you must migrate your existing instance to using object storage before taking the backup. See [issue 646](https://gitlab.com/charts/gitlab/issues/646)

Backup utility provided by GitLab Helm chart supports restoring a tarball from either of the following two locations

1. `gitlab-backups` bucket in the object storage service associated to the instance. This is the default scenario.
1. A public URL that can be accessed from the pod.

The steps for restoring a GitLab installation are
1. Make sure you have a running GitLab instance by deploying the charts. Ensure the `task-runner` pod is enabled and running.
1. Get the tarball ready in either of the above two locations. Make sure it is named in the `<timestamp>_<version>_gitlab_backup.tar` format.
1. Run the backup utility to restore the tarball

    ```
    $ kubectl exec <task-runner pod name> -it -- backup-utility --restore -t <timestamp>_<version>
    ```
   Here, `<timestamp>_<version>` is from the name of the tarball stored in `gitlab-backups` bucket. In case you want to provide a public URL, use the following command
    ```
    $ kubectl exec <task-runner pod name> -it -- backup-utility --restore -f <URL>
    ```
1. This process will take time depending on the size of the tarball.
1. The restoration process will erase the existing contents of database, move existing repositories to temporary locations and extract the contents of the tarball. Repositories will be moved to their corresponding locations on the disk and otherdata, like artifacts, uploads, LFS etc. will be uploaded to corresponding buckets in Object Storage.
1. Sign in to the GitLab instance and confirm the data has been restored.
