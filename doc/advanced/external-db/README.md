# External PostgreSQL database

This document assumes you already have your own PostgreSQL database.

If you do not have one, consider a cloud provided solution like [AWS Aurora](https://aws.amazon.com/rds/aurora/) or [GCP Cloud SQL](https://cloud.google.com/sql/). For on-premise or deployment to VM, consider our [Omnibus GitLab package](./external-omnibus-psql.md).

## External database requirements

To use an external database with the `gitlab` chart, there are a few prerequisites.

1. GitLab requires PostgreSQL 9.6.
1. The `pg_trgm` extension must be available
1. An empty database to use
1. A user with full access granted to the database above
1. A [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) with the password for the user above
1. Ensure that the database is reachable from the cluster. Be sure firewall policies are in place to allow traffic.

## Configuring `gitlab` to use an external database

You need to set the following parameters:
* `postgresql.install`: Set to `false` to disable the embedded database.
* `global.psql.host`: Set to the hostname of the external database, can be a domain or an IP address.
* `global.psql.password.secret`: The name of the [secret which contains the database password for the `gitlab` user.](doc/installation/secrets.md#postgres-password)
* `global.psql.password.key`: The key within the secret, which contains the password. The password should be *unencoded* value.

Items below can be further customized if you are not using the defaults:
* `global.psql.port`: The port the database is available on, defaults to `5432`.
* `global.psql.database`: The name of the database.
* `global.psql.username`: The user with access to the database.

For example, pass these values via helm's `--set` flag while deploying:

```
helm install
  --set postgresql.install=false
  --set global.psql.host=psql.example
  --set global.psql.password.secret=gitlab-postgresql-password
  --set global.psql.password.key=postgres-password
```
