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

| Parameter                    | Description                            | Default                                  |
| ---                          | ---                                    | ---                                      |
| image.repository             | Gitaly image repository                | registry.com/gitlab-org/build/cng/gitaly |
| internal.names[]             | Ordered names of statfulset storages   | - default                                |
| external[].name              | name of external node storage          | - ""                                     |
| external[].hostname          | hostname of external node              | - ""                                     |
| external[].port              | port of external node                  | - ""                                     |
| image.tag                    | Gitaly image tag                       | latest                                   |
| image.pullPolicy             | Gitaly image pull policy               | Always                                   |
| image.pullSecrets            | Secrets for the image repository       |                                          |
| init.image                   | initContainer image                    | busybox                                  |
| init.tag                     | initContainer image tag                | latest                                   |
| service.name                 | Gitaly service name                    | gitaly                                   |
| service.type                 | Gitaly service type                    | ClusterIP                                |
| service.externalPort         | Gitaly service exposed port            | 8075                                     |
| service.internalPort         | Gitaly internal port                   | 8075                                     |
| enabled                      | Gitaly enable flag                     | true                                     |
| serviceName                  | Gitaly service name                    | gitaly                                   |
| persistence.enabled          | Gitaly enable persistence flag         | true                                     |
| persistence.accessMode       | Gitaly persistence access mode         | ReadWriteOnce                            |
| persistence.size             | Gitaly persistence volume size         | 50Gi                                     |
| persistence.subPath          | Gitaly persistence volume mount path   |                                          |
| persistence.storageClass     | storageClassName for provisioning      |                                          |
| persistence.matchLabels      | Label-value matches to bind            |                                          |
| persistence.matchExpressions | Label-expression matches to bind       |                                          |

## Chart configuration examples
### image.pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image:
  repository: my.gitaly.repository
  tag: latest
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

## External Services

This chart should be attached the Unicorn service, and should also use the same Redis as the attached Unicorn service.

### Redis

```YAML
redis:
  host: redis.example.com
  serviceName: redis
  port: 6379
```

#### host

The hostname of the Redis server with the database to use. This can be omitted in lieu of `serviceName`

#### serviceName

The name of the `service` which is operating the Redis database. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Redis as a part of the overall GitLab chart. This will default to `redis`

#### port

The port on which to connect to the Redis server. Defaults to `6379`.

#### credentials

Credentials will be sourced from `global.redis.password` values.

### Unicorn

```YAML
unicorn:
  host: unicorn.example.com
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

Gitaly uses an Auth Token to authenticate with the Unicorn and Sidekiq services. Auth Token secret and key are sourced from the `global.gitaly.authToken` value.

## GitLab Shell

Gitaly container has a copy of GitLab Shell, which has some configuration that can be set.

#### shell.authToken

Shell authToken is sourced from `global.shell.authToken` values.

### Git Repository Persistence

This chart provisions a PersistentVolumeClaim and mounts a corresponding persistent volume for the Git repository data.
You'll need physical storage available in the Kubernetes cluster for this to work. If you'd rather use emptyDir,
disable PersistentVolumeClaim by: `persitence.enabled: false`

> **Note:** The persistence settings for gitaly are used in a volumeClaimTemplate, that should be valid for all your
> gitaly pods. You should *not* include settings that are meant to reference a single specific volume (ie volumeName).
> If you want to reference a specific volume, you need to manually create the PersistentVolumeClaim.

```
persistence:
  enabled: true
  storageClass: standard
  accessMode: ReadWriteOnce
  size: 50Gi
  matchLabels: {}
  matchExpressions: []
  subPath: "/data"
```

#### enabled

Sets whether or not to use a PersistentVolumeClaims for the repo data. Otherwise a emptyDir volume is used. Defaults to true.

#### storageClass

Sets the storageClassName on the Volume Claim for dynamic provisioning. When unset or null, the default provisioner will be used.
If set to a hyphen, dynamic provisioning is disabled. Defaults to unset.

#### accessMode

Sets the accessMode requested in the PersistentVolumeClaim. See [Kubernetes Access Modes Documentation][access-modes] for details.
Defaults to ReadWriteOnce

#### size

The minimum volume size to request for the data persistence. Defaults to 50Gi

#### matchLabels

`matchLabels` accepts a dictionary of label name and label values to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

#### matchExpressions

`matchExpressions` accepts an array of label condition objects to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

#### subPath

Sets the path within the volume to mount, rather than the volume root. The root is used if the subPath is empty. Defaults to empty.

[access-modes]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes
