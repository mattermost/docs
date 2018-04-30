#!/bin/bash
set -e ;

issuer_file=$1
namespace={{ .Release.Namespace }}

set +e ; # The CRD check is allowed to fail
echo "Waiting for the CRD to exist: issuers.certmanager.k8s.io " ;
STATUS=1 ;
until [ $STATUS -eq 0 ] ;
do
  CMD=$(kubectl --namespace=$namespace get crd issuers.certmanager.k8s.io > /dev/null 2>&1)
  STATUS=$?
  sleep 1;
done ;
set -e ; # reset `e` as active

echo "Create the certmanager issuer" ;
kubectl --namespace=$namespace apply -f ${issuer_file:=issuer.yml}
