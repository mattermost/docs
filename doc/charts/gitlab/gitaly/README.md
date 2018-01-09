# Using the GitLab-Gitaly chart

The `gitaly` sub-chart provides a configurable deployment of Gitaly Servers.

## Requirements

This chart depends on access to Redis and Unicorn services, either as part of the complete GitLab chart or provided as external services reachable from the Kubernetes cluster this chart is deployed onto.

## Design Choices

The Gitlay container used in this chart also contains the gitlab-shell code-base in order to perform the actions on the Git repos that have not yet been ported into Gitaly. The Gitaly container includes a copy of the gitlab-shell container within it, and as a result we also need to configure gitlab-shell within this chart.

# Configuration

The `gitaly` chart is configured in two parts: external services, and chart settings.

## External Services

This chart should be attached the Unicorn service, and should also use the same Redis as the attached Unicorn service.

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

### Unicorn

```YAML
unicorn:
  host: rank-racoon-unicorn
  serviceName: 'unicorn'
  port: 8080
```

#### host

The hostname of the Unicorn server. This can be omitted in lieu of `serviceName`

#### serviceName

The name of the `service` which is operating the Unicorn server. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Unicorn as a part of the overall GitLab chart. This will default to `unicorn`

#### port

The port on which to connect to the Unicorn server. Defaults to `8080`.

## Chart Settings

The following values are used to configure the Gitaly Pods.

#### authToken

Gitaly uses an Auth Token to authenticate with the Unicorn and Sidekiq services. Share the token with Gitaly, Unicorn, and Sidekiq using a shared Secret.

```YAML
authToken:
  secret: gitaly-secret
  key: token
```

The `authToken` attribute has two sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the authToken.

## GitLab Shell

Gitaly container has a copy of GitLab Shell, which has some configuration that can be set.

#### shell.authToken

GitLab Shell uses an Auth Token in its communication with Unicorn. Share the token with GitLab Shell and Unicorn using a shared Secret.

```YAML
shell:
  authToken:
   secret: gitlab-shell-secret
   key: secret
```

The `authToken` attribute has two sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the authToken.
