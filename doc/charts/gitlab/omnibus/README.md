# Using the Omnibus GitLab container

The `omnibus` sub-chart provides the [Omnibus GitLab][og-docker] container as a
stepping stone for development of component isolation. It is intended to provide
a method for testing and development of each other sub-chart as we migrate to
individual component / concerns per chart.

This is container is not meant to be a permanent member of this chart. It should
not be used for anything other than development and testing.

**NOTE:** *This chart does not persist any data.* This means that it will be a fresh container on every pod deployment, and absolutely no state is persisted.

## Design Choices

This sub-chart was implemented explicitly to ease the development process of
[this helm chart][helm-gitlab]. Every sub-component that will eventually be
extracted has been configured to expose itself over their respective default TCP ports to enable inter-container communication.

Components / Services not exposed:
- The [Registry][registry] sub-chart had already been completed.
- [Mattermost][mattermost] is a contained service.
- [GitLab Pages][gl-pages] requires being present on a different address to the
primary services
- Prometheus could be exposed, but was not.

The available components are:
- psql (on by default)

The components below have been replaced by other charts
- [nginx][]
- [redis][]
- shell ([gitlab-shell][] / ssh)
- [unicorn][] (primary Rails)
- [workhorse][unicorn] (primary in-line smart proxy)
- [sidekiq][]
- [gitaly][]

# Configuration

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                         | Description                            | Default                                                           |
| ---                               | ---                                    | ---                                                               |
| replicaCount                      | Omnibus replicas                       | 1                                                                 |
| image.repository                  | Omnibus image repository               | gitlab/gitlab-ee                                                  |
| image.tag                         | Omnibus image tag                      | nightly                                                           |
| image.pullPolicy                  | Omnibus image pull policy              | Always                                                            |
| service.name                      | Omnibus service name                   | omnibus                                                           |
| service.type                      | Omnibus service type                   | ClusterIP                                                         |
| service.clusterIP                 | Omnibus cluster IP                     | 0.0.0.0                                                           |
| service.ports.psql                | Omnibus psql port                      | 5432                                                              |
| enabled                           | Omnibus enable flag                    | true                                                              |
| external_url                      | Omnibus external url                   | http://example.local                                              |
| trusted_proxies                   |                                        | ["127.0.0.1/24", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"] |
| redis.serviceName                 | Redis service name                     | redis                                                             |
| redis.password.secret             | Redis secret                           | gitlab-redis                                                      |
| redis.password.key                | Key to redis password in redis secret  | redis-password                                                    |
| psql.shared_buffers               | Size of psql shared buffers            | 1MB                                                               |
| psql.password.secret              | Secret containing psql password        | gitlab-postgres                                                   |
| psql.password.key                 | Key to psql password in psql secret    | psql-password                                                     |
| psql.persistence.enabled          | psql persistence enabled flag          | true                                                              |
| psql.persistence.accessMode       | psql persistence access mode           | ReadWriteOnce                                                     |
| psql.persistence.size             | psql persistence volume size           | 10Gi                                                              |
| psql.persistence.subPath          | psql persistence volume mountpath      |                                                                   |
| psql.persistence.storageClass     | psql storageClassName for provisioning |                                                                   |
| psql.persistence.volumeName       | psql Existing persistent volume name   |                                                                   |
| psql.persistence.matchLabels      | psql Label-value matches to bind       |                                                                   |
| psql.persistence.matchExpressions | psql Label-expression matches to bind  |                                                                   |

## Enable the sub-chart

The `omnibus` chart is disabled out of the box. To make use of it as a developer
you will need to enable it by settings `enabled: true`.

## Configure the image

This section dictates the settings for the container image used by this sub-chart's [Deployment][]. You can change the included version of the [Omnibus Gitlab][og-gitlab] and `pullPolicy`.

Default settings:
- `tag: '10.0.2-ee.0'`
- `pullPolicy: 'IfNotPresent'`

## Configuring Omnibus settings

`external_url` [provides the external hostname and scheme][oq-external-url] to the Omnibus container.

```
external_url: http://gitlab.example.local
```

`trusted_proxies` list will be used to populate [NGINX Real IP][og-nginx-proxy] and [Trusted Proxies][og-trusted-proxy]. Entries should be in quoted CIDR format.

```
trusted_proxies:
- "127.0.0.1/24"
- "10.0.0.0/8"
- "172.16.0.0/12"
- "192.168.0.0/16"
```

## Redis

### Configure Redis

Regardless of using the component, Redis is a requirement of the GitLab stack.
If you use the built-in Redis, the following will default to connect internally.

- `host` contains the hostname of the Redis server.
- `serviceName` contains the name of the service in-chart [Redis service][redis].
- `port` contains the port on the `host` to connect to.
- `password` contains a map of `secret` and `key`. This should contain the secret name, and key name which house the password that will be used for the Redis server.

```
redis:
  enabled: false
  host: '127.0.0.1'
  serviceName: redis
  port: 6397
  # password provided as ENV, via Secret
  password:
    secret: gitlab-redis
    key: redis-password
```
## PostgreSQL

### Configure PostgreSQL

Regardless of using the component, PostgreSQL is a requirement of the GitLab stack.
If you use the built-in PostgreSQL, the following will default to connect internally.

- `database` contains the database name GitLab will use. Default: `gitlabhq_production`
- `username` contains the username for authentication to the server. Default: `gitlab`
- `password` contains a map of `secret` and `key`. This should contain the secret name, and key name which house the password that will be used for the PostgreSQL server.

When using an external PostgreSQL, you will need to provide all of the above.

```
psql:
  database: 'gitlabhq_production'
  username: 'gitlab'
  password:
    secret: gitlab-postgres
    key: psql-password
```

### PostgreSQL Persistence

This chart provisions a PersistentVolumeClaim and mounts corresponding persistent volume for the PostgreSQL data.
You'll need physical storage available in the Kubernetes cluster for this to work. If you'd rather use emptyDir,
disable PersistentVolumeClaim by: `psql.persitence.enabled: false`

```
psql:
  persistence:
    enabled: true
    volumeName: gitlab-psql-data
    storageClass: standard
    accessMode: ReadWriteOnce
    size: 10Gi
    matchLabels: {}
    matchExpressions: []
    subPath: "/data"
```

#### enabled

Sets whether or not to use a PersistentVolumeClaims for the PostgreSQL data. Otherwise a emptyDir volume is used. Defaults to true.

#### volumeName

If set, the chart will use the existing named PersistentVolume. Use this when you are not using dynamic provisioning. Defaults to unset.

#### storageClass

Sets the storageClassName on the Volume Claim for dynamic provisioning. When unset or null, the default provisioner will be used.
If set to a hyphen, dynamic provisioning is disabled. Defaults to unset.
f defined, storageClassName: <storageClass>

#### accessMode

Sets the accessMode requested in the PersistentVolumeClaim. See [Kubernetes Access Modes Documentation][access-modes] for details.
Defaults to ReadWriteOnce

#### size

The minimum volume size to request for the data persistence. Defaults to 10Gi

#### matchLabels

`matchLabels` accepts a dictionary of label name and label values to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

#### matchExpressions

`matchExpressions` accepts an array of label condition objects to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

#### subPath

Sets the path within the volume to mount, rather than the volume root. The root is used if the subPath is empty. Defaults to empty.

[og-docker]: https://gitlab.com/gitlab-org/ominbus-gitlab/container_registry
[helm-gitlab]: https://gitlab.com/charts/helm.gitlab.io
[nginx]: ../../nginx
[registry]: ../../registry
[redis]: ../../redis
[unicorn]: ../unicorn
[sidekiq]: ../sidekiq
[gitlay]: ../gitaly
[gitlab-shell]: ../gitlab-shell
[mattermost]: https://gitlab.com/mattermost
[gl-pages]: https://about.gitlab.com/features/pages/
[og-external-url]: https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab
[og-nginx-proxy]: https://docs.gitlab.com/omnibus/settings/nginx.html#configuring-gitlab-trusted_proxies-and-the-nginx-real_ip-module
[og-trusted-proxy]: https://docs.gitlab.com/omnibus/settings/nginx.html#using-a-non-bundled-web-server
[access-modes]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes

[Service]: ../../../../charts/gitlab/charts/omnibus/templates/service.yaml
[Deployment]: ../../../../charts/gitlab/charts/omnibus/templates/deployment.yaml
[ConfigMap]: ../../../../charts/gitlab/charts/omnibus/templates/registry-configmap.yaml
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
