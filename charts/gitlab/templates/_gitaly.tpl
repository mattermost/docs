{{/* ######### Gitaly related templates */}}

{{/*
Return the gitaly hostname
If the gitaly host is provided, it will use that, otherwise it will fallback
to the service name 'gitaly'. Preference is local, global, default.
*/}}
{{- define "gitlab.gitaly.host" -}}
{{- if or .Values.gitaly.host .Values.global.gitaly.host -}}
{{- coalesce .Values.gitaly.host .Values.global.gitaly.host -}}
{{- else -}}
{{- $podName := printf "%s-gitaly-0" .Release.Name -}}
{{- $name := coalesce .Values.gitaly.serviceName .Values.global.gitaly.serviceName "gitaly" -}}
{{- printf "%s.%s-%s" $podName .Release.Name $name -}}
{{- end -}}
{{- end -}}

{{/*
Return the gitaly port
Preference is local, global, default (`8075`)
*/}}
{{- define "gitlab.gitaly.port" -}}
{{- coalesce .Values.gitaly.port .Values.global.gitaly.port 8075 -}}
{{- end -}}

{{/*
Return the gitaly secret name
Preference is local, global, default (`gitaly-secret`)
*/}}
{{- define "gitlab.gitaly.authToken.secret" -}}
{{- coalesce .Values.gitaly.authToken.secret .Values.global.gitaly.authToken.secret "gitaly-secret" | quote -}}
{{- end -}}

{{/*
Return the gitaly secret name
Preference is local, global, default (`token`)
*/}}
{{- define "gitlab.gitaly.authToken.key" -}}
{{- coalesce .Values.gitaly.authToken.key .Values.global.gitaly.authToken.key "token" | quote -}}
{{- end -}}
