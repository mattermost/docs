# Gitlab version mappings

The table below maps some of the key previous chart versions and GitLab versions.

| Chart version | GitLab version |
|---------------|----------------|
| 2.2.6 | 12.0.9 |
| 2.2.5 | 12.2.4 |
| 2.2.4 | 12.2.4 |
| 2.2.3 | 12.2.4 |
| 2.2.1 | 12.2.1 |
| 2.2.0 | 12.2.0 |
| 2.1.7 | 12.1.6 |
| 2.1.6 | 12.1.4 |
| 2.1.5 | 12.1.4 |
| 2.1.4 | 12.1.4 |
| 2.1.3 | 12.1.3 |
| 2.1.2 | 12.1.2 |
| 2.1.1 | 12.1.1 |
| 2.1.0 | 12.1.0 |
| 2.0.5 | 12.0.6 |
| 2.0.4 | 12.0.4 |
| 2.0.3 | 12.0.3 |
| 2.0.2 | 12.0.2 |
| 2.0.1 | 12.0.1 |
| 2.0.0 | 12.0.0 |
| 1.9.8 | 11.11.8 |
| 1.9.7 | 11.11.7 |
| 1.9.5 | 11.11.4 |
| 1.9.4 | 11.11.3 |
| 1.9.3 | 11.11.3 |
| 1.9.2 | 11.11.2 |
| 1.9.1 | 11.11.1 |
| 1.9.0 | 11.11.0 |
| 1.8.4 | 11.10.4 |
| 1.8.3 | 11.10.3 |
| 1.8.2 | 11.10.2 |
| 1.8.1 | 11.10.1 |
| 1.8.0 | 11.10.0 |
| 1.7.5 | 11.9.8 |
| 1.7.4 | 11.9.7 |
| 1.7.3 | 11.9.6 |
| 1.7.2 | 11.9.4 |
| 1.7.1 | 11.9.1 |
| 1.7.0 | 11.9.0 |
| 1.6.3 | 11.8.3 |
| 1.6.2 | 11.8.2 |
| 1.6.1 | 11.8.1 |
| 1.6.0 | 11.8.0 |
| 1.5.3 | 11.7.5 |
| 1.5.2 | 11.7.4 |
| 1.5.1 | 11.7.3 |
| 1.5.0 | 11.7.0 |
| 1.4.4 | 11.6.5 |
| 1.4.3 | 11.6.4 |
| 1.4.2 | 11.6.3 |
| 1.4.1 | 11.6.2 |
| 1.4.0 | 11.6.0 |
| 1.3.4 | 11.5.4 |
| 1.3.3 | 11.5.3 |
| 1.3.2 | 11.5.2 |
| 1.3.1 | 11.5.1 |
| 1.3.0 | 11.5.0 |
| 1.2.6 | 11.4.7 |
| 1.2.5 | 11.4.6 |
| 1.2.4 | 11.4.5 |
| 1.2.3 | 11.4.4 |
| 1.2.2 | 11.4.3 |
| 1.2.1 | 11.4.2 |
| 1.2.0 | 11.4.0 |
| 1.1.6 | 11.3.6 |
| 1.1.5 | 11.3.5 |
| 1.1.4 | 11.3.4 |
| 1.1.3 | 11.3.3 |
| 1.1.2 | 11.3.2 |
| 1.1.1 | 11.3.1 |
| 1.1.0 | 11.3.0 |
| 1.0.2 | 11.2.3 |
| 1.0.1 | 11.2.1 |
| 1.0.0 | 11.2.0 |
| 0.3.5 | 11.1.4 |
| 0.3.4 | 11.1.4 |
| 0.3.3 | 11.1.3 |
| 0.3.2 | 11.1.2 |
| 0.3.1 | 11.1.1 |
| 0.3.0 | 11.1.0 |
| 0.2.4 | 11.0.4 |
| 0.2.3 | 11.0.3 |
| 0.2.2 | 11.0.2 |
| 0.2.1 | 11.0.1 |
| 0.2.0 | 11.0.0 |

To see the full list, you can issue the following command with helm:

```
helm repo add gitlab https://charts.gitlab.io/
helm search -l gitlab/gitlab
```

You will receive an output similar to:

```
NAME                    CHART VERSION   APP VERSION
gitlab/gitlab           1.5.0           11.7.0
gitlab/gitlab           1.4.4           11.6.5
gitlab/gitlab           1.4.3           11.6.4
gitlab/gitlab           1.4.2           11.6.3
gitlab/gitlab           1.4.1           11.6.2
```

Read more about our charts versioning [here](../development/release.md#chart-versioning)

Check the [releases documentation](../releases/index.md) for information on important releases,
and see the [changelog](https://gitlab.com/gitlab-org/charts/gitlab/blob/master/CHANGELOG.md) for the full details on any release.
