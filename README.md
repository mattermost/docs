# Cloud Native GitLab Helm Chart

> **Notes**:
* The chart is currently **beta** This means that breaking changes could still be introduced on short notice but that the project is mostly stable
* There are [known issues and limitations](doc/architecture/beta.md#known-issues-and-limitations).


We are working on a new cloud native method of deploying GitLab on Kubernetes, using the [Helm chart in this repository](#helm-charts) along with a [new set of Docker containers](https://gitlab.com/gitlab-org/build/CNG) that are specific to each component of GitLab.

The `gitlab` chart is the best way to operate GitLab on Kubernetes. This chart contains all the required components to get started, and can scale to large deployments.

Some of the key benefits of the new chart and containers are:
* Improved scalability and reliability
* No requirement for root privileges
* Utilization of object storage instead of NFS for storage

The default deployment includes:

- Core GitLab components: Unicorn, Shell, Workhorse, Registry, Sidekiq, and Gitaly
- Optional dependencies: Postgres, Redis, Minio
- An auto-scaling, unprivileged [GitLab Runner](https://docs.gitlab.com/runner/) using the Kubernetes executor
- Automatically provisioned SSL via [Let's Encrypt](https://letsencrypt.org/).

## Architecture and goals

See [architecture documentation](doc/architecture/README.md) for an overview
of this project goals and architecture.

## Known issues and limitations

The current beta release of this chart contains a number of known issues and limitations. Please review our [beta documentation](doc/architecture/beta.md) for more details.

## Quick-start installation

See the [installation documentation](doc/installation/README.md) for a quick-start to using this chart.

## Detailed documentation

See the [repository documentation](doc/README.md) for detailed documentation on charts, tools, and advanced configuration.

## Contributing

Please see the [contribution guidelines](CONTRIBUTING.md)
And then check out the [development styleguide](doc/development/README.md).
