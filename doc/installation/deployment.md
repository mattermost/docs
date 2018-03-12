# Deploy

In order to deploy, make sure you have done the following:

- `Secrets` are created - [secrets documentation](secrets.md)
- You have the static-ip for the `loadBalancerIP`
- DNS entry made for the domain pointing to the `loadBalancerIP`
- `initialRootPassword` - created or chosen at random

For these examples:

- We will use domain `example.local` as our `DNS entry`, and expect our hostnames
  to be: `gitlab.example.local`, `registry.example.local`.
- We will use `X.X.X.X` as our `loadBalancerIP`
- Our `initialRootPassword` will be `example-password`

To deploy, we'll run `helm install` with our settings, from the
root of this repository. Ensure you are at the root of your git checkout!

## Deploy with Let's Encrypt

```
helm install . --name gitlab --timeout 600 \
  --set global.hosts.domain=example.local \
  --set nginx.service.loadBalancerIP=X.X.X.X \
  --set kube-lego.config.LEGO_EMAIL=user@example.local \
  --set gitlab.migrations.initialRootPassword="example-password"
```

## Deploy with Custom Certificates

```
helm install . --name gitlab --timeout 600 \
  --set global.hosts.domain=example.local \
  --set global.hosts.tls.secretName=example-local-tls \
  --set nginx.service.loadBalancerIP=X.X.X.X \
  --set nginx.ingress.acme=false \
  --set kube-lego.enabled=false \
  --set gitlab.migrations.initialRootPassword=<Your Password>
```

A complete list  of command line options can be found [here](./command-line-options.md)

## Monitoring Deployment

This will output the list of resources installed once the deployment finishes which may take 5-10 minutes.

The status of the deployment can be checked by running `helm status gitlab` which can also be done while
the deployment is taking place if you run the command in another terminal.

[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
