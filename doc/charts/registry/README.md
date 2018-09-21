# Using the Container Registry

The `registry` sub-chart provides the Registry component to a complete cloud-native
GitLab deployment on Kubernetes. This sub-chart makes use of the upstream [registry][]
[container][docker-distribution-library] containing [Docker Distribution][docker-distribution]. This chart is composed of 3 primary parts: [Service][], [Deployment][], and [ConfigMap][].

All configuration is handled according to the official [Registry configuration documentation][docker-distribution-config-docs]
using `/etc/docker/registry/config.yml` variables provided to the [Deployment][], populated from the [ConfigMap][]. The [ConfigMap][] overrides the upstream defaults, but is [based upon them][registry-config].

## Design Choices

A Kubernetes `Deployment` was chosen as the deployment method for this chart to
allow for simple scaling of instances, while allowing for [rolling-update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update-intro/)s.

This chart makes use of only two secrets:
- `global.registry.certificate.secret`: A global secret that will contain the public certificate bundle to verify
the authentication tokens provided by the associated GitLab instance(s). See
[documentation](https://docs.gitlab.com/ee/administration/container_registry.html#disable-container-registry-but-use-gitlab-as-an-auth-endpoint) on using GitLab as an auth endpoint.
- `global.registry.httpSecret.secret`: A global secret that will contain the [shared secret](https://docs.docker.com/registry/configuration/#http) between registry pods.

# Configuration

We will describe all the major sections of the configuration below. When configuring from the parent chart, these values will be as such:

```
registry:
  enabled:
  image:
  service:
  httpSecret:
  authEndpoint:
  tokenIssuer:
  certificate:
  replicas:
  storage:
  ingress:
    enabled:
    tls:
      secretName
    annotations:
    proxyReadTimeout:
    proxyBodySize:
    proxyBuffering:
```

If you should chose to deploy this chart as a standalone, remove the top level `registry`.

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                | Description                             | Default              |
| ---                      | ---                                     | ---                  |
| image.repository         | Registry image                          | registry             |
| image.tag                | Version of the image to use             | 2.6                  |
| image.pullPolicy         | Pull policy for the registry image      |                      |
| image.pullSecrets        | Secrets to use for image repository     |                      |
| init.image               | initContainer image                     | busybox              |
| init.tag                 | initContainer image tag                 | latest               |
| enabled                  | Enable registry flag                    | true                 |
| httpSecret               | Https secret                            |                      |
| authEndpoint             | Auth endpoint                           | Undefined by default |
| tokenService             | JWT token service                       | container_registry   |
| tokenIssuer              | JWT token issuer                        | gitlab-issuer        |
| certificate.secret       | JWT certificate                         | gitlab-registry      |
| replicas                 | Number of replicas                      | 1                    |
| minio.bucket             | Legacy registry bucket name             | Undefined by default |

## Chart configuration examples
### pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image:
  repository: my.registry.repository
  tag: latest
  pullPolicy: Always
  pullSecrets:
  - name: my-secret-name
  - name: my-secondary-secret-name
```

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

## Configuring the `ingress`

This section controls the registry ingress.

### enabled

Setting that controls whether to create ingress objects for services that support them.

When `false` the `global.ingress.enabled` setting is used.

Defaults to `false`.

### tls.secretName

The name of the Kubernetes TLS Secret that contains a valid certificate and key for the registry url.

When not set, the `global.ingress.tls.secretName` is used instead.

Defaults to not being set.

### annotations

This field is an exact match to the standard `annotations` for [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress).

## Defining the Registry Configuration

The following properties of this chart pertains to the configuration of the underlying
[registry][] container. Only most critical values for integration with GitLab are
exposed. For this integration, we make use of the `auth.token.x` settings of
[Docker Distribution][docker-distribution], controlling authentication to the registry via JWT
 [authentication tokens](https://docs.docker.com/registry/spec/auth/token/).

#### httpSecret

Field `httpSecret` is a map that contains two items: `secret` and `key`.

The content of key this references correlates to the `http.secret` value of [registry][].
This value should be populated with a cryptographically generated random string.

The `shared-secrets` Job will automatically create this secret if not provided. It will be
filled with a securely generated 128 character alpha-numeric string that is base64 encoded.

To create this secret manually:
```
kubectl create secret generic gitlab-registry-httpsecret --from-literal=secret=strongrandomstring
```

#### authEndpoint

Field `authEndpoint` is a string, providing the URL to the GitLab instance(s) that the [registry][] will authenticate to.

The value should include the protocol and hostname only. The chart template will automatically append the necessary request path. The resulting value will be populated to `auth.token.realm` inside the container.

Example: `authEndpoint: "https://gitlab.example.com"`

By default this field is populated with gitlab hostname configuration set using the [Global Settings][globals].

#### certificate

Field `certificate` is a map containing two items: `secret` and `key`.

`secret` is a string containing the name of the [Kubernetes Secret][kubernetes-secret] that houses the certificate bundle to be used to verify the tokens created by the GitLab instance(s).

`key` is the name of the `key` in the `Secret` which houses the certificate
bundle that will be provided to the [registry][] container as `auth.token.rootcertbundle`.

Default Example:
```
certificate:
  secret: gitlab-registry
  key: registry-auth.crt
```

#### replicas

Field `replicas` is an integer, controlling the number of [registry][] instances to create as a part of the set. This defaults to `1`.

#### storage

```
storage:
  secret:
  key: storage
  extraKey:
```

Field `storage` is a reference to a Kubernetes Secret and associated key.
The contents of this secret is taken directly from [Registry Configuration: `storage`](https://docs.docker.com/registry/configuration/#storage).
Please refer to that documentation for extended details.

Example contents of the `storage` block, to be placed in the secret:
```
s3:
  accesskey: BOGUS_ACCESS_KEY
  secretkey: BOGUS_SECRET_KEY
  bucket: gitlab-registry
  v4auth: true
  region: us-east-1
```

Place the _contents_ of the `storage` block into the secret,
and provide the following as items to the `storage` map:

- `secret`: name of the Kubernetes Secret housing the YAML block.
- `key`: name of the key in the secret to use. Defaults to `storage`.
- `extraKey`: (optional) name of an extra key on the secret, which will be mounted to `/etc/docker/registry/storage/${extraKey}` within the container. This can be used to provide the `keyfile` for the `gcs` driver.


If you chose to use the `filesystem` driver:
- You will need to provide persistent volumes for this data.
- [replicas](#replicas) should be set to `1`

For the sake of resiliency and simplicity, it is recommended to make use of an
external service, such as `s3`, `gcs`, `azure` or other compatible Object Storage.


[registry]: https://hub.docker.com/_/registry/
[docker-distribution]: https://github.com/docker/distribution
[docker-distribution-library]: https://github.com/docker/distribution-library-image
[docker-distribution-config-docs]: https://docs.docker.com/registry/configuration
[registry-config]: https://github.com/docker/distribution-library-image/blob/master/registry/config-example.yml

[Service]: ../../../charts/registry/templates/service.yaml
[Deployment]: ../../../charts/registry/templates/deployment.yaml
[ConfigMap]: ../../../charts/registry/templates/configmap.yaml
[values.yml]: ../../../charts/registry/values.yaml
[globals]: ../globals.md

[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
