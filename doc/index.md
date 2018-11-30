# GitLab cloud native Helm Chart

This is the official and recommended way to install GitLab on a cloud native environment.
For more information on other available GitLab Helm Charts, see the [charts overview](./charts/index.md).

## Introduction

The `gitlab` chart is the best way to operate GitLab on Kubernetes. This chart
contains all the required components to get started, and can scale to large deployments.

The default deployment includes:

- Core GitLab components: Unicorn, Shell, Workhorse, Registry, Sidekiq, and Gitaly
- Optional dependencies: Postgres, Redis, Minio
- An auto-scaling, unprivileged [GitLab Runner](https://docs.gitlab.com/runner/) using the Kubernetes executor
- Automatically provisioned SSL via [Let's Encrypt](https://letsencrypt.org/).

- [Charts](charts/index.md) (laid out as the charts are)
- [Example values.yaml files](https://gitlab.com/charts/gitlab/tree/master/examples)
- [Minikube](minikube/index.md)
- [Helm](helm/index.md)

## Limitations

Some features of GitLab are not currently available using the Helm chart:

- [GitLab Pages](https://gitlab.com/charts/gitlab/issues/37)
- [GitLab Geo](https://gitlab.com/charts/gitlab/issues/8)
- [No in-cluster HA database](https://gitlab.com/charts/gitlab/issues/48)
- MySQL will not be supported, as support is [deprecated within GitLab](https://docs.gitlab.com/omnibus/settings/database.html#using-a-mysql-database-management-server-enterprise-edition-only)

## Requirements

In order to deploy GitLab on Kubernetes, the following are required:

1. `helm` and `kubectl` [installed on your computer](installation/tools.md).
1. A Kubernetes cluster, version 1.8 or higher. 6vCPU and 16GB of RAM is recommended.
   - [Google GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-container-cluster)
   - [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
   - [Microsoft AKS](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal)

## Installing GitLab using the Helm Chart

The `gitlab` chart includes all required dependencies, and takes a few minutes
to deploy:

1. [Preparation](installation/index.md)
1. [Deployment](installation/deployment.md)

## Updating GitLab using the Helm Chart

Once your GitLab Chart is installed, configuration changes and chart updates
should be done using `helm upgrade`:

```sh
helm repo update
helm upgrade --reuse-values gitlab gitlab/gitlab
```

For more detailed information see [Upgrading](installation/upgrade.md).

## Uninstalling GitLab using the Helm Chart

To uninstall the GitLab Chart, run the following:

```sh
helm delete gitlab
```

## Advanced configuration

See [Advanced Configuration](advanced/index.md).

## Troubleshooting

See [Troubleshooting](troubleshooting/index.md).

## Misc

[Weekly demos preparation](preparation/index.md)

[kube-srv]: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services---service-types
[storageclass]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#storageclasses
