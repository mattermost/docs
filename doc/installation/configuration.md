# Generate configuration

Based on the [example-config.yaml](../example-config.yaml) file, you can generate
your own yaml template.

For this example, we will use domain `helm-charts.win`, and host names based on that: `gitlab.helm-charts.win`, `registry.helm-charts.win`.

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

`echo -n '${SQLPassword}gitlab' | md5sum - | cut -d ' ' -f1`

Next, we are replacing the contents of the `configuration.yaml` with valid
information:

Set the following properties in `configuration.yaml` (in order of appearance):
- nginx.service.loadBalancerIP: [static-ip][]
- nginx.ingress.hosts[0].name: gitlab.helm-charts.win
- nginx.ingress.hosts[1].name: registry.helm-charts.win
- registry.registry.authEndpoint: 'https://gitlab.helm-charts.win'
- gitlab.unicorn.gitlabHost: gitlab.helm-charts.win
- gitlab.unicorn.registry.host: registry.helm-charts.win
- gitlab.unicorn.psql.password: SQLPassword
- gitlab.sidekiq.psql.password: SQLPassword
- gitlab.migrations.initialRootPassword: initialRootPassword
- gitlab.migrations.psql.password: SQLPassword
- gitlab.omnibus.psql.sql_user_password: encodedSQLPassword

If you are using [Let's Encrypt certificates](secrets.md#lets-encrypt):
- nginx.ingress.acme: true

If you are using [Wildcard certificates](secrets.md#wildcard-certificates):
- nginx.ingress.tls[0].secretName: helm-charts-win-tls
- nginx.ingress.tls[0].hosts[]: gitlab.helm-charts.win, registry.helm-charts.win

If you are using a cluster with [RBAC](rbac.md):
- nginx.servieAccount.autoGenerate: true

Now that the template is generated, we can proceed [to deployment](README.md#deploy).

[static-ip]: resources.md#static-ip
[DNS entry]: resources.md#dns-entry
[secret-gl-certs]: secrets.md#gitlab-certificates
[secret-reg-certs]: secrets.md#registry-certificates
