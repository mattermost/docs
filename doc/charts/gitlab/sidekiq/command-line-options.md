# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                         | Description                                    | Default                                          |
| ---                               | ---                                            | ---                                              |
| sidekiq.image.repository          | Sidekiq image repository                       | registry.com/gitlab-org/build/cng/gitlab-sidekiq |
| sidekiq.image.tag                 | Sidekiq image tag                              | latest                                           |
| sidekiq.image.pullPolicy          | Sidekiq image pull policy                      | Always                                           |
| sidekiq.enabled                   | Sidekiq enabled flag                           | true                                             |
| sidekiq.redis.serviceName         | Redis service name                             | redis                                            |
| sidekiq.redis.password.secret     | Redis secret                                   | gitlab-redis                                     |
| sidekiq.redis.password.key        | Key to redis password in redis secret          | redis-password                                   |
| sidekiq.psql.serviceName          | psql service name                              | omnibus                                          |
| sidekiq.psql.password.secret      | psql password secret                           | gitlab-postgres                                  |
| sidekiq.psql.password.key         | key to psql password in psql secret            | psql-password                                    |
| sidekiq.gitaly.serviceName        | gitaly service name                            | gitaly                                           |
| sidekiq.gitaly.authToken.secret   | gitaly secret                                  | gitaly-secret                                    |
| sidekiq.gitaly.authToken.key      | key to gitaly token in gitaly secret           | token                                            |
| sidekiq.replicas                  | Sidekiq replicas                               | 1                                                |
| sidekiq.railsSecrets.secret       | Secret containing rails secrets.yml            | rails-secrets                                    |
| sidekiq.railsSecrets.key          | Key to contents of secrets.yml in rails secret | secrets.yml                                      |
| sidekiq.concurrency               | Sidekiq default concurrency                    | 10                                               |
| sidekiq.timeout                   | Sidekiq job timeout                            | 5                                                |
| sidekiq.resources.requests.cpu    | Sidekiq minimum needed cpu                     | 100m                                             |
| sidekiq.resources.requests.memory | Sidekiq minimum needed memory                  | 600M                                             |

