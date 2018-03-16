## Architecture

We plan to support three tiers of components:

1. Docker Containers
1. Scheduler (Kubernetes)
1. Higher level configuration tool (Helm)

The main method customers would use to install would be the [Helm Charts]() in this repository.
At some point in the future, we may also offer other deployment methods like
Amazon CloudFormation or Docker Swarm.

## Docker Container Images

As a foundation, we will be creating a Docker container for each service.
This will allow easier horizontal scaling with reduced image size and complexity.
Configuration should be passed in a standard way for Docker, perhaps environment
variables or a mounted file. This provides a clean common interface with the
scheduler software.

We plan to offer a container for the following services:

* Sidekiq
* Unicorn
* Gitaly
* Workhorse
* Pages
* Postgres (perhaps upstream Postgres), along with Postgres Exporter
* Redis
* GitLab Monitor

We likely plan to leverage the following existing official containers for
underlying services:

* Docker Distribution ([Docker Registry 2.0](https://github.com/docker/distribution))
* Prometheus
* Node Exporter
* Nginx
* kube-lego


## The GitLab Chart

This is the top level `gitlab` chart, which configures all necessary resources
for a complete configuration of GitLab. This includes GitLab, PostgreSQL, Redis,
Ingress, and LEGO certificate management charts.

At this high level, a customer can make decisions like:

* Whether they want to use the embedded Postgres chart, or to use an external
database like Aamzon RDS for Postgres.
* To bring their own SSL certificates, or leverage Let's Encrypt.
* To use a load balancer, or a dedicated ingress.

Customers who would like to get started quickly and easily should begin with this chart.

### The GitLab-Services Charts

This chart is dedicated to core GitLab services that make up the Idea to
Production workflow: code repository, issue tracking, CI/CD, monitoring, container
registry, etc.

This chart would also include options to configure exactly how these services
should work, whether all of them should be available, etc.

Included in this chart are the Helm Charts for each service:
* [registry](https://gitlab.com/charts/helm.gitlab.io/tree/master/charts/registry)
* [sidekiq](https://gitlab.com/charts/helm.gitlab.io/tree/master/charts/gitlab/charts/sidekiq)
* [unicorn](https://gitlab.com/charts/helm.gitlab.io/tree/master/charts/gitlab/charts/unicorn)
* workhorse (currently a part of the unicorn chart)
* [gitaly](https://gitlab.com/charts/helm.gitlab.io/tree/master/charts/gitlab/charts/gitaly)
* pages
* prometheus
* [gitlab-shell](https://gitlab.com/charts/helm.gitlab.io/tree/master/charts/gitlab/charts/gitlab-shell)

## Design Decisions

Documentation of the decisions made regarding the architecture of these charts can
be found in [Design Decisions](decisions.md) documentation
