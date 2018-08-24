# Storage Guide

Some of the applications run within the GitLab chart require persistent storage to maintain state. This includes:

 - [gitaly](../charts/gitlab/gitaly) (persists the git repositories)
 - [postgres](https://github.com/kubernetes/charts/tree/master/stable/postgresql) (persists the gitlab database data)
 - [redis](../charts/redis) (persists gitlab job data)
 - [minio](../charts/minio) (persists the object storage data)

By default these applications will create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) for the storage they need, and use the cluster's [dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#dynamic), and the default Storage Class, to acquire access to a [Persistent Volume][pv].

For a production environment, you should review the settings of your cluster's default storage class to ensure they are what you desire. We recommend that Volumes be setup with a `reclaimPolicy` of `Retain`, and ideally with fast SSD storage if available. If the default storage class does not meet these requirements, you will want to look at using a custom storage class.

## Using a custom Storage Class

We recommend creating your own [Storage Class][] for use in these charts, and updating your config to use it.

For a production deploy of GitLab, we recommend you use [Persistent Volumes][pv] that have a reclaimPolicy set to `Retain` rather than `Delete`.  On some platforms like GKE, the default [Storage Class][] has a reclaimPolicy of `Delete`. Meaning that uninstalling GitLab, or deleting a PVC, will result in the persistent volume being completely deleted by an automated task that goes through and deletes the volume and disk from GCE. (The gitaly PVCs do not get deleted in this case because they belong to a [StatefulSet][])

For example, create a new [Storage Class][] object in your GKE cluster:

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: pd-gitlab
provisioner: kubernetes.io/gce-pd
reclaimPolicy: Retain
parameters:
  type: pd-standard
```

and use the class in your GitLab config:

```
--set gitlab.gitaly.persistence.storageClass=pd-gitlab
```

## Configuring the storage settings

> **Important**: After initial installation, making changes to your storage settings requires manually editing Kubernetes
> objects, so it's best to plan ahead before installing your production instance of GitLab to avoid extra storage migration work.

Storage configuration is provided per-service for the deployments that require persistent storage.

Gitaly (used for the git repositories), PostgreSQL, Minio, and Redis are all configured similarly. For example:

```
--set gitlab.gitaly.persistence.size=50Gi
--set gitlab.gitaly.persistence.storageClass=pd-gitlab
--set postgresql.persistence.size=8Gi
--set postgresql.persistence.storageClass=pd-gitlab
--set minio.persistence.size=10Gi
--set minio.persistence.storageClass=pd-gitlab
--set redis.persistence.size=5Gi
--set redis.persistence.storageClass=pd-gitlab
```

Documentation for all available persistence options for these can be found in the chart specific docs:

- [Gitaly persistence configuration](../charts/gitlab/gitaly/README.md#git-repository-persistence)
- [Minio persistence configuration](../charts/minio/README.md#persistence)
- [Redis persistence configuration](../charts/redis/README.md#persistence)
- [Upstream PostgreSQL chart configuration](https://github.com/helm/charts/tree/master/stable/postgresql#configuration)

> **Note**: Some of the advanced persistence options differ between PostgreSQL and the others, so it's important to check
> the specific documentation for each before making changes.

## Manually creating Static Volumes

If the cluster does not have a dynamic provisioner, you will need to create the [Persistent Volumes][pv] manually.

For example, create a new volume for an existing GCE disk:

```yaml
kind: PersistentVolume
apiVersion: v1
metadata:
  name: pv-gitaly
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 50Gi
  storageClassName: standard
  gcePersistentDisk:
    fsType: ext4
    pdName: pd-gitaly-disk
```

### Manually creating PersistentVolumeClaims

For services that are deployed using a [StatefulSet][], like `gitaly`, you will also need to manually create the [PersistentVolumeClaim][pvc].
These claims will be automatically used by the StatefulSet Pods, based on their name. [StatefulSet][]s match PVC names using the following:
`<mount-name>-<statefulset-pod-name>` and StatefulSet Pod names are determined using `<statefulset-name>-<pod-index>`, and in our chart the
StatefulSet names are determined using `<chart-release-name>-<service-name>`.

The `gitaly` service has a mount called `repo-data`. So if you installed the chart with the name `gitlab` when using helm install, the PVC name for the first gitaly pod would be
`repo-data-gitlab-gitaly-0`

Example:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: repo-data-gitlab-gitaly-0
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 50
  storageClassName: standard
  volumeName: pv-gitaly
```

> For services that do not use a [StatefulSet][]; once you create the volume, you can provide the `volumeName` to the config and this chart will still take care of creating the [volume claim][pvc], and it will attempt to bind to the volume you created. More information on how to provide the `volumeName`, and additional claim information, is available in the chart documentation for each included application.
>
>
> Using the volumeName in your config:
>
>`--set minio.persistence.volumeName=pv-minio`

## Making changes to storage after installation

After the initial installation, storage changes like migrating to new volumes,
or changing disk sizes, require editing the Kubernetes objects outside of the the
Helm upgrade command.

See the [managing persistent volumes documentation](../advanced/persistent-volumes/README.md).

[pv]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes
[pvc]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims
[Storage Class]: https://kubernetes.io/docs/concepts/storage/storage-classes/
[StatefulSet]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
