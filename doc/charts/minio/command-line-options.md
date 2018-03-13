# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                 | Description                         | Default                      |
| ---                       | ---                                 | ---                          |
| image                     | Minio image                         | minio/minio                  |
| imageTag                  | Minio image tag                     | RELEASE.2017-12-28T01-21-00Z |
| imagePullPolicy           | Minio image pull policy             | Always                       |
| enabled                   | Minio enable flag                   | true                         |
| credentials.secret        | Minio credentials secret            | gitlab-minio                 |
| mountPath                 | Minio config file mount path        | /export                      |
| replicas                  | Minio number of replicas            | 4                            |
| persistence.enabled       | Minio enable persistence flag       | true                         |
| persistence.accessMode    | Minio persistence access mode       | ReadWriteOnce                |
| persistence.size          | Minio persistence volume size       | 10Gi                         |
| persistence.subPath       | Minio persistence volume mount path |                              |
| serviceType               | Minio service type                  | ClusterIP                    |
| servicePort               | Minio service port                  | 9000                         |
| resources.requests.memory | Minio minimum memory requested      | 256Mi                        |
| resources.requests.cpu    | Minio minimum cpu requested         | 250m                         |
| defaultBuckets            | Minio default buckets               | [{"name": "registry"}]       |
| minioConfig.region        | Minio region                        | us-east-1                    |
| minioConfig.browser       | Minio browser flag                  | on                           |
| minioConfig.domain        | Minio domain                        |                              |
