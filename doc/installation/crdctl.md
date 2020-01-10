# `crdctl` Utility

`scripts/crdctl` is a utility for managing the lifecycle of GitLab CRD. It helps you to create or delete the CRD.
You may find it useful for more advanced use-cases such as development or CI-managed environments.

## Usage

```bash
crdctl ACTION [PREFIX]
```

Currently only `create` and `delete` actions are supported which respectively create/update or delete the GitLab CRD.

You can pass an optional prefix for GitLab CRD. This prefix will be added to the group name of GitLab CRD. It can be
used to distinguish different CRDs in a cluster. For example GitLab Chart CI uses this feature to separate CRDs of
different pipelines.

When you decide to use CRD prefix, you need to pass it to the Chart as well, so the Operator will be able to work with
the expected CRD. To do so, use `gitlab.operator.crdPrefix` value.

**NOTE:** This utility uses `kubectl`. For versions prior to v1.14 you also need `kustomize`. To use an external
`kustomize` set `KUSTOMIZE_CMD` environment variable, e.g. `export KUSTOMIZE_CMD="kustomize build"`.
