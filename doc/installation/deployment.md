To deploy, we'll run `helm install` with our configuration file, from the
root of this repository:

```
helm install --name gitlab --timeout 600 -f configuration.yaml .
```

This will output the list of resources installed once the deployment finishes which may take 5-10 minutes.

The status of the deployment can be checked by running `helm status gitlab` which can also be done while
the deployment is taking place if you run the command in another terminal.
