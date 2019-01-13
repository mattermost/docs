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

{{- define "gitlab.appConfig.rackAttack" -}}
rack_attack:
  git_basic_auth:
    {{- if .Values.rack_attack.git_basic_auth.enabled }}
  {{ toYaml .Values.rack_attack.git_basic_auth | indent 2 }}
    {{- end }}
{{- end -}}
