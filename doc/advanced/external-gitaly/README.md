# Configure this chart with External Gitaly

This document intends to provide documentation on how to configure this Helm chart with an external Gitaly service.

We'll make use of the [Omnibus GitLab][] package for Ubuntu. This package provides versions of the services that are guaranteed to be compatible with the charts' services.

## Set up the VM

### Create a Virtual Machine
Create a VM on your provider of choice, or locally. This was tested with VirtualBox, KVM, and Bhyve. Ensure that the Gitaly instance will be reachable from the cluster. Be sure firewall policies are in place to allow traffic.

### Install and Configure Ubuntu Server

Install Ubuntu Server onto the VM that you have created. Ensure that `openssh-server` is installed, and that all packages are up to date. Configure networking and a hostname. Make note of the hostname/IP, and ensure it is both resolvable and reachable from your Kubernetes cluster.

### Install Omnibus GitLab

Follow the installation instructions for [Omnibus GitLab][]. When you perform the package installation, **_do not_** provide the `EXTERNAL_URL=` value. We do not want automatic configuration to occur, as we'll provide a very specific configuration in the next step.

### Configure Omnibus GitLab

We'll create a minimal `gitlab.rb` file to be placed at `/etc/gitlab/gitlab.rb`. We'll intentionally _not_ use [Roles](https://docs.gitlab.com/omnibus/roles/README.html), so that we are _very_ explicit about what we want on this node. The contents of that file are below.

_**NOTE**: The values below should be replaced_
- `AUTH_TOKEN` should be replaced with the value in the [`gitaly-secret` secret](../../installation/secrets.md#gitaly-secret)
- `GITLAB_URL` should be replaced with the URL of the GitLab instance
- `SHELL_TOKEN` should be replaced with the value in the [`gitlab-shell-secret` secret](../../installation/secrets.md#gitlab-shell-secret)

```Ruby
## Gitaly
gitaly['enable'] = true
gitaly['auth_token'] = 'AUTH_TOKEN'
gitaly['listen_addr'] = '0.0.0.0:8075'

## Needed to get user made/managed
gitlab_rails['enable'] = true
gitlab_rails['auto_migrate'] = false
## Needed to have GitLab Shell connect to GitLab API
gitlab_rails['internal_api_url'] = 'GITLAB_URL'
gitlab_shell['secret_token'] = 'SHELL_TOKEN'

## Disable everything else
sidekiq['enable'] = false
unicorn['enable'] = false
registry['enable'] = false
gitlab_workhorse['enable'] = false
nginx['enable'] = false
prometheus['enable'] = false
prometheus_monitoring['enable'] = false
postgresql['enable'] = false
redis['enable'] = false
```

After creating `gitlab.rb`, we'll reconfigure the package with `gitlab-ctl reconfigure`. Once the task has completed, check the running processes with `gitlab-ctl status`. The output should appear as such:
```
# gitlab-ctl status
run: gitaly: (pid 30562) 77637s; run: log: (pid 30561) 77637s
run: logrotate: (pid 4856) 1859s; run: log: (pid 31262) 77460s
```

## Configure the Chart

To connect the charts' services to the external databases, we'll need to set a few items. [external-gitaly-snippet.yaml](external-gitaly-snippet.yaml) is a subset of items that show minimal configuration changes as opposed to using the `gitaly` chart to provide Gitaly services. In summary, disable the `gitaly` chart and the Gitaly service it provides, and point the other services to the external one.

Set the `host` value to the FQDN/IP of the server/vm.

Pass [external-gitaly-snippet.yaml](external-gitaly-snippet.yaml) values to `helm` with the `-f` flag: `helm <command> [options] -f external-gitaly-snippet.yaml`.

## Deploy!

Once you have a complete configuration in YAML, provide that to the Helm command.

`helm install . -f external-gitaly-snippet.yaml --set ...`

[Omnibus GitLab]: https://about.gitlab.com/installation/#ubuntu
