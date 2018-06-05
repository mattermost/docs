# Setup standalone Redis

The instructions here make use of the [Omnibus GitLab][] package for Ubuntu. This package provides versions of the services that are guaranteed to be compatible with the charts' services.

## Create VM with Omnibus GitLab

Create a VM on your provider of choice, or locally. This was tested with VirtualBox, KVM, and Bhyve.
Ensure that the instance is reachable from the cluster.

Install Ubuntu Server onto the VM that you have created. Ensure that `openssh-server` is installed, and that all packages are up to date.
Configure networking and a hostname. Make note of the hostname/IP, and ensure it is both resolvable and reachable from your Kubernetes cluster.
Be sure firewall policies are in place to allow traffic.

Follow the installation instructions for [Omnibus GitLab][]. When you perform the package installation, **_do not_** provide the `EXTERNAL_URL=` value. We do not want automatic configuration to occur, as we'll provide a very specific configuration in the next step.

## Configure Omnibus GitLab

Create a minimal `gitlab.rb` file to be placed at `/etc/gitlab/gitlab.rb`. Be _very_ explicit about what is enabled on this node, use the contents below.

*Note*: This example is not intended to provide [Redis HA](https://docs.gitlab.com/ee/administration/high_availability/redis.html#configuring-redis-ha).


* `REDIS_PASSWORD` should be replaced with the value in the [`gitlab-redis` secret](../../installation/secrets.md#redis-password).

```Ruby
# Listen on all addresses
redis['bind'] = '0.0.0.0'
# Set the defaul port, must be set.
redis['port'] = 6379
# Set password, as in the secret `gitlab-redis` populated in Kubernetes
redis['password'] = 'REDIS_PASSWORD'


## Disable everything else
gitlab_rails['enable'] = false
sidekiq['enable'] = false
unicorn['enable'] = false
registry['enable'] = false
gitaly['enable'] = false
gitlab_workhorse['enable'] = false
nginx['enable'] = false
prometheus_monitoring['enable'] = false
postgresql['enable'] = false
```

After creating `gitlab.rb`, we'll reconfigure the package with `gitlab-ctl reconfigure`. Once the task has completed, check the running processes with `gitlab-ctl status`. The output should appear as such:
```
# gitlab-ctl status
run: logrotate: (pid 4856) 1859s; run: log: (pid 31262) 77460s
run: redis: (pid 30562) 77637s; run: log: (pid 30561) 77637s
```

[Omnibus GitLab]: https://about.gitlab.com/installation/#ubuntu
