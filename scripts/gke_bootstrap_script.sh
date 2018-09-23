#!/bin/bash
# This bash script shall create a GKE cluster, an external IP, setup kubectl to
# connect to the cluster without changing the home kube config and finally installs
# helm with the appropriate service account if RBAC is enabled

set -e

REGION=${REGION-us-central1}
ZONE_EXTENSION=${ZONE_EXTENSION-b}
ZONE=${REGION}-${ZONE_EXTENSION}
CLUSTER_NAME=${CLUSTER_NAME-gitlab-cluster}
MACHINE_TYPE=${MACHINE_TYPE-n1-standard-4}
RBAC_ENABLED=${RBAC_ENABLED-true}
NUM_NODES=${NUM_NODES-2}
PREEMPTIBLE=${PREEMPTIBLE-false}
EXTRA_CREATE_ARGS=${EXTRA_CREATE_ARGS-""}
USE_STATIC_IP=${USE_STATIC_IP-false};
external_ip_name=${CLUSTER_NAME}-external-ip;

# MacOS does not support readlink, but it does have perl
KERNEL_NAME=$(uname -s)
if [ "${KERNEL_NAME}" = "Darwin" ]; then
  SCRIPT_PATH=$(perl -e 'use Cwd "abs_path";use File::Basename;print dirname(abs_path(shift))' "$0")
else
  SCRIPT_PATH=$(dirname "$(readlink -f "$0")")
fi

source $SCRIPT_PATH/common.sh;

function bootstrap(){
  set -e
  validate_required_tools;

  # Use the default cluster version for the specified zone if not provided
  if [ -z "${CLUSTER_VERSION}" ]; then
    CLUSTER_VERSION=$(gcloud container get-server-config --zone $ZONE --project $PROJECT --format='value(defaultClusterVersion)');
  fi

  if $PREEMPTIBLE; then
    EXTRA_CREATE_ARGS="$EXTRA_CREATE_ARGS --preemptible"
  fi

  gcloud container clusters create $CLUSTER_NAME --zone $ZONE \
    --cluster-version $CLUSTER_VERSION --machine-type $MACHINE_TYPE \
    --scopes "https://www.googleapis.com/auth/ndev.clouddns.readwrite","https://www.googleapis.com/auth/compute","https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" \
    --node-version $CLUSTER_VERSION --num-nodes $NUM_NODES --project $PROJECT --enable-basic-auth $EXTRA_CREATE_ARGS;

  if ${USE_STATIC_IP}; then
    gcloud compute addresses create $external_ip_name --region $REGION --project $PROJECT;
    address=$(gcloud compute addresses describe $external_ip_name --region $REGION --project $PROJECT --format='value(address)');

    echo "Successfully provisioned external IP address $address , You need to add an A record to the DNS name to point to this address. See https://gitlab.com/charts/gitlab/blob/master/doc/cloud/gke.md#dns-entry.";
  fi

  mkdir -p demo/.kube;
  touch demo/.kube/config;
  export KUBECONFIG=$(pwd)/demo/.kube/config;

  gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE --project $PROJECT;

  # Create roles for RBAC Helm
  if $RBAC_ENABLED; then
    status_code=$(curl -L -w '%{http_code}' -o rbac-config.yaml -s "https://gitlab.com/charts/gitlab/raw/master/doc/helm/examples/rbac-config.yaml");
    if [ "$status_code" != 200 ]; then
      echo "Failed to download rbac-config.yaml, status code: $status_code";
      exit 1;
    fi

    kubectl config set-credentials ${CLUSTER_NAME}-admin-user --username=admin --password=$(cluster_admin_password_gke)
    kubectl --user=${CLUSTER_NAME}-admin-user create -f rbac-config.yaml;
  fi

  echo "Installing helm..."
  helm init --wait --service-account tiller
  helm repo update

  if ! ${USE_STATIC_IP}; then
    helm install --name dns --namespace kube-system stable/external-dns \
      --set provider=google \
      --set google.project=$PROJECT \
      --set txtOwnerId=$CLUSTER_NAME \
      --set rbac.create=true \
      --set policy=sync
  fi
}

#Deletes everything created during bootstrap
function cleanup_gke_resources(){
  validate_required_tools;

  gcloud container clusters delete -q $CLUSTER_NAME --zone $ZONE --project $PROJECT;
  echo "Deleted $CLUSTER_NAME cluster successfully";

  if ${USE_STATIC_IP}; then
    gcloud compute addresses delete -q $external_ip_name --region $REGION --project $PROJECT;
    echo "Deleted ip: $external_ip_name successfully";
  fi

  echo "\033[;33m Warning: Disks, load balancers, DNS records, and other cloud resources created during the helm deployment are not deleted, please delete them manually from the gcp console \033[0m";
}

if [ -z "$1" ]; then
  echo "You need to pass up or down";
fi

case $1 in
  up)
    bootstrap;
    ;;
  down)
    cleanup_gke_resources;
    ;;
  chaos)
    $SCRIPT_PATH/kube-monkey.sh;
    ;;
  *)
    echo "Unknown command $1";
    exit 1;
  ;;
esac
