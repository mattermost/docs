#!/bin/bash

set -e

REGION=${REGION-us-central1}
ZONE=${REGION}-a
CLUSTER_NAME=${CLUSTER_NAME-gitlab-cluster}
RBAC_ENABLED=${RBAC_ENABLED-true}
DIR=$(dirname "$(readlink -f "$0")")

source $DIR/common.sh

validate_required_tools;
if $RBAC_ENABLED; then
  password=$(cluster_admin_password_gke);
  kubectl --username=admin --password=$password create -f $DIR/kube-monkey-resources/kube-monkey-role.yaml;
fi

kubectl --namespace=kube-system create configmap km-config --from-file=config.toml=$DIR/kube-monkey-resources/km-config.toml

kubectl create -f $DIR/kube-monkey-resources/kube-monkey-deployment.yaml
