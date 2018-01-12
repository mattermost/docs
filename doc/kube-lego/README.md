# Let's Encrypt via kube-lego

This chart is capable of making use of Let's Encrypt integration via [kube-lego][]. To make use of `kube-lego`, deploy it before you deploy the chart.

## Configuration

[kube-lego.yaml](kube-lego.yaml) is included in this directory. Copy this file, and make small edits.

```
cp doc/kube-lego/kube-lego.yaml .
```

Edit the file, filling in the following properties:
- `config.LEGO_EMAIL` should be replaced with a valid email address.
- `config.LEGO_URL` should be uncommented **if** you desire production ready certificates. This defaults to the [staging environment](https://letsencrypt.org/docs/staging-environment/), which produces untrusted but valid certificates.
- `rbac.create` should be set to `true` if using a cluster with [RBAC][] enabled.

## Installation

To install the `kube-lego` chart, with the configuation as prepared:

```
helm install -f kube-lego.yaml stable/kube-lego --version 0.3.0
```

This will install `kube-lego`, as well as create the needed [RBAC][] configuration for it, if `rbac.create` was set to `true` as described in [configuration](#configuration).

[kube-lego]: https://github.com/kubernetes/charts/blob/master/stable/kube-lego/README.md
[RBAC]: https://kubernetes.io/docs/admin/authorization/rbac/
[namespace]: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
