# TLS options

This chart is capable of doing TLS termination using the nginx Ingress controller. You have the choice of how to
acquire the TLS certificates for your deployment.

## Option 1: cert-manager and Let's Encrypt

Let’s Encrypt is a free, automated, and open Certificate Authority. Certificates can be automatically requested
using various tools. This chart comes ready to integrate with a popular choice [cert-manager](https://github.com/jetstack/cert-manager).

*If you are already using cert-manager*, you can use `globals.ingress.annotations` to configure [appropriate annotations](https://github.com/jetstack/cert-manager/blob/master/docs/user-guides/ingress-shim.md) for your cert-manager deployment.

*If you don't already have cert-manager installed in your cluster*, you can install and configure it as a dependency of this chart. Due
to limitations in `helm`, this is a multi-step process.

### Get the cert-manager chart

```
helm dep update
```

### Install normally with cert-manager enabled

```
helm install ...
  --set certmanager.install=true
```

### Upgrade to configure cert-manager

```
helm upgrade ...
  --reuse-values \
  --set certmanager.issuer.email=you@example.local \
  --set certmanager.install=true \
  --set global.ingress.configureCertmanager=true
```

## Option 2: Use your own wildcard certificate

Add you certificate to the cluster as a `Secret`

```
kubectl --namespace yournamespace create secret tls <name> --cert=<path/to.crt> --key=<path/to.key>
```

Include the option to 
```
helm install ...
  --namespace yournamespace \
  --set
