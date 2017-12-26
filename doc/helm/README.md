# Helm

This document is intended to provide an overview of working with [Helm][helm] for [Kubernetes][k8s-io], and is targetted at using Kubernetes in [Minikube](../minikube/README.md). This document will be based on the official [using helm][helm-using] documentation.

## Helm is not stand-alone

To make use of Helm, you must have a [Kubernetes][k8s-io] cluster.

Helm consists of two parts, `helm` client and `tiller` server inside Kubernetes.

## Getting Helm

You can get Helm from the project's [releases page](https://github.com/kubernetes/helm/releases), or follow other options under the official documentation of [Installing Helm](https://docs.helm.sh/using_helm/#installing-helm).

## Initialize Helm and Tiller

Check which cluster `kubectl` is targeting.
You can find the current active cluster using the `kubectl cluster-info`
command. You can also list all available clusters with `kubectl config get-clusters`.

You can use:

* [GKE cluster](#connect-to-gke-cluster)
* [Local minikube cluster](#connect-to-local-minikube-cluster)

Once you are connected to a Kubernetes cluster, you can initialize Helm
using `helm init`. If your cluster
already had Tiller, run `helm init --upgrade` to ensure that the deployed version of Tiller matches.

At the time of writing this doc, the output of `helm version`:

```
$ helm version
Client: &version.Version{SemVer:"v2.7.0", GitCommit:"08c1144f5eb3e3b636d9775617287cc26e53dba4", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.5.1", GitCommit:"7cf31e8d9a026287041bae077b09165be247ae66", GitTreeState:"clean"}
```

### Connect to GKE cluster

The command for connection to the cluster can be obtained from the [Google Cloud Platform Console][gcp-k8s]
under the individual cluster. Look for `Connect to the cluster` link at the top
of the cluster properties page.

For example:

```
$ gcloud container clusters get-credentials <cluster-name> --zone <zone> --project <project-id>
$ kubectl get endpoints
NAME         ENDPOINTS           AGE
kubernetes   <cluster-ip>:443   22d
```

### Connect to local minikube cluster

If you are doing local development, you can use `minikube` as your
local cluster. If `kubectl cluster-info` is not showing `minikube` as the current
cluster, use `kubectl config set-cluster minikube` to set the active cluster.

## Additional Information

The Build Team has a [training presentation for Helm Charts](https://docs.google.com/presentation/d/1CStgh5lbS-xOdKdi3P8N9twaw7ClkvyqFN3oZrM1SNw/present).

### Templates

Templating in Helm is done via golang's [text/template][] and [sprig][].

Some information on how all the inner workings behave:
- [Functions and Pipelines][helm-func-pipeline]
- [Subcharts and Globals][helm-subchart-global]

### Tips and Tricks

Helm repository has some additional information on developing with helm in it's
[tips and tricks section](https://github.com/kubernetes/helm/blob/master/docs/charts_tips_and_tricks.md).


[helm]: https://helm.sh
[helm-using]: https://docs.helm.sh/using_helm
[k8s-io]: https://kubernetes.io/
[gcp-k8s]: https://console.cloud.google.com/kubernetes/list

[text/template]: https://golang.org/pkg/text/template/
[sprig]: https://godoc.org/github.com/Masterminds/sprig
[helm-func-pipeline]: https://github.com/kubernetes/helm/blob/master/docs/chart_template_guide/functions_and_pipelines.md
[helm-subchart-global]: https://github.com/kubernetes/helm/blob/master/docs/chart_template_guide/subcharts_and_globals.md
