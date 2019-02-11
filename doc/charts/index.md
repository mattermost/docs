# Chart documentation

Documentation on a per-chart basis contained here. Each chart is documented individually, and laid in a structure that matches the
[charts](https://gitlab.com/charts/gitlab/tree/master/charts) directory structure.

Non-GitLab components are packaged and documented on the top level. GitLab component services are documented under the [GitLab](gitlab/index.md) chart & subfolder.

## Global settings

There are some common global settings that apply to multiple charts. See the [Globals Documentation](globals.md) for details
on the different global configuration.

## Charts

- [NGINX](nginx/index.md)
- [Redis](redis/index.md)
- [Minio](minio/index.md)
- [Registry](registry/index.md)
- GitLab/[sidekiq](gitlab/sidekiq/index.md)
- GitLab/[gitlab-shell](gitlab/gitlab-shell/index.md)
- GitLab/[gitaly](gitlab/gitaly/index.md)
- GitLab/[unicorn](gitlab/unicorn/index.md)
- GitLab/[migrations](gitlab/migrations/index.md)
