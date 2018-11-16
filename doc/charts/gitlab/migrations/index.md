# Using the GitLab-Migrations Chart

The `migrations` sub-chart provides a single migration [Job][] that handles seeding/migrating the GitLab database. The chart runs using the gitlab-rails codebase.

After migrating, this Job also edits the application settings in the database to turn off [writes to authorized keys file](https://docs.gitlab.com/ee/administration/operations/fast_ssh_key_lookup.html#setting-up-fast-lookup-via-gitlab-shell). In the charts we are only supporting use of the GitLab Authorized Keys API with the SSH `AuthorizedKeysCommand` instead of support for writing to an authorized keys file.

## Requirements

This chart depends on Redis, and PostgreSQL, either as part of the complete GitLab chart or provided as external services reachable from the Kubernetes cluster this chart is deployed onto.

## Design Choices

The `migrations` is configured to use Helm post-install/post-upgrade hooks in order to create a new migrations [Job][] each time the chart is deployed. In order to prevent job name collisions, we append the chart revision, and a random alpha-numeric value to the Job name each time is created. The purpose of the random text is described further in this section.

For now we also have the jobs remain as objects in the cluster after they complete. This is so we can observe the migration logs. Currently this means these Jobs persist even after a `helm delete`. This is one of the reasons why we append random text to the Job name, so that future deployments using the same release name don't cause conflicts. Once we have some form of log-shipping in place, we can revisit the persistence of these objects.

The container used in this chart has some additional optimizations that we are not currently using in this Chart. Mainly the ability to quickly skip running migrations if they are already up to date, without needing to boot up the rails application to check. This optimization requires us to persist the migration status. Which we are not doing with this chart at the moment. In the future we will introduce storage support for the migrations status to this chart.

# Configuration

The `migrations` chart is configured in two parts: external services, and chart settings.

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter             | Description                                    | Default                                        |
| ---                   | ---                                            | ---                                            |
| image.repository      | Migrations image repository                    | registry.gitlab.com/gitlab-org/build/cng/gitlab-rails-ee |
| image.tag             | Migrations image tag                           |                                                |
| image.pullPolicy      | Migrations pull policy                         | Always                                         |
| image.pullSecrets     | Secrets for the image repository               |                                                |
| init.image            | initContainer image                            | busybox                                        |
| init.tag              | initContainer image tag                        | latest                                         |
| enabled               | Migrations enable flag                         | true                                           |
| redis.serviceName     | Redis service name                             | redis                                          |
| psql.password.secret  | psql secret                                    | gitlab-postgres                                |
| psql.password.key     | key to psql password in psql secret            | psql-password                                  |

## Chart configuration examples
### image.pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image:
  repository: my.migrations.repository
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

## Using the Community Edition of this chart

By default, the Helm charts use the Enterprise Edition of GitLab. If desired, you can instead use the Community Edition. Learn more about the [difference between the two](https://about.gitlab.com/installation/ce-or-ee/).

In order to use the Community Edition, set `image.repository` to `registry.gitlab.com/gitlab-org/build/cng/gitlab-rails-ce`

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

[Job]: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/
