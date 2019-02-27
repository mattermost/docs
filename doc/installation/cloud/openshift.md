# Installing GitLab on OKD (OpenShift Origin)

This document describes a basic outline of how to get GitLab up and running on
an OKD instance using the official Helm charts.

NOTE: **Note:**:
This guide has been tested only on Openshift Origin 3.11.0 and is not guaranteed
to work on other versions, or SaaS offering of OpenShift, OpenShift Online.
If you face any problems in installing or configuring GitLab by following this
guide, open issues at our [issue tracker](https://gitlab.com/charts/gitlab/issues).
Feedback and Merge Requests to improve this document are welcome.

## Known issues

The following issues are known and expected to be applicable to GitLab
installations on OpenShift:

1. Requirement of `anyuid` scc:

    - Different components of GitLab, like Sidekiq, unicorn, etc., use UID 1000 to run services.
    - PostgreSQL chart runs the service as the `root` user.
    - [Issue #752](https://gitlab.com/charts/gitlab/issues/752) is open to investigate more on fixing this.

1. If using `hostpath` volumes, the persistent volume directories in host need to
   be given `0777` permissions, for granting all users access to the volumes.
1. Git operations over SSH are not supported by OpenShift's built-in router.
   [Issue #892](https://gitlab.com/charts/gitlab/issues/892) is open to
   investigate more on fixing this.
1. GitLab Registry is known not to work with OpenShift's built-in router.
   [Issue #893](https://gitlab.com/charts/gitlab/issues/893) is open to
   investigate more on fixing this.
1. Automatic issuing of SSL certificates from Let's Encrypt will not work with
   OpenShift router. We suggest [using your own certificates](../tls.md#option-2-use-your-own-wildcard-certificate).
   [Issue #894](https://gitlab.com/charts/gitlab/issues/894) is open to
   investigate more on fixing this.

## Prerequisite steps

1. Refer to [official documentation](https://www.okd.io/download.html#oc-platforms)
   to install and configure a cluster.
1. Run `oc cluster status` and confirm the cluster is running:

    ```bash
    oc cluster status
    ```

    The output should be similar to:

    ```
    Web console URL: https://gitlab.example.com:8443/console/

    Config is at host directory
    Volumes are at host directory
    Persistent volumes are at host directory /home/okduser/openshift/openshift.local.clusterup/openshift.local.pv
    Data will be discarded when cluster is destroyed
    ```

    Note the location of Persistent Volumes in the host machine (in the above example
    `/home/okduser/openshift/openshift.local.clusterup/openshift.local.pv`).
    The following command expects that path in the `PV_HOST_DIRECTORY` environment variable.

1. Modify the permissions of PV directories (replace the path in the following
   command by the value from above):

    ```bash
    sudo chmod -R a+rwx ${PV_HOST_DIRECTORY}/*
    ```

1. Switch to the system administrator user:

    ```bash
    oc login -u system:admin
    ```

1. Add `anyuid` scc to the system user:

    ```bash
    oc adm policy add-scc-to-group anyuid system:authenticated
    ```

    CAUTION: **Warning**:
    This setting will be applied across all namespaces and will result in Docker
    images that does not explicitly specify USER running as `root` user.
    [Issue #895](https://gitlab.com/charts/gitlab/issues/895) is open to
    document different service accounts required and to describe adding scc to
    those service accounts only, so the impact can be limited.

1. Create the service account and `rolebinding` for RBAC and [install Tiller](../tools.md#helm):

    ```bash
    kubectl create -f https://gitlab.com/charts/gitlab/raw/master/doc/installation/examples/rbac-config.yaml
    helm init --service-account tiller
    ```

## Next Steps

Continue with the [installation of the chart](../deployment.md) once you have
the cluster up and running, and the static IP and DNS entry ready.

Before doing so take note of the following changes from the normal chart
installation procedure:

1. We will be using OpenShift's built-in router, and hence need to disable
   the nginx-ingress service that is included in the charts. Pass the following
   flag to the `helm install` command:

      ```bash
      --set nginx-ingress.enabled=false
      ```

1. Since built-in Registry is known not to work with OpenShift using the Helm
   charts, disable the registry service. Pass the following flag to the
   `helm install` command:

      ```sh
      --set registry.enabled=false
      ```

1. [Use your own SSL certificates](../tls.md#option-2-use-your-own-wildcard-certificate)
