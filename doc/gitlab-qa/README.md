# Running GitLab QA

The following documentation is meant to provide instructions for running [GitLab QA][qa]
against a deployed cloud native GitLab. These steps are performed as a part of the
[CI for this project][ci], but manual runs may be requested during development or demo.

## Preparation

### Ruby and Gem

Ensure you have a functional version of Ruby, preferably of the `2.4` branch.
Install the `gitlab-qa` Gem with `gem install gitlab-qa`, per [documentation][qa-use].

### Docker

GitLab QA makes use of Docker, as such, you will need to have an operational
installation. Ensure that the daemon is running, and can pull images.

### Network access

To run GitLab QA, you will need sustained network access to the deployed instance.
Ensure this by visiting the deployment from any browser, or via cURL.

### Configuration

Items needed for execution, which [will be set as environment variables][qa-env]:
- `GITLAB_USERNAME`: This will be `root`
- `GITLAB_PASSWORD`: This will be the password for the `root` user.
  If your deployment had the `gitlab.migrations.initialRootPassword` property set,
  use this value. This can be retrieved with `helm get values $RELEASE_NAME`.
  If you manually set this on first login, provide the correct value.
- `GITLAB_URL`: The fully-qualifies URL to the deployed instance. This should be
  in the form of `https://gitlab.domain.tld`
- `EE_LICENSE`: A string containing a GitLab EE license. This can be handled
  via `export EE_LICENSE=$(cat GitLab.gitlab-license)`

Retrieve the above items, and export them as environment variables.

## Execution

Assuming you have set the environment variables from [Prepration, Configuration](#configuration),
the following command will perform the tests against the deployed GitLab.

```
  gitlab-qa Test::Instance::Any EE nightly $GITLAB_URL
```

**NOTE:** The above command runs with _nightly_ because the containers used as a
part of this chart are currently based on nightly builds of the `master` branches
of `gitlab-(ee|ce)` repositories.

[qa]: https://gitlab.com/gitlab-org/gitlab-qa
[qa-use]: https://gitlab.com/gitlab-org/gitlab-qa#how-can-you-use-it
[qa-env]:https://gitlab.com/gitlab-org/gitlab-qa#supported-environment-variables
[ci]: https://gitlab.com/charts/gitlab/tree/master/.gitlab-ci.yml
