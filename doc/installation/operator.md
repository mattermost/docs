# GitLab Operator

GitLab operator is an implementation of the [Operator pattern](https://coreos.com/blog/introducing-operators.html) for management of deployment lifecycle. This component provides a method of synchronizing and controlling various stages of cloud-native GitLab installation/upgrade procedures. Using the operator provides the ability to perform rolling upgrades without down time.

## Operator chart

We provide an [operator chart](../../charts/gitlab/charts/operator) for installing the operator. If enabled, the operator will assume control of the upgrade process that was previously managed via [Helm hooks](https://docs.helm.sh/developing_charts/#hooks).

### Enabling the operator

We provide the flag `global.operator.enabled`, when set to true it enables the operator and allows it to manage resources.

## Installing using the operator

The operator makes use of Kubernetes CustomResourceDefinitions (CRD). Since Helm will be used for the instllation, we need to ensure that this CRD is in place prior to attempting to use it. In order to do this, we have to run an additional command prior to use.

1. `helm upgrade --install <release-name> . --set global.gitlab.operator.enabled=true --set global.operator.bootstrap=true ... ` where `...` shall be replaced by the rest of the values you would like to set.
2. `helm upgrade <release-name> . --set global.gitlab.operator.enabled=true --set global.operator.bootstrap=false ...`.

The first command will install only the `CRD` but will not actually attempt to deploy the operator. The second command will deploy the operator itself, now that the CRD is in place.

**NOTE:** This needs done only the first time you install the operator, further upgrades will follow the normal [upgrade procedures](./upgrade.md)
