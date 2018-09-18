{{/* vim: set filetype=mustache: */}}

{{/*
Returns the secret name for the Secret containing the TLS certificate and key.
Uses `ingress.tls.secretName` first and falls back to `global.ingress.tls.secretName`
if there is a shared tls secret for all ingresses.
*/}}
{{- define "unicorn.tlsSecret" -}}
{{- $defaultName := (dict "secretName" "") -}}
{{- if .Values.global.ingress.configureCertmanager -}}
{{- $_ := set $defaultName "secretName" (printf "%s-gitlab-tls" .Release.Name) -}}
{{- else -}}
{{- $_ := set $defaultName "secretName" (include "gitlab.wildcard-self-signed-cert-name" .) -}}
{{- end -}}
{{- pluck "secretName" .Values.ingress.tls .Values.global.ingress.tls $defaultName | first -}}
{{- end -}}

{{/*
Returns the workhorse image depending on the value of global.edition.

Used to switch the deployment from Enterprise Edition (default) to Community
Edition. If global.edition=ce, returns the Community Edition workhorse.image
value set in the Gitlab values.yaml. Otherwise returns .Values.workhorse.image.
*/}}
{{- define "workhorse.image" -}}
{{- if eq "ce" .Values.global.edition -}}
{{ index .Values "global" "communityEdition" .Chart.Name "workhorse" "image" }}
{{- else -}}
{{ .Values.workhorse.image }}
{{- end -}}
{{- end -}}
