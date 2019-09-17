# Configure Charts using Globals

To reduce configuration duplication when installing our wrapper Helm chart, several
configuration settings are available to be set in the `global` section of `values.yml`.
These global settings are used across several charts, while all other settings are scoped
within their chart. See the [Helm documentation on globals](https://helm.sh/docs/developing_charts/#global-values)
for more information on how the global variables work.

- [Hosts](#configure-host-settings)
- [Ingress](#configure-ingress-settings)
- [GitLab Version](#gitlab-version)
- [PostgreSQL](#configure-postgresql-settings)
- [Redis](#configure-redis-settings)
- [Grafana](#configure-grafana-integration)
- [Registry](#configure-registry-settings)
- [Gitaly](#configure-gitaly-settings)
- [Minio](#configure-minio-settings)
- [appConfig](#configure-appconfig-settings)
- [GitLab Shell](#configure-gitlab-shell)
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

| Name                   | Type    | Default       | Description |
|:---------------------- |:-------:|:------------- |:----------- |
| `domain`               | String  | `example.com` | The base domain. GitLab and Registry will be exposed on the subdomain of this setting. This defaults to `example.com`, but is not used for hosts that have their `name` property configured. See the `gitlab.name`, `minio.name`, and `registry.name` sections below. |
| `externalIP`           |         | `nil`         | Set the external IP address that will be claimed from the provider. This will be templated into the [nginx chart](nginx/index.md#configuring-nginx), in place of the more complex `nginx.service.loadBalancerIP`. |
| `https`                | Boolean | `true`        | If set to true, you will need to ensure the nginx chart has access to the certificates. In cases where you have TLS-termination in front of your ingresses, you probably want to look at [`global.ingress.tls.enabled`](#configure-ingress-settings). Set to false for external urls to use `http://` instead of `https`. |
| `hostSuffix`           | String  |               | [See Below](#hostsuffix). |
| `gitlab.https`         | Boolean | `false`       | If `hosts.https` or `gitlab.https` are `true`, the GitLab external url will use `https://` instead of `http://`. |
| `gitlab.name`          | String  |               | The hostname for gitlab. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings. |
| `gitlab.serviceName`   | String  | `unicorn`     | The name of the `service` which is operating the GitLab server. The chart will template the hostname of the service (and current `.Release.Name`) to create the proper internal serviceName. |
| `gitlab.servicePort`   | String  | `workhorse`   | The named port of the `service` where the GitLab server can be reached. |
| `minio.https`          | Boolean | `false`       | If `hosts.https` or `minio.https` are `true`, the Minio external url will use `https://` instead of `http://`. |
| `minio.name`           | String  |               | The hostname for Minio. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings. |
| `minio.serviceName`    | String  | `minio`       | The name of the `service` which is operating the Minio server. The chart will template the hostname of the service (and current `.Release.Name`) to create the proper internal serviceName. |
| `minio.servicePort`    | String  | `minio`       | The named port of the `service` where the Minio server can be reached. |
| `registry.https`       | Boolean | `false`       | If `hosts.https` or `registry.https` are `true`, the Registry external url will use `https://` instead of `http://`. |
| `registry.name`        | String  |               | The hostname for Registry. If set, this hostname is used, regardless of the `global.hosts.domain` and `global.hosts.hostSuffix` settings. |
| `registry.serviceName` | String  | `registry`    | The name of the `service` which is operating the Registry server. The chart will template the hostname of the service (and current `.Release.Name`) to create the proper internal serviceName. |
| `registry.servicePort` | String  | `registry`    | The named port of the `service` where the Registry server can be reached. |

### hostSuffix

The `hostSuffix` is appended to the subdomain when assembling a hostname using the
base `domain`, but is not used for hosts that have their own `name` set.

Defaults to being unset. If set, the suffix is appended to the subdomain with a hyphen.
The example below would result in using external hostnames like `gitlab-staging.example.com`
and `registry-staging.example.com`:

```yaml
global:
  hosts:
    domain: example.com
    hostSuffix: staging
```

## Configure Ingress settings

The GitLab global host settings for Ingress are located under the `global.ingress` key:

| Name                           | Type    | Default        | Description |
|:------------------------------ |:-------:|:-------        |:----------- |
| `annotations.*annotation-key*` | String  |                | Where `annotation-key` is a string that will be used with the value as an annotation on every ingress. For Example: `global.ingress.annotations."nginx\.ingress\.kubernetes\.io/enable-access-log"=true`. No global annotations are provided by default. |
| `configureCertmanager`         | Boolean | `true`         | [See below](#globalingressconfigurecertmanager). |
| `class`                        | String  | `gitlab-nginx` | Global setting that controls `kubernetes.io/ingress.class` annotation in `Ingress` resources. |
| `enabled`                      | Boolean | `true`         | Global setting that controls whether to create ingress objects for services that support them. |
| `tls.enabled`                  | Boolean | `true`         | When set to `false`, this disables TLS in Gitlab. This is useful for cases in which you cannot use TLS termination of ingresses, such as when you have a TLS-terminating proxy before the ingress controller. If you want to disable https completely, this should be set to `false` together with [`global.hosts.https`](#configure-host-settings). |
| `tls.secretName`               | String  |                | The name of the [Kubernetes TLS Secret](https://kubernetes.io/docs/concepts/services-networking/ingress/#tls) that contains a **wildcard** certificate and key for the domain used in `global.hosts.domain`. |

### global.ingress.configureCertmanager

Global setting that controls the automatic configuration of [cert-manager](https://github.com/helm/charts/tree/master/stable/cert-manager)
for ingress objects. If `true`, relies on `certmanager-issuer.email` being set.

If `false` and `global.ingress.tls.secretName` is not set, this will activate automatic
self-signed certificate generation, which creates a **wildcard** certificate for all
ingress objects.

NOTE: **Note:** If you wish to use an external `cert-manager`, you must provide the following:

- `gitlab.unicorn.ingress.tls.secretName`
- `registry.ingress.tls.secretName`
- `minio.ingress.tls.secretName`
- `global.ingress.annotations`

## GitLab Version

The GitLab version used in the default image tag for the charts can be changed using
the `global.gitlabVersion` key:

```bash
--set global.gitlabVersion=11.0.1
```

This impacts the default image tag used in the `unicorn`, `sidekiq`, and `migration`
charts. Note that the `gitaly`, `gitlab-shell` and `gitlab-runner` image tags should
be separately updated to versions compatible with the GitLab version.

## Configure PostgreSQL settings

The GitLab global PostgreSQL settings are located under the `global.psql` key. For
more details, see the documentation within the [unicorn chart](gitlab/unicorn/index.md#postgresql).

```YAML
global:
  psql:
    host: db.example.com
    # serviceName:
    port: 5432
    preparedStatements: false
    password:
      secret: gitlab-postgres
      key: psql-password
```

If you want to connect Gitlab with a PostgreSQL database over mutual TLS, create a secret
containing the client key, client certificate and server certificate authority as different
secret keys. Then describe the secret's structure using the `global.psql.ssl` mapping.

```YAML
global:
  psql:
    host: db.example.com
    # ... further settings like in the previous example ...
    ssl:
      secret: db-example-ssl-secrets # Name of the secret
      clientKey: key.pem             # Secret key of the certificate's key
      clientCertificate: cert.pem    # Secret key storing the certificate
      serverCA: server-ca.pem        # Secret key containing the CA for the database server
```

## Configure Redis settings

The GitLab global Redis settings are located under the `global.redis` key. For more
details on these settings, see the documentation within the [unicorn chart](gitlab/unicorn/index.md#redis).

```YAML
global:
  redis:
    host: redis.example.com
    # serviceName:
    port: 6379
    password:
      enabled: true
      secret: gitlab-redis
      key: redis-password
```

## Configure Grafana integration

The GitLab global grafana settings are located under `global.grafana`. At this time, the only setting available is `global.grafana.enabled`.

When set to `true`, the GitLab chart will deploy the [Grafana chart](https://github.com/helm/helm/tree/master/stable/grafana), expose it under `/-/grafana` of the GitLab Ingress, and pre-configure it with a secure random password. The generated password can be found in the Secret named `gitlab-grafana-initial-root-password`.

The GitLab chart connects to the deployed Prometheus instance.

## Configure Registry settings

The global Registry settings are located under the `global.registry` key. For more
details on these settings, see the documentation within the [registry chart](registry/index.md).

```YAML
global:
  registry:
    bucket: registry
    certificate:
    httpSecret:
```

## Configure Gitaly settings

The global Gitaly settings are located under the `global.gitaly` key.

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
        port: 8075
    authToken:
      secret: gitaly-secret
      key: token
```

### Gitaly hosts

[Gitaly](https://gitlab.com/gitlab-org/gitaly) is a service that provides high-level
RPC access to Git repositories, which handles all Git calls made by GitLab.

Administrators can chose to use Gitaly nodes in the following ways:

- [Internal to the chart](#internal), as part of a `StatefulSet` via the [Gitaly chart](gitlab/gitaly/).
- [External to the chart](#external), as external pets.
- [Mixed environment](#mixed) using both internal and external nodes.

See [Repository Storage Paths](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)
documentation for details on managing which nodes will be used for new projects.

NOTE: **Note:** If `gitaly.host` is provided, `gitaly.internal` and `gitaly.external`
  properties will *be ignored*. See the [deprecated Gitaly settings](#deprecated-gitaly-settings).

#### Internal

The `internal` key currently consists of only one key, `names`, which is a list of
[storage names](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)
to be managed by the chart. For each listed name, *in logical order*, one pod will
be spawned, named `${releaseName}-gitaly-${ordinal}`, where `ordinal` is the index
within the `names` list. If dynamic provisioning is enabled, the `PersistentVolumeClaim`
will match.

This list defaults to `['default']`, which provides for 1 pod related to one
[storage path](https://docs.gitlab.com/ee/administration/repository_storage_paths.html).

NOTE: **Note:** Manual scaling of this item is required, by adding or removing entries in
  `gitaly.internal.names`. When scaling down, any repository that has not been moved
  to another node will become unavailable. Since the Gitaly chart is a `StatefulSet`,
  dynamically provisioned disks *will not* be reclaimed. This means the data disks
  will persist, and the data on them can be accessed when the set is scaled up again
  by re-adding a node to the `names` list.

A sample [configuration of multiple internal nodes](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/gitaly/values-multiple-internal.yaml)
can be found in the examples folder.

#### External

The `external` key provides a configuration for Gitaly nodes external to the cluster.
Each item of this list has 3 keys:

- `name`: The name of the [storage](https://docs.gitlab.com/ee/administration/repository_storage_paths.html).
- `hostname`: The host of Gitaly services.
- `port`: (optional) The port number to reach the host on. Defaults to `8075`.

NOTE: **Note:** You must have an entry with `name: default`.

A sample [configuration of multiple external nodes](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/gitaly/values-multiple-external.yaml)
can be found in the examples folder.

#### Mixed

It is possible to use both internal and external Gitaly nodes, but be aware that:

- There must always be a node named `default`, which Internal provides by default.
- External nodes will be populated first, then Internal.

A sample [configuration of mixed internal and external nodes](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/gitaly/values-multiple-mixed.yaml)
can be found in the examples folder.

### authToken

The `authToken` attribute for Gitaly has two sub keys:

- `secret` defines the name of the kubernetes `Secret` to pull from.
- `key` defines the name of the key in the above secret that contains the authToken.

NOTE: **Note:** All Gitaly nodes **must** share the same authentication token.

### Deprecated Gitaly settings

| Name                         | Type    | Default | Description |
|:---------------------------- |:-------:|:------- |:----------- |
| `host` *(deprecated)*        | String  |         | The hostname of the Gitaly server to use. This can be omitted in lieu of `serviceName`. If this setting is used, it will override any values of `internal` or `external`. |
| `port` *(deprecated)*        | Integer | `8075`  | The port on which to connect to the Gitaly server. |
| `serviceName` *(deprecated)* | String  |         | The name of the `service` which is operating the Gitaly server. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Gitaly as a part of the overall GitLab chart. |

## Configure Minio settings

The GitLab global Minio settings are located under the `global.minio` key. For more
details on these settings, see the documentation within the [minio chart](minio/index.md).

```
global:
  minio:
    enabled: true
    credentials: {}
```

## Configure appConfig settings

The [unicorn](gitlab/unicorn/index.md), [sidekiq](gitlab/sidekiq/index.md), and
[gitaly](gitlab/gitaly/index.md) charts share multiple settings, which are configured
with the `global.appConfig` key.

```
global:
  appConfig:
    enableUsagePing: true
    enableImpersonation: true
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
      containerRegistry: true
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
    packages:
      enabled: true
      proxy_download: true
      bucket: gitlab-packages
      connection: {}
    externalDiffs:
      enabled:
      when:
      proxy_download: true
      bucket: gitlab-mr-diffs
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
    pseudonymizer:
      configMap:
      bucket: gitlab-pseudo
      connection: {}
    cron_jobs: {}
```

### General application settings

The `appConfig` settings that can be used to tweak the general properties of the Rails
application are described below:

| Name                                | Type    | Default | Description |
|:----------------------------------- |:-------:|:------- |:----------- |
| `enableUsagePing`                   | Boolean | `true`  | A flag to disable the [usage ping support](https://docs.gitlab.com/ee/user/admin_area/settings/usage_statistics.html). |
| `enableImpersonation`               |         | `nil`   | A flag to disable [user impersonation by Administrators](https://docs.gitlab.com/ee/api/README.html#disable-impersonation). |
| `defaultCanCreateGroup`             | Boolean | `true`  | A flag to decide if users are allowed to create groups. |
| `usernameChangingEnabled`           | Boolean | `true`  | A flag to decide if users are allowed to change their username. |
| `issueClosingPattern`               | String  | (empty) | [Pattern to close issues automatically](https://docs.gitlab.com/ee/administration/issue_closing_pattern.html). |
| `defaultTheme`                      | Integer |         | [Numeric ID of the default theme for the GitLab instance](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/lib/gitlab/themes.rb#L14-25). It takes a number, denoting the id of the theme. |
| `defaultProjectsFeatures.*feature*` | Boolean | `true`  | [See below](#defaultProjectsFeatures) |
| `webHookTimeout`                    | Integer |         | Waiting time in seconds before a [hook is deemed to have failed](https://docs.gitlab.com/ce/user/project/integrations/webhooks.html#receiving-duplicate-or-multiple-web-hook-requests-triggered-by-one-event). |

#### defaultProjectsFeatures

Flags to decide if new projects should be created with the respective features by
default. All flags default to `true`.

```YAML
defaultProjectsFeatures:
  issues: true
  mergeRequests: true
  wiki: true
  snippets: true
  builds: true
  containerRegistry: true
```

### Gravatar/Libravatar settings

By default, the charts work with Gravatar avatar service available at gravatar.com.
However, a custom Libravatar service can also be used if needed:

| Name                | Type   | Default | Description |
|:------------------- |:------:|:------- |:----------- |
| `gravatar.plainURL` | String | (empty) | [HTTP URL to libravatar instance (instead of using gravatar.com)](https://docs.gitlab.com/ee/customization/libravatar.html). |
| `gravatar.sslUrl`   | String | (empty) | [HTTPS URL to libravatar instance (instead of using gravatar.com)](https://docs.gitlab.com/ee/customization/libravatar.html). |

### Hooking Analytics services to the GitLab instance

Settings to configure Analytics services like Google Analytics and Piwik are defined
under the `extra` key below `appConfig`:

| Name                      | Type   | Default | Description |
|:------------------------- |:------:|:------- |:----------- |
| `extra.googleAnalyticsId` | String | (empty) | Tracking ID for Google Analytics. |
| `extra.piwikSiteId`       | String | (empty) | Piwik Site ID. |
| `extra.piwikUrl`          | String | (empty) | Piwik Url. |

### LFS, Artifacts, Uploads, Packages, and External MR diffs

Details on these settings are below. Documentation is not repeated individually,
as they are structurally identical aside from the default value of the `bucket` property.

```YAML
  enabled: true
  proxy_download: true
  bucket:
  connection:
    secret:
    key:
```

| Name             | Type    | Default | Description |
|:---------------- |:-------:|:------- |:----------- |
| `enabled`        | Boolean | `true` except for MR diffs  | Enable the use of these features with object storage. |
| `proxy_download` | Boolean | `true`  | Enable proxy of all downloads via GitLab, in place of direct downloads from the `bucket`. |
| `bucket`         | String  | Various | Name of the bucket to use from object storage provider. Default will be `git-lfs`, `gitlab-artifacts`, `gitlab-uploads`, or `gitlab-packages`, depending on the service. |
| `connection`     | String  | `{}`    | [See below](#connection). |

#### connection

The `connection` property has been transitioned to a Kubernetes Secret. The contents
of this secret should be a YAML formatted file. Defaults to `{}` and will be ignored
if `global.minio.enabled` is `true`.

This property has two sub-keys: `secret` and `key`.

- `secret` is the name of a Kubernetes Secret. This value is required to use external object storage.
- `key` is the name of the key in the secret which houses the YAML block. Defaults to `connection`.

Valid configuration keys can be found in the [GitLab Job Artifacts Administration](https://docs.gitlab.com/ee/administration/job_artifacts.html#s3-compatible-connection-settings)
documentation. This matches to [Fog](https://github.com/fog), and is different between
provider modules.

Examples for [AWS](https://fog.io/storage/#using-amazon-s3-and-fog) and [Google](https://fog.io/storage/#google-cloud-storage)
providers can be found in [examples/objectstorage](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage).

- [rails.s3.yaml](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/rails.s3.yaml)
- [rails.gcs.yaml](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/rails.gcs.yaml)

Once a YAML file containing the contents of the `connection` has been created, use
this file to create the secret in Kubernetes.

```bash
kubectl create secret generic gitlab-rails-storage \
    --from-file=connection=rails.yaml
```

#### when (only for External MR Diffs)

`externalDiffs` setting has an additional  key `when` to
[conditionally store specific diffs on object storage](https://docs.gitlab.com/ee/administration/merge_request_diffs.html#alternative-in-database-storage).
This setting is left empty by default in the Charts, for a default value to be
assigned by the Rails code.

### Incoming email settings

The incoming email settings are explained in the [command line options page](../installation/command-line-options.md#incoming-email-configuration).

### LDAP

The `ldap.servers` setting allows for the configuration of [LDAP](https://docs.gitlab.com/ee/administration/auth/ldap.html)
user authentication. It is presented as a map, which will be translated into the appropriate
LDAP servers configuration in `gitlab.yml`, as with an installation from source.

Configuring passwords can be done by supplying a `secret` which holds the password.
This password will then be injected into GitLab's configuration at runtime.

An example configuration snippet:

```YAML
ldap:
  servers:
    # 'main' is the GitLab 'provider ID' of this LDAP server
    main:
      label: 'LDAP'
      host: '_your_ldap_server'
      port: 636
      uid: 'sAMAccountName'
      bind_dn: 'cn=administrator,cn=Users,dc=domain,dc=net'
      password:
        secret: my-ldap-password-secret
        key: the-key-containing-the-password
```

Example `--set` configuration items, when using the global chart:

```
--set global.appConfig.ldap.servers.main.label='LDAP' \
--set global.appConfig.ldap.servers.main.host='your_ldap_server' \
--set global.appConfig.ldap.servers.main.port='636' \
--set global.appConfig.ldap.servers.main.uid='sAMAccountName' \
--set global.appConfig.ldap.servers.main.bind_dn='cn=administrator\,cn=Users\,dc=domain\,dc=net'
--set global.appConfig.ldap.servers.main.password.secret='my-ldap-password-secret'
--set global.appConfig.ldap.servers.main.password.key='the-key-containing-the-password'
```

NOTE: **Note:** Commas are considered [special characters](https://github.com/kubernetes/helm/blob/master/docs/using_helm.md#the-format-and-limitations-of---set)
  within Helm `--set` items. Be sure to escape commas in values such as `bind_dn`: `--set global.appConfig.ldap.servers.main.bind_dn='cn=administrator\,cn=Users\,dc=domain\,dc=net'`.

#### Using a custom CA or self signed LDAP certificates

If the LDAP server uses a custom CA or self-signed certificate, you must:

1. Ensure that the custom CA/Self-Signed certificate is created as a secret in the cluster/namespace:

   ```bash
   kubectl -n gitlab create secret generic my-custom-ca --from-file=my-custom-ca.pem
   ```

1. Then, specify:

   ```bash
   --set global.certificates.customCAs[0].secret=my-custom-ca.pem
   --set global.appConfig.ldap.servers.main.ca_file=/etc/ssl/certs/ca-cert-my-custom-ca.pem
   ```

This will ensure that the CA is mounted in the relevant pods under `/etc/ssl/certs/ca-cert-my-custom-ca.pem` and specifies its use in the LDAP configuration.

### OmniAuth

GitLab can leverage OmniAuth to allow users to sign in using Twitter, GitHub, Google,
and other popular services. Expanded documentation can be found in the [OmniAuth documentation](https://docs.gitlab.com/ee/integration/omniauth.html)
for GitLab.

```YAML
omniauth:
  enabled: false
  autoSignInWithProvider:
  syncProfileFromProvider: []
  syncProfileAttributes: ['email']
  allowSingleSignOn: ['saml']
  blockAutoCreatedUsers: true
  autoLinkLdapUser: false
  autoLinkSamlUser: false
  externalProviders: []
  providers: []
  # - secret: gitlab-google-oauth2
  #   key: provider
```

| Name                      | Type    | Default     | Description |
|:------------------------- |:-------:|:----------- |:----------- |
| `allowSingleSignOn`       | Boolean | `false`     | Enable the automatic creation of accounts when signing in with OmniAuth. |
| `autoLinkLdapUser`        | Boolean | `false`     | Can be used if you have LDAP / ActiveDirectory integration enabled. When enabled, users automatically created through OmniAuth will be linked to their LDAP entry as well. |
| `autoLinkSamlUser`        | Boolean | `false`     | Can be used if you have SAML integration enabled. When enabled, users automatically created through OmniAuth will be linked to their SAML entry as well. |
| `autoSignInWithProvider`  |         | `nil`       | Single provider name allowed to automatically sign in. This should match the name of the provider, such as `saml` or `google_oauth2`. |
| `blockAUtoCreatedUsers`   | Boolean | `true`      | If `true` auto created users will be blocked by default and will have to be unblocked by an administrator before they are able to sign in. |
| `enabled`                 | Boolean | `false`     | Enable / disable the use of OmniAuth with GitLab. |
| `externalProviders`       |         | `[]`        | You can define which OmniAuth providers you want to be `external`, so that all users **creating accounts, or logging in via these providers** will be unable to access internal projects. You will need to use the full name of the provider, like `google_oauth2` for Google. See [Configure OmniAuth Providers as External](https://docs.gitlab.com/ee/integration/omniauth.html#configure-omniauth-providers-as-external). |
| `providers`               |         | `[]`        | [See below](#providers). |
| `syncProfileAttributes`   |         | `['email']` | List of profile attributes to sync from the provider upon login. See [Keep OmniAuth user profiles up to date](https://docs.gitlab.com/ee/integration/omniauth.html#keep-omniauth-user-profiles-up-to-date) for options. |
| `syncProfileFromProvider` |         | `[]`        | List of provider names that GitLab should automatically sync profile information from. Entries should match the name of the provider, such as `saml` or `google_oauth2`. See [Keep OmniAuth user profiles up to date](https://docs.gitlab.com/ee/integration/omniauth.html#keep-omniauth-user-profiles-up-to-date). |

#### providers

`providers` is presented as an array of maps that are used to populate `gitlab.yml`
as when installed from source. See GitLab documentation for the available selection
of [Supported Providers](https://docs.gitlab.com/ee/integration/omniauth.html#supported-providers).
Defaults to `[]`.

This property has two sub-keys: `secret` and `key`:

- `secret`: *(required)* The name of a Kubernetes `Secret` containing the provider block.
- `key`: *(optional)* The name of the key in the `Secret` containing the provider block.
  Defaults to `provider`

The `Secret` for these entries contains YAML or JSON formatted blocks, as described
in [OmniAuth Providers](https://docs.gitlab.com/ee/integration/omniauth.html). To
create this secret, follow the appropriate instructions for retrieval of these items,
and create a YAML or JSON file.

Example of configuration of Google OAuth2:

```YAML
name: google_oauth2
label: Google
app_id: 'APP ID'
app_secret: 'APP SECRET'
args:
  access_type: offline
  approval_prompt: ''
```

This content can be saved as `provider.yaml`, and then a secret created from it:

```bash
kubectl create secret generic -n NAMESPACE SECRET_NAME --from-file=provider=provider.yaml
```

Once created, the `providers` are enabled by providing the maps in configuration, as
shown below:

```YAML
omniauth:
  providers:
    - secret: gitlab-google-oauth2
    - secret: gitlab-azure-oauth2
    - secret: gitlab-cas3
```

Example configuration `--set` items, when using the global chart:

```bash
--set global.appConfig.omniauth.providers[0].secret=gitlab-google-oauth2 \
```

Due to the complexity of using `--set` arguments, a user may wish to use a YAML snippet,
passed to `helm` with `-f omniauth.yaml`.

### Pseudonymizer settings

Use these settings to configure the [Pseudonymizer service](https://docs.gitlab.com/ee/administration/pseudonymizer.html).

```
global:
  appConfig:
    pseudonymizer:
      configMap:
      bucket: gitlab-pseudo
      connection: {}
```

| Name          | Type    | Default         | Description |
|:------------- |:-------:|:--------------- |:----------- |
| `bucket`      | String  | `gitlab-pseudo` | Name of the bucket to use from the object storage provider. |
| `configMap`   | String  |                 | [See Below](#configMap). |
| `connnection` |         | `{}`            | [See Below](#connection). |

#### configMap

Name of the `configMap` containing a custom manifest file. Defaults to empty.

GitLab ships with a [default manifest file for Pseudonymizer](https://gitlab.com/gitlab-org/gitlab-ee/blob/master/config/pseudonymizer.yml).
Users can provide a custom one as a configMap.

First, create a configMap:

```bash
kubectl create configmap <name of the configmap> --from-file=pseudonymizer.yml=<path to pseudonymizer_config.yml>
```

NOTE: **Note:** Please make sure the key specified in the above command to create configMap
  is `pseudonymizer.yml`. It is used to point the service to the correct location and
  an incorrect key will cause Pseudonymizer to not work.

Then pass the argument `--set global.appConfig.pseudonymizer.configMap=<name of the configmap>`
to the `helm install` command to instruct GitLab to use this manifest instead of the
default one.

#### connection

Details of the Kubernetes secret that contains the connection information for the
object storage provider. The contents of this secret should be a YAML formatted file.

Defaults to `{}` and will be ignored if `global.minio.enabled` is `true`.

This property has two sub-keys: `secret` and `key`:

- `secret` is the name of a Kubernetes Secret. This value is required to use external object storage.
- `key` is the name of the key in the secret which houses the YAML block. Defaults to `connection`.

Examples for [AWS (s3)](https://fog.io/storage/#using-amazon-s3-and-fog) and [Google (GCS)](https://fog.io/storage/#google-cloud-storage)
providers can be found in [examples/objectstorage](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage):

- [rails.s3.yaml](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/rails.s3.yaml)
- [rails.gcs.yaml](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/rails.gcs.yaml)

Once a YAML file containing the contents of the `connection` has been created, create
the secret in Kubernetes:

```bash
kubectl create secret generic gitlab-rails-storage \
    --from-file=connection=rails.yaml
```

### Cron jobs related settings

Sidekiq includes maintenance jobs that can be configured to run on a periodic
basis using cron style schedules. A few examples are included below. See the
sample [gitlab.yml](https://gitlab.com/gitlab-org/gitlab-ee/blob/master/config/gitlab.yml.example#L237-302)
for more job examples.

These settings are shared between Sidekiq, Unicorn (for showing tooltips in UI)
and task-runner (for debugging purposes) pods.

```YAML
global:
  appConfig:
    cron_jobs:
      stuck_ci_jobs_worker:
        cron: "0 * * * *"
      pipeline_schedule_worker:
        cron: "19 * * * *"
      expire_build_artifacts_worker:
        cron: "50 * * * *"
```

## Configure GitLab Shell

There are several items for the global configuration of [GitLab Shell](gitlab/gitlab-shell/index.md)
chart.

```yaml
global:
  shell:
    port:
    authToken: {}
    hostKeys: {}
```

| Name        | Type    | Default | Description |
|:----------- |:-------:|:------- |:----------- |
| `port`      | Integer | `22`    | You can control the port used by the Ingress to pass SSH traffic, as well as the port used in SSH URLs provided from GitLab via `global.shell.port`. |
| `authToken` |         |         | See [authToken](gitlab/gitlab-shell/index.md#authtoken) in the GitLab Shell chart specific documentation. |
| `hostKeys`  |         |         | See [hostKeys](gitlab/gitlab-shell/index.md#hostkeyssecret) in the GitLab Shell chart specific documentation. |

## Custom Certificate Authorities

NOTE: **Note:**: These settings do not affect charts from outside of this repository,
  via `requirements.yaml`.

Some users may need to add custom certificate authorities, such as when using internally
issued SSL certificates for TLS services. To provide this functionaliy, we provide
a mechanism for injecting these custom root CAs into the application via secrets.

```
global:
  certificates:
    customCAs:
      - secret: internal-cas
      - secret: other-custom-cas
```

A user can provide any number of secrets, each containing any number of keys that hold
PEM encoded CA certificates. These are configured as entries under `global.certificates.customCAs`.
All keys within the secret will be mounted, so all keys across all secrets must be unique.

NOTE: **Note:** These secrets can be named in any fashion, but they *must not* contain
  key names that collide.

To create a secret:

```bash
kubectl create secret generic custom-ca --from-file=unique_name=/path/to/cert
```

To configure the secret:

```
helm install gitlab \
  --set global.certificates.customCAs[0].secret=custom-ca
```

## Application Resource

GitLab can optionally include an [Application resource](https://github.com/kubernetes-sigs/application),
which can be created to identify the GitLab application within the cluster. Requires the
[Application CRD](https://github.com/kubernetes-sigs/application#installing-the-crd),
version `v1beta1`, to already be deployed to the cluster.

To enable, set `global.application.create` to `true`:

```yaml
global:
  application:
    create: true
```

Some environments, such as Google GKE Marketplace, do not allow the creation
of ClusterRole resources. Set the following values to disable ClusterRole
components in the Application Custom Resource Definition as well as the
relevant charts packaged with Cloud Native GitLab.

```yaml
global:
  application:
    allowClusterRoles: false
  operator:
     enabled: false
nginx:
  controller:
    scope:
      enabled: true
gitlab-runner:
  rbac:
    clusterWideAccess: false
certmanager:
  install: false
```
