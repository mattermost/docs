#!/bin/bash

umask 007

certname="${CRT_FILENAME:-"mattermost-x509"}"
openssl x509 \
    -in <(
        openssl req \
            -days 3650 \
            -newkey rsa:4096 \
            -nodes \
            -keyout "${certname}.key" \
            -subj "/C=${CRT_C:-"US"}/L=${CRT_L:-"Palo Alto"}/O=${CRT_O:-"Mattermost"}/OU=${CRT_OU:-"DevOps"}/CN=${CRT_CN:-"base.example.com"}"
        ) \
    -req \
    -signkey "${certname}.key" \
    -sha256 \
    -days 3650 \
    -out "${certname}.crt" \
    -extfile <(echo -e "basicConstraints=critical,CA:true,pathlen:0\nsubjectAltName=${CRT_SAN:-"DNS.1:logs.example.com,DNS.2:metrics.example.com,IP.1:192.168.0.1,IP.2:127.0.0.1"}")

chmod 600 ${certname}.crt
