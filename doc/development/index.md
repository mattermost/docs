# Development styleguide

Our contribution policies can be found in [CONTRIBUTING.md](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/CONTRIBUTING.md)

## Versioning and Release

Details on the version scheme, branching and tags can be found in [release document](release.md).

## Changelog Entries

All `CHANGELOG.md` entries should be created via the [changelog entries](changelog.md) workflow.

## Installation from Repo

Details on installing from the git repo can be found in the [developer deployment](deploy.md) documentation.

## Running GitLab QA

[GitLab QA](https://gitlab.com/gitlab-org/gitlab-qa) can be used against a
deployed cloud native GitLab installation.

[Read more in the GitLab QA chart docs](gitlab-qa/index.md).

## Kube monkey

[kube monkey](https://github.com/asobti/kube-monkey) is an implementation of
Netflix's [chaos monkey](https://github.com/Netflix/chaosmonkey) for kubernetes
clusters. It schedules randomly killing of pods in order to test fault tolerance
of a highly available system.

[Read more in the kube monkey chart docs](kube-monkey/index.md).

## Developing for Kubernetes with Minikube

Read how to [use minikube for setting up a local Kubernetes development environment](minikube/index.md).

## Naming Conventions

We are using [camelCase](https://en.wikipedia.org/wiki/Camel_case) for our function names, and properties where they are used in values.yaml

Example: `gitlab.assembleHost`

Template functions are placed into namespaces according to the chart they are associated with, and named to match the affected populated value in the target file. Note that chart _global_ functions generally fall under the `gitlab.*` namespace.

Examples:

- `gitlab.redis.host`: provides the host name of the Redis server, as a part of the `gitlab` chart.
- `registry.minio.url`: provides the URL to the Minio host as part of the `registry` chart.

## Common structure for values.yaml

Many charts need to be provided with the same information, for example we need to provide the redis and postgres connection settings to  multiple charts. Here we outline our standard naming and structure for those settings.

### Connecting to other services

```yaml
redis:
  host: redis.example.com
  serviceName: redis
  port: 8080
    sentinels:
    - host: sentinel1.example.com
      port: 26379
  password:
    secret: gitlab-redis
    key: redis-password
```

- `redis` - the name for what the current chart needs to connect to
- `host`  - overrides the use of serviceName, comment out by default use `0.0.0.0` as the example. If using Redis Sentinels, the `host` attribute needs to be set to the cluster name as specified in the `sentinel.conf`.
- `serviceName` - intended to be used by default instead of the host, connect using the Kubernetes Service name
- `port` - the port to connect on. Comment out by default, and use the default port as the example.
- `password`- defines settings for the Kubernetes Secret containing the password.
- `sentinels.[].host` - defines the hostname of Redis Sentinel server for a Redis HA setup.
- `sentinels.[].port` - defines the port on which to connect to the Redis Sentinel server. Defaults to `26379`.

_Note:_ The current Redis Sentinel support only supports Sentinels that have
been deployed separately from the GitLab chart. As a result, the Redis
deployment through the GitLab chart should be disabled with `redis.enabled=false`
and `redis-ha.enabled=false`. The Secret containing the Redis password
will need to be manually created before deploying the GitLab chart.

### Sharing secrets

We use secrets to store sensitive information like passwords and share them among the different charts/pods.

The common fields we use them in are:

- **Certificates** - TLS certificates for the registry etc.
- **Passwords** - Sharing the redis password.
- **Auth Tokens** - Sharing the inter-service auth tokens

### Certificates

For example, where `registry` was the owning chart, and the other charts need to reference the `registry` certificate.

The owning chart should define its certificate secret like the following:

```yaml
certificate:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same certificate secret like the following:

```yaml
registry:
  certificate:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

### Passwords

For example, where `redis` was the owning chart, and the other charts need to reference the `redis` password.

The owning chart should define its password secret like the following:

```yaml
password:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same password secret like the following:

```yaml
redis:
  password:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

### Auth Tokens

The owning chart should define its authToken secret like the following:

```yaml
authToken:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same password secret like the following:

```yaml
gitaly:
  authToken:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

For example, where `gitaly` was the owning chart, and the other charts need to reference the `gitaly` authToken.

## Developing template helpers

A charts template helpers are located in `templates/_helpers.tpl`. These contain the [named templates](https://helm.sh/docs/chart_template_guide/#declaring-and-using-templates-with-define-and-template)
used within the chart.

When using these templates, there a few things to keep in mind regarding the [golang templating syntax](https://golang.org/pkg/text/template/).

### Trapping non-printed values from actions

In the go templating syntax, all actions (indicated by `{{  }}`) are expected
to print a string, with the exception of control structures (define, if, with, range) and variable assignment.

This means you will sometimes need to use variable assignment to trap output that is not meant to be printed.

For example:

```
{{- $details := .Values.details -}}
{{- $_ := set $details "serviceName" "example" -}}
{{ template "serviceHost" $details }}
```

In the above example, we want to add some additional data to a Map before passing it to a template function for output.
We trapped the output of the `set` function by assigning it to the the `$_` variable. Without this assignment, the
template would try to output the result of `set` (which returns the Map it modified) as a string.

### Passing variables between control structures

The go templating syntax only gives us one way to assign variables, and that is by using [shorthand assignment](https://golang.org/pkg/text/template/#hdr-Variables).

As a result you cannot reassign a variable that existed outside your control structure (if/with/range), and variables declared
within your control structure are not available outside.

For example:

```
{{- define "exampleTemplate" -}}
{{- $someVar := "default" -}}
{{- if true -}}
{{-   $someVar := "desired" -}}
{{- end -}}
{{- $someVar -}}
{{- end -}}
```

In the above example, calling `exampleTemplate` will always return `default` because the variable that contained `desired` was
only accessible within the `if` control structure.

To work around this issue, we either avoid the problem, or use a Dictionary to hold the values we want to change.

Example of avoiding the issue:

```
{{- define "exampleTemplate" -}}
{{- if true -}}
{{-   "desired" -}}
{{- else -}}
{{-   "default" -}}
{{- end -}}
```

Example of using a Dictionary:

```
{{- define "exampleTemplate" -}}
{{- $result := dict "value" "default" -}}
{{- if true -}}
{{-   $_ := set $result "value" "desired" -}}
{{- end -}}
{{- $result.value -}}
{{- end -}}
```

## When to fork upstream charts

### No changes, no fork

Let it be stated that any chart that does not require changes to function
for our use *should not* be forked into this repository.

### Guidelines for forking

#### Sensitive information

If a given chart expects that sensitive communication secrets will be presented
from within environment, such as passwords or cryptographic keys, [we prefer to
use initContainers][initContainer-vs-env].

[initContainer-vs-env]: ../architecture/decisions.md#preference-of-secrets-in-initcontainer-over-environment

#### Extending functionality

There are some cases where it is needed to extend the functionality of a chart in
such a way that an upstream may not accept.

#### When to utilize `toYaml` in templates

It is frowned upon to default to utilizing a `toYaml` in the template files as
this will put undue burden on supporting all functionalities of both Kuberentes
and desired community configurations.  We primary focus on providing a
reasonable default using the bare minimum configuration.  Our secondary focus
would be to provide the ability to override the defaults for more advanced users
of Kubernetes.  This should be done on a case-by-case basis as there are
certainly scenarios where either option may be too cumbersome to support, or
provides an unnecessarily complex template to maintain.

An good example of a reasonable default with the ability to override can be
found in the Horizontal Pod Autoscaler configuration for the registry subchart.
We default to providing the bare minimum that can easily be supported, by
exposing a specific configuration of controlling the HPA via the CPU Utilization
and exposing only one configuration option to the community, the
`targetAverageUtilization`.  Being that an HPA can provide much more
flexibility, more advanced users may want to target different metrics and as
such, is a perfect example of where we can utilize and if statement allowing the
end user to provide a more complex HPA configuration in place.

```yaml
  metrics:
  {{- if not .Values.hpa.customMetrics }}
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          targetAverageUtilization: {{ .Values.hpa.cpu.targetAverageUtilization }}
  {{- else -}}
    {{- toYaml .Values.hpa.customMetrics | nindent 4 -}}
  {{- end -}}
```

In the above example, the minimum configuration will be a simple change in the
`values.yaml` to update the `targetAverageUtilization`.

Advanced users who have identified a better metric can override this overly
simplistic HPA configuration by setting `.customMetrics` to an array containing
precisely the Kubernetes API compatible configuration for the HPA metrics array.

It is important that we maintain ease of use for the more advanced users to
minimize their own configuration files without it being cumbersome.

## Handling configuration deprecations

There are times in a development where changes in behavior require a functionally breaking change. We try to avoid such changes, but some items can not be handled without such a change.

To handle this, we have implemented the [deprecations template][]. This template is designed to recognize properties that need to be replaced or relocated, and inform the user of the actions they need to take. This template will compile all messages into a list, and then cause the deployment to stop via a `fail` call. This provides a method to inform the user at the same time as preventing the deployment the chart in a broken or unexpected state.

See the documentation of the [deprecations template][] for further information on the design, functionality, and how to add new deprecations.

[deprecations template]: deprecations.md

## Attempt to catch problematic configurations

Due to the complexity of these charts and their level of flexibility, there are some overlaps where it is possible to produce a configuration that would lead to an unpredictable, or entirely non-functional deployment. In an effort to prevent known problematic settings combinations, we have implemented template logic designed to detect and warn the user that their configuration will not work

See the documentation of the [checkConfig template](checkconfig.md) for further information on the design, functionality, and how to add new configuration checks.

## Verifying registry

In development mode, verifying Registry with Docker clients can be difficult. This is partly due to issues with certificate of
the registry. You can either [add the certificate](https://docs.docker.com/registry/insecure/#use-self-signed-certificates) or
[expose the registry over HTTP](https://docs.docker.com/registry/insecure/#deploy-a-plain-http-registry) (see `global.hosts.registry.https`).
Note that adding the certificate is more secure than the insecure registry solution.

Please keep in mind that Registry uses the external domain name of Minio service (see `global.hosts.minio.name`). You may
encounter an error when using internal domain names, e.g. with custom TLDs for development environment. The common symptom
is that you can login to the Registry but you can't push or pull images. This is generally because the Registry container(s)
can not resolve the Minio domain name and find the correct endpoint (you can see the errors in container logs).
