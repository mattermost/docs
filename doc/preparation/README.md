# Pre-install preparations

This document covers our weekly demos preparation steps but can also be useful to anyone who tries to install using the charts before going through [installation](../installation/README.md).
The person giving the demo needs to go throw this document before the demo,
and should perform setup the day prior to the demo itself.

- [GKE setup](#gke-setup)
- [External resources](#external-resources)
- [Omniauth for Google OAuth2](#omniauth-for-google-oauth2)

## GKE setup

### Gcloud user

Make sure to have a gcloud user with permissions to access `cloud-native` project. All the [installation procedures](../installation/README.md) will need to be done
in this project.

### gcloud installation

You will need to have [gcloud](https://cloud.google.com/sdk/gcloud/) tool installed on your system.

#### Install gcloud:

```
mkdir gcloud-build && cd gcloud-build;
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-189.0.0-linux-x86_64.tar.gz;
tar -xzf google-cloud-sdk-189.0.0-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh
source google-cloud-sdk/path.bash.inc && echo "source google-cloud-sdk/path.bash.inc" >> $HOME/.profile
```

#### Initialize gcloud

Run `./google-cloud-sdk/bin/gcloud init` and interactively go through authentication and initialization of gcloud.

### Domain name

During the demo you will need a valid domain name that will resolve to our cluster load balancer through a wild card entry.
Make sure to have one of the Domain names ready for the demo either by creating a new one or by using an existing one.

We usually use `cloud-native-win` or `k8s-ftw`

## Kube monkey

Follow our [kube monkey](../kube-monkey/README.md) guide for running kube monkey, this is usually done after the demo.

## Git LFS

In order to test LFS storage in the chart, you will need to have the ability to use `git lfs`.

### Install git-lfs

Start by installing `git-lfs`, per instructions at https://git-lfs.github.com

### Prepare binary source

Next, have a non-text file on hand to add to your test repository via LFS. A good example is [the GitLab logo](https://gitlab.com/gitlab-com/gitlab-artwork/raw/master/logo/logo.png).

### Example workflow

```
git clone URL
cd project
curl -JLO https://gitlab.com/gitlab-com/gitlab-artwork/raw/master/logo/logo.png
git lfs track "*.png"
git add .gitattributes
git add logo.png
git commit -m "Add logo via LFS"
git push origin master
```

## External resources

As a part of the demo, we also wish to provide for testing the use of external
resources for PostgreSQL and Redis.

Ensure that these external sources will be reachable from the deployed
cluster, which may mean configuring firewall rules. The `cloud-native` GCP
project used for our CI has firewall rules in place, which can be used by
applying the `demo-pgsql` and `demo-redis` tags to any VM instance created
within the project.

### PostgreSQL

Preparation of chart-external PostgreSQL services (as a pet or SaaS), can
be found in [advanced/external-db](../advanced/external-db/README.md). This
can be done several ways documented there. Once that is configured, the chart
should be configured with the external service by making use of the `globals.psql`
properties section of the global chart.

### Redis

Preparation of chart-external Redis services (as a pet or SaaS), can
be found in [advanced/external-redis](../advanced/external-redis/README.md).
This can be done as documented there. Once that is configured, the chart should
be configured with the external service by making use of the `globals.redis`
properties section of the global chart.

### Gitaly

Preparation of chart-external Gitaly services can
be found in [advanced/external-gitaly](../advanced/external-gitaly/README.md).
This can be done as documented there. Once that is configured, the chart should
be configured with the external service by making use of the `globals.gitaly`
properties section of the global chart.

## Omniauth for Google OAuth2

Configuring a deployment with the capability to integrate with GKE requires
the use of Omniauth. You will need to ensure that a set of
**OAuth Client ID** credentials have been created for the hostname of the GitLab
endpoint in your cluster.

Cursory instructions for [creating a set of OAuth credentials can be found
here](https://support.google.com/cloud/answer/6158849?hl=en).

The credentials from GCP can be added per the [`unicorn` chart's `omniauth.providers` configuration documentation](../charts/gitlab/unicorn/README.md#omniauthproviders).

## Run GitLab QA

As preparation for the demo, one should also [run GitLab QA against the deployed chart](../gitlab-qa/README.md)
