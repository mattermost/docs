{{/* vim: set filetype=mustache: */}}
{{/*
Return the db hostname
If the postgresql host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "unicorn.psql.host" -}}
{{- if or .Values.psql.host .Values.global.psql.host -}}
{{- coalesce .Values.psql.host .Values.global.psql.host | quote -}}
{{- else -}}
{{- $name := default "omnibus" .Values.psql.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}

{{/*
Return the db username
If the postgresql username is provided, it will use that, otherwise it will fallback
to "gitlab" default
*/}}
{{- define "unicorn.psql.username" -}}
{{- coalesce .Values.psql.username .Values.global.psql.username "gitlab" -}}
{{- end -}}

{{/*
Return the db port
If the postgresql port is provided, it will use that, otherwise it will fallback
to 5432 default
*/}}
{{- define "unicorn.psql.port" -}}
{{- coalesce .Values.psql.port .Values.global.psql.port 5432 -}}
{{- end -}}

{{/*
Return the redis hostname
If the redis host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "unicorn.redis.host" -}}
{{- if .Values.redis.host -}}
{{- .Values.redis.host -}}
{{- else -}}
{{- $name := default "redis" .Values.redis.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}

{{/*
Return the gitaly hostname
If the gitaly host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "unicorn.gitaly.host" -}}
{{- if .Values.gitaly.host -}}
{{- .Values.gitaly.host -}}
{{- else -}}
{{- $name := default "gitaly" .Values.gitaly.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}

{{/*
Return the registry api hostname
If the registry api host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "unicorn.registry.api.host" -}}
{{-   if .Values.registry.api.host -}}
{{-     .Values.registry.api.host -}}
{{-   else -}}
{{-     $name := default .Values.global.hosts.registry.serviceName .Values.registry.api.serviceName -}}
{{-     printf "%s-%s" .Release.Name $name -}}
{{-   end -}}
{{- end -}}

{{/*
Return the registry external hostname
If the chart registry host is provided, it will use that, otherwise it will fallback
to the global registry host name.
*/}}
{{- define "unicorn.registry.host" -}}
{{-   if .Values.registry.host -}}
{{-     .Values.registry.host -}}
{{-   else -}}
{{-     template "registryHost" . -}}
{{-   end -}}
{{- end -}}
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
{{- coalesce .Values.ingress.hostname .Values.global.hosts.gitlab.name (include "assembleHost"  (dict "name" "gitlab" "context" . )) -}}
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
Return the minio service endpoint
*/}}
{{- define "unicorn.minio.endpoint" -}}
{{- $name := default "minio-svc" .Values.minio.serviceName -}}
{{- $port := default 9000 .Values.minio.port | int -}}
{{- printf "http://%s-%s:%d" .Release.Name $name $port -}}
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
{{- if (pluck "configureExternaldns" .Values.ingress .Values.global.ingress (dict "configureExternaldns" false) | first) -}}
{{- printf "external-dns.alpha.kubernetes.io/hostname: %s" (include "gitlabHost" . | quote) -}}
{{- end -}}
{{- end -}}
