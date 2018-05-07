{{/* ######### Gitaly related templates */}}

{{/*
Return the gitaly hostname
If the gitaly host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "gitlab.gitaly.host" -}}
{{- if .Values.gitaly.host -}}
{{- .Values.gitaly.host -}}
{{- else -}}
{{- $podName := printf "%s-gitaly-0" .Release.Name -}}
{{- $name := default "gitaly" .Values.gitaly.serviceName -}}
{{- printf "%s.%s-%s" $podName .Release.Name $name -}}
{{- end -}}
{{- end -}}
