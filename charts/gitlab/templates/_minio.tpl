{{/* ######### Minio related templates */}}

{{/*
Return the minio service endpoint
*/}}
{{- define "gitlab.minio.endpoint" -}}
{{- $name := default "minio-svc" .Values.minio.serviceName -}}
{{- $port := default 9000 .Values.minio.port | int -}}
{{- printf "http://%s-%s:%d" .Release.Name $name $port -}}
{{- end -}}
