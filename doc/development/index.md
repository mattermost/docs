# Development Styleguide

Our contribution policies can be found in [CONTRIBUTING.md](../../CONTRIBUTING.md)

**Table of Contents**
- [Versioning and Release](#versioning-and-release)
- [Changelog Entries](#changelog-entries)
- [Naming Conventions](#naming-conventions)
- [Common Structure for values.yaml](#common-structure-for-valuesyaml)
- [Developing template helpers](#developing-template-helpers)
- [When to fork from upstream charts](#when-to-fork-upstream-charts)
- [Handling configuration deprecation](#handling-configuration-deprecation)

## Versioning and Release

Details on the version scheme, branching and tags can be found in [release document](release.md)

## Changelog Entries

All `CHANGELOG.md` entries should be created via the [changelog entries](changelog.md) workflow.

## Naming Conventions

We are using [camelCase](https://en.wikipedia.org/wiki/Camel_case) for our function names, and properties where they are used in values.yaml

Example: `gitlab.assembleHost`

Template functions are placed into namespaces according to the chart they are associated with, and named to match the affected populated value in the target file. Note that chart _global_ functions generally fall under the `gitlab.*` namespace.

Exmaples:
- `gitlab.redis.host`: provides the host name of the Redis server, as a part of the `gitlab` chart.
- `registry.minio.url`: provides the URL to the Minio host as part of the `registry` chart.

## Common structure for values.yaml

Many charts need to be provided with the same information, for example we need to provide the redis and postgres connection settings to  multiple charts. Here we outline our standard naming and structure for those settings.

### Connecting to other services

```
redis:
  host: redis.example.com
  serviceName: redis
  port: 8080
  password:
    secret: gitlab-redis
    key: redis-password
```

- `redis` - the name for what the current chart needs to connect to
- `host`  - overrides the use of serviceName, comment out by default use `0.0.0.0` as the example
- `serviceName` - intended to be used by default instead of the host, connect using the Kubernetes Service name
- `port` - the port to connect on. Comment out by default, and use the default port as the example.
- `password`- defines settings for the Kubernetes Secret containing the password.

### Sharing secrets

We use secrets to store sensitive information like passwords and share them among the different charts/pods.

The common fields we use them in are:

- **Certificates** - TLS certificates for the registry etc.
- **Passwords** - Sharing the redis password.
- **Auth Tokens** - Sharing the inter-service auth tokens

### Certificates

For example, where `registry` was the owning chart, and the other charts need to reference the `registry` certificate.

The owning chart should define its certificate secret like the following:

```
certificate:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same certificate secret like the following:

```
registry:
  certificate:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

### Passwords

For example, where `redis` was the owning chart, and the other charts need to reference the `redis` password.

The owning chart should define its password secret like the following:

```
password:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same password secret like the following:

```
redis:
  password:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

### Auth Tokens

The owning chart should define its authToken secret like the following:

```
authToken:
  secret: <secret name>
  key: <key name inside the secret to fetch>
```

Other charts should share the same password secret like the following:

```
gitaly:
  authToken:
    secret: <secret name>
    key: <key name inside the secret to fetch>
```

For example, where `gitaly` was the owning chart, and the other charts need to reference the `gitaly` authToken.

## Developing template helpers

A charts template helpers are located in `templates/_helpers.tpl`. These contain the [named templates](https://docs.helm.sh/chart_template_guide/#declaring-and-using-templates-with-define-and-template)
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

## Handling configuration deprecations

There are times in a development where changes in behavior require a functionally breaking change. We try to avoid such changes, but some items can not be handled without such a change.

To handle this, we have implemented the [deprecations template][]. This template is designed to recogonize properties that need to be replaced or relocated, and inform the user of the actions they need to take. This template will compile all messages into a list, and then cause the deployment to stop via a `fail` call. This provides a method to inform the user at the same time as preventing the deployment the chart in a broken or unexpected state.

See the documentation of the [deprecations template][] for further information on the design, functionality, and how to add new deprecations.

[deprecations template]: deprecations.md
