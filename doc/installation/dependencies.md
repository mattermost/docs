# Dependencies

Items and information needed:
- GKE cluster >= 1.8.5 (via `gcloud`)
- [kubectl][] latest version (part of `gcloud`)
- [helm][] latest version
- SSL certificates
- Secrets for Certificates, Registry, Redis
- A regional static IP in Google Cloud, with an A record in DNS

## Google Cloud SDK

Install this per [gcloud installation documentation][gcloud-install].
If already installed, ensure they are up to date with `gcloud components update`.

At the time of writing this doc, the output of `gcloud version`:

```
Google Cloud SDK 179.0.0
app-engine-python 1.9.62
bq 2.0.27
core 2017.11.06
gcloud
gsutil 4.28
kubectl
```

## Install with defaults

Google Cloud SDK is a dependency of this script, you will have to make sure it is set up correctly in order for the script to work. Follow the [instructions](../helm/README.md#connect-to-the-cluster) for connecting your GKE cluster.

The `[scripts/gke_bootstrap_script.sh](../../scripts/gke_bootstrap_script.sh)` script creates a new GKE cluster, sets up kubectl to connect to it and has helm installed and initialized.

The script reads various parameters from environment variables.

The table below describes all variables.

| Variable        | Description                                                          | Default value                    |
|-----------------|----------------------------------------------------------------------|----------------------------------|
| REGION          | The region where your cluster lives                                  | us-central1                      |
| ZONE            | The zone where your cluster instances lives                          | us-central1a                     |
| CLUSTER_NAME    | The name of the cluster                                              | gitlab-cluster                   |
| CLUSTER_VERSION | The version of your GKE cluster                                      | 1.8.5-gke.0                      |
| MACHINE_TYPE    | The cluster instances' type                                          | n1-standard-2                    |
| NUM_NODES       | The number of nodes required.                                        | 2                                |
| PROJECT         | the name of your project                                             | No defaults, required to be set. |
| RBAC_ENABLED    | If you know whether your cluster has RBAC enabled set this variable. | true                             |

Run the script, passing in your desired parameters. (The script can work with default parameters except for `PROJECT` which is required.)

```bash
PROJECT=<gcloud project name> ./scripts/gke_bootstrap_script.sh
```

> *Note:* You need to be logged into your account using gcloud before running the bootstrap script

 Skip the Custom Install section if you used the script.

## Custom Install

### Kubectl

Skip this if you ran the above install with defaults script

The [gcloud][] sdk & command contains `kubectl` binary. If you are not using gcloud,
you can setup kubectl using the installation documentation for [kubectl][].

At the time of writing this doc, the output of `kubectl version`:

```
Client Version: version.Info{Major:"1", Minor:"8", GitVersion:"v1.8.2", GitCommit:"bdaeafa71f6c7c04636251031f93464384d54963", GitTreeState:"clean", BuildDate:"2017-10-24T19:48:57Z", GoVersion:"go1.8.3", Compiler:"gc", Platform:"linux/amd64"}
Unable to connect to the server:
```

> Note: The server version of kubectl cannot be obtained until we connect to a
cluster. Proceed with setting up Helm.

### Helm

Skip this if you ran the above install with defaults script

Follow the [helm][] document for installation instructions.

# Next Steps

Once all dependencies are installed and configured, you can continue to setting up
[GKE resources](resources.md).

[gcloud]: https://cloud.google.com/sdk/gcloud/
[gcloud-install]: https://cloud.google.com/sdk/docs/quickstarts
[kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
[helm]: ../helm/README.md
