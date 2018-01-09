# Using the Redis chart

The `redis` sub-chart provides the Redis key-value store component to a complete cloud-native GitLab deployment on Kubernetes. This sub-chart makes use of the upstream [redis][] container This chart is composed of 3 primary parts: [Service][], [Deployment][], and [ConfigMap][].

All configuration is handled according to the official [Redis configuration documentation][redis-config-docs] using `/etc/redis/redis.conf` provided to the [Deployment][], populated from the [ConfigMap][]. The `ConfigMap` templates [redis.conf][] and [Secret][]s are integrated using an `initContainer` that executes the `configure` script contained within the `ConfigMap`.

## Design Choices

At this time, this chart provides the capability of persistence via a [persistentVolumeClaim][], and when not provided will default to a [emptyDir][] to ensure persistence across the lifespan of the `Pod`.

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
  password:
    secret: gitlab-redis
    key: redis-password
  persistence
    disk:
      persistentVolumeClaim:
    save:
    - time: 60
      writes: 1000
    - time: 300
      writes: 10
    - time: 900
      writes: 1
```

If you should chose to deploy this chart as a standalone, remove the top level `redis`. Not that any setting not provided will result in the defaults being used. Thus, it is not required to provided all values.

See [values.yaml][] for all available options.

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

This chart relies on one [Secret][kubernetes-secret], `password`.
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the password that will be required to access the Redis service

### persistence

#### disk.persistentVolumeClaim

If an administrator provides a [PersistentVolumeClaim][] name, the chart will make use of that external [PersistentVolume][] and data will survive the `Pod`. If an administrator does not provide the [PersistentVolumeClaim][] name, the chart will fall back to creating an [emptyDir][] volume limited to `10` gigabytes. This volume will live as long as the `Pod` that created it exists, and provides for persistence across `Pod` restarts and any unforseen incidents a the contaier level, so long as that pod remains on the same node.

[Investigation][issue-112] showed that a standard disk (e.g. `pd-standard` on GKE) is sufficient for the throughput needs of a properly configured Redis pod. The size of the disk should be at leat the requested memory of the Redis instance. For example, if providing a `maxmemory` of `1gb`, the [PersistentVolume][] should be a minimum of that `1gb`.

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

[issue-112]:https://gitlab.com/charts/helm.gitlab.io/issues/112
