# Using the GitLab-Unicorn Chart

The `unicorn` sub-chart provides the gitlab rails web-server running two unicorn workers per pod. (The minimum necessary for a single pod to be able to serve any web request in GitLab)

Currently the container used in the chart also includes a copy of gitlab-workhorse, which we haven't yet split out.

## Requirements

This chart depends on Redis, PostgreSQL, Gitaly, and Registry services, either as part of the complete GitLab chart or provided as external services reachable from the Kubernetes cluster this chart is deployed onto.

# Configuration

The `unicorn` chart is configured in two parts: chart-wide external services, and chart-wide defaults.

## External Services

### Redis

```YAML
redis:
  host: rank-racoon-redis
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

The `password` atribute for Redis has to sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the password.

### PostgreSQL

```YAML
psql:
  host: rank-racoon-psql
  serviceName: omnibus
  port: 5432
  database: gitlabhq_production
  username: gitlab
  password: nil
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

The password with which to authenticate to the database. (This will be moved to a secret in the future)

### Gitaly

```YAML
gitaly:
  host: 'rank-racoon-gitaly'
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

### Registry

```YAML
registry:
  host: rank-racoon-registry
  port: 443
  api:
    protocol: http
    serviceName: registry
    port: 5000
  tokenIssuer: gitlab-issuer
  certificate:
    secret: gitlab-registry
    key: gitlab-registry.key
```
