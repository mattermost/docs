# Upgrade Guide

Before upgrading your GitLab installation, you need to check the
[changelog](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/CHANGELOG.md)
corresponding to the specific release you want to upgrade to and look for any
[release notes](../releases/index.md) that might pertain to the new GitLab chart
version.

Warning: **Warning:**
If you are upgrading from the `1.x` version of the chart to the latest, you need
to first update to the latest `1.9.x` patch release in order for the upgrade to work.
The [2.0 release notes](../releases/2_0.md) describe the supported upgrade path.

We also recommend that you take a [backup](../backup-restore/index.md) first.
Also note that you need to provide all values using `helm upgrade --set key=value` syntax or `-f values.yml` instead of using `--reuse-values` because some of the current values might be deprecated.

NOTE: **Note:**
You can retrieve your previous `--set` arguments cleanly, with
`helm get values <release name>`. If you direct this into a file
(`helm get values <release name> > gitlab.yaml`), you can safely pass this
file via `-f`. Thus `helm upgrade gitlab gitlab/gitlab -f gitlab.yaml`.
This safely replaces the behavior of `--reuse-values`

Mappings between chart versioning and GitLab versioning can be found [here](../index.md#gitlab-version-mappings).

## Steps

The following are the steps to upgrade GitLab to a newer version:

1. Check the [change log](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/CHANGELOG.md) for the specific version you would like to upgrade to
1. Go through [deployment documentation](./deployment.md) step by step
1. Extract your previous `--set` arguments with

   ```
   helm get values gitlab > gitlab.yaml
   ```

1. Decide on all the values you need to set
1. If you would like to use the GitLab Operator go through the steps outlined in [Operator installation](./operator.md)
1. Perform the upgrade, with all `--set` arguments extracted in step 4

   ```
   helm upgrade gitlab gitlab/gitlab \
     --version <new version> \
     -f gitlab.yaml \
     --set ...
   ```
