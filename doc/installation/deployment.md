# Deployment Guide

To deploy, first clone the repository locally: `git clone git@gitlab.com:charts/helm.gitlab.io.git`

Before running `helm install`, you need to make some decisions about how you will run gitlab.
Options can be specified using helm's `--set option.name=value` command line option.
A complete list  of command line options can be found [here](./command-line-options.md).
This guide will cover required values and common options.

## Selecting configuration options

In each section collect the options that will be combined to use with `helm install`.

### Secrets

There are some secrets that need to be created (e.g. ssh keys). By default they will be generated automatically, but if you want to specify them, you can follow the [secrets guide](secrets.md).

### Networking

Before beginning, you should have a domain name with A records for `gitlab`,
`registry`, and `minio` all pointing to a single static IP. For example if you choose
`example.local` and you have a static IP of `10.10.10.10`, then `gitlab.example.local`,
`registry.example.local` and `minio.example.local` should all resolve to `10.10.10.10`.

*Include these options in your helm install command:*
```
--set global.hosts.domain=example.local
--set nginx.service.loadBalancerIP=10.10.10.10
```

### Initial root password

Select a root password for your gitlab install. The root account will have full
administrative access and can be used to create other accounts.

*Include these options in your helm install command:*
```
--set gitlab.migrations.initialRootPassword="example-password"
```

### TLS certificates

You should be running gitlab using https which requires TLS certificates. By default the
chart will install and configure [cert-manager](https://github.com/jetstack/cert-manager)
to obtain free TLS certificates.
If you have your own wildcard certificate, you already have cert-manager installed, or you
have some other way of obtaining TLS certificates, read more about TLS options [here](./tls.md).

For the default configuration, you must specify an email address to register your TLS
certificates.
*Include these options in your helm install command:*
```
--set gitlab.certmanager-issuer.email=me@example.local
```

### Postgresql

By default we use the Gitlab omnibus chart to provide an in-kubernetes postgresql database. This
configuration should not be used in production.

You can read more about setting up your production-ready database in the [advanced database docs](../advanced/external-db/README.md).

If you have an external postgres database ready,

*Include these options in your helm install command:*
```
--set global.psql.host=production.postgress.hostname.local
--set global.psql.password.secret=kubernetes_secret_name
--set global.psql.password.key=key_that_contains_postgres_password
```

### Redis

By default we use an single, non-replicated Redis instance. If desired, a highly available redis can be deployed instead. You can learn more about configuring: [Redis](../charts/redis) and [Redis-ha](../charts/redis-ha).

* To deploy `redis-ha` instead of the default `redis`, include these options in your helm install command:*
```
--set redis.enabled=false
--set redis-ha.enabled=true
```

## Deploy using helm

Once you have all of your configuration options collected, we can get any dependencies and
run helm. In this example, we've named our helm release "gitlab".

```
helm dependencies update
helm upgrade --install gitlab . \
  --timeout 600 \
  --set global.hosts.domain=example.local \
  --set nginx.service.loadBalancerIP=10.10.10.10 \
  --set gitlab.migrations.initialRootPassword="example-password" \
  --set gitlab.certmanager-issuer.email=me@example.local
```

## Monitoring the Deployment

This will output the list of resources installed once the deployment finishes which may take 5-10 minutes.

The status of the deployment can be checked by running `helm status gitlab` which can also be done while
the deployment is taking place if you run the command in another terminal.

[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
