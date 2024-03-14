Manage the Mattermost Kubernetes Operator
=========================================

Reviewing Mattermost Resource Status
------------------------------------

After a Mattermost installation has been created with the Operator, you can review its status with the following:

.. code-block:: sh

  kubectl -n [namespace] get mattermost

The ``kubectl describe`` command can be used to obtain more information about the Mattermost server pods:

.. code-block:: sh

  kubectl -n [namespace] describe pod

Logs
----

The following command can be used to follow logs on any kubernetes pod:

.. code-block:: sh

  kubectl -n [namespace] logs -f [pod name]

If the ``-n [namespace]`` is omitted, then the default namespace of the current context is used. We recommend specifying the namespace based on your deployment.

This command can be used to review the Mattermost Operator or Mattermost server logs as needed.