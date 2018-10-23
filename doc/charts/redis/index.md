# Using the Redis chart

The `redis` sub-chart provides the Redis key-value store component to a complete cloud-native GitLab deployment on Kubernetes. This sub-chart makes use of the upstream [redis][] container This chart is composed of 3 primary parts: [Service][], [Deployment][], and [ConfigMap][].

All configuration is handled according to the official [Redis configuration documentation][redis-config-docs] using `/etc/redis/redis.conf` provided to the [Deployment][], populated from the [ConfigMap][]. The `ConfigMap` templates [redis.conf][] and [Secret][]s are integrated using an `initContainer` that executes the `configure` script contained within the `ConfigMap`.

## Design Choices

It [was decided][issue-112] that this chart will have persistence based on [RDB][persistence] saved to a [PersistentVolume][], if provided with a [PersistentVolumeClaim][]. The use of [AOF][persistence] has been deemed a research item for future development.

We will add the capability to split Redis queues based on class, along with High Availability features in the future.

# Configuration

We will describe all the major sections of the configuration below. When configuring from the parent chart, these values will be as such:

```
redis:
  enabled: false
  image:
    tag: 3.2.5
    pullPolicy: IfNotPresent
  timeout: 60
  tcpKeepalive: 30
  loglevel: "notice"
  persistence:
    enabled: true
    volumeName: gitlab-redis-data
    storageClass: standard
    accessMode: ReadWriteOnce
    size: 5Gi
    matchLabels: {}
    matchExpressions: []
    subPath: "/data"
    save:
    - time: 60
      writes: 1000
    - time: 300
      writes: 10
    - time: 900
      writes: 1
```

If you should chose to deploy this chart as a standalone, remove the top level `redis`. Not that any setting not provided will result in the defaults being used. Thus, it is not required to provided all values.

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                    | Description                                 | Default        |
| ---                          | ---                                         | ---            |
| image.repository             | Redis image repository                      | redis          |
| image.tag                    | Redis image tag                             | 3.2.5          |
| image.pullPolicy             | Redis image pull policy                     | IfNotPresent   |
| image.pullSecrets            | Secrets for the image repository            |                |
| init.image                   | initContainer image                         | busybox        |
| init.tag                     | initContainer image tag                     | latest         |
| service.name                 | Redis service name                          | redis          |
| service.type                 | Redis service type                          | ClusterIP      |
| service.externalPort         | Redis internal port                         | 6379           |
| service.internalPort         | Redis exposed port                          | 6379           |
| service.clusterIP            | Cluster IP                                  | 0.0.0.0        |
| replicas                     | Number of replicas                          | 1              |
| enabled                      | Enable flag for the chart                   | true           |
| timeout                      | Timeout in seconds                          | 60             |
| tcpKeepalive                 | Keep alive in seconds                       | 300            |
| loglevel                     | Log verbosity                               | notice         |
| metrics.enabled              | Toggle Prometheus exporter sidecar          | true           |
| persistence.enabled          | Enable persistence flag                     | true           |
| persistence.accessMode       | Redis access mode                           | ReadWriteOnce  |
| persistence.size             | Size of volume needed for redis persistence | 5Gi            |
| persistence.subPath          | Subpath to mount persistence volume at      |                |
| persistence.storageClass     | storageClassName for provisioning           |                |
| persistence.volumeName       | Existing persistent volume name             |                |
| persistence.matchLabels      | Label-value matches to bind                 |                |
| persistence.matchExpressions | Label-expression matches to bind            |                |

## Chart configuration examples
### image.pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image:
  repository: my.minio.repository
  tag: latest
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

## Enable the sub-chart

They way we've chosen to implement compartmentalized sub-charts includes the ability to disable the components that you may not want in a given deployment. For this reason, the first settings you should decided upon is `enabled:`.

By default, Redis is disabled out of the box. Should you wish to enable it, set `enabled: true`.

## Configuring the `image`

This section dictates the settings for the container image used by this sub-chart's [Deployment][]. You can change the included version of Redis and `pullPolicy`.

Default settings:
- `tag: '3.2.5'`
- `pullPolicy: 'IfNotPresent'`

## Configuring the `service`

This section controls the name and type of the [Service][]. These settings will
be populated by the [values.yml][].

By default, the [Service][] is configured as:
- `type: ClusterIP` on `0.0.0.0`, restricting access to the interal network of the Kubernetes cluster.
- `name:` is set to `redis`.

## Configuring `metrics`

By default, a sidecar container exposing a Prometheus metrics exporter is launched along with each Redis container. The exporter exposes a `/metrics` endpoint on port `9121`. When metrics are enabled, annotations are added to the Redis service allowing a Prometheus server to discover and scrape the exposed metrics.

## Configuring Redis

### timeout

The `timeout` value provides the number of seconds before an idle client connection will be terminated by the Redis service. See https://redis.io/topics/clients#client-timeouts for further details.

### tcpKeepalive

The `tcpKeepalive` value provides the number of seconds to wait for a client connection to be detected as 'dead' by the underlying TCP socket (`SO_KEEPALIVE`). See https://redis.io/topics/clients#tcp-keepalive for further details.

### loglevel

The `loglevel` value provides the matching configuration item from [redis.conf][], allowing to to specify the verbosity level of logging from the Redis service. This defaults to `notice`. Valid values are:
- `debug` (a lot of information, useful for development/testing)
- `verbose` (many rarely useful info, but not a mess like the debug level)
- `notice` (moderately verbose, what you want in production probably)
- `warning` (only very important / critical messages are logged)

### password

This chart sources credentials from `global.redis.password` global value.

### persistence

This chart provisions a PersistentVolumeClaim and mounts corresponding persistent volume for the Redis data.
You'll need physical storage available in the Kubernetes cluster for this to work. If you'd rather use emptyDir,
disable PersistentVolumeClaim by: `persitence.enabled: false`

#### enabled

Sets whether or not to use a PersistentVolumeClaims for the Redis data. Otherwise a emptyDir volume is used. Defaults to true.

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

The minimum volume size to request for the data persistence. Defaults to 5Gi

#### subPath

Sets the path within the volume to mount, rather than the volume root. The root is used if the subPath is empty. Defaults to empty.

#### matchLabels

`matchLabels` accepts a dictionary of label name and label values to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

#### matchExpressions

`matchExpressions` accepts an array of label condition objects to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

#### save

The `save` array provides for configuration of Redis data snapshotting, as described in the Redis [persistence][] documentation. The items are formatted in a manner to ensure clarity, with the default values taken directly from the stable [redis.conf][].

Each item consists of two parts: `time` and `writes`. Each line denotes a point at which Redis will save the DB if both the given number of seconds and the given number of write operations against the DB occurred.

It is also possible to entirely disable snapshotting by providing an empty array, resulting in the value of `save ""` being populated into the [redis.conf][].

[redis]: https://hub.docker.com/_/redis/
[redis.conf]: http://download.redis.io/redis-stable/redis.conf
[redis-config-docs]: https://redis.io/topics/config

[Service]: ../../../charts/redis/templates/service.yaml
[Deployment]: ../../../charts/redis/templates/deployment.yaml
[ConfigMap]: ../../../charts/redis/templates/configmap.yaml
[values.yaml]: ../../../charts/redis/values.yaml

[PersistentVolume]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
[PersistentVolumeClaim]: https://kubernetes.io/docs/concepts/storage/volumes/#persistentvolumeclaim
[emptyDir]: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir

[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[persistence]: https://redis.io/topics/persistence
[access-modes]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes

[issue-112]:https://gitlab.com/charts/gitlab/issues/112
