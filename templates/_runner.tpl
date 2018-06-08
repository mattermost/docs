{{/*
Return the gitlab-runner registration token secret name
*/}}
{{- define "gitlab.gitlab-runner.registrationToken.secret" -}}
{{- default (printf "%s-gitlab-runner-secret" .Release.Name) .Values.global.runner.registrationToken.secret | quote -}}
{{- end -}}

{{/*
Return the gitlab-runner registration token secret key
*/}}
{{- define "gitlab.gitlab-runner.registrationToken.key" -}}
{{- coalesce .Values.global.runner.registrationToken.key "runner-registration-token" | quote -}}
{{- end -}}
