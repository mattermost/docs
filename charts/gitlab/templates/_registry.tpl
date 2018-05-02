{{/* ######### Registry related templates */}}

{{/*
Returns the Registry hostname.
If the hostname is set in `global.hosts.registry.name`, that will be returned,
otherwise the hostname will be assembed using `registry` as the prefix, and the `assembleHost` function.
*/}}
{{- define "gitlab.registryHost" -}}
{{- coalesce .Values.registry.host .Values.global.hosts.registry.name (include "assembleHost"  (dict "name" "registry" "context" . )) -}}
{{- end -}}
