# Cloud Native GitLab Helm Chart

**THIS REPOSITORY IS UNDER HEAVY DEVELOPMENT.**

These charts are considered Alpha at the moment and things will not always work as
expected. Be advised that we are not recommending using this in production workloads.
See [Alpha documentation](doc/architecture/alpha.md) for more details.

We are working on a new method of installing GitLab for customers who are
looking to deploy into container schedulers like Kubernetes.

While this is possible today using our [Omnibus GitLab based Docker image](https://docs.gitlab.com/omnibus/docker/README.html) and [corresponding Helm charts](https://gitlab.com/charts/charts.gitlab.io), there are challenges.
One key example is that an "all-in-one container" becomes a challenge to configure and operate at large scale.

To address this need we are working on the [Helm charts in this repository](#helm-charts) along with a new set of Docker containers that are specific to each component of GitLab.

For more information on all of GitLab's Helm Charts, please consult our [documentation](http://docs.gitlab.com/ce/install/kubernetes/).

## Architecture and goals

See [architecture documentation](doc/architecture/README.md) for an overview
of this project goals and architecture.

## Quick-Start Installation

See [installation documentation](doc/installation/README.md) for a quick-start to using this chart.

## Detailed Documentation

See the [repository documentation](doc/README.md) for detailed documentation on charts, tools, and advanced configuration.

## Contributing

Please see the [contribution guidelines](CONTRIBUTING.md)
And then check out the [development styleguide](doc/development/README.md)
