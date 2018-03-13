# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter              | Description                                 | Default        |
| ---                    | ---                                         | ---            |
| image.repository       | Redis image repository                      | redis          |
| image.tag              | Redis image tag                             | 3.2.5          |
| image.pullPolicy       | Redis image pull policy                     | IfNotPresent   |
| service.name           | Redis service name                          | redis          |
| service.type           | Redis service type                          | ClusterIP      |
| service.externalPort   | Redis internal port                         | 6379           |
| service.internalPort   | Redis exposed port                          | 6379           |
| service.clusterIP      | Cluster IP                                  | 0.0.0.0        |
| replicas               | Number of replicas                          | 1              |
| enabled                | Enable flag for the chart                   | true           |
| timeout                | Timeout in seconds                          | 60             |
| tcpKeepalive           | Keep alive in seconds                       | 300            |
| loglevel               | Log verbosity                               | notice         |
| password.secret        | Secret name                                 | gitlab-redis   |
| password.key           | Key to password in the secret               | redis-password |
| persistence.enabled    | Enable persistence flag                     | true           |
| persistence.accessMode | Redis access mode                           | ReadWriteOnce  |
| persistence.size       | Size of volume needed for redis persistence | 5Gi            |
| persistence.subPath    | Subpath to mount persistence volume at      |                |
