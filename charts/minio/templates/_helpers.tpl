{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "minio.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "minio.fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Return the appropriate apiVersion for networkpolicy.
*/}}
{{- define "minio.networkPolicy.apiVersion" -}}
{{- if and (ge .Capabilities.KubeVersion.Minor "4") (le .Capabilities.KubeVersion.Minor "6") -}}
{{- print "extensions/v1beta1" -}}
{{- else if ge .Capabilities.KubeVersion.Minor "7" -}}
{{- print "networking.k8s.io/v1" -}}
{{- end -}}
{{- end -}}

{{/*
Create a default fully qualified job name for creating default buckets.
Due to the job only being allowed to run once, we add the chart revision so helm
upgrades don't cause errors trying to create the already ran job.
Due to the helm delete not cleaning up these jobs, we add a random value to
reduce collision
*/}}
{{- define "minio.createBucketsJobName" -}}
{{- $name := include "minio.fullname" . | trunc 40 | trimSuffix "-" -}}
{{- $rand := randAlphaNum 3 | lower }}
{{- printf "%s-create-buckets.%d-%s" $name .Release.Revision $rand -}}
{{- end -}}

{{/*
Returns the minio hostname.
If the hostname is set in `global.hosts.minio.name`, that will be returned,
otherwise the hostname will be assembed using `minio` as the prefix, and the `assembleHost` function.
*/}}
{{- define "minioHost" -}}
{{- coalesce .Values.global.hosts.minio.name (include "assembleHost"  (dict "name" "minio" "context" . )) -}}
{{- end -}}

{{/*
Returns the minio Url, ex: `http://minio.example.local`
If `global.hosts.https` or `global.hosts.minio.https` is true, it uses https, otherwise http.
Calls into the `minioHost` function for the hostname part of the url.
*/}}
{{- define "minioUrl" -}}
{{- if or .Values.global.hosts.https .Values.global.hosts.minio.https -}}
{{-   printf "https://%s" (include "minioHost" .) -}}
{{- else -}}
{{-   printf "http://%s" (include "minioHost" .) -}}
{{- end -}}
{{- end -}}

{{/*
Returns the secret name for the Secret containing the minio TLS certificate and key.
*/}}
{{- define "minioTLSSecret" -}}
{{- $fullname := include "minio.fullname" . -}}
{{- if coalesce .Values.ingress.acme .Values.global.ingress.acme | default false -}}
{{- printf "%s-acme-tls" $fullname -}}
{{- else -}}
{{- default "" (coalesce .Values.ingress.tls.secretName .Values.global.ingress.tls.secretName) -}}
{{- end -}}
{{- end -}}
