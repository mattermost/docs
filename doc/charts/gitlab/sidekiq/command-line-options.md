# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                 | Description                                    | Default                                          |
| ---                       | ---                                            | ---                                              |
| image.repository          | Sidekiq image repository                       | registry.com/gitlab-org/build/cng/gitlab-sidekiq |
| image.tag                 | Sidekiq image tag                              | latest                                           |
| image.pullPolicy          | Sidekiq image pull policy                      | Always                                           |
| enabled                   | Sidekiq enabled flag                           | true                                             |
| redis.serviceName         | Redis service name                             | redis                                            |
| redis.password.secret     | Redis secret                                   | gitlab-redis                                     |
| redis.password.key        | Key to redis password in redis secret          | redis-password                                   |
| psql.serviceName          | psql service name                              | omnibus                                          |
| psql.password.secret      | psql password secret                           | gitlab-postgres                                  |
| psql.password.key         | key to psql password in psql secret            | psql-password                                    |
| gitaly.serviceName        | gitaly service name                            | gitaly                                           |
| gitaly.authToken.secret   | gitaly secret                                  | gitaly-secret                                    |
| gitaly.authToken.key      | key to gitaly token in gitaly secret           | token                                            |
| replicas                  | Sidekiq replicas                               | 1                                                |
| railsSecrets.secret       | Secret containing rails secrets.yml            | rails-secrets                                    |
| railsSecrets.key          | Key to contents of secrets.yml in rails secret | secrets.yml                                      |
| concurrency               | Sidekiq default concurrency                    | 10                                               |
| timeout                   | Sidekiq job timeout                            | 5                                                |
| resources.requests.cpu    | Sidekiq minimum needed cpu                     | 100m                                             |
| resources.requests.memory | Sidekiq minimum needed memory                  | 600M                                             |
