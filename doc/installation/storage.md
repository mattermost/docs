# Storage Guide

Some of the applications run within the GitLab chart require persistent storage to maintain state. This includes:

 - postgres (persists the gitlab database data)
 - redis (persists gitlab job data)
 - gitaly (persists the git repositories)
 - minio (persists the object storage data)

By default these applications will create a [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) for the storage they need, and use the cluster's [dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#dynamic), and the default Storage Class, to acquire access to a [Persistent Volume][pv].

For a production environment, you should review the settings of your cluster's default storage class to ensure they are what you desire. We recommend that Volumes be setup with a `reclaimPolicy` of `Retain`, and ideally with fast SSD storage if available. If the default storage class does not meet these requirements, you will want to look at using a custom storage class.

## Using a custom Storage Class

For a production deploy of GitLab, we recommend you use [Persistent Volumes][pv] that have a reclaimPolicy set to `Retain` rather than `Delete`.  The default [Storage Class][] on GKE, named `standard`, has a reclaimPolicy of `Delete`. Meaning that uninstalling GitLab, or deleting a PVC, will result in the persistent volume being completely deleted by an automated task that goes through and deletes the volume and disk from GCE.

We recommend creating your own [Storage Class][] for use in these charts, and updating your config to use it.

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

## Manually creating Static Volumes

If the cluster does not have a dynamic provisioner, you will need to create the [Persistent Volumes][pv] manually, and provide the `volumeName` to the application. This chart will still take care of creating the volume claim, and it will attempt to bind to the volume you created. More information on how to provide the `volumeName`, and additional claim information, is available in the chart documentation for each included application.

For example, create a new volume for an existing GCE disk:

```
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

and using the volumeName in your GitLab config:

```
--set gitlab.gitaly.persistence.volumeName=pv-gitaly
```

[pv]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes
[Storage Class]: https://kubernetes.io/docs/concepts/storage/storage-classes/
