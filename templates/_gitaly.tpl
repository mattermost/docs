{{/* ######### Gitaly related templates */}}

{{/*
Return the gitaly secret name
Preference is local, global, default (`gitaly-secret`)
*/}}
{{- define "gitlab.gitaly.authToken.secret" -}}
{{- coalesce .Values.global.gitaly.authToken.secret (printf "%s-gitaly-secret" .Release.Name) | quote -}}
{{- end -}}

{{/*
Return the gitaly secret key
Preference is local, global, default (`token`)
*/}}
{{- define "gitlab.gitaly.authToken.key" -}}
{{- coalesce .Values.global.gitaly.authToken.key "token" | quote -}}
{{- end -}}

{{/*
Return the gitaly TLS secret name
*/}}
{{- define "gitlab.gitaly.tls.secret" -}}
{{- default (printf "%s-gitaly-tls" .Release.Name) .Values.global.gitaly.tls.secretName | quote -}}
{{- end -}}
