.. _use-kubernetes-mattermost:

Using Mattermost Operator Functionality
======================================

Rolling Upgrades
----------------

The Mattermost Kubernetes Operator supports rolling upgrades so you can upgrade
your Mattermost deployment with zero downtime. This process
requires at least two replicas as a rolling upgrade cannot be performed if there is only one pod.
Replicas are created when a user count is selected and exceeds 100.

New Mattermost releases are announced via our community server, as well as social media.

**Performing rolling upgrades**

1. Log in to your Kubernetes instance.
2. Open the ``clusterinstallation.yaml`` manifest (the one created during installation).
3. Update the ``spec.version`` value to the new version.
4. Save the changes.

Apply the changes with kubectl using

.. code-block:: sh

  $ kubectl apply -n mattermost -f /path/to/cluster-installation.yaml

The operator initiates a job in the Kubernetes cluster and once migration is complete the pods are restarted. If necessary,
a database migration is also performed.

To view information about the running job, use

.. code-block:: sh

  $ kubectl -n mattermost get jobs

At least one pod is available at all times and once all pods are restarted with the new version the upgrade is complete.

To view the status of the pods and to confirm their state, use

.. code-block:: sh

  $ kubectl -n mattermost get pods

The *STATUS* of the pods should be running/ready, with an *AGE* of a few seconds.

Blue-green Deployments
----------------------

Blue-green deployments can reduce downtime and increase stability during automated tasks in a production environment.
This technique entails running two identical production environments in tandem, with one acting as a
live environment and one as an idle environment.

An upgrade can be rolled out to the idle environment (“blue”) while the other (“green”) is the production environment.
Once the upgrade has been successfully rolled out, all traffic can be switched from “green” to “blue”.

**Note:** Blue/green can be run on a permanent basis but utilizes more resources in the Kubernetes cluster than normal deployments.

**Configuring Blue-green Deployments**

Open the ``clusterinstallation manifest.yaml`` file and add ``blueGreen`` under ``spec``.

.. code-block:: yaml

    blueGreen:
    enable: true
    productionDeployment: blue
    blue:
      version: <version number>
      image: mattermost/mattermost-enterprise-edition
    green:
      version: <version number>
      image: mattermost/mattermost-enterprise-edition


**Parameters**

- ``enable``. When enabled it ignores the regular ``spec.version`` and ``spec.image``. When set to ``false`` it is ignored.
- ``productionDeployment``. Set to ``blue`` or ``green`` to route all users to the specified deployment.
- ``image``.  Optional. Select the image used.

When the manifest is updated, two new ingresses (proxies) are created at ``blue.yourmattermosturl.com`` and ``green.yourmattermosturl.com``.

To access the new ingresses, create CNAME or IP address records in your DNS registration service for the ``ingressName`` in your manifest, pointing to the address you just copied. For example, on AWS you would do this within a hosted zone in Route53. Use the required ``ingressName`` URL in your browser to directly access blue or green at any time.

To update the version of blue or green, change the version in the manifest to
match the current version or the version you’d like to deploy. This
change (regardless of which is the ``productionDeployment``) initiates a database migration.
The schema is backwards and forwards compatible across minor versions and will not disrupt the production deployment.

Canary Builds
-------------
