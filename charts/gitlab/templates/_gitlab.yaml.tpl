{{- define "gitlab.appConfig.gitaly" -}}
gitaly:
  client_path: /home/git/gitaly/bin
  token: "<%= File.read('/etc/gitlab/gitaly/gitaly_token') %>"
{{- end -}}

{{- define "gitlab.appConfig.repositories" -}}
repositories:
  storages: # You must have at least a `default` storage path.
{{ include "gitlab.gitaly.storages" . | indent 4 }}
{{- end -}}

{{- define "gitlab.configYaml.incoming_email" -}}
incoming_email:
  enabled: {{ eq .incomingEmail.enabled true }}
  address: {{ .incomingEmail.address | quote }}
{{- end -}}
