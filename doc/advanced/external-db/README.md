# Configure this chart with External Database

This document intends to provide documentation on how to configure this Helm chart with external PostgreSQL service.

We'll make use of the [Omnibus GitLab][] package for Ubuntu. This package provides versions of the services that are guaranteed to be compatible with the charts' services.

## Set up the VM

### Create a Virtual Machine
Create a VM on your provider of choice, or locally. This was tested with VirtualBox, KVM, and Bhyve.

### Install and Configure Ubuntu Server

Install Ubuntu Server onto the VM that you have created. Ensure that `openssh-server` is installed, and that all packages are up to date. Configure networking and a hostname. Make note of the hostname, and ensure it is both resolvable and reachable from your Kubernetes cluster.

### Install Omnibus GitLab

Follow the installation instructions for [Omnibus GitLab][]. When you perform the package installation, **_do not_** provide the `EXTERNAL_URL=` value. We do not want automatic configuration to occur, as we'll provide a very specific configuration in the next step.

### Configure Omnibus GitLab

We'll create a minimal `gitlab.rb` file to be placed at `/etc/gitlab/gitlab.rb`. We'll intentionally _not_ use [Roles](https://docs.gitlab.com/omnibus/roles/README.html), so that we are _very_ explicit about what we want on this node. This example _is not intended_ to provide [PG HA](https://docs.gitlab.com/ee/administration/high_availability/database.html). The contents of that file are below.

*Note*: You will need to choose the password for the PostgreSQL database. Provide the unencoded value to `db_password`, and the encoded value to `sql_user_password` below. See the comments on the snippet on how to encode it.

```Ruby
## Configure PostgreSQL
postgresql['enable'] = true
# You can ding to a specific address if desired
postgresql['listen_address'] = '0.0.0.0'
# Set to approximately 1/4 of available RAM.
postgresql['shared_buffers'] = "512MB"
# This password is: `echo -n '${password}${username}' | md5sum - | cut -d' ' -f1`
# The default username is `gitlab`
postgresql['sql_user_password'] = "306a43a5ca6b2d72a89cf54dff4f1367"
# Configure the CIDRs for MD5 authentication
# These should be the smallest possible subnets of your cluster or it's gateway.
# The below example is a section of a LAN with `minikube`.
postgresql['md5_auth_cidr_addresses'] = ['192.168.100.0/12']
# Configure the CIDRs for trusted authentication (passwordless)
postgresql['trust_auth_cidr_addresses'] = ['127.0.0.1/24']

## Configure gitlab_rails
# needed for PostgreSQL user, db, pg_trgm creation
# Not needed for migrations
gitlab_rails['enable'] = true
gitlab_rails['auto_migrate'] = false
gitlab_rails['db_username'] = "gitlab"
gitlab_rails['db_password'] = "non-encoded-password"


## Disable everything else
sidekiq['enable'] = false
unicorn['enable'] = false
registry['enable'] = false
gitaly['enable'] = false
gitlab_workhorse['enable'] = false
nginx['enable'] = false
prometheus['enable'] = false
prometheus_monitoring['enable'] = false
redis['enable'] = false
```

After creating `gitlab.rb`, we'll reconfigure the package with `gitlab-ctl reconfigure`. Once the task has completed, check the running processes with `gitlab-ctl status`. The output should appear as such:
```
# gitlab-ctl status
run: logrotate: (pid 4856) 1859s; run: log: (pid 31262) 77460s
run: postgresql: (pid 30562) 77637s; run: log: (pid 30561) 77637s
```

## Configure the Chart

To connect the charts' services to the external databases, we'll need to set a few items. [external-db-snippet.yaml](external-db-snippet.yaml) is a subset of items that show minimal configuration changes as opposed to using the `omnibus` chart to provide PostgreSQL services. In summary, disable the `omnibus` chart and the PostgreSQL service it provides, and point the other services to the external one.

Set the `host` value to the FQDN of the server/vm. Set `password` value to the un-encoded password for the PostgreSQL, which you should have chosen in the previous step.

Combine [external-db-snippet.yaml](external-db-snippet.yaml) values  with [`example-config.yaml`](../../example-config.yaml) to create `external-db.yaml` used below.

## Deploy!

Once you have a complete configuration in YAML, provide that to the Helm command.

`helm install -f external-db.yaml .`

[Omnibus GitLab]: https://about.gitlab.com/installation/#ubuntu
