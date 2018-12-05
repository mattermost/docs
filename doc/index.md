# GitLab cloud native Helm Chart

This is the official and recommended way to install GitLab on a cloud native environment.

## Introduction

The `gitlab` chart is the best way to operate GitLab on Kubernetes. This chart
contains all the required components to get started, and can scale to large deployments.

The default deployment includes:

- Core GitLab components: Unicorn, Shell, Workhorse, Registry, Sidekiq, and Gitaly
- Optional dependencies: Postgres, Redis, Minio
- An auto-scaling, unprivileged [GitLab Runner](https://docs.gitlab.com/runner/) using the Kubernetes executor
- Automatically provisioned SSL via [Let's Encrypt](https://letsencrypt.org/).

For more information on other available GitLab Helm Charts, see the [charts overview](./charts/index.md).

There are also some [example values.yaml files](https://gitlab.com/charts/gitlab/tree/master/examples).

## Limitations

Some features of GitLab are not currently available using the Helm chart:

- [GitLab Pages](https://gitlab.com/charts/gitlab/issues/37)
- [GitLab Geo](https://gitlab.com/charts/gitlab/issues/8)
- [No in-cluster HA database](https://gitlab.com/charts/gitlab/issues/48)
- MySQL will not be supported, as support is [deprecated within GitLab](https://docs.gitlab.com/omnibus/settings/database.html#using-a-mysql-database-management-server-enterprise-edition-only)

## GitLab version mappings

The table below maps some of the key previous chart versions and GitLab versions.

| Chart version | GitLab version |
|---------------|----------------|
| 1.5.0 | 11.7.0 |
| 1.4.0 | 11.6.0 |
| 1.3.0 | 11.5.0 |
| 1.2.0 | 11.4.0 |
| 1.1.0 | 11.3.0 |
| 1.0.0 | 11.2.0 |
| 0.3.5 | 11.1.4 |
| 0.2.4 | 11.0.4 |

To see the full list of the `gitlab` chart versions and the GitLab version they
maps to, issue the following command with [helm](installation/tools.md#helm):

```sh
helm repo add gitlab https://charts.gitlab.io/
helm search -l gitlab/gitlab
```

You will receive an output similar to:

```
NAME                    CHART VERSION   APP VERSION
gitlab/gitlab           1.5.0           11.7.0
gitlab/gitlab           1.4.4           11.6.5
gitlab/gitlab           1.4.3           11.6.4
gitlab/gitlab           1.4.2           11.6.3
gitlab/gitlab           1.4.1           11.6.2
```

Read more about our [charts versioning](development/release.md) in our
development docs.

Make sure to also check the [releases documentation](releases/index.md) for
information on important releases, and see the
[changelog](https://gitlab.com/charts/gitlab/blob/master/CHANGELOG.md) for the
full details on any release.

## Installing GitLab using the Helm Chart

The `gitlab` chart includes all required dependencies, and takes a few minutes
to deploy:

1. [Preparation](installation/index.md)
1. [Deployment](installation/deployment.md)

## Updating GitLab using the Helm Chart

Once your GitLab Chart is installed, configuration changes and chart updates
should be done using `helm upgrade`:

```sh
helm repo add gitlab https://charts.gitlab.io/
helm repo update
helm upgrade --reuse-values gitlab gitlab/gitlab
```

For more detailed information see [Upgrading](installation/upgrade.md).

## Uninstalling GitLab using the Helm Chart

To uninstall the GitLab Chart, run the following:

```sh
helm delete gitlab
```

## Migrate from Omnibus GitLab to Kubernetes

To migrate your existing Omnibus GitLab instance to your Kubernetes cluster,
follow the [migration documentation](installation/migration/index.md).

## Advanced configuration

See [Advanced Configuration](advanced/index.md).

## Troubleshooting

See [Troubleshooting](troubleshooting/index.md).

## Misc

[Weekly demos preparation](preparation/index.md)
