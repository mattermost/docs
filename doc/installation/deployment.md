# Deployment Guide

Before running `helm install`, you need to make some decisions about how you will run GitLab.
Options can be specified using Helm's `--set option.name=value` command line option.
A complete list  of command line options can be found [here](./command-line-options.md).
This guide will cover required values and common options.

## Selecting configuration options

In each section collect the options that will be combined to use with `helm install`.

### Secrets

There are some secrets that need to be created (e.g. SSH keys). By default they will be generated automatically, but if you want to specify them, you can follow the [secrets guide](secrets.md).

### Networking and DNS

By default, the chart relies on Kubernetes `Service` objects of `type: LoadBalancer`
to expose GitLab services using name-based virtual servers configured with`Ingress`
objects. You'll need to specify a domain which will contain records to resolve
`gitlab`, `registry`, and `minio` (if enabled) to the appropriate IP for your chart.

*Include these options in your Helm install command:*

```
--set global.hosts.domain=example.com
```

#### Dynamic IPs with external-dns

If you plan to use an automatic DNS registration service like [external-dns](https://github.com/kubernetes-incubator/external-dns),
you won't need any additional configuration.

If you provisioned a GKE cluster using the scripts in this repo, [external-dns](https://github.com/kubernetes-incubator/external-dns)
is already installed in your cluster.

#### Static IP

If you plan to manually configure your DNS records they should all point to a
static IP. For example if you choose `example.com` and you have a static IP
of `10.10.10.10`, then `gitlab.example.com`, `registry.example.com` and
`minio.example.com` (if using MinIO) should all resolve to `10.10.10.10`.

If you are using GKE, there is some documentation [here](cloud/gke.md#creating-the-external-ip)
for configuring static IPs and DNS. Consult your Cloud and/or DNS provider's
documentation for more help on this process.

*Include these options in your Helm install command:*

```
--set global.hosts.externalIP=10.10.10.10
```

### Persistence

By default the chart will create Volume Claims with the expectation that a dynamic provisioner will create the underlying Persistent Volumes. If you would like to customize the storageClass or manually create and assign volumes, please review the [storage documentation](storage.md).

> **Important**: After initial installation, making changes to your storage settings requires manually editing Kubernetes
> objects, so it's best to plan ahead before installing your production instance of GitLab to avoid extra storage migration work.

### TLS certificates

You should be running GitLab using https which requires TLS certificates. By default the
chart will install and configure [cert-manager](https://github.com/jetstack/cert-manager)
to obtain free TLS certificates.
If you have your own wildcard certificate, you already have cert-manager installed, or you
have some other way of obtaining TLS certificates, [read about more TLS options here](./tls.md).

For the default configuration, you must specify an email address to register your TLS
certificates.
*Include these options in your Helm install command:*

```
--set certmanager-issuer.email=me@example.com
```

### PostgreSQL

By default this chart provides an in-cluster PostgreSQL database, for trial
purposes only.

> **NOTE: This configuration is not recommended for use in production.**
>
> - The container runs as root
> - A single, non-resilient Deployment is used

You can read more about setting up your production-ready database in the [advanced database docs](../advanced/external-db/index.md).

If you have an external postgres database ready, the chart can be configured to
use it as shown below.

*Include these options in your Helm install command:*

```
--set postgresql.install=false
--set global.psql.host=production.postgress.hostname.local
--set global.psql.password.secret=kubernetes_secret_name
--set global.psql.password.key=key_that_contains_postgres_password
```

### Redis

By default we use an single, non-replicated Redis instance. If desired, a highly available Redis can be deployed instead. You can learn more about configuring: [Redis](../charts/redis) and [Redis-ha](../charts/redis-ha).

*To deploy `redis-ha` instead of the default `redis`, include these options in your Helm install command:*

```
--set redis.enabled=false
--set redis-ha.enabled=true
```

### MinIO

By default this chart provides an in-cluster MinIO deployment to provide an object storage API.
This configuration should not be used in production.

You can read more about setting up your production-ready object storage in the [external object storage](../advanced/external-object-storage/index.md)

### Prometheus

We use the [upstream Prometheus chart][prometheus-configuration],
and do not override values from our own defaults.
We do, however, default disable `alertmanager`, `nodeExporter`, and
`pushgateway`.

Refer to the [Prometheus chart documentation][prometheus-configuration] for the
exhaustive list of configuration options and ensure they are sub-keys to
`prometheus`, as we use this as requirement chart.

For instance, the requests for persistent storage can be controlled with:

```yaml
prometheus:
  alertmanager:
    enabled: false
    persistentVolume:
      enabled: false
      size: 2GiB
  pushgateway:
    enabled: false
    persistentVolume:
      enabled: false
      size: 2GiB
  server:
    persistentVolume:
      enabled: true
      size: 8GiB
```

[prometheus-configuration]: https://github.com/helm/charts/tree/master/stable/prometheus#configuration

### Outgoing email

By default outgoing email is disabled. To enable it, provide details for your SMTP server
using the `global.smtp` and `global.email` settings. You can find details for these settings in the
[command line options](command-line-options.md#outgoing-email-configuration).

If your SMTP server requires authentication make sure to read the section on providing
your password in the [secrets documentation](secrets.md#smtp-password).
You can disable authentication settings with `--set global.smtp.authentication=""`.

If your Kubernetes cluster is on GKE, be aware that SMTP [port 25
is blocked](https://cloud.google.com/compute/docs/tutorials/sending-mail/#using_standard_email_ports).

### Incoming email

By default incoming email is disabled. To enable it, provide details of your
IMAP server and access credentials using the `global.appConfig.incomingEmail`
settings. You can find details for these settings in the [command line options](command-line-options.md#incoming-email-configuration).
You will also have to create a Kubernetes secret containing IMAP password as
described in the [secrets guide](secrets.md#imap-password-for-incoming-emails).

To use reply-by-email feature, where users can reply to notification emails to
comment on issues and MRs, you need to configure both outgoing email and
incoming email settings.

### Deploy the Community Edition

By default, the Helm charts use the Enterprise Edition of GitLab. If desired, you can instead use the Community Edition. Learn more about the [difference between the two](https://about.gitlab.com/install/ce-or-ee/).

*To deploy the Community Edition, include this option in your Helm install command:*

```
--set global.edition=ce
```

### RBAC

This chart defaults to creating and using RBAC. If your cluster does not have RBAC enabled, you will need to disable these settings:

```
--set certmanager.rbac.create=false
--set nginx-ingress.rbac.createRole=false
--set prometheus.rbac.create=false
--set gitlab-runner.rbac.create=false
```

### CPU and RAM Resource Requirements

The resource requests, and number of replicas for the GitLab components (not PostgreSQL, Redis, or MinIO) in this Chart
are set by default to be adequate for a small production deployment. This is intended to fit in a cluster with at least 8vCPU
and 30gb of RAM. If you are trying to deploy a non-production instance, you can reduce the defaults in order to fit into
a smaller cluster.

The [minimal GKE example values file](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/values-gke-minimum.yaml) provides an example of tuning the resources
to fit within a 3vCPU 12gb cluster.

The [minimal minikube example values file](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/values-minikube-minimum.yaml) provides an example of tuning the
resources to fit within a 2vCPU, 4gb minikube instance.

## Deploy using Helm

Once you have all of your configuration options collected, we can get any dependencies and
run Helm. In this example, we've named our Helm release `gitlab`.

```
helm repo add gitlab https://charts.gitlab.io/
helm repo update
helm upgrade --install gitlab gitlab/gitlab \
  --timeout 600 \
  --set global.hosts.domain=example.com \
  --set global.hosts.externalIP=10.10.10.10 \
  --set certmanager-issuer.email=me@example.com
```

You can also use `--version <installation version>` option if you would like to install a specific version of GitLab.

Mappings between chart versions and GitLab versions can be found [here](../index.md#gitlab-version-mappings).

Instructions for installing a development branch rather than a tagged release can be found in the [developer deploy documentation](../development/deploy.md).

### GitLab operator (experimental)

If you would like to use GitLab operator to achieve zero downtime upgrades, please follow the [documentation for using the operator](./operator.md)

## Monitoring the Deployment

This will output the list of resources installed once the deployment finishes which may take 5-10 minutes.

The status of the deployment can be checked by running `helm status gitlab` which can also be done while
the deployment is taking place if you run the command in another terminal.

## Initial login

You can access the GitLab instance by visiting the domain specified during
installation. If you manually created the secret for initial root password, you
can use that to sign in as `root` user. If not, GitLab would've automatically
created a random password for `root` user. This can be extracted by the
following command (replace `<name>` by name of the release - which is `gitlab`
if you used the command above).

```
kubectl get secret <name>-gitlab-initial-root-password -ojsonpath='{.data.password}' | base64 --decode ; echo
```

[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
