# Configure Charts using Globals

To reduce configuration duplication when installing our wrapper Helm chart, several configuration settings are available
to be set in the `global` section of `values.yml`. These global settings are used across several charts, all other settings
are scoped within their chart. See the [Helm documentation on globals](https://docs.helm.sh/developing_charts/#global-values)
for more information on how the global variables work.

- [Hosts](#configure-host-settings)
- [Ingress](#configure-ingress-settings)
- [GitLab Version](#gitlab-version)
- [PostgreSQL](#configure-postgresql-settings)
- [Redis](#configure-redis-settings)
- [Registry](#configure-registry-settings)
- [Gitaly](#configure-gitaly-settings)
- [Minio](#configure-minio-settings)
- [appConfig](#configure-appconfig-settings)
- [GitLab Shell](#configure-gitlab-shell-settings)
- [Custom Certificate Authorities](#custom-certificate-authorities)
- [Application Resource](#application-resource)

## Configure Host settings

The GitLab global host settings are located under the `global.hosts` key.

```YAML
global:
  hosts:
    domain: example.com
    hostSuffix: staging
    https: false
    externalIP:
    gitlab:
      name: gitlab.example.com
      https: false
    registry:
      name: registry.example.com
      https: false
    minio:
      name: minio.example.com
      https: false
```

#### domain

The base domain. GitLab and Registry will be exposed on the subdomain of this setting. This defaults to `example.com`,
but is not used for hosts that have their `name` property configured. See the `gitlab.name`, `minio.name`, and `registry.name` sections below.

#### hostSuffix

Appended to the subdomain when assembling a hostname using the base `domain`. But this is not used for hosts that have their
own `name` set.

Defaults to being unset. If set the suffix is appended to the subdomain with a hyphen.

```yaml
global:
  hosts:
    domain: example.com
    hostSuffix: staging
```

The above config would result in using external hostnames like: `gitlab-staging.example.com` and `registry-staging.example.com`

#### https

Set to false for external urls to use `http://` instead of `https`. Defaults to true. If set to true, you will need to ensure
the nginx chart has access to the certificates.

#### externalIP

Set the external IP address that will be claimed from the provider. This will be templated into the
[nginx chart](nginx/README.md#configuring-the-service), in place of the more complex `nginx.service.loadBalancerIP`.
Defaults to `nil`.

### gitlab

The `gitlab` section of `global.hosts` includes configuration for the GitLab external hostname, and which internal service
to point the hostname to.

#### gitlab.name

The hostname for gitlab. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings.

#### gitlab.https

If `hosts.https` or `gitlab.https` are `true`, the GitLab external url to use `https://` instead of `http://`. Defaults to `false`.

#### gitlab.serviceName

The name of the `service` which is operating the GitLab server. The chart will template the hostname of the service (and
current `.Release.Name`) to create the proper internal serviceName. This will default to `unicorn`

#### gitlab.servicePort

The named port of the `service` where the GitLab server can be reached. This defaults to `workhorse`.

### registry

The `registry` section of `global.hosts` includes configuration for the Registry external hostname, and which internal service
to point the hostname to.

#### registry.name

The hostname for Registry. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings.

#### registry.https

If `hosts.https` or `registry.https` are `true`, the Registry external url to use `https://` instead of `http://`. Defaults to `false`.

#### registry.serviceName

The name of the `service` which is operating the Registry server. The chart will template the hostname of the service (and
current `.Release.Name`) to create the proper internal serviceName. This will default to `registry`

#### registry.servicePort

The named port of the `service` where the Registry server can be reached. This defaults to `registry`.

### minio

The `minio` section of `global.hosts` includes configuration for the Minio external hostname, and which internal service
to point the hostname to.

#### minio.name

The hostname for Minio. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings.

#### minio.https

If `hosts.https` or `minio.https` are `true`, the Minio external url to use `https://` instead of `http://`. Defaults to `false`.

#### minio.serviceName

The name of the `service` which is operating the Minio server. The chart will template the hostname of the service (and
current `.Release.Name`) to create the proper internal serviceName. This will default to `minio`

#### minio.servicePort

The named port of the `service` where the Minio server can be reached. This defaults to `minio`.

## Configure Ingress settings

The GitLab global host settings are located under the `global.ingress` key.

|name|type|default|
|:---|:---|:------|
|[global.ingress.enabled](#global-ingress-enabled)|boolean|true|
|[global.ingress.configureCertmanager](#global-ingress-configurecertmanger)|boolean|true|
|[global.ingress.tls.secretName](#global-ingress-tls-secretName)|string|(empty)|
|[global.ingress.annotations.*annotation-key*](#global-ingress-annotations-annotation-key)|string|(empty)|

### global.ingress.enabled

Global setting that controls whether to create ingress objects for services that support them. Defaults to `true`.

### global.ingress.configureCertmanager

Global setting that controls the automatic configuration of [cert-manager](https://github.com/helm/charts/tree/master/stable/cert-manager) for ingress objects.

If `true`, relies on `certmanager-issuer.email` being set.

If `false`, and `global.ingress.tls.secretName` is not set, this will activate automatic self-signed certificate generation, which creates a **wildcard** certificate for all ingress objects.

**NOTE:** If you wish to use an external `cert-manager`, you must provide the following:
- `gitlab.unicorn.ingress.tls.secretName`
- `registry.ingress.tls.secretName`
- `minio.ingress.tls.secretName`
- `global.ingress.annotations`

Defaults to `true`.

### global.ingress.tls.secretName

The name of the [Kubernetes TLS Secret](https://kubernetes.io/docs/concepts/services-networking/ingress/#tls) that contains a **wildcard** certificate and key for the domain used in `global.hosts.domain`.

Defaults to not being set.

### global.ingress.annotations.annotation-key

Where `annotation-key` is a string that will be used with the value as an annotation on every ingress.

ex:

`global.ingress.annotations."nginx\.ingress\.kubernetes\.io/enable-access-log"=true`

No global annotations are provided by default.

## GitLab Version

The GitLab version used in the default image tag for the charts can be changed using the `global.gitlabVersion` key.

```bash
--set global.gitlabVersion=11.0.1
```

This impacts the default image tag used in the `unicorn`, `sidekiq`, and `migration` charts. Note that the `gitaly`, `gitlab-shell` and `gitlab-runner`
image tags should be separately updated to versions compatible with the GitLab version.

## Configure PostgreSQL settings

The GitLab global PostgreSQL settings are located under the `global.psql` key.

```YAML
global:
  psql:
    host: db.example.com
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
    host: redis.example.com
    port: 6379
    password:
      secret: gitlab-redis
      key: redis-password
```

For further details on these settings, see the documentation within the
[unicorn chart](gitlab/unicorn/README.md#redis)

## Configure Registry settings

The global Registry settings are located under the `global.registry` key.

```YAML
global:
  registry:
    bucket: registry
    certificate:
    httpSecret:
```

For futher details on these settings, see the documentation within the
[registry chart](registry/README.md)

## Configure Gitaly settings

The GitLab global Gitaly settings are located under the `global.gitaly` key.

```YAML
global:
  gitaly:
    internal:
      names:
        - default
        - default2
    external:
      - name: node1
        hostname: node1.example.com
        port: 8079
    authToken:
      secret: gitaly-secret
      key: token
```

For further details on these settings, see the documentation within the
[unicorn chart](gitlab/unicorn/README.md#gitaly)

## Configure Minio settings

The GitLab global Minio settings are located under the `global.minio` key.

```
global:
  minio:
    enabled: true
    credentials: {}
```

For further details on these settings, see the documentation within the
[minio chart](minio/README.md)

## Configure appConfig settings

The [unicorn][], [sidekiq][], and [task-runner][] charts share multiple settings, which are configured
with the `global.appConfig` key.

```
global:
  appConfig:
    enableUsagePing: true
    defaultCanCreateGroup: true
    usernameChangingEnabled: true
    issueClosingPattern:
    defaultTheme:
    defaultProjectsFeatures:
      issues: true
      mergeRequests: true
      wiki: true
      snippets: true
      builds: true
    webhookTimeout:
    gravatar:
      plainUrl:
      sslUrl:
    extra:
      googleAnalyticsId:
      piwikUrl:
      piwikSiteId:
    lfs:
      enabled: true
      proxy_download: true
      bucket: git-lfs
      connection: {}
    artifacts:
      enabled: true
      proxy_download: true
      bucket: gitlab-artifacts
      connection: {}
    uploads:
      enabled: true
      proxy_download: true
      bucket: gitlab-uploads
      connection: {}
    backups:
      bucket: gitlab-backups
    incomingEmail:
      enabled: false
      address: ""
      host: "imap.gmail.com"
      port: 993
      ssl: true
      startTls: false
      user: ""
      password:
        secret:
        key: password
      mailbox: inbox
      idleTimeout: 60
```

[unicorn]: gitlab/unicorn/README.md
[sidekiq]: gitlab/sidekiq/README.md
[task-runner]: gitlab/task-runner/README.md

### General application settings

The settings that can be used to tweak the general properties of the Rails
application are described below.

#### enableUsagePing

A flag to disable the [usage ping support](https://docs.gitlab.com/ee/user/admin_area/settings/usage_statistics.html).

Defaults to `true`

#### defaultCanCreateGroup

A flag to decide if users are allowed to create groups.

Defaults to `true`.

#### usernameChangingEnabled

A flag to decide if users are allowed to change their username.

Defaults to `true`.

#### issueClosingPattern

[Pattern to close issues automatically](https://docs.gitlab.com/ee/administration/issue_closing_pattern.html).
It takes a string value, and defaults to an empty value.

#### defaultTheme

[Numeric ID of the default theme for the GitLab instance](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/lib/gitlab/themes.rb#L14-25). It takes a number, denoting the id of the theme, as value and has an empty
default value.

#### defaultProjectsFeatures

Flags to decide if new projects should by default be created with respective
feature.

All flags default to `true`.

```YAML
defaultProjectsFeatures:
  issues: true
  mergeRequests: true
  wiki: true
  snippets: true
  builds: true
```

#### webHookTimeout

[Waiting time in seconds before a hook is deemed failure](https://docs.gitlab.com/ce/user/project/integrations/webhooks.html#receiving-duplicate-or-multiple-web-hook-requests-triggered-by-one-event). It takes a
number, denoting the time in seconds, as value and has an empty default value.

### Gravatar/Libravatar settings

By default, the charts work with Gravatar avatar service available at
gravatar.com. However, if needed, a custom Libravatar service can also be used.
It consists of two subkeys, both of which take string values pointing to URLs
and have an empty default value.

#### plainUrl

[HTTP URL to libravatar instance (instead of using gravatar.com)](https://docs.gitlab.com/ee/customization/libravatar.html)

#### sslUrl

[HTTPS URL to libravatar instance (instead of using gravatar.com)](https://docs.gitlab.com/ee/customization/libravatar.html)

### Hooking Analytics services to the GitLab instance

Settings to configure Analytics services like Google Analytics and Piwik are
defined under the `extra` key below `appConfig`.

#### googleAnalyticsId

Tracking ID for Google Analytics. Takes a string value as input and has an empty
default value.

#### piwikUrl

Piwik URL. Takes a string value as input and has an empty default value.

#### piwikSiteId

Piwik Site ID. Takes a string value as input and has an empty default value.

### LFS / Artifacts / Uploads

Details on these settings are below. Documentation is not repeated individually,
as they are structurally identical aside default value of the `bucket` property.

```YAML
  enabled: true
  proxy_download: true
  bucket:
  connection:
    secret:
    key:
```

#### enabled

Enable the use of these features with object storage.

Defaults to `true`

#### proxy_download

Enable proxy of all downloads via GitLab, in place of direct downloads from the `bucket`.

Defaults to `true`

#### bucket

Name of the bucket to use from object storage provider.

Defaults shown above.

#### connection

The `connection` property has been transitioned to a Kubernetes Secret. The contents
of this secret should be a yaml config file.

Defaults to `{}` and will be ignored if `global.minio.enabled` is `true`.

This property has two sub-keys: `secret` and `key`.
- `secret` is the name of a Kubernetes Secret. This value is required to use external object storage.
- `key` is the name of the key in the secret which houses the YAML block. Defaults to `connection`.

Valid configuration keys can be found at
[GitLab Job Artifacts Administration][artifactscon] documentation. This matches to
[Fog](https://github.com/fog), and is different between provider modules.

Example contents to be placed in the secret:

```
provider: AWS
aws_access_key_id: BOGUS_ACCESS_KEY
aws_secret_access_key: BOGUS_SECRET_KEY
region: us-east-1
```

[artifactscon]: https://docs.gitlab.com/ee/administration/job_artifacts.html#s3-compatible-connection-settings


### Incoming email settings

These settings are explained in [command line options page](../installation/command-line-options.md#incoming-email-configuration).

## Configure GitLab Shell

There are several items for the global configuration of [GitLab Shell](gitlab/gitlab-shell/README.md) chart.

```yaml
global:
  shell:
    port:
    authToken: {}
    hostKeys: {}
```

### Ingress port

You can control the port use by the Ingress to pass SSH traffic, as well as the port used in SSH URLs provided from GitLab via `global.shell.port`. This defaults to `22`

### Authorization token

See [authToken](gitlab/gitlab-shell#authtoken) in chart specific documentaion.

### Host Keys

See [hostKeys](gitlab/gitlab-shell#hostkeyssecret) in chart specific documentaion.

## Custom Certificate Authorities

> **NOTE**: These settings do not affect charts from outside of this repository, via requirements.yaml.

Some users may need to add custom certificate authorities, such as when using internally issued SSL certificates for TLS services. To provide this functionaliy, we provide a mechanism for injecting these custom root CAs into the application via secrets.

```
global:
  certificates:
    customCAs:
      - secret: internal-cas
      - secret: other-custom-cas
```

A user can provide any number of secrets, each containing any number of keys that hold PEM encoded CA certificates. These are configured as entries under `global.certificates.customCAs`. All keys within the secret will be mounted, so all keys across all secrets must be unique.

> **NOTE** These secrets can be named in any fashion, but they _must not_ contain key names that collide.

To create a secret:

`kubectl create secret generic custom-ca --from-file=unique_name=/path/to/cert`

To configure:

```
helm install gitlab \
  --set global.certificates.customCAs[0].secret=custom-ca
```

## Application Resource

GitLab optionally includes an [Application resource](https://github.com/kubernetes-sigs/application), which can created to identify the GitLab application within the cluster. Requires the [Application CRD](https://github.com/kubernetes-sigs/application#installing-the-crd), version`v1beta1`, to already be deployed to the cluster.

To enable, set to `global.application.create` to `true`:

```yaml
global:
  application:
    create: true
```
