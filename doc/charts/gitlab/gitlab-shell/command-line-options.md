# Using the GitLab-Shell chart

The `gitlab-shell` sub-chart provides a SSH server configured for Git SSH access to GitLab.

| Parameter             | Description                           | Default                                        |
| ---                   | ---                                   | ---                                            |
| replicaCount          | Shell replicas                        | 1                                              |
| image.repository      | Shell image repository                | registry.com/gitlab-org/build/cng/gitlab-shell |
| image.tag             | Shell image tag                       | latest                                         |
| image.pullPolicy      | Shell image pull policy               | Always                                         |
| service.name          | Shell service name                    | gitlab-shell                                   |
| service.type          | Shell service type                    | ClusterIP                                      |
| service.externalPort  | Shell exposed port                    | 22                                             |
| service.internalPort  | Shell internal port                   | 22                                             |
| enabled               | Shell enable flag                     | true                                           |
| authToken.secret      | Shell auth secret                     | gitlab-shell-secret                            |
| authToken.key         | Shell auth secret key                 | secret                                         |
| unicorn.serviceName   | Unicorn service name                  | unicorn                                        |
| redis.serviceName     | Redis service name                    | redis                                          |
| redis.password.secret | Redis secret                          | gitlab-redis                                   |
| redis.password.key    | Key to redis password in redis secret | redis-password                                 |

