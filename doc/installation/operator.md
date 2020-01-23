# GitLab Operator

GitLab Operator is an implementation of the [Operator pattern](https://coreos.com/blog/introducing-operators.html)
for management of deployment lifecycle. This component provides a method of synchronizing and controlling various
stages of cloud-native GitLab installation/upgrade procedures. Using the Operator provides the ability to perform
rolling upgrades without down time.

## Operator Chart

We provide an [Operator Chart](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/charts/gitlab/charts/operator)
for installing the Operator. When enabled, the Operator will assume control of the upgrade process that was previously
managed via [Helm hooks](https://helm.sh/docs/topics/charts_hooks/).

### Installing the CRD

The Operator makes use of [Kubernetes Custom Resource Definitions (CRD)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions).
Since Helm handles the installation, we need to ensure that the GitLab CRD is in place prior to attempting to use it.
In order to do this, we have to install the CRD with a separate command:

```bash
GITLAB_CHART_VERSION=v3.0.0
kubectl apply -f https://gitlab.com/gitlab-org/charts/gitlab/raw/${GITLAB_CHART_VERSION}/support/crd.yaml
```

**NOTE:** This needs to done only for the first time before installing the Operator or _when the CRD is changed_.
Further upgrades will follow the normal [upgrade procedures](./upgrade.md).

### Enabling the Operator

We provide the flag `global.operator.enabled`, when set to true it enables the Operator and allows it to manage
resources.

Once the GitLab CRD is in place, you can install GitLab with the following command, where `...` must be replaced by
the rest of the values you would like to set:

```bash
helm upgrade --install <release-name> . --set global.operator.enabled=true ...
```

GitLab Chart does not manage the lifecycle of the CRD and it needs to be done outside the Chart. For more details see
[crdctl](crdctl.md) utility.

**NOTE:** The Operator is transitioning from a ClusterRole to a regular Role that operates within a Namespace. Operator
containers after version `0.4` will have this new behavior by default.

**NOTE:** Test new versions of the Operator by setting `gitlab.operator.image.tag` to either the branch name of a GitLab
Operator container build or a specific tagged release number.

**NOTE:** The versions prior to 1.9.0 use the release name as a prefix for CRD name. This feature has been removed and
the CRD does not have a prefix. This can cause Helm complain about missing `GitLab` type while upgrading from an older
version. To solve this issue you can use `gitlab.operator.crdPrefix` value and pass the release name for upgrade.
