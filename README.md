# Cloud Native GitLab Helm Chart

The `gitlab` chart is the best way to operate GitLab on Kubernetes. This chart contains all the required components to get started, and can scale to large deployments.

Do note that it is not necessary to have GitLab installed on Kubernetes in order to use [GitLab Kubernetes integration](https://docs.gitlab.com/ee/user/project/clusters/index.html). 

Some of the key benefits of this chart and [corresponding containers](https://gitlab.com/gitlab-org/build/CNG) are:
* Improved scalability and reliability
* No requirement for root privileges
* Utilization of object storage instead of NFS for storage

The default deployment includes:

- Core GitLab components: Unicorn, Shell, Workhorse, Registry, Sidekiq, and Gitaly
- Optional dependencies: Postgres, Redis, Minio
- An auto-scaling, unprivileged [GitLab Runner](https://docs.gitlab.com/runner/) using the Kubernetes executor
- Automatically provisioned SSL via [Let's Encrypt](https://letsencrypt.org/).

## Architecture and goals

See [architecture documentation](doc/architecture/index.md) for an overview
of this project goals and architecture.

## Known issues and limitations

Some features of GitLab are not currently available:

* [GitLab Pages](https://gitlab.com/charts/gitlab/issues/37)
* [GitLab Geo](https://gitlab.com/charts/gitlab/issues/8)
* [GitLab Elastic Search support](https://gitlab.com/charts/gitlab/issues/976)
* [No in-cluster HA database](https://gitlab.com/charts/gitlab/issues/48)
* MySQL will not be supported, as support is [deprecated within GitLab](https://docs.gitlab.com/omnibus/settings/database.html#using-a-mysql-database-management-server-enterprise-edition-only)

Limitations:

* Support is only available for Postgres 9.6. Backup and restore [will not work with other versions](https://gitlab.com/charts/gitlab/issues/852).

## Release Notes

Check the [releases documentation](doc/releases/index.md) for information on important releases,
and see the [changelog](CHANGELOG.md) for the full details on any release.   

## Quick-start installation

See the [installation documentation](doc/installation/index.md) for a quick-start to using this chart.

## Detailed documentation

See the [repository documentation](doc/index.md) for detailed documentation on charts, tools, and advanced configuration.

## Contributing

Please see the [contribution guidelines](CONTRIBUTING.md)
And then check out the [development styleguide](doc/development/index.md).
