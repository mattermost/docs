# External nginx ingress controller

This chart configures `Ingress` resources for use with the official
[ingress-nginx](https://github.com/kubernetes/ingress-nginx) implementation. The
nginx ingress controller is deployed as a part of this chart. If you want to
reuse an existing nginx ingress controller already available in your cluster,
this guide will help.

## TCP services

The docker registry component requires access TCP traffic to pass through on
port 22. The nginx ingress controller handles configuring TCP services with a
`ConfigMap` (see docs [here](https://github.com/kubernetes/ingress-nginx/blob/master/docs/user-guide/exposing-tcp-udp-services.md)).
Assuming your Gitlab chart is deployed to the namespace `gitlab` and your helm
release is named `mygitlab` your `ConfigMap` should be something like this:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: tcp-configmap-example
data:
  22: "gitlab/mygitlab-gitlab-shell:22"
```

After you have that `ConfigMap` you can enable that as describe in the nginx
ingress controller [docs](https://github.com/kubernetes/ingress-nginx/blob/master/docs/user-guide/exposing-tcp-udp-services.md)
using the `--tcp-services-configmap` option.

Finally make sure that the `Service` for your nginx ingress controller is exposing
port 22 in addition to 80 and 443.

## Customize your ingress.class

The nginx ingress controller uses an annotation to mark which ingress controller
will service a particular `Ingress` (see [docs](https://github.com/kubernetes/ingress-nginx#annotation-ingressclass)).
You can configure the ingress class to use with this chart using the
`global.ingress.class` setting. Make sure to set this in your helm options.

```
helm upgrade --install --reuse-values \
  --set global.ingress.class=myingressclass
```
