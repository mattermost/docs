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
Return the workhorse auth backend
If the backend host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "workhorse.auth_backend" -}}
{{- $port := coalesce .Values.workhorse.auth_backend.port .Values.service.ports.unicorn 8080 | toString -}}
{{- if .Values.workhorse.auth_backend.host -}}
{{- printf "%s:%s" .Values.workhorse.auth_backend.host $port -}}
{{- else -}}
{{- $name := default "omnibus" .Values.workhorse.auth_backend.serviceName -}}
{{- printf "http://%s-%s:%s" .Release.Name $name $port -}}
{{- end -}}
{{- end -}}

{{/*
Return the unicorn internal_api host
If host is specified in the values it will use that.
Else the serviceName will be used
*/}}
{{- define "unicorn.internal_api_host" -}}
{{- if .Values.unicorn.internal_api.host -}}
{{- .Values.unicorn.internal_api.host -}}
{{- else if .Values.unicorn.internal_api.serviceName -}}
{{- $name := default "omnibus" .Values.unicorn.internal_api.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}
