:orphan:

.. _manage_kubernetes:

Managing the Mattermost Kubernetes Operator
============================================

CLI commands
------------

You can manage and monitor your Mattermost installation's installation and deployment process in the CLI, using the commands listed below.

.. code-block:: sh

    $ kubectl -n mattermost get jobs

.. code-block:: sh

    $ kubectl -n mattermost get all

Logs
----

.. code-block:: sh

    $ mattermost logs -f [pod name]
