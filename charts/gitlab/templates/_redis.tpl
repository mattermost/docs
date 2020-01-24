{{/* ######### Redis related templates */}}

{{/*
Return the redis hostname
If the redis host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "gitlab.redis.host" -}}
{{-   if or .Values.redis.host .Values.global.redis.host -}}
{{-     coalesce .Values.redis.host .Values.global.redis.host -}}
{{-   else -}}
{{-     $name := default "redis" .Values.redis.serviceName -}}
{{-     printf "%s-%s-master" .Release.Name $name -}}
{{-   end -}}
{{- end -}}

{{/*
Return the redis port
If the redis port is provided, it will use that, otherwise it will fallback
to 6379 default
*/}}
{{- define "gitlab.redis.port" -}}
{{- coalesce .Values.redis.port .Values.global.redis.port 6379 -}}
{{- end -}}

{{/*
Return the redis scheme, or redis. Allowing people to use rediss clusters
*/}}
{{- define "gitlab.redis.scheme" -}}
{{- $valid := list "redis" "rediss" "tcp" -}}
{{- $name := coalesce .Values.redis.scheme .Values.global.redis.scheme "redis" -}}
{{- if has $name $valid -}}
{{ $name }}
{{- else -}}
{{ cat "Invalid redis scheme" $name | fail }}
{{- end -}}
{{- end -}}

{{/*
Return the redis url.
*/}}
{{- define "gitlab.redis.url" -}}
{{ template "gitlab.redis.scheme" . }}://{{- if .Values.global.redis.password.enabled -}}:<%= URI.escape(File.read("/etc/gitlab/redis/password").strip) %>@{{- end -}}{{ template "gitlab.redis.host" . }}:{{ template "gitlab.redis.port" . }}
{{- end -}}

{{/*
Build the structure describing sentinels
*/}}
{{- define "gitlab.redis.sentinels" -}}
sentinels:
{{- range $i, $entry := .Values.global.redis.sentinels }}
  - host: {{ $entry.host }}
    port: {{ default 26379 $entry.port }}
{{- end }}
{{- end -}}

{{- define "gitlab.redis.workhorse.sentinel-list" }}
{{- $sentinelList := list }}
{{- range $i, $entry := .Values.global.redis.sentinels }}
  {{- $sentinelList = append $sentinelList (quote (print "tcp://" (trim $entry.host) ":" ( default 26379 $entry.port | int ) ) ) }}
{{- end }}
{{- $sentinelList | join "," }}
{{- end -}}
