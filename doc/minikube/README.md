# Developing for Kubernetes with Minikube

This guide is meant to serve as a cross-plaform resource for setting up a local Kubernetes development environment. In this guide, we'll be using [Minikube][minikube-getting-started] as it is current defacto.

## Getting Started with Minikube

We'll extract and expound on the official documentation from the [Kubernetes project][k8s-io], [Running Kubernetes Locally with Minikube][minikube-getting-started].

1. Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
1. Install [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
1. Choosing a [VM driver](https://github.com/kubernetes/minikube/blob/master/docs/drivers.md#driver-plugin-installation) (for this guide, VirtualBox)
1. Starting / Stopping Minikube

### Installing kubectl

The official documentation provides several options, but the result is that you can do one of three things:
- Download as a part of the [Google Cloud SDK][gcloud-sdk]
  - You can install the [Google Cloud SDK][gcloud-sdk] from Google Cloud Platform's [Cloud SDK](https://cloud.google.com/sdk/) page.
  - `sudo gcloud components install kubectl`
  - If `kubectl` already installed via this method, ensure it is updated: `sudo gcloud components update`
- Install directly from the [Google Storage APIs](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-via-curl)
- Install with the appropriate package management system.
  - Linux: your package manager of choice, or Snap
  - [MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos)
  - [Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-chocolatey-on-windows)

### Installing Minikube

See [install-minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) from the kubernetes documentation, where they suggest directly installing from the [releases on GitHub](https://github.com/kubernetes/minikube/releases)

### Choosing a VM driver

For the purposes of cross-plaform compatibility in this guide, we'll stick with VirtualBox, however there are drivers for VMware Fusion, HyperV, KVM, and Xhyve.

### Starting / Stopping Minikube

Once you have all the tools installed and configured, starting at stopping Minikube is easy:

```
[helm.gitlab.io]$ minikube start
Starting local Kubernetes v1.7.0 cluster...
Starting VM...
Downloading Minikube ISO
 97.80 MB / 97.80 MB [==============================================] 100.00% 0s
Getting VM IP address...
Moving files into cluster...
Setting up certs...
Starting cluster components...
Connecting to cluster...
Setting up kubeconfig...
Kubectl is now configured to use the cluster.
[helm.gitlab.io]$ minikube ip
192.168.99.100
[helm.gitlab.io]$ minikube stop
Stopping local Kubernetes cluster...
Machine stopped.
```

While this is simple, we may want to provide higher than default resources for developing GitLab applications. Key configuration items can be found with `minkube start --help`. A selection is provided below, for what we may want to change according to the pieces being tested, and the requirements as listed .

- `--cpus int`: Number of CPUs allocated to the minikube VM (default `2`). See [CPU](https://docs.gitlab.com/ce/install/requirements.html#cpu) requirements of GitLab
- `--memory int`: Amount of RAM allocated to the minikube VM (default `2048`). See [Memory](https://docs.gitlab.com/ce/install/requirements.html#memory) requirements of GitLab
- `--disk-size string`: Disk size allocated to the minikube VM (format: `<number>[<unit>]`, where unit = `b`, `k`, `m` or `g`) (default `20g`). See [Storage](https://docs.gitlab.com/ce/install/requirements.html#storage) and [Database](https://docs.gitlab.com/ce/install/requirements.html#database) requirements of GitLab. **Note**: *this is created in your home directory under `~/.minikube/machines/minikube/`*
- `--kubernetes-version string`: The kubernetes version that the minikube VM will use (ex: `v1.2.3`)
- `--registry-mirror stringSlice`: Registry mirrors to pass to the Docker daemon

*Note: changing these values in a second `start` commands requires first `delete`ing the existing instance with `minikube delete`, or manually you can alter the properties with VirtualBox Manager*

## Using Minikube

Minikube can be used directly as a Kubernetes installation, and treated as a single node cluster. There some behaviors that are slightly difference between Minikube and full-fledged Kubernetes clusters, such as [Google Container Engine (GKE)][gke].

Different:
- Persistent Volumes: `hostPath` only.

Unavailable:
- Load Balancers (requires cloud provider)
- Advanced Scheduling Policies (requires multiple nodes)

### Gotcha: Persistent Volumes

Minikube supports [PersistenVolumes](k8s-pv) of the `hostPath` type, which are mapped to directories inside the VM. As Minikube boots into a `tmpfs`, most directories will not persist across reboots via `minikube stop`.

Further details, and listings of directories that _do_ persist, can be found [in the getting started guide](https://kubernetes.io/docs/getting-started-guides/minikube/#persistent-volumes)

### Enable Addons

Minikube handles some features apart from the base configuration. For the development of this project, we'll need access to `Ingress` and `kube-dns` will be helpful.

- `minikube addons enable ingress`
- `minikube addons enable kube-dns`

### Connecting to the dashboard

You can find the URL for the dashboard by calling `minikube dashboard --url`.

## Hooking Helm to Minikube

Once your Minikube is up and running, you can hook [Helm] to it easily with `helm init`.

For further details on [Helm][helm], we'll move to [Developing for Helm](../helm/README.md)

[minikube-getting-started]: https://kubernetes.io/docs/getting-started-guides/minikube/
[k8s-io]: https://kubernetes.io/
[gcloud-sdk]: https://cloud.google.com/sdk/
[gke]: https://cloud.google.com/
[k8s-pv]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
[helm]: https://helm.sh/
