# Secrets

For a functional deployment, different types of secrets are needed:

* Registry authentication certificates
* SSH Host Keys and Certificates for GitLab Shell
* Passwords for individual components

A user of these charts may chose to provide any or all of the below secrets.
**Any secret not provided by the user will be automatically generated automatically,
via the included [`shared-secrets` Job](../../charts/gitlab/charts/shared-secrets) which will
populate all necessary secrets with random values. When used in combination with
the integration of Let's Encrypt ACME, a user need not complete any of the following.**

To make use of automatic secret handling, you may skip to [Next steps](#next-steps)

To provide one or more manual secrets, continue reading.

**Table of Contents**

- [Registry authentication certificates](#registry-authentication-certificates)
- [SSH Host Keys](#ssh-host-keys)
- [Passwords](#passwords)
  * [Redis password](#redis-password)
  * [Postgres password](#postgres-password)
  * [GitLab Shell](#gitLab-shell)
  * [Gitaly Secret](#gitaly-secret)
  * [Minio Secret](#minio-secret)
- [Next Steps](#next-steps)

## Registry authentication certificates

Communication between GitLab and Registry happens behind an Ingress so it is sufficient in most cases to use self-signed certificates
for this communication. If this traffic is exposed over a network, you
should generate publicly valid certificates.

In the example below, we assume that we require self-signed certificates.

Generate a certificate-key pair:

```
mkdir -p certs
openssl req -new -newkey rsa:4096 -subj "/CN=gitlab-issuer" -nodes -x509 -keyout certs/registry-example-local.key -out certs/registry-example-local.crt
```

Create a secret containing these certificates.
 We will create `registry-auth.key` and `registry-auth.crt` keys inside the
`gitlab-registry` secret.

```
kubectl create secret generic gitlab-registry --from-file=registry-auth.key=certs/registry-example-local.key --from-file=registry-auth.crt=certs/registry-example-local.crt
```

In more isolated clusters, these certificates can be in separate secrets, as long
as the configuration information as to which secret to use is passed to the appropriate
chart.

## SSH Host Keys

Generate the OpenSSH certificate-key pairs:

```
mkdir -p hostKeys
ssh-keygen -t rsa  -f hostKeys/ssh_host_rsa_key -N ""
ssh-keygen -t dsa  -f hostKeys/ssh_host_dsa_key -N ""
ssh-keygen -t ecdsa  -f hostKeys/ssh_host_ecdsa_key -N ""
ssh-keygen -t ed25519  -f hostKeys/ssh_host_ed25519_key -N ""
```

Create the secret containing these certificates.

```
kubectl create secret generic gitlab-shell-host-keys --from-file hostKeys
```

## Passwords

### Redis password

Generate a random 64 character alpha-numeric password for Redis.

```
kubectl create secret generic gitlab-redis --from-literal=redis-password=$(head -c 512 /dev/urandom | LC_CTYPE=C tr -cd 'a-zA-Z0-9' | head -c 64)
```

### Postgres password

Generate a random 64 character alpha-numeric password for Postgres.

```
kubectl create secret generic gitlab-postgres --from-literal=psql-password=$(head -c 512 /dev/urandom | LC_CTYPE=C tr -cd 'a-zA-Z0-9' | head -c 64)
```

### GitLab Shell

Generate a random 64 character alpha-numeric secret for GitLab Shell.

```
kubectl create secret generic gitlab-shell-secret --from-literal=secret=$(head -c 512 /dev/urandom | LC_CTYPE=C tr -cd 'a-zA-Z0-9' | head -c 64)
```

### Gitaly Secret

Generate a random 64 character alpha-numeric token for Gitaly.

```
kubectl create secret generic gitaly-secret --from-literal=token=$(head -c 512 /dev/urandom | LC_CTYPE=C tr -cd 'a-zA-Z0-9' | head -c 64)
```

### Minio Secret

Generate a set of random 20 & 64 character alpha-numeric keys for Minio.

```
kubectl create secret generic gitlab-minio --from-literal=accesskey=$(head -c 512 /dev/urandom | LC_CTYPE=C tr -cd 'a-zA-Z0-9' | head -c 20) --from-literal=secretkey=$(head -c 512 /dev/urandom | LC_CTYPE=C tr -cd 'a-zA-Z0-9' | head -c 64)
```

# Next Steps

Once all secrets have been generated and stored, you can proceed [deploying GitLab](deployment.md).
