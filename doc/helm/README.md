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

If your cluster has Role Based Access Control (RBAC) enabled, you will need to [grant permissions to Helm Tiller first](#preparing-for-helm-with-rbac) and [deploy it with a service account](#deploy-helm-tiller-with-a-service-account).

If your cluster does not have RBAC enabled, you can initialize Helm
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

### Preparing for Helm with RBAC

> **Note**: Ensure you have kubectl installed and it is up to date. Older versions do not have support for RBAC and will generate errors.

When RBAC is enabled, Helm's Tiller will need to be granted permissions to perform operations. These instructions grant cluster wide permissions, however for more advanced deployments [permissions can be restricted to a single namespace](https://docs.helm.sh/using_helm/#example-deploy-tiller-in-a-namespace-restricted-to-deploying-resources-only-in-that-namespace). To grant access to the cluster, we will create a new `tiller` service account and bind it to the `cluster-admin` role.

Create a file called `rbac-config.yaml` containing the role and binding, an example is [available here](examples/rbac-config.yaml).

This role and binding then needs to be applied before Helm can run using `kubectl`. Ensure [kubectl is installed and up to date](https://kubernetes.io/docs/tasks/tools/install-kubectl/), as older versions do not support RBAC.

Depending on the Kubernetes provider, you may need to provide additional authentication to kubectl beyond your user account:
* [Creating ClusterRoles on GKE with kubectl](#creating-clusterroles-on-gke-with-kubectl)

#### Creating ClusterRoleBindings on GKE with kubectl

On GKE, your standard user account does not have permissions to provision new ClusterRoles. You will need to instead utilize the `admin` account that was provisioned automatically during cluster setup. To do this, we will use the `gcloud` utility to display the information on the cluster:

```
gcloud container clusters describe cluster_name --zone cluster_zone
```

This command will output detailed information on the cluster, including the admin credentials that were created. We need the password to authenticate with `kubectl` and create the role:

```
...
  password: xxxxxxxxxxxxxx
  username: admin
...
```

With the credentials on hand, we can now provision the role and binding using the YML file created [earlier](#preparing-for-helm-with-rbac):

```
kubectl --username=admin --password=xxxxxxxxxxxxxx create -f rbac-config.yaml
```

### Deploy Helm Tiller with a service account

Now that we have a ServiceAccount and ClusterRoleBinding for Tiller, we are ready to deploy it. To do so we will need to specify the desired service account we created earlier:

```
helm init --service-account tiller
```

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
