# TLS options

This chart is capable of doing TLS termination using the nginx Ingress controller. You have the choice of how to
acquire the TLS certificates for your deployment. Extensive details can be found in [global Ingress settings](../charts/globals.md#configure-ingress-settings).

## Option 1: cert-manager and Let's Encrypt

Let’s Encrypt is a free, automated, and open Certificate Authority. Certificates can be automatically requested
using various tools. This chart comes ready to integrate with a popular choice [cert-manager](https://github.com/jetstack/cert-manager).

*If you are already using cert-manager*, you can use `global.ingress.annotations` to configure [appropriate annotations][cm-annotations] for your cert-manager deployment.

*If you don't already have cert-manager installed in your cluster*, you can install and configure it as a dependency of this chart.

### Internal cert-manager and Issuer

```
helm repo update
helm dep update
helm install ...
  --set certmanager-issuer.email=you@example.com
```

Installing certmanager is controlled by the `certmanager.install` setting, and using it in the charts is controlled by the
`global.ingress.configureCertmanager` setting. Both of these are `true` by default, so only the issuer email needs to be
provided by default.

### External cert-manager and internal Issuer

It is possible to make use of an external `cert-manager` but provide an Issuer as a part of this chart.

```
helm install ...
  --set certmanager.install=false \
  --set certmanager-issuer.email=you@example.com \
  --set global.ingress.annotations."kubernetes\.io/tls-acme"=true
```

### External cert-manager and Issuer (external)

To make use of an external `cert-manager` and `Issuer` resource you must provide several items, so that self-signed certificates
are not activated.

1. Annotations to activate the external `cert-manager` (see [documentation](cm-annotations) for further details)
1. Names of TLS secrets for each service (this deactivates [self-signed behaviors](#option-4-use-auto-generated-self-signed-wildcard-certificate))

```
helm install ...
  --set cert-manager.install=false \
  --set global.ingress.configureCertmanager=false \
  --set global.ingress.annotations."kubernetes\.io/tls-acme"=true \
  --set gitlab.unicorn.ingress.tls.secretName=RELEASE-gitlab-tls \
  --set registry.ingress.tls.secretName=RELEASE-registry-tls \
  --set minio.ingress.tls.secretName=RELEASE-minio-tls
```

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

## Option 3: Use individual certificate per service

Add your full chain certificates to the cluster as secrets, and then pass those secret names to each ingress.

```
helm install ...
  --set certmanager.install=false \
  --set global.ingress.configureCertmanager=false \
  --set gitlab.unicorn.ingress.tls.secretName=RELEASE-gitlab-tls \
  --set registry.ingress.tls.secretName=RELEASE-registry-tls \
  --set minio.ingress.tls.secretName=RELEASE-minio-tls
```

## Option 4: Use auto-generated self-signed wildcard certificate

These charts also provide the capability to provide a auto-generated self-signed wildcard certificate.
This can be useful in environments where Let's Encrypt is not an option, but security via SSL is stil
desired. This functionality is provided by the [shared-secrets](../charts/shared-secrets/README.md) chart.

> **Note**: The `gitlab-runner` chart does not function properly with self-signed certificates. We recommend
disabling it, as shown below.

```
helm install ...
  --set certmanager.install=false \
  --set global.ingress.confgureCertmanager=false \
  --set gitlab-runner.install=false
```

The `shared-secrets` chart will then produce a CA certificate and wildcard certificate for use by all externally
accessible services. The secrets containing these will be `RELEASE-wildcard-tls` and `RELEASE-wildcard-tls-ca`.
The `RELEASE-wildcard-tls-ca` contains the public CA certificate that can be distributed to users and systems that
will access the deployed GitLab instance.

[cm-annotations]: https://github.com/jetstack/cert-manager/blob/master/docs/reference/ingress-shim.rst#supported-annotations