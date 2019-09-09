# Deploy Development Branch

Clone the repository, and checkout the branch you want to deploy:

```sh
git clone git@gitlab.com:gitlab-org/charts/gitlab.git
git checkout <BRANCH_NAME>
```

> **Note:**
> You can test changes to external dependencies by modifying `requirements.yaml`
>
> It is possible to test external dependencies using a local repository. Use `file://PATH_TO_DEPENDENCY_REPO`
> where the path may be relative to the chartpath or absolute. For example, if using
> `/home/USER/charts/gitlab` as the main checkout and `/home/USER/charts/gitlab-runner`, the
> relative path would be `file://../gitlab-runner/` and the absolute path would be
> `file:///home/USER/charts/gitlab-runner/`. Pay close attention with absolute paths as it
> is very easy to miss the leading slash on the filepath.

Other steps from the [installation documentation](../installation/index.md) still apply. The difference is when deploying
a development branch, you need to update the local dependencies, and pass the local git repo location to the helm command.

From within your git checkout of the repo, run the following helm commands to install:

```sh
helm repo add gitlab https://charts.gitlab.io/
helm dependencies update
helm upgrade --install gitlab . \
  --timeout 600 \
  --set global.imagePullPolicy=Always \
  --set global.hosts.domain=example.com \
  --set global.hosts.externalIP=10.10.10.10 \
  --set certmanager-issuer.email=me@example.com
```
