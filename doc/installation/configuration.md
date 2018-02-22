# Generate configuration

In order to complete the configuration, make sure you have done the following:

- `Secrets` are created - [secrets documentation](secrets.md)
- You have the static-ip for the `loadBalancerIP`
- DNS entry made for the domain pointing to the `loadBalancerIP`
- `initialRootPassword` - created or chosen at random

Now you can, based on the [example-config.yaml](../example-config.yaml) file, generate
your own configuration file.

```
cp doc/example-config.yaml configuration.yaml
```
For this example:

- We will use domain `example.local` as our `DNS entry`, and expect our hostnames
  to be: `gitlab.example.local`, `registry.example.local`.
- We will use `X.X.X.X` as our `loadBalancerIP`
- Our `initialRootPassword` will be `example-password`

Next, we are replacing the contents of the `configuration.yaml` with valid
information:

Set the following properties in `configuration.yaml`
> *Note:* Find and edit each property. They should already exist, but will need their value set, and may need to be uncommented.

```YAML
global:
  hosts:
    domain: example.local

nginx:
  service:
    loadBalancerIP: X.X.X.X

kube-lego:
  LEGO_EMAIL: <valid email address>
  # LEGO_URL: <url> should be uncommented if you desire production ready certificates

gitlab:
  migrations:
    initialRootPassword: example-password
```

If you wish to use your own [custom wildcard certificates](secrets.md#custom-certificates),
edit the config file as follows:

```YAML
nginx:
  ingress:
    acme: false
```

```YAML
kube-lego:
  enabled: false
```

```YAML
global:
  hosts:
    tls:
      secretName: example-local-tls
```

# Next Steps

Now that the template is generated, we can proceed [to deployment](deployment.md).

[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
