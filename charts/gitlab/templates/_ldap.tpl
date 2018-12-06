{{- define "gitlab.appConfig.ldap.configuration" -}}
{{- if not .Values.global.appConfig.ldap.servers -}}
ldap:
  enabled: false
{{- else -}}
ldap:
  enabled: true
  servers:
    {{- toYaml .Values.global.appConfig.ldap.servers | nindent 4 }}
{{- end -}}
{{- end -}}{{/* "gitlab.appConfig.ldap.configuration" */}}
