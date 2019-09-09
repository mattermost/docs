# Installing GitLab using Helm

NOTE: **Note**:
There are currently [known limitations](../index.md#limitations)
when using this chart, and not all features of GitLab are available.

Install GitLab on Kubernetes with the cloud native GitLab Helm chart.

## Requirements

In order to deploy GitLab on Kubernetes, the following are required:

1. kubectl 1.11 or higher, compatible with your cluster
   ([+/- 1 minor release from your cluster](https://kubernetes.io/docs/tasks/tools/install-kubectl/#before-you-begin)).
1. Helm 2.12 or higher. **Note** Helm 3 is [not yet supported](https://gitlab.com/gitlab-org/charts/gitlab/issues?label_name%5B%5D=Helm+3).
1. A Kubernetes cluster, version 1.11 or higher. 6vCPU and 16GB of RAM is recommended.

## Environment setup

Before proceeding to deploying GitLab, you need to prepare your environment.

### Tools

`helm` and `kubectl` need to be [installed on your computer](tools.md).

### Cloud cluster preparation

NOTE: **Note**:
[Kubernetes 1.11 or higher is required](#requirements), due to the usage of certain
Kubernetes features.

Follow the instructions to create and connect to the Kubernetes cluster of your
choice:

- [Google Kubernetes Engine](cloud/gke.md)
- [Amazon EKS](cloud/eks.md)
- [OpenShift Origin](cloud/openshift.md)
- Azure Container Service - Documentation to be added.
- Pivotal Container Service - Documentation to be added.
- On-Premises solutions - Documentation to be added.

## Deploying GitLab

With the environment set up and configuration generated, you can now proceed to
the [deployment of GitLab](deployment.md).

## Upgrading GitLab

If you are upgrading an existing Kubernetes installation, follow the
[upgrade documentation](upgrade.md) instead.

## Migrating from Omnibus GitLab to Kubernetes

To migrate your existing Omnibus GitLab instance to your Kubernetes cluster,
follow the [migration documentation](migration/index.md).
