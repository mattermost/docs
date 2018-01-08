# Using NGINX

We provide an complet NGINX deployment to be used as an ingress. Not all Kubernetes providers natively support the NGINX [Ingress][kubernetes-ingress], to ensure compatibility.

This chart provides two services: `nginx` which is `nginx-ingress-controller`,
and `nginx-default-backend` which is `defaultbackend` from the [`gcr.io/google_containers`][] registry.

## Configuring NGINX

The NGINX deployment requires 2 [ConfigMap][]s: one for NGINX configuration,
and one for TCP services configuration.

### Configuring the Service

The [Service][] is configured as `type: LoadBalancer`. If you are on a hosted
Kubernetes cluster that requires claiming a static IP (e.g. GKE), you will need
add the `loadBalancerIP` value, which will populate into the [Service][] if present.

```
service:
  name: nginx
  type: LoadBalancer
  ports:
  - http: 80
  - https: 443
  - ssh: 22
```

### NGINX options

```
proxyConnectTimeout: 15
proxyReadTimeout: 600
proxySendTimeout: 600
proxyBodySize: "512m"
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

## Configuring the Ingress

This section describes configuring the [Ingress][]. By default this is disabled, so you'll have to enable it to make use of the following series of settings. Primarily, these settings will be familiar with [Kubernetes Ingress][kubernetes-ingress] documentation, but slightly simplified thanks to [Helm][helm].

#### enabled

Field `enabled:`, boolean

This enables or disables this dedicated [Ingress][].

Default `false`, set `true` to enable.

#### hosts

Field `hosts:`, a list of items in the form below:
```
hosts:
  - name: gitlab.example.local
    serviceName: omnibus
    servicePort: og-workhorse
  - name: registry.example.local
    serviceName: registry
    servicePort: registry
```

This controls the hostnames accepted by the [Ingress][], and to which service
the requests will be routed.

#### tls

Field `tls:`, a map of items, per the [Kubernetes Ingress][kubernetes-ingress] documentation.

As the official documentation shows, this field should contain a map including a
list of `hosts` by hostname, and a `secretName` which names the [Kubernetes Secret][kubernetes-secret]
that houses the TLS certificate and key to be used for that hostname. And exmaple
is found below appear as such:
```
tls:
  - hosts:
    - registry.example.local
    secretName: registry-example-tls
```

*Note:* While you may be able to combine `tls` with ACME, it is not tested.

#### annotations

This field is an exact match to the standard `annotations` for [Kubernetes Ingress][kubernetes-ingress].

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

Enable it in the `serviceAccount` field:

```
serviceAccount:
  autoGenerate: true
```

Otherwise, you will need to supply an existing ServiceAccount.

### Provide existing Service Account

If you have already created a ServiceAccount that has the adequate permissions for nginx. You can specify it by name in the `serviceAccount` field.

```
serviceAccount:
  name: default
```

[Service]: ../../../charts/nginx/templates/service.yaml
[Deployment]: ../../../charts/nginx/templates/deployment.yaml
[ConfigMap]: ../../../charts/nginx/templates/configmap.yaml
[ConfigMapTcp]: ../../../charts/nginx/templates/configmap-tcp.yaml
[Ingress]: ../../../charts/nginx/templates/ingress.yaml
[values.yml]: ../../../charts/nginx/values.yml

[registry]: https://hub.docker.com/_/registry/
[kubernetes-ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/#tls
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[helm]: https://helm.sh
[kubernetes-ingress-nginx-configuration]: https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md
[RBAC]: https://kubernetes.io/docs/admin/authorization/rbac/
