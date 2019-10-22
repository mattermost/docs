{{/* ######### Gitaly related templates */}}

{{/*
Return gitaly host for internal statefulsets
*/}}
{{- define "gitlab.gitaly.storage.internal" -}}
{{- $releaseName := .Release.Name -}}
{{- $name := coalesce .Values.gitaly.serviceName .Values.global.gitaly.serviceName "gitaly" -}}
{{- range $i, $storage := .Values.global.gitaly.internal.names -}}
{{- printf "%s:\n" $storage -}}
{{- printf  "path: /var/opt/gitlab/repo\n" | indent 2 -}}
{{- $podName := printf "%s-gitaly-%d" $releaseName $i -}}
{{- if $.Values.global.gitaly.tls.enabled }}
{{- printf "gitaly_address: tls://%s.%s-%s.%s:%d\n" $podName $releaseName $name $.Release.Namespace 8076 -}}
{{- else }}
{{- printf "gitaly_address: tcp://%s.%s-%s.%s:%d\n" $podName $releaseName $name $.Release.Namespace 8075 -}}
{{- end -}}
{{- end -}}
{{- end -}}


{{/*
Return gitaly storage for external hosts
*/}}
{{- define "gitlab.gitaly.storage.external" -}}
{{- range $i, $storage := .Values.global.gitaly.external -}}
{{- printf "%s:\n" $storage.name -}}
{{- printf  "path: /var/opt/gitlab/repo\n" | indent 2 -}}
{{- if $.Values.global.gitaly.tls.enabled }}
{{- printf "gitaly_address: tls://%s:%d\n" $storage.hostname (default 8076 $storage.port | int64) -}}
{{- else }}
{{- printf "gitaly_address: tcp://%s:%d\n" $storage.hostname (default 8075 $storage.port | int64) -}}
{{- end -}}
{{- end -}}
{{- end -}}


{{/*
Return the gitaly storages list
*/}}
{{- define "gitlab.gitaly.storages" -}}
{{- if .Values.global.gitaly.host -}}
default:
  path: /var/opt/gitlab/repo
  {{- if $.Values.global.gitaly.tls.enabled }}
  gitaly_address: {{ printf "tls://%s:%d" .Values.global.gitaly.host (default 8076 .Values.global.gitaly.port | int64 ) }}
  {{- else }}
  gitaly_address: {{ printf "tcp://%s:%d" .Values.global.gitaly.host (default 8075 .Values.global.gitaly.port | int64 ) }}
  {{- end -}}
{{- else -}}
{{- if .Values.global.gitaly.external -}}
{{ template "gitlab.gitaly.storage.external" . }}
{{- end -}}
{{- if .Values.global.gitaly.internal.names -}}
{{ template "gitlab.gitaly.storage.internal" . }}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Return the number of replicas set for Gitaly statefulset
*/}}
{{- define "gitlab.gitaly.replicas" -}}
{{- if .Values.global.gitaly.host }} 0 {{- else }} {{ len .Values.global.gitaly.internal.names }} {{- end }}
{{- end -}}
