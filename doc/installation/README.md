# Installing GitLab using Helm

This document provides all steps in installing a complete GitLab environment via
helm, and should be followed in order.

## Required tools

Before you can install GitLab in a Kubernetes cluster, make sure you have
all required tools. See [local setup][] document for more information.

## Where do you want to install GitLab?

### Google Kubernetes Engine

If you want to install GitLab on Google Kubernetes engine, please follow the
[installing on GKE][] documentation.

### Amazon EKS

Documentation to be added.

### Azure Container Service

Documentation to be added.

### On-Premises solutions

Documentation to be added.

## GKE resources

You will need to create a few resources to use this chart, such as a static IP and DNS entry. See [GKE resources document][resources] for more information.

## Secrets

For a functional deployment, various secrets are necessary. See [secrets document][secrets] for more information.

## Configuration file

Next, populate your configuration which will be used to deploy. See
[generating configuration document][configuration] for more information.

## Deploy

Now that we have the environment setup and configuration generated,
we can proceed to [deployment][].

[installing on GKE]: cloud/gke.md
[local setup]: tools.md
[resources]: resources.md
[secrets]: secrets.md
[configuration]: configuration.md
[deployment]: deployment.md
