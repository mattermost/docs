#!/bin/bash
# This bash script shall create a GKE cluster, an external IP, setup kubectl to
# connect to the cluster without chaning the home kube config and finally installs
# helm with the appropriate service account if RBAC is enabled

set -e

REGION=${REGION-us-central1}
ZONE=${REGION}-a
CLUSTER_NAME=${CLUSTER_NAME-gitlab-cluster}
CLUSTER_VERSION=${CLUSTER_VERSION-1.8.8-gke.0}
MACHINE_TYPE=${MACHINE_TYPE-n1-standard-4}
RBAC_ENABLED=${RBAC_ENABLED-true}
NUM_NODES=${NUM_NODES-2}
PREEMPTIBLE=${PREEMPTIBLE-false}
EXTRA_CREATE_ARGS=${EXTRA_CREATE_ARGS-""}
external_ip_name=${CLUSTER_NAME}-external-ip;
DIR=$(dirname "$(readlink -f "$0")")

source $DIR/common.sh;

function bootstrap(){
  set -e
  validate_required_tools;

  if $PREEMPTIBLE; then
    EXTRA_CREATE_ARGS="$EXTRA_CREATE_ARGS --preemptible"
  fi

  gcloud container clusters create $CLUSTER_NAME --zone $ZONE \
    --cluster-version $CLUSTER_VERSION --machine-type $MACHINE_TYPE \
    --node-version $CLUSTER_VERSION --num-nodes $NUM_NODES --project $PROJECT $EXTRA_CREATE_ARGS;

  gcloud compute addresses create $external_ip_name --region $REGION --project $PROJECT;
  address=$(gcloud compute addresses describe $external_ip_name --region $REGION --project $PROJECT --format='value(address)');

  echo "Successfully provisioned external IP address $address , You need to add an A record to the DNS name to point to this address. See https://gitlab.com/charts/helm.gitlab.io/blob/master/doc/cloud/gke.md#dns-entry.";

  mkdir -p demo/.kube;
  touch demo/.kube/config;
  export KUBECONFIG=$(pwd)/demo/.kube/config;

  gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE --project $PROJECT;

  # Create roles for RBAC Helm
  if $RBAC_ENABLED; then
    status_code=$(curl -w '%{http_code}' -o rbac-config.yaml -s "https://gitlab.com/charts/helm.gitlab.io/raw/master/doc/helm/examples/rbac-config.yaml");
    if [ "$status_code" != 200 ]; then
      echo "Failed to download rbac-config.yaml, status code: $status_code";
      exit 1;
    fi

    password=$(cluster_admin_password_gke);

    kubectl --username=admin --password=$password create -f rbac-config.yaml;
  fi

  helm init --service-account tiller;

  helm repo update;
}

#Deletes everything created during bootstrap
function cleanup_gke_resources(){
  validate_required_tools;

  gcloud container clusters delete -q $CLUSTER_NAME --zone $ZONE --project $PROJECT;
  echo "Deleted $CLUSTER_NAME cluster successfully";

  gcloud compute addresses delete -q $external_ip_name --region $REGION --project $PROJECT;
  echo "Deleted ip: $external_ip_name successfully";

  echo "\033[;33m Warning: Disks created during the helm deployment are not deleted, please delete them manually from the gcp console \033[0m";
}

if [ -z "$1" ]; then
  echo "You need to pass up or down";
fi

DIR=$(dirname "$(readlink -f "$0")")

case $1 in
  up)
    bootstrap;
    ;;
  down)
    cleanup_gke_resources;
    ;;
  chaos)
    $DIR/kube-monkey.sh;
    ;;
  *)
    echo "Unknown command $1";
    exit 1;
  ;;
esac
