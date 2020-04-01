.. _use-kubernetes-mattermost:

Using Mattermost Operator Functionality
======================================

Rolling Upgrades
----------------

The Mattermost Kubernetes Operator supports rolling upgrades so you can upgrade
your Mattermost deployment with zero downtime. This process
requires at least two replicas as a rolling upgrade cannot be performed if there is only one pod.
Replicas are created when a user count is selected and exceeds 100.

New Mattermost releases are announced via our community server, as well as social media and email.

**Performing rolling upgrades**

1. Log in to your Kubernetes instance.
2. Open the ``mattermost-installation.yaml`` manifest (the one created during installation).
3. Update the ``spec.version`` value to the new version.
4. Save the changes.

Apply the changes with kubectl using

.. code-block:: sh

  $ kubectl apply -n mattermost -f /path/to/mattermost-installation.yaml

The operator initiates a job in the Kubernetes cluster and once migration is complete the pods are restarted. If necessary,
a database migration is also performed.

To view information about the running job, use

.. code-block:: sh

  $ kubectl -n mattermost get jobs

At least one pod is available at all times and once all pods are restarted with the new version the upgrade is complete.

To view the status of the pods and to confirm their state, use

.. code-block:: sh

  $ kubectl -n mattermost get pods

The *STATUS* of the pods should be running/ready, with an *AGE* of 10-15 seconds.

Blue-green Deployments
----------------------

Blue-green deployments can reduce downtime and increase stability during automated tasks in a production environment.
This technique entails running two identical production environments in tandem, with one acting as a
live environment and one as an idle environment.

An upgrade can be rolled out to the idle environment (“blue”) while the other (“green”) is the production environment.
Once the upgrade has been successfully rolled out, all traffic can be switched from “green” to “blue”.

**Note:** Blue-green can be run on a permanent basis but utilizes more resources in the Kubernetes cluster than normal deployments.

**Configuring Blue-green Deployments**

Open the ``mattermost-installation.yaml`` file and add ``blueGreen`` under ``spec``.

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

To access the new ingresses, create CNAME or IP address records in your DNS registration service for the ``ingressName`` in your
manifest, pointing to the address you just copied.

For example, on AWS you would do this within a hosted zone in Route 53. Use the required ``ingressName`` URL in your browser to directly access blue or green at any time.

To update the version of blue or green, change the version in the manifest to
match the current version or the version you’d like to deploy. This
change (regardless of which is the ``productionDeployment``) initiates a database migration.
The schema is backwards and forwards compatible across minor versions (from 5.9 onwards) and will not disrupt the production deployment.
However, it will auto-upgrade the database.


Canary Builds
-------------

A canary build is used to test an experimental or untested build. It's similar to a blue-green deployment in that multiple environments
are run simultaneously. However, where blue-green deployments have different URLs, canary builds are set up to direct a random segment of users
to the test environment. Users are not explicitly aware that they're on the canary build environment.

The redirect is managed with a cookie, which is valid for 24 hours.

The Mattermost Operator currently allows segmenting by percentage (i.e., splitting the user pool between production and the canary build). In
future releases segmentation options will include teams and individual users.

Configuring canary builds requires an update to the ``mattermost-installation.yaml`` file and the addition of a plugin via System Console. Before
proceeding, first download the `Mattermost Plugin for Canary Deployments <https://github.com/mattermost/mattermost-plugin-canary/releases>`__.

**Configuring Canary Builds**

Open the ``mattermost-installation.yaml`` file and add the following under ``spec``.

.. code-block:: yaml

    canary:
    enable: true
    Deployment:
      version: 5.15.0
      image: mattermost/mattermost-enterprise-edition

Next, navigate to **System Console > Plugin Management**, enable plugins, and upload the Mattermost Canary Plugin. Once uploaded, refresh
your page and then select **Settings** from the Canary plugin modal. Enter the percentage of users you'd like to direct to the canary build.

Once complete, navigate to your Mattermost instance and open the Developer Tools menu in your browser. The entry for the Mattermost instance
will display *always* or *never* depending on the segment you've been allocated to.

You can disable canary builds in the ``mattermost-installation.yaml`` file by changing the ``enable`` field to ``false``.
