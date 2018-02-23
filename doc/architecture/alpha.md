# Alpha charts

During the alpha release of these charts, certain features and functionality
won't be available.

## Tools

During Alpha, we will be using the latest versions of tools such as `kubectl`,
`helm` and we will upgrade and downgrade them as needed.

## Clusters

We are working on Google Kubernetes Engine exclusively, but other k8s deployments
may also work. In case of a specific non-GKE deployment issue, please raise an issue.

As of the moment of writing this document, we are using Kubernetes version 1.8.5.
Definitive minimum cluster version requirement will be set after the next
chart milestone, most likely during Beta.

## GitLab Enterprise Edition

During Alpha, we will only support GitLab Enterprise Edition. GitLab EE offers
same functionality as GitLab CE when no licence is supplied.

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

## Functionality and features

Below you can find a non-definitive list of issues that are currently known
not to be fully functional:

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
* No support for configuring the unicorn workers https://gitlab.com/charts/helm.gitlab.io/issues/237
* CI traces are not persisted https://gitlab.com/charts/helm.gitlab.io/issues/245
* No support for scaling unicorn separate from workhorse https://gitlab.com/charts/helm.gitlab.io/issues/61
* GitLab maintenace rake tasks won't work in k8s environments
* No guarantees on safe pod shutdown: https://gitlab.com/charts/helm.gitlab.io/issues/239
* New ssh hostkeys each time the shell container restarts https://gitlab.com/charts/helm.gitlab.io/issues/247

Once GitLab is deployed and running, you might encounter currently known issues:

* No LFS support https://gitlab.com/charts/helm.gitlab.io/issues/242
* Adding attachment to a comment does not work https://gitlab.com/charts/helm.gitlab.io/issues/227
* Navigating to Registry shows page 500 https://gitlab.com/charts/helm.gitlab.io/issues/225
* Navigating to Wiki shows page 500 https://gitlab.com/charts/helm.gitlab.io/issues/226
* Emails are not sent https://gitlab.com/charts/helm.gitlab.io/issues/234

List below includes features that are currently out of scope:

* Support for mysql https://gitlab.com/charts/helm.gitlab.io/issues/250
* Mattermost https://gitlab.com/charts/helm.gitlab.io/issues/251
