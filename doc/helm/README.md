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

Initialize Helm, and install the Tiller service with `helm init`. If your cluster already had Tiller, run `helm init --upgrade` to ensure that the deployed version of Tiller matches.


[helm]: https://helm.sh
[helm-using]: https://docs.helm.sh/using_helm
[k8s-io]: https://kubernetes.io/
