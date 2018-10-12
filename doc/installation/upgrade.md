# Upgrade Guide

Before upgrading your GitLab installation, you need to check the [change log](https://gitlab.com/charts/gitlab/blob/master/CHANGELOG.md) corresponding to the specific release you want to upgrade to. And look for any [release notes](../releases/README.md) that might pertain to the new GitLab chart version. We also recommend that you take a [backup](https://gitlab.com/charts/gitlab/blob/master/doc/backup-restore/README.md) first. Also note that you need to provide all values using `helm upgrade --set key=value` syntax or `-f values.yml` instead of using `--reuse-values` because some of the current values might be deprecated.

Mappings between chart versioning and GitLab versioning can be found [here](./version-mappings.md)

# Steps

The following are the steps to upgrade GitLab to a newer version:

1. Check the [change log](https://gitlab.com/charts/gitlab/blob/master/CHANGELOG.md) for the specific version you would like to upgrade to
2. Go through [deployment documentation](./deployment.md) step by step
3. Decide on all the values you need to set
4. If you would like to use the GitLab operator go through the steps outlined in [Operator installation](./operator.md)
5. Do `helm upgrade gitlab . --version <new version> ` followed by all `--set` values you extracted in step 3
