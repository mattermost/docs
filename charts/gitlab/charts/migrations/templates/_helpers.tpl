{{/* vim: set filetype=mustache: */}}

{{/*
Validates initialRootPassword making sure it is >= 6 characters
Returns an empty string if invalid password else password
*/}}
{{- define "migrations.validate_root_password" -}}
{{ $length := len .Values.initialRootPassword }}
{{- if ge $length 6 -}}
{{ .Values.initialRootPassword }}
{{- end -}}
{{- end -}}

{{/*
Create a default fully qualified job name.
Due to the job only being allowed to run once, we add the chart revision so helm
upgrades don't cause errors trying to create the already ran job.
Due to the helm delete not cleaning up these jobs, we add a randome value to
reduce collision
*/}}
{{- define "migrations.jobname" -}}
{{- $name := include "fullname" . | trunc 55 | trimSuffix "-" -}}
{{- printf "%s.%d" $name .Release.Revision | trunc 63 | trimSuffix "-" -}}
{{- end -}}
