# Using the GitLab-Gitaly chart

The `gitaly` sub-chart provides a configurable deployment of Gitaly Servers.

## Requirements

This chart depends on access to Redis and Unicorn services, either as part of the
complete GitLab chart or provided as external services reachable from the Kubernetes
cluster this chart is deployed onto.

## Design Choices

The Gitaly container used in this chart also contains the GitLab Shell codebase in
order to perform the actions on the Git repos that have not yet been ported into Gitaly.
The Gitaly container includes a copy of the GitLab Shell container within it, and
as a result we also need to configure GitLab Shell within this chart.

## Configuration

The `gitaly` chart is configured in two parts: [external services](#external-services),
and [chart settings](#chart-settings).

### Installation command line options

The table below contains all the possible charts configurations that can be supplied to
the `helm install` command using the `--set` flags.

| Parameter                      | Default         | Description                              |
| ------------------------------ | --------------- | ---------------------------------------- |
| `annotations`                  |                 | Pod annotations                          |
| `enabled`                      | `true`          | Gitaly enable flag                       |
| `external[].hostname`          | `- ""`          | hostname of external node                |
| `external[].name`              | `- ""`          | name of external node storage            |
| `external[].port`              | `- ""`          | port of external node                    |
| `extraContainers`              |                 | List of extra containers to include      |
| `extraInitContainers`          |                 | List of extra init containers to include |
| `extraVolumeMounts`            |                 | List of extra volumes mountes to do      |
| `extraVolumes`                 |                 | List of extra volumes to create          |
| `image.pullPolicy`             | `Always`        | Gitaly image pull policy                 |
| `image.pullSecrets`            |                 | Secrets for the image repository         |
| `image.repository`             | `registry.com/gitlab-org/build/cng/gitaly` |Gitaly image repository |
| `image.tag`                    | `latest`        | Gitaly image tag                         |
| `init.image`                   | `busybox`       | initContainer image                      |
| `init.tag`                     | `latest`        | initContainer image tag                  |
| `internal.names[]`             | `- default`     | Ordered names of statfulset storages     |
| `service.externalPort`         | `8075`          | Gitaly service exposed port              |
| `service.internalPort`         | `8075`          | Gitaly internal port                     |
| `service.name`                 | `gitaly`        | Gitaly service name                      |
| `service.type`                 | `ClusterIP`     | Gitaly service type                      |
| `serviceName`                  | `gitaly`        | Gitaly service name                      |
| `tolerations`                  | `[]`            | Toleration labels for pod assignment     |
| `persistence.accessMode`       | `ReadWriteOnce` | Gitaly persistence access mode           |
| `persistence.enabled`          | `true`          | Gitaly enable persistence flag           |
| `persistence.matchExpressions` |                 | Label-expression matches to bind         |
| `persistence.matchLabels`      |                 | Label-value matches to bind              |
| `persistence.size`             | `50Gi`          | Gitaly persistence volume size           |
| `persistence.storageClass`     |                 | storageClassName for provisioning        |
| `persistence.subPath`          |                 | Gitaly persistence volume mount path     |

## Chart configuration examples

### image.pullSecrets

`pullSecrets` allows you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods can be
found in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`

```yaml
image:
  repository: my.gitaly.repository
  tag: latest
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

`annotations` allows you to add annotations to the gitaly pods.

Below is an example use of `annotations`:

```yaml
annotations:
  kubernetes.io/example-annotation: annotation-value
```

## External Services

This chart should be attached the Unicorn service, and should also use the same Redis
as the attached Unicorn service.

### Redis

```yaml
redis:
  host: redis.example.com
  serviceName: redis
  port: 6379
```

| Name          | Type    | Default | Description |
|:------------- |:-------:|:------- |:----------- |
| `host`        | String  |         | The hostname of the Redis server with the database to use. This can be omitted in lieu of `serviceName`. |
| `port`        | Integer | `6379`  | The port on which to connect to the Redis server. |
| `serviceName` | String  | `redis` | The name of the `service` which is operating the Redis database. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Redis as a part of the overall GitLab chart. |

NOTE: **Note:** Credentials will be sourced from `global.redis.password` values.

### Unicorn

```yaml
unicorn:
  host: unicorn.example.com
  serviceName: unicorn
  port: 8080
```

| Name          | Type    | Default   | Description |
|:------------- |:-------:|:--------- |:----------- |
| `host`        | String  |           | The hostname of the Unicorn server. This can be omitted in lieu of `serviceName`. |
| `port`        | Integer | `8080`    | The port on which to connect to the Unicorn server.|
| `serviceName` | String  | `unicorn` | The name of the `service` which is operating the Unicorn server. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Unicorn as a part of the overall GitLab chart. |

## Chart Settings

The following values are used to configure the Gitaly Pods.

NOTE: **Note:** Gitaly uses an Auth Token to authenticate with the Unicorn and Sidekiq
  services. The Auth Token secret and key are sourced from the `global.gitaly.authToken`
  value. Additionally, the Gitaly container has a copy of GitLab Shell, which has some configuration
  that can be set. The Shell authToken is sourced from the `global.shell.authToken`
  values.

### Git Repository Persistence

This chart provisions a PersistentVolumeClaim and mounts a corresponding persistent
volume for the Git repository data. You'll need physical storage available in the
Kubernetes cluster for this to work. If you'd rather use emptyDir, disable PersistentVolumeClaim
with: `persistence.enabled: false`.

NOTE: **Note:** The persistence settings for gitaly are used in a volumeClaimTemplate
  that should be valid for all your gitaly pods. You should *not* include settings
  that are meant to reference a single specific volume (ie volumeName). If you want
  to reference a specific volume, you need to manually create the PersistentVolumeClaim.

```yaml
persistence:
  enabled: true
  storageClass: standard
  accessMode: ReadWriteOnce
  size: 50Gi
  matchLabels: {}
  matchExpressions: []
  subPath: "/data"
```

| Name               | Type    | Default         | Description |
|:------------------ |:-------:|:--------------- |:----------- |
| `accessMode`       | String  | `ReadWriteOnce` | Sets the accessMode requested in the PersistentVolumeClaim. See [Kubernetes Access Modes Documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) for details. |
| `enabled`          | Boolean | `true`          | Sets whether or not to use a PersistentVolumeClaims for the repo data. If `false`, an emptyDir volume is used. |
| `matchExpressions` | Array   |                 | Accepts an array of label condition objects to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector). |
| `matchLabels`      | Map     |                 | Accepts a Map of label names and label values to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector). |
| `size`             | String  | `50Gi`          | The minimum volume size to request for the data persistence. |
| `storageClass`     | String  |                 | Sets the storageClassName on the Volume Claim for dynamic provisioning. When unset or null, the default provisioner will be used. If set to a hyphen, dynamic provisioning is disabled. |
| `subPath`          | String  |                 | Sets the path within the volume to mount, rather than the volume root. The root is used if the subPath is empty. |
