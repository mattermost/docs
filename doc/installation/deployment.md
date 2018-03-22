# Deploying GitLab

In order to deploy, make sure you have completed the following:

- [`Secrets` have been created](secrets.md)
- An [external IP](../cloud/gke.md#creating-the-external-ip) in the same region as your cluster, to be used as the `loadBalancerIP`
- A wildcard [DNS entry](../cloud/gke.md#dns-entry) which resolves to the external IP above

For these examples:

- We will use domain `example.local` as our `DNS entry`, and expect our hostnames
  to be: `gitlab.example.local`, `registry.example.local`.
- We will use `X.X.X.X` as our `loadBalancerIP`
- Our `initialRootPassword` will be `example-password`

To deploy, first clone the repository locally: `git clone git@gitlab.com:charts/helm.gitlab.io.git`

We will run `helm install` with our settings, from the
root of this repository.

## Deploy with Let's Encrypt

```
helm install . --name gitlab --timeout 600 \
  --set global.hosts.domain=example.local \
  --set nginx.service.loadBalancerIP=X.X.X.X \
  --set kube-lego.config.LEGO_EMAIL=user@example.local \
  --set kube-lego.config.LEGO_URL=https://acme-v01.api.letsencrypt.org/directory \
  --set gitlab.migrations.initialRootPassword="example-password"
```

## Deploy with Custom Certificates

```
helm install . --name gitlab --timeout 600 \
  --set global.hosts.domain=example.local \
  --set global.ingress.tls.secretName=example-local-tls \
  --set global.ingress.acme=false \
  --set nginx.service.loadBalancerIP=X.X.X.X \
  --set kube-lego.enabled=false \
  --set gitlab.migrations.initialRootPassword="example-password"
```

A complete list  of command line options can be found [here](./command-line-options.md)

## PostgreSQL

By default we use a single node PostgreSQL instance for deployments. This postgres instance is not production ready and should not be used in production.

To use an external database follow the [advanced database docs](../advanced/external-db/README.md)

## Monitoring the Deployment

This will output the list of resources installed once the deployment finishes which may take 5-10 minutes.

The status of the deployment can be checked by running `helm status gitlab` which can also be done while
the deployment is taking place if you run the command in another terminal.

[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
