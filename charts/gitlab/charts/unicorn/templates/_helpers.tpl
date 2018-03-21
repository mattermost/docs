{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

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
  A helper function for assembling a hostname using the base domain specified in `global.hosts.domain`
  Takes a `Map/Dictonary` as an argument. Where key `name` is the domain to build, and `context` should be a
  reference to the chart's $ object.
  eg: `template "assembleHost" (dict "name" "gitlab" "context" .)`

  The hostname will be the combined name with the domain. eg: If domain is `example.local`, it will produce `gitlab.example.local`
  Additionally if `global.hosts.hostSuffix` is set, it will append a hyphen, then the suffix to the name:
  eg: If hostSuffix is `beta` it will produce `gitlab-beta.example.local`
*/}}
{{- define "assembleHost" -}}
{{- $name := .name -}}
{{- $context := .context -}}
{{- $result := dict -}}
{{- if $context.Values.global.hosts.domain -}}
{{-   $_ := set $result "domainHost" (printf ".%s" $context.Values.global.hosts.domain) -}}
{{-   if $context.Values.global.hosts.hostSuffix -}}
{{-     $_ := set $result "domainHost" (printf "-%s%s" $context.Values.global.hosts.hostSuffix $result.domainHost) -}}
{{-   end -}}
{{-   $_ := set $result "domainHost" (printf "%s%s" $name $result.domainHost) -}}
{{- end -}}
{{- $result.domainHost -}}
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
Returns the Registry hostname.
If the hostname is set in `global.hosts.registry.name`, that will be returned,
otherwise the hostname will be assembed using `registry` as the prefix, and the `assembleHost` function.
*/}}
{{- define "registryHost" -}}
{{- coalesce .Values.registry.host .Values.global.hosts.registry.name (include "assembleHost"  (dict "name" "registry" "context" . )) -}}
{{- end -}}

{{/*
Returns the hostname.
If the hostname is set in `global.hosts.gitlab.name`, that will be returned,
otherwise the hostname will be assembed using `gitlab` as the prefix, and the `assembleHost` function.
*/}}
{{- define "gitlabHost" -}}
{{- coalesce .Values.global.hosts.gitlab.name (include "assembleHost"  (dict "name" "gitlab" "context" . )) -}}
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
Returns the secret name for the Secret containing the TLS certificate and key.
Uses `ingress.tls.secretName` first and falls back to `global.ingress.tls.secretName`
if there is a shared tls secret for all ingresses.
*/}}
{{- define "gitlabTLSSecret" -}}
{{- $defaultName := (dict "secretName" "") -}}
{{- if .Values.global.ingress.configureCertmanager -}}
{{- $_ := set $defaultName "secretName" (printf "%s-gitlab-tls" .Release.Name) -}}
{{- end -}}
{{- pluck "secretName" .Values.ingress.tls .Values.global.ingress.tls $defaultName | first -}}
{{- end -}}
