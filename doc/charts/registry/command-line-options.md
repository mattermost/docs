# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                         | Description                         | Default              |
| ---                               | ---                                 | ---                  |
| registry.enabled                  | Enable registry flag                | true                 |
| registry.httpSecret               | Https secret                        |                      |
| registry.authEndpoint             | Auth endpoint                       | Undefined by default |
| registry.tokenService             | JWT token service                   | container_registry   |
| registry.tokenIssuer              | JWT token issuer                    | gitlab-issuer        |
| registry.certificate.secret       | JWT certificate                     | gitlab-registry      |
| registry.certificate.key          | JWT certificate private key         | registry-auth.crt    |
| registry.replicas                 | Number of replicas                  | 1                    |
| registry.minio.enabled            | Enable minio flag                   | true                 |
| registry.minio.bucket             | Minio registry bucket name          | registry             |
| registry.minio.credentials.secret | Secret containing minio credentials | gitlab-minio         |
