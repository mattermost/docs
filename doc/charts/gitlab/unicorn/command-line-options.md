# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                     | Description                                    | Default                                          |
| ---                           | ---                                            | ---                                              |
| replicaCount                  | Unicorn number of replicas                     | 1                                                |
| image.repository              | Unicorn image repository                       | registry.com/gitlab-org/build/cng/gitlab-unicorn |
| image.tag                     | Unicorn image tag                              | latest                                           |
| image.pullPolicy              | Unicorn image pull policy                      | Always                                           |
| service.name                  | Unicorn service name                           | unicorn                                          |
| service.type                  | Unicorn service type                           | ClusterIP                                        |
| service.externalPort          | Unicorn exposed port                           | 8080                                             |
| service.internalPort          | Unicorn internal port                          | 8080                                             |
| service.workhorseExternalPort | Workhorse exposed port                         | 8181                                             |
| service.workhorseInternalPort | Workhorse internal port                        | 8181                                             |
| enabled                       | Unicorn enabled flag                           | true                                             |
| workerProcesses               | Unicorn number of workers                      | 2                                                |
| workerTimeout                 | Unicorn worker timeout                         | 60                                               |
| railsSecrets.secret           | Secret containing rails secrets.yml            | rails-secrets                                    |
| railsSecrets.key              | Key to contents of secrets.yml in rails secret | secrets.yml                                      |
| redis.serviceName             | Redis service name                             | redis                                            |
| redis.password.secret         | Redis secret                                   | gitlab-redis                                     |
| redis.password.key            | Key to redis password in redis secret          | redis-password                                   |
| psql.serviceName              | psql service name                              | omnibus                                          |
| psql.password.secret          | psql secret name                               | gitlab-postgres                                  |
| psql.password.key             | Key to psql password in psql secret            | psql-password                                    |
| shell.authToken.secret        | Shell token secret                             | gitlab-shell-secret                              |
| shell.authToken.key           | Key to shell token in shell secret             | secret                                           |
| gitaly.serviceName            | Gitaly service name                            | gitaly                                           |
| gitaly.authToken.secret       | Gitaly secret name                             | gitaly-secret                                    |
| gitaly.authToken.key          | Key to gitaly token in gitaly secret           | token                                            |
| registry.api.protocol         | Registry protocol                              | http                                             |
| registry.api.serviceName      | Registry service name                          | registry                                         |
| registry.api.port             | Registry port                                  | 5000                                             |
| registry.tokenIssuer          | Registry token issuer                          | gitlab-issuer                                    |
| registry.certificate.secret   | Registry certificate                           | gitlab-registry                                  |
| registry.certificate.key      | Registry certificate key                       | registry-auth.key                                |
| resources.requests.cpu        | Unicorn minimum cpu                            | 200m                                             |
| resources.requests.memory     | Unicorn minimum memory                         | 1.4G                                             |
