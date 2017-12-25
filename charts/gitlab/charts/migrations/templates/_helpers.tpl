{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "migrations.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "migrations.fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified job name.
Due to the job only being allowed to run once, we add the chart revision so helm
upgrades don't cause errors trying to create the already ran job.
Due to the helm delete not cleaning up these jobs, we add a randome value to
reduce collision
*/}}
{{- define "migrations.jobname" -}}
{{- $name := include "migrations.fullname" . | trunc 55 | trimSuffix "-" -}}
{{- $rand := randAlphaNum 3 | lower }}
{{- printf "%s.%d-%s" $name .Release.Revision $rand | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Return the db hostname
If the postgresql host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "migrations.psql.host" -}}
{{- if .Values.psql.host -}}
{{- .Values.psql.host | quote -}}
{{- else -}}
{{- $name := default "omnibus" .Values.psql.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}

{{/*
Return the redis hostname
If the redis host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "migrations.redis.host" -}}
{{- if .Values.redis.host -}}
{{- .Values.redis.host -}}
{{- else -}}
{{- $name := default "redis" .Values.redis.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}
