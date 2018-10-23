# Using the gitlab-runner chart

The gitlab-runner subchart provides a gitlab runner for running CI jobs. It is enabled by default and should work out of the box with support for caching using s3 compatible object storage.

## Requirements

This chart depends on the shared-secrets subchart to populate it's `registrationToken` for automatic registration. If you intend to run this chart as a stand-alone chart with an existing gitlab instance then you will need to manually set the `registrationToken` in the `gitlab-runner` secret to be equal to that displayed by the running gitlab instance.

## Configuration

There are no required settings, it should work out of the box if you deploy all of the charts together.

## Deploying a stand-alone runner

By default we do infer `gitlabUrl`, automatically generate a registration token, and generate it through the `migrations` chart. This behaviour will not work if you intend to deploy it with a running gitlab instance.

In this case you will need to set `gitlabUrl` value to be the url of the running gitlab instance. You will also need to manually create `gitlab-runner` secret and fill it with the `registrationToken` provided by the running gitlab.

## Using docker-in-docker

In order to run docker-in-docker, the runner container needs to be privileged to have access to the needed capabilities. To enable it set the `privileged` value to `true`.

### Security concerns

Priveleged containers have extended capabilities, for example they can mount arbitrary files from the host they run on. Make sure to run the container in an isolated environment such that nothing important runs beside it.

## Installation command line options

| Parameter                                    | Description                                | Default                             |
| ---                                          | ---                                        | ---                                 |
| gitlab-runner.image                          | runner image                               | gitlab/gitlab-runner:alpine-v10.5.0 |
| gitlab-runner.enabled                        |                                            | redis                               |
| gitlab-runner.imagePullPolicy                | image pull policy                          | IfNotPresent                        |
| gitlab-runner.init.image                     | initContainer image                        | busybox                             |
| gitlab-runner.init.tag                       | initContainer image tag                    | latest                              |
| gitlab-runner.pullSecrets                    | Secrets for the image repository           |                                     |
| gitlab-runner.unregisterRunners              | unregister all runners before termination  | true                                |
| gitlab-runner.concurrent                     | number of concurrent jobs                  | 20                                  |
| gitlab-runner.checkInterval                  | polling interval                           | 30s                                 |
| gitlab-runner.rbac.create                    | whether to create rbac service account     | true                                |
| gitlab-runner.rbac.clusterWideAccess         | deploy containers of jobs cluster-wide     | false                               |
| gitlab-runner.rbac.serviceAccountName        | name of the rbac service account to create | default                             |
| gitlab-runner.runners.image                  | default container image to use in builds   | ubuntu:16.04                        |
| gitlab-runner.runners.imagePullSecrets       | imagePullSecrets                           | []                                  |
| gitlab-runner.runners.privileged             | run in privileged mode,needed for `dind`   | false                               |
| gitlab-runner.runners.namespace              | numespace to run jobs in                   | default                             |
| gitlab-runner.runners.cache.cacheType        | cache type                                 | s3                                  |
| gitlab-runner.runners.cache.s3BucketName.    | name of the bucket                         | runner-cache                        |
| gitlab-runner.runners.cache.cacheShared      | share the cache between runners            | true                                |
| gitlab-runner.runners.cache.s3BucketLocation | bucket region                              | us-east-1                           |
| gitlab-runner.runners.cache.secretName       | secret to accesskey and secretkey from     | gitlab-minio                        |
| gitlab-runner.runners.cache.s3CachePath      | path in the bucket                         | gitlab-runner                       |
| gitlab-runner.runners.cache.s3CacheInsecure  | use http                                   | false                               |
| gitlab-runner.runners.builds.cpuLimit        | build container limit                      |                                     |
| gitlab-runner.runners.build.memoryLimit      | build container limit                      |                                     |
| gitlab-runner.runners.build.cpuRequests      | build container limit                      |                                     |
| gitlab-runner.runners.build.memoryRequests   | build container limit                      |                                     |
| gitlab-runner.runners.service.cpuLimit       | service container limit                    |                                     |
| gitlab-runner.runners.service.memoryLimit    | service container limit                    |                                     |
| gitlab-runner.runners.service.cpuRequests    | service container limit                    |                                     |
| gitlab-runner.runners.service.memoryRequests | service container limit                    |                                     |
| gitlab-runner.resources.limits.memory        | runner memory limit                        |                                     |
| gitlab-runner.resources.limits.cpu           | runner cpu limit                           |                                     |
| gitlab-runner.resources.requests.memory      | runner requested memory                    |                                     |
| gitlab-runner.resources.requests.cpu         | runner requested cpu                       |                                     |

## Chart configuration examples
### gitlab-runner.pullSecrets
`pullSecrets` allow you to authenticate to a private registry to pull images for a pod.

Additional details about private registries and their authentication methods
can be found in [the Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).

Below is an example use of `pullSecrets`
```YAML
image: my.runner.repository
imagePullPolicy: Always
pullSecrets:
- name: my-secret-name
- name: my-secondary-secret-name
```
