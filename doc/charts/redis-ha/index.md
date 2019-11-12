# Redis-ha subchart

[Redis](https://redis.io/) is an advanced key-value cache and store. It is often referred
to as a data structure server since keys can contain strings, hashes, lists, sets,
sorted sets, bitmaps and hyperloglogs.

The chart deploys Redis on the Kubernetes cluster in the default configuration. By
default this chart installs one master pod containing a Redis master container, a
sentinel container, 3 sentinels and 2 Redis slaves. The [configuration](#configuration)
section lists the parameters that can be configured during installation.

## Prerequisites

- Kubernetes 1.5+ with Beta APIs enabled
- PV provisioner support in the underlying infrastructure

## Configuration

The following table lists the configurable parameters of the Redis chart and their
default values.

| Parameter               | Default                      | Description |
| ----------------------- | ---------------------------- | ----------- |
| `image.pullPolicy`      |                              | Pull policy for the Redis image.                       |
| `image.pullSecrets`     |                              | Secrets to use for image repository.                   |
| `image.repository`      | `registry.gitlab.com/gitlab-org/build/cng/gitlab-redis-ha`| Redis image.              |
| `image.tag`             | `latest`                     | Version of the Redis image to use.                     |
| `init.image`            | `busybox`                    | initContainer image.                                   |
| `init.tag`              | `latest`                     | initContainer image tag.                               |
| `metrics.enabled`       | `true`                       | Toggle Prometheus Redis exporter sidecar container.    |
| `nodeSelector`          | `{}`                         | Node labels for pod assignment.                        |
| `rbac.create`           | `true`                       | Whether RBAC resources should be created.              |
| `replicas.sentinels`    | `3`                          | Number of sentinel pods.                               |
| `replicas.servers`      | `3`                          | Number of Redis master/slave pods.                     |
| `resources.master`      | Memory: `200Mi`, CPU: `100m` | CPU/Memory for master nodes resource requests/limits.  |
| `resources.sentinel`    | Memory: `200Mi`, CPU: `100m` | CPU/Memory for sentinel node resource requests/limits. |
| `resources.slave`       | Memory: `200Mi`, CPU: `100m` | CPU/Memory for slave nodes  resource requests/limits.  |
| `servers.annotations`   | `{}`                         | See Appliance mode.                                    |
| `servers.serviceType`   | `ClusterIP`                  | Set to "LoadBalancer" to enable access from the VPC.   |
| `serviceAccount.create` | `true`                       | Whether a new service account name that the agent will use should be created. |
| `serviceAccount.name`   |                              | Service account to be used. If not set and `serviceAccount.create` is `true` a name is generated using the fullname template. |
| `tolerations`           | `[]`                         | Toleration labels for pod assignment.                  |

## Chart configuration examples

### pullSecrets

`pullSecrets` allows you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods can be
found in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`:

```YAML
image:
  repository: my.redis-ha.repository
  tag: latest
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

## Configuring `metrics`

By default, a sidecar container exposing a Prometheus metrics exporter is launched
along with each Redis master/slave container. The exporter exposes a `/metrics` endpoint
on port `9121`. When metrics are enabled, annotations are added to each service allowing
a Prometheus server to discover and scrape the exposed metrics.

## Internals

This customized Redis server image determines whether the pod that executes it will
be a Redis Sentinel, Master, or Slave and launches the appropriate service. This Helm
chart signals Sentinel status with environment variables. If not set, the newly launched
pod will query K8s for an active master. If none exists, it uses a deterministic means
of sensing whether it should launch as master, then writes "master" or "slave" to the
`redis-role` label as appropriate. This label determines which LB a pod can be seen
through.

The `redis-role=master` pod is the key for the cluster to get started. Sentinels will
wait for it to appear in the LB before they finish launching. All other pods wait for
the Sentinels to ID the master. Running Pods also set the labels `podIP` and `runID`.
`runID` is the first few characters of the unique `run_id` value generated by each
Redis sever.

During normal operation, there should be only one `redis-role=master` pod. If it fails,
the Sentinels will nominate a new master and change all the `redis-role` values appropriately.

To see the pod roles, run the following:

```bash
kubectl get pods -L redis-role
```
