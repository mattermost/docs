# Installation command line options

Tables below contain all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

## Basic configuration

| Parameter                                       | Description                                                                  | Default                                    |
| ---                                             | ---                                                                          | ---                                        |
| global.hosts.domain                             | Domain name that will be used for all publicly exposed services              | Required                                   |
| global.hosts.externalIP | Static IP to assign to nginx ingress controller                              | Required                                   |
| global.hosts.ssh                                | Domain name that will be used for git ssh access                             | gitlab.{global.hosts.domain}                                          |
| gitlab.migrations.initialRootPassword.secret    | Global name of the secret containing the root account password               | {Release.Name}-gitlab-initial-root-password |
| gitlab.migrations.initialRootPassword.key       | Key pointing to the root account password in the migrations secret           | password           |
| global.psql.host                                | Global hostname of an external psql, overrides subcharts' psql configuration | _Uses in-cluster non-production postgress_ |
| global.psql.password.secret                     | Global name of the secret containing the psql password                       | _Uses in-cluster non-production postgress_ |
| global.psql.password.key                        | Key pointing to the psql password in the psql secret                         | _Uses in-cluster non-production postgress_ |
| global.time_zone                                | Global time zone                                                             | UTC                                        |
| global.service.annotations                      | Annotations to add to every `Service`                                        | {}                     |
| global.registry.bucket                          | registry bucket name                    | registry             |
| global.application.create                       | Create an [Application resource](https://github.com/kubernetes-sigs/application) for GitLab                                    | false

## TLS configuration

| Parameter                                    | Description                                                       | Default                      |
| ---                                          | ---                                                               | ---                          |
| global.hosts.https                           | Serve over https                                                  | true                         |
| global.ingress.configureCertmanager          | Configure cert-manager to get certificates from Let's Encrypt     | true                         |
| certmanager-issuer.email                     | Email for Let's Encrypt account                                   | false                        |
| global.ingress.tls.secretName                | Existing `Secret` containing wildcard TLS certificate and key     | _none_                       |
| gitlab.unicorn.ingress.tls.secretName        | Existing `Secret` containing TLS certificate and key for gitlab   | _none_                       |
| minio.ingress.tls.secretName                 | Existing `Secret` containing TLS certificate and key for minio    | _none_                       |
| registry.ingress.tls.secretName              | Existing `Secret` containing TLS certificate and key for registry | _none_                       |

## Outgoing Email configuration

| Parameter                       | Description                                                                             | Default               |
| ---                             | ---                                                                                     | ---                   |
| global.smtp.enabled             | Enable outgoing email                                                                   | false                 |
| global.smtp.address             | Hostname or IP of the remote mail server                                                | smtp.mailgun.org      |
| global.smtp.port                | Port for SMTP                                                                           | 2525                  |
| global.smtp.user_name           | Username for SMTP authentication https                                                  | ""                    |
| global.smtp.password.secret     | Name of a `Secret` containing the SMTP password                                         | ""                    |
| global.smtp.password.key        | Key in `global.smtp.password.secret` that contains the SMTP password                    | password              |
| global.smtp.domain              | Optional HELO domain for SMTP                                                           | ""                    |
| global.smtp.authentication      | Type of SMTP authentication ("plain", "login", "cram_md5", or "" for no authentication) | plain                 |
| global.smtp.starttls_auto       | Use STARTTLS if enabled on the mail server                                              | false                 |
| global.smtp.openssl_verify_mode | TLS verification mode ("none", "peer", or "ssl/tls")                                    | peer                  |
| global.email.from               | Email address that appears as the sender for emails from GitLab                         | gitlab@example.com  |
| global.email.display_name       | Name that appears as the sender for emails from GitLab                                  | GitLab                |
| global.email.reply_to           | Reply-to email listed in emails from GitLab                                             | noreply@example.com |
| global.email.subject_suffix     | Suffix on the subject of all outgoing email from GitLab                                 | ""                    |

## Incoming Email configuration

| Parameter                                          | Description                                                                                              | Default               |
| ---                                                | ---                                                                                                      | ---                   |
| global.appConfig.incomingEmail.enabled             | Enable incoming email                                                                                    | false                 |
| global.appConfig.incomingEmail.address             | The email address to reference the item being replied to (example: gitlab-incoming+%{key}@gmail.com)     | empty                 |
| global.appConfig.incomingEmail.host                | Host for IMAP                                                                                            | empty                 |
| global.appConfig.incomingEmail.port                | Port for IMAP                                                                                            | 993                   |
| global.appConfig.incomingEmail.ssl                 | Whether IMAP server uses SSL                                                                             | true                  |
| global.appConfig.incomingEmail.startTls            | Whether IMAP server uses StartTLS                                                                        | false                 |
| global.appConfig.incomingEmail.user                | Username for IMAP authentication                                                                         | empty                 |
| global.appConfig.incomingEmail.password.secret     | Name of a `Secret` containing the IMAP password                                                          | empty                 |
| global.appConfig.incomingEmail.password.key        | Key in `global.appConfig.incomingEmail.password.secret` that contains the IMAP password                  | password              |
| global.appConfig.incomingEmail.mailbox             | Mailbox where incoming mail will end up.                                                                 | inbox                 |
| global.appConfig.incomingEmail.idleTimeout         | The IDLE command timeout                                                                                 | 60                    |


## GitLab Shell

| Parameter              | Description                              | Default |
| ---                    | ---                                      | ---     |
| global.shell.port      | Port number to expose on Ingress for SSH |         |
| global.shell.authToken | Secret containing shared secret          |         |
| global.shell.hostKeys  | Secret containing SSH host keys          |         |

## RBAC Settings
| Parameter                                    | Description                                                       | Default                      |
| ---                                          | ---                                                               | ---                          |
| certmanager.rbac.create                      | Create and use RBAC resources                                     | true                         |
| nginx-ingress.rbac.create                    | Create and use default RBAC resources                             | false                        |
| nginx-ingress.rbac.createClusterRole         | Create and use Cluster role                                       | false                        |
| nginx-ingress.rbac.createRole                | Create and use namespaced role                                    | true                         |
| prometheus.rbac.create                       | Create and use RBAC resources                                     | true                         |
| gitlab-runner.rbac.create                    | Create and use RBAC resources                                     | true                         |

## Advanced nginx ingress configuration

See [nginx-ingress chart](../../charts/nginx/README.md)

## Advanced in-cluster redis configuration

| Parameter                                    | Description                                 | Default        |
| ---                                          | ---                                         | ---            |
| redis.image.repository                       | Redis image repository                      | redis          |
| redis.image.tag                              | Redis image tag                             | 3.2.5          |
| redis.image.pullPolicy                       | Redis image pull policy                     | IfNotPresent   |
| redis.service.name                           | Redis service name                          | redis          |
| redis.service.type                           | Redis service type                          | ClusterIP      |
| redis.service.externalPort                   | Redis internal port                         | 6379           |
| redis.service.internalPort                   | Redis exposed port                          | 6379           |
| redis.service.clusterIP                      | Cluster IP                                  | 0.0.0.0        |
| redis.service.annotations                    | Annotations to add to the `Service`         | {}             |
| redis.replicas                               | Number of replicas                          | 1              |
| redis.enabled                                | Enable flag for the chart                   | true           |
| redis.timeout                                | Timeout in seconds                          | 60             |
| redis.tcpKeepalive                           | Keep alive in seconds                       | 300            |
| redis.loglevel                               | Log verbosity                               | notice         |
| redis.persistence.enabled                    | Enable persistence flag                     | true           |
| redis.persistence.accessMode                 | Redis access mode                           | ReadWriteOnce  |
| redis.persistence.size                       | Size of volume needed for redis persistence | 5Gi            |
| redis.persistence.subPath                    | Subpath to mount persistence volume at      |                |
| redis.persistence.storageClass               | storageClassName for provisioning           |                |
| redis.persistence.volumeName                 | Existing persistent volume name             |                |
| redis.persistence.matchLabels                | Label-value matches to bind                 |                |
| redis.persistence.matchExpressions           | Label-expression matches to bind            |                |

## Advanced registry configuration

| Parameter                                    | Description                         | Default              |
| ---                                          | ---                                 | ---                  |
| registry.enabled                             | Enable docker registry              | true                 |
| registry.httpSecret                          | Https secret                        |                      |
| registry.authEndpoint                        | Auth endpoint                       | Undefined by default |
| registry.tokenService                        | JWT token service                   | container_registry   |
| registry.tokenIssuer                         | JWT token issuer                    | gitlab-issuer        |
| registry.replicas                            | Number of replicas                  | 1                    |
| registry.minio.enabled                       | Enable minio flag                   | true                 |
| registry.minio.bucket                        | Minio registry bucket name          | registry             |
| registry.service.annotations                 | Annotations to add to the `Service` | {}                   |

## Advanced minio configuration

| Parameter                                    | Description                         | Default                      |
| ---                                          | ---                                 | ---                          |
| minio.image                                  | Minio image                         | minio/minio                  |
| minio.imageTag                               | Minio image tag                     | RELEASE.2017-12-28T01-21-00Z |
| minio.imagePullPolicy                        | Minio image pull policy             | Always                       |
| minio.enabled                                | Minio enable flag                   | true                         |
| minio.mountPath                              | Minio config file mount path        | /export                      |
| minio.replicas                               | Minio number of replicas            | 4                            |
| minio.persistence.enabled                    | Minio enable persistence flag       | true                         |
| minio.persistence.accessMode                 | Minio persistence access mode       | ReadWriteOnce                |
| minio.persistence.size                       | Minio persistence volume size       | 10Gi                         |
| minio.persistence.subPath                    | Minio persistence volume mount path |                              |
| minio.persistence.storageClass               | Minio storageClassName for provisioning |                          |
| minio.persistence.volumeName                 | Minio existing persistent volume name   |                          |
| minio.persistence.matchLabels                | Minio label-value matches to bind       |                          |
| minio.persistence.matchExpressions           | Minio label-expression matches to bind  |                          |
| minio.serviceType                            | Minio service type                  | ClusterIP                    |
| minio.servicePort                            | Minio service port                  | 9000                         |
| minio.service.annotations                    | Annotations to add to the `Service` | {}                           |
| minio.resources.requests.memory              | Minio minimum memory requested      | 256Mi                        |
| minio.resources.requests.cpu                 | Minio minimum cpu requested         | 250m                         |
| minio.defaultBuckets                         | Minio default buckets               | [{"name": "registry"}]       |
| minio.minioConfig.region                     | Minio region                        | us-east-1                    |
| minio.minioConfig.browser                    | Minio browser flag                  | on                           |
| minio.minioConfig.domain                     | Minio domain                        |                              |

## Advanced gitlab configuration

| Parameter                                           | Description                                    | Default                                                    |
| ---                                                 | ---                                            | ---                                                        |
| gitlab.gitaly.image.repository                      | Gitaly image repository                        | registry.gitlab.com/gitlab-org/build/cng/gitaly            |
| gitlab.gitaly.image.tag                             | Gitaly image tag                               | latest                                                     |
| gitlab.gitaly.image.pullPolicy                      | Gitaly image pull policy                       | Always                                                     |
| gitlab.gitaly.service.name                          | Gitaly service name                            | gitaly                                                     |
| gitlab.gitaly.service.type                          | Gitaly service type                            | ClusterIP                                                  |
| gitlab.gitaly.service.externalPort                  | Gitaly service exposed port                    | 8075                                                       |
| gitlab.gitaly.service.internalPort                  | Gitaly internal port                           | 8075                                                       |
| gitlab.gitaly.service.annotations                   | Annotations to add to the `Service`            | {}                                                         |
| gitlab.gitaly.enabled                               | Gitaly enable flag                             | true                                                       |
| gitlab.gitaly.serviceName                           | Gitaly service name                            | gitaly                                                     |
| gitlab.gitaly.authToken.secret                      | Gitaly secret name                             | {.Release.Name}-gitaly-secret                                              |
| gitlab.gitaly.authToken.key                         | Key to gitaly token in the secret              | token                                                      |
| gitlab.gitaly.shell.authToken.secret                | Shell secret                                   | {Release.Name}-gitlab-shell-secret                                        |
| gitlab.gitaly.shell.authToken.key                   | Shell key                                      | secret                                                     |
| gitlab.gitaly.persistence.enabled                   | Gitaly enable persistence flag                 | true                                                       |
| gitlab.gitaly.persistence.accessMode                | Gitaly persistence access mode                 | ReadWriteOnce                                              |
| gitlab.gitaly.persistence.size                      | Gitaly persistence volume size                 | 50Gi                                                       |
| gitlab.gitaly.persistence.subPath                   | Gitaly persistence volume mount path           |                                                          |
| gitlab.gitaly.persistence.storageClass              | storageClassName for provisioning              |                                                  |
| gitlab.gitaly.persistence.volumeName                | Existing persistent volume name                |                                                  |
| gitlab.gitaly.persistence.matchLabels               | Label-value matches to bind                    |                                                  |
| gitlab.gitaly.persistence.matchExpressions          | Label-expression matches to bind               |                                                  |
| gitlab.gitaly.securityContext.runAsUser             | User ID under which the pod should be started  | 1000                                             |
| gitlab.gitaly.securityContext.fsGroup               | Group ID under which the pod should be started | 1000                                             |
| gitlab.gitlab-shell.replicaCount                    | Shell replicas                                 | 1                                                          |
| gitlab.gitlab-shell.image.repository                | Shell image repository                         | registry.gitlab.com/gitlab-org/build/cng/gitlab-shell      |
| gitlab.gitlab-shell.image.tag                       | Shell image tag                                | latest                                                     |
| gitlab.gitlab-shell.image.pullPolicy                | Shell image pull policy                        | Always                                                     |
| gitlab.gitlab-shell.service.name                    | Shell service name                             | gitlab-shell                                               |
| gitlab.gitlab-shell.service.type                    | Shell service type                             | ClusterIP                                                  |
| gitlab.gitlab-shell.service.externalPort            | Shell exposed port                             | 22                                                         |
| gitlab.gitlab-shell.service.internalPort            | Shell internal port                            | 22                                                         |
| gitlab.gitlab-shell.service.annotations             | Annotations to add to the `Service`            | {}                                                         |
| gitlab.gitlab-shell.enabled                         | Shell enable flag                              | true                                                       |
| gitlab.gitlab-shell.authToken.secret                | Shell auth secret                              | {Release.Name}-gitlab-shell-secret                                        |
| gitlab.gitlab-shell.authToken.key                   | Shell auth secret key                          | secret                                                     |
| gitlab.gitlab-shell.unicorn.serviceName             | Unicorn service name                           | unicorn                                                    |
| gitlab.gitlab-shell.redis.serviceName               | Redis service name                             | redis                                                      |
| gitlab.sidekiq.image.repository                     | Sidekiq image repository                       | registry.gitlab.com/gitlab-org/build/cng/gitlab-sidekiq-ee |
| gitlab.sidekiq.image.tag                            | Sidekiq image tag                              | latest                                                     |
| gitlab.sidekiq.image.pullPolicy                     | Sidekiq image pull policy                      | Always                                                     |
| gitlab.sidekiq.enabled                              | Sidekiq enabled flag                           | true                                                       |
| gitlab.sidekiq.redis.serviceName                    | Redis service name                             | redis                                                      |
| gitlab.sidekiq.psql.password.secret                 | psql password secret                           | gitlab-postgres                                            |
| gitlab.sidekiq.psql.password.key                    | key to psql password in psql secret            | psql-password                                              |
| gitlab.sidekiq.gitaly.serviceName                   | gitaly service name                            | gitaly                                                     |
| gitlab.sidekiq.gitaly.authToken.secret              | gitaly secret                                  | {.Release.Name}-gitaly-secret                                              |
| gitlab.sidekiq.gitaly.authToken.key                 | key to gitaly token in gitaly secret           | token                                                      |
| gitlab.sidekiq.replicas                             | Sidekiq replicas                               | 1                                                          |
| gitlab.sidekiq.concurrency                          | Sidekiq default concurrency                    | 10                                                         |
| gitlab.sidekiq.timeout                              | Sidekiq job timeout                            | 5                                                          |
| gitlab.sidekiq.resources.requests.cpu               | Sidekiq minimum needed cpu                     | 100m                                                       |
| gitlab.sidekiq.resources.requests.memory            | Sidekiq minimum needed memory                  | 600M                                                       |
| gitlab.unicorn.replicaCount                         | Unicorn number of replicas                     | 1                                                          |
| gitlab.unicorn.image.repository                     | Unicorn image repository                       | registry.gitlab.com/gitlab-org/build/cng/gitlab-unicorn-ee |
| gitlab.unicorn.image.tag                            | Unicorn image tag                              | latest                                                     |
| gitlab.unicorn.image.pullPolicy                     | Unicorn image pull policy                      | Always                                                     |
| gitlab.unicorn.service.name                         | Unicorn service name                           | unicorn                                                    |
| gitlab.unicorn.service.type                         | Unicorn service type                           | ClusterIP                                                  |
| gitlab.unicorn.service.externalPort                 | Unicorn exposed port                           | 8080                                                       |
| gitlab.unicorn.service.internalPort                 | Unicorn internal port                          | 8080                                                       |
| gitlab.unicorn.service.workhorseExternalPort        | Workhorse exposed port                         | 8181                                                       |
| gitlab.unicorn.service.workhorseInternalPort        | Workhorse internal port                        | 8181                                                       |
| gitlab.unicorn.service.annotations                  | Annotations to add to the `Service`            | {}                                                         |
| gitlab.unicorn.enabled                              | Unicorn enabled flag                           | true                                                       |
| gitlab.unicorn.workerProcesses                      | Unicorn number of workers                      | 2                                                          |
| gitlab.unicorn.workerTimeout                        | Unicorn worker timeout                         | 60                                                         |
| gitlab.unicorn.redis.serviceName                    | Redis service name                             | redis                                                      |
| gitlab.unicorn.psql.password.secret                 | psql secret name                               | gitlab-postgres                                            |
| gitlab.unicorn.psql.password.key                    | Key to psql password in psql secret            | psql-password                                              |
| gitlab.unicorn.shell.authToken.secret               | Shell token secret                             | {Release.Name}-gitlab-shell-secret                                        |
| gitlab.unicorn.shell.authToken.key                  | Key to shell token in shell secret             | secret                                                     |
| gitlab.unicorn.gitaly.serviceName                   | Gitaly service name                            | gitaly                                                     |
| gitlab.unicorn.gitaly.authToken.secret              | Gitaly secret name                             | {.Release.Name}-gitaly-secret                                              |
| gitlab.unicorn.gitaly.authToken.key                 | Key to gitaly token in gitaly secret           | token                                                      |
| gitlab.unicorn.registry.api.protocol                | Registry protocol                              | http                                                       |
| gitlab.unicorn.registry.api.serviceName             | Registry service name                          | registry                                                   |
| gitlab.unicorn.registry.api.port                    | Registry port                                  | 5000                                                       |
| gitlab.unicorn.registry.tokenIssuer                 | Registry token issuer                          | gitlab-issuer                                              |
| gitlab.unicorn.resources.requests.cpu               | Unicorn minimum cpu                            | 200m                                                       |
| gitlab.unicorn.resources.requests.memory            | Unicorn minimum memory                         | 1.4G                                                       |
| gitlab.unicorn.workhorse.image                      | Workhorse image repository                     | registry.gitlab.com/gitlab-org/build/cng/gitlab-workhorse-ee |
| gitlab.unicorn.workhorse.tag                        | Workhorse image tag                            |                                                            |
| gitlab.unicorn.workhorse.sentryDSN                  | DSN for Sentry instance for error reporting    | ""                                                         |
| gitlab.unicorn.workhorse.extraArgs                  | String of extra parameters for workhorse       | ""                                                         |
| gitlab.migrations.image.repository                  | Migrations image repository                    | registry.gitlab.com/gitlab-org/build/cng/gitlab-rails-ee   |
| gitlab.migrations.image.tag                         | Migrations image tag                           | latest                                                     |
| gitlab.migrations.image.pullPolicy                  | Migrations pull policy                         | Always                                                     |
| gitlab.migrations.enabled                           | Migrations enable flag                         | true                                                       |
| gitlab.migrations.redis.serviceName                 | Redis service name                             | redis                                                      |
| gitlab.migrations.psql.password.secret              | psql secret                                    | gitlab-postgres                                            |
| gitlab.migrations.psql.password.key                 | key to psql password in psql secret            | psql-password                                              |
| gitlab-runner.image                                 | runner image                                   | gitlab/gitlab-runner:alpine-v10.5.0                        |
| gitlab-runner.enabled                               |                                                | redis                                                      |
| gitlab-runner.imagePullPolicy                       | image pull policy                              | IfNotPresent                                               |
| gitlab-runner.unregisterRunners                     | unregister all runners before termination      | true                                                       |
| gitlab-runner.concurrent                            | number of concurrent jobs                      | 20                                                         |
| gitlab-runner.checkInterval                         | polling interval                               | 30s                                                        |
| gitlab-runner.rbac.create                           | whether to create rbac service account         | true                                                       |
| gitlab-runner.rbac.clusterWideAccess                | deploy containers of jobs cluster-wide         | false                                                      |
| gitlab-runner.rbac.serviceAccountName               | name of the rbac service account to create     | default                                                    |
| gitlab-runner.runners.image                         | default container image to use in builds       | ubuntu:16.04                                               |
| gitlab-runner.runners.imagePullSecrets              | imagePullSecrets                               | []                                                         |
| gitlab-runner.runners.privileged                    | run in privieleged mode,needed for `dind`      | false                                                      |
| gitlab-runner.runners.namespace                     | numespace to run jobs in                       | default                                                    |
| gitlab-runner.runners.cache.cacheType               | cache type                                     | s3                                                         |
| gitlab-runner.runners.cache.s3BucketName.           | name of the bucket                             | runner-cache                                               |
| gitlab-runner.runners.cache.cacheShared             | share the cache between runners                | true                                                       |
| gitlab-runner.runners.cache.s3BucketLocation        | bucket region                                  | us-east-1                                                  |
| gitlab-runner.runners.cache.secretName              | secret to accesskey and secretkey from         | gitlab-minio                                               |
| gitlab-runner.runners.cache.s3CachePath             | path in the bucket                             | gitlab-runner                                              |
| gitlab-runner.runners.cache.s3CacheInsecure         | use http                                       | false                                                      |
| gitlab-runner.runners.builds.cpuLimit               | build container limit                          |                                                            |
| gitlab-runner.runners.build.memoryLimit             | build container limit                          |                                                            |
| gitlab-runner.runners.build.cpuRequests             | build container limit                          |                                                            |
| gitlab-runner.runners.build.memoryRequests          | build container limit                          |                                                            |
| gitlab-runner.runners.service.cpuLimit              | service container limit                        |                                                            |
| gitlab-runner.runners.service.memoryLimit           | service container limit                        |                                                            |
| gitlab-runner.runners.service.cpuRequests           | service container limit                        |                                                            |
| gitlab-runner.runners.service.memoryRequests        | service container limit                        |                                                            |
| gitlab-runner.resources.limits.memory               | runner resources                               |                                                            |
| gitlab-runner.resources.limits.cpu                  | runner resources                               |                                                            |
| gitlab-runner.resources.requests.memory             | runner resources                               |                                                            |
| gitlab-runner.resources.requests.cpu                | runner resources                               |                                                            |
