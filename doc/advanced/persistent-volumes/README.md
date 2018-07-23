# Managing Persistent Volumes

Some of the included services require persistent storage, configured through
[Persistent Volumes][pv] that specify which disks your cluster has access to.
Documentation on the storage configuration necessary to install this chart can be found in our
[Storage Guide][guide]

Storage changes after installation need to be manually handled by your cluster
administrators. Automated management of these volumes after installation is not
handled by the GitLab chart.

Examples of changes not automatically managed after initial installation
include:

 - Mounting Pods to different volumes
 - Changing the effective accessModes or [Storage Class][]
 - Expanding the storage size of your volume*<sup>1</sup>

<sup>1</sup> In Kubernetes 1.11, [expanding the storage size of your volume is supported](https://kubernetes.io/blog/2018/07/12/resizing-persistent-volumes-using-kubernetes/)
if you have `allowVolumeExpansion` configured to true in your [Storage Class][].

Automating theses changes is complicated due to:

1. Kubernetes does not allow changes to most fields in an existing [PersistentVolumeClaim][pvc]
2. Unless [manually configured][guide] otherwise, the [PVC][pvc] is the only reference to dynamically provisioned [PersistentVolumes][pv]
3. `Delete` is the default [reclaimPolicy][reclaim] for dynamically provisioned [PersistentVolumes][pv]

This means in order to make changes, we need to delete the[PersistentVolumeClaim][pvc]
and create a new one with our changes. But due to the default [reclaimPolicy][reclaim],
deleting the [PersistentVolumeClaim][pvc] may delete the [PersistentVolumes][pv]
and underlying disk. And unless configured with appropriate volumeNames and/or
labelSelectors, the chart won't know the volume to attach to.

We will continue to look into making this process easier, but for now a manual
process needs to be followed to make changes to your storage.

## Before making storage changes

> **Note**: The person making the changes needs to have admin access to the cluster,
> and appropriate access to the storage solutions being used. Often the changes
> will first need to be applied in the storage solution, then the results need
> to be updated in the Kubernetes.

TODO update existing volumes reclaimPolicy to retain

---

# WIP notes

First you make the desired changes to the disk outside the cluster. (Resize the disk in gke, or create a new disk from a snapshot or clone, etc)
Next step is to use kubectl edit on existing volume, to change their ReclaimPolicy to Retain. This is to ensure the system does not delete your existing volumes during pvc deletion.
After this the specifics diverge a bit based on whether you are using a new disk, or re-using the same one. But from a high level:

you ensure you have a volume with config that reflects your changes, and is pointing at your disk.
You have a re-created pvc with the new options.
You restart your pods to mount using the new options
You delete the statefulset, but keep the pods if you are working with a statefulset
You helm upgrade with the persistence settings that already match what you manually put in the pvcs. (Which will recreate the statefulset object)


[pv]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes
[pvc]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims
[reclaim]: https://kubernetes.io/docs/concepts/storage/storage-classes/#reclaim-policy
[guide]: ../../installation/storage.md
[Storage Class]: https://kubernetes.io/docs/concepts/storage/storage-classes/
