{{/*
Template for handling deprecation messages

The messages templated here will be combined into a single `fail` call. This creates a means for the user to receive all messages at one time, in place a frustrating iterative approach.

- `define` a new template, prefixed `gitlab.deprecate.`
- Check for deprecated values / patterns, and directly output messages (see message format below)
- Add a line to `gitlab.deprecations` to include the new template.

Message format:

**NOTE**: The `if` statement preceding the block should _not_ trim the following newline (`}}` not `-}}`), to ensure formatting during output.

```
chart:
    MESSAGE
```
*/}}
{{/*
Compile all deprecations into a single message, and call fail.

Due to gotpl scoping, we can't make use of `range`, so we have to add action lines.

We then check the number of items in the array vs the string length. If the string length is larger than the size of the array, then we have message contents. We are assured of this because `join "\n"` will insert n-1 "\n" into the string, thus a 3 item array, with no contents will be turned into a 2 character string.
*/}}
{{- define "gitlab.deprecations" -}}
{{- $deprecated := list -}}
{{/* add templates here */}}
{{- $deprecated := append $deprecated (include "gitlab.deprecate.railsConnection" .) -}}
{{- $deprecated := append $deprecated (include "gitlab.deprecate.minio" .) -}}
{{- $deprecated := append $deprecated (include "gitlab.deprecate.registryStorage" .) -}}
{{/* prepare output, check lengths */}}
{{- $message := join "\n" $deprecated -}}
{{- if lt (len $deprecated) (len $message) -}}
{{-   printf "\nDEPRECATIONS:\n%s" $message | fail -}}
{{- end -}}
{{- end -}}

{{/* Migration of rails `connection` blocks to secrets */}}
{{- define "gitlab.deprecate.railsConnection" -}}
{{- if .Values.gitlab.unicorn.lfs.connection -}}
{{-   if without (keys .Values.gitlab.unicorn.lfs.connection) "secret" "key" | len | ne 0 }}
gitlab.unicorn:
    The `lfs.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.unicorn.lfs.connection.secret`
{{-   end -}}
{{- end -}}
{{- if .Values.gitlab.unicorn.artifacts.connection -}}
{{-   if without (keys .Values.gitlab.unicorn.artifacts.connection) "secret" "key" | len | ne 0 }}
gitlab.unicorn:
    The `artifacts.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.unicorn.artifacts.connection.secret`
{{-   end -}}
{{- end -}}
{{- if .Values.gitlab.unicorn.uploads.connection -}}
{{-   if without (keys .Values.gitlab.unicorn.uploads.connection) "secret" "key" | len | ne 0 }}
gitlab.unicorn:
    The `uploads.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.unicorn.uploads.connection.secret`
{{-   end -}}
{{- end -}}
{{- if .Values.gitlab.sidekiq.lfs.connection -}}
{{-   if without (keys .Values.gitlab.sidekiq.lfs.connection) "secret" "key" | len | ne 0 }}
gitlab.sidekiq:
    The `lfs.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.sidekiq.lfs.connection.secret`
{{-   end -}}
{{- end -}}
{{- if .Values.gitlab.sidekiq.artifacts.connection -}}
{{-   if without (keys .Values.gitlab.sidekiq.artifacts.connection) "secret" "key" | len | ne 0 }}
gitlab.sidekiq:
    The `artifacts.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.sidekiq.artifacts.connection.secret`
{{-   end -}}
{{- end -}}
{{- if .Values.gitlab.sidekiq.uploads.connection -}}
{{-   if without (keys .Values.gitlab.sidekiq.uploads.connection) "secret" "key" | len | ne 0 }}
gitlab.sidekiq:
    The `uploads.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.sidekiq.uploads.connection.secret`
{{-   end -}}
{{- end -}}
{{- if index .Values.gitlab "task-runner" "lfs" "connection" -}}
{{-   if without (keys (index .Values.gitlab "task-runner" "lfs" "connection")) "secret" "key" | len | ne 0 }}
gitlab.task-runner:
    The `lfs.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.task-runner.lfs.connection.secret`
{{-   end -}}
{{- end -}}
{{- if index .Values.gitlab "task-runner" "artifacts.connection" -}}
{{-   if without (keys (index .Values "gitlab.task-runner" "artifacts.connection")) "secret" "key" | len | ne 0 }}
gitlab.task-runner:
    The `artifacts.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.task-runner.artifacts.connection.secret`
{{-   end -}}
{{- end -}}
{{- if index .Values.gitlab "task-runner" "uploads.connection" -}}
{{-   if without (keys (index .Values.gitlab "task-runner" "uploads.connection")) "secret" "key" | len | ne 0 }}
gitlab.task-runner:
    The `uploads.connection` declarations have been moved into a secret. Please create a secret with these contents, and set `gitlab.task-runner.uploads.connection.secret`
{{-   end -}}
{{- end -}}
{{- end -}}
{{/* END deprecate.connection */}}

{{/* Deprecation behaviors for global configuration of Minio */}}
{{- define "gitlab.deprecate.minio" -}}
{{- if ( hasKey .Values.minio "enabled" ) }}
minio:
    Chart-local `enabled` property has been moved to global. Please remove `minio.enabled` from your properties, and set `global.minio.enabled` instead.
{{- end -}}
{{- if .Values.registry.minio -}}
{{-   if ( hasKey .Values.registry.minio "enabled" ) }}
registry:
    Chart-local configuration of Minio features has been moved to global. Please remove `registry.minio.enabled` from your properties, and set `global.minio.enabled` instead.
{{-   end -}}
{{- end -}}
{{- if .Values.gitlab.unicorn.minio -}}
{{-   if ( hasKey .Values.gitlab.unicorn.minio "enabled" ) }}
gitlab.unicorn:
    Chart-local configuration of Minio features has been moved to global. Please remove `gitlab.unicorn.minio.enabled` from your properties, and set `global.minio.enabled` instead.
{{-   end -}}
{{- end -}}
{{- if .Values.gitlab.sidekiq.minio -}}
{{-   if ( hasKey .Values.gitlab.sidekiq.minio "enabled" ) }}
gitlab.sidekiq:
    Chart-local configuration of Minio features has been moved to global. Please remove `gitlab.sidekiq.minio.enabled` from your properties, and set `global.minio.enabled` instead.
{{-   end -}}
{{- end -}}
{{- if index .Values.gitlab "task-runner" "minio" -}}
{{-   if ( hasKey ( index .Values.gitlab "task-runner" "minio" ) "enabled" ) }}
gitlab.task-runner:
    Chart-local configuration of Minio features has been moved to global. Please remove `gitlab.task-runner.minio.enabled` from your properties, and set `global.minio.enabled` instead.
{{-   end -}}
{{- end -}}
{{- end -}}
{{/* END deprecate.minio */}}

{{/* Migration of Registry `storage` dict to a secret */}}
{{- define "gitlab.deprecate.registryStorage" -}}
{{- if .Values.registry.storage -}}
{{-   $keys := without (keys .Values.registry.storage) "secret" "key" "extraKey" -}}
{{-   if len $keys | ne 0 }}
registry:
    The `storage` property has been moved into a secret. Please create a secret with these contents, and set `storage.secret`.
{{-   end -}}
{{- end -}}
{{- end -}}
