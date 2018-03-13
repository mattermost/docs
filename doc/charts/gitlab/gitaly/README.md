# Using the GitLab-Gitaly chart

The `gitaly` sub-chart provides a configurable deployment of Gitaly Servers.

## Requirements

This chart depends on access to Redis and Unicorn services, either as part of the complete GitLab chart or provided as external services reachable from the Kubernetes cluster this chart is deployed onto.

## Design Choices

The Gitlay container used in this chart also contains the gitlab-shell code-base in order to perform the actions on the Git repos that have not yet been ported into Gitaly. The Gitaly container includes a copy of the gitlab-shell container within it, and as a result we also need to configure gitlab-shell within this chart.

# Configuration

The `gitaly` chart is configured in two parts: external services, and chart settings.

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter              | Description                            | Default                                  |
| ---                    | ---                                    | ---                                      |
| replicaCount           | Gitaly replicas                        | 1                                        |
| image.repository       | Gitaly image repository                | registry.com/gitlab-org/build/cng/gitaly |
| image.tag              | Gitaly image tag                       | latest                                   |
| image.pullPolicy       | Gitaly image pull policy               | Always                                   |
| service.name           | Gitaly service name                    | gitaly                                   |
| service.type           | Gitaly service type                    | ClusterIP                                |
| service.externalPort   | Gitaly service exposed port            | 8075                                     |
| service.internalPort   | Gitaly internal port                   | 8075                                     |
| enabled                | Gitaly enable flag                     | true                                     |
| serviceName            | Gitaly service name                    | gitaly                                   |
| authToken.secret       | Gitaly secret name                     | gitaly-secret                            |
| authToken.key          | Key to gitaly token in the secret      | token                                    |
| redis.password.secret  | Redis secret containing redis password | gitlab-redis                             |
| redis.password.key     | Key to redis password in redis secret  | redis-password                           |
| shell.authToken.secret | Shell secret                           | gitlab-shell-secret                      |
| shell.authToken.key    | Shell key                              | secret                                   |
| persistence.enabled    | Gitaly enable persistence flag         | true                                     |
| persistence.accessMode | Gitaly persistence access mode         | ReadWriteOnce                            |
| persistence.size       | Gitaly persistence volume size         | 50Gi                                     |
| persistence.subPath    | Gitaly persistence volume mount path   |                                          |

## External Services

This chart should be attached the Unicorn service, and should also use the same Redis as the attached Unicorn service.

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

The `password` atribute for Redis has to sub keys:
- `secret` defines the name of the kubernetes `Secret` to pull from
- `key` defines the name of the key in the above secret that contains the password.

### Unicorn

```YAML
unicorn:
  host: unicorn.example.local
  serviceName: unicorn
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

### Git Repository Persistence

This chart provisions a PersistentVolumeClaim and mounts a corresponding persistent volume for the Git repository data.
You'll need physical storage available in the Kubernetes cluster for this to work. If you'd rather use emptyDir,
disable PersistentVolumeClaim by: `persitence.enabled: false`

```
persistence:
  enabled: true
  volumeName: gitlab-repo-data
  storageClass: standard
  accessMode: ReadWriteOnce
  size: 50Gi
  subPath: "/data"
```

#### enabled

Sets whether or not to use a PersistentVolumeClaims for the repo data. Otherwise a emptyDir volume is used. Defaults to true.

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

The minimum volume size to request for the data persistence. Defaults to 50Gi

#### subPath

Sets the path within the volume to mount, rather than the volume root. The root is used if the subPath is empty. Defaults to empty.

[access-modes]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes
