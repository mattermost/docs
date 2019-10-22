{{/* Templates for certificates injection */}}

{{- define "gitlab.certificates.initContainer" -}}
{{- $customCAsEnabled := .Values.global.certificates.customCAs }}
{{- $internalGitalyTLSEnabled := and $.Values.global.gitaly.tls.enabled $.Values.global.gitaly.tls.secretName }}
{{- $certmanagerDisabled := not (or $.Values.global.ingress.configureCertmanager $.Values.global.ingress.tls) }}
- name: certificates
  image: "{{ .Values.global.certificates.image.repository }}:{{ .Values.global.certificates.image.tag }}"
  {{ template "gitlab.imagePullPolicy" . }}
  volumeMounts:
  - name: etc-ssl-certs
    mountPath: /etc/ssl/certs
    readOnly: false
{{- if or $customCAsEnabled (or $certmanagerDisabled $internalGitalyTLSEnabled) }}
  - name: custom-ca-certificates
    mountPath: /usr/local/share/ca-certificates
    readOnly: true
{{- end }}
  resources:
{{ toYaml .Values.init.resources | indent 4 }}
{{- end -}}

{{- define "gitlab.certificates.volumes" -}}
{{- $customCAsEnabled := .Values.global.certificates.customCAs }}
{{- $internalGitalyTLSEnabled := and $.Values.global.gitaly.tls.enabled $.Values.global.gitaly.tls.secretName }}
{{- $certmanagerDisabled := not (or $.Values.global.ingress.configureCertmanager $.Values.global.ingress.tls) }}
- name: etc-ssl-certs
  emptyDir:
    medium: "Memory"
{{- if or $customCAsEnabled (or $certmanagerDisabled $internalGitalyTLSEnabled) }}
- name: custom-ca-certificates
  projected:
    defaultMode: 0400
    sources:
    {{- range $index, $customCA := .Values.global.certificates.customCAs }}
    - secret:
        name: {{ $customCA.secret }}
        # items not specified, will mount all keys
    {{- end }}
    {{- if not (or $.Values.global.ingress.configureCertmanager $.Values.global.ingress.tls) }}
    - secret:
        name: {{ template "gitlab.wildcard-self-signed-cert-name" $ }}-ca
    {{- end }}
    {{- if $internalGitalyTLSEnabled }}
    - secret:
        name: {{ template "gitlab.gitaly.tls.secret" $ }}
        items:
          - key: "tls.crt"
            path: "gitaly-internal-tls.crt"
    {{- end }}
{{- end -}}
{{- end -}}

{{- define "gitlab.certificates.volumeMount" -}}
- name: etc-ssl-certs
  mountPath: /etc/ssl/certs/
  readOnly: true
{{- end -}}
