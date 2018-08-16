# Using the Shared-Secrets chart

The `shared-secrets` sub-chart is responsible for provisioning a variety of secrets used across the installation, unless otherwise manually specified. This includes:
1. Initial root password
1. Self-signed TLS certificates for all public services: GitLab, Minio, and Registry
1. Registry authentication certificates
1. Minio, Registry, GitLab Shell, Gitaly secrets
1. Redis, Postgres passwords
1. SSH host keys

## Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                    | Description                            | Default                                  |
| ---                          | ---                                    | ---                                      |
| image.repository             | Gitaly image repository                | registry.gitlab.com/gitlab-org/build/cng/kubectl |
| image.tag                    | Gitaly image tag                       | 1f8690f03f7aeef27e727396927ab3cc96ac89e7 |
| image.pullPolicy             | Gitaly image pull policy               | Always                                   |
| image.pullSecrets            | Secrets for the image repository       |                                          |
| selfsign.image               | selfsign image repository              | registry.gitlab.com/gitlab-org/build/cnf/cfssl-self-sign |
| selfsign.tag                 | selfsign image tag                     | ---------------------------------------------------------------- |
| selfsign.keyAlgorithm        | selfsign cert key algorithm            | rsa                                      |
| selfsign.keySize             | selfsign cert key size                 | 4096                                     |
| selfsign.caSubject           | selfsign CA Subject                    | GitLab Helm Chart                        |
| resources                    | resource requests, limits              |                                          |
| env                          | Rails environment                      | production                               |
| rbac.create                  | Create RBAC roles and bindings         | true                                     |
