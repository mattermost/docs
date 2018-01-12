# Configure this chart with External Redis

This document intends to provide documentation on how to configure this Helm chart with external Redis service.

We'll make use of the [Omnibus GitLab][] package for Ubuntu. This package provides versions of the services that are guaranteed to be compatible with the charts' services.

## Set up the VM

### Create a Virtual Machine
Create a VM on your provider of choice, or locally. This was tested with VirtualBox, KVM, and Bhyve.

### Install and Configure Ubuntu Server

Install Ubuntu Server onto the VM that you have created. Ensure that `openssh-server` is installed, and that all packages are up to date. Configure networking and a hostname. Make note of the hostname, and ensure it is both resolvable and reachable from your Kubernetes cluster.

### Install Omnibus GitLab

Follow the installation instructions for [Omnibus GitLab][]. When you perform the package installation, **_do not_** provide the `EXTERNAL_URL=` value. We do not want automatic configuration to occur, as we'll provide a very specific configuration in the next step.

### Configure Omnibus GitLab

We'll create a minimal `gitlab.rb` file to be placed at `/etc/gitlab/gitlab.rb`. We'll intentionally _not_ use [Roles](https://docs.gitlab.com/omnibus/roles/README.html), so that we are _very_ explicit about what we want on this node. This example _is not intended_ to provide [Redis HA](https://docs.gitlab.com/ee/administration/high_availability/redis.html#configuring-redis-ha). The contents of that file are below.

_**NOTE**: The value of `redis-password-goes-here` should be replaced with the value in the [`gitlab-redis` secret](../../installation/secrets.md#redis-password)._


```Ruby
## Configure Redis
redis['enable'] = true
# Listen on all addresses
redis['bind'] = '0.0.0.0'
# Set the defaul port, must be set.
redis['port'] = 6379
# Set password, as in the secret `gitlab-redis` populated in Kubernetes
redis['password'] = 'redis-password-goes-here'


## Disable everything else
gitlab_rails['enable'] = false
sidekiq['enable'] = false
unicorn['enable'] = false
registry['enable'] = false
gitaly['enable'] = false
gitlab_workhorse['enable'] = false
nginx['enable'] = false
prometheus['enable'] = false
prometheus_monitoring['enable'] = false
postgresql['enable'] = false
```

After creating `gitlab.rb`, we'll reconfigure the package with `gitlab-ctl reconfigure`. Once the task has completed, check the running processes with `gitlab-ctl status`. The output should appear as such:
```
# gitlab-ctl status
run: logrotate: (pid 4856) 1859s; run: log: (pid 31262) 77460s
run: redis: (pid 30562) 77637s; run: log: (pid 30561) 77637s
```

## Configure the Chart

To connect the charts' services to the external databases, we'll need to set a few items. [external-redis-snippet.yaml](external-redis-snippet.yaml) is a subset of items that show minimal configuration changes as opposed to using the `redis` chart to provide Redis services. In summary, disable the `redis` chart and the Redis service it provides, and point the other services to the external one.

Set the `host` value to the FQDN of the server/vm.

Combine [external-redis-snippet.yaml](external-redis-snippet.yaml) values  with [`example-config.yaml`](../../example-config.yaml) to create `external-redis.yaml` used below.

## Deploy!

Once you have a complete configuration in YAML, provide that to the Helm command.

`helm install -f external-redis.yaml .`

[Omnibus GitLab]: https://about.gitlab.com/installation/#ubuntu
