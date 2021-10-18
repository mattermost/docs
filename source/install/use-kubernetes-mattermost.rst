.. _use-kubernetes-mattermost:

Using Mattermost Operator Functionality
---------------------------------------

Rolling Upgrades
~~~~~~~~~~~~~~~~

The Mattermost Kubernetes Operator supports rolling upgrades, so you can upgrade
your Mattermost deployment with zero downtime. This process
requires at least two replicas as a rolling upgrade cannot be performed if there is only one pod.
Replicas are created when a user count is selected and exceeds 100.

New Mattermost releases are announced via our community server, as well as social media and email.

**Performing rolling upgrades**

1. Log in to your Kubernetes instance.
2. Open the ``mattermost-installation.yaml`` manifest (the one created during installation).
3. Update the ``spec.version`` value to the new version.
4. Save the changes.

Apply the changes with ``kubectl``:

.. code-block:: sh

  $ kubectl apply -n mattermost -f [PATH_TO_MATTERMOST_MANIFEST]

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
