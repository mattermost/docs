# Using GitLab's helm.gitlab.io

## Configuring the Ingress (optional)

This section describes configuring the *optional* shared [Ingress][]. By default this is disabled, so you'll have to enable it to make use of the following series of settings. Primarily, these settings will be familiar with [Kubernetes Ingress][kubernetes-ingress] documentation, but slightly simplified thanks to [Helm][helm].

#### enabled

Field `enable:`, boolean

This enables or disables this dedicated [Ingress][].

Default `false`, set `true` to enable.

#### hosts

Field `hosts:`, a list of items in the form of `name: fqdn`

This controls the hostnames accepted by the [Ingress][]. Note that we do not make
use of any other component fields that could be used when defining an `host:`, as
we're only linking to the [Service][] contained in the chart.

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
The default value includes setting of `kubernetes.io/ingress.class: nginx`.
If you need to replace this value, or add additional, you may do so.

When using `nginx` as the `ingress.class`, it is also recommended to add
`ingress.kubernetes.io/proxy-body-size: 1024M`. This controls `client_max_body_size`,
and should be sized appropriately when used in conjunction with the [registry][]
to allow large images.

One example of an additional `annotation` is `kubernetes.io/tls-acme: "true"`
to enable automatic Lets Encrypt as a part of the [Ingress][] in combination with  `kube-lego`.

Further details of available `ingress.class: nginx` options can be found
[in the documentation][kubernetes-ingress-nginx-configuration] for the NGINX Ingress.

## Configuring sub-charts

- [Registry](registry/README.md)
- [Omnibus](omnibus/README.md) (under gitlab)


```
ingress:
registry:
gitlab:
  omnibus:
```
