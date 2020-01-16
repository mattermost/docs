# Configure this chart with External Gitaly

This document intends to provide documentation on how to configure this Helm chart with an external Gitaly service.

If you don't have Gitaly configured, for on-premise or deployment to VM,
consider using our [Omnibus GitLab package](./external-omnibus-gitaly.md).

## Configure the Chart

Disable the `gitaly` chart and the Gitaly service it provides, and point the other services to the external service.

You need to set the following parameters:

- `global.gitaly.enabled`: Set to `false` to disable the included Gitaly chart.
- `global.gitaly.host`: Set to the hostname of the external Gitaly, can be a domain or an IP address.
- `global.gitaly.authToken.secret`: The name of the [secret which contains the token for authentication][gitaly-secret].
- `global.gitaly.authToken.key`: The key within the secret, which contains the token content.
- `gitlab.gitaly.shell.authToken.secret`: The name of the [secret which contains secret for GitLab Shell][gitlab-shell-secret].
- `gitlab.gitaly.shell.authToken.key`: The key within the secret, which contains the secret content.

Items below can be further customized if you are not using the defaults:

- `global.gitaly.port`: The port the service is available on, defaults to `8075`

```
helm install .  \
  --set global.gitaly.enabled=false \
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

### Connecting to external Gitaly over TLS

If your external [Gitaly server listens over TLS port](https://docs.gitlab.com/ee/administration/gitaly/#tls-support),
you can make your GitLab instance communicate with it over TLS. To do this, you
have to

1. Create a Kubernetes secret containing the certificate of the Gitaly
   server

   ```
   kubectl create secret generic gitlab-gitaly-tls-certificate --from-file=gitaly-tls.crt=<path to certificate>
   ```

1. Add the certificate of external Gitaly server to the list of
   [custom Certificate Authorities](https://docs.gitlab.com/charts/charts/globals#custom-certificate-authorities)
   In the values file, specify the following

   ```yml
   global:
     certificates:
       customCAs:
         - secret: gitlab-gitaly-tls-certificate
   ```

   or pass it to the `helm upgrade` command using `--set`

   ```
   --set global.certificates.customCAs[0].secret=gitlab-gitaly-tls-certificate
   ```

1. Enable Gitaly TLS by setting `global.gitaly.tls.enabled=true`

NOTE: **Note**: You can choose any valid secret name and key for this, but make
sure the key is unique across all the secrets specified in `customCAs` to avoid
collision since all keys within the secrets will be mounted. You **do not**
need to provide the key for the certificate, as this is the _client side_.
