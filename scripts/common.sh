#!/bin/bash

# Checks that appropriate gke params are set and
# that gcloud and kubectl are properly installed and authenticated

function validate_required_tools(){
  if [ -z "$PROJECT" ]; then
    echo "$PROJECT needs to be set to your project id";
    exit 1;
  fi

  command -v gcloud  >/dev/null 2>&1 || { echo >&2 "gcloud is required please follow: https://cloud.google.com/sdk/downloads"; exit 1; }
  command -v kubectl >/dev/null 2>&1 || { echo >&2 "kubectl is required please follow: https://kubernetes.io/docs/tasks/tools/install-kubectl"; exit 1; }
  command -v helm    >/dev/null 2>&1 || { echo >&2 "helm is required please follow: https://github.com/kubernetes/helm/blob/master/docs/install.md"; exit 1; }

  gcloud container clusters list >/dev/null 2>&1 || { echo >&2 "Gcloud seems to be configured incorrectly or authentication is unsuccessfull"; exit 1; }

}

function cluster_admin_password_gke(){
  gcloud container clusters describe $CLUSTER_NAME --zone $ZONE --project $PROJECT --format='value(masterAuth.password)';
}
