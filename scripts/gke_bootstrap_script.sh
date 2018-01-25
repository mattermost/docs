#!/bin/bash
# This bash script shall create a GKE cluster, an external IP, setup kubectl to
# connect to the cluster without chaning the home kube config and finally installs
# helm with the appropriate service account if RBAC is enabled

set -e

REGION=${REGION-us-central1}
ZONE=${REGION}-a
CLUSTER_NAME=${CLUSTER_NAME-gitlab-cluster}
CLUSTER_VERSION=${CLUSTER_VERSION-1.8.5-gke.0}
MACHINE_TYPE=${MACHINE_TYPE-n1-standard-2}
RBAC_ENABLED=${RBAC_ENABLED-true}
NUM_NODES=${NUM_NODES-2}

if [ -z "$PROJECT" ]; then
  echo "$PROJECT needs to be set to your project id";
  exit 1;
fi

command -v gcloud >/dev/null 2>&1 || { echo >&2 "gcloud is required please follow: https://cloud.google.com/sdk/downloads"; exit 1; }
command -v kubectl >/dev/null 2>&1 || { echo >&2 "kubectl is required please follow: https://kubernetes.io/docs/tasks/tools/install-kubectl"; exit 1; }

gcloud container clusters list >/dev/null 2>&1 || { echo >&2 "Gcloud seems to be configured incorrectly or authentication is unsuccessfull"; exit 1; }

gcloud container clusters create $CLUSTER_NAME --zone $ZONE \
  --cluster-version $CLUSTER_VERSION --machine-type $MACHINE_TYPE \
  --node-version $CLUSTER_VERSION --num-nodes $NUM_NODES --project $PROJECT

external_ip_name=${CLUSTER_NAME}-external-ip
gcloud compute addresses create $external_ip_name --region $REGION --project $PROJECT
address=$(gcloud compute addresses describe $external_ip_name --region $REGION --project $PROJECT --format='value(address)')

echo "Successfully provisioned external IP address $address , You need to add an A record to the DNS name to point to this address. See https://gitlab.com/charts/helm.gitlab.io/blob/master/doc/installation/resources.md#dns-entry."

mkdir -p demo/.kube
touch demo/.kube/config
export KUBECONFIG=$(pwd)/demo/.kube/config

gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE --project $PROJECT

# Get helm
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash

# Create roles for RBAC Helm
if $RBAC_ENABLED; then
  curl -o rbac-config.yaml -s "https://gitlab.com/charts/helm.gitlab.io/raw/master/doc/helm/examples/rbac-config.yaml"
  password=$(gcloud container clusters describe $CLUSTER_NAME --zone $ZONE --project $PROJECT --format='value(masterAuth.password)')

  kubectl --username=admin --password=$password create -f rbac-config.yaml
fi

helm init --service-account tiller

helm repo update
