Manage the Mattermost Kubernetes Operator
=========================================

CLI commands
------------

You can manage and monitor your Mattermost installation and deployment process in the CLI, using the commands listed below.

.. code-block:: sh

  kubectl -n mattermost get jobs

.. code-block:: sh

  kubectl -n mattermost get all

Logs
----

The following command can be used for operator or mattermost pod/container logs:

.. code-block:: sh

  kubectl -n [namespace] logs -f [pod name]

If the ``-n [namespace]`` is omitted, then the default namespace of the current context is used. We recommend specifying the namespace based on your deployment.

