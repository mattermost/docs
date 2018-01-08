# Generate configuration

Based on the [example-config.yaml](../example-config.yaml) file, you can generate
your own yaml template.

As an example, we will use domain `helm-charts.win`.
The filename of the template is derived from the domain name, `helm-charts-win`:

```
$cp doc/example-config.yaml helm-charts-win.yaml
```

Next, we are replacing the contents of the `helm-charts-win.yaml` with valid
information:

Set the following properties in `helm-charts-win.yaml`:
- nginx.service.loadBalancerIP: [static-ip]
- nginx.ingress.hosts[0].name: gitlab.helm-charts.win
- nginx.ingress.hosts[1].name: registry.helm-charts.win
- nginx.ingress.tls[0].secretName: helm-charts-win-tls
- nginx.ingress.tls[0].hosts[]: gitlab.helm-charts.win, registry.helm-charts.win
- gitlab.migrations.initialRootPassword: [from 1Password]
- registry.service.type: NodePort
- registry.registry.authEndpoint: 'https://gitlab.helm-charts.win'
- registry.registry.tokenIssuer: gitlab-issuer
- registry.registry.certificate.secret: gitlab-registry
- registry.registry.certificate.key: registry-auth.crt
- gitlab.omnibus.service.type: NodePort
- gitlab.omnibus.enabled: true
- gitlab.omnibus.external_url: 'https://gitlab.helm-charts.win'
- gitlab.omnibus.redis.enabled: false
- gitlab.omnibus.redis.serviceName: redis
- gitlab.omnibus.redis.password.secret: gitlab-redis
- gitlab.omnibus.redis.password.key: redis-password
- gitlab.omnibus.psql.enabled: true
- gitlab.omnibus.registry.host: registry.helm-charts.win
- gitlab.omnibus.registry.port: 80
- gitlab.omnibus.registry.secret: gitlab-registry
- gitlab.omnibus.registry.certificate: registry-auth.key

Now that the template is generated, we can proceed [to deployment](README.md#deploy).
