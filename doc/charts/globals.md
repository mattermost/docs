# Configure Charts using Globals

To reduce configuration duplication when installing our wrapper Helm chart, several configuration settings are available
to be set in the `global` section of `values.yml`. These global settings are used across several charts, all other settings
are scoped within their chart. See the [Helm documentation on globals](https://docs.helm.sh/developing_charts/#global-values)
for more information on how the global variables work.

- [Hosts](#configure-host-settings)
- [Ingress](#configure-ingress-settings)
- [PostgreSQL](#configure-postgresql-settings)
- [Redis](#configure-redis-settings)
- [Gitaly](#configure-gitaly-settings)

## Configure Host settings

The GitLab global host settings are located under the `global.hosts` key.

```YAML
global:
  hosts:
    domain: example.local
    hostSuffix: staging
    https: false
    externalIP:
    gitlab:
      name: gitlab.example.local
      https: false
    registry:
      name: registry.example.local
      https: false
    minio:
      name: minio.example.local
      https: false
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

Set to false for external urls to use `http://` instead of `https`. Defaults to true. If set to true, you will need to ensure
the nginx chart has access to the certificates.

#### externalIP

Set the external IP address that will be claimed from the provider. This will be templated into the
[nginx chart](nginx/README.md#configuring-the-service), in place of the more complex `nginx.service.loadBalancerIP`.
Defaults to `nil`.

#### tls.secretName

Set the name of the [Kubernetes TLS Secret][Secret] that contains a **wildcard** certificate and key to use for all subdomains
of the base `domain` ([See our docs on creating the secrets][GitLab Secrets]). Alternatively you can give each host a different
certificate in their own `tls` section. See `gitlab.tls.secretName` and `registry.tls.secretName` below.

Defaults to not being set.

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

### minio

The `minio` section of `global.hosts` includes configuration for the Minio external hostname, and which internal service
to point the hostname to.

#### minio.name

The hostname for Minio. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings.

#### minio.https

Set to true for the Minio external url to use `https://` instead of `http`. Defaults to false. If set to true, the `minio.tls.secretName`
should also be provided

#### minio.serviceName

The name of the `service` which is operating the Minio server. The chart will template the hostname of the service (and
current `.Release.Name`) to create the proper internal serviceName. This will default to `minio`

#### minio.servicePort

The named port of the `service` where the Minio server can be reached. This defaults to `minio`.

#### minio.tls.secretName

The name of the [Kubernetes TLS Secret][Secret] that containers a certificate and key for the Minio external hostname.
Falls back to the `global.hosts.tls.secretName` when not provided. Defaults to not being set.

## Configure Ingress settings

The GitLab global host settings are located under the `global.ingress` key.

|name|type|default|
|:---|:---|:------|
|[global.ingress.enabled](#global-ingress-enabled)|boolean|true|
|[global.ingress.tls.secretName](#global-ingress-tls-secretName)|string|(empty)|
|[global.ingress.annotations.*annotation-key*](#global-ingress-annotations-annotation-key)|string|(empty)|

### global.ingress.enabled

Global setting that controls whether to create ingress objects for services that support them. Defaults to `true`.

### global.ingress.tls.secretName

The name of the [Kubernetes TLS Secret][Secret] that contains a **wildcard** certificate and key for the domain used in `global.hosts.domain`.

Defaults to not being set.

### global.ingress.annotations.annotation-key

Where `annotation-key` is a string that will be used with the value as an annotation on every ingress.

ex:

`global.ingress.annotations."nginx\.ingress\.kubernetes\.io/enable-access-log"=true`

No global annotations are provided by default.

## Configure PostgreSQL settings

The GitLab global PostgreSQL settings are located under the `global.psql` key.

```YAML
global:
  psql:
    host: db.example.local
    port: 5432
    password:
      secret: gitlab-postgres
      key: psql-password
```

For further details on these settings, see the documentation within the
[unicorn chart](gitlab/unicorn/README.md#postgresql)

## Configure Redis settings

The GitLab global Redis settings are located under the `global.redis` key.

```YAML
global:
  redis:
    host: redis.example.local
    port: 6379
    password:
      secret: gitlab-redis
      key: redis-password
```

For further details on these settings, see the documentation within the
[unicorn chart](gitlab/unicorn/README.md#redis)

## Configure Gitaly settings

The GitLab global Gitaly settings are located under the `global.gitaly` key.

```YAML
global:
  gitaly:
    host: gitaly.example.local
    port: 8079
    authToken:
      secret: gitaly-secret
      key: token
```

For further details on these settings, see the documentation within the
[unicorn chart](gitlab/unicorn/README.md#gitaly)
