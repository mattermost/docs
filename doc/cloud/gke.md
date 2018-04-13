# Preparing GKE resources

For a fully functional GitLab instance, you will need to create a few resources before deployment of this chart.

1. A [GKE cluster](#creating-the-gke-cluster) with an associated external IP

## Creating the GKE cluster

To make getting started easier, we have provided a script to [automate cluster creation](#scripted-cluster-creation-on-gke). Alternatively, a cluster can be [created manually](#manual-cluster-creation) as well.

### Scripted cluster creation

We have created a [bootstrap script](../../scripts/gke_bootstrap_script.sh) to automate much of the setup process for users on GCP/GKE. It will:
* Create a new GKE cluster
* Allow the cluster to modify DNS records
* Setup kubectl, and connect it to the cluster
* Initialize Helm and install Tiller

Google Cloud SDK is a dependency of this script, you will have to make sure it is [set up correctly](../helm/README.md#connect-to-the-cluster) in order for the script to work.

The script reads various parameters from environment variables and an argument `up` or `down` for bootstrap and clean up respectively.

The table below describes all variables.

| Variable        | Description                                                                 | Default value                    |
|-----------------|-----------------------------------------------------------------------------|----------------------------------|
| REGION          | The region where your cluster lives                                         | us-central1                      |
| ZONE            | The zone where your cluster instances lives                                 | us-central1-a                     |
| CLUSTER_NAME    | The name of the cluster                                                     | gitlab-cluster                   |
| CLUSTER_VERSION | The version of your GKE cluster                                             | GKE default, check [GKE release notes][]. |
| MACHINE_TYPE    | The cluster instances' type                                                 | n1-standard-4                    |
| NUM_NODES       | The number of nodes required.                                               | 2                                |
| PROJECT         | the id of your GCP project                                                  | No defaults, required to be set. |
| RBAC_ENABLED    | If you know whether your cluster has RBAC enabled set this variable.        | true                             |
| PREEMPTIBLE     | Cheaper, clusters live at *most* 24 hrs. No SLA on nodes/disks              | false                            |
| USE_STATIC_IP   | Create a static IP for Gitlab instead of an ephemeral IP with managed DNS   | false                            |

[GKE release notes]: https://cloud.google.com/kubernetes-engine/release-notes

Run the script, passing in your desired parameters. (The script can work with default parameters except for `PROJECT` which is required.)

```bash
PROJECT=<gcloud project id> ./scripts/gke_bootstrap_script.sh up
```

The script can also be used to clean up the created GKE resources by running

```bash
PROJECT=<gcloud project id> ./scripts/gke_bootstrap_script.sh down
```

With the cluster created, continue to [creating the DNS entry](#dns-entry).

### Manual cluster creation

Two resources need to be created in GCP, a Kubernetes cluster and an external IP.

#### Creating the Kubernetes cluster

To provision the Kubernetes cluster manually, follow the [GKE instructions](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-container-cluster).

* We recommend a cluster with 8vCPU and 30gb of RAM.
* Make a note of the cluster's region, it will be needed in the next step.

#### Creating the external IP

An external IP is required so that your cluster can be reachable. The external IP needs to be regional and in the same region as the cluster itself.

> A global IP or an IP outside the cluster's region will not work.

To create a static IP run the following gcloud command:

`gcloud compute addresses create ${CLUSTER_NAME}-external-ip --region $REGION --project $PROJECT`

To get the address of the newly created IP run the following gcloud command:

`gcloud compute addresses describe ${CLUSTER_NAME}-external-ip --region $REGION --project $PROJECT --format='value(address)'`

We will use this IP to bind with a DNS name in the next section.

## DNS Entry

If you created your cluster manually or used the `USE_STATIC_IP` option with the scripted creation,
you'll need a public domain with an `A record` wild card DNS entry pointing to the IP we just created.

Follow [This](https://cloud.google.com/dns/quickstart) to create the DNS entry.

# Next Steps

Continue with the [installation of the chart](../installation/README.md) once you have the cluster up and running, and have the static IP and DNS entry ready.
