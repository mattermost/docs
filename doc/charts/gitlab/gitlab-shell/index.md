# Using the GitLab-Shell chart

The `gitlab-shell` sub-chart provides an SSH server configured for Git SSH access to GitLab.

## Requirements

This chart depends on access to Redis and Unicorn services, either as part of the
complete GitLab chart or provided as external services reachable from the Kubernetes
cluster this chart is deployed onto.

## Design Choices

In order to easily support SSH replicas, and avoid using shared storage for the ssh
authorized keys, we are using the SSH [AuthorizedKeysCommand](https://man.openbsd.org/sshd_config#AuthorizedKeysCommand)
to authenticate against GitLab's authorized keys endpoint. As a result, we don't persist
or update the AuthorizedKeys file within these pods.

## Configuration

The `gitlab-shell` chart is configured in two parts: [external services](#external-services),
and [chart settings](#chart-settings). The port exposed through Ingress is configured
with `global.shell.port`, and defaults to `22`.

## Installation command line options

| Parameter                | Default        | Description                              |
| ------------------------ | -------------- | ---------------------------------------- |
| `annotations`            |                | Pod annotations                          |
| `enabled`                | `true`         | Shell enable flag                        |
| `extraContainers`        |                | List of extra containers to include      |
| `extraInitContainers`    |                | List of extra init containers to include |
| `extraVolumeMounts`      |                | List of extra volumes mounts to do       |
| `extraVolumes`           |                | List of extra volumes to create          |
| `hpa.targetAverageValue` | `100m`         | Set the autoscaling target value         |
| `image.pullPolicy`       | `Always`       | Shell image pull policy                  |
| `image.pullSecrets`      |                | Secrets for the image repository         |
| `image.repository`       | `registry.com/gitlab-org/build/cng/gitlab-shell` | Shell image repository |
| `image.tag`              | `latest`       | Shell image tag                          |
| `init.image`             | `busybox`      | initContainer image                      |
| `init.tag`               | `latest`       | initContainer image tag                  |
| `redis.serviceName`      | `redis`        | Redis service name                       |
| `replicaCount`           | `1`            | Shell replicas                           |
| `service.externalPort`   | `22`           | Shell exposed port                       |
| `service.internalPort`   | `22`           | Shell internal port                      |
| `service.name`           | `gitlab-shell` | Shell service name                       |
| `service.type`           | `ClusterIP`    | Shell service type                       |
| `service.loadBalancerIP` |                | IP address to assign to LoadBalancer (if supported) |
| `service.loadBalancerSourceRanges` |      | List of IP CIDRs allowed access to LoadBalancer (if supported)  |
| `service.type`           | `ClusterIP`    | Shell service type                       |
| `tolerations`            | `[]`           | Toleration labels for pod assignment     |
| `unicorn.serviceName`    | `unicorn`      | Unicorn service name                     |

## Chart configuration examples

### image.pullSecrets

`pullSecrets` allows you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods can be
found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`:

```yaml
image:
  repository: my.shell.repository
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

`annotations` allows you to add annotations to the GitLab Shell pods.

Below is an example use of `annotations`

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
  password:
    secret: gitlab-redis
    key: redis-password
```

| Name            | Type    | Default | Description |
|:----------------|:-------:|:--------|:------------|
| host            | String  |         | The hostname of the Redis server with the database to use. This can be omitted in lieu of `serviceName`. |
| password.key    | String  |         | The name of the key in the secret below that contains the password. |
| password.secret | String  |         | The name of the Kubernetes `Secret` to pull from. |
| port            | Integer | `6379`  | The port on which to connect to the Redis server. |
| serviceName     | String  | `redis` | The name of the `service` which is operating the Redis database. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Redis as a part of the overall GitLab chart. |

### Unicorn

```yaml
unicorn:
  host: unicorn.example.com
  serviceName: unicorn
  port: 8080
```

| Name        | Type    | Default   | Description |
|:------------|:-------:|:----------|:------------|
| host        | String  |           | The hostname of the Unicorn server. This can be omitted in lieu of `serviceName`. |
| port        | Integer | `8080`    | The port on which to connect to the Unicorn server.|
| serviceName | String  | `unicorn` | The name of the `service` which is operating the Unicorn server. If this is present, and `host` is not, the chart will template the hostname of the service (and current `.Release.Name`) in place of the `host` value. This is convenient when using Unicorn as a part of the overall GitLab chart. |

## Chart Settings

The following values are used to configure the GitLab Shell Pods.

### hostKeys.secret

The name of the Kubernetes `secret` to grab the SSH host keys from. The keys in the
secret must start with the key names `ssh_host_` in order to be used by GitLab Shell.

### authToken

GitLab Shell uses an Auth Token in its communication with Unicorn. Share the token
with GitLab Shell and Unicorn using a shared Secret.

```yaml
authToken:
 secret: gitlab-shell-secret
 key: secret
```

| Name             | Type    | Default | Description |
|:-----------------|:-------:|:--------|:------------|
| authToken.key    | String  |         | The name of the key in the above secret that contains the authToken. |
| authToken.secret | String  |         | The name of the Kubernetes `Secret` to pull from. |

### LoadBalancer Service

If the `service.type` is set to `LoadBalancer`, you can optionally specify `service.loadBalancerIP` to create
the `LoadBalancer` with a user-specified IP (if your cloud provider supports it).

You can also optionally specify a list of `service.loadBalancerSourceRanges` to restrict
the CIDR ranges that can access the `LoadBalancer` (if your cloud provider supports it).

Additional information about the `LoadBalancer` service type can be found in
[the Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/#loadbalancer)

```yaml
service:
  type: LoadBalancer
  loadBalancerIP: 1.2.3.4
  loadBalancerSourceRanges:
  - 5.6.7.8/32
  - 10.0.0.0/8
```
