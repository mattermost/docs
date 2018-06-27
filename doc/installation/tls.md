# TLS options

This chart is capable of doing TLS termination using the nginx Ingress controller. You have the choice of how to
acquire the TLS certificates for your deployment.

## Option 1: cert-manager and Let's Encrypt

Let’s Encrypt is a free, automated, and open Certificate Authority. Certificates can be automatically requested
using various tools. This chart comes ready to integrate with a popular choice [cert-manager](https://github.com/jetstack/cert-manager).

*If you are already using cert-manager*, you can use `global.ingress.annotations` to configure [appropriate annotations](https://github.com/jetstack/cert-manager/blob/master/docs/user-guides/ingress-shim.md) for your cert-manager deployment.

*If you don't already have cert-manager installed in your cluster*, you can install and configure it as a dependency of this chart.

### Get the cert-manager chart

```
helm dep update
```

### Install with cert-manager enabled and configured

```
helm install ...
  --set certmanager-issuer.email=you@example.local
```

Intalling certmanager is controlled by the `certmanager.install` setting, and using it in the charts is controlled by the
`global.ingress.configureCertmanager` setting. Both of these are true by default, so only the issuer email needs to be
provided by default.

## Option 2: Use your own wildcard certificate

Add your full chain certificate and key to the cluster as a `Secret`, e.g.:

```
kubectl create secret tls <tls-secret-name> --cert=<path/to-full-chain.crt> --key=<path/to.key>
```

Include the option to
```
helm install ...
  --set certmanager.install=false \
  --set global.ingress.configureCertmanager=false \
  --set global.ingress.tls.secretName=<tls-secret-name>
```
