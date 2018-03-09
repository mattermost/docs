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
Returns the GitLab hostname.
If the hostname is set in `global.hosts.gitlab.name`, that will be returned,
otherwise the hostname will be assembed using `gitlab` as the prefix, and the `assembleHost` function.
*/}}
{{- define "gitlabHost" -}}
{{- coalesce .Values.global.hosts.gitlab.name (include "assembleHost"  (dict "name" "gitlab" "context" . )) -}}
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
{{- coalesce .Values.global.hosts.registry.name (include "assembleHost"  (dict "name" "registry" "context" . )) -}}
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

{{/*
Returns the secret name for the Secret containing the registry TLS certificate and key.
*/}}
{{- define "registryTLSSecret" -}}
{{- $fullname := include "fullname" . -}}
{{- if coalesce .Values.ingress.acme .Values.global.ingress.acme | default false -}}
{{- printf "%s-acme-tls" $fullname -}}
{{- else -}}
{{- default "" (coalesce .Values.ingress.tls.secretName .Values.global.ingress.tls.secretName) -}}
{{- end -}}
{{- end -}}
