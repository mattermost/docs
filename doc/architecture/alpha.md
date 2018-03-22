# GitLab Cloud Native Chart Alpha

We have been working hard on the chart and it's underlying containers, and are excited to be able to reach alpha status to share it with the GitLab community.

This effort has required extensive changes across the  product:
* Support for directly uploading to object storage
* No dependency on shared storage
* New containers for each component of GitLab
* New Helm chart

While much of the underlying work has been completed, there are a few changes that will be arriving after alpha has started. This means that there are a few features of GitLab [that may not work as expected](#known-issues-and-limitations).

## Release cadence

In order to maximize our testing opportunity in alpha, the chart and containers will be rebuilt off `master` as changes are merged. This means that fixes and improvements will be available in alpha as soon as they are merged, instead of waiting for a specific release window.

Along with the standard issues and merge requests in this repo, a [changelog](https://gitlab.com/charts/helm.gitlab.io/issues/289) is being made available to more easily follow along with updates throughout the alpha period.

## Tools

During alpha, we will be using the latest versions of tools such as `kubectl`,
`helm` and we will upgrade and downgrade them as needed.

## Kubernetes Cluster Support

GitLab development and testing is taking place on [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) exclusively, but other k8s deployments
may also work. In case of a specific non-GKE deployment issue, please raise an issue.

As of the moment of writing this document, we are using Kubernetes version 1.8.7.
Definitive minimum cluster version requirement will be set after the next
chart milestone, most likely during Beta.

## GitLab Enterprise Edition

During Alpha, we will only support GitLab Enterprise Edition. GitLab EE offers
same functionality as GitLab CE when no license is supplied.

Before making these charts generally available, we will address this support
in issue https://gitlab.com/charts/helm.gitlab.io/issues/173 .

## Support

During the Alpha release of charts, we welcome any improvements contributed in the
form of Merge Requests.

Due to workload on the road to Beta, we might not be able to provide support for
every user request. This means that we won't be able to provide support
for failed installations/upgrades and various other debugging requests.

We will reserve the right to close issues without providing a reason. Issues
accumulate quickly and we would rather spend time working on charts then doing
issue triage.

Before raising an issue, please see the list below of known limitations of charts
during Alpha.

## Known issues and limitations

Below you can find a non-definitive list of issues that are currently known not to be fully functional:

* No in-cluster database https://gitlab.com/charts/helm.gitlab.io/issues/48
* No backup restore procedure https://gitlab.com/charts/helm.gitlab.io/issues/28
* No update procedures, and support for no-downtime upgrades: https://gitlab.com/charts/helm.gitlab.io/issues/238
* No support for changing/migrating your storage capacity/options after installation https://gitlab.com/charts/helm.gitlab.io/issues/233
* No GitLab Pages support https://gitlab.com/charts/helm.gitlab.io/issues/37
* No Monitoring support https://gitlab.com/charts/helm.gitlab.io/issues/29
* No support for outgoing email https://gitlab.com/charts/helm.gitlab.io/issues/234
* No support for incoming email https://gitlab.com/charts/helm.gitlab.io/issues/235
* No support for customizing GitLab options, eg. LDAP https://gitlab.com/charts/helm.gitlab.io/issues/236
* No support for advanced workhorse configuration https://gitlab.com/charts/helm.gitlab.io/issues/249
* CI traces are not persisted https://gitlab.com/charts/helm.gitlab.io/issues/245
* No support for scaling unicorn separate from workhorse https://gitlab.com/charts/helm.gitlab.io/issues/61
* GitLab maintenance rake tasks won't work in k8s environments
* No guarantees on safe pod shutdown: https://gitlab.com/charts/helm.gitlab.io/issues/239
* New ssh hostkeys each time the shell container restarts https://gitlab.com/charts/helm.gitlab.io/issues/247

Once GitLab is deployed and running, you might encounter currently known issues:

* User uploaded content such as attachments to comments, are not persisted https://gitlab.com/charts/helm.gitlab.io/issues/227
* Navigating to Wiki shows page 500 https://gitlab.com/charts/helm.gitlab.io/issues/226
* Emails are not sent https://gitlab.com/charts/helm.gitlab.io/issues/234

List below includes features that are currently out of scope:

* Support for mysql https://gitlab.com/charts/helm.gitlab.io/issues/250
* Mattermost https://gitlab.com/charts/helm.gitlab.io/issues/251
