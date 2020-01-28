{{/* ######### workhorse templates */}}

{{/*
Return the workhorse hostname
If the workhorse host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "gitlab.workhorse.host" -}}
{{- if .Values.workhorse.host -}}
{{- .Values.workhorse.host -}}
{{- else -}}
{{- $name := default "unicorn" .Values.workhorse.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}

{{- define "gitlab.workhorse.port" -}}
{{- if .Values.workhorse.port -}}
{{- .Values.workhorse.port -}}
{{- else -}}
{{- $port:= default "8181" .Values.workhorse.port -}}
{{- $port -}}
{{- end -}}
{{- end -}}
