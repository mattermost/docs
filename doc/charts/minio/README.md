# Using Minio for Object storage

This chartis based on [`stable/minio`][minio-chart] version [`0.4.3`][minio-043], and inherits most settings from there.

The documentation for the upstream chart can be found [here][minio-043].

## Design Choices

Design choices related to the [upstream chart][minio-chart] can be found in their README.

GitLab chose to alter that chart in order to simplify configuration of the secrets, and to remove all use of secrets in environment variables. GitLab added `initContainer`s to control the population of secrets into the `config.json` and a chart-wide `enabled` flag.

This chart makes use of only one secret:
- `global.minio.credentials.secret`: A global secret containing the `accesskey` and `secretkey` values that will be used for authentication to the bucket(s).

# Configuration

We will describe all the major sections of the configuration below. When configuring from the parent chart, these values will be as such:

```
minio:
  init:
  ingress:
    enabled:
    tls:
      secretName
    annotations:
    proxyReadTimeout:
    proxyBodySize:
    proxyBuffering:
  persistence: (upstream)
    volumeName:
    matchLabels:
    matchExpressions:
  serviceType: (upstream)
  servicePort: (upstream)
  defaultBuckets:
  minioConfig: (upstream)
```

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                    | Description                             | Default                      |
| ---                          | ---                                     | ---                          |
| image                        | Minio image                             | minio/minio                  |
| imageTag                     | Minio image tag                         | RELEASE.2017-12-28T01-21-00Z |
| imagePullPolicy              | Minio image pull policy                 | Always                       |
| pullSecrets                  | Secrets for the image repository        |                              |
| mountPath                    | Minio config file mount path            | /export                      |
| replicas                     | Minio number of replicas                | 4                            |
| minioMc.image                | Minio mc image                          | minio/mc                     |
| minioMc.tag                  | Minio mc image tag                      | latest                       |
| persistence.enabled          | Minio enable persistence flag           | true                         |
| persistence.accessMode       | Minio persistence access mode           | ReadWriteOnce                |
| persistence.size             | Minio persistence volume size           | 10Gi                         |
| persistence.subPath          | Minio persistence volume mount path     |                              |
| persistence.storageClass     | Minio storageClassName for provisioning |                              |
| persistence.volumeName       | Minio existing persistent volume name   |                              |
| persistence.matchLabels      | Minio label-value matches to bind       |                              |
| persistence.matchExpressions | Minio label-expression matches to bind  |                              |
| serviceType                  | Minio service type                      | ClusterIP                    |
| servicePort                  | Minio service port                      | 9000                         |
| resources.requests.memory    | Minio minimum memory requested          | 256Mi                        |
| resources.requests.cpu       | Minio minimum cpu requested             | 250m                         |
| defaultBuckets               | Minio default buckets                   | [{"name": "registry"}]       |
| minioConfig.region           | Minio region                            | us-east-1                    |
| minioConfig.browser          | Minio browser flag                      | on                           |
| minioConfig.domain           | Minio domain                            |                              |

## Chart configuration examples
### pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image: my.minio.repository
imageTag: latest
imagePullPolicy: Always
pullSecrets:
- name: my-secret-name
- name: my-secondary-secret-name
```

## Enable the sub-chart

They way we've chosen to implement compartmentalized sub-charts includes the ability to disable the components that you may not want in a given deployment. For this reason, the first settings you should decided upon is `enabled:`.

By default, Minio is enabled out of the box. Minio is not recommended for production use.
When you are ready to disable it, `--set global.minio.enabled: false`.

## Configure the initContainer

While rarely altered, the `initContainer` behaviors can be changed via the following items.

```
init:
  image: busybox
  tag: latest
  pullPolicy: IfNotPresent
  script:
```

### initContainer image

The initContainer image settings are just as with a normal image configuration. The defaults are provided [above](#configure-the-initcontainer).

### initContainer script

The initContainer is handed the following items:
- The secret containing authentication items mounted in `/config`, usually `accesskey` and `secretkey`
- The ConfigMap containing the `config.json` template and `configure` containing a script to be executed with `sh`, mounted in `/config`
- An `emptyDir` mounted at `/minio` that will be passed to the daemon's container.

The initContainer is expected to populate `/minio/config.json` with a completed configuration, using `/config/configure` script. When the `minio-config` container has completed that task, the `/minio` directory will be passed to the `minio` container, and used to provide the `config.json` to the [minio][] server.

## Configuring the Ingress

This section controls the minio ingress.

### enabled

Setting that controls whether to create ingress objects for services that support them.

When `false` the `global.ingress.enabled` setting is used.

Defaults to `false`.

### tls.secretName

The name of the Kubernetes TLS Secret that contains a valid certificate and key for the minio url.

When not set, the `global.ingress.tls.secretName` is used instead.

Defaults to not being set.

### annotations

This field is an exact match to the standard `annotations` for [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress).

## Configuring the image

The `image`, `imageTag` and `imagePullPolicy` defaults are [documented upstream][minio-config].

## Persistence

The behaviors for [`persistence`][minio-persistence] are [documented upstream][minio-config]. The key summary is:

> This chart provisions a PersistentVolumeClaim and mounts corresponding persistent volume to default location /export. You'll need physical storage available in the Kubernetes cluster for this to work. If you'd rather use emptyDir, disable PersistentVolumeClaim by: `persitence.enabled: false`

GitLab has added a few items:

```
persistence:
  volumeName:
  matchLabels:
  matchExpressions:
```

### volumeName

When `volumeName` is provided, the `PersistentVolumeClaim` will use the provided `PersistentVolume` by name, in place of creating a `PersistentVolume` dynamically. This overrides the upstream behavior.

### matchLabels

`matchLabels` accepts a dictionary of label name and label values to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

### matchExpressions

`matchExpressions` accepts an array of label condition objects to match against when choosing a volume to bind. This is used in the `PersistentVolumeClaim` `selector` section. See the [volumes documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector)

## defaultBuckets

`defaultBuckets` provides a mechanism to automatically create buckets on the Minio pod at _installation_. This property contains an array of items, each with up to three properties: `name`, `policy`, and `purge`.

```
defaultBuckets:
  - name: public
    policy: public
    purge: true
  - name: private
  - name: public-read
    policy: download
```

### name

The value of `name` will be the name of the bucket that is created. The provided value should conform to [AWS ucket naming rules][bucket-naming], meaning that it should be compliant with DNS and contain only the characters a-z, 0-9, and – (hyphen) in strings between 3 and 63 characters in length.

The `name` property is _required_ for all entries.

### policy

The value of `policy` controlls the policy of the bucket on Minio.

Possible values are listed below, with description in regards to **anonymous** access:
- `none`: no anonymous access
- `download`: anonymous read-only access
- `upload`: anonymounts write-only access
- `public`: anonymous read/write access

The `policy` property is not required, and default value is `none`.

### purge

The `purge` property is provided as a means to cause any existing bucket to be removed with force, at installation time. This only comes into play when using a pre-existing `PersistentVolume` for the [volumeName](#volumeName) property of [persistence](#persistence). If you make use of a dynamically created `PersistentVolume`, this will have no valuable affect as it only happens at chart installation and there will be no data in the `PersistentVolume` that was just created.

This property is not required, and the default value is `false`. You may specify this property, with a value of `true`, in order to cause a bucket to purged with force: `mc rm -r --force`

## Service Type and Port

These are [documented upstream][minio-config], and the key summary is:
```
## Expose the Minio service to be accessed from outside the cluster (LoadBalancer service).
## or access it from within the cluster (ClusterIP service). Set the service type and the port to serve it.
## ref: http://kubernetes.io/docs/user-guide/services/
##
serviceType: LoadBalancer
servicePort: 9000
```

The chart does not expect to be of the `type: NodePort`, so **do not** set it as such.

## Upstream items

The [upstream documentation][minio-chart] for the following applies completely to this chart.
- `resources`
- `nodeSelector`
- `minioConfig`

And further explanation for the `minioConfig` settings can be found in the [minio notify documentation](https://docs.minio.io/docs/minio-bucket-notification-guide).
This includes details on publishing notifications when Bucket Objects are accessed or changed.

[minio]: https://minio.io
[minio-chart]: https://github.com/kubernetes/charts/tree/master/stable/minio
[minio-043]: https://github.com/kubernetes/charts/tree/aaaf98b5d25c26cc2d483925f7256f2ce06be080/stable/minio
[minio-config]: https://github.com/kubernetes/charts/tree/master/stable/minio#configuration
[minio-persistence]: https://github.com/kubernetes/charts/tree/master/stable/minio#persistence
[bucket-naming]: https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html
