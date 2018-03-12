# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                        | Description                                    | Default                                        |
| ---                              | ---                                            | ---                                            |
| migrations.image.repository      | Migrations image repository                    | registry.com/gitlab-org/build/cng/gitlab-rails |
| migrations.image.tag             | Migrations image tag                           | latest                                         |
| migrations.image.pullPolicy      | Migrations pull policy                         | Always                                         |
| migrations.enabled               | Migrations enable flag                         | true                                           |
| migrations.redis.serviceName     | Redis service name                             | redis                                          |
| migrations.redis.password.secret | Redis secret                                   | gitlab-redis                                   |
| migrations.redis.password.key    | Key to redis password in redis secret          | redis-password                                 |
| migrations.psql.serviceName      | psql service name                              | omnibus                                        |
| migrations.psql.password.secret  | psql secret                                    | gitlab-postgres                                |
| migrations.psql.password.key     | key to psql password in psql secret            | psql-password                                  |
| migrations.railsSecrets.secret   | Secret containing rails secrets.yml            | rails-secrets                                  |
| migrations.railsSecrets.key      | Key to contents of secrets.yml in rails secret | secrets.yml                                    |
| migrations.initialRootPassword   | Password to the gitlab root account            | Required                                       |

