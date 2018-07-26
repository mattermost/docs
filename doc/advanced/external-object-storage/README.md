# External object stoarge

Gitlab relies on object storage in Kubernetes highly-available persisted data.
By default, an S3-compatible storage solution named `minio` is deployed with the
chart, but for production quality deployments, we recommend using a hosted
object storage solution like Google Cloud Storage or AWS S3.

To disable minio, set this option and then follow the related documentation below:

```
--set global.minio.enabled=false
```

## Docker Registry images

Configuration of object storage for the `registry` chart is done via the `registry.storage` key. See the [registry chart documentation on storage](../../charts/registry/README.md#storage) for more details.

Create the secret per documentation, then configure the chart to make use of this secret:

```
--set registry.storage.secret=registry-storage
```

## LFS, Artifacts, Uploads

Configuration of object storage for LFS, artifacts, and uploads is done via the `global.appConfig.lfs`, `global.appConfig.artifacts`, and `global.appConfig.uploads` keys. See the [charts/globals documentaion on appConfig](../../charts/globals.md#configure-appconfig-settings) for more details.

Create the secret(s) per documentation, and then configure the chart to use the provided secrets. Note, you can use the same secret for all 3 if you so chose.

Configure the chart to use these secrets:

```
--set global.appConfig.lfs.connection.secret=objectstore-lfs
--set global.appConfig.lfs.connection.secret=objectstore-artifacts
--set global.appConfig.lfs.connection.secret=objectstore-uploads
````
