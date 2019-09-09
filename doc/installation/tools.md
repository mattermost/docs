# Required tools

Before deploying GitLab to your Kubernetes cluster, there are some tools you
must have installed locally.

## kubectl

kubectl is the tool that talks to the Kubernetes API. kubectl 1.11 or higher is
required and it needs to be compatible with your cluster
([+/- 1 minor release from your cluster](https://kubernetes.io/docs/tasks/tools/install-kubectl/#before-you-begin)).

[> Install kubectl locally by following the Kubernetes documentation.](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl)

The server version of kubectl cannot be obtained until we connect to a
cluster. Proceed with setting up Helm.

## Helm

Helm is the package manager for Kubernetes. The `gitlab` chart is only tested and
supported with Helm `v2` and helm 2.12 or higher is required. Helm `v1` is
explicitly not supported. Helm `v3` is not yet supported, and open issues can be
found under our [Helm 3 issue label](https://gitlab.com/gitlab-org/charts/gitlab/issues?label_name%5B%5D=Helm+3).

Helm consists of two parts, the `helm` (client) installed locally, and `tiller`
(server) installed inside Kubernetes.

NOTE: **Note**:
If you are not able to run tiller in your cluster, for example on OpenShift,
it's possible to use [tiller locally](#local-tiller) and avoid deploying it
into the cluster. This should only be used when tiller cannot be normally deployed.

### Getting Helm

You can get Helm from the project's [releases page](https://github.com/kubernetes/helm/releases),
or follow other options under the official documentation of
[installing Helm](https://docs.helm.sh/using_helm/#installing-helm).

Tiller is deployed into the cluster and interacts with the Kubernetes API to
deploy your applications. If role based access control (RBAC) is enabled, Tiller
will need to be [granted permissions](#preparing-for-helm-with-rbac) to allow it
to talk to the Kubernetes API.

If RBAC is not enabled, skip to [initializing Helm](#initializing-helm).

If you are not sure whether RBAC is enabled in your cluster, or to learn more,
read through our [RBAC documentation](rbac.md).

### Preparing for Helm with RBAC

NOTE: **Note**:
Ensure you have `kubectl` installed and it's up to date. Older versions do not
have support for RBAC and will generate errors.

Helm's Tiller will need to be granted permissions to perform operations. These
instructions grant cluster wide permissions, however for more advanced deployments
[permissions can be restricted to a single namespace](https://docs.helm.sh/using_helm/#example-deploy-tiller-in-a-namespace-restricted-to-deploying-resources-only-in-that-namespace).

To grant access to the cluster, we will create a new `tiller` service account
and bind it to the `cluster-admin` role:

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

For ease of use, these instructions will utilize the
[sample YAML file](examples/rbac-config.yaml) in this repository. To apply the
configuration, we first need to connect to the cluster.

#### Connecting to the GKE cluster

The command to connect to the cluster can be obtained from the
[Google Cloud Platform Console](https://console.cloud.google.com/kubernetes/list)
by the individual cluster, by looking for the **Connect** button in the clusters
list page.

Alternatively, use the command below, filling in your cluster's information:

```sh
gcloud container clusters get-credentials <cluster-name> --zone <zone> --project <project-id>
```

#### Connecting to an EKS cluster

For the most up to date instructions, follow the Amazon EKS documentation on
[connecting to a cluster](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html#eks-configure-kubectl).

#### Connect to a local minikube cluster

If you are doing local development, you can use `minikube` as your
local cluster. If `kubectl cluster-info` is not showing `minikube` as the current
cluster, use `kubectl config set-cluster minikube` to set the active cluster.

### Upload the RBAC config

#### Upload the RBAC config in GKE

For GKE, you need to grab the admin credentials:

```sh
gcloud container clusters describe <cluster-name> --zone <zone> --project <project-id> --format='value(masterAuth.password)'
```

This command will output the admin password. We need the password to authenticate
with `kubectl` and create the role.

We will also create an admin user for this cluster.  Use a name you prefer but
for this example we will include the cluster's name in it:

```sh
CLUSTER_NAME=name-of-cluster
kubectl config set-credentials $CLUSTER_NAME-admin-user --username=admin --password=xxxxxxxxxxxxxx
kubectl --user=$CLUSTER_NAME-admin-user create -f https://gitlab.com/gitlab-org/charts/gitlab/raw/master/doc/installation/examples/rbac-config.yaml
```

#### Upload the RBAC config in non-GKE clusters

For other clusters like Amazon EKS, you can directly upload the RBAC configuration:

```sh
kubectl create -f https://gitlab.com/gitlab-org/charts/gitlab/raw/master/doc/installation/examples/rbac-config.yaml
```

### Initializing Helm

Finally, deploy Helm Tiller with a service account:

```sh
helm init --service-account tiller
```

If your cluster previously had Helm/Tiller installed, run the following command
to ensure that the deployed version of Tiller matches the local Helm version:

```sh
helm init --upgrade --service-account tiller
```

## Next steps

Once kubectl and Helm are configured, you can continue to configuring your
[Kubernetes cluster](index.md#cloud-cluster-preparation).

## Additional information

The Distribution Team has a [training presentation for Helm Charts](https://docs.google.com/presentation/d/1CStgh5lbS-xOdKdi3P8N9twaw7ClkvyqFN3oZrM1SNw/present).

### Templates

Templating in Helm is done via golang's [text/template](https://golang.org/pkg/text/template/)
and [sprig](https://godoc.org/github.com/Masterminds/sprig).

Some information on how all the inner workings behave:

- [Functions and Pipelines](https://github.com/kubernetes/helm/blob/master/docs/chart_template_guide/functions_and_pipelines.md)
- [Subcharts and Globals](https://github.com/kubernetes/helm/blob/master/docs/chart_template_guide/subcharts_and_globals.md)

### Tips and tricks

Helm repository has some additional information on developing with helm in it's
[tips and tricks section](https://github.com/kubernetes/helm/blob/master/docs/charts_tips_and_tricks.md).

[helm-using]: https://docs.helm.sh/using_helm

### Local tiller

CAUTION: **Not recommended:**
This method is not well supported, but should work.

If you are not able to run tiller in your cluster,
[a script](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/bin/localtiller-helm)
is included that should allow you to use helm with running tiller in your cluster.
The script uses your personal Kubernetes credentials and configuration to apply
the chart.

To use the script, skip this entire section about initializing helm. Instead,
make sure you have Docker installed locally and run:

```sh
bin/localtiller-helm --client-only
```

After that, you can substitute `bin/localtiller-helm` anywhere these
instructions direct you to run `helm`.
