# Using the Shared-Secrets chart

The `shared-secrets` sub-chart is responsible for provisioning a variety of secrets
used across the installation, unless otherwise manually specified. This includes:

1. Initial root password
1. Self-signed TLS certificates for all public services: GitLab, Minio, and Registry
1. Registry authentication certificates
1. Minio, Registry, GitLab Shell, and Gitaly secrets
1. Redis and Postgres passwords
1. SSH host keys

## Installation command line options

The table below contains all the possible charts configurations that can be supplied
to the `helm install` command using the `--set` flag:

| Parameter                  | Default             | Description                         |
| -------------------------- | ------------------- | ----------------------------------- |
| `enabled`                  | `true`              | [See Below](#disable-functionality) |
| `env`                      | `production`        | Rails environment                   |
| `image.pullPolicy`         | `Always`            | Gitaly image pull policy            |
| `image.pullSecrets`        |                     | Secrets for the image repository    |
| `image.repository`         | `registry.gitlab.com/gitlab-org/build/cng/kubectl` | Gitaly image repository |
| `image.tag`                | `1f8690f03f7aeef27e727396927ab3cc96ac89e7` | Gitaly image tag |
| `rbac.create`              | `true`              | Create RBAC roles and bindings      |
| `resources`                |                     | resource requests, limits           |
| `securitContext.fsGroup`   | `65534`             | User ID to mount filesystems as     |
| `securitContext.runAsUser` | `65534`             | User ID to run the container as     |
| `selfsign.caSubject`       | `GitLab Helm Chart` | selfsign CA Subject                 |
| `selfsign.image`           | `registry.gitlab.com/gitlab-org/build/cnf/cfssl-self-sign` | selfsign image repository |
| `selfsign.keyAlgorithm`    | `rsa`               | selfsign cert key algorithm         |
| `selfsign.keySize`         | `4096`              | selfsign cert key size              |
| `selfsign.tag`             |                     | selfsign image tag                  |
| `tolerations`              | `[]`                | Toleration labels for pod assignment|

## Chart configuration examples

### tolerations

`tolerations` allow you schedule pods on tainted worker nodes

Below is an example use of `tolerations`:

```yaml
tolerations:
- key: "node_label"
  operator: "Equal"
  value: "true"
  effect: "NoSchedule"
- key: "node_label"
  operator: "Equal"
  value: "true"
  effect: "NoExecute"
```

## Disable functionality

Some users may wish to explicitly disable the functionality provided by this sub-chart.
To do this, we have provided the `enabled` flag as a boolean, defaulting to `true`.

To disable the chart, pass `--set shared-secrets.enabled=false`, or pass the following
in a YAML via the `-f` flag to `helm`:

```yaml
shared-secrets:
  enabled: false
```

NOTE: **Note:** If you disable this sub-chart, you **must** manually create all secrets,
  and provide all necessary secret content. See [installation/secrets](../../installation/secrets.md#manual-secret-creation-optional)
  for further details.
