# Setup standalone Gitaly

The instructions here make use of the [Omnibus GitLab][] package for Ubuntu. This package provides versions of the services that are guaranteed to be compatible with the charts' services.

## Create VM with Omnibus GitLab

Create a VM on your provider of choice, or locally. This was tested with VirtualBox, KVM, and Bhyve.
Ensure that the instance is reachable from the cluster.

Install Ubuntu Server onto the VM that you have created. Ensure that `openssh-server` is installed, and that all packages are up to date.
Configure networking and a hostname. Make note of the hostname/IP, and ensure it is both resolvable and reachable from your Kubernetes cluster.
Be sure firewall policies are in place to allow traffic.

Follow the installation instructions for [Omnibus GitLab][]. When you perform the package installation, **_do not_** provide the `EXTERNAL_URL=` value. We do not want automatic configuration to occur, as we'll provide a very specific configuration in the next step.

## Configure Omnibus GitLab

Create a minimal `gitlab.rb` file to be placed at `/etc/gitlab/gitlab.rb`. Be _very_ explicit about what is enabled on this node, use the contents below based on [Running Gitaly on its own server docs](https://docs.gitlab.com/ce/administration/gitaly/#running-gitaly-on-its-own-server).

_**NOTE**: The values below should be replaced_
- `AUTH_TOKEN` should be replaced with the value in the [`gitaly-secret` secret][gitaly-secret]
- `GITLAB_URL` should be replaced with the URL of the GitLab instance
- `SHELL_TOKEN` should be replaced with the value in the [`gitlab-shell-secret` secret](../../installation/secrets.md#gitlab-shell-secret)

```Ruby
## Gitaly
gitaly['auth_token'] = 'AUTH_TOKEN'
gitaly['listen_addr'] = '0.0.0.0:8075'

## Needed to get user made/managed
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
prometheus_monitoring['enable'] = false
postgresql['enable'] = false
redis['enable'] = false
```

After creating `gitlab.rb`, reconfigure the package with `gitlab-ctl reconfigure`. Once the task has completed, check the running processes with `gitlab-ctl status`. The output should appear as such:
```
# gitlab-ctl status
run: gitaly: (pid 30562) 77637s; run: log: (pid 30561) 77637s
run: logrotate: (pid 4856) 1859s; run: log: (pid 31262) 77460s
```

[Omnibus GitLab]: https://about.gitlab.com/installation/#ubuntu
[gitaly-secret]: ../../installation/secrets.md#gitaly-secret
