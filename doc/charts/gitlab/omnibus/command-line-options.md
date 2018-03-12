# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                           | Description                           | Default                                                           |
| ---                                 | ---                                   | ---                                                               |
| omnibus.replicaCount                | Omnibus replicas                      | 1                                                                 |
| omnibus.image.repository            | Omnibus image repository              | gitlab/gitlab-ee                                                  |
| omnibus.image.tag                   | Omnibus image tag                     | nightly                                                           |
| omnibus.image.pullPolicy            | Omnibus image pull policy             | Always                                                            |
| omnibus.service.name                | Omnibus service name                  | omnibus                                                           |
| omnibus.service.type                | Omnibus service type                  | ClusterIP                                                         |
| omnibus.service.clusterIP           | Omnibus cluster IP                    | 0.0.0.0                                                           |
| omnibus.service.ports.psql          | Omnibus psql port                     | 5432                                                              |
| omnibus.enabled                     | Omnibus enable flag                   | true                                                              |
| omnibus.external_url                | Omnibus external url                  | http://example.local                                              |
| omnibus.trusted_proxies             |                                       | ["127.0.0.1/24", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"] |
| omnibus.redis.serviceName           | Redis service name                    | redis                                                             |
| omnibus.redis.password.secret       | Redis secret                          | gitlab-redis                                                      |
| omnibus.redis.password.key          | Key to redis password in redis secret | redis-password                                                    |
| omnibus.psql.shared_buffers         | Size of psql shared buffers           | 1MB                                                               |
| omnibus.psql.password.secret        | Secret containing psql password       | gitlab-postgres                                                   |
| omnibus.psql.password.key           | Key to psql password in psql secret   | psql-password                                                     |
| omnibus.psql.persistence.enabled    | psql persistence enabled flag         | true                                                              |
| omnibus.psql.persistence.accessMode | psql persistence access mode          | ReadWriteOnce                                                     |
| omnibus.psql.persistence.size       | psql persistence volume size          | 10Gi                                                              |
| omnibus.psql.persistence.subPath    | psql persistence volume mountpath     |                                                                   |

