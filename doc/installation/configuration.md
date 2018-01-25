# Generate configuration

Based on the [example-config.yaml](../example-config.yaml) file, you can generate
your own yaml template.

For this example, we will use domain `example.local`, and expect our hostnames to be: `gitlab.example.local`, `registry.example.local`.

```
$ cp doc/example-config.yaml configuration.yaml
```

In order to complete the configuration, we will need to prepare a few values:
- Creation of `Secrets` from [secrets documentation](secrets.md)
- [static-ip][] for the `loadBalancerIP`
- [DNS entry][] made for the domain
- `initialRootPassword`, from 1Password or chosen at random
- PostgreSQL database password, chosen and then encoded, for `SQLPassword` and `encodedSQLPassword`

To create the create the encoded form of the PostgreSQL password, we'll note our selected password and then run the following command, replacing `${SQLPassword}` with your chosen password, using the value where you see `encodedSQLPassword`:

`echo -n "${SQLPassword}gitlab" | md5sum - | cut -d ' ' -f1`

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

gitlab:
  unicorn:
    psql:
      password: SQLPassword

  sidekiq:
    psql:
      password: SQLPassword

  migrations:
    psql:
      password: SQLPassword
    initialRootPassword: initialRootPassword

  omnibus:
    psql:
      sql_user_password: encodedSQLPassword
```

If you are using [Let's Encrypt certificates](secrets.md#lets-encrypt):

```YAML
nginx:
  ingress:
    acme: true
```

Or If you are using [Wildcard certificates](secrets.md#wildcard-certificates):

```YAML
global:
  hosts:
    tls:
      secretName: example-local-tls
```

Now that the template is generated, we can proceed [to deployment](README.md#deploy).

[static-ip]: resources.md#static-ip
[DNS entry]: resources.md#dns-entry
[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
