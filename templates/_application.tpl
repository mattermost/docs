{{- define "gitlab.application.labels" -}}
app.kubernetes.io/name: {{ .Values.global.application.name }}
{{- end -}}

{{- define "gitlab.standardLabels" -}}
app: {{ template "name" . }}
chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
release: {{ .Release.Name }}
heritage: {{ .Release.Service }}
{{ if .Values.global.application.name -}}
{{ include "gitlab.application.labels" . }}
{{- end -}}
{{- end -}}

{{- define "gitlab.immutableLabels" -}}
app: {{ template "name" . }}
chart: {{ .Chart.Name }}
release: {{ .Release.Name }}
heritage: {{ .Release.Service }}
{{ if .Values.global.application.name -}}
{{ include "gitlab.application.labels" . }}
{{- end -}}
{{- end -}}
