# Using the GitLab-Sidekiq chart

The `sidekiq` sub-chart provides configurable deployment of Sidekiq workers, explicitly designed to provide separation of queues across multiple `Deployment`s with individual scalability and configuration.

While this chart provides a default `pods:` declaration, if you provide an empty definition, you will have _no_ workers.

## Requirements

This chart depends on access to Redis, PostgreSQL, and Gitaly services, either as part of the complete GitLab chart or provided as external services reachable from the Kubernetes cluster this chart is deployed onto.

## Design Choices

This chart creates multiple `Deployment`s and associated `ConfigMap`s. It was decided that it would be clearer to make use of `ConfigMap` behaviours over using `environment` attributes or additional arguments to the `command` for the containers in order to avoid any concerns about command length. This choice results in a large number of `ConfigMap`s, but provides a very clear definition of what each pod should be doing.

# Configuration

The `sidekiq` chart is configured in three parts: chart-wide external services, chart-wide defaults, and per-pod definitions.

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                 | Description                                    | Default                                          |
| ---                       | ---                                            | ---                                              |
| image.repository          | Sidekiq image repository                       | registry.gitlab.com/gitlab-org/build/cng/gitlab-sidekiq-ee |
| image.tag                 | Sidekiq image tag                              |                                                  |
| image.pullPolicy          | Sidekiq image pull policy                      | Always                                           |
| image.pullSecrets         | Secrets for the image repository               |                                                  |
| init.image                | initContainer image                            | busybox                                          |
| init.tag                  | initContainer image tag                        | latest                                           |
| enabled                   | Sidekiq enabled flag                           | true                                             |
| metrics.enabled           | Toggle Prometheus metrics exporter             | true                                             |
| redis.serviceName         | Redis service name                             | redis                                            |
| psql.password.secret      | psql password secret                           | gitlab-postgres                                  |
| psql.password.key         | key to psql password in psql secret            | psql-password                                    |
| gitaly.serviceName        | gitaly service name                            | gitaly                                           |
| cron_jobs                 | Auxiliary cron jobs                            | {}                                               |
| replicas                  | Sidekiq replicas                               | 1                                                |
| concurrency               | Sidekiq default concurrency                    | 10                                               |
| hpa.targetAverageValue    | Set the autoscaling target value               | 400m                                             |
| timeout                   | Sidekiq job timeout                            | 5                                                |
| resources.requests.cpu    | Sidekiq minimum needed cpu                     | 100m                                             |
| resources.requests.memory | Sidekiq minimum needed memory                  | 600M                                             |

## Chart configuration examples
### image.pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image:
  repository: my.sidekiq.repository
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

## Using the Community Edition of this chart

By default, the Helm charts use the Enterprise Edition of GitLab. If desired, you can instead use the Community Edition. Learn more about the [difference between the two](https://about.gitlab.com/installation/ce-or-ee/).

In order to use the Community Edition, set `image.repository` to `registry.gitlab.com/gitlab-org/build/cng/gitlab-sidekiq-ce`

## External Services

This chart should be attached to the same Redis, PostgreSQL, and Gitaly instances as the Unicorn chart. The values of external services will be populated into a `ConfigMap` that is shared across all Sidekiq pods.

### Redis

```YAML
redis:
  host: rank-racoon-redis
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
  host: rank-racoon-psql
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

## Metrics

By default, a Prometheus metrics exporter is enabled per pod. Metrics are only available when [GitLab Prometheus metrics](https://docs.gitlab.com/ee/administration/monitoring/prometheus/gitlab_metrics.html) are enabled in the Admin area. The exporter exposes a `/metrics` endpoint on port `3807`. When metrics are enabled, annotations are added to each pod allowing a Prometheus server to discover and scrape the exposed metrics.

## Chart-wide defaults

The following values will be used chart-wide, in the event that a value is not presented on a per-pod basis.

#### replicas

The number of `replicas` to use by default per pod definition. The default value is `1`.

#### timeout

The number of seconds _____ . This default value is `4`.

#### concurrency

The number of tasks to process simultaneously. The default value is `25`.

#### cron_jobs

Sidekiq includes maintenance jobs that can be configured to run on a periodic basis using cron style schedules. A few examples are included below. See the sample [gitlab.yml](https://gitlab.com/gitlab-org/gitlab-ee/blob/master/config/gitlab.yml.example#L237-302) for more job examples.

Cron jobs are configured globally for all Sidekiq pods. There are no per-pod settings.

```YAML
cron_jobs:
  stuck_ci_jobs_worker:
    cron: "0 * * * *"
  pipeline_schedule_worker:
    cron: "19 * * * *"
  expire_build_artifacts_worker:
    cron: "50 * * * *"
```

## Per-pod Settings `pods`

The `pods` declaration provides declaration of all attributes for a worker pod. These will be templated to `Deployment`s, with individual `ConfigMap`s for their Sidekiq instances.

You must provide no definitions, relying on the defaults, or provide at least one entry. If you do not, you will have _no_ workers.

#### name

The `name` attribute is used to name the `Deployment` and `ConfigMap` for this pod. It should be kept to short, and should not be duplicated between any two entries.

#### replicas

The number of `replicas` to create for this `Deployment`. If not provided, this will pull from the chart-wide default.

#### timeout

The number of seconds _____ . If not provided, this will pull from the chart-wide default.

#### concurrency

The number of tasks to process simultaneously. If not provided, this will pull from the cahrt-wide default.

#### queues

The `queues` value will be directly templated into the Sidekiq configuration file. As such, you may follow the documentation from Sidekiq for the value of `:queues:`. If this is not provided, the [upstream defaults](https://gitlab.com/gitlab-org/gitlab-ee/blob/master/config/sidekiq_queues.yml) will be used, resulting in the handling of _all_ queues.

In summary, provide an list of queue names to process. Each item in the list may be a queue name (`merge`) or an array of queue name and priority (`[merge, 5]`).

Any queue to which jobs are added but are not represented as a part of at least one pod item _will not b processed_. See [GitLab source for `config/sidekiq_queues.yml`]() for a complete list of all queues.

#### resources

Each pod can present it's own `resources` requirements, which will be added to the `Deployment` created for it, if present. There is no chart-wide default.

These match the kubernetes documentation.

#### nodeSelector

Each pod can be configured with a `nodeSelector` attribute, which will be added to the `Deployment` created for it, if present. There is no chart-wide default.

These definitions match the kubernetes documentation.

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


### Production usage

By default all of sidekiq queues run in an all-in-one container which is not suitable for production use cases.

Check the [example config](./example-queues.yaml) for a more production ready sidekiq deployment. You can move queues around pods as a part of your tuning.
