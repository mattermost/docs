# Gitlab version mappings

The table below maps some of the key previous chart versions and GitLab versions.

| Chart version | GitLab version |
|---------------|----------------|
| 1.6.3 | 11.8.3 |
| 1.6.2 | 11.8.2 |
| 1.5.0 | 11.7.0 |
| 1.4.0 | 11.6.0 |
| 1.3.0 | 11.5.0 |
| 1.2.0 | 11.4.0 |
| 1.1.0 | 11.3.0 |
| 1.0.0 | 11.2.0 |
| 0.3.5 | 11.1.4 |
| 0.2.4 | 11.0.4 |


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

Read more about our charts versioning [here](https://gitlab.com/charts/gitlab/blob/master/doc/development/release.md#chart-versioning)

Check the [releases documentation](../releases/index.md) for information on important releases,
and see the [changelog](https://gitlab.com/charts/gitlab/blob/master/CHANGELOG.md) for the full details on any release.