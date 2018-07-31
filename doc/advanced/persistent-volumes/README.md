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

 - Mounting different volumes to the Pods
 - Changing the effective accessModes or [Storage Class][]
 - Expanding the storage size of your volume*<sup>1</sup>

<sup>1</sup> In Kubernetes 1.11, [expanding the storage size of your volume is supported](https://kubernetes.io/blog/2018/07/12/resizing-persistent-volumes-using-kubernetes/)
if you have `allowVolumeExpansion` configured to true in your [Storage Class][].

Automating theses changes is complicated due to:

1. Kubernetes does not allow changes to most fields in an existing [PersistentVolumeClaim][pvc]
2. Unless [manually configured][guide], the [PVC][pvc] is the only reference to dynamically provisioned [PersistentVolumes][pv]
3. `Delete` is the default [reclaimPolicy][reclaim] for dynamically provisioned [PersistentVolumes][pv]

This means in order to make changes, we need to delete the [PersistentVolumeClaim][pvc]
and create a new one with our changes. But due to the default [reclaimPolicy][reclaim],
deleting the [PersistentVolumeClaim][pvc] may delete the [PersistentVolumes][pv]
and underlying disk. And unless configured with appropriate volumeNames and/or
labelSelectors, the chart won't know the volume to attach to.

We will continue to look into making this process easier, but for now a manual
process needs to be followed to make changes to your storage.

## Locate the GitLab Volumes

Find the volumes/claims that are being used:

```bash
kubectl --namespace <namespace> get PersistentVolumeClaims -l release=<chart release name> -ojsonpath='{range .items[*]}{.spec.volumeName}{"\t"}{.metadata.labels.app}{"\n"}{end}'
```

- `<namespace>` should be replaced with the namespace where you installed the GitLab chart.
- `<chart release name>` should be replaced with the name you used to install the GitLab chart.

The command will print a list of the volume names, followed by the name of the
service they are for.

For example:

```bash
$ kubectl --namespace helm-charts-win get PersistentVolumeClaims -l release=review-update-app-h8qogp -ojsonpath='{range .items[*]}{.spec.volumeName}{"\t"}{.metadata.labels.app}{"\n"}{end}'
pvc-6247502b-8c2d-11e8-8267-42010a9a0113	gitaly
pvc-61bbc05e-8c2d-11e8-8267-42010a9a0113	minio
pvc-61bc6069-8c2d-11e8-8267-42010a9a0113	postgresql
pvc-61bcd6d2-8c2d-11e8-8267-42010a9a0113	prometheus
pvc-61bdf136-8c2d-11e8-8267-42010a9a0113	redis
```

## Before making storage changes

> **Note**: The person making the changes needs to have admin access to the cluster,
> and appropriate access to the storage solutions being used. Often the changes
> will first need to be applied in the storage solution, then the results need
> to be updated in Kubernetes.

Before making changes, you should ensure your [PersistentVolumes][pv] are using
the `Retain` [reclaimPolicy][reclaim] so they don't get removed while you are
making changes.

First, [find the volumes/claims that are being used](#locate-the-gitlab-volumes).

Next, edit each volume and change the value of `persistentVolumeReclaimPolicy`
under the `spec` field, to be `Retain` rather than `Delete`

For example:

```bash
$ kubectl --namespace helm-charts-win edit PersistentVolume pvc-6247502b-8c2d-11e8-8267-42010a9a0113
```

<details>
  <summary>
    Editing Output:
  </summary>

  <br><pre><code>
  # Please edit the object below. Lines beginning with a '#' will be ignored,
  # and an empty file will abort the edit. If an error occurs while saving this file will be
  # reopened with the relevant failures.
  #
  apiVersion: v1
  kind: PersistentVolume
  metadata:
    annotations:
      kubernetes.io/createdby: gce-pd-dynamic-provisioner
      pv.kubernetes.io/bound-by-controller: "yes"
      pv.kubernetes.io/provisioned-by: kubernetes.io/gce-pd
    creationTimestamp: 2018-07-20T14:58:43Z
    labels:
      failure-domain.beta.kubernetes.io/region: europe-west2
      failure-domain.beta.kubernetes.io/zone: europe-west2-b
    name: pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    resourceVersion: "48362431"
    selfLink: /api/v1/persistentvolumes/pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    uid: 650bd649-8c2d-11e8-8267-42010a9a0113
  spec:
    accessModes:
    - ReadWriteOnce
    capacity:
      storage: 50Gi
    claimRef:
      apiVersion: v1
      kind: PersistentVolumeClaim
      name: repo-data-review-update-app-h8qogp-gitaly-0
      namespace: helm-charts-win
      resourceVersion: "48362307"
      uid: 6247502b-8c2d-11e8-8267-42010a9a0113
    gcePersistentDisk:
      fsType: ext4
      pdName: gke-cloud-native-81a17-pvc-6247502b-8c2d-11e8-8267-42010a9a0113
  # Changed the following line
    persistentVolumeReclaimPolicy: Retain
    storageClassName: standard
  status:
    phase: Bound
  </code></pre><br>
</details>

## Making storage changes

First, make the desired changes to the disk outside of the cluster. (Resize the
disk in gke, or create a new disk from a snapshot or clone, etc).

How you do this, and whether or not it can be done live, without downtime, is
dependant on the storage solutions you are using, and can't be covered by this
document.

Next, evaluate whether you need these changes to be reflected in the Kubernetes
objects. For example: with expanding the disk storage size, the storage size
settings in the [PersistentVolumeClaim][pvc] will only be used when a new volume
resource is requested. So you would only need to increase the values in the
[PersistentVolumeClaim][pvc] if you intend to scale up more disks (for use in
additional gitaly pods).

If you do need to have the changes reflected in Kubernetes, be sure that you've
updated your reclaim policy on the volumes as described in the [Before making storage changes](#before-making-storage-changes)
section.

The paths we have documented for storage changes are:

- [Changes to an existing Volume](#changes-to-an-existing-volume)
- [Switching to a different Volume](#switching-to-a-different-volume)

### Changes to an existing Volume

First [locate the volume name](#locate-the-gitlab-volumes) you are changing.

Use `kubectl edit` to make the desired config changes to the volume. (These changes
should only be updates to reflect the real state of the attached disk)

For example:

```bash
$ kubectl --namespace helm-charts-win edit PersistentVolume pvc-6247502b-8c2d-11e8-8267-42010a9a0113
```

<details>
  <summary>
    Editing Output:
  </summary>

  <br><pre><code>
  # Please edit the object below. Lines beginning with a '#' will be ignored,
  # and an empty file will abort the edit. If an error occurs while saving this file will be
  # reopened with the relevant failures.
  #
  apiVersion: v1
  kind: PersistentVolume
  metadata:
    annotations:
      kubernetes.io/createdby: gce-pd-dynamic-provisioner
      pv.kubernetes.io/bound-by-controller: "yes"
      pv.kubernetes.io/provisioned-by: kubernetes.io/gce-pd
    creationTimestamp: 2018-07-20T14:58:43Z
    labels:
      failure-domain.beta.kubernetes.io/region: europe-west2
      failure-domain.beta.kubernetes.io/zone: europe-west2-b
    name: pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    resourceVersion: "48362431"
    selfLink: /api/v1/persistentvolumes/pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    uid: 650bd649-8c2d-11e8-8267-42010a9a0113
  spec:
    accessModes:
    - ReadWriteOnce
    capacity:
      # Updated the storage size
      storage: 100Gi
    claimRef:
      apiVersion: v1
      kind: PersistentVolumeClaim
      name: repo-data-review-update-app-h8qogp-gitaly-0
      namespace: helm-charts-win
      resourceVersion: "48362307"
      uid: 6247502b-8c2d-11e8-8267-42010a9a0113
    gcePersistentDisk:
      fsType: ext4
      pdName: gke-cloud-native-81a17-pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    persistentVolumeReclaimPolicy: Retain
    storageClassName: standard
  status:
    phase: Bound
  </code></pre><br>
</details>
<br>

Now that the changes have been reflected in the [volume][pv], we need to update
the [claim][pvc].

Follow the instructions in the [Make changes to the PersistentVolumeClaim](#make-changes-to-the-persistentvolumeclaim) section.

#### Update the volume to bind to the claim

In a separate terminal, start watching to see when the [claim][pvc] has its status change to bound,
and then move onto the next step to make the volume available for use in the new claim.

```bash
kubectl --namespace <namespace> get --watch PersistentVolumeClaim <claim name>
```

Edit the volume to make it available to the new claim. Remove the `.spec.claimRef` section.

```bash
kubectl --namespace <namespace> edit PersistentVolume <volume name>
```

<details>
  <summary>
    Editing Output:
  </summary>

  <br><pre><code>
  # Please edit the object below. Lines beginning with a '#' will be ignored,
  # and an empty file will abort the edit. If an error occurs while saving this file will be
  # reopened with the relevant failures.
  #
  apiVersion: v1
  kind: PersistentVolume
  metadata:
    annotations:
      kubernetes.io/createdby: gce-pd-dynamic-provisioner
      pv.kubernetes.io/bound-by-controller: "yes"
      pv.kubernetes.io/provisioned-by: kubernetes.io/gce-pd
    creationTimestamp: 2018-07-20T14:58:43Z
    labels:
      failure-domain.beta.kubernetes.io/region: europe-west2
      failure-domain.beta.kubernetes.io/zone: europe-west2-b
    name: pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    resourceVersion: "48362431"
    selfLink: /api/v1/persistentvolumes/pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    uid: 650bd649-8c2d-11e8-8267-42010a9a0113
  spec:
    accessModes:
    - ReadWriteOnce
    capacity:
      storage: 100Gi
    gcePersistentDisk:
      fsType: ext4
      pdName: gke-cloud-native-81a17-pvc-6247502b-8c2d-11e8-8267-42010a9a0113
    persistentVolumeReclaimPolicy: Retain
    storageClassName: standard
  status:
    phase: Released
  </code></pre><br>
</details>
<br>

Shortly after making the change to the [Volume][pv], the terminal watching the claim status should show `Bound`.

Finally, [apply the changes to the GitLab chart](#apply-the-changes-to-the-gitlab-chart)

### Switching to a different Volume

If you want to switch to using a new volume, using a disk that has a copy of the
appropriate data from the old volume, then first you need to create the the new
[Persistent Volume][pv] in Kubernetes.

In order to create a [Persistent Volume][pv] for your disk, you will need to
locate the [driver specific documentation](https://kubernetes.io/docs/concepts/storage/volumes/#types-of-volumes)
for your storage type.

There are a couple of things to keep in mind when following the driver documentation:

- You need to use the driver to create a [Persistent Volume][pv], not a Pod object with a volume as shown in a lot of the documentation.
- You do **not** want to create a [PersistentVolumeClaim][pvc] for the volume, we will be editing the existing claim instead.

The driver documentation often includes examples for using the driver in a Pod, for example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: k8s.gcr.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /test-pd
      name: test-volume
  volumes:
  - name: test-volume
    # This GCE PD must already exist.
    gcePersistentDisk:
      pdName: my-data-disk
      fsType: ext4
```

What you actually want, is to create a [Persistent Volume][pv], like so:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: test-volume
spec:
  capacity:
    storage: 400Gi
  accessModes:
  - ReadWriteOnce
  gcePersistentDisk:
    pdName: my-data-disk
    fsType: ext4
```

You normally create a local `yaml` file with the [PersistentVolume][pv] information,
then issue a create command to Kubernetes to create the object using the file.

```bash
kubectl --namespace <your namespace> create -f <local-pv-file>.yaml
```

Once your volume is created, you can move on to [Making changes to the PersistentVolumeClaim](#make-changes-to-the-persistentvolumeclaim)

## Make changes to the PersistentVolumeClaim

Find the [PersistentVolumeClaim][pvc] you want to change.

```bash
kubectl --namespace <namespace> get PersistentVolumeClaims -l release=<chart release name> -ojsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.labels.app}{"\n"}{end}'
```

- `<namespace>` should be replaced with the namespace where you installed the GitLab chart.
- `<chart release name>` should be replaced with the name you used to install the GitLab chart.

The command will print a list of the PersistentVolumeClaim names, followed by the name of the
service they are for.


Then save a copy of the [claim][pvc] to your local filesystem:

```bash
kubectl --namespace <namespace> get PersistentVolumeClaim <claim name> -o yaml > <claim name>.bak.yaml
```

<details>
  <summary>
    Example Output:
  </summary>

  <br><pre><code>
  apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
    annotations:
      pv.kubernetes.io/bind-completed: "yes"
      pv.kubernetes.io/bound-by-controller: "yes"
      volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/gce-pd
    creationTimestamp: 2018-07-20T14:58:38Z
    labels:
      app: gitaly
      release: review-update-app-h8qogp
    name: repo-data-review-update-app-h8qogp-gitaly-0
    namespace: helm-charts-win
    resourceVersion: "48362433"
    selfLink: /api/v1/namespaces/helm-charts-win/persistentvolumeclaims/repo-data-review-update-app-h8qogp-gitaly-0
    uid: 6247502b-8c2d-11e8-8267-42010a9a0113
  spec:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 50Gi
    storageClassName: standard
    volumeName: pvc-6247502b-8c2d-11e8-8267-42010a9a0113
  status:
    accessModes:
    - ReadWriteOnce
    capacity:
      storage: 50Gi
    phase: Bound
  </code></pre><br>
</details>
<br>

Create a new yaml file for a new PVC object. Have it use the same `metadata.name`, `metadata.labels`, `metadata,namespace`, and `spec` fields. (With your updates applied). And drop the other settings:

Example:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  labels:
    app: gitaly
    release: review-update-app-h8qogp
  name: repo-data-review-update-app-h8qogp-gitaly-0
  namespace: helm-charts-win
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      # This is our updated field
      storage: 100Gi
  storageClassName: standard
  volumeName: pvc-6247502b-8c2d-11e8-8267-42010a9a0113
```

Now delete the old [claim][pvc]:

```bash
kubectl --namespace <namespace> delete PersistentVolumeClaim <claim name>
```

Create the new claim:

```bash
kubectl --namespace <namespace> create PersistentVolumeClaim -f <new claim yaml file>
```

If you are binding to the same [PersistentVolume][pv] that was previous bound to
the claim, then proceed to [update the volume to bind to the claim](#update-the-volume-to-bind-to-the-claim)

Otherwise, if you have bound the claim to a new volume, move onto [apply the changes to the GitLab chart](#apply-the-changes-to-the-gitlab-chart)

## Apply the changes to the GitLab chart

After making changes to the [PersistentVolumes][pv] and [PersistentVolumeClaims][pvc],
you will also want to issue a helm update with the changes applied to the chart
settings as well.

See the [installation storage guide](../../installation/storage.md#configuring-the-storage-settings)
for the options.

> **Note**: If you made changes to the Gitaly [volume claim][pvc], you will need to delete the
> Gitaly [StatefulSet][statefulset] before you will be able to issue a helm update. This is
> because the StatefulSet's Volume Template is immutable, and cannot be changed.
>
> You can delete the statefulset without deleting the Gitaly Pods:
> `kubectl --namespace <namespace> delete --cascade=false StatefulSet <release-name>-gitaly`
> The helm update command will recreate the StatefulSet, which will adopt and
> update the Gitaly pods.

Update the chart, and include the updated configuration:

Example:

```bash
helm --namespace helm-charts-win upgrade --install review-update-app-h8qogp gitlab/gitlab \
  --set gitlab.gitaly.persistence.size=100Gi \
  <your other config settings>
```

[pv]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes
[pvc]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims
[reclaim]: https://kubernetes.io/docs/concepts/storage/storage-classes/#reclaim-policy
[statefulset]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
[guide]: ../../installation/storage.md
[Storage Class]: https://kubernetes.io/docs/concepts/storage/storage-classes/
