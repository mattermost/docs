# Using the GitLab-Sidekiq chart

The `sidekiq` sub-chart provides configurable deployment of Sidekiq workers, explicitly
designed to provide separation of queues across multiple `Deployment`s with individual
scalability and configuration.

While this chart provides a default `pods:` declaration, if you provide an empty definition,
you will have *no* workers.

## Requirements

This chart depends on access to Redis, PostgreSQL, and Gitaly services, either as
part of the complete GitLab chart or provided as external services reachable from
the Kubernetes cluster this chart is deployed onto.

## Design Choices

This chart creates multiple `Deployment`s and associated `ConfigMap`s. It was decided
that it would be clearer to make use of `ConfigMap` behaviours instead of using `environment`
attributes or additional arguments to the `command` for the containers, in order to
avoid any concerns about command length. This choice results in a large number of
`ConfigMap`s, but provides very clear definitions of what each pod should be doing.

## Configuration

The `sidekiq` chart is configured in three parts: chart-wide [external services](#external-services),
[chart-wide defaults](#chart-wide-defaults), and [per-pod definitions](#per-pod-settings).

## Installation command line options

The table below contains all the possible charts configurations that can be supplied
to the `helm install` command using the `--set` flags:

| Parameter                   | Default           | Description                              |
| --------------------------- | ----------------- | ---------------------------------------- |
| `annotations`               |                   | Pod annotations                          |
| `concurrency`               | `10`              | Sidekiq default concurrency              |
| `enabled`                   | `true`            | Sidekiq enabled flag                     |
| `extraContainers`           |                   | List of extra containers to include      |
| `extraInitContainers`       |                   | List of extra init containers to include |
| `extraVolumeMounts`         |                   | List of extra volumes mountes to do      |
| `extraVolumes`              |                   | List of extra volumes to create          |
| `gitaly.serviceName`        | `gitaly`          | gitaly service name                      |
| `hpa.targetAverageValue`    | `400m`            | Set the autoscaling target value         |
| `image.pullPolicy`          | `Always`          | Sidekiq image pull policy                |
| `image.pullSecrets`         |                   | Secrets for the image repository         |
| `image.repository`          | `registry.gitlab.com/gitlab-org/build/cng/gitlab-sidekiq-ee` | Sidekiq image repository |
| `image.tag`                 |                   | Sidekiq image tag                        |
| `init.image`                | `busybox`         | initContainer image                      |
| `init.tag`                  | `latest`          | initContainer image tag                  |
| `metrics.enabled`           | `true`            | Toggle Prometheus metrics exporter       |
| `psql.password.key`         | `psql-password`   | key to psql password in psql secret      |
| `psql.password.secret`      | `gitlab-postgres` | psql password secret                     |
| `redis.serviceName`         | `redis`           | Redis service name                       |
| `replicas`                  | `1`               | Sidekiq replicas                         |
| `resources.requests.cpu`    | `100m`            | Sidekiq minimum needed cpu               |
| `resources.requests.memory` | `600M`            | Sidekiq minimum needed memory            |
| `timeout`                   | `5`               | Sidekiq job timeout                      |
| `tolerations`               | `[]`              | Toleration labels for pod assignment     |
| `memoryKiller.maxRss`       | `2000000`         | Maximum RSS before delayed shutdown triggered expressed in kilobytes |
| `memoryKiller.graceTime`    | `900`             | Time to wait before a triggered shutdown expressed in seconds|
| `memoryKiller.shutdownWait` | `30`              | Amount of time after triggered shutdown for existing jobs to finish expressed in seconds |

## Chart configuration examples

### image.pullSecrets

`pullSecrets` allows you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods can be
found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`:

```yaml
image:
  repository: my.sidekiq.repository
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

### tolerations

`tolerations` allow you schedule pods on tainted worker nodes

Below is an example use of `tolerations`:

```yaml
tolerations:
- key: "node_label"
  operator: "Equal"
  value: "true"
  effect: "NoSchedule"
- key: "node_label"
  operator: "Equal"
  value: "true"
  effect: "NoExecute"
```

### annotations

`annotations` allows you to add annotations to the sidekiq pods.

Below is an example use of `annotations`:

```yaml
annotations:
  kubernetes.io/example-annotation: annotation-value
```

## Using the Community Edition of this chart

By default, the Helm charts use the Enterprise Edition of GitLab. If desired, you
can use the Community Edition instead. Learn more about the
[differences between the two](https://about.gitlab.com/install/ce-or-ee/).

In order to use the Community Edition, set `image.repository` to
`registry.gitlab.com/gitlab-org/build/cng/gitlab-sidekiq-ce`.

## External Services

This chart should be attached to the same Redis, PostgreSQL, and Gitaly instances
as the Unicorn chart. The values of external services will be populated into a `ConfigMap`
that is shared across all Sidekiq pods.

### Redis

```yaml
redis:
  host: rank-racoon-redis
  port: 6379
  sentinels:
    - host: sentinel1.example.com
      port: 26379
  password:
    secret: gitlab-redis
    key: redis-password
```

| Name               | Type    | Default | Description |
|:------------------ |:-------:|:------- |:----------- |
| `host`             | String  |         | The hostname of the Redis server with the database to use. This can be omitted in lieu of `serviceName`. If using Redis Sentinels, the `host` attribute needs to be set to the cluster name as specified in the `sentinel.conf`. |
| `password.key`     | String  |         | The `password.key` attribute for Redis defines the name of the key in the secret (below) that contains the password. |
| `password.secret`  | String  |         | The `password.secret` attribute for Redis defines the name of the Kubernetes `Secret` to pull from. |
| `port`             | Integer | `6379`  | The port on which to connect to the Redis server. |
| `serviceName`      | String  | `redis` | The name of the `service` which is operating the Redis database. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Redis as a part of the overall GitLab chart. |
| `sentinels.[].host`| String  |         | The hostname of Redis Sentinel server for a Redis HA setup. |
| `sentinels.[].port`| Integer | `26379` | The port on which to connect to the Redis Sentinel server. |

_Note:_ The current Redis Sentinel support only supports Sentinels that have
been deployed separately from the GitLab chart. As a result, the Redis
deployment through the GitLab chart should be disabled with `redis.enabled=false`
and `redis-ha.enabled=false`. The Secret containing the Redis password
will need to be manually created before deploying the GitLab chart.

### PostgreSQL

```yaml
psql:
  host: rank-racoon-psql
  serviceName: pgbouncer
  port: 5432
  database: gitlabhq_production
  username: gitlab
  preparedStatements: false
  password:
    secret: gitlab-postgres
    key: psql-password
```

| Name              | Type    | Default               | Description |
|:----------------  |:-------:|:--------------------- |:----------- |
| `host`            | String  |                       | The hostname of the PostgreSQL server with the database to use. This can be omitted if `postgresql.install=true` (default non-production). |
| `serviceName`     | String  |                       | The name of the `service` which is operating the PostgreSQL database. If this is present, and `host` is not, the chart will template the hostname of the service in place of the `host` value. |
| `database`        | String  | `gitlabhq_production` | The name of the database to use on the PostgreSQL server. |
| `password.key`    | String  |                       | The `password.key` attribute for PostgreSQL defines the name of the key in the secret (below) that contains the password. |
| `password.secret` | String  |                       | The `password.secret` attribute for PostgreSQL defines the name of the Kubernetes `Secret` to pull from. |
| `port`            | Integer | `5432`                | The port on which to connect to the PostgreSQL server. |
| `username`        | String  | `gitlab`              | The username with which to authenticate to the database. |
| `preparedStatements`| Bool  | `false`               | If prepared statements should be used when communicating with the PostgreSQL server. |

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

| Name               | Type    | Default  | Description |
|:-----------------  |:-------:|:-------- |:----------- |
| `host`             | String  |          | The hostname of the Gitaly server to use. This can be omitted in lieu of `serviceName`. |
| `serviceName`      | String  | `gitaly` | The name of the `service` which is operating the Gitaly server. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Gitaly as a part of the overall GitLab chart. |
| `port`             | Integer | `8075`   | The port on which to connect to the Gitaly server. |
| `authToken.key`    | String  |          | The name of the key in the secret below that contains the authToken. |
| `authToken.secret` | String  |          | The name of the Kubernetes `Secret` to pull from. |

## Metrics

By default, a Prometheus metrics exporter is enabled per pod. Metrics are only available
when [GitLab Prometheus metrics](https://docs.gitlab.com/ee/administration/monitoring/prometheus/gitlab_metrics.html)
are enabled in the Admin area. The exporter exposes a `/metrics` endpoint on port
`3807`. When metrics are enabled, annotations are added to each pod allowing a Prometheus
server to discover and scrape the exposed metrics.

## Chart-wide defaults

The following values will be used chart-wide, in the event that a value is not presented
on a per-pod basis.

| Name          | Type    | Default | Description |
|:------------- |:-------:|:------- |:----------- |
| `concurrency` | Integer | `25`    | The number of tasks to process simultaneously. |
| `replicas`    | Integer | `1`     | The number of `replicas` to use by default per pod definition. |
| `timeout`     | Integer | `4`     | The sidekiq shutdown timeout. The number of seconds after sidekiq gets the TERM signal before it forcefully shuts down its processes. |
| `memoryKiller.maxRss`       | Integer | `2000000`         | Maximum RSS before delayed shutdown triggered expressed in kilobytes |
| `memoryKiller.graceTime`    | Integer | `900`             | Time to wait before a triggered shutdown expressed in seconds|
| `memoryKiller.shutdownWait` | Integer | `30`              | Amount of time after triggered shutdown for existing jobs to finish expressed in seconds |

NOTE: **Note**: [Detailed documentation of the sidekiq memory killer is
  available](https://docs.gitlab.com/ee/administration/operations/sidekiq_memory_killer.html#sidekiq-memorykiller)
  in the Omnibus documentation.

## Per-pod Settings

The `pods` declaration provides for the declaration of all attributes for a worker
pod. These will be templated to `Deployment`s, with individual `ConfigMap`s for their
Sidekiq instances.

NOTE: **Note**: The settings default to including a single pod that is set up to monitor
  all queues. Making changes to to the pods section will *overwrite the default pod* with
  a different pod configuration. It will not add a new pod in addition to the default.

| Name           | Type    | Default | Description |
|:-------------- |:-------:|:------- |:----------- |
| `concurrency`  | Integer |         | The number of tasks to process simultaneously. If not provided, it will be pulled from the chart-wide default. |
| `name`         | String  |         | Used to name the `Deployment` and `ConfigMap` for this pod. It should be kept short, and should not be duplicated between any two entries. |
| `queues`       |         |         | [See below](#queues). |
| `replicas`     | Integer |         | The number of `replicas` to create for this `Deployment`. If not provided, it will be pulled from the chart-wide default. |
| `timeout`      | Integer |         | The sidekiq shutdown timeout. The number of seconds after sidekiq gets the TERM signal before it forcefully shuts down its processes. If not provided, it will be pulled from the chart-wide default. |
| `resources`    |         |         | Each pod can present it's own `resources` requirements, which will be added to the `Deployment` created for it, if present. These match the Kubernetes documentation. |
| `nodeSelector` |         |         | Each pod can be configured with a `nodeSelector` attribute, which will be added to the `Deployment` created for it, if present. These definitions match the Kubernetes documentation.|

### queues

The `queues` value will be directly templated into the Sidekiq configuration file.
As such, you may follow the documentation from Sidekiq for the value of `:queues:`.
If this is not provided, the [upstream defaults](https://gitlab.com/gitlab-org/gitlab/blob/master/config/sidekiq_queues.yml)
will be used, resulting in the handling of *all* queues.

In summary, provide a list of queue names to process. Each item in the list may be
a queue name (`merge`) or an array of queue names with priorities (`[merge, 5]`).

Any queue to which jobs are added but are not represented as a part of at least one
pod item *will not be processed*. See [`config/sidekiq_queues.yml`](https://gitlab.com/gitlab-org/gitlab/blob/master/config/sidekiq_queues.yml)
in the GitLab source for a complete list of all queues.

### Example `pod` entry

```YAML
pods:
  - name: immediate
    concurrency: 10
    replicas: 3
    - [post_receive, 5]
    - [merge, 5]
    - [update_merge_requests, 3]
    - [process_commit, 3]
    - [new_note, 2]
    - [new_issue, 2]
    resources:
      limits:
        cpu: 800m
        memory: 2Gi
```

## Production usage

By default, all of sidekiq queues run in an all-in-one container which is not suitable
for production use cases. Check the [example config](./example-queues.yaml) for a more production ready sidekiq
deployment. You can move queues around pods as part of your tuning.
