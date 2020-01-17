{{- define "gitlab.appConfig.gitaly" -}}
gitaly:
  client_path: /home/git/gitaly/bin
  token: "<%= File.read('/etc/gitlab/gitaly/gitaly_token').strip.dump[1..-2] %>"
{{- end -}}

{{- define "gitlab.appConfig.repositories" -}}
repositories:
  storages: # You must have at least a `default` storage path.
{{ include "gitlab.gitaly.storages" . | indent 4 }}
{{- end -}}


{{- define "gitlab.appConfig.incoming_email" -}}
incoming_email:
  enabled: {{ eq .incomingEmail.enabled true }}
  address: {{ .incomingEmail.address | quote }}
{{- end -}}

{{- define "gitlab.appConfig.shell" -}}
gitlab_shell:
  path: /home/git/gitlab-shell/
  hooks_path: /home/git/gitlab-shell/hooks/
  upload_pack: true
  receive_pack: true
{{- end -}}

{{- define "gitlab.appConfig.shell.ssh_port" -}}
ssh_port: {{ include "gitlab.shell.port" . | int }}
{{- end -}}

{{- define "gitlab.appConfig.shell.secret_file" -}}
secret_file: /etc/gitlab/shell/.gitlab_shell_secret
{{- end -}}

{{- define "gitlab.appConfig.extra" -}}
extra:
  {{ if .extra.googleAnalyticsId }}
  google_analytics_id: {{ .extra.googleAnalyticsId | quote }}
  {{- end }}
  {{ if .extra.piwikUrl }}
  piwik_url: {{ .extra.piwikUrl | quote }}
  {{- end }}
  {{ if .extra.piwikSiteId }}
  piwik_site_id: {{ .extra.piwikSiteId | quote }}
  {{- end }}
{{- end -}}

{{- define "gitlab.appConfig.rackAttack" -}}
rack_attack:
  git_basic_auth:
    {{- if .Values.rack_attack.git_basic_auth.enabled }}
  {{ toYaml .Values.rack_attack.git_basic_auth | indent 2 }}
    {{- end }}
{{- end -}}

{{- define "gitlab.appConfig.cronJobs" -}}
{{- if .cron_jobs }}
cron_jobs:
{{ toYaml .cron_jobs | indent 2 }}
{{- end }}
{{- end }}

{{- define "gitlab.appConfig.maxRequestDurationSeconds" -}}
{{/*
    Unless explicitly provided, we need to set maxRequestDurationSeconds to 95% of the
    workerTimeout value specified for unicorn (and use its ceiling value).
    However, sprig's `mul` function does not work with floats, so a
    multiplication with `0.95` is not possible. To workaround this, we do the
    following
    1. Scale up the value to the order of 10000 by multiplying it
    with (95 * 100).
    2. Divide the scaled up value by 10000, and the result will be an integer.
    3. If a reminder was present during the division (this is checked using
       modular division), we increment the result by 1. This does the function
       of `ceil` in Ruby.
    4. For example, if unicorn's timeout is the default value of 60, the result
       we need is 57. The various values in this workaround will be
       (i)   $workerTimeout = 60
       (ii)  $scaledResult = 570000
       (iii) $reminder = 0
       (iv)  $result = 57
    5. Another example, if unicorn's timeout is 61, the result we need is
       58 (ceiling of 0.95 * 61 = 57.95). The various values in this workaround
       will be
       (i)   $workerTimeout = 61
       (ii)  $scaledResult = 579500
       (iii) $reminder = 9500
       (iv)  $result = 57
       (v)   $result = 58 (because there was a remainder, result got incremented)
*/}}
{{- $workerTimeout := $.Values.global.unicorn.workerTimeout }}
{{- $scaledResult := mul $workerTimeout 100 95 }}
{{- $remainder := mod $scaledResult 10000 }}
{{- $doCeil := gt $remainder 0 }}
{{- $result := div $scaledResult 10000 }}
{{- if $doCeil }}
{{-   $result = add1 $result }}
{{- end }}
{{- $result }}
{{- end }}
{{/* END gitlab.appConfig.maxRequestDurationSeconds */}}
