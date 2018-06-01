{{/*
Returns the minio hostname.
If the hostname is set in `global.hosts.minio.name`, that will be returned,
otherwise the hostname will be assembed using `minio` as the prefix, and the `assembleHost` function.
*/}}
{{- define "gitlab.task-runner.minioHost" -}}
{{- coalesce .Values.global.hosts.minio.name (include "assembleHost"  (dict "name" "minio" "context" . )) -}}
{{- end -}}

{{/*
Returns the minio Url, ex: `http://minio.example.local`
If `global.hosts.https` or `global.hosts.minio.https` is true, it uses https, otherwise http.
Calls into the `minioHost` function for the hostname part of the url.
*/}}
{{- define "gitlab.task-runner.minioUrl" -}}
{{- if or .Values.global.hosts.https .Values.global.hosts.minio.https -}}
{{-   printf "https://%s" (include "gitlab.task-runner.minioHost" .) -}}
{{- else -}}
{{-   printf "http://%s" (include "gitlab.task-runner.minioHost" .) -}}
{{- end -}}
{{- end -}}
