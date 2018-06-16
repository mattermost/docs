## Architecture

We plan to support three tiers of components:

1. Docker Containers
1. Scheduler (Kubernetes)
1. Higher level configuration tool (Helm)

The main method customers would use to install would be the [Helm Chart](https://helm.sh/) in this repository.
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
* Postgres (perhaps upstream Postgres), along with Postgres Exporter
* Redis
* GitLab Monitor

We likely plan to leverage the following existing official containers for
underlying services:

* Docker Distribution ([Docker Registry 2.0](https://github.com/docker/distribution))
* Prometheus
* Node Exporter
* Nginx
* cert-manager


## The GitLab Chart

This is the top level `gitlab` chart, which configures all necessary resources
for a complete configuration of GitLab. This includes GitLab, PostgreSQL, Redis,
Ingress, and certificate management charts.

At this high level, a customer can make decisions like:

* Whether they want to use the embedded Postgres chart, or to use an external
database like Amazon RDS for Postgres.
* To bring their own SSL certificates, or leverage Let's Encrypt.
* To use a load balancer, or a dedicated ingress.

Customers who would like to get started quickly and easily should begin with this chart.

### Subcharts

The gitlab chart is made of multiple subcharts. These charts provide individual components of the GitLab software.

Subcharts included are :
* [sidekiq](https://gitlab.com/charts/gitlab/tree/master/charts/gitlab/charts/sidekiq)
* [unicorn](https://gitlab.com/charts/gitlab/tree/master/charts/gitlab/charts/unicorn)
* [gitlab-shell](https://gitlab.com/charts/gitlab/tree/master/charts/gitlab/charts/gitlab-shell)
* [gitaly](https://gitlab.com/charts/gitlab/tree/master/charts/gitlab/charts/gitaly)
* [minio](https://gitlab.com/charts/gitlab/tree/master/charts/minio)
* [redis](https://gitlab.com/charts/gitlab/tree/master/charts/redis)
* [nginx](https://gitlab.com/charts/gitlab/tree/master/charts/nginx)
* [registry](https://gitlab.com/charts/gitlab/tree/master/charts/registry)

## Design Decisions

Documentation of the decisions made regarding the architecture of these charts can
be found in [Design Decisions](decisions.md) documentation
