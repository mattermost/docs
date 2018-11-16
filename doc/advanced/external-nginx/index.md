# External nginx ingress controller

This chart configures `Ingress` resources for use with the official
[ingress-nginx](https://github.com/kubernetes/ingress-nginx) implementation. The
nginx ingress controller is deployed as a part of this chart. If you want to
reuse an existing nginx ingress controller already available in your cluster,
this guide will help.

## TCP services in the external ingress controller

The gitlab-shell component requires TCP traffic to pass through on
port 22 (by default; this can be changed). Ingress does not directly support TCP services, so some additonal configuration is necessary. Your nginx ingress controller may have been [deployed directly](https://github.com/kubernetes/ingress-nginx/blob/master/docs/deploy/index.md) (i.e. with a Kubernetes spec file) or through the [official Helm chart](https://github.com/helm/charts/tree/master/stable/nginx-ingress). The configuration of the TCP pass through will differ depending on the deployment approach.

### Direct deployment

In a direct deployment, the nginx ingress controller handles configuring TCP services with a
`ConfigMap` (see docs [here](https://github.com/kubernetes/ingress-nginx/blob/master/docs/user-guide/exposing-tcp-udp-services.md)).
Assuming your Gitlab chart is deployed to the namespace `gitlab` and your helm
release is named `mygitlab`, your `ConfigMap` should be something like this:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: tcp-configmap-example
data:
  22: "gitlab/mygitlab-gitlab-shell:22"
```

After you have that `ConfigMap`, you can enable it as described in the nginx
ingress controller [docs](https://github.com/kubernetes/ingress-nginx/blob/master/docs/user-guide/exposing-tcp-udp-services.md)
using the `--tcp-services-configmap` option.

```yaml
args:
  - /nginx-ingress-controller
  - --tcp-services-configmap=gitlab/tcp-configmap-example
```

Finally make sure that the `Service` for your nginx ingress controller is exposing
port 22 in addition to 80 and 443.

### Helm deployment

If you have installed or will install the nginx ingress controller via it's [Helm chart](https://github.com/helm/charts/tree/master/stable/nginx-ingress), then you will need to add a value to the chart via the command line:

```bash
--set tcp.22="gitlab/mygitlab-gitlab-shell:22"
```

or a `values.yaml` file:

```yaml
tcp:
  22: "gitlab/mygitlab-gitlab-shell:22"
```

The format for the value is the same as describe above in the "Direct Deployment" section.

## Customize the gitlab ingress options

The nginx ingress controller uses an annotation to mark which ingress controller
will service a particular `Ingress` (see [docs](https://github.com/kubernetes/ingress-nginx#annotation-ingressclass)).
You can configure the ingress class to use with this chart using the
`global.ingress.class` setting. Make sure to set this in your helm options.

```bash
--set global.ingress.class=myingressclass
```

While not necessarily required, if you're using an external ingress controller, you will likely want to
disable the ingress controller that is deployed by default with this chart:

```bash
--set nginx-ingress.enabled=false
```

## Custom certifcate management
The full scope of your TLS options are documented [elswhere](https://gitlab.com/charts/gitlab/blob/master/doc/installation/tls.md).

If you are using an external ingress controller, you may also be using an external cert-manager instance
or managing your certificates in some other custom manner. The full documentation around your TLS options is [here](https://gitlab.com/charts/gitlab/blob/master/doc/installation/tls.md),
however for the purposes of this discussion, here are the two values that would need to be set to disable the cert-manager chart and tell 
the gitlab component charts to NOT look for the built in certificate resources:

```bash
--set certmanager.install=false
--set global.ingress.configureCertmanager=false
```
