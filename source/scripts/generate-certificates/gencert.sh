#!/bin/bash

umask 007

FILE_NAME="${CRT_FILENAME:-"mattermost-x509"}"
CERT="${FILE_NAME}.crt"
KEY="${FILE_NAME}.key"
CSR="${FILE_NAME}.csr"

# generate key
openssl genrsa -out $KEY 4096

if [ $? -ne 0 ]; then
    echo "Error generating key"
    exit
fi

# generate certificate signing request
openssl req \
    -new \
    -key $KEY \
    -out $CSR \
    -subj "/C=${CRT_C:-"US"}/L=${CRT_L:-"Palo Alto"}/O=${CRT_O:-"Mattermost"}/OU=${CRT_OU:-"DevOps"}/CN=${CRT_CN:-"base.example.com"}"

if [ $? -ne 0 ]; then
    echo "Error generating certificate signing request (csr)"
    exit
fi

# generate self-signed certificate
openssl x509 \
    -req \
    -days 3650 \
    -in $CSR \
    -signkey $KEY \
    -sha256 \
    -out $CERT \
    -extfile <(echo -e "basicConstraints=critical,CA:true,pathlen:0\nsubjectAltName=${CRT_SAN:-"DNS.1:logs.example.com,DNS.2:metrics.example.com,IP.1:192.168.0.1,IP.2:127.0.0.1"}")

if [ $? -ne 0 ]; then
    echo "Error generating self-signed certificate"
    exit
fi

rm $CSR
chmod 600 $CERT

echo -e "\nSuccess! $KEY and $CERT generated."
