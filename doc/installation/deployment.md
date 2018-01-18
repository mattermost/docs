To deploy, we'll run `helm install` with our configuration file, from the
root of this repository:

```
$ helm install -f configuration.yaml .
```

This will output the list of resources being installed.

Later, the status of the deployment can be checked with `helm status <deployment-name>`.

```
$ helm status ill-dachshund
```
