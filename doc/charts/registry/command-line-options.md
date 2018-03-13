# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                | Description                         | Default              |
| ---                      | ---                                 | ---                  |
| enabled                  | Enable registry flag                | true                 |
| httpSecret               | Https secret                        |                      |
| authEndpoint             | Auth endpoint                       | Undefined by default |
| tokenService             | JWT token service                   | container_registry   |
| tokenIssuer              | JWT token issuer                    | gitlab-issuer        |
| certificate.secret       | JWT certificate                     | gitlab-registry      |
| certificate.key          | JWT certificate private key         | registry-auth.crt    |
| replicas                 | Number of replicas                  | 1                    |
| minio.enabled            | Enable minio flag                   | true                 |
| minio.bucket             | Minio registry bucket name          | registry             |
| minio.credentials.secret | Secret containing minio credentials | gitlab-minio         |
