# Troubleshooting

## UPGRADE FAILED: "$name" has no deployed releases

This error will occur on your second install/upgrade if your initial
install failed.

If your initial install completely failed, and GitLab was never operational, you
should first purge the failed install before installing again.

```
helm delete --purge <release-name>
```

If instead, the initial install command timed out, but GitLab still came up successfully,
you can add the `--force` flag to the `helm upgrade` command to ignore the error
and attempt to update the release.

Otherwise, if you received this error after having previously had successful deploys
of the GitLab chart, then you are encountering a bug. Please open an issue on our
[issue tracker](https://gitlab.com/gitlab-org/charts/gitlab/issues), and also check out
[issue #630](https://gitlab.com/gitlab-org/charts/gitlab/issues/630) where we recovered our
CI server from this problem.

## Error: this command needs 2 arguments: release name, chart path

An error like this could occur when you run `helm upgrade`
and there are some spaces in the parameters. In the following
example, `Test Username` is the culprit:

```sh
helm upgrade gitlab gitlab/gitlab --timeout 600 --set global.email.display_name=Test Username ...
```

To fix it, pass the parameters in single quotes:

```sh
helm upgrade gitlab gitlab/gitlab --timeout 600 --set global.email.display_name='Test Username' ...
```

## Application containers constantly initializing

If you experience Sidekiq, Unicorn, or other Rails based containers in a constant
state of Initializing, you're likely waiting on the `dependencies` container to
pass.

If you check the logs of a given Pod specifically for the `dependencies` container,
you may see the following repeated:

```
Checking database connection and schema version
WARNING: This version of GitLab depends on gitlab-shell 8.7.1, ...
Database Schema
Current version: 0
Codebase version: 20190301182457
```

This is an indication that the `migrations` Job has not yet completed. The purpose
of this Job is to both ensure that the database is seeded, as well as all
relevant migrations are in place. The application containers are attempting to
wait for the database to be at or above their expected database version. This is
to ensure that the application does not malfunction to the schema not matching
expectations of the codebase.

1. Find the `migrations` Job. `kubectl get job -lapp=migrations`
1. Find the Pod being run by the Job. `kubectl get pod -ljob-name=<job-name>`
1. Examine the output, checking the `STATUS` column.

If the `STATUS` is `Running`, continue. If the `STATUS` is `Completed`, the application conainers should start shortly after the next check passes.

Examine the logs from this pod. `kubectl logs <pod-name>`

Any failures during the run of this job should be addressed. These will block
the use of the application until resolved. Possible problems are:

- Unreachable or failed authentication to the configured PostgreSQL database
- Unreachable or failed authentication to the configured Redis services
- Failure to reach a Gitaly instance

## Included GitLab Runner failing to register

This can happen when the runner registration token has been changed in GitLab. (This often happens after you have restored a backup)

1. Find the new shared runner token located on the `admin/runners` webpage of your GitLab installation.
1. Find the name of existing runner token Secret stored in Kubernetes

   ```
   kubectl get secrets | grep gitlab-runner-secret
   ```

1. Delete the existing secret

   ```
   kubectl delete secret <runner-secret-name>
   ```

1. Create the new secret with two keys, (`runner-regisration-token` with your shared token, and an empty `runner-token`)

   ```
   kubectl create secret generic <runner-secret-name> --from-literal=runner-registration-token=<new-shared-runner-token> --from-literal=runner-token=""
   ```

## Too many redirects

This can happen when you have TLS termination before the NGINX Ingress, and the tls-secrets are specified in the configuration.

1. Update your values to set `global.ingress.annotations."nginx.ingress.kubernetes.io/ssl-redirect": "false"`

   Via a values file:

   ```yml
   # values.yml
   global:
     ingress:
       annotations:
         "nginx.ingress.kubernetes.io/ssl-redirect": "false"
   ```

   Via the Helm CLI:

   ```sh
   helm ... --set-string global.ingress.annotations."nginx.ingress.kubernetes.io/ssl-redirect"=false
   ```

1. Apply the change

>>>
**NOTE:**
When using an external service for SSL termination, that service is responsible for redirecting to https (if so desired).
>>>
