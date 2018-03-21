{{/* vim: set filetype=mustache: */}}

{{/*
Return the registry authEndpoint
Defaults to the globally set gitlabHostname if an authEndpoint hasn't been provided
to the chart
*/}}
{{- define "registry.authEndpoint" -}}
{{- if .Values.authEndpoint -}}
{{- .Values.authEndpoint -}}
{{- else -}}
{{- template "gitlabUrl" . -}}
{{- end -}}
{{- end -}}

{{/*
Returns the hostname.
If the hostname is set in `global.hosts.registry.name`, that will be returned,
otherwise the hostname will be assembed using `minio` as the prefix, and the `assembleHost` function.
*/}}
{{- define "registryHost" -}}
{{- coalesce .Values.global.hosts.gitlab.name (include "assembleHost"  (dict "name" "registry" "context" . )) -}}
{{- end -}}

{{/*
Returns the secret name for the Secret containing the TLS certificate and key.
Uses `ingress.tls.secretName` first and falls back to `global.ingress.tls.secretName`
if there is a shared tls secret for all ingresses.
*/}}
{{- define "registryTLSSecret" -}}
{{- $defaultName := (dict "secretName" "") -}}
{{- if .Values.global.ingress.configureCertmanager -}}
{{- $_ := set $defaultName "secretName" (printf "%s-registry-tls" .Release.Name) -}}
{{- end -}}
{{- pluck "secretName" .Values.ingress.tls .Values.global.ingress.tls $defaultName | first -}}
{{- end -}}

{{/*
Returns the registry Url, ex: `http://registry.example.local`
If `global.hosts.https` or `global.hosts.registry.https` is true, it uses https, otherwise http.
Calls into the `registryHost` function for the hostname part of the url.
*/}}
{{- define "registryUrl" -}}
{{- if or .Values.global.hosts.https .Values.global.hosts.registry.https -}}
{{-   printf "https://%s" (include "registryHost" .) -}}
{{- else -}}
{{-   printf "http://%s" (include "registryHost" .) -}}
{{- end -}}
{{- end -}}

{{/*
Returns the minio hostname.
If the hostname is set in `global.hosts.minio.name`, that will be returned,
otherwise the hostname will be assembed using `minio` as the prefix, and the `assembleHost` function.
*/}}
{{- define "minioHost" -}}
{{- coalesce .Values.global.hosts.minio.name (include "assembleHost"  (dict "name" "minio" "context" . )) -}}
{{- end -}}

{{/*
Returns the minio Url, ex: `http://minio.example.local`
If `global.hosts.https` or `global.hosts.minio.https` is true, it uses https, otherwise http.
Calls into the `minioHost` function for the hostname part of the url.
*/}}
{{- define "minioUrl" -}}
{{- if or .Values.global.hosts.https .Values.global.hosts.minio.https -}}
{{-   printf "https://%s" (include "minioHost" .) -}}
{{- else -}}
{{-   printf "http://%s" (include "minioHost" .) -}}
{{- end -}}
{{- end -}}
