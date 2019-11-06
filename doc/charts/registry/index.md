# Using the Container Registry

The `registry` sub-chart provides the Registry component to a complete cloud-native
GitLab deployment on Kubernetes. This sub-chart makes use of the upstream
[registry](https://hub.docker.com/_/registry/) [container](https://github.com/docker/distribution-library-image)
containing [Docker Distribution](https://github.com/docker/distribution). This chart
is composed of 3 primary parts: [Service](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/registry/templates/service.yaml),
[Deployment](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/registry/templates/deployment.yaml),
and [ConfigMap](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/registry/templates/configmap.yaml).

All configuration is handled according to the official [Registry configuration documentation](https://docs.docker.com/registry/configuration/)
using `/etc/docker/registry/config.yml` variables provided to the `Deployment` populated
from the `ConfigMap`. The `ConfigMap` overrides the upstream defaults, but is
[based on them](https://github.com/docker/distribution-library-image/blob/master/config-example.yml).
See below for more details:

- [distribution/cmd/registry/config-example.yml](https://github.com/docker/distribution/blob/master/cmd/registry/config-example.yml)
- [distribution-library-image/config-example.yml](https://github.com/docker/distribution-library-image/blob/master/config-example.yml)

## Design Choices

A Kubernetes `Deployment` was chosen as the deployment method for this chart to allow
for simple scaling of instances, while allowing for
[rolling updates](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/).

This chart makes use of only two secrets:

- `global.registry.certificate.secret`: A global secret that will contain the public
  certificate bundle to verify the authentication tokens provided by the associated
  GitLab instance(s). See [documentation](https://docs.gitlab.com/ee/administration/container_registry.html#disable-container-registry-but-use-gitlab-as-an-auth-endpoint)
  on using GitLab as an auth endpoint.
- `global.registry.httpSecret.secret`: A global secret that will contain the
  [shared secret](https://docs.docker.com/registry/configuration/#http) between registry pods.

## Configuration

We will describe all the major sections of the configuration below. When configuring
from the parent chart, these values will be:

```yaml
registry:
  enabled:
  maintenance:
    readOnly:
      enabled: false
  image:
    tag: '2.7.1'
    pullPolicy: IfoNtPresent
  annotations:
  service:
    type: ClusterIP
    name: registry
  httpSecret:
    secret:
    key:
  authEndpoint:
  tokenIssuer:
  certificate:
    secret: gitlab-registry
    key: registry-auth.crt
  deployment:
    terminationGracePeriodSeconds: 30
  draintimeout: '0'
  hpa:
    minReplicas: 2
    maxReplicas: 10
    cpu:
      targetAverageUtilization: 75
  storage:
    secret:
    key: storage
    extraKey:
  compatibility:
    schema1:
      enabled: false
  validation:
    disabled: true
  tolerations: []
  ingress:
    enabled: false
    tls:
      enabled: true
      serviceName: redis
    annotations:
    proxyReadTimeout:
    proxyBodySize:
    proxyBuffering:
  networkpolicy:
    enabled: false
    egress:
      enabled: false
      rules: []
    ingress:
      enabled: false
      rules: []
```

If you chose to deploy this chart as a standalone, remove the `registry` at the top level.

## Installation command line options

| Parameter                                  | Default                                      | Description                                                                                          |
|--------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------|
| `annotations`                              |                                              | Pod annotations                                                                                      |
| `authAutoRedirect`                         | `true`                                       | Auth auto-redirect (must be true for Windows clients to work)                                        |
| `authEndpoint`                             | `global.hosts.gitlab.name`                   | Auth endpoint (only host and port)                                                                   |
| `certificate.secret`                       | `gitlab-registry`                            | JWT certificate                                                                                      |
| `compatiblity`                             |                                              | Configuration of compatibility settings                                                              |
| `debug`                                    |                                              | Debug port and prometheus metrics                                                                    |
| `deployment.terminationGracePeriodSeconds` | `30`                                         | Optional duration in seconds the pod needs to terminate gracefully.                                  |
| `draintimeout`                             | `'0'`                                        | Amount of time to wait for HTTP connections to drain after receiving a SIGTERM signal (e.g. `'10s'`) |
| `relativeurls`                             | `false`                                      | Enable the registry to return relative URLs in Location headers. |
| `enabled`                                  | `true`                                       | Enable registry flag                                                                                 |
| `hpa.cpu.targetAverageUtilization`         | `75`                                         | Target value of the average of the resource metric across all relevant pods which governs the HPA    |
| `hpa.customMetrics`                        | `[]`                                         | autoscaling/v2beta1 Metrics contains the specifications for which to use to calculate the desired replica count (overrides the default use of Average CPU Utilization configured in `targetAverageUtilization`) |
| `hpa.minReplicas`                          | `2`                                          | Minimum number of replicas                                                                           |
| `hpa.maxReplicas`                          | `10`                                         | Maximum number of replicas                                                                           |
| `httpSecret`                               |                                              | Https secret                                                                                         |
| `image.pullPolicy`                         |                                              | Pull policy for the registry image                                                                   |
| `image.pullSecrets`                        |                                              | Secrets to use for image repository                                                                  |
| `image.repository`                         | `registry`                                   | Registry image                                                                                       |
| `image.tag`                                | `2.7.1`                                      | Version of the image to use                                                                          |
| `init.image`                               | `busybox`                                    | initContainer image                                                                                  |
| `init.tag`                                 | `latest`                                     | initContainer image tag                                                                              |
| `log`                                      | `{level: warn, fields: {service: registry}}` | Configure the logging options                                                                        |
| `minio.bucket`                             | `global.registry.bucket`                     | Legacy registry bucket name                                                                          |
| `maintenance.readOnly.enabled`             | `false`                                      | Enable registry's read-only mode                                                                     |
| `tokenService`                             | `container_registry`                         | JWT token service                                                                                    |
| `tokenIssuer`                              | `gitlab-issuer`                              | JWT token issuer                                                                                     |
| `tolerations`                              | `[]`                                         | Toleration labels for pod assignment                                                                 |

## Chart configuration examples

### pullSecrets

`pullSecrets` allows you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods can be
found in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`:

```yaml
image:
  repository: my.registry.repository
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

`annotations` allows you to add annotations to the registry pods.

Below is an example use of `annotations`

```yaml
annotations:
  kubernetes.io/example-annotation: annotation-value
```

## Enable the sub-chart

The way we've chosen to implement compartmentalized sub-charts includes the ability
to disable the components that you may not want in a given deployment. For this reason,
the first setting you should decide on is `enabled`.

By default, Registry is enabled out of the box. Should you wish to disable it, set `enabled: false`.

## Configuring the `image`

This section details the settings for the container image used by this sub-chart's
[Deployment](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/registry/templates/deployment.yaml).
You can change the included version of the Registry and `pullPolicy`.

Default settings:

- `tag: '2.7.1'`
- `pullPolicy: 'IfNotPresent'`

## Configuring the `service`

This section controls the name and type of the [Service](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/registry/templates/service.yaml).
These settings will be populated by [values.yaml](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/registry/values.yaml).

By default, the Service is configured as:

| Name             | Type    | Default    | Description |
|:---------------- |:-------:|:---------- |:----------- |
| `name`           | String  | `registry` | Configures the name of the service |
| `type`           | String  | `ClusterIP`| Configures the type of the service |
| `externalPort`   | Int     | `5000`     | Port exposed by the Service |
| `internalPort`   | Int     | `5000`     | Port utilized by the Pod to accept request from the service |
| `clusterIP`      | String  | `null`     | Allows one to configure a custom Cluster IP as necessary |
| `loadBalancerIP` | String  | `null`     | Allows one to configure a custom LoadBalancer IP address as necessary |

## Configuring the `ingress`

This section controls the registry ingress.

| Name              | Type    | Default | Description |
|:----------------- |:-------:|:------- |:----------- |
| `annotations`     | String  |         | This field is an exact match to the standard `annotations` for [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/). |
| `enabled`         | Boolean | `false` | Setting that controls whether to create ingress objects for services that support them. When `false` the `global.ingress.enabled` setting is used. |
| `tls.enabled`     | Boolean | `true`  | When set to `false`, you disable TLS for the Registry subchart. This is mainly useful for cases in which you cannot use TLS termination at ingress-level, like when you have a TLS-terminating proxy before the ingress controller. |
| `tls.serviceName` | String  | `redis` | The name of the Kubernetes TLS Secret that contains a valid certificate and key for the registry url. When not set, the `global.ingress.tls.secretName` is used instead. Defaults to not being set. |

## Configuring the `networkpolicy`

This section controls the registry
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
This configuration is optional and is used to limit egress and ingress of the registry to specific endpoints.
and ingress to specific endpoints.

| Name              | Type    | Default | Description |
|:----------------- |:-------:|:------- |:----------- |
| `enabled`         | Boolean | `false` | This setting enables the networkpolicy for registry |
| `ingress.enabled` | Boolean | `false` | When set to `true`, the `Ingress` network policy will be activated. This will block all ingress connections unless rules are specified. |
| `ingress.rules`   | Array   | `[]`    | Rules for the ingress policy, for details see <https://kubernetes.io/docs/concepts/services-networking/network-policies/#the-networkpolicy-resource> and the example below |
| `egress.enabled`  | Boolean | `false` | When set to `true`, the `Egress` network policy will be activated. This will block all egress connections unless rules are specified. |
| `egress.rules`    | Array   | `[]`    | Rules for the egress policy, these for details see <https://kubernetes.io/docs/concepts/services-networking/network-policies/#the-networkpolicy-resource> and the example below |

### Example policy for preventing connections to all internal endpoints

The Registry service normally requires egress connections to object storage,
ingress connections from docker clients, and kube-dns for DNS lookups. This
adds the following network restrictions to the Registry service:

- All egress requests to the local network on `10.0.0.0/8` port 53 are allowed (for kubeDNS)
- Other egress requests to the local network on `10.0.0.0/8` are restricted
- Egress requests outside of the `10.0.0.0/8` are allowed

_Note that the registry service requires outbound connectivity to the public
internet for images on [external object storage](../../advanced/external-object-storage)_

```yaml
networkpolicy:
  enabled: true
  egress:
    enabled: true
    # The following rules enable traffic to all external
    # endpoints, except the local
    # network (except DNS requests)
    rules:
      - to:
        - ipBlock:
            cidr: 10.0.0.0/8
        ports:
        - port: 53
          protocol: UDP
      - to:
        - ipBlock:
            cidr: 0.0.0.0/0
            except:
            - 10.0.0.0/8
```

## Defining the Registry Configuration

The following properties of this chart pertain to the configuration of the underlying
[registry](https://hub.docker.com/_/registry/) container. Only the most critical values
for integration with GitLab are exposed. For this integration, we make use of the `auth.token.x`
settings of [Docker Distribution](https://github.com/docker/distribution), controlling
authentication to the registry via JWT [authentication tokens](https://docs.docker.com/registry/spec/auth/token/).

### httpSecret

Field `httpSecret` is a map that contains two items: `secret` and `key`.

The content of the key this references correlates to the `http.secret` value of
[registry](https://hub.docker.com/_/registry/). This value should be populated with
a cryptographically generated random string.

The `shared-secrets` job will automatically create this secret if not provided. It will be
filled with a securely generated 128 character alpha-numeric string that is base64 encoded.

To create this secret manually:

```sh
kubectl create secret generic gitlab-registry-httpsecret --from-literal=secret=strongrandomstring
```

### authEndpoint

The `authEndpoint` field is a string, providing the URL to the GitLab instance(s) that
the [registry](https://hub.docker.com/_/registry/) will authenticate to.

The value should include the protocol and hostname only. The chart template will automatically
append the necessary request path. The resulting value will be populated to `auth.token.realm`
inside the container. For example: `authEndpoint: "https://gitlab.example.com"`

By default this field is populated with the GitLab hostname configuration set by the
[Global Settings](../globals.md).

### certificate

The `certificate` field is a map containing two items: `secret` and `key`.

`secret` is a string containing the name of the [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/)
that houses the certificate bundle to be used to verify the tokens created by the GitLab instance(s).

`key` is the name of the `key` in the `Secret` which houses the certificate
bundle that will be provided to the [registry](https://hub.docker.com/_/registry/)
container as `auth.token.rootcertbundle`.

Default Example:

```yaml
certificate:
  secret: gitlab-registry
  key: registry-auth.crt
```

### compatibility

The `compatibility` field is a map relating directly to the configuration file's
[compatiblity](https://github.com/docker/distribution/blob/master/docs/configuration.md#compatibility)
section.

Default contents:

```yaml
compatibility:
  schema1:
    enabled: false
```

### readiness and liveness probe

By default there is a readiness and liveness probe configured to
check `/debug/health` on port `5001` which is the debug port.

#### schema1

The `schema1` section controls the compatibility of the service with version 1
of the Docker manifest schema. This setting is provide as a means of supporting
Docker clients earlier than `1.10`, after which schema v2 is used by default.

If you _must_ support older verions of Docker clients, you can do so by setting
`registry.compatbility.schema1.enabled: true`.

### validation

The `validation` field is a map that controls the docker image validation
process in the registry. When image validation is enabled the registry rejects
windows images with foreign layers.

The image validation is turned off by default.

To enable image validation you need to explicitly set `registry.validation.disabled: false`.

### hpa

The `hpa` field is an object, controlling the number of [registry](https://hub.docker.com/_/registry/)
instances to create as a part of the set. This defaults to a `minReplicas` value
of `2`, a `maxReplicas` value of 10, and configures the
`cpu.targetAverageUtilization` to 75%.

### storage

```yaml
storage:
  secret:
  key: config
  extraKey:
```

The `storage` field is a reference to a Kubernetes Secret and associated key. The content
of this secret is taken directly from [Registry Configuration: `storage`](https://docs.docker.com/registry/configuration/#storage).
Please refer to that documentation for more details.

Examples for [AWS s3](https://docs.docker.com/registry/storage-drivers/s3/) and
[Google GCS](https://docs.docker.com/registry/storage-drivers/gcs/) drivers can be
found in [examples/objectstorage](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage):

- [registry.s3.yaml](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/registry.s3.yaml)
- [registry.gcs.yaml](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/objectstorage/registry.gcs.yaml)

Place the *contents* of the `storage` block into the secret, and provide the following
as items to the `storage` map:

- `secret`: name of the Kubernetes Secret housing the YAML block.
- `key`: name of the key in the secret to use. Defaults to `config`.
- `extraKey`: *(optional)* name of an extra key in the secret, which will be mounted
  to `/etc/docker/registry/storage/${extraKey}` within the container. This can be
  used to provide the `keyfile` for the `gcs` driver.

```bash
# Example using S3
kubectl create secret generic registry-storage \
    --from-file=config=registry-storage.yaml

# Example using GCS with JSON key
# - Note: `registry.storage.extraKey=gcs.json`
kubectl create secret generic registry-storage \
    --from-file=config=registry-storage.yaml \
    --from-file=gcs.json=example-project-382839-gcs-bucket.json
```

If you chose to use the `filesystem` driver:

- You will need to provide persistent volumes for this data.
- [hpa.minReplicas](#hpa) should be set to `1`
- [hpa.maxReplicas](#hpa) should be set to `1`

For the sake of resiliency and simplicity, it is recommended to make use of an
external service, such as `s3`, `gcs`, `azure` or other compatible Object Storage.

NOTE: **Note:** The chart will populate `delete.enabled: true` into this configuration
  by default if not specified by the user. This keeps expected behavior in line with
  the default use of Minio, as well as the Omnibus GitLab. Any user provided value
  will supersede this default.

### debug

The debug port is enabled by default and is used for the liveness/readiness
probe. Additionally, prometheus metrics can be enabled.

```yaml
debug:
  addr:
    port: 5001
  prometheus:
    enabled: true
    path: '/metrics'
```

### health

The `health` property is optional, and contains preferences for
a periodic health check on the storage driver's backend storage.
For more details, see Docker's [configuration documentation](https://docs.docker.com/registry/configuration/#health).

```
health:
  storagedriver:
    enabled: false
    interval: 10s
    threshold: 3
```

## Garbage Collection

The Docker Registry will build up extraneous data over time which can be freed using
[garbage collection](https://docs.docker.com/registry/garbage-collection/).
As of [now](https://gitlab.com/gitlab-org/charts/gitlab/issues/1586) there is no
fully automated or scheduled way to run the garbage collection with this Chart.

### Manual Garbage Collection

Manual garbage collection requires the registry to be in read-only mode first. Let's assume that you've already
installed the GitLab Chart using Helm, named it `mygitlab` and installed it in the namespace `gitlabns`.
Replace these values in the commands below according to your actual configuration.

```bash
# Because of https://github.com/helm/helm/issues/2948 we can't rely on --reuse-values, so let's get our current config.
helm get config mygitlab > mygitlab.yml
# Upgrade Helm installation and configure the registry to be read-only.
# The --wait parameter makes Helm wait until all ressources are in ready state, so we are safe to continue.
helm upgrade mygitlab gitlab/gitlab -f mygitlab.yml --set registry.readOnly.enabled=true --wait
# Our registry is in r/o mode now, so let's get the name of one of the registry Pods.
# Note down the Pod name and replace the '<registry-pod>' placeholder below with that value.
# Replace the single quotes to double quotes (' => ") if you are using this with Windows' cmd.exe.
kubectl get pods -n gitlabns -l app=registry -o jsonpath='{.items[0].metadata.name}'
# Run the actual garbage collection. Check the registry's manual if you really want the '-m' parameter.
kubectl exec -n gitlabns <registry-pod> -- /bin/registry garbage-collect -m /etc/docker/registry/config.yml
# Reset registry back to original state.
helm upgrade mygitlab gitlab/gitlab -f mygitlab.yml --wait
# All done :)
```
