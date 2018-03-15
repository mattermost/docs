# Design Decisions

This documentation collects reasoning and documentation regard decisions made
regarding the design of the charts in this repository.

## Preference of Secrets in initContainer over Environment

Much of the container ecosystem has, or expects, the capability to be configured
through environment variables. This [configuration practice](https://12factor.net/config) stems from the concept of [The Twelve-Factor App](https://12factor.net). This
greatly simplifies configuration across multiple deployment environemnts, there
remains a security concern with passing connection secrets such as passwords and
private keys via the container's environment.

Most container ecosystems provide a simple method to inspect the state of a running
container, which usually includes the environment. Using [Docker](https://www.docker.com/)
as an example, any process capable of communicating with the daemon can query the
state of all running containers. This means that if you have a privileged container
such as [dind][], that container can then inspect the environment of _any_ container
on a given node, and expose _all_ secrets contained within.
As a part of the [complete DevOps lifecycle][devops-post], [dind][] is regularly
used for building containers that will be pushed to a registry and subsequently
deployed.

This concern is why we've decided to prefer the population of sensitive information
via [initContainers][].

Related issues:
- [#90](https://gitlab.com/charts/helm.gitlab.io/issues/90)
- [#114](https://gitlab.com/charts/helm.gitlab.io/issues/114)

[dind]: (https://hub.docker.com/r/gitlab/dind/)
[devops-post]: https://about.gitlab.com/2017/10/11/from-dev-to-devops/
[initContainers]: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

## Forked charts

The following charts have been forked or re-created in this repository following
our [guidelines for forking](../development/README.md#guidelines-for-forking)

### redis

The [redis chart][] was altered to

[redis chart]: ../../charts/redis

### redis-ha

[redis chart]: ../../charts/redis-ha

### minio

### registry
