# Developing for Helm

This document is intended to provide an overview of working with [Helm][helm] for [Kubernetes][k8s-io], and is targetted at using Kubernetes in [Minikube](../minikube/README.md). This document will be based on the official [using helm][helm-using] documentation.

## Helm is not stand alone

To make use of Helm, you must have a [Kubernetes][k8s-io] cluster.

Helm is actually two parts, `helm` client and `tiller` server inside Kubernetes

## Getting Helm

You can get Helm from the project's [releases page](https://github.com/kubernetes/helm/releases), or follow other options under the official documentation of [Installing Helm](https://docs.helm.sh/using_helm/#installing-helm).

## Initialize Helm and Tiller

Check that `kubectl` will be tagetting your Minikube install.

- Check the current cluster: `kubectl cluster-info`, which should be `minikube`
- If the current cluster is not `minikube`
  - List available clusters for `kubectl`: `kubectl config get-clusters`
  - Change to `minikube`: `kubectl config set-cluster minikube`

Initialize Helm, and install the Tiller service with `helm init`. If your cluster
already had Tiller, run `helm init --upgrade` to ensure that the deployed version of Tiller matches.

## Useful documentation for Helm

The Build Team has a [training presentation for Helm Charts](https://docs.google.com/presentation/d/1CStgh5lbS-xOdKdi3P8N9twaw7ClkvyqFN3oZrM1SNw/present)

### Templates

Templating in Helm is done via golang's [text/template][] and [sprig][].

Some information on how all the inner workings behave:
- [Functions and Pipelines][helm-func-pipeline]
- [Subcharts and Globals][helm-subchart-global]

### Tips and Tricks

https://github.com/kubernetes/helm/blob/master/docs/charts_tips_and_tricks.md

[helm]: https://helm.sh
[helm-using]: https://docs.helm.sh/using_helm
[k8s-io]: https://kubernetes.io/

[text/template]: https://golang.org/pkg/text/template/
[sprig]: https://godoc.org/github.com/Masterminds/sprig
[helm-func-pipeline]: https://github.com/kubernetes/helm/blob/master/docs/chart_template_guide/functions_and_pipelines.md
[helm-subchart-global]: https://github.com/kubernetes/helm/blob/master/docs/chart_template_guide/subcharts_and_globals.md
