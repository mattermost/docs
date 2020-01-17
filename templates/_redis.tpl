{{/* ######### Redis related templates */}}

{{/*
Return the redis password secret name

This define is not currently used, but left in place for when the
a dynamic secret name can be specified to the Redis chart.
*/}}
{{- define "gitlab.redis.password.secret" -}}
{{- default (printf "%s-redis-secret" .Release.Name) .Values.global.redis.password.secret | quote -}}
{{- end -}}

{{/*
Return the redis password secret key
*/}}
{{- define "gitlab.redis.password.key" -}}
{{- coalesce .Values.global.redis.password.key "secret" | quote -}}
{{- end -}}
