# Using the Omnibus GitLab container

The `omnibus` sub-chart provides the [Omnibus GitLab][og-docker] container as a
stepping stone for development of component isolation. It is intended to provide
a method for testing and development of each other sub-chart as we migrate to
individual component / concerns per chart.

This is container is not meant to be a permanent member of this chart. It should
not be used for anything other than development and testing.

**NOTE:** *This chart does not persist any data.* This means that it will be a fresh container on every pod deployment, and absolutely no state is persisted.

## Design Choices

This sub-chart was implemented explicitly to ease the development process of
[this helm chart][helm-gitlab]. Every sub-component that will eventually be
extracted has been configured to expose itself over their respective default TCP ports to enable inter-container communication.

Components / Services not exposed:
- The [Registry][registry] sub-chart had already been completed.
- [Mattermost][mattermost] is a contained service.
- [GitLab Pages][gl-pages] requires being present on a different address to the
primary services
- Prometheus could be exposed, but was not.

The available components are:
- psql (on by default)

The components below have been replaced by other charts
- [nginx][]
- [redis][]
- shell ([gitlab-shell][] / ssh)
- [unicorn][] (primary Rails)
- [workhorse][unicorn] (primary in-line smart proxy)
- [sidekiq][]
- [gitaly][]

# Configuration

## Enable the sub-chart

The `omnibus` chart is disabled out of the box. To make use of it as a developer
you will need to enable it by settings `enabled: true`.

## Configure the image

This section dictates the settings for the container image used by this sub-chart's [Deployment][]. You can change the included version of the [Omnibus Gitlab][og-gitlab] and `pullPolicy`.

Default settings:
- `tag: '10.0.2-ee.0'`
- `pullPolicy: 'IfNotPresent'`

## Configuring Omnibus settings

`external_url` [provides the external hostname and scheme][oq-external-url] to the Omnibus container.

```
external_url: http://gitlab.example.local
```

`trusted_proxies` list will be used to populate [NGINX Real IP][og-nginx-proxy] and [Trusted Proxies][og-trusted-proxy]. Entries should be in quoted CIDR format.

```
trusted_proxies:
- "127.0.0.1/24"
- "10.0.0.0/8"
- "172.16.0.0/12"
- "192.168.0.0/16"
```

## Redis

### Configure Redis

Regardless of using the component, Redis is a requirement of the GitLab stack.
If you use the built-in Redis, the following will default to connect internally.

- `host` contains the hostname of the Redis server.
- `serviceName` contains the name of the service in-chart [Redis service][redis].
- `port` contains the port on the `host` to connect to.
- `password` contains a map of `secret` and `key`. This should contain the secret name, and key name which house the password that will be used for the Redis server.

```
redis:
  enabled: false
  host: '127.0.0.1'
  serviceName: redis
  port: 6397
  # password provided as ENV, via Secret
  password:
    secret: gitlab-redis
    key: redis-password
```
## PostgreSQL

### Configure PostgreSQL

Regardless of using the component, PostgreSQL is a requirement of the GitLab stack.
If you use the built-in PostgreSQL, the following will default to connect internally.

- `database` contains the database name GitLab will use. Default: `gitlabhq_production`
- `username` contains the username for authentication to the server. Default: `gitlab`
- `password` contains the password for authentication to the server. Default: `nil`
- `sql_user_password` contains the encoded password for MD5 authentication to the psql server. Default: `nil`
  - The value of this should be `echo -n "${password}gitlab" | md5sum - | cut -d ' ' -f 1`

When using an external PostgreSQL, you will need to provide all of the above.

```
psql:
  database: 'gitlabhq_production'
  username: 'gitlab'
  password: nil
  sql_user_password: nil
```

[og-docker]: https://gitlab.com/gitlab-org/ominbus-gitlab/container_registry
[helm-gitlab]: https://gitlab.com/charts/helm.gitlab.io
[nginx]: ../../nginx
[registry]: ../../registry
[redis]: ../../redis
[unicorn]: ../unicorn
[sidekiq]: ../sidekiq
[gitlay]: ../gitaly
[gitlab-shell]: ../gitlab-shell
[mattermost]: https://gitlab.com/mattermost
[gl-pages]: https://about.gitlab.com/features/pages/
[og-external-url]: https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab
[og-nginx-proxy]: https://docs.gitlab.com/omnibus/settings/nginx.html#configuring-gitlab-trusted_proxies-and-the-nginx-real_ip-module
[og-trusted-proxy]: https://docs.gitlab.com/omnibus/settings/nginx.html#using-a-non-bundled-web-server

[Service]: ../../../../charts/gitlab/charts/omnibus/templates/service.yaml
[Deployment]: ../../../../charts/gitlab/charts/omnibus/templates/deployment.yaml
[ConfigMap]: ../../../../charts/gitlab/charts/omnibus/templates/registry-configmap.yaml
[kubernetes-secret]: https://kubernetes.io/docs/concepts/configuration/secret/
