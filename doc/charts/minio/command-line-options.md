# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                       | Description                         | Default                      |
| ---                             | ---                                 | ---                          |
| minio.image                     | Minio image                         | minio/minio                  |
| minio.imageTag                  | Minio image tag                     | RELEASE.2017-12-28T01-21-00Z |
| minio.imagePullPolicy           | Minio image pull policy             | Always                       |
| minio.enabled                   | Minio enable flag                   | true                         |
| minio.credentials.secret        | Minio credentials secret            | gitlab-minio                 |
| minio.mountPath                 | Minio config file mount path        | /export                      |
| minio.replicas                  | Minio number of replicas            | 4                            |
| minio.persistence.enabled       | Minio enable persistence flag       | true                         |
| minio.persistence.accessMode    | Minio persistence access mode       | ReadWriteOnce                |
| minio.persistence.size          | Minio persistence volume size       | 10Gi                         |
| minio.persistence.subPath       | Minio persistence volume mount path |                              |
| minio.serviceType               | Minio service type                  | ClusterIP                    |
| minio.servicePort               | Minio service port                  | 9000                         |
| minio.resources.requests.memory | Minio minimum memory requested      | 256Mi                        |
| minio.resources.requests.cpu    | Minio minimum cpu requested         | 250m                         |
| minio.defaultBuckets            | Minio default buckets               | [{"name": "registry"}]       |
| minio.minioConfig.region        | Minio region                        | us-east-1                    |
| minio.minioConfig.browser       | Minio browser flag                  | on                           |
| minio.minioConfig.domain        | Minio domain                        |                              |

