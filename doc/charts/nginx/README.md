# Using NGINX

We provide a complete NGINX deployment to be used as an Ingress controller. Not all Kubernetes providers natively support the NGINX [Ingress][kubernetes-ingress], to ensure compatibility.

This chart provides two services: `nginx` which is `nginx-ingress-controller`,
and `nginx-default-backend` which is `defaultbackend` from the [`gcr.io/google_containers`][] registry.

## Configuring NGINX

See [documentation in the nginx chart](../../charts/nginx/README.md) for configuration details.

### Global Settings

We share some common global settings among our charts. See the [Globals Documentation][globals] for common configuration
options, such as GitLab and Registry hostnames.

## Configure hosts using the Global Settings.

The hostnames for the GitLab Server and the Registry Server can be configured using our chart [Global Settings][globals]

[globals]: ../globals.md

[registry]: https://hub.docker.com/_/registry/
[kubernetes-ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/#tls
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
[helm]: https://helm.sh
[kubernetes-ingress-nginx-configuration]: https://github.com/kubernetes/ingress/blob/master/controllers/nginx/configuration.md
[RBAC]: https://kubernetes.io/docs/admin/authorization/rbac/
