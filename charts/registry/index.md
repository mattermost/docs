Forked from https://github.com/helm/charts/tree/master/stable/docker-registry

With a few tweaks to make it play nicely with GitLab, including Minio S3
storage and GitLab authentication endpoint.

## Notable additional configuration

Parameter | Description | Default
--- | --- | ---
`enabled` | enable/disable registry | `true`
`authEndpoint` | override authentication endpoint (only host and port) | `global.hosts.gitlab.name`
`authAutoRedirect` | enable/disable authentication auto-redirect (don't change it to `false` otherwise Windows clients won't work) | `true`
`tokenIssuer` | authentication token issuer (must match your GitLab Rails configuration) | `gitlab-issuer`
`minio.bucket` | Minio bucket name to use, precedes `.global.registry.bucket` | ``

## Development

For more details, see [development notes](../../doc/development/index.md#verifying-registry) 