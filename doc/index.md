# GitLab cloud native Helm Chart

This is the official and recommended way to install GitLab on a cloud native environment.

Do note that it is not necessary to have GitLab installed on Kubernetes in order to use
the [GitLab Kubernetes integration](https://docs.gitlab.com/ee/user/project/clusters/).

## Introduction

The `gitlab` chart is the best way to operate GitLab on Kubernetes. This chart
contains all the required components to get started, and can scale to large deployments.

The default deployment includes:

- Core GitLab components: Unicorn, Shell, Workhorse, Registry, Sidekiq, and Gitaly
- Optional dependencies: Postgres, Redis, Minio
- An auto-scaling, unprivileged [GitLab Runner](https://docs.gitlab.com/runner/) using the Kubernetes executor
- Automatically provisioned SSL via [Let's Encrypt](https://letsencrypt.org/).

There are also some [example values.yaml files](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples).

## Limitations

Some features of GitLab are not currently available using the Helm chart:

- [GitLab Pages](https://gitlab.com/gitlab-org/charts/gitlab/issues/37)
- [GitLab Geo](https://gitlab.com/gitlab-org/charts/gitlab/issues/8)
- [No in-cluster HA database](https://gitlab.com/gitlab-org/charts/gitlab/issues/48)
- [Smartcard authentication](https://gitlab.com/gitlab-org/charts/gitlab/issues/988)

Database limitations:

- MySQL will not be supported, as support is [deprecated within GitLab](https://docs.gitlab.com/omnibus/settings/database.html#using-a-mysql-database-management-server-enterprise-edition-only)
- Support is only available for Postgres 9.6. Backup and restore [will not work with other versions](https://gitlab.com/gitlab-org/charts/gitlab/issues/852).

## GitLab version mappings

The GitLab chart doesn't have the same version number as GitLab itself.
Breaking changes are anticipated that may need to be introduced to the chart
that would warrant a major version bump, and the requirement for these changes
could completely block other development on these charts until completed.

To quickly see the full list of the `gitlab` chart versions and the GitLab version
they map to, issue the following command with [helm](installation/tools.md#helm):

```sh
helm repo add gitlab https://charts.gitlab.io/
helm search -l gitlab/gitlab
```

For more information, visit the [version mappings docs](installation/version_mappings.md).

## List of charts

The main GitLab chart is based on a variety of other charts. Each sub-chart is
documented individually, and laid in a structure that matches the
[charts](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/charts) directory structure.

Non-GitLab components are packaged and documented on the top level. GitLab
component services are documented under the [GitLab](charts/gitlab/index.md) chart:

- [NGINX](charts/nginx/index.md)
- [Redis](charts/redis/index.md)
- [Minio](charts/minio/index.md)
- [Registry](charts/registry/index.md)
- GitLab/[sidekiq](charts/gitlab/sidekiq/index.md)
- GitLab/[gitlab-shell](charts/gitlab/gitlab-shell/index.md)
- GitLab/[gitaly](charts/gitlab/gitaly/index.md)
- GitLab/[unicorn](charts/gitlab/unicorn/index.md)
- GitLab/[migrations](charts/gitlab/migrations/index.md)

## Global settings

There are some common global settings that apply to multiple charts. See the
[Globals documentation](charts/globals.md) for details on the different global
configuration.

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
helm get values gitlab > gitlab.yaml
helm upgrade gitlab gitlab/gitlab -f gitlab.yaml
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

## Contributing

See the [developer documentation](development/index.md) to learn how to contribute
to the GitLab charts.

## Misc

[Weekly demos preparation](development/preparation/index.md)
