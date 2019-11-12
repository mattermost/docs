# Using the Redis chart

The `redis` sub-chart provides the Redis key-value store component to a complete cloud-native
GitLab deployment on Kubernetes. This sub-chart makes use of the upstream [Redis](https://hub.docker.com/_/redis/)
container, and is composed of 3 primary parts: [Service](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/redis/templates/service.yaml),
[Deployment](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/redis/templates/deployment.yaml),
and [ConfigMap](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/redis/templates/configmap.yaml).

All configuration is handled according to the official [Redis configuration documentation](https://redis.io/topics/config),
using `/etc/redis/redis.conf` provided to the Deployment, populated from the ConfigMap.
The `ConfigMap` templates [`redis.conf`](http://download.redis.io/redis-stable/redis.conf)
and [Secrets](../../installation/secrets.md#redis-password)
are integrated using an `initContainer` that executes the `configure` script contained
within the `ConfigMap`.

## Design Choices

It [was decided](https://gitlab.com/gitlab-org/charts/gitlab/issues/112) that this chart will
have persistence based on [RDB](https://redis.io/topics/persistence) saved to a
[PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/),
if provided with a [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/volumes/#persistentvolumeclaim).
The use of [AOF](https://redis.io/topics/persistence) is currently a research item
for future development.

We will add the capability to split Redis queues based on class, along with High Availability
features, in the future.

## Configuration

We will describe all the major configuration options below. When configuring from
the parent chart, these values are:

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

If you choose to deploy this chart as a standalone, remove the top level `redis`. Note
that any setting not provided will result in the defaults being used. Thus, it is
not required to provided all values.

## Installation command line options

The table below contains all the possible chart configurations that can be supplied
to the `helm install` command using the `--set` flags:

| Parameter                      | Default         | Description                                 |
| ------------------------------ | --------------- | ------------------------------------------- |
| `enabled`                      | `true`          | Enable flag for the chart                   |
| `image.pullPolicy`             | `IfNotPresent`  | Redis image pull policy                     |
| `image.pullSecrets`            |                 | Secrets for the image repository            |
| `image.repository`             | `redis`         | Redis image repository                      |
| `image.tag`                    | `3.2.5`         | Redis image tag                             |
| `init.image`                   | `busybox`       | initContainer image                         |
| `init.tag`                     | `latest`        | initContainer image tag                     |
| `loglevel`                     | `notice`        | Log verbosity                               |
| `metrics.enabled`              | `true`          | Toggle Prometheus exporter sidecar          |
| `persistence.accessMode`       | `ReadWriteOnce` | Redis access mode                           |
| `persistence.enabled`          | `true`          | Enable persistence flag                     |
| `persistence.matchExpressions` |                 | Label-expression matches to bind            |
| `persistence.matchLabels`      |                 | Label-value matches to bind                 |
| `persistence.size`             | `5Gi`           | Size of volume needed for Redis persistence |
| `persistence.storageClass`     |                 | storageClassName for provisioning           |
| `persistence.subPath`          |                 | Subpath to mount persistence volume at      |
| `persistence.volumeName`       |                 | Existing persistent volume name             |
| `replicas`                     | `1`             | Number of replicas                          |
| `service.clusterIP`            | `0.0.0.0`       | Cluster IP                                  |
| `service.externalPort`         | `6379`          | Redis internal port                         |
| `service.internalPort`         | `6379`          | Redis exposed port                          |
| `service.name`                 | `redis`         | Redis service name                          |
| `service.type`                 | `ClusterIP`     | Redis service type                          |
| `timeout`                      | `60`            | Timeout in seconds                          |
| `tcpKeepalive`                 | `300`           | Keep alive in seconds                       |

## Chart configuration examples

### image.pullSecrets

`pullSecrets` allows you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods can be
found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`:

```yaml
image:
  repository: my.minio.repository
  tag: latest
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

## Enable the sub-chart

They way we've chosen to implement compartmentalized sub-charts includes the ability
to disable the components that you may not want in a given deployment. For this reason,
the first setting you should decide upon is `enabled:`.

By default, Redis is disabled out of the box. Should you wish to enable it, set `enabled: true`.

## Configuring the `image`

This section explains the settings for the container image used by this sub-chart's
[Deployment](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/redis/templates/deployment.yaml).
You can change the included version of Redis and `pullPolicy`.

Default settings:

- `tag: '3.2.5'`
- `pullPolicy: 'IfNotPresent'`

## Configuring the `service`

This section controls the name and type of the [Service](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/redis/templates/service.yaml).
These settings will be populated by the [values.yaml](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/redis/values.yaml).

By default, the Service is configured as:

- `type: ClusterIP` is set to `0.0.0.0`, restricting access to the internal network of the Kubernetes cluster.
- `name:` is set to `redis`.

## Configuring `metrics`

By default, a sidecar container exposing a Prometheus metrics exporter is launched
along with each Redis container. The exporter exposes a `/metrics` endpoint on port
`9121`. When metrics are enabled, annotations are added to the Redis service allowing
a Prometheus server to discover and scrape the exposed metrics.

## Configuring Redis

More details about certain Redis configuration options are explained below:

| Name           | Type    | Default  | Description |
| :------------- | :-----: | :------- | :---------- |
| `loglevel`     | String  | `notice` | [See below](#loglevel). |
| `password`     |         |          | The Redis chart sources credentials from the `global.redis.password` global value. |
| `tcpKeepalive` | Integer | `300`    | Provides the number of seconds to wait for a client connection to be detected as 'dead' by the underlying TCP socket (`SO_KEEPALIVE`). See [Redis tcpkeepalive documentation](https://redis.io/topics/clients#tcp-keepalive). |
| `timeout`      | Integer | `60`     | Provides the number of seconds before an idle client connection will be terminated by the Redis service. See [Redis timeouts documentation](https://redis.io/topics/clients#client-timeouts). |

### loglevel

The `loglevel` value provides the matching configuration item from [`redis.conf`](http://download.redis.io/redis-stable/redis.conf),
allowing the Redis service to specify the verbosity level of logging. This defaults
to `notice`. Valid values are:

- `debug` (a lot of information, useful for development/testing)
- `verbose` (many rarely useful info, but not a mess like the debug level)
- `notice` (moderately verbose, what you want in production probably)
- `warning` (only very important / critical messages are logged)

## persistence

The Redis chart provisions a PersistentVolumeClaim and mounts corresponding persistent
volume for the Redis data. You'll need physical storage available in the Kubernetes
cluster for this to work. If you'd rather use emptyDir, disable PersistentVolumeClaim
with `persistence.enabled: false`.

| Name               | Type    | Default         | Description |
|:------------------ |:-------:|:--------------- |:----------- |
| `accessMode`       | String  | `ReadWriteOnce` | Sets the accessMode requested in the PersistentVolumeClaim. See [Kubernetes Access Modes Documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) for details. |
| `enabled`          | Boolean | `true`          | Sets whether or not to use a PersistentVolumeClaims for the Redis data. Otherwise an emptyDir volume is used. |
| `matchExpressions` | Array   |                 | Accepts an array of label condition objects to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector). |
| `matchLabels`      | Map     |                 | Accepts a dictionary (Map) of label name and label values to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector). |
| `save`             | Array   |                 | [See Below](#save). |
| `size`             | String  | `5Gi`           | The minimum volume size to request for the data persistence. |
| `storageClass`     | String  |                 | Sets the storageClassName on the Volume Claim for dynamic provisioning. When unset or null, the default provisioner will be used. If set to `-` (hyphen), dynamic provisioning is disabled. |
| `subPath`          | String  |                 | Sets the path within the volume to mount, rather than the volume root. The root is used if the subPath is empty. Defaults to empty. |
| `volumeName`       | String  |                 | If set, the chart will use the existing named PersistentVolume. Use this when you are not using dynamic provisioning. |

### save

The `save` array provides for configuration of Redis data snapshotting, as described
in the Redis [persistence](https://redis.io/topics/persistence) documentation. The
items are formatted in a manner to ensure clarity, with the default values taken directly
from the stable [`redis.conf`](http://download.redis.io/redis-stable/redis.conf).

Each item consists of two parts: `time` and `writes`. Each line denotes a point at
which Redis will save the DB if both the given number of seconds and the given number
of write operations against the DB occurred.

It is also possible to entirely disable snapshotting by providing an empty array,
resulting in the value of `save ""` being populated into the [`redis.conf`](http://download.redis.io/redis-stable/redis.conf).
