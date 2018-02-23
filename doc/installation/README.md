# Installing GitLab using Helm

This document provides all steps in installing a complete GitLab environment via
helm, and should be followed in order.

## 1. Required tools

Before you can install GitLab in a Kubernetes cluster, make sure you have
all required tools. See [local setup][] document for more information.

## 2. Where do you want to install GitLab?

* [Google Kubernetes Engine][]
* Amazon EKS - Documentation to be added.
* Azure Container Service - Documentation to be added.
* On-Premises solutions - Documentation to be added.

## 3. Secrets

For a functional deployment, various secrets are necessary.
See [secrets document][secrets] for more information.

## 4. Configuration file

Next, populate your configuration which will be used to deploy. See
[generating configuration][configuration] for more information.

## 5. Deploy

Now that we have the environment setup and configuration generated,
we can proceed to [deployment][].

[Google Kubernetes Engine]: ../cloud/gke.md
[local setup]: tools.md
[resources]: resources.md
[secrets]: secrets.md
[configuration]: configuration.md
[deployment]: deployment.md
