# GitLab Geo

GitLab Geo provides the ability to have read-only, geographically distributed
application deployments.

While external database services can be used, these documents currently focus on
the use of the [Omnibus GitLab](https://docs.gitlab.com/omnibus) for PostgreSQL in order to provide the
most platform agnostic guide, and make use of the automation included within `gitlab-ctl`.

## Requirements

In order to use GitLab Geo with the GitLab Helm chart, the following requirements must be met:

- The use of [external PostgreSQL](../external-db/index.md) services, as the
  PostgresSQL included with the chart is not exposed to outside networks, or currently
  have WAL support required for replication.
- The supplied database must:
  - Support replication.
  - The primary database must reachable by the primary application deployment,
    and all secondary database nodes (for replication).
  - Secondary databases only need to be reachable by the secondary application
    deployments.
  - Support SSL between primary and secondary.
- The primary application instance must be reachable via HTTPS by all secondary instances.
  Secondary application instances must be accessible to the primary instance via HTTPS.

## Overview

This guide will use 2 Omnibus GitLab instances, configuring only the PostgreSQL
services needed, and 2 deployments of the GitLab Helm chart. It is intended to be
the _minimal_ required configuration. This documentation does not currently
include SSL from application to database, support for other database providers, or
promoting a secondary instance to primary.

The outline below should be followed in order:

1. [Setup Omnibus instances](#setup-omnibus-instances)
1. [Setup Kubernetes clusters](#setup-kubernetes-clusters)
1. [Collect information](#collect-information)
1. [Configure Primary database](#configure-primary-database)
1. [Deploy chart as Geo Primary](#deploy-chart-as-geo-primary)
1. [Set the Geo primary instance](#set-the-geo-primary-instance)
1. [Configure Secondary database](#configure-secondary-database)
1. [Copy secrets from primary cluster to secondary cluster](#copy-secrets-from-the-primary-cluster-to-the-secondary-cluster)
1. [Deploy chart as Geo Secondary](#deploy-chart-as-geo-secondary)
1. [Add Secondary Geo instance via Primary](#add-secondary-geo-instance-via-primary)
1. [Confirm Operational Status](#confirm-operational-status)

## Setup Omnibus instances

For this process, two instances are required. One will be the Primary, the other
the Secondary. You may use any provider of machine infrastructure, on-premise or
from a cloud provider.

Bear in mind that communication is required:

- Between the two database instances for replication.
- Between each database instance and their respective Kubernetes deployments:
  - Primary will need to expose TCP port `5432`.
  - Secondary will need to expose TCP ports `5432` & `5431`.

Install an [operating system supported by Omnibus GitLab][og-os], and then
[install the Omnibus GitLab][og-install] onto it. Do not provide the
`EXTERNAL_URL` environment variable when installing, as we'll provide a minimal
configuration file before reconfiguring the package.

Once you have installed the operating system, and the GitLab package, configuration
can be created for the services that will be used. Before we do that, information
must be collected.

[og-os]: https://docs.gitlab.com/ee/install/requirements.html#operating-systems
[og-install]: https://about.gitlab.com/install/

## Setup Kubernetes clusters

For this process, two Kubernetes clusters should be used. These can be from any
provider, on-premise or from a cloud provider.

Bear in mind that communication is required:

- To the respective database instances:
  - Primary outbound to TCP `5432`.
  - Secondary outbound to TCP `5432` and `5431`.
- Between both Kubernetes Ingress via HTTPS.

Each cluster that is provisioned should have:

- Enough resources to support a base-line installation of these charts.
- Access to persistent storage:
  - Minio not required if using [external object storage][ext-object]
  - Gitaly not required if using [external Gitaly][ext-gitaly]
  - Redis not required if using [external Redis][ext-redis]

[ext-object]: ../external-object-storage/index.md
[ext-gitaly]: ../external-gitaly/index.md
[ext-redis]: ../external-redis/index.md

## Collect information

To continue with the configuration, the following information needs to be
collected from the various sources. Collect these, and make notes for use through
the rest of this documentation.

- Primary database:
  - IP address
  - hostname (optional)
- Secondary database:
  - IP address
  - hostname (optional)
- Primary cluster:
  - IP addresses of nodes
- Secondary cluster:
  - IP addresses of nodes
- Database Passwords (_must  pre-decide the password(s)_)
  - `gitlab` (used in `postgresql['sql_user_password']`, `global.psql.password`)
  - `gitlab_geo` (used in `geo_postgresql['sql_user_password']`, `global.geo.psql.password`)
  - `gitlab_replicator` (needed for replication)
- Your GitLab license file

The `gitlab` and `gitlab_geo` database user passwords will need to exist in two
forms: bare password, and PostgreSQL hashed password. To obtain the hashed form,
perform the following commands on one of the Omnibus instances, which will ask
you to enter, and confirm the password before outputting an appropriate hash
value for you to make note of.

1. `gitlab-ctl pg-password-md5 gitlab`
1. `gitlab-ctl pg-password-md5 gitlab_geo`

## Configure Primary database

_This section will be performed on the Primary Omnibus GitLab instance._

To configure the Primary database instance's Omnibus GitLab, we'll work from
this example configuration.

```ruby
### Geo Primary
external_url 'http://gitlab-primary.example.com'
roles ['geo_primary_role']
gitlab_rails['auto_migrate'] = false
## turn off everything but the DB
sidekiq['enable']=false
unicorn['enable']=false
gitlab_workhorse['enable']=false
nginx['enable']=false
geo_logcursor['enable']=false
grafana['enable']=false
gitaly['enable']=false
redis['enable']=false
prometheus_monitoring['enable'] = false
## Configure the DB for network
postgresql['enable'] = true
postgresql['listen_address'] = '0.0.0.0'
postgresql['sql_user_password'] = 'gitlab_user_password_hash'
# !! CAUTION !!
# This list of CIDR addresses should be customized
# - primary application deployment
# - secondary database instance(s)
postgresql['md5_auth_cidr_addresses'] = ['0.0.0.0/0']
```

We need to replace several items:

- `external_url` must be updated to reflect the host name of our Primary
instance.
- `gitlab_user_password_hash` must be replaced with the hashed form of the
`gitlab` password.
- `postgresql['md5_auth_cidr_addresses']` can be update to be a list of
explicit IP addresses, or address blocks in CIDR notation.

The `md5_auth_cidr_addresses` should be in the form of
`[ '127.0.0.1/24', '10.41.0.0/16']`. It is important to include `127.0.0.1` in
this list, as the automation within Omnibus GitLab will connect using this. The
addresses in this list should include the IP address (not hostname) of your
Secondary database, and all nodes of your primary Kubernetes cluster. This _can_
be left as `['0.0.0.0/0']`, however _it is not best practice_.

Once the configuration above is prepared:

1. Place the content into `/etc/gitlab/gitlab.rb`
1. Run `gitlab-ctl reconfigure`
1. Run `gitlab-ctl set-replication-password` in order to set the password for
the `gitlab_replicator` user.
1. Retrieve the Primary database server's public certificate, this will be needed
for the Secondary database to be able to replicate.
    1. `cat ~gitlab-psql/data/server.crt`
    1. **Store this output.**

## Deploy chart as Geo Primary

_This section will be performed on the Primary Kubernetes cluster._

In order to deploy this chart as a Geo Primary, we'll start [from this example configuration](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/geo/primary.yaml).

```yaml
### Geo Primary
global:
  # See docs.gitlab.com/charts/charts/globals
  # Configure host & domain
  hosts:
    domain: example.com
  # configure DB connection
  psql:
    host: geo-1.db.example.com
    port: 5432
    password:
      secret: geo
      key: postgresql-password
  # configure geo (primary)
  geo:
    enabled: true
    role: primary
# External DB, disable
postgresql:
  install: false
```

1. We'll need to create a secret containing the database password, for the
chart to consume. Replace `PASSWORD` below with the password for the `gitlab`
database user.

   ```sh
   kubectl create secret generic geo --from-literal=postgresql-password=PASSWORD
   ```

1. Update the configuration to reflect the correct values for:

   - [global.hosts.domain](../../charts/globals.md#configure-host-settings)
   - [global.psql.host](../../charts/globals.md#configure-postgresql-settings)
   - Also configure any additional settings, such as:
     - [Configuring SSL/TLS](../../installation/deployment.html#tls-certificates)
     - [Using external Redis][ext-redis]
     - [using external Object Storage][ext-object]

1. Deploy the chart using this configuration

   ```sh
   helm upgrade --install gitlab-geo gitlab/gitlab --namespace gitlab -f primary.yaml
   ```

1. Wait for the deployment to complete, and the application to come online. Once
the application is reachable, login.

1. Login to GitLab, and upload your GitLab license file by navigating to
`/admin/license`. **This step is required for Geo to function.**

## Set the Geo Primary instance

Now that the chart has been deployed, and a license uploaded, we can configure
this as the Primary instance. We will do this via the `task-runner` Pod.

1. Find the `task-runner` Pod

   ```sh
   kubectl get pods -lapp=task-runner --namespace gitlab
   ```

1. Run `gitlab-rake geo:set_primary_node` with `kubectl exec`

   ```sh
   kubectl exec -ti gitlab-geo-task-runner-XXX -- gitlab-rake geo:set_primary_node
   ```

1. Check the status of Geo configuration

   ```sh
   kubectl exec -ti gitlab-geo-task-runner-XXX -- gitlab-rake gitlab:geo:check
   ```

   You should see output similar to below:

   ```
   WARNING: This version of GitLab depends on gitlab-shell 10.2.0, but you're running Unknown. Please update gitlab-shell.
   Checking Geo ...

   GitLab Geo is available ... yes
   GitLab Geo is enabled ... yes
   GitLab Geo secondary database is correctly configured ... not a secondary node
   Database replication enabled? ... not a secondary node
   Database replication working? ... not a secondary node
   GitLab Geo tracking database is configured to use Foreign Data Wrapper? ... not a secondary node
   GitLab Geo tracking database Foreign Data Wrapper schema is up-to-date? ... not a secondary node
   GitLab Geo HTTP(S) connectivity ... not a secondary node
   HTTP/HTTPS repository cloning is enabled ... yes
   Machine clock is synchronized ... Exception: getaddrinfo: Servname not supported for ai_socktype
   Git user has default SSH configuration? ... yes
   OpenSSH configured to use AuthorizedKeysCommand ... no
     Reason:
     Cannot find OpenSSH configuration file at: /assets/sshd_config
     Try fixing it:
     If you are not using our official docker containers,
     make sure you have OpenSSH server installed and configured correctly on this system
     For more information see:
     doc/administration/operations/fast_ssh_key_lookup.md
   GitLab configured to disable writing to authorized_keys file ... yes
   GitLab configured to store new projects in hashed storage? ... yes
   All projects are in hashed storage? ... yes

   Checking Geo ... Finished
   ```

   - Don't worry about `Exception: getaddrinfo: Servname not supported for ai_socktype`, as Kubernetes containers will not have access to the host clock. _This is OK_.
   - `OpenSSH configured to use AuthorizedKeysCommand ... no` _is expected_. This
   Rake task is checking for a local SSH server, which is actually present in the
   `gitlab-shell` chart, deployed elsewhere, and already configured appropriately.

## Configure Secondary database

_This section will be performed on the Secondary Omnibus GitLab instance._

To configure the Secondary database instance's Omnibus GitLab, we'll work from
this example configuration.

```ruby
### Geo Secondary
external_url 'http://gitlab-secondary.example.com'
roles ['geo_secondary_role']
gitlab_rails['auto_migrate'] = false
geo_secondary['auto_migrate'] = false
## turn off everything but the DB
sidekiq['enable']=false
unicorn['enable']=false
gitlab_workhorse['enable']=false
nginx['enable']=false
geo_logcursor['enable']=false
grafana['enable']=false
gitaly['enable']=false
redis['enable']=false
prometheus_monitoring['enable'] = false
## Configure the DBs for network
postgresql['enable'] = true
postgresql['listen_address'] = '0.0.0.0'
postgresql['sql_user_password'] = 'gitlab_user_password_hash'
# !! CAUTION !!
# This list of CIDR addresses should be customized
# - secondary application deployment
# - secondary database instance(s)
postgresql['md5_auth_cidr_addresses'] = ['0.0.0.0/0']
geo_postgresql['listen_address'] = '0.0.0.0'
geo_postgresql['sql_user_password'] = 'gitlab_geo_user_password_hash'
# !! CAUTION !!
# This list of CIDR addresses should be customized
# - secondary application deployment
# - secondary database instance(s)
geo_postgresql['md5_auth_cidr_addresses'] = ['0.0.0.0/0']
## Settings so we can automatically configure the FDW
geo_secondary['db_fdw'] = true
gitlab_rails['db_password']='gitlab_user_password'
```

We need to replace several items:

- `external_url` must be updated to reflect the host name of our Secondary
instance.
- `gitlab_user_password_hash` must be replaced with the hashed form of the
`gitlab` password.
- `postgresql['md5_auth_cidr_addresses']` should be updated to be a list of
explicit IP addresses, or address blocks in CIDR notation.
- `gitlab_geo_user_password_hash` must be replaced with the hashed form of the
`gitlab_geo` password.
- `geo_postgresql['md5_auth_cidr_addresses']` should be updated to be a list of
explicit IP addresses, or address blocks in CIDR notation.
- `gitlab_user_password` must be updated, and is used here to allow Omnibus Gitlab
to automate the configuration of Foreign Data Wrappers in PostgreSQL.

The `md5_auth_cidr_addresses` should be in the form of
`[ '127.0.0.1/24', '10.41.0.0/16']`. It is important to include `127.0.0.1` in
this list, as the automation within Omnibus GitLab will connect using this. The
addresses in this list should include the IP addresses of all nodes of your
Secondary Kubernetes cluster. This _can_ be left as `['0.0.0.0/0']`, however
_it is not best practice_.

Once the configuration above is prepared:

1. Check TCP connectivity to the **primary** node's PostgreSQL server:

   ```sh
   openssl s_client -connect <primary_node_ip>:5432 </dev/null
   ```

   The output should show the following:

   ```
   CONNECTED(00000003)
   write:errno=0
   ```

   NOTE: **Note:**
   If this step fails, you may be using the wrong IP address, or a firewall may
   be preventing access to the server. Check the IP address, paying close
   attention to the difference between public and private addresses and ensure
   that, if a firewall is present, the **secondary** node is permitted to connect
   to the **primary** node on port 5432.

1. Place the content into `/etc/gitlab/gitlab.rb`
1. Run `gitlab-ctl reconfigure`
1. Place the Primary database's certificate content from above into `primary.crt`
1. Set up PostgreSQL TLS verification on the **secondary** node:

   Install the `primary.crt` file:

   ```sh
   install \
      -D \
      -o gitlab-psql \
      -g gitlab-psql \
      -m 0400 \
      -T primary.crt ~gitlab-psql/.postgresql/root.crt
   ```

   PostgreSQL will now only recognize that exact certificate when verifying TLS
   connections. The certificate can only be replicated by someone with access
   to the private key, which is **only** present on the **primary** node.

1. Test that the `gitlab-psql` user can connect to the **primary** node's database
   (the default Omnibus database name is gitlabhq_production):

   ```sh
   sudo \
      -u gitlab-psql /opt/gitlab/embedded/bin/psql \
      --list \
      -U gitlab_replicator \
      -d "dbname=gitlabhq_production sslmode=verify-ca" \
      -W \
      -h <primary_node_ip>
   ```

   When prompted enter the password collected earlier for the
   `gitlab_replicator` user. If all worked correctly, you should see
   the list of **primary** node's databases.

   A failure to connect here indicates that the TLS configuration is incorrect.
   Ensure that the contents of `~gitlab-psql/data/server.crt` on the **primary** node
   match the contents of `~gitlab-psql/.postgresql/root.crt` on the **secondary** node.

1. Reconfigure again, which will configure the Foreign Data Wrapper support.

   ```sh
   gitlab-ctl reconfigure
   ```

1. Replicate the databases. Replace `PRIMARY_DATABASE_HOST` with the IP or hostname
of your Primary database instance.

   ```sh
   gitlab-ctl replicate-geo-database --slot-name=geo_2 --host=PRIMARY_DATABASE_HOST
   ```

1. After replication has finished, we must reconfigure the Omnibus GitLab one last time
   to ensure `pg_hba.conf` is correct for the secondary.

   ```sh
   gitlab-ctl reconfigure
   ```

## Copy secrets from the primary cluster to the secondary cluster

We now need to copy a few secrets from the Primary Kubernetes deployment to the
Secondary Kubernetes deployment.

- gitlab-geo-gitlab-shell-host-keys
- gitlab-geo-rails-secret

1. Change your `kubectl` context to that of your Primary.
1. Collect these secrets from the Primary deployment

  ```sh
  kubectl get -n gitlab -o yaml secret gitlab-geo-gitlab-shell-host-keys > ssh-host-keys.yaml
  kubectl get -n gitlab -o yaml secret gitlab-geo-rails-secret > rails-secrets.yaml
  ```

1. Change your `kubectl` context to that of your Secondary.
1. Apply these secrets

   ```sh
   kubectl apply -f ssh-host-keys.yaml
   kubectl apply -f rails-secrets.yaml
   ```

We'll now need to create a secret containing the database passwords. Replace the
passwords below with the appropriate values.

```sh
kubectl create secret generic geo \
   --from-literal=postgresql-password=gitlab_user_password \
   --from-literal=geo-postgresql-password=gitlab_geo_user_password
```

## Deploy chart as Geo Secondary

_This section will be performed on the Secondary Kubernetes cluster._

In order to deploy this chart as a Geo Secondary, we'll start [from this example configuration](https://gitlab.com/gitlab-org/charts/gitlab/tree/master/examples/geo/secondary.yaml).

```yaml
## Geo Secondary
global:
  # See docs.gitlab.com/charts/charts/globals
  # Configure host & domain
  hosts:
    hostSuffix: secondary
    domain: example.com
  # configure DB connection
  psql:
    host: geo-2.db.example.com
    port: 5432
    password:
      secret: geo
      key: postgresql-password
  # configure geo (secondary)
  geo:
    enabled: true
    role: secondary
    psql:
      host: geo-2.db.example.com
      port: 5431
      password:
        secret: geo
        key: geo-postgresql-password
# External DB, disable
postgresql:
  install: false
```

1. Update the configuration to reflect the correct values for:

   - [global.hosts.domain](../../charts/globals.md#configure-host-settings)
   - [global.psql.host](../../charts/globals.md#configure-postgresql-settings)
   - [global.geo.psql.host](../../charts/globals.md#configure-postgresql-settings)
   - Also configure any additional settings, such as:
     - [Configuring SSL/TLS](../../installation/deployment.html#tls-certificates)
     - [Using external Redis][ext-redis]
     - [using external Object Storage][ext-object]

1. Deploy the chart using this configuration

   ```sh
   helm upgrade --install gitlab-geo gitlab/gitlab --namespace gitlab -f secondary.yaml
   ```

1. Wait for the deployment to complete. Watch for the `task-runner` Pod to become `Ready`.
   **Note:** The `geo-logcursor` Pod _will not start properly_ until further configuration
   steps are completed, as these configure the database it uses.

We now need to configure the Geo database, via the `task-runner` Pod.

1. Find the `task-runner` Pod

   ```sh
   kubectl get pods -lapp=task-runner --namespace gitlab
   ```

1. Attach to the Pod with `kubectl exec`

   ```sh
   kubectl exec -ti gitlab-geo-task-runner-XXX -- bash -l
   ```

1. Populate the Geo database

   ```sh
   gitlab-rake geo:db:setup
   ```

1. Refresh the foreign tables

   ```sh
   gitlab-rake geo:db:refresh_foreign_tables
   ```

## Add Secondary Geo instance via Primary

Now that both databases are configured and applications are deployed, we must tell
the Primary that the Secondary exists:

1. Visit the **primary** instance's **Admin Area > Geo**
   (`/admin/geo/nodes`) in your browser.
1. Click the **New node** button.
1. Add the **secondary** instance. Use the full URL for the name and URL.
   **Do NOT** check the **This is a primary node** checkbox.
1. Optionally, choose which groups or storage shards should be replicated by the
   **secondary** instance. Leave blank to replicate all.
1. Click the **Add node** button.

Once added to the admin panel, the **secondary** instance will automatically start
replicating missing data from the **primary** instance in a process known as **backfill**.
Meanwhile, the **primary** instance will start to notify each **secondary** instance of any changes, so
that the **secondary** instance can act on those notifications immediately.

## Confirm Operational Status

The final step is to verify the Geo replication status on the secondary instance once fully
configured, via the `task-runner` Pod.

1. Find the `task-runner` Pod

   ```sh
   kubectl get pods -lapp=task-runner --namespace gitlab
   ```

1. Attach to the Pod with `kubectl exec`

   ```sh
   kubectl exec -ti gitlab-geo-task-runner-XXX -- bash -l
   ```

1. Check the status of Geo configuration

   ```sh
   gitlab-rake gitlab:geo:check
   ```

   You should see output similar to below:

   ```
   WARNING: This version of GitLab depends on gitlab-shell 10.2.0, but you're running Unknown. Please update gitlab-shell.
   Checking Geo ...

   GitLab Geo is available ... yes
   GitLab Geo is enabled ... yes
   GitLab Geo secondary database is correctly configured ... yes
   Database replication enabled? ... yes
   Database replication working? ... yes
   GitLab Geo tracking database is configured to use Foreign Data Wrapper? ... yes
   GitLab Geo tracking database Foreign Data Wrapper schema is up-to-date? ... yes
   GitLab Geo HTTP(S) connectivity ...
   * Can connect to the primary node ... yes
   HTTP/HTTPS repository cloning is enabled ... yes
   Machine clock is synchronized ... Exception: getaddrinfo: Servname not supported for ai_socktype
   Git user has default SSH configuration? ... yes
   OpenSSH configured to use AuthorizedKeysCommand ... no
     Reason:
     Cannot find OpenSSH configuration file at: /assets/sshd_config
     Try fixing it:
     If you are not using our official docker containers,
     make sure you have OpenSSH server installed and configured correctly on this system
     For more information see:
     doc/administration/operations/fast_ssh_key_lookup.md
   GitLab configured to disable writing to authorized_keys file ... yes
   GitLab configured to store new projects in hashed storage? ... yes
   All projects are in hashed storage? ... yes

   Checking Geo ... Finished
   ```

   - Don't worry about `Exception: getaddrinfo: Servname not supported for ai_socktype`,
   as Kubernetes containers will not have access to the host clock. _This is OK_.
   - `OpenSSH configured to use AuthorizedKeysCommand ... no` _is expected_. This
   Rake task is checking for a local SSH server, which is actually present in the
   `gitlab-shell` chart, deployed elsewhere, and already configured appropriately.
