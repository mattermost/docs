# Using the GitLab-Shell chart

The `gitlab-shell` sub-chart provides a SSH server configured for Git SSH access to GitLab.

| Parameter                          | Description                           | Default                                        |
| ---                                | ---                                   | ---                                            |
| gitlab-shell.replicaCount          | Shell replicas                        | 1                                              |
| gitlab-shell.image.repository      | Shell image repository                | registry.com/gitlab-org/build/cng/gitlab-shell |
| gitlab-shell.image.tag             | Shell image tag                       | latest                                         |
| gitlab-shell.image.pullPolicy      | Shell image pull policy               | Always                                         |
| gitlab-shell.service.name          | Shell service name                    | gitlab-shell                                   |
| gitlab-shell.service.type          | Shell service type                    | ClusterIP                                      |
| gitlab-shell.service.externalPort  | Shell exposed port                    | 22                                             |
| gitlab-shell.service.internalPort  | Shell internal port                   | 22                                             |
| gitlab-shell.enabled               | Shell enable flag                     | true                                           |
| gitlab-shell.authToken.secret      | Shell auth secret                     | gitlab-shell-secret                            |
| gitlab-shell.authToken.key         | Shell auth secret key                 | secret                                         |
| gitlab-shell.unicorn.serviceName   | Unicorn service name                  | unicorn                                        |
| gitlab-shell.redis.serviceName     | Redis service name                    | redis                                          |
| gitlab-shell.redis.password.secret | Redis secret                          | gitlab-redis                                   |
| gitlab-shell.redis.password.key    | Key to redis password in redis secret | redis-password                                 |

