# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                             | Description                                    | Default                                          |
| ---                                   | ---                                            | ---                                              |
| unicorn.replicaCount                  | Unicorn number of replicas                     | 1                                                |
| unicorn.image.repository              | Unicorn image repository                       | registry.com/gitlab-org/build/cng/gitlab-unicorn |
| unicorn.image.tag                     | Unicorn image tag                              | latest                                           |
| unicorn.image.pullPolicy              | Unicorn image pull policy                      | Always                                           |
| unicorn.service.name                  | Unicorn service name                           | unicorn                                          |
| unicorn.service.type                  | Unicorn service type                           | ClusterIP                                        |
| unicorn.service.externalPort          | Unicorn exposed port                           | 8080                                             |
| unicorn.service.internalPort          | Unicorn internal port                          | 8080                                             |
| unicorn.service.workhorseExternalPort | Workhorse exposed port                         | 8181                                             |
| unicorn.service.workhorseInternalPort | Workhorse internal port                        | 8181                                             |
| unicorn.enabled                       | Unicorn enabled flag                           | true                                             |
| unicorn.workerProcesses               | Unicorn number of workers                      | 2                                                |
| unicorn.workerTimeout                 | Unicorn worker timeout                         | 60                                               |
| unicorn.railsSecrets.secret           | Secret containing rails secrets.yml            | rails-secrets                                    |
| unicorn.railsSecrets.key              | Key to contents of secrets.yml in rails secret | secrets.yml                                      |
| unicorn.redis.serviceName             | Redis service name                             | redis                                            |
| unicorn.redis.password.secret         | Redis secret                                   | gitlab-redis                                     |
| unicorn.redis.password.key            | Key to redis password in redis secret          | redis-password                                   |
| unicorn.psql.serviceName              | psql service name                              | omnibus                                          |
| unicorn.psql.password.secret          | psql secret name                               | gitlab-postgres                                  |
| unicorn.psql.password.key             | Key to psql password in psql secret            | psql-password                                    |
| unicorn.shell.authToken.secret        | Shell token secret                             | gitlab-shell-secret                              |
| unicorn.shell.authToken.key           | Key to shell token in shell secret             | secret                                           |
| unicorn.gitaly.serviceName            | Gitaly service name                            | gitaly                                           |
| unicorn.gitaly.authToken.secret       | Gitaly secret name                             | gitaly-secret                                    |
| unicorn.gitaly.authToken.key          | Key to gitaly token in gitaly secret           | token                                            |
| unicorn.registry.api.protocol         | Registry protocol                              | http                                             |
| unicorn.registry.api.serviceName      | Registry service name                          | registry                                         |
| unicorn.registry.api.port             | Registry port                                  | 5000                                             |
| unicorn.registry.tokenIssuer          | Registry token issuer                          | gitlab-issuer                                    |
| unicorn.registry.certificate.secret   | Registry certificate                           | gitlab-registry                                  |
| unicorn.registry.certificate.key      | Registry certificate key                       | registry-auth.key                                |
| unicorn.resources.requests.cpu        | Unicorn minimum cpu                            | 200m                                             |
| unicorn.resources.requests.memory     | Unicorn minimum memory                         | 1.4G                                             |

