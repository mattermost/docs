# Using GitLab's helm.gitlab.io

## Configuring sub-charts

- [NGINX](nginx/README.md)
- [Registry](registry/README.md)
- [Omnibus](omnibus/README.md) (under gitlab)

```
nginx:
registry:
gitlab:
  omnibus:
```

## Secrets

### Ingress

If used, the chart-wide Ingress will need a `tls` secret containing the private key and full-chain certificate in PEM format. It is critical that the full-chain is used, and not the end-certificate.

### Omnibus

Pertaining to the Container Registry:
- `registry.secret` provides the name of the secret that houses the private certificate used for signing JWT authentication tokens for the [Registry][].
- (`registry.certificate`) contains the name of the key in that secret, which contains the certificate that will be used by GitLab Unicorn.

This certificate can be created with the following example:
`openssl req -new -newkey rsa:4096 -subj "/CN=gitlab-issuer" -nodes -x509 -keyout gitlab-registry.key -out registry-certificate.crt`. The `-subj`, `-*out` values can be modified as you see fit.
Once these files are created, create the k8s secret(s):
- `kubectl create secret generic omnibus-registry  --from-file=registry-auth.key=gitlab-registry.key`
- `kubectl create secret generic gitlab-registry-certbundle --from-file=registry-auth.crt=registry-certificate.crt`

Pertaining to Redis:
- `password.secret` provides the name of the secret which houses the password for Redis
- `password.key` provides the name of the key that actually houses the password itself.

This value should be a securely generated string. Create it using `kubectl create secret generic gitlab-redis --from-literal=redis-password=<value>`.
For security purposes, this values is mapped as a file in the [omnibus][] chart.

### Registry

`registry.certBundle` contains two items:
- `secret` provides the name of the secret that houses the public certificate used for verifying JWT authentication tokens for the [Registry][].
- `certificate` contains the name of the key in that secret which contains the cerficate itself.

Use the `registry-auth.crt` and `secret` created in configuring the [omnibus][] chart secrets above.
