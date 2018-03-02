{{/* vim: set filetype=mustache: */}}
{{/*
Returns the GitLab Url, ex: `http://gitlab.example.local`
If `global.hosts.https` or `global.hosts.gitlab.https` is true, it uses https, otherwise http.
Calls into the `gitlabHost` function for the hostname part of the url.
*/}}
{{- define "gitlabUrl" -}}
{{- if or .Values.global.hosts.https .Values.global.hosts.gitlab.https -}}
{{-   printf "https://%s" (include "gitlabHost" .) -}}
{{- else -}}
{{-   printf "http://%s" (include "gitlabHost" .) -}}
{{- end -}}
{{- end -}}

{{/*
Returns the hostname.
If the hostname is set in `global.hosts.gitlab.name`, that will be returned,
otherwise the hostname will be assembed using `gitlab` as the prefix, and the `assembleHost` function.
*/}}
{{- define "gitlabHost" -}}
{{- coalesce .Values.ingress.hostname (include "assembleHost"  (dict "name" "gitlab" "context" . )) -}}
{{- end -}}

{{/*
Returns the secret name for the Secret containing the gitlab TLS certificate and key.
Uses `ingress.tls.secretName` first and falls back to `global.ingress.tls.secretName`
if there is a shared tls secret for all ingresses.
*/}}
{{- define "gitlabTLSSecret" -}}
{{- pluck "secretName" .Values.ingress.tls .Values.global.ingress.tls (dict "secretName" (printf "%s-gitlab-tls" .Release.Name)) | first -}}
{{- end -}}

{{- define "gitlab.externaldns_annotations" -}}
{{- if (pluck "configure_externaldns" .Values.global.ingress .Values.ingress (dict "configure_externaldns" false) | first) -}}
{{- printf "external-dns.alpha.kubernetes.io/hostname: %s" (include "gitlabHost" . | quote) -}}
{{- end -}}
{{- end -}}
