# Cloud Native GitLab Helm Chart

> **Notes**:
  * This chart is **alpha**. It should not be used for production deployments.
  * There are [known issues and limitations](doc/architecture/alpha.md).


We are working on a new cloud native method of deploying GitLab on Kubernetes.

While this is possible today using our [Omnibus GitLab based Docker image](https://docs.gitlab.com/omnibus/docker/README.html) and [corresponding Helm charts](https://gitlab.com/charts/charts.gitlab.io), there are challenges.
One key example is that an "all-in-one container" becomes a challenge to configure and operate at scale.

To address this need we are working on the [Helm chart in this repository](#helm-charts) along with a [new set of Docker containers](https://gitlab.com/gitlab-org/build/CNG) that are specific to each component of GitLab.

For more information on all of GitLab's Helm Charts, please consult our [documentation](http://docs.gitlab.com/ce/install/kubernetes/).

## Architecture and goals

See [architecture documentation](doc/architecture/README.md) for an overview
of this project goals and architecture.

## Known Issues and Limitations

The current alpha release of this chart contains a number of known issues and limitations. Please review our [alpha documentation]() for more details.

## Quick-Start Installation

See [installation documentation](doc/installation/README.md) for a quick-start to using this chart.

## Detailed Documentation

See the [repository documentation](doc/README.md) for detailed documentation on charts, tools, and advanced configuration.

## Contributing

Please see the [contribution guidelines](CONTRIBUTING.md)
And then check out the [development styleguide](doc/development/README.md)
