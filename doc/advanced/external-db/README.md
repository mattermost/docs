# External postgresql database

This document assumes that you have an external postgresql that is up and running.

If you need to spawn a postgresql instance for non-production purposes follow setting up [external omnibus postgresql instance](./external-omnibus-psql.md)

## Configure the Chart

`migrations`, `unicorn` and `sidekiq` gitlab charts needs a postgresql database and so we will need to provide to all of them.

Each of these chart has it's postgresql configurations. However, these charts support overriding their psql configs by specifying it globally if you intend
to deploy multiple of these charts together instead of specifying the same config multiple times.

### Specify per-chart value

To specify it per chart you will need to set `gitlab.omnibus.enabled=false`, `chartName.psql.host`, `chartname.psql.password.secret` and `chartname.psql.password.key` values
via helm's `--set` flag while [deploying](../installation/deployment.md)

example: `helm install --set gitlab.omnibus.enabled=false unicorn.psql.host=omnibus-vm --set unicorn.psql.password.secret=psql-secret --set unicorn.psql.password.key=<password>`

You can also set the port number using `chartName.psql.port` setting. Default port is assumed to be 5432

### Specify a global value

You need to set `gitlab.omnibus.enabled=false`, `global.psql.host`, `global.psql.password.secret` and `global.psql.password.key`values via helm's `--set` flag while deploying

`helm install --set gitlab.omnibus.enabled=false --set global.psql.host=omnibus-vm --set global.psql.password.secret=psql-secret --set global.psql.password.key=<password>`

You can also set the port number useing `global.psql.port` setting. Default is assumed to be 5432


> For a description for these configurations [lookup](../installation/command-line-options.md)
