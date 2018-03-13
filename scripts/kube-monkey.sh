#!/bin/bash

REGION=${REGION-us-central1}
ZONE=${REGION}-a
CLUSTER_NAME=${CLUSTER_NAME-gitlab-cluster}
RBAC_ENABLED=${RBAC_ENABLED-true}

if [ -z "$PROJECT" ]; then
  echo "$PROJECT needs to be set to your project id";
  exit 1;
fi

command -v gcloud  >/dev/null 2>&1 || { echo >&2 "gcloud is required please follow: https://cloud.google.com/sdk/downloads"; exit 1; }
command -v kubectl >/dev/null 2>&1 || { echo >&2 "kubectl is required please follow: https://kubernetes.io/docs/tasks/tools/install-kubectl"; exit 1; }
command -v helm    >/dev/null 2>&1 || { echo >&2 "helm is required please follow: https://github.com/kubernetes/helm/blob/master/docs/install.md"; exit 1; }

gcloud container clusters list >/dev/null 2>&1 || { echo >&2 "Gcloud seems to be configured incorrectly or authentication is unsuccessfull"; exit 1; }

DIR=$(dirname "$(readlink -f "$0")")

if $RBAC_ENABLED; then
  password=$(gcloud container clusters describe $CLUSTER_NAME --zone $ZONE --project $PROJECT --format='value(masterAuth.password)');
  kubectl --username=admin --password=$password create -f $DIR/kube-monkey-resources/kube-monkey-role.yaml;
fi

kubectl --namespace=kube-system create configmap km-config --from-file=config.toml=$DIR/kube-monkey-resources/km-config.toml

kubectl create -f $DIR/kube-monkey-resources/kube-monkey-deployment.yaml
