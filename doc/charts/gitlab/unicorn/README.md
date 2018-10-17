# Using the GitLab-Unicorn Chart

The `unicorn` sub-chart provides the gitlab rails web-server running two unicorn workers per pod. (The minimum necessary for a single pod to be able to serve any web request in GitLab)

Currently the container used in the chart also includes a copy of gitlab-workhorse, which we haven't yet split out.

## Requirements

This chart depends on Redis, PostgreSQL, Gitaly, and Registry services, either as part of the complete GitLab chart or provided as external services reachable from the Kubernetes cluster this chart is deployed onto.

# Configuration

The `unicorn` chart is configured as follows: Global Settings, Ingress Settings External Services, and Chart Settings.

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                        | Description                                    | Default                                          |
| ---                              | ---                                            | ---                                              |
| replicaCount                     | Unicorn number of replicas                     | 1                                                |
| image.repository                 | Unicorn image repository                       | registry.gitlab.com/gitlab-org/build/cng/gitlab-unicorn-ee |
| image.tag                        | Unicorn image tag                              |                                                  |
| image.pullPolicy                 | Unicorn image pull policy                      | Always                                           |
| image.pullSecrets                | Secrets for the image repository               |                                                  |
| init.image                       | initContainer image                            | busybox                                          |
| init.tag                         | initContainer image tag                        | latest                                           |
| service.name                     | Unicorn service name                           | unicorn                                          |
| service.type                     | Unicorn service type                           | ClusterIP                                        |
| service.externalPort             | Unicorn exposed port                           | 8080                                             |
| service.internalPort             | Unicorn internal port                          | 8080                                             |
| service.workhorseExternalPort    | Workhorse exposed port                         | 8181                                             |
| service.workhorseInternalPort    | Workhorse internal port                        | 8181                                             |
| enabled                          | Unicorn enabled flag                           | true                                             |
| workerProcesses                  | Unicorn number of workers                      | 2                                                |
| hpa.targetAverageValue           | Set the autoscaling target value               | 400m                                             |
| workerTimeout                    | Unicorn worker timeout                         | 60                                               |
| metrics.enabled                  | Toggle Prometheus metrics exporter             | true                                             |
| ldap.servers                     | LDAP user authentication servers               | nil                                              |
| omniauth.enabled                 | Enable OmniAuth                                | false                                            |
| omniauth.autoSignInWithProvider  | Allow automatic SSO from this provider         | nil                                              |
| omniauth.syncProfileFromProvider | Enable profile syncing from providers          | []                                               |
| omniauth.syncProfileAttributes   | List of profile attributes to sync             | ['email']                                        |
| omniauth.allowSingleSignOn       | Providers allowed automatic account creation   | ['saml']                                         |
| omniauth.blockAutoCreatedUsers   | Block automatically created users by default   | true                                             |
| omniauth.autoLinkLdapUser        | Automatically link LDAP users                  | false                                            |
| omniauth.autoLinkSamlUser        | Automatically link SAML users                  | false                                            |
| omniauth.externalProviders       | List of providers to be treated as external    | []                                               |
| omniauth.providers               | List of secrets for Omniauth providers         | nil                                              |
| redis.serviceName                | Redis service name                             | redis                                            |
| psql.password.secret             | psql secret name                               | gitlab-postgres                                  |
| psql.password.key                | Key to psql password in psql secret            | psql-password                                    |
| shell.authToken.secret           | Shell token secret                             | gitlab-shell-secret                              |
| shell.authToken.key              | Key to shell token in shell secret             | secret                                           |
| shell.port                       | Port number to use in SSH URLs generated by UI | nil                                              |
| gitaly.serviceName               | Gitaly service name                            | gitaly                                           |
| minio.bucket                     | Name of storage bucket, when using Minio       | git-lfs                                          |
| minio.serviceName                | Name of Minio service                          | minio-svc                                        |
| minio.port                       | Port for Minio service                         | 9000                                             |
| registry.enabled                 | Add/Remove registry link in all projects menu  | true                                             |
| registry.api.protocol            | Registry protocol                              | http                                             |
| registry.api.serviceName         | Registry service name                          | registry                                         |
| registry.api.port                | Registry port                                  | 5000                                             |
| registry.tokenIssuer             | Registry token issuer                          | gitlab-issuer                                    |
| resources.requests.cpu           | Unicorn minimum cpu                            | 200m                                             |
| resources.requests.memory        | Unicorn minimum memory                         | 1.4G                                             |
| extras.google_analytics_id       | Google Analytics Id for frontend               | nil                                              |
| rack_attack.git_basic_auth       | See [GitLab documentation][rackattack] for details | {}                                           |
| trusted_proxies                  | See [GitLab documentation][proxies] for details | []                                              |
| gitlab.unicorn.workhorse.image   | Workhorse image repository                     | registry.gitlab.com/gitlab-org/build/cng/gitlab-workhorse-ee |
| gitlab.unicorn.workhorse.tag     | Workhorse image tag                            |                                                  |
## Chart configuration examples
### image.pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image:
  repository: my.unicorn.repository
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

## Using the Community Edition of this chart

By default, the Helm charts use the Enterprise Edition of GitLab. If desired, you can instead use the Community Edition. Learn more about the [difference between the two](https://about.gitlab.com/installation/ce-or-ee/).

In order to use the Community Edition, set `image.repository` to `registry.gitlab.com/gitlab-org/build/cng/gitlab-unicorn-ce`
and `workhorse.image` to `registry.gitlab.com/gitlab-org/build/cng/gitlab-workhorse-ce`

## Global Settings

We share some common global settings among our charts. See the [Globals Documentation][globals] for common configuration
options, such as GitLab and Registry hostnames.

## Ingress Settings

|name|type|default|
|:---|:---|:------|
|[ingress.enabled](#ingress-enabled)|boolean|false|
|[ingress.tls.secretName](#ingress-tls-secretName)|string|(empty)|
|[ingress.annotations.*annotation-key*](#ingress-annotations-annotation-key)|string|(empty)|

### ingress.enabled

Setting that controls whether to create ingress objects for services that support them.

When `false` the `global.ingress.enabled` setting is used.

Defaults to `false`.

### ingress.tls.secretName

The name of the Kubernetes TLS Secret that contains a valid certificate and key for the gitlab url.

When not set, the `global.ingress.tls.secretName` is used instead.

Defaults to not being set.

### ingress.annotations.annotation-key

Where `annotation-key` is a string that will be used with the value as an annotation on every ingress.

ex:

`ingress.annotations."nginx\.ingress\.kubernetes\.io/enable-access-log"=true`

No annotations are provided by default.

## External Services

### Redis

```YAML
redis:
  host: redis.example.com
  serviceName: redis
  port: 6379
  password:
    secret: gitlab-redis
    key: redis-password
```

#### host

The hostname of the Redis server with the database to use. This can be omitted in lieu of `serviceName`

#### serviceName

The name of the `service` which is operating the Redis database. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Redis as a part of the overall GitLab chart. This will default to `redis`

#### port

The port on which to connect to the Redis server. Defaults to `6379`.

#### password

The `password` attribute for Redis has to sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the password.

### PostgreSQL

```YAML
psql:
  host: psql.example.com
  port: 5432
  database: gitlabhq_production
  username: gitlab
  password:
    secret: gitlab-postgres
    key: psql-password
```

#### host

The hostname of the PostgreSQL server with the database to use. This can be omitted if `postgresql.install=true` (default non-production).

#### port

The port on which to connect to the PostgreSQL server. Defaults to `5432`.

#### database

The name of the database to use on the PostgreSQL server. This defaults to `gitlabhq_production`.

#### username

The username with which to authenticate to the database. This defaults to `gitlab`

#### password

The `password` attribute for PostgreSQL has to sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the password.

### Gitaly

```YAML
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

#### host

The hostname of the Gitaly server to use. This can be omitted in lieu of `serviceName`

#### serviceName

The name of the `service` which is operating the Gitaly server. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Gitaly as a part of the overall GitLab chart. This will default to `gitaly`

#### port

The port on which to connect to the Gitaly server. Defaults to `8075`.

#### authToken

The `authToken` attribute for Gitaly has to sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the authToken.

### Minio

```YAML
minio:
  serviceName: 'minio-svc'
  port: 9000
```

#### serviceName

Name of the `Service` that exposed by Minio pod.

Defaults to `minio-svc`.

#### port

Port number to reach the Minio `Service` on.

Defaults to `9000`.

### Registry

```YAML
registry:
  host: registry.example.com
  port: 443
  api:
    protocol: http
    host: registry.example.com
    serviceName: registry
    port: 5000
  tokenIssuer: gitlab-issuer
  certificate:
    secret: gitlab-registry
    key: registry-auth.key
```

#### host

The external hostname to use for providing docker commands to users in the GitLab UI. Falls back to the value set in the
`registry.hostname` template. Which determines the registry hostname based on the values set in `global.hosts`. See the [Globals Documentation][globals]
for more information.

#### port

The external port used in the hostname. Using port `80` or `443` will result in the URLs being formed with `http`/`https`. Other ports
will all use `http` and append the port to the end of hostname. ex: `http://registry.example.com:8443`

#### api

Field `api` is a map containing four items: `host`, `protocol`, `serviceName`, and `port`

#### api.host

The hostname of the Registry server to use. This can be omitted in lieu of `api.serviceName`

#### api.protocol

The protocol Unicorn should use to reach the Registry api.

#### api.serviceName

The name of the `service` which is operating the Registry server. If this is present, and `api.host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `api.host` value. This is convenient when using Registry as a part of the overall GitLab chart. This will default to `registry`

#### api.port

The port on which to connect to the Registry api. Defaults to `5000`.

#### tokenIssuer

The name of the auth token issuer. This must match the name used in the Registry's configuration, as it incorporated into the token when it is sent. Defaults to `gitlab-issuer`, which is the same default we use in the Registry chart.

#### certificate

Field `certificate` is a map containing two items: `secret` and `key`.

#### certificate.secret

`secret` is a string containing the name of the [Kubernetes Secret][kubernetes-secret] that houses the certificate bundle to be used to verify the tokens created by the GitLab instance(s).

#### certificate.key

`key` is the name of the `key` in the `Secret` which houses the certificate
bundle that will be provided to the [registry][] container as `auth.token.rootcertbundle`.

## Chart Settings

The following values are used to configure the Unicorn Pods.

#### replicaCount

Field `replicaCount` is an integer, controlling the number of Unicorn instances to create in the deployment. This defaults to `1`.

#### workerProcesses

Field `workerProcesses` is an integer, controller the number of Unicorn workers to run per pod. You must have at least `2` workers available in your cluster in order for GitLab to properly function. Note that as you increase the `workerProcesses` the memory required will increase by approximately `400MB`, so you should update the pod `resources` accordingly.  `workerProcesses` defaults to `2`.

#### workerTimeout

Field `workerTimeout` is an integer specifying the number of seconds a request can be pending before it times out. Defaults to `60`

### metrics.enabled

By default, each pod exposes a metrics endpoint at `/-/metrics`. Metrics are only available when [GitLab Prometheus metrics](https://docs.gitlab.com/ee/administration/monitoring/prometheus/gitlab_metrics.html) are enabled in the Admin area. When metrics are enabled, annotations are added to each pod allowing a Prometheus server to discover and scrape the exposed metrics.

#### ldap.servers

This setting allows for the configuration of [LDAP](https://docs.gitlab.com/ee/administration/auth/ldap.html) user authentication. It is presented as a map, which will be translated into the the appropriate LDAP servers configuration in `gitlab.yml`, as with an installation from source.

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
```

Example configuration `--set` items, when using the global chart:
```
--set gitlab.unicorn.ldap.servers.main.label='LDAP' \
--set gitlab.unicorn.ldap.servers.main.host='your_ldap_server' \
--set gitlab.unicorn.ldap.servers.main.port='636' \
--set gitlab.unicorn.ldap.servers.main.uid='sAMAccountName' \
--set gitlab.unicorn.ldap.servers.main.bind_dn='cn=administrator\,cn=Users\,dc=domain\,dc=net'
```

Commas are considered [special characters](https://github.com/kubernetes/helm/blob/master/docs/using_helm.md#the-format-and-limitations-of---set) within Helm `--set` items. Be sure to escape commas in values such as `bind_dn`: `--set gitlab.unicorn.ldap.servers.main.bind_dn='cn=administrator\,cn=Users\,dc=domain\,dc=net'`

### OmniAuth

GitLab can leverage OmniAuth to allow users to sign in using Twitter, GitHub, Google, and other popular services. Expanded documentation can be found in [OmniAuth documentation][omniauth] for GitLab.

```YAML
gitlab:
  unicorn:
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

#### enabled

Enable / disable the use of OmniAuth with GitLab.

Defaults to `false`

#### autoSignInWithProvider

Single provider name to be allowed to automatically sign in. This should match the name of the provider, such as `saml` or `google_oauth2`.

Defaults to `nil`

#### syncProfileFromProvider

List of provider names that GitLab should automatically sync profile information from. Entries should match the name of the provider, such as `saml` or `google_oauth2`

Defaults to `[]`

See [Keep OmniAuth user profiles up to date][omniauth-profiles]

#### syncProfileAttributes

List of profile attributes to sync from the provider upon login. See [Keep OmniAuth user profiles up to date][omniauth-profiles] for options.

Defaults to `['email']`

#### allowSingleSignOn

Enable the automatic creation of accounts when signing in with OmniAuth.

Defaults to `false`

#### blockAutoCreatedUsers

If `true` auto created users will be blocked by default and will have to be unblocked by an administrator before they are able to sign in.

Defaults to `true`

#### autoLinkLdapUser

`autoLinkLdapUser` can be used if you have LDAP / ActiveDirectory integration enabled. When enabled, users automatically created through OmniAuth will be linked to their LDAP entry as well.

Defaults to `false`

#### autoLinkSamlUser

`autoLinkSamlUser` can be used if you have SAML integration enabled. When enabled, users automatically created through OmniAuth will be linked to their SAML entry as well.

Defaults to `false`

#### externalProviders

You can define which OmniAuth providers you want to be `external` so that all users **creating accounts, or logging in via these providers** will not be able to have access to internal projects. You will need to use the full name of the provider, like `google_oauth2` for Google.

Defaults to `[]`

See [Configure OmniAuth Providers as External](https://docs.gitlab.com/ee/integration/omniauth.html#configure-omniauth-providers-as-external)

#### providers

`providers` is presented as an array of maps that are used to populate `gitlab.yml` as when installed from source. The available selection of [Supported Providers](https://docs.gitlab.com/ee/integration/omniauth.html#supported-providers) can be found in GitLab documentation.

Member items:
- `secret`: (required) The name of a Kubernetes `Secret` containing the provider block.
- `key`: (optional) The name of the key in the `Secret` containing provider block. Defaults to `provider`

The `Secret` for these entries contains YAML or JSON formatted blocks, as describe in [OmniAuth Providers][omniauth-providers]. To create this secret, follow the appropriate instructions for retrieval of these items, and create a YAML or JSON file.

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

This content can be saved `provider.yaml`, and then a secret created from it: `kubectl create secret generic -n NAMESPACE SECRET_NAME --from-file=provider=provider.yaml`

Once created, the `providers` are enabled by providing the map in configuration, as shown below.

```YAML
gitlab:
  unicorn:
    omniauth:
      providers:
        - secret: gitlab-google-oauth2
        - secret: gitlab-azure-oauth2
        - secret: gitlab-cas3
```

Example configuration `--set` items, when using the global chart:
```
--set gitlab.unicorn.omniauth.providers[0].secret=gitlab-google-oauth2 \
```

Due to the complexity of using `--set` arguments, a user may wish to use a YAML snippet, passed to `helm` with `-f omniauth.yaml`.

Defaults to `[]`.

### GitLab Shell

GitLab Shell uses an Auth Token in its communication with Unicorn. Share the token with GitLab Shell and Unicorn using a shared Secret.

```YAML
shell:
  authToken:
   secret: gitlab-shell-secret
   key: secret
  port:
```

#### authToken

The `authToken` attribute for Gitaly has to sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the authToken.

#### port

The port number to use in the generation of SSH URLs within the GitLab UI. Defaults to `22`, and is controlled by `global.shell.port`.


[registry]: https://hub.docker.com/_/registry/
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[globals]: ../../globals.md
[lfscon]: https://docs.gitlab.com/ee/workflow/lfs/lfs_administration.html
[uplcon]: https://docs.gitlab.com/ee/administration/uploads.html#using-object-storage
[rackattack]: https://docs.gitlab.com/ee/security/rack_attack.html
[proxies]: https://docs.gitlab.com/ee/install/installation.html#adding-your-trusted-proxies
[omniauth]: https://docs.gitlab.com/ee/integration/omniauth.html
[omniauth-providers]: https://docs.gitlab.com/ee/integration/omniauth.html
[omniauth-profiles]: https://docs.gitlab.com/ee/integration/omniauth.html#keep-omniauth-user-profiles-up-to-date
