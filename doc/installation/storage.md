# Storage Guide

## Overview

The following applications within the GitLab chart require persistent storage to maintain state.

- [gitaly](../charts/gitlab/gitaly/index.md) (persists the git repositories)
- [postgres](https://github.com/helm/charts/tree/master/stable/postgresql) (persists the gitlab database data)
- [redis](../charts/redis/index.md) (persists gitlab job data)
- [minio](../charts/minio/index.md) (persists the object storage data)

The administrator may choose to provision this storage using [dynamic][] or [static][] volume provisioning.

> **Important:** Minimize extra storage migration tasks after installation through pre-planning. Changes made
> after the first deployment require manual edits to existing Kubernetes objects prior to running `helm upgrade`.

## Typical Installation Behavior

The installer creates storage using the default storage class and [dynamic volume provisioning][dynamic]. Applications
connect to this storage through a [Persistent Volume Claim][pvc]. Administrators are encouraged to use [dynamic volume provisioning][dynamic]
instead of [static volume provisioning][static] when it is available.

> Administrators should determine the default storage class in their production environment using `kubectl get storageclass`
> and then examine it using `kubectl describe storageclass *STORAGE_CLASS_NAME*`. Some providers, such as Amazon EKS, do not provide a default storage class.

## Configuring Cluster Storage

### Recommendations

The default storage class should:

- Use fast SSD storage when available
- Set `reclaimPolicy` to `Retain`

> Uninstalling GitLab without the `reclaimPolicy` set to `Retain` allows automated jobs to completely delete the volume, disk and data.
> Some platforms set the default `reclaimPolicy` to `Delete`. The `gitaly` persistent volume claims do not follow this rule because
> they belong to a [StatefulSet][].

### Minimal Storage Class Configurations

The following `YAML` configurations provide the bare minimum required to create a custom storage class for GitLab. Replace
`CUSTOM_STORAGE_CLASS_NAME` with a value appropriate for the target installation environment.

- [Example Storage Class for GKE on Google Cloud](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/storage/gke_storage_class.yml)
- [Example Storage Class for EKS on Amazon Web Services](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/storage/eks_storage_class.yml)

> Some users report that Amazon EKS exhibits behavior where the creation of nodes are not always
> in the same zone as the pods. Setting the ***zone*** parameter above will mitigate any risk.

### Using the Custom Storage Class

Set the custom storage class to the cluster default and it will be used for all dynamic provisioning.

```sh
kubectl patch storageclass CUSTOM_STORAGE_CLASS_NAME -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

Alternatively, the custom storage class and other options may be provided per service to helm during installation. View
the provided [example configuration file](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/storage/helm_options.yml) and modify for your environment.

```sh
helm install -upgrade gitlab gitlab/gitlab -f HELM_OPTIONS_YAML_FILE
```

Follow the links below for further reading and additional persistence options:

- [Gitaly persistence configuration](../charts/gitlab/gitaly/index.md#git-repository-persistence)
- [Minio persistence configuration](../charts/minio/index.md#persistence)
- [Redis persistence configuration](../charts/redis/index.md#persistence)
- [Upstream PostgreSQL chart configuration](https://github.com/helm/charts/tree/master/stable/postgresql#configuration)

> **Note**: Some of the advanced persistence options differ between PostgreSQL and the others, so it's important to check
> the specific documentation for each before making changes.

## Using Static Volume Provisioning

Dynamic volume provisioning is recommended, however, some clusters or environments may not support it. Administrators
will need to create the [Persistent Volume][pv] manually.

### Using Google GKE

1. [Create a persistent disk in the cluster.](https://kubernetes.io/docs/concepts/storage/volumes/#creating-a-pd)

```sh
gcloud compute disks create --size=50GB --zone=*GKE_ZONE* *DISK_VOLUME_NAME*
```

1. Create the Persistent Volume after modifying the [example `YAML` configuration](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/storage/gke_pv_example.yml).

```sh
kubectl create -f *PV_YAML_FILE*
```

### Using Amazon EKS

1. [Create a persistent disk in the cluster.](https://kubernetes.io/docs/concepts/storage/volumes/#creating-an-ebs-volume)

```sh
aws ec2 create-volume --availability-zone=*AWS_ZONE* --size=10 --volume-type=gp2
```

1. Create the Persistent Volume after modifying the [example `YAML` configuration](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/storage/eks_pv_example.yml).

```sh
kubectl create -f *PV_YAML_FILE*
```

### Manually creating PersistentVolumeClaims

The ***gitaly*** service deploys using a [StatefulSet][]. Create the [PersistentVolumeClaim][pvc]
using the following naming convention for it to be properly recognized and used.

```
<mount-name>-<statefulset-pod-name>
```

The `mount-name` for ***gitaly*** is ***repo-data***. The StatefulSet pod names are created using:

```
<statefulset-name>-<pod-index>
```

The GitLab Cloud Native Chart determines the `statefulset-name` using:

```
<chart-release-name>-<service-name>
```

The correct name for the ***gitaly*** PersistentVolumeClaim is: ***repo-data-gitlab-gitaly-0***.

Modify the [example YAML configuration](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/storage/gitaly_persistent_volume_claim.yml) for your environment and reference it when invoking `helm`.

> The other services that do not use a [StatefulSet][] allow administrators to provide the `volumeName`
> to the config. This chart will still take care of creating the [volume claim][pvc] and attempt to bind
> to the manually created volume. Check the chart documentation for each included application.
>
> For most cases, just modify the [example yaml config](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/storage/use_manual_volumes.yml) keeping only those services which
> will use the manually created disk volumes.

## Making changes to storage after installation

After the initial installation, storage changes like migrating to new volumes,
or changing disk sizes, require editing the Kubernetes objects outside of the
Helm upgrade command.

See the [managing persistent volumes documentation](../advanced/persistent-volumes/index.md).

## Optional volumes

For larger installations, you may need to add persistent storage to the task-runner pod to get backups/restores working. See our [troubleshooting documentation](../backup-restore/#pod-eviction-issues) for a guide on how to do this.

[pv]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes
[pvc]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims
[Storage Class]: https://kubernetes.io/docs/concepts/storage/storage-classes/
[StatefulSet]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
[dynamic]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#dynamic
[static]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#static
