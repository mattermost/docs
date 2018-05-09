# Chart Documentation

Documentation on a per-chart basis contained here. Each chart is documented individually, and laid in a structure that matches the
[charts](../../charts/) directory structure.

Non-GitLab components are packaged and documented on the top level. GitLab component services are documented under the [GitLab](gitlab/) chart & subfolder.

## Global Settings

There are some common global settings that apply to multiple charts. See the [Globals Documentation](globals.md) for details
on the different global configuration.

## Charts:
- [NGINX](nginx/README.md)
- [Redis](redis/README.md)
- [Minio](minio/README.md)
- [Registry](registry/README.md)
- GitLab/[sidekiq](gitlab/sidekiq/README.md)
- GitLab/[gitlab-shell](gitlab/gitlab-shell/README.md)
- GitLab/[gitaly](gitlab/gitaly/README.md)
- GitLab/[unicorn](gitlab/unicorn/README.md)
- GitLab/[migrations](gitlab/migrations/README.md)
