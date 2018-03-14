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
{{- define "sidekiq.psql.host" -}}
{{- if or .Values.psql.host .Values.global.psql.host -}}
{{- .Values.global.psql.host | default .Values.psql.host | quote -}}
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
{{- define "sidekiq.psql.username" -}}
{{- if or .Values.psql.username .Values.global.psql.username -}}
{{- .Values.global.psql.username | default .Values.psql.username | quote -}}
{{- else -}}
gitlab
{{- end -}}
{{- end -}}

{{/*
Return the db port
If the postgresql port is provided, it will use that, otherwise it will fallback
to 5432 default
*/}}
{{- define "sidekiq.psql.port" -}}
{{- if or .Values.psql.port .Values.global.psql.port -}}
{{- .Values.global.psql.port | default .Values.psql.port -}}
{{- else -}}
5432
{{- end -}}
{{- end -}}

{{/*
Return the redis hostname
If the postgresql host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "sidekiq.redis.host" -}}
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
{{- define "sidekiq.gitaly.host" -}}
{{- if .Values.gitaly.host -}}
{{- .Values.gitaly.host -}}
{{- else -}}
{{- $name := default "gitaly" .Values.gitaly.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}
