# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter              | Description                            | Default                                  |
| ---                    | ---                                    | ---                                      |
| replicaCount           | Gitaly replicas                        | 1                                        |
| image.repository       | Gitaly image repository                | registry.com/gitlab-org/build/cng/gitaly |
| image.tag              | Gitaly image tag                       | latest                                   |
| image.pullPolicy       | Gitaly image pull policy               | Always                                   |
| service.name           | Gitaly service name                    | gitaly                                   |
| service.type           | Gitaly service type                    | ClusterIP                                |
| service.externalPort   | Gitaly service exposed port            | 8075                                     |
| service.internalPort   | Gitaly internal port                   | 8075                                     |
| enabled                | Gitaly enable flag                     | true                                     |
| serviceName            | Gitaly service name                    | gitaly                                   |
| authToken.secret       | Gitaly secret name                     | gitaly-secret                            |
| authToken.key          | Key to gitaly token in the secret      | token                                    |
| redis.password.secret  | Redis secret containing redis password | gitlab-redis                             |
| redis.password.key     | Key to redis password in redis secret  | redis-password                           |
| shell.authToken.secret | Shell secret                           | gitlab-shell-secret                      |
| shell.authToken.key    | Shell key                              | secret                                   |
| persistence.enabled    | Gitaly enable persistence flag         | true                                     |
| persistence.accessMode | Gitaly persistence access mode         | ReadWriteOnce                            |
| persistence.size       | Gitaly persistence volume size         | 50Gi                                     |
| persistence.subPath    | Gitaly persistence volume mount path   |                                          |

