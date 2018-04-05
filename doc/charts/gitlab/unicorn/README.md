# Using the GitLab-Unicorn Chart

The `unicorn` sub-chart provides the gitlab rails web-server running two unicorn workers per pod. (The minimum necessary for a single pod to be able to serve any web request in GitLab)

Currently the container used in the chart also includes a copy of gitlab-workhorse, which we haven't yet split out.

## Requirements

This chart depends on Redis, PostgreSQL, Gitaly, and Registry services, either as part of the complete GitLab chart or provided as external services reachable from the Kubernetes cluster this chart is deployed onto.

# Configuration

The `unicorn` chart is configured as follows: Global Settings, Ingress Settings External Services, and Chart Settings.

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                     | Description                                    | Default                                          |
| ---                           | ---                                            | ---                                              |
| replicaCount                  | Unicorn number of replicas                     | 1                                                |
| image.repository              | Unicorn image repository                       | registry.com/gitlab-org/build/cng/gitlab-unicorn |
| image.tag                     | Unicorn image tag                              | latest                                           |
| image.pullPolicy              | Unicorn image pull policy                      | Always                                           |
| service.name                  | Unicorn service name                           | unicorn                                          |
| service.type                  | Unicorn service type                           | ClusterIP                                        |
| service.externalPort          | Unicorn exposed port                           | 8080                                             |
| service.internalPort          | Unicorn internal port                          | 8080                                             |
| service.workhorseExternalPort | Workhorse exposed port                         | 8181                                             |
| service.workhorseInternalPort | Workhorse internal port                        | 8181                                             |
| enabled                       | Unicorn enabled flag                           | true                                             |
| workerProcesses               | Unicorn number of workers                      | 2                                                |
| workerTimeout                 | Unicorn worker timeout                         | 60                                               |
| omniauth.providers            | Omniauth providers                             | nil                                              |
| railsSecrets.secret           | Secret containing rails secrets.yml            | rails-secrets                                    |
| railsSecrets.key              | Key to contents of secrets.yml in rails secret | secrets.yml                                      |
| redis.serviceName             | Redis service name                             | redis                                            |
| redis.password.secret         | Redis secret                                   | gitlab-redis                                     |
| redis.password.key            | Key to redis password in redis secret          | redis-password                                   |
| psql.serviceName              | psql service name                              | omnibus                                          |
| psql.password.secret          | psql secret name                               | gitlab-postgres                                  |
| psql.password.key             | Key to psql password in psql secret            | psql-password                                    |
| shell.authToken.secret        | Shell token secret                             | gitlab-shell-secret                              |
| shell.authToken.key           | Key to shell token in shell secret             | secret                                           |
| gitaly.serviceName            | Gitaly service name                            | gitaly                                           |
| gitaly.authToken.secret       | Gitaly secret name                             | gitaly-secret                                    |
| gitaly.authToken.key          | Key to gitaly token in gitaly secret           | token                                            |
| lfs.enabled                   | Enable Git LFS storage                         | true                                             |
| lfs.proxy_download            | Proxy all LFS downloads through GitLab         | true                                             |
| lfs.bucket                    | Object storage bucket name                     | nil                                              |
| lfs.connection                | See [GitLab documentation][lfscon] for details | {}                                               |
| minio.bucket                  | Name of storage bucket, when using Minio       | git-lfs                                          |
| minio.credentials.secret      | Secret containing access/secret keys for Minio | gitlab-minio                                     |
| minio.serviceName             | Name of Minio service                          | minio-svc                                        |
| minio.port                    | Port for Minio service                         | 9000                                             |
| registry.api.protocol         | Registry protocol                              | http                                             |
| registry.api.serviceName      | Registry service name                          | registry                                         |
| registry.api.port             | Registry port                                  | 5000                                             |
| registry.tokenIssuer          | Registry token issuer                          | gitlab-issuer                                    |
| registry.certificate.secret   | Registry certificate                           | gitlab-registry                                  |
| registry.certificate.key      | Registry certificate key                       | registry-auth.key                                |
| resources.requests.cpu        | Unicorn minimum cpu                            | 200m                                             |
| resources.requests.memory     | Unicorn minimum memory                         | 1.4G                                             |

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
  host: redis.example.local
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
  host: psql.example.local
  serviceName: omnibus
  port: 5432
  database: gitlabhq_production
  username: gitlab
  password:
    secret: gitlab-postgres
    key: psql-password
```

#### host

The hostname of the PostgreSQL server with the database to use. This can be omitted in lieu of `serviceName`

#### serviceName

The name of the `service` which is operating the PostgreSQL database. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using PostgreSQL as a part of the overall GitLab chart. This will default to `omnibus`

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
  host: gitaly.example.local
  serviceName: 'gitaly'
  port: 8075
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

### LFS

```YAML
lfs:
  enabled: true
  proxy_download: true
  bucket: git-lfs
  connection: {}
```

#### enabled

Enable the use of Git LFS storage, via object storage.

Defaults to `true`

#### proxy_download

Enable proxy of all LFS downloads via GitLab, in place of direct downloads from the `bucket`.

Defaults to `true`

#### bucket

Name of the bucket to use from object storage provider.

Defaults to `nil`, not used when `minio.enabled: true`

#### connection

The `connection` property is a YAML block, in accordance with the documentation
present at [GitLab LFS Administration][lfscon] documentation. This matches to
[Fog](https://github.com/fog), is different between provider modules.

Defaults to `{}` and will be ignored if `minio.enabled` is `true`.

### Minio

```YAML
minio:
  enabled: true
  bucket: git-lfs
  credentials:
    secret: gitlab-minio
  serviceName: 'minio-svc'
  port: 9000
```

#### enabled

Enable the use of the in-chart Minio provider for object storage. When `true`, all settings provided under `lfs.connection` will be ignored.

Defaults to `true`

#### bucket

Name of the bucket on Minio service to use.

See [Minio chart documentation](../../minio/README.md#defaultbuckets) for further details on bucket naming and creation.

Defaults to `git-lfs`.

#### credentials.secret

Name of `secret` which holds the credentials (`accesskey`, `secretkey`) for accessing Minio.

Defaults to `gitlab-minio`, as generated by [`shared-secrets` Job](../../../charts/gitlab/charts/shared-secrets)

#### serviceName

Name of the `Service` that exposed by Minio pod.

Defaults to `minio-svc`.

#### port

Port number to reach the Minio `Service` on.

Defaults to `9000`.

### Registry

```YAML
registry:
  host: registry.example.local
  port: 443
  api:
    protocol: http
    host: registry.example.local
    serviceName: registry
    port: 5000
  tokenIssuer: gitlab-issuer
  certificate:
    secret: gitlab-registry
    key: registry-auth.key
```

#### host

The external hostname to use for providing docker commands to users in the GitLab UI. Falls back to the value set in the
`registryHost` template. Which determines the registry hostname based on the values set in `global.hosts`. See the [Globals Documentation][globals]
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

#### omniauth.providers

This setting allows for the configuration of [Omniauth Providers](https://docs.gitlab.com/ee/integration/omniauth.html). It is presented as an array of maps, which will be translated into the the appropriate configuration in `gitlab.yml`, as with an instllation from source. The available selection of [Supported Providers](https://docs.gitlab.com/ee/integration/omniauth.html#supported-providers) can be found in GitLab documentation.

Required items:
- `name`: The name to be given for this provider.
- `secretName`: The name of a Kubernetes `Secret` containing two items: `app_id` and `app_secret`.

The `Secret` for these entries contains two items: `app_id` and `app_secret`. To create this secret, follow the appropriate instructions for retrieval of these items, then use the following command.
```
kubectl create secret generic -n NAMESPACE SECRET_NAME \
    --from-literal=app_id='APP_ID' \
    --from-literal=app_secret='APP_SECRET'
```

If your chosen provider requires arguments, they should be supplied as items under `args` per the example below.


An example configuration snippet:
```YAML
omniauth:
  providers:
    - name: google_oauth2
      secretName: gitlab-google-oauth2
      args:
        access_type: offline
        approval_prompt: ''
```

Example configuration `--set` items, when using the global chart:
```
--set gitlab.unicorn.omniauth.providers[0].name=google_oauth2 \
--set gitlab.unicorn.omniauth.providers[0].secretName=gitlab-google-oauth2 \
--set gitlab.unicorn.omniauth.providers[0].args.access_type=offline \
--set gitlab.unicorn.omniauth.providers[0].args.approval_prompt=''
```

Due to the complexity of using `--set` arguments, a user may with to use a YAML snippet, passed to `helm` with `-f omniauth.yaml`. If this is done for the global chart, note that that `omniauth` should be nested under `gitlab.unicorn` as shown below.

```YAML
gitlab:
  unicorn:
    omniauth:
```

Defaults to `[]`, which results in Omniauth being disabled.

### GitLab Shell

GitLab Shell uses an Auth Token in its communication with Unicorn. Share the token with GitLab Shell and Unicorn using a shared Secret.

```YAML
shell:
  authToken:
   secret: gitlab-shell-secret
   key: secret
```

#### authToken

The `authToken` attribute for Gitaly has to sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the authToken.


[registry]: https://hub.docker.com/_/registry/
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[globals]: ../../globals.md
[lfscon]: https://docs.gitlab.com/ee/workflow/lfs/lfs_administration.html
