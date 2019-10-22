#!/bin/bash
#
# gitaly_statefulset_certificates.sh
#--------------------------------------
# Script to generate a certificate & key for Gitaly chart to serve TLS
# Generates `gitlay.crt` & `gitaly.key` in a temporary directory, and
# places them into the current working directory.
# After generation, create a TLS secret:
#   kubectl create secret tls gitaly-server-tls --cert=gitaly.crt --key=gitaly.key
# Then, configure the chart to use this:
#   global:
#     gitaly:
#       tls:
#         enabled: true
#         secretName: gitaly-server-tls
#--------------------------------------

VALID_DAYS=${VALID_DAYS-365}
CERT_NAME=${CERT_NAME-gitaly}
RELEASE_NAME=${RELEASE_NAME-gitlab}
NAMESPACE=${NAMESPACE-default}

WORKDIR=`pwd`
TEMP_DIR=$(mktemp -d)
pushd $TEMP_DIR || exit

GITALY="${RELEASE_NAME}-gitaly"
GITALY="${GITALY:0:63}"

(
cat <<SANDOC
[req_ext]
subjectAltName = @san

[san]
DNS.1 = *.${GITALY}.${NAMESPACE}

SANDOC
) > san.conf

openssl req -x509 -nodes -newkey rsa:4096 \
  -keyout "${CERT_NAME}.key" \
  -out "${CERT_NAME}.crt" \
  -days ${VALID_DAYS} \
  -subj '/CN=gitaly' \
  -reqexts req_ext -extensions req_ext \
  -config <(cat /etc/ssl/openssl.cnf san.conf )

mv ${CERT_NAME}.* $WORKDIR/

popd
rm -rf $TEMP_DIR
