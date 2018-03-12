# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                     | Description                            | Default                                  |
| ---                           | ---                                    | ---                                      |
| gitaly.replicaCount           | Gitaly replicas                        | 1                                        |
| gitaly.image.repository       | Gitaly image repository                | registry.com/gitlab-org/build/cng/gitaly |
| gitaly.image.tag              | Gitaly image tag                       | latest                                   |
| gitaly.image.pullPolicy       | Gitaly image pull policy               | Always                                   |
| gitaly.service.name           | Gitaly service name                    | gitaly                                   |
| gitaly.service.type           | Gitaly service type                    | ClusterIP                                |
| gitaly.service.externalPort   | Gitaly service exposed port            | 8075                                     |
| gitaly.service.internalPort   | Gitaly internal port                   | 8075                                     |
| gitaly.enabled                | Gitaly enable flag                     | true                                     |
| gitaly.serviceName            | Gitaly service name                    | gitaly                                   |
| gitaly.authToken.secret       | Gitaly secret name                     | gitaly-secret                            |
| gitaly.authToken.key          | Key to gitaly token in the secret      | token                                    |
| gitaly.redis.password.secret  | Redis secret containing redis password | gitlab-redis                             |
| gitaly.redis.password.key     | Key to redis password in redis secret  | redis-password                           |
| gitaly.shell.authToken.secret | Shell secret                           | gitlab-shell-secret                      |
| gitaly.shell.authToken.key    | Shell key                              | secret                                   |
| gitaly.persistence.enabled    | Gitaly enable persistence flag         | true                                     |
| gitaly.persistence.accessMode | Gitaly persistence access mode         | ReadWriteOnce                            |
| gitaly.persistence.size       | Gitaly persistence volume size         | 50Gi                                     |
| gitaly.persistence.subPath    | Gitaly persistence volume mount path   |                                          |

