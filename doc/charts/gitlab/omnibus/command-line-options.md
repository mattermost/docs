# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                   | Description                           | Default                                                           |
| ---                         | ---                                   | ---                                                               |
| replicaCount                | Omnibus replicas                      | 1                                                                 |
| image.repository            | Omnibus image repository              | gitlab/gitlab-ee                                                  |
| image.tag                   | Omnibus image tag                     | nightly                                                           |
| image.pullPolicy            | Omnibus image pull policy             | Always                                                            |
| service.name                | Omnibus service name                  | omnibus                                                           |
| service.type                | Omnibus service type                  | ClusterIP                                                         |
| service.clusterIP           | Omnibus cluster IP                    | 0.0.0.0                                                           |
| service.ports.psql          | Omnibus psql port                     | 5432                                                              |
| enabled                     | Omnibus enable flag                   | true                                                              |
| external_url                | Omnibus external url                  | http://example.local                                              |
| trusted_proxies             |                                       | ["127.0.0.1/24", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"] |
| redis.serviceName           | Redis service name                    | redis                                                             |
| redis.password.secret       | Redis secret                          | gitlab-redis                                                      |
| redis.password.key          | Key to redis password in redis secret | redis-password                                                    |
| psql.shared_buffers         | Size of psql shared buffers           | 1MB                                                               |
| psql.password.secret        | Secret containing psql password       | gitlab-postgres                                                   |
| psql.password.key           | Key to psql password in psql secret   | psql-password                                                     |
| psql.persistence.enabled    | psql persistence enabled flag         | true                                                              |
| psql.persistence.accessMode | psql persistence access mode          | ReadWriteOnce                                                     |
| psql.persistence.size       | psql persistence volume size          | 10Gi                                                              |
| psql.persistence.subPath    | psql persistence volume mountpath     |                                                                   |
