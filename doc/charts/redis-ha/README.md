# Redis-ha subchart

[Redis](http://redis.io/) is an advanced key-value cache and store. It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets, sorted sets, bitmaps and hyperloglogs.

By default this chart install one master pod containing redis master container and sentinel container, 3 sentinels and 2 redis slave.

## Prerequisites

- Kubernetes 1.5+ with Beta APIs enabled
- PV provisioner support in the underlying infrastructure

The command deploys Redis on the Kubernetes cluster in the default configuration. By default this chart install one master pod containing redis master container and sentinel container, 2 sentinels and 1 redis slave. The [configuration](#configuration) section lists the parameters that can be configured during installation.

## Configuration

The following tables lists the configurable parameters of the Redis chart and their default values.

| Parameter                        | Description                                                                                                                  | Default                                                   |
| -------------------------------- | -----------------------------------------------------                                                                        | --------------------------------------------------------- |
| `redis_image`                    | Redis image                                                                                                                  | `registry.gitlab.com/gitlab-org/build/cng/gitlab-redis-ha:latest`                             |
| `resources.master`               | CPU/Memory for master nodes resource requests/limits                                                                         | Memory: `200Mi`, CPU: `100m`                              |
| `resources.slave`                | CPU/Memory for slave nodes  resource requests/limits                                                                         | Memory: `200Mi`, CPU: `100m`                              |
| `resources.sentinel`             | CPU/Memory for sentinel node resource requests/limits                                                                        | Memory: `200Mi`, CPU: `100m`                              |
| `replicas.servers`               | Number of redis master/slave pods                                                                                            | 3                                                         |
| `replicas.sentinels`             | Number of sentinel pods                                                                                                      | 3                                                         |
| `nodeSelector`                   | Node labels for pod assignment                                                                                               | {}                                                        |
| `tolerations`                    | Toleration labels for pod assignment                                                                                         | []                                                        |
| `servers.serviceType`            | Set to "LoadBalancer" to enable access from the VPC                                                                          | ClusterIP                                                 |
| `servers.annotations`            | See Appliance mode                                                                                                           | ``                                                        |
| `rbac.create`                    |  whether RBAC resources should be created                                                                                    | true                                                      |
| `serviceAccount.create`          | whether a new service account name that the agent will use should be created.                                                | true                                                      |
| `serviceAccount.name`            | service account to be used.  If not set and serviceAccount.create is `true` a name is generated using the fullname template. | ``                                                        |
| `metrics.enabled`                | Toggle Prometheus Redis exporter sidecar container                                                                           | true                                                      |

## Configuring `metrics`

By default, a sidecar container exposing a Prometheus metrics exporter is launched along with each Redis master/slave container. The exporter exposes a `/metrics` endpoint on port `9121`. When metrics are enabled, annotations are added to each service allowing a Prometheus server to discover and scrape the exposed metrics.

## Internals
The customized Redis server image determines whether the pod that executes it will be a Redis Sentinel,
Master, or Slave and launches the appropriate service. This Helm chart signals Sentinel status with
environment variables. If not set, the newly launched pod will query K8S for an active master. If none
exists, it uses a deterministic means of sensing whether it should launch as master then writes "master"
or "slave" to the label called redis-role as appropriate. It's this label that determines which LB a pod
can be seen through.

The redis-role=master pod is the key for the cluster to get started. Sentinels will wait for it to appear
in the LB before they finish launching. All other pods wait for the Sentinels to ID the master. Running
Pods also set the labels podIP and runID. runID is the first few characters of the unique run_id value
generated by each Redis sever.

During normal operation, there should be only one redis-role=master pod. If it fails, the Sentinels
will nominate a new master and change all the redis-role values appropriately.

To see the pod roles, run the following:

```bash
$ kubectl get pods -L redis-role
```
