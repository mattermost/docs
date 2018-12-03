# Installing GitLab using Helm

NOTE: **Note**:
There are currently [known limitations](../../index.md#known-issues-and-limitations)
when using this chart, and not all features of GitLab are available.

Install GitLab on Kubernetes with the cloud native GitLab Helm chart. Follow the instructions below to get started.

## Requirements

1. A Kubernetes cluster, version 1.8 or higher.
1. [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl) version 1.8 or higher, compatible with your cluster. ([+/- 1 minor release from your cluster](https://kubernetes.io/docs/tasks/tools/install-kubectl/#before-you-begin))
1. [`Helm`](https://docs.helm.sh/using_helm/#installing-helm) `v2.x`, we require 2.9 or higher. See also our [documentation on Helm](../helm/index.md)

## Get started with GitLab

### 1. Prerequisites

In order to install GitLab in a Kubernetes cluster, there are a few required tools. To get started, [prepare your computer](tools.md).

### 2. Where do you want to install GitLab?

NOTE: **Note**:
[Kubernetes 1.8 or higher is required](#requirements), due to the usage of certain
Kubernetes features.

Follow the instructions to connect to the Kubernetes cluster of your choice:

- [Google Kubernetes Engine](../cloud/gke.md)
- [Amazon EKS](../cloud/eks.md)
- [OpenShift Origin](../cloud/openshift.md)
- Azure Container Service - Documentation to be added.
- Pivotal Container Service - Documentation to be added.
- On-Premises solutions - Documentation to be added.

### 3. Deploy

With the environment setup and configuration generated, we can proceed to
[deployment](deployment.md).

If you are upgrading an existing installation follow [upgrade docs](upgrade.md).

### 4. Migrate data from an existing GitLab

To migrate your existing GitLab instance to your deployed Kubernetes GitLab instance, follow the [migration documentation](./migration/index.md).
