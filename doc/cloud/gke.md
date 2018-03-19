# Preparing GKE resources

To operate effectively, you will need to create a few resources before configuration and deployment of this chart.

You'll need a domain on which to host the services, which we will not cover here.

You will need a [static IP](#static-ip) for the Ingress, so that you can create a [DNS entry](#dns-entry) for your hostnames.

## Bootstrap

Google Cloud SDK is a dependency of this script, you will have to make sure it is set up correctly in order for the script to work.

Follow the [instructions](../helm/README.md#connect-to-the-cluster) for connecting your GKE cluster.

The [scripts/gke_bootstrap_script.sh](../../scripts/gke_bootstrap_script.sh) script creates a new GKE cluster, sets up kubectl to connect to it and initializes helm.

The script reads various parameters from environment variables and an argument `up` or `down` for bootstrap and clean up respectively.

The table below describes all variables.

| Variable        | Description                                                          | Default value                    |
|-----------------|----------------------------------------------------------------------|----------------------------------|
| REGION          | The region where your cluster lives                                  | us-central1                      |
| ZONE            | The zone where your cluster instances lives                          | us-central1a                     |
| CLUSTER_NAME    | The name of the cluster                                              | gitlab-cluster                   |
| CLUSTER_VERSION | The version of your GKE cluster                                      | 1.8.8-gke.0                      |
| MACHINE_TYPE    | The cluster instances' type                                          | n1-standard-4                    |
| NUM_NODES       | The number of nodes required.                                        | 2                                |
| PROJECT         | the id of your GCP project                                           | No defaults, required to be set. |
| RBAC_ENABLED    | If you know whether your cluster has RBAC enabled set this variable. | true                             |

Run the script, passing in your desired parameters. (The script can work with default parameters except for `PROJECT` which is required.)

```bash
PROJECT=<gcloud project id> ./scripts/gke_bootstrap_script.sh up
```

The script can also be used to clean up the created GKE resources by running

```bash
PROJECT=<gcloud project id> ./scripts/gke_bootstrap_script.sh down
```
> *Note:* You need to be logged into your account using gcloud before running the bootstrap script


## Static IP

**If you used the default bootstrap install script to setup your cluster, the script will have output your static IP address when it completed. Skip the rest of this section and use that IP address to configure DNS in the next section.**

External IP for ingress is required so that your cluster can be reachable. The external IP needs to be regional and in the same region as the cluster itself

> A global IP or an IP outside the region will not work.

To create a static IP run the following gcloud command:

`gcloud compute addresses create ${CLUSTER_NAME}-external-ip --region $REGION --project $PROJECT`

To get the address of the newly created IP run the following gcloud command:

`gcloud compute addresses describe ${CLUSTER_NAME}-external-ip --region $REGION --project $PROJECT --format='value(address)'`

We will use this IP to bind with a DNS name in the next section.

## DNS Entry

In order to use ingress host rules to access various components of gitlab we will need a public domain with an `A record` wild card DNS entry pointing to the IP we just created.

Follow [This](https://cloud.google.com/dns/quickstart) to create the DNS entry.

# Next Steps

Continue with the [installation of the chart](../installation/README.md) once you have the cluster up and running, and have the static IP and DNS entry ready.
