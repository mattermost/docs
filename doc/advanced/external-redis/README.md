# Configure this chart with External Redis

This document intends to provide documentation on how to configure this Helm chart with an external Redis service.

If you don't have Redis configured, for on-premise or deployment to VM,
consider using our [Omnibus GitLab package](./external-omnibus-redis.md).

## Configure the Chart

Disable the `redis` chart and the Redis service it provides, and point the other services to the external service.

You need to set the following parameters:
* `redis.enabled`: Set to `false` to disable the included Redis chart.
* `global.redis.host`: Set to the hostname of the external Redis, can be a domain or an IP address.
* `global.redis.password.secret`: The name of the [secret which contains the token for authentication][redis-secret].
* `global.redis.password.key`: The key within the secret, which contains the token content.

Items below can be further customized if you are not using the defaults:
* `global.redis.port`: The port the database is available on, defaults to `6379`

For example, pass these values via helm's `--set` flag while deploying:

```
helm install .  \
  --set redis.enabled=false \
  --set global.redis.host=redis.example \
  --set global.redis.password.secret=gitlab-redis \
  --set global.redis.password.key=redis-password \
```

[redis-secret]: ../../installation/secrets.md#redis-secret
