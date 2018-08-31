# Backing up a GitLab installation

GitLab backups are taken by running the `backup-utility` command on the `task-runner` pod provided in the chart.

Before running the backup for the first time, you should ensure the [task-runner is properly configured](README.md) for
access to [object storage](README.md#object-storage)

Follow these steps for backing up a GitLab Helm chart based installation

## Create the backup

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

## Backup the secrets

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

## Additional Information

- [GitLab Chart Backup/Restore Introduction](README.md)
- [Restoring a GitLab installation](restore.md)
