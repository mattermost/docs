{{/* ######## Geo related tempaltes */}}

{{/*
Returns parts for a Gitlab configuration to setup a mutual TLS connection
with the Geo PostgreSQL database.
*/}}
{{- define "gitlab.geo.psql.ssl.config" -}}
{{- if .Values.global.geo.psql.ssl }}
sslmode: verify-ca
sslrootcert: '/etc/gitlab/postgres/ssl/geo-server-ca.pem'
sslcert: '/etc/gitlab/postgres/ssl/geo-client-certificate.pem'
sslkey: '/etc/gitlab/postgres/ssl/geo-client-key.pem'
{{- end -}}
{{- end -}}

{{/*
Returns volume definition of a secret containing information required for
a mutual TLS connection.
*/}}
{{- define "gitlab.geo.psql.ssl.volume" -}}
{{- if .Values.global.geo.psql.ssl }}
- name: geo-postgresql-ssl-secrets
  projected:
    defaultMode: 400
    sources:
    - secret:
        name: {{ .Values.global.geo.psql.ssl.secret | required "Missing required secret containing SQL SSL certificates and keys. Make sure to set `global.geo.psql.ssl.secret`" }}
        items:
          - key: {{ .Values.global.geo.psql.ssl.serverCA | required "Missing required key name of SQL server certificate. Make sure to set `global.geo.psql.ssl.serverCA`" }}
            path: geo-server-ca.pem
          - key: {{ .Values.global.geo.psql.ssl.clientCertificate | required "Missing required key name of SQL client certificate. Make sure to set `global.geo.psql.ssl.clientCertificate`" }}
            path: geo-client-certificate.pem
          - key: {{ .Values.global.geo.psql.ssl.clientKey | required "Missing required key name of SQL client key file. Make sure to set `global.geo.psql.ssl.clientKey`" }}
            path: geo-client-key.pem
{{- end -}}
{{- end -}}

{{/*
Returns mount definition for the volume mount definition above.
*/}}
{{- define "gitlab.geo.psql.ssl.volumeMount" -}}
{{- if .Values.global.geo.psql.ssl }}
- name: geo-postgresql-ssl-secrets
  mountPath: '/etc/postgresql/geo/ssl/'
  readOnly: true
{{- end -}}
{{- end -}}

{{/*
Returns a shell script snippet, which extends the script of a configure
container to copy the mutual TLS files to the proper location. Further
it sets the permissions correctly.
*/}}
{{- define "gitlab.geo.psql.ssl.initScript" -}}
{{- if .Values.global.geo.psql.ssl }}
if [ -d /etc/postgresql/geo/ssl ]; then
  mkdir -p /${secret_dir}/postgres/ssl
  cp -v -r -L /etc/postgresql/geo/ssl/* /${secret_dir}/postgres/ssl/
  chmod 600 /${secret_dir}/postgres/ssl/*
  chmod 700 /${secret_dir}/postgres/ssl
fi
{{- end -}}
{{- end -}}
