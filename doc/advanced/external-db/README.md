# External PostgreSQL database

This document assumes you already have your own PostgreSQL database. 

If you do not have one, consider a cloud provided solution like [AWS Aurora](https://aws.amazon.com/rds/aurora/) or [GCP Cloud SQL](https://cloud.google.com/sql/). For on-premise or deployment to VM, consider our [Omnibus GitLab package](./external-omnibus-psql.md).

## External database requirements

To use an external database with the `gitlab` chart, there are a few prerequisites.

1. GitLab requires PostgreSQL 9.6.
1. The `pg_trgm` extension must be available
1. A user named `gitlab` with the password created as a [Kubernetes Secret](../../installation/secrets.md#postgres-password)
1. A database named `gitlabhq_production`, which the `gitlab` user has access to

## Configuring `gitlab` to use an external database

You need to set the following parameters: 
* `gitlab.omnibus.enabled`: Set to `false` to disable the embedded database
* `global.psql.host`: Set to the hostname of the external database
* `global.psql.port`: The port the database is available on, defaults to `5432`
* `global.psql.password.secret`: The name of the secret which contains the database password for the `gitlab` user
* `global.psql.password.key`: The key within the secret, which contains the password

For example, pass these values via helm's `--set` flag while deploying:

```
helm install
  --set gitlab.omnibus.enabled=false
  --set global.psql.host=omnibus-vm
  --set global.psql.password.secret=psql-secret
  --set global.psql.password.key=<key>
```