# Using the Container Registry

The `registry` sub-chart provides the Registry component to a complete cloud-native
GitLab deployment on Kubernetes. This sub-chart makes use of the upstream [registry][]
[container][docker-distribution-library] containing [Docker Distribution][docker-distribution]. This chart is composed of 3 primary parts: [Service][], [Deployment][], and [ConfigMap][]. An additional optional [Ingress][] has been
provided to allow separation from the global [Ingress](../README.md#ingress) as provided by the parent chart.

All configuration is handled according to the official [Registry configuration documentation][docker-distribution-config-docs]
using `/etc/docker/registry/config.yml` variables provided to the [Deployment][], populated from the [ConfigMap][]. The [ConfigMap][] overrides the upstream defaults, but is [based upon them][registry-config].

## Design Choices

A Kubernetes `Deployment` was chosen as the deployment method for this chart to
allow for simple scaling of instances, while allowing for [rolling-update](https://kubernetes.io/docs/user-guide/kubectl/v1.7/#rolling-update)s.

This chart makes use of only two secrets:
- `certBundle`: A secret that will contain the public certificate bundle to verify
the authentication tokens provided by the associated GitLab instance(s). See
[documentation](https://docs.gitlab.com/ee/administration/container_registry.html#disable-container-registry-but-use-gitlab-as-an-auth-endpoint) on using GitLab as an auth endpoint.
- *optional*: The secret which will contain the SSL certificates for the HTTPS
termination by the [Ingress][]. This secret follows the requirements set forth in
[Kubernetes Ingress's TLS section][kubernetes-ingress]. If you chose to use
the global [Ingress](../README.md#ingress) from the parent chart, this will not
be required at all.

# Configuration

We will describe all the major sections of the configuration below. When configuring from the parent chart, these values will be as such:

```
registry:
  enabled:
  image:
  service:
  registry:
```

If you should chose to deploy this chart as a standalone, remove the top level `registry`.

## Enable the sub-chart

They way we've chosen to implement compartmentalized sub-charts includes the ability to disable the components that you may not want in a given deployment. For this reason, the first settings you should decided upon is `enabled:`.

By default, Registry is enabled out of the box. Should you wish to disable it,
set `enabled: false`.

## Configuring the `image`

This section dictates the settings for the container image used by this sub-chart's [Deployment][]. You can change the included version of the Registry and `pullPolicy`.

Default settings:
- `tag: '2.6'`
- `pullPolicy: 'IfNotPresent'`

## Configuring the `service`

This section controls the name and type of the [Service][]. These settings will
be populated by the [values.yml][].

By default, the [Service][] is configured as:
- `type: ClusterIP` on `0.0.0.0`, restricting access to the interal network of the Kubernetes cluster.
- `name:` is set to `registry`.

## Configuring the Registry

The `registry` section of this chart pertains to the configuration of the underlying
[registry][] container. Only most critical values for integration with GitLab are
exposed. For this integration, we make use of the `auth.token.x` settings of
[Docker Distribution][docker-distribution], controlling authentication to the registry via JWT
 [authentication tokens](https://docs.docker.com/registry/spec/auth/token/).

#### httpSecret

Field `httpSecret` is a string that correlates to the `http.secret` value of [registry][].
This value will be automatically populated with a random string of 128 alpha-numeric
characters encoded to base64.

You should only need to supply this value when using a load balancer across
multiple clusters. See the following note from the [Registry configuration documents][docker-distribution-config-docs]:

> If you are building a cluster of registries behind a load balancer, you MUST ensure the secret is the same for all registries.

#### authEndpoint

Field `authEndpoint` is a string, providing the URL to the GitLab instance(s) that the [registry][] will authenticate to.

The value should include the protocol and hostname only. The chart template will automatically append the necessary request path. The resulting value will be populated to `auth.token.realm` inside the container.

Example: `authEndpoint: "https://gitlab.example.local"`

#### certBundle

Field `certBundle` is a map containing two items: `secretName` and `bundleName`.

`secretName` is a string containing the name of the [Kubernetes Secret][kubernetes-secret] that houses the certificate bundle to be used to verify the tokens created by the GitLab instance(s).

`bundleName` is the name of the `key` in the `Secret` which houses the certificate
bundle that will be provided to the [registry][] container as `auth.token.rootcertbundle`.

Default Example:
```
certBundle:
  secretName: gitlab-registry-certbundle
  bundleName: gitlab-registry.crt
```

#### replicas

Field `replicas` is an integer, controlling the number of [registry][] instances to create as a part of the set. This defaults to `1`.

#### storage

Field `storage` is a map, the value of which is taken directly from [Registry Configuration: `storage`](https://docs.docker.com/registry/configuration/#storage). Please refer to that documentation for extended details.

If you chose to use the `filesystem` driver, you will need to provide persistent volumes for this data.

For the sake of resiliency and simplicity, it is recommended to make use of an
external service other than the `filesystem` driver, such as `s3`, `gcs` or `azure`.

## Configuring the Ingress (optional)

This section describes configuring the *optional* dedicated [Ingress][]. By default this is disabled, so you'll have to enable it to make use of the following series of settings. Primarily, these settings will be familiar with [Kubernetes Ingress][kubernetes-ingress] documentation, but slightly simplified thanks to [Helm][helm].

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



[registry]: https://hub.docker.com/_/registry/
[docker-distribution]: https://github.com/docker/distribution
[docker-distribution-library]: https://github.com/docker/distribution-library-image
[docker-distribution-config-docs]: https://docs.docker.com/registry/configuration
[registry-config]: https://github.com/docker/distribution-library-image/blob/master/registry/config-example.yml

[Service]: ../../charts/registry/templates/service.yaml
[Deployment]: ../../charts/registry/templates/deployment.yaml
[ConfigMap]: ../../charts/registry/templates/registry-configmap.yaml
[Ingress]: ../../charts/registry/templates/ingress.yaml
[values.yml]: ../../charts/registry/values.yml

[kubernetes-ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/#tls
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[helm]: https://helm.sh
[kubernetes-ingress-nginx-configuration]: https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md
