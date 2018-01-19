# Configure Charts using Globals

To reduce configuration duplication when installing our wrapper Helm chart, several configuration settings are available
to be set in the `global` section of `values.yml`. These global settings are used across several charts, all other settings
are scoped within their chart. See the [Helm documentation on globals](https://docs.helm.sh/developing_charts/#global-values)
for more information on how the global variables work.

## Configure Host settings

The GitLab global host settings are located under the `global.hosts` key.

```YAML
global:
  hosts:
    domain: example.local
    hostSuffix: staging
    https: false
    tls:
      secretName: example-tls
    gitlab:
      name: gitlab.example.local
      https: false
      serviceName: unicorn
      servicePort: workhorse
      tls:
        secretName: gitlab-example-tls
    registry:
      name: registry.example.local
      https: false
      serviceName: registry
      servicePort: registry
      tls:
         secretName: registry.example.local
```

#### domain

The base domain. GitLab and Registry will be exposed on the subdomain of this setting. This defaults to `example.local`,
but is not used for hosts that have their `name` property configured. See the `gitlab.name` and `registry.name` sections below.

#### hostSuffix

Appended to the subdomain when assembling a hostname using the base `domain`. But this is not used for hosts that have their
own `name` set.

Defaults to being unset. If set the suffix is appended to the subdomain with a hyphen.

```yaml
global:
  hosts:
    domain: example.local
    hostSuffix: staging
```

The above config would result in using external hostnames like: `gitlab-staging.example.local` and `registry-staging.example.local`

#### https

Set to true for external urls to use `https://` instead of `http`. Defaults to false. If set to true, you will need to ensure
the nginx chart has access to the certificates. This can be done by providing the `tls.secretName` (see below) or by setting
up [kube-lego](../kube-lego/README.md) and enabling [acme support in the nginx chart](nginx/README.md#acme).

#### tls.secretName

Set the name of the [Kubernetes TLS Secret][Secret] that contains the **wildcard** certificate and key to use for all subdomains
of the base `domain` ([See our docs on creating the secrets][GitLab Secrets]). Alternatively you can give each host a different
certificate in their own `tls` section. See `gitlab.tls.secretName` and `registry.tls.secretName` below.

Defaults to not being set.

*Note:* This secretName is ignored if kube-lego is being used on the ingress, in favor of the `acme` secret.

### gitlab

The `gitlab` section of `global.hosts` includes configuration for the GitLab external hostname, and which internal service
to point the hostname to.

#### gitlab.name

The hostname for gitlab. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings.

#### gitlab.https

Set to true for the GitLab external url to use `https://` instead of `http`. Defaults to false. If set to true, the `gitlab.tls.secretName`
should also be provided

#### gitlab.serviceName

The name of the `service` which is operating the GitLab server. The chart will template the hostname of the service (and
current `.Release.Name`) to create the proper internal serviceName. This will default to `unicorn`

#### gitlab.servicePort

The named port of the `service` where the GitLab server can be reached. This defaults to `workhorse`.

#### gitlab.tls.secretName

The name of the [Kubernetes TLS Secret][Secret] that containers a certificate and key for the gitlab external hostname.
Falls back to the `global.hosts.tls.secretName` when not provided. Defaults to not being set.

*Note:* This secretName is ignored if kube-lego is being used on the ingress, in favor of the `acme` secret.

### registry

The `registry` section of `global.hosts` includes configuration for the Registry external hostname, and which internal service
to point the hostname to.

#### registry.name

The hostname for Registry. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings.

#### registry.https

Set to true for the Registry external url to use `https://` instead of `http`. Defaults to false. If set to true, the `registry.tls.secretName`
should also be provided

#### registry.serviceName

The name of the `service` which is operating the Registry server. The chart will template the hostname of the service (and
current `.Release.Name`) to create the proper internal serviceName. This will default to `registry`

#### registry.servicePort

The named port of the `service` where the Registry server can be reached. This defaults to `registry`.

#### registry.tls.secretName

The name of the [Kubernetes TLS Secret][Secret] that containers a certificate and key for the Registry external hostname.
Falls back to the `global.hosts.tls.secretName` when not provided. Defaults to not being set.

*Note:* This secretName is ignored if kube-lego is being used on the ingress, in favor of the `acme` secret.

[Secret]:https://kubernetes.io/docs/concepts/configuration/secret/
[GitLab Secrets]:../installation/secrets.md
