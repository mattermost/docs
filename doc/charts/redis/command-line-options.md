# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                    | Description                                 | Default        |
| ---                          | ---                                         | ---            |
| redis.image.repository       | Redis image repository                      | redis          |
| redis.image.tag              | Redis image tag                             | 3.2.5          |
| redis.image.pullPolicy       | Redis image pull policy                     | IfNotPresent   |
| redis.service.name           | Redis service name                          | redis          |
| redis.service.type           | Redis service type                          | ClusterIP      |
| redis.service.externalPort   | Redis internal port                         | 6379           |
| redis.service.internalPort   | Redis exposed port                          | 6379           |
| redis.service.clusterIP      | Cluster IP                                  | 0.0.0.0        |
| redis.replicas               | Number of replicas                          | 1              |
| redis.enabled                | Enable flag for the chart                   | true           |
| redis.timeout                | Timeout in seconds                          | 60             |
| redis.tcpKeepalive           | Keep alive in seconds                       | 300            |
| redis.loglevel               | Log verbosity                               | notice         |
| redis.password.secret        | Secret name                                 | gitlab-redis   |
| redis.password.key           | Key to password in the secret               | redis-password |
| redis.persistence.enabled    | Enable persistence flag                     | true           |
| redis.persistence.accessMode | Redis access mode                           | ReadWriteOnce  |
| redis.persistence.size       | Size of volume needed for redis persistence | 5Gi            |
| redis.persistence.subPath    | Subpath to mount persistence volume at      |                |

