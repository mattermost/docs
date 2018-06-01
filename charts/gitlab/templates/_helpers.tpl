{{/* vim: set filetype=mustache: */}}

{{/*
Return the version tag used to fetch the GitLab images
Defaults to using the information from the chart appVersion field, but can be
overridden using the global.gitlabVersion field in values.
*/}}
{{- define "gitlab.versionTag" -}}
{{- template "gitlab.parseAppVersion" (coalesce .Values.global.gitlabVersion .Chart.AppVersion) -}}
{{- end -}}

{{/*
Returns a image tag from the passed in app version or branchname

If the version is 'master' we use the 'latest' image tag.
Else if the version is a semver version, we use the 'vx.x.x' image tag
Else we just use the version passed as the image tag
*/}}
{{- define "gitlab.parseAppVersion" -}}
{{- $appVersion := coalesce . "master" -}}
{{- if eq $appVersion "master" -}}
latest
{{- else if regexMatch "^\\d+\\.\\d+\\.\\d+(-rc\\d+)?(-pre)?$" $appVersion -}}
{{- printf "v%s" $appVersion -}}
{{- else -}}
{{- $appVersion -}}
{{- end -}}
{{- end -}}
