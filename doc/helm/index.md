# Helm

This document is intended to provide an overview of working with [Helm][helm] for [Kubernetes][k8s-io].

## Supported versions

This chart currently only tested and support with Helm `v2`.

Helm `v1` is explicitly not supported. Helm `v3` may work, but there has been and will not be any testing for the time being.

## Helm is not stand-alone

To make use of Helm, you must have a [Kubernetes][k8s-io] cluster. Follow the [dependencies documentation](../installation/dependencies.md)
to ensure you can access your cluster using `kubectl`.

Helm consists of two parts, `helm` client and `tiller` server inside Kubernetes.

> **Note**: If you are not able to run tiller in your cluster, for example on OpenShift, it is possible to use [tiller locally](#local-tiller) and avoid deploying it into the cluster. This should only be used when Tiller cannot be normally deployed.

# Getting Helm

> **Note**: We support using Helm versions in the 2.x line with 2.9.0 being our minimum supported version.

You can get Helm from the project's [releases page](https://github.com/kubernetes/helm/releases), or follow other options under the official documentation of [Installing Helm](https://docs.helm.sh/using_helm/#installing-helm).

# Initialize Helm and Tiller

Tiller is deployed into the cluster and interacts with the Kubernetes API to deploy your applications. If role based access control (RBAC) is enabled, Tiller will need to be [granted permissions](#preparing-for-helm-with-rbac) to allow it to talk to the Kubernetes API.

If RBAC is not enabled, skip to [initalizing Helm](#initialize-helm).

If you are not sure whether RBAC is enabled in your cluster, or to learn more, read through our [RBAC documentation](../installation/rbac.md).

## Preparing for Helm with RBAC

> **Note**: Ensure you have kubectl installed and it is up to date. Older versions do not have support for RBAC and will generate errors.

Helm's Tiller will need to be granted permissions to perform operations. These instructions grant cluster wide permissions, however for more advanced deployments [permissions can be restricted to a single namespace](https://docs.helm.sh/using_helm/#example-deploy-tiller-in-a-namespace-restricted-to-deploying-resources-only-in-that-namespace).

To grant access to the cluster, we will create a new `tiller` service account and bind it to the `cluster-admin` role:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
```

For ease of use, these instructions will utilize the [sample YAML file](examples/rbac-config.yaml) in this repository. To apply the configuration, we first need to connect to the cluster.

### Connect to the cluster

You can use:

* [GKE cluster](#connect-to-gke-cluster)
* [EKS cluster](#connect-to-eks-cluster)
* [Local minikube cluster](#connect-to-local-minikube-cluster)

#### Connect to GKE cluster

The command for connection to the cluster can be obtained from the [Google Cloud Platform Console][gcp-k8s]
by the individual cluster.

Look for the **Connect** button in the clusters list page.

**Or**

Use the command below, filling in your cluster's informtion:

```
gcloud container clusters get-credentials <cluster-name> --zone <zone> --project <project-id>
```

#### Connect to EKS cluster

For the most up to date instructions, follow the Amazon EKS documentation on [connecting to a cluster](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html#eks-configure-kubectl).

#### Connect to local minikube cluster

If you are doing local development, you can use `minikube` as your
local cluster. If `kubectl cluster-info` is not showing `minikube` as the current
cluster, use `kubectl config set-cluster minikube` to set the active cluster.

### Upload the RBAC config


#### Upload the RBAC config as an admin user (GKE)

For GKE, you need to grab the admin credentials:

```
gcloud container clusters describe <cluster-name> --zone <zone> --project <project-id> --format='value(masterAuth.password)'
```

This command will output the admin password. We need the password to authenticate with `kubectl` and create the role.

We will also create an admin user for this cluster.  Use a name you prefer but
for this example we will include the cluster's name in it.

```
CLUSTER_NAME=name-of-cluster
kubectl config set-credentials $CLUSTER_NAME-admin-user --username=admin --password=xxxxxxxxxxxxxx
kubectl --user=$CLUSTER_NAME-admin-user create -f https://gitlab.com/charts/gitlab/raw/master/doc/helm/examples/rbac-config.yaml
```

#### Upload the RBAC config

For other clusters like Amazon EKS, you can direclty upload the RBAC configuration.

kubectl create -f https://gitlab.com/charts/gitlab/raw/master/doc/helm/examples/rbac-config.yaml

## Initialize Helm

Deploy Helm Tiller with a service account

```
helm init --service-account tiller
```

If your cluster
previously had Helm/Tiller installed, run the following to ensure that the deployed version of Tiller matches the local Helm version:

```
helm init --upgrade --service-account tiller
```

### Patching Helm Tiller for EKS

Helm Tiller requires a flag to be enabled to work properly on EKS:

`kubectl -n kube-system patch deployment tiller-deploy -p '{"spec": {"template": {"spec": {"automountServiceAccountToken": true}}}}'`

# Additional Information

The Distribution Team has a [training presentation for Helm Charts](https://docs.google.com/presentation/d/1CStgh5lbS-xOdKdi3P8N9twaw7ClkvyqFN3oZrM1SNw/present).

## Templates

Templating in Helm is done via golang's [text/template][] and [sprig][].

Some information on how all the inner workings behave:
- [Functions and Pipelines][helm-func-pipeline]
- [Subcharts and Globals][helm-subchart-global]

## Tips and Tricks

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

## Local tiller

_This is not recommended_

If you are not able to run tiller in your cluster, this chart includes a script
that should allow you to use helm with running tiller in your cluster. The
script uses your personal Kubernetes credentials and configuration to apply
the chart. This method is not well supported, but should work.

To use the script, skip this entire section about initializing helm. Instead,
make sure you have Docker installed locally and run
`bin/localtiller-helm --client-only`. After that, you can substitute
`bin/localtiller-helm` anywhere these instructions direct you to run `helm`.
