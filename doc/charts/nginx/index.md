# Using NGINX

We provide a complete NGINX deployment to be used as an Ingress Controller. Not all
Kubernetes providers natively support the NGINX [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/#tls),
to ensure compatibility.

This chart provides two services: `nginx` and `nginx-default-backend`, which are `nginx-ingress-controller`
and `defaultbackend` from the [Google Container Registry](https://gcr.io/google_containers).

## Configuring NGINX

See [NGINX chart documentation](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/charts/nginx/index.md)
for configuration details.

### Global Settings

We share some common global settings among our charts. See the [Globals Documentation](../globals.md)
for common configuration options, such as GitLab and Registry hostnames.

## Configure hosts using the Global Settings

The hostnames for the GitLab Server and the Registry Server can be configured using
our [Global Settings](../globals.md) chart.
