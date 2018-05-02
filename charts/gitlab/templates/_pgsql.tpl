{{/* ######### PostgreSQL related templates */}}

{{/*
Return the db hostname
If the postgresql host is provided, it will use that, otherwise it will fallback
to the service name
*/}}
{{- define "gitlab.psql.host" -}}
{{- if or .Values.psql.host .Values.global.psql.host -}}
{{- coalesce .Values.psql.host .Values.global.psql.host | quote -}}
{{- else -}}
{{- $name := default "omnibus" .Values.psql.serviceName -}}
{{- printf "%s-%s" .Release.Name $name -}}
{{- end -}}
{{- end -}}

{{/*
Return the db database name
*/}}
{{- define "gitlab.psql.database" -}}
{{- coalesce .Values.psql.database .Values.global.psql.database "gitlabhq_production" | quote -}}
{{- end -}}

{{/*
Return the db username
If the postgresql username is provided, it will use that, otherwise it will fallback
to "gitlab" default
*/}}
{{- define "gitlab.psql.username" -}}
{{- coalesce .Values.psql.username .Values.global.psql.username "gitlab" -}}
{{- end -}}

{{/*
Return the db port
If the postgresql port is provided, it will use that, otherwise it will fallback
to 5432 default
*/}}
{{- define "gitlab.psql.port" -}}
{{- coalesce .Values.psql.port .Values.global.psql.port 5432 -}}
{{- end -}}
