# Configure this chart with External Gitaly

This document intends to provide documentation on how to configure this Helm chart with an external Gitaly service.

If you don't have Gitaly configured, for on-premise or deployment to VM,
consider using our [Omnibus GitLab package](./external-omnibus-gitaly.md).

## Configure the Chart

Disable the `gitaly` chart and the Gitaly service it provides, and point the other services to the external service.

You need to set the following parameters:

- `gitlab.gitaly.enabled`: Set to `false` to disable the included Gitaly chart.
- `global.gitaly.host`: Set to the hostname of the external Gitaly, can be a domain or an IP address.
- `global.gitaly.authToken.secret`: The name of the [secret which contains the token for authentication][gitaly-secret].
- `global.gitaly.authToken.key`: The key within the secret, which contains the token content.
- `gitlab.gitaly.shell.authToken.secret`: The name of the [secret which contains secret for GitLab Shell][gitlab-shell-secret].
- `gitlab.gitaly.shell.authToken.key`: The key within the secret, which contains the secret content.

Items below can be further customized if you are not using the defaults:

- `global.gitaly.port`: The port the service is available on, defaults to `8075`

```
helm install .  \
  --set gitlab.gitaly.enabled=false \
  --set global.gitaly.host=gitaly.example \
  --set global.gitaly.authToken.secret=gitaly-secret \
  --set global.gitaly.authToken.key=token
```

## Multiple external Gitaly

If your implementation uses multiple Gitaly nodes external to these charts,
you can define multiple hosts as well. The syntax is slightly different, as
to allow the complexity required.

An [example values file][multiple-external] is provided, which shows the
appropriate set of configuration. The content of this values file is not
interpreted correctly via `--set` arguments, so should be passed to Helm
with the `-f / --values` flag.

[gitaly-secret]: ../../installation/secrets.md#gitaly-secret
[gitlab-shell-secret]: ../../installation/secrets.md#gitlab-shell-secret
[multiple-external]: https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/gitaly/values-multiple-external.yaml
