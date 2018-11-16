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
[issue tracker](https://gitlab.com/charts/gitlab/issues), and also check out
[issue #630](https://gitlab.com/charts/gitlab/issues/630) where we recovered our
CI server from this problem.

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
