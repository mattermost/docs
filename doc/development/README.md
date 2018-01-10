# Development Styleguide

Our contribution policies can be found in [CONTRIBUTING.md](../../CONTRIBUTING.md)

## Naming Conventions

We are using camelCase for our function names, and properties where they are used in values.yaml

## Common structure for values.yaml

Many charts need to be provided with the same information, for example we need to provide the redis and postgres connection settings to  multiple charts. Here we outline our standard naming and structure for those settings.

### Connecting to other services

```
redis:
  host: redis.example.local
  serviceName: redis
  port: 8080
  password:
    secret: gitlab-redis
    key: redis-password
```

- `redis` - the name for what the current chart needs to connect to
- `host`  - overrides the use of serviceName, comment out by default use `0.0.0.0` as the example
- `serviceName` - intended to be used by default instead of the host, connect using the Kubernetes Service name
- `port` - the port to connect on. Comment out by default, and use the default port as the example. 
- `password`- defines settings for the Kubernetes Secret containing the password.

### Sharing secrets

We use secrets to store sensitive information like passwords and share them among the different charts/pods.

The common fields we use them in are:

- **Certificates** - TLS certificates for the registry etc.
- **Passwords** - Sharing the redis password.
- **Auth Tokens** - Sharing the inter-service auth tokens

### Certificates

For example, where `registry` was the owning chart, and the other charts need to reference the `registry` certificate.

The owning chart should define its certificate secret like the following:

```
certificate:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same certificate secret like the following:

```
registry:
  certificate:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

### Passwords

For example, where `redis` was the owning chart, and the other charts need to reference the `redis` password.

The owning chart should define its password secret like the following:

```
password:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same password secret like the following:

```
redis:
  password:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

### Auth Tokens

The owning chart should define its authToken secret like the following:

```
authToken:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same password secret like the following:

```
gitaly:
  authToken:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

For example, where `gitaly` was the owning chart, and the other charts need to reference the `gitaly` authToken.
