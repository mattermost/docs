# Using the GitLab Runner chart

The GitLab Runner subchart provides a GitLab Runner for running CI jobs. It is enabled by default and should work out of the box with support for caching using s3 compatible object storage.

## Requirements

This chart depends on the shared-secrets subchart to populate its `registrationToken` for automatic registration. If you intend to run this chart as a stand-alone chart with an existing GitLab instance then you will need to manually set the `registrationToken` in the `gitlab-runner` secret to be equal to that displayed by the running GitLab instance.

## Configuration

There are no required settings, it should work out of the box if you deploy all of the charts together.

## Deploying a stand-alone runner

By default we do infer `gitlabUrl`, automatically generate a registration token, and generate it through the `migrations` chart. This behaviour will not work if you intend to deploy it with a running GitLab instance.

In this case you will need to set `gitlabUrl` value to be the url of the running GitLab instance. You will also need to manually create `gitlab-runner` secret and fill it with the `registrationToken` provided by the running GitLab.

## Using docker-in-docker

In order to run docker-in-docker, the runner container needs to be privileged to have access to the needed capabilities. To enable it set the `privileged` value to `true`. See the [upstream documentation](https://docs.gitlab.com/runner/install/kubernetes.html#running-docker-in-docker-containers-with-gitlab-runners) in regards to why this is does not default to `true`.

### Security concerns

Privileged containers have extended capabilities, for example they can mount arbitrary files from the host they run on. Make sure to run the container in an isolated environment such that nothing important runs beside it.

## Installation command line options

| Parameter                                      | Description                                | Default                               |
| ---------------------------------------------- | ------------------------------------------ | ------------------------------------- |
| `gitlab-runner.image`                          | Runner image                               | `gitlab/gitlab-runner:alpine-v10.5.0` |
| `gitlab-runner.install`                        | Install the `gitlab-runner` chart          | `true`                                |
| `gitlab-runner.imagePullPolicy`                | Image pull policy                          | `IfNotPresent`                        |
| `gitlab-runner.init.image.repository`          | `initContainer` image                      |                                       |
| `gitlab-runner.init.image.tag`                 | `initContainer` image tag                  |                                       |
| `gitlab-runner.pullSecrets`                    | Secrets for the image repository           |                                       |
| `gitlab-runner.unregisterRunners`              | Unregister all runners before termination  | `true`                                |
| `gitlab-runner.concurrent`                     | Number of concurrent jobs                  | `20`                                  |
| `gitlab-runner.checkInterval`                  | Polling interval                           | `30s`                                 |
| `gitlab-runner.rbac.create`                    | Whether to create rbac service account     | `true`                                |
| `gitlab-runner.rbac.clusterWideAccess`         | Deploy containers of jobs cluster-wide     | `false`                               |
| `gitlab-runner.rbac.serviceAccountName`        | Name of the rbac service account to create | `default`                             |
| `gitlab-runner.runners.image`                  | Default container image to use in builds   | `ubuntu:16.04`                        |
| `gitlab-runner.runners.imagePullSecrets`       | `imagePullSecrets`                         | `[]`                                  |
| `gitlab-runner.runners.privileged`             | Run in privileged mode, needed for `dind`  | `false`                               |
| `gitlab-runner.runners.namespace`              | Namespace to run jobs in                   | `default`                             |
| `gitlab-runner.runners.cache.cacheType`        | Cache type                                 | `s3`                                  |
| `gitlab-runner.runners.cache.s3BucketName`     | Name of the bucket                         | `runner-cache`                        |
| `gitlab-runner.runners.cache.cacheShared`      | Share the cache between runners            | `true`                                |
| `gitlab-runner.runners.cache.s3BucketLocation` | Bucket region                              | `us-east-1`                           |
| `gitlab-runner.runners.cache.secretName`       | Secret to access key and secretkey from    | `gitlab-minio`                        |
| `gitlab-runner.runners.cache.s3CachePath`      | Path in the bucket                         | `gitlab-runner`                       |
| `gitlab-runner.runners.cache.s3CacheInsecure`  | Use http                                   | `false`                               |
| `gitlab-runner.runners.builds.cpuLimit`        | Build container cpu limit                  |                                       |
| `gitlab-runner.runners.builds.memoryLimit`     | Build container memory limit               |                                       |
| `gitlab-runner.runners.builds.cpuRequests`     | Build container requested cpu              |                                       |
| `gitlab-runner.runners.builds.memoryRequests`  | Build container requested memory           |                                       |
| `gitlab-runner.runners.service.cpuLimit`       | Service container cpu limit                |                                       |
| `gitlab-runner.runners.service.memoryLimit`    | Service container memory limit             |                                       |
| `gitlab-runner.runners.service.cpuRequests`    | Service container requested cpu            |                                       |
| `gitlab-runner.runners.service.memoryRequests` | Service container requested memory         |                                       |
| `gitlab-runner.resources.limits.cpu`           | Runner cpu limit                           |                                       |
| `gitlab-runner.resources.limits.memory`        | Runner memory limit                        |                                       |
| `gitlab-runner.resources.requests.cpu`         | Runner requested cpu                       |                                       |
| `gitlab-runner.resources.requests.memory`      | Runner requested memory                    |                                       |

## Chart configuration examples

### `gitlab-runner.pullSecrets`

`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`

```YAML
image: my.runner.repository
imagePullPolicy: Always
pullSecrets:
- name: my-secret-name
- name: my-secondary-secret-name
```
