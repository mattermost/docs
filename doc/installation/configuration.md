# Generate configuration

Based on the [example-config.yaml](../example-config.yaml) file, you can generate
your own yaml template.

For this example, we will use domain `example.local`, and expect our hostnames to be: `gitlab.example.local`, `registry.example.local`.

```
cp doc/example-config.yaml configuration.yaml
```

In order to complete the configuration, we will need to prepare a few values:
- Creation of `Secrets` from [secrets documentation](secrets.md)
- [static-ip][] for the `loadBalancerIP`
- [DNS entry][] made for the domain
- `initialRootPassword`, from 1Password or chosen at random

Next, we are replacing the contents of the `configuration.yaml` with valid
information:

Set the following properties in `configuration.yaml`

> *Note:* Find and edit each property. They should already exist, but will need their value set, and may need to be uncommented.

```YAML
global:
  hosts:
    domain: example.local
    https: true

nginx:
  service:
    loadBalancerIP: <static ip>
  serviceAccount:
    autoGenerate: true

kube-lego:
  LEGO_EMAIL: <valid email address>
  # LEGO_URL: <url> should be uncommented if you desire production ready certificates

gitlab:
  migrations:
    initialRootPassword: initialRootPassword
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

[static-ip]: resources.md#static-ip
[DNS entry]: resources.md#dns-entry
[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
