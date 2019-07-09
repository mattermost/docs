{{/*
Return list of Sidekiq queue names
*/}}
{{- define "sidekiq.queueNames" -}}
{{- $fullName := include "fullname" . -}}
{{- range .Values.pods -}}
{{- printf "%s-%s " $fullName .name | trunc 63 -}}
{{- end -}}
{{- end -}}
