{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
  A helper function for assembling a hostname using the base domain specified in `global.hosts.domain`
  Takes a `Map/Dictonary` as an argument. Where key `name` is the domain to build, and `context` should be a
  reference to the chart's $ object.
  eg: `template "assembleHost" (dict "name" "minio" "context" .)`

  The hostname will be the combined name with the domain. eg: If domain is `example.local`, it will produce `minio.example.local`
  Additionally if `global.hosts.hostSuffix` is set, it will append a hyphen, then the suffix to the name:
  eg: If hostSuffix is `beta` it will produce `minio-beta.example.local`
*/}}
{{- define "assembleHost" -}}
{{- $name := .name -}}
{{- $context := .context -}}
{{- $result := dict -}}
{{- if $context.Values.global.hosts.domain -}}
{{-   $_ := set $result "domainHost" (printf ".%s" $context.Values.global.hosts.domain) -}}
{{-   if $context.Values.global.hosts.hostSuffix -}}
{{-     $_ := set $result "domainHost" (printf "-%s%s" $context.Values.global.hosts.hostSuffix $result.domainHost) -}}
{{-   end -}}
{{-   $_ := set $result "domainHost" (printf "%s%s" $name $result.domainHost) -}}
{{- end -}}
{{- $result.domainHost -}}
{{- end -}}

{{- define "gitlab.certmanager_annotations" -}}
{{- if (pluck "configureCertmanager" .Values.global.ingress .Values.ingress (dict "configureCertmanager" false) | first) -}}
certmanager.k8s.io/issuer: "{{ .Release.Name }}-issuer"
{{- end -}}
{{- end -}}

{{/*
  Generates smtp settings for ActionMailer to be used in unicorn and sidekiq
*/}}
{{- define "gitlab.smtp_settings" -}}
{{- if .Values.global.smtp.enabled -}}
Rails.application.config.action_mailer.delivery_method = :smtp

ActionMailer::Base.delivery_method = :smtp
ActionMailer::Base.smtp_settings = {
  address: {{ .Values.global.smtp.address | quote }},
  port: {{ .Values.global.smtp.port | int }},
  {{- if .Values.global.smtp.domain }}
  domain: {{ .Values.global.smtp.domain | quote }},
  {{- end }}
  {{ if has .Values.global.smtp.authentication (list "login" "plain" "cram_md5") }}
  authentication: :{{.Values.global.smtp.authentication}},
  user_name: {{ .Values.global.smtp.user_name | quote }},
  password: File.read("/etc/gitlab/smtp/smtp-password"),
  {{- end }}
  {{- if .Values.global.smtp.starttls_auto }}
  enable_starttls_auto: true,
  {{- else }}
  enable_starttls_auto: false,
  {{- end }}
  {{- if eq .Values.global.smtp.openssl_verify_mode "peer" }}
  openssl_verify_mode: 'peer'
  {{- else if eq .Values.global.smtp.openssl_verify_mode "none" }}
  openssl_verify_mode: 'none'
  {{- else if eq .Values.global.smtp.openssl_verify_mode "ssl/tls" }}
  openssl_verify_mode: :ssl/:tls
  {{- end }}
}
{{- end -}}
{{- end -}}

{{/* Default from address for emails based on domain */}}
{{- define "gitlab.email.from" -}}
{{ .Values.global.email.from | default (printf "gitlab@%s" .Values.global.hosts.domain ) | quote -}}
{{- end -}}

{{/* Default replyto address for emails based on domain */}}
{{- define "gitlab.email.reply_to" -}}
{{ .Values.global.email.reply_to | default (printf "noreply@%s" .Values.global.hosts.domain ) | quote -}}
{{- end -}}
