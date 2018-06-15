charts/gitlab/charts/sidekiq/templates/configmap.yaml
  - .Values.artifacts.connection
  - .Values.lfs.connection
  - .Values.uploads.connection
charts/gitlab/charts/sidekiq/templates/deployment.yaml
  - If minio isn't enabled, there's no secret mounting?

charts/gitlab/charts/task-runner/templates/configmap.yaml
  - .Values.lfs.bucket
  - .Values.lfs.connection
  - host_base = {{ template "gitlab.minio.hostname" . }}
    host_bucket = {{ template "gitlab.minio.hostname" . }}/%(bucket)
charts/gitlab/charts/task-runner/templates/depolyment.yaml
  - If minio isn't enabled, there's no secret mounting?

charts/gitlab/charts/unicorn/templates/configmap.yml
  - .Values.artifacts.connection
  - .Values.lfs.connection
  - .Values.uploads.connection
charts/gitlab/charts/unicorn/templates/depolyment.yaml
  - If minio isn't enabled, there's no secret mounting?

charts/registry/templates/configmap.yaml
  - .Values.storage
