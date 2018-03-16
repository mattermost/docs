# External postgresql database

This document assumes that you have an external postgresql that is up and running.

If you need to spawn a postgresql instance for non-production purposes follow setting up [external omnibus postgresql instance](./external-omnibus-psql.md)

## Configure the Chart

The `migrations`, `unicorn`, and `sidekiq` charts require a Postgres database to function. When not using the GitLab chart's provided service, we'll need to provide the configuration information to all three. Each chart can be configured individually on a per-chart basis, or you can make use of global values to configure all charts from a single point.

### Specify per-chart value

To specify it per chart you will need to set `gitlab.omnibus.enabled=false`, `chartName.psql.host`, `chartname.psql.password.secret` and `chartname.psql.password.key` values
via helm's `--set` flag while [deploying](../installation/deployment.md)

example:

```
helm install
  --set gitlab.omnibus.enabled=false unicorn.psql.host=omnibus-vm
  --set unicorn.psql.password.secret=psql-secret
  --set unicorn.psql.password.key=<key>
```

You can also set the port number using `chartName.psql.port` setting. Default port is assumed to be `5432`

### Specify a global value

You need to set `gitlab.omnibus.enabled=false`, `global.psql.host`, `global.psql.password.secret` and `global.psql.password.key`values via helm's `--set` flag while deploying

```
helm install
  --set gitlab.omnibus.enabled=false
  --set global.psql.host=omnibus-vm
  --set global.psql.password.secret=psql-secret
  --set global.psql.password.key=<key>
```

You can also set the port number useing `global.psql.port` setting. Default is assumed to be `5432`


> For a description for these configurations [lookup](../installation/command-line-options.md)
