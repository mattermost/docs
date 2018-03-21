# Deployment Guide

In order to deploy, you need to make some decisions about how you will run gitlab.
Options can be specified using helm's `--set option.name=value` command line option.
A complete list  of command line options can be found [here](./command-line-options.md).
This guide will cover required values and common options.

## Selecting configuration options

In each section collect the options that will be combined to use with `helm install`.

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
--set certmanager.issuer.email=me@example.local
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

If you are using the default in-kubernetes postgres database, you'll need to be sure to allow traffic
from your cluster's IP ranges. For example if your cluster has pods using `100.64.0.0/10`:

*Include these options in your helm install command:*
```
--set 'gitlab.omnibus.trusted_proxies[0]=100.64.0.0/10'
--set 'gitlab.omnibus.trusted_proxies[1]=127.0.0.1/32'
```

## Deploy using helm

Once you have all of your configuration options collected, we can get any dependencies and
run helm. In this example, we've named our helm release "gitlab" and we're installing it in
the "gitlab" namespace

```
$ helm dependencies update
$ helm upgrade --install gitlab . \
  --namespace gitlabdemo \
  --timeout 600 \
  --set global.hosts.domain=example.local \
  --set nginx.service.loadBalancerIP=10.10.10.10 \
  --set gitlab.migrations.initialRootPassword="example-password" \
  --set certmanager.issuer.email=me@example.local \
  --set 'gitlab.omnibus.trusted_proxies[0]=100.64.0.0/10' \
  --set 'gitlab.omnibus.trusted_proxies[1]=127.0.0.1/32'
```

## Monitoring Deployment

This will output the list of resources installed once the deployment finishes which may take 5-10 minutes.

The status of the deployment can be checked by running `helm status gitlab` which can also be done while
the deployment is taking place if you run the command in another terminal.

[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
