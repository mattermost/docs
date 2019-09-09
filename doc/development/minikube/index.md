# Developing for Kubernetes with Minikube

This guide is meant to serve as a cross-plaform resource for setting up a local
Kubernetes development environment. In this guide, we'll be using
[Minikube](https://kubernetes.io/docs/getting-started-guides/minikube/) as it is the defacto standard.

## Getting Started with Minikube

We'll extract and expound on the official documentation from the
[Kubernetes project](https://kubernetes.io/),
[Running Kubernetes Locally with Minikube](https://kubernetes.io/docs/getting-started-guides/minikube/).

### Installing kubectl

The official documentation provides several options, but the result is that you
can do one of three things:

- Download as a part of the Google Cloud SDK from Google Cloud Platform's
  [Cloud SDK](https://cloud.google.com/sdk/) page. Once you have `gcloud`
  installed, you can install `kubectl`:

  ```sh
  sudo gcloud components install kubectl
  ```

  If you've already installed `kubectl` via this method, ensure it is updated:

  ```sh
  sudo gcloud components update
  ```

- Install directly from the [Google Storage APIs](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-via-curl).
- Install with the appropriate package management system:
  - Linux: your package manager of choice, or Snap.
  - [macOS](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos)
  - [Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-chocolatey-on-windows)

### Installing Minikube

See the [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/install-minikube/)
where they suggest directly installing from the [releases on GitHub](https://github.com/kubernetes/minikube/releases).

### Choosing a VM driver

For the purposes of cross-platform compatibility in this guide, we'll stick
with VirtualBox, however there are drivers for VMware Fusion, HyperV, KVM, and Xhyve.

### Starting / Stopping Minikube

Minikube resource requests must be set higher than the default for developing
the GitLab chart. The key configuration items can be found with
`minkube start --help`. A selection is provided below, for what we may want to
change according to the pieces being tested, and the requirements as listed:

- `--cpus int`: Number of CPUs allocated to the minikube VM (default `2`).
  The absolute minimum necessary CPU is `2`. Deploying the _complete_ chart requires `3`.
- `--memory int`: Amount of RAM allocated to the minikube VM (default `2048`).
  The absolute same minimum is `5120` (5 GB). Recommendation is `8192` (8 GB).
- `--disk-size string`: Disk size allocated to the minikube VM (format: `<number>[<unit>]`,
  where unit = `b`, `k`, `m` or `g`) (default `20g`). See GitLab's
  [storage](https://docs.gitlab.com/ce/install/requirements.html#storage) and
  [database](https://docs.gitlab.com/ce/install/requirements.html#database)
  requirements.

  NOTE: **Note**:
  This is created in your home directory under `~/.minikube/machines/minikube/`.

- `--kubernetes-version string`: The Kubernetes version that the minikube VM will use (e.g., `v1.2.3`).
- `--registry-mirror stringSlice`: Registry mirrors to pass to the Docker daemon.

NOTE: **Note:**
Changing these values in a second `start` command, requires to first delete
the existing instance with `minikube delete`, or manually you can alter the
properties with VirtualBox Manager.

Once you have all the tools installed and configured, starting at stopping Minikube
can be done with:

```sh
minikube start --cpus 3 --memory 8192
```

This command should output something similar to:

```
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

Take note of the result from running the `minikube ip` command. If the output is not `192.168.99.100`, the output IP will be needed later.

## Using Minikube

Minikube can be used directly as a Kubernetes installation, and treated as a
single node cluster. There are some behaviors that are slightly different between
Minikube and full-fledged Kubernetes clusters, such as [Google Container Engine (GKE)](https://cloud.google.com/).

Different:

- Persistent Volumes: `hostPath` only.

Unavailable:

- Load Balancers (requires cloud provider).
- Advanced Scheduling Policies (requires multiple nodes).

### Gotcha: Persistent Volumes

Minikube supports [PersistenVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
of the `hostPath` type, which are mapped to directories inside the VM. As Minikube
boots into a `tmpfs`, most directories will not persist across reboots via `minikube stop`.

Further details and listings of directories that do persist, can be found
in the [Minikube getting started guide](https://kubernetes.io/docs/getting-started-guides/minikube/#persistent-volumes).

### Enable Addons

Minikube handles some features apart from the base configuration. For the
development of this project, we'll need access to `Ingress`:

```sh
minikube addons enable ingress
```

### Connecting to the dashboard

You can find the URL for the dashboard by calling:

```sh
minikube dashboard --url
```

## Hooking Helm to Minikube

Once your Minikube is up and running, you can hook [Helm](https://helm.sh/)
to it with `helm init`.

For further details on Helm, see [Developing for Helm](../../installation/tools.md#helm).

## Deploying the chart

When deploying this chart into minikube, some chart resources need to be reduced or disabled.
It is not possible to use the `nginx-ingress` chart to provide ports `22`, `80`,
`443`. It's best to disable it and set the ingress class by setting
`nginx-ingress.enabled=false,global.ingress.class="nginx"`.

The `certmanager` chart can not be used with minikube. You must disable this by
setting `certmanager.install=false,global.ingress.configureCertmanager=false`.
As a result, if you don't provide your own SSL certificates, self-signed
certificates will be generated. The `gitlab-runner` chart is not compatible with
self-signed certificates at this time, and as such, should be disabled by setting
`gitlab-runner.install=false`.

### Deploying GitLab with recommended settings

When using the recommended 3 CPU and 8 GB of RAM, use
[`values-minikube.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/values-minikube.yaml)
as a base.

```shell
helm repo add gitlab https://charts.gitlab.io/
helm repo update
helm upgrade --install gitlab gitlab/gitlab \
  --timeout 600 \
  -f https://gitlab.com/gitlab-org/charts/gitlab/raw/master/examples/values-minikube.yaml
```

### Deploying GitLab with minimal settings

If using _absolute minimum_ resources, 2 CPU and 4GB of RAM, you must reduce all replicas
and disable unneeded services. See [`values-minikube-minimum.yaml`](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/examples/values-minikube-minimum.yaml)
as a reasonable base.

```shell
helm repo add gitlab https://charts.gitlab.io/
helm repo update
helm upgrade --install gitlab gitlab/gitlab \
  --timeout 600 \
  -f https://gitlab.com/gitlab-org/charts/gitlab/raw/master/examples/values-minikube-minimum.yaml
```

If the output of `minikube ip` was not `192.168.99.100`, add these arguments to override the IP endpoints in the example configuration files:

```sh
  --set global.hosts.domain=$(minikube ip) \
  --set global.hosts.externalIP=$(minikube ip).nip.io
```

### Handling DNS

The example configurations provided, configure the domain as `192.168.99.100.nip.io`
in an attempt to reduce the overhead of handling alterations to host files, or
other domain name resolution services. However, this relies on the network
reachability of [nip.io](http://nip.io).

If this is not available to you, then you may need to make alterations to your
`/etc/hosts` file, or provide another means of DNS resolution.

Example `/etc/hosts` file addition:

```text
192.168.99.100 gitlab.some.domain registry.some.domain minio.some.domain
```

### Incorporating Self-Signed CA

Once the chart is deployed, if using self-signed certificates, the user will be
given the notice on how to fetch the CA certificate that was generated. This
certificate can be added to the system store, so that all browsers, Docker daemon,
and `git` command recognize the deployed certificates as trusted. The method
depends on your operating system.

[BounCA](https://www.bounca.org) has a [good tutorial](https://www.bounca.org/tutorials/install_root_certificate.html),
covering most operating systems.

### Logging in

You can access the GitLab instance by visiting the domain specified, [https://gitlab.192.168.99.100.nip.io](https://gitlab.192.168.99.100.nip.io) is used in these examples. If you manually created the secret for initial root password, you can use that to sign in as root user. If not, GitLab automatically created a random password for the root user. This can be extracted by the following command (replace `<name>` by name of the release - which is `gitlab` if you used the command above).

```shell
kubectl get secret <name>-gitlab-initial-root-password -ojsonpath='{.data.password}' | base64 --decode ; echo
```
