# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter             | Description                                    | Default                                        |
| ---                   | ---                                            | ---                                            |
| image.repository      | Migrations image repository                    | registry.com/gitlab-org/build/cng/gitlab-rails |
| image.tag             | Migrations image tag                           | latest                                         |
| image.pullPolicy      | Migrations pull policy                         | Always                                         |
| enabled               | Migrations enable flag                         | true                                           |
| redis.serviceName     | Redis service name                             | redis                                          |
| redis.password.secret | Redis secret                                   | gitlab-redis                                   |
| redis.password.key    | Key to redis password in redis secret          | redis-password                                 |
| psql.serviceName      | psql service name                              | omnibus                                        |
| psql.password.secret  | psql secret                                    | gitlab-postgres                                |
| psql.password.key     | key to psql password in psql secret            | psql-password                                  |
| railsSecrets.secret   | Secret containing rails secrets.yml            | rails-secrets                                  |
| railsSecrets.key      | Key to contents of secrets.yml in rails secret | secrets.yml                                    |
| initialRootPassword   | Password to the gitlab root account            | Required                                       |
