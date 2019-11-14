# Kube monkey

[kube monkey](https://github.com/asobti/kube-monkey) is an implementation of
Netflix's [chaos monkey](https://github.com/Netflix/chaosmonkey) for Kubernetes
clusters. It schedules randomly killing of pods in order to test fault tolerance
of a highly available system.

## Why

As a part of our charts development we needed a way to test the fault tolerance
of our deployments.

## How

Using kube monkey is a manual step we do after our weekly demos. The intended
use case of kube monkey is to kill pods randomly at random times during a
working day to test the ability to recover. The way we use it is a bit different,
we manually launch kube monkey in debug mode and manually identify the weak
points of our deployment.

Later, we intend to integrate it into our CI pipeline, so whenever new changes
are rolled out we have a kube monkey run for that release.

## Configuration

Kube monkey can be configured by editing the `scripts/kube-monkey-resources/km-config.toml`
file. For more info read the official [kube monkey docs](https://github.com/asobti/kube-monkey#configuring).

## Usage

The [gke_bootstrap_script.sh](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/scripts/gke_bootstrap_script.sh)
takes an argument `chaos` which installs and unleashes kube monkey by
scheduling a run 60s after installing kube monkey by default. It also sets up
the needed service account and role if RBAC is enabled.

After you clone the charts repository, to install and unleash kube monkey run:

```sh
scripts/gke-bootstrap-script.sh chaos
```
