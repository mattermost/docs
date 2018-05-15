# Using NGINX

We provide an complet NGINX deployment to be used as an ingress. Not all Kubernetes providers natively support the NGINX [Ingress][kubernetes-ingress], to ensure compatibility.

This chart provides two services: `nginx` which is `nginx-ingress-controller`,
and `nginx-default-backend` which is `defaultbackend` from the [`gcr.io/google_containers`][] registry.

## Configuring NGINX

The NGINX deployment requires 2 [ConfigMap][]s: one for NGINX configuration,
and one for TCP services configuration.

### Global Settings

We share some common global settings among our charts. See the [Globals Documentation][globals] for common configuration
options, such as GitLab and Registry hostnames.

### Configuring the Service

The [Service][] is configured as `type: LoadBalancer`. If you are on a hosted
Kubernetes cluster that requires claiming a static IP (e.g. GKE), you will need
add the `loadBalancerIP` value, which will populate into the [Service][] if present.
If this value is not provided, the [Service][] will claim an ephemeral IP address
from the provider.

You may specify this value via `service.loadBalancerIP` or via the chart global
`global.hosts.externalIP`.

```
service:
  name: nginx
  type: LoadBalancer
  loadBalancerIP: <address>
  ports:
  - http: 80
  - https: 443
  - ssh: 22
```

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                         | Description                                            | Default                                                        |
| ---                               | ---                                                    | ---                                                            |
| replicaCount                      | Number of replicas                                     | 1                                                              |
| images.defaultbackend.repository  | Default backend that nginx routes to eg: 404           | gcr.io/google_containers/defaultbackend                        |
| images.defaultbackend.tag         | dafault backend image tag                              | 1.4                                                            |
| images.defaultbackend.pullPolicy  | default backend pull policy                            | IfNotPresent                                                   |
| images.defaultbackend.pullSecrets | Secrets for the image repository                       |                                                                |
| images.nginxIngress.repository    | nginx repository                                       | quay.io/kubernetes-ingress-controller/nginx-ingress-controller |
| images.nginxIngress.tag           | nginx image tag                                        | 0.9.0                                                          |
| images.nginxIngress.pullPolicy    | nginx image pull policy                                | IfNotPresent                                                   |
| images.nginxIngress.pullSecrets   | Secrets for the image repository                       |                                                                |
| service.name                      | nginx service name                                     | nginx                                                          |
| service.type                      | nginx service type                                     | LoadBalancer                                                   |
| service.ports                     | nginx service ports                                    | [{"http": 80}, {"https": 443}, {"ssh": 22}]                    |
| service.loadBalancerIP            | IP of the external load balancer                       | Undefined                                                      |
| serviceAccount.autoGenerate       | Whether chart should generate service account for RBAC | true                                                           |
| serviceAccount.name               | Service account name                                   | default                                                        |
| proxyConnectTimeout               | Defines a timeout for establishing a connection        | 15                                                             |
| proxyReadTimeout                  | Defines a timeout for reading a response               | 600                                                            |
| proxySendTimeout                  | Sets a timeout for transmitting a request              | 600                                                            |
| proxyBodySize                     | body size                                              | 512m                                                           |
| hstsIncludeSubdomains             | set HSTS for all subdomains                            | false                                                          |
| serverNameHashBucketSize          | Sets the bucket size for the server names hash tables  | 256                                                            |
| global.hosts.domain               | Domain name                                            | example.local                                                  |
| global.hosts.hostSuffix           |                                                        | Undefined by default                                           |
| global.hosts.https                | True if nginx will serve over https                    | false                                                          |
| global.hosts.gitlab.serviceName   | Gitlab service name                                    | unicorn                                                        |
| global.hosts.gitlab.servicePort   | Gitlab service port name                               | workhorse                                                      |
| global.hosts.registry.serviceName | Registry service name                                  | registry                                                       |
| global.hosts.registry.servicePort | Registry port name                                     | registry                                                       |
| global.hosts.minio.serviceName    | Minio service name                                     | minio-svc                                                      |
| global.hosts.minio.servicePort    | Minio port name                                        | service                                                        |
| global.hosts.externalIP           | IP of the external load balancer, from global          | Undefined                                                      |
| shell.name                        | Shell service name                                     | gitlab-shell                                                   |
| shell.port                        | Shell port name                                        | ssh                                                            |
| ingress.enabled                   | Enable ingress                                         | true                                                           |
| ingress.hosts                     | Hosts ingress listens to                               | Empty array                                                    |
| ingress.annotations               | Annotations                                            | Undefined by default                                           |
| ingress.tls                       | Tls certificates (custom)                              | Undefined by default                                           |

### NGINX options

```
hstsIncludeSubdomains: false
serverNameHashBucketSize: 256
```

The above values correlate directly to their values in the NGINX configuration file.
Further explanation of all items can be found [in upstream documentation](https://github.com/nginxinc/kubernetes-ingress/tree/master/examples/customization)


### TCP options

The [ConfigMap for Tcp][ConfigMapTcp] sets the `Service` to which SSH connections
on port `22` will be fowarded. This is controlled by setting the value of `shell:`

```
shell:
  name: omnibus
  port: og-shell
```

The above defaults will populate into the `ConfigMap`, setting `namespace/deployment-name:port`.
At this time, all charts in the same `namespace`, and the same `deployment`.
This will result in a value like `default/spiffy-fox-omnibus:og-shell`.

## Configure hosts using the Global Settings.

The hostnames for the GitLab Server and the Registry Server can be configured using our chart [Global Settings][globals]

## Setting the Service Account

If your cluster is enforcing [Role Based Access Control][RBAC], then the nginx chart will need to run using a ServiceAccount
that has adequate permissions.

The ServiceAccount needs Role access to:

- Get
  * pods, namespaces, secrets, configmaps, endpoints, and nginx ingress resources
- Create
  * configmaps, endpoints
- Update
  * configmaps, endpoints, and nginx ingress resources

It also needs ClusterRole access to:

- Get
  * nodes, services, extensions, ingresses
- List/Watch
  * configmaps, endpoints, nodes, pods, secrets, services, extensions, ingresses
- Create/Patch
  * events
- Update
  * services, extensions, and the ingressStatus resources

### Generate the Service Account

If the Helm Tiller server is running as a ServiceAccount with the [cluster-admin role](../../helm/README.md#preparing-for-helm-with-rbac),
then the chart can create and manage the ServiceAccount required for nginx.

This is enabled by default in the `serviceAccount` field:

```
serviceAccount:
  autoGenerate: true
```

Rather than auto-generate the account, you can supply an existing ServiceAccount.

### Provide existing Service Account

If you have already created a ServiceAccount that has the adequate permissions for nginx. You can specify it by name in
the `serviceAccount` field, and turning off the `autoGenerate` option.

```
serviceAccount:
  autoGenerate: false
  name: default
```

[Service]: ../../../charts/nginx/templates/service.yaml
[Deployment]: ../../../charts/nginx/templates/deployment.yaml
[ConfigMap]: ../../../charts/nginx/templates/configmap.yaml
[ConfigMapTcp]: ../../../charts/nginx/templates/configmap-tcp.yaml
[Ingress]: ../../../charts/nginx/templates/ingress.yaml
[values.yml]: ../../../charts/nginx/values.yml
[globals]: ../globals.md

[registry]: https://hub.docker.com/_/registry/
[kubernetes-ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/#tls
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[helm]: https://helm.sh
[kubernetes-ingress-nginx-configuration]: https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md
[RBAC]: https://kubernetes.io/docs/admin/authorization/rbac/
