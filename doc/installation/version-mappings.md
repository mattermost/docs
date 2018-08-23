# Gitlab version mappings

The table below maps some of the key previous chart versions and GitLab versions.

| Chart version | GitLab version |
|---------------|----------------|
| 1.0.0         | 11.2.0         |
| 0.3.5        	| 11.1.4     	 |
| 0.2.4        	| 11.0.4     	 |


To see the full list, you can issue the following command with helm:

```
helm repo add gitlab https://charts.gitlab.io/
helm search -l gitlab/gitlab
```

Read more about our charts versioning [here](https://gitlab.com/charts/gitlab/blob/master/doc/development/release.md#chart-versioning)

Check the [releases documentation](../releases/README.md) for information on important releases,
and see the [changelog](https://gitlab.com/charts/gitlab/blob/master/CHANGELOG.md) for the full details on any release.   
