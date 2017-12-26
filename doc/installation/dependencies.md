# Dependencies

Items and information needed:
- GKE cluster (via `gcloud`)
- [kubectl][] latest version (part of `gcloud`)
- [helm][] latest version
- SSL certificates
- Secrets for Certificates, Registry, Redis
- A regional static IP in Google Cloud, with an A record in DNS

## Gcloud

Install this per [gcloud installation documentation][gcloud].
If already installed, ensure they are up to date with `gcloud components update`.

At the time of writing this doc, the output of `gcloud version`:

```
$ gcloud version
Google Cloud SDK 179.0.0
app-engine-python 1.9.62
bq 2.0.27
core 2017.11.06
gcloud
gsutil 4.28
kubectl
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"8", GitVersion:"v1.8.2", GitCommit:"bdaeafa71f6c7c04636251031f93464384d54963", GitTreeState:"clean", BuildDate:"2017-10-24T19:48:57Z", GoVersion:"go1.8.3", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"7+", GitVersion:"v1.7.8-gke.0", GitCommit:"a7061d4b09b53ab4099e3b5ca3e80fb172e1b018", GitTreeState:"clean", BuildDate:"2017-10-10T18:48:45Z", GoVersion:"go1.8.3", Compiler:"gc", Platform:"linux/amd64"}
```
### Kubectl

The [gcloud][] sdk & command contains `kubectl` binary. If you are not using gcloud,
you can setup kubectl using the installation documentation for [kubectl][].

### Helm

Follow the [helm][] document for [installation instructions](https://github.com/kubernetes/helm#install).

Once all dependencies are installed and configured, you can continue to
[GitLab configuration](README.md#Configure).


[gcloud]: https://cloud.google.com/sdk/gcloud/
[kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
[helm]: helm/README.md
