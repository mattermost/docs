.. _manage_kubernetes:

Managing the Mattermost Kubernetes operator
============================================

CLI commands
------------

You can manage and monitor your Mattermost instance's installation and deployment process in the CLI, using the commands listed below.

.. code-block:: sh

    $ kubectl -n mattermost get jobs

.. code-block:: sh

    $ kubectl -n mattermost get all

Logs
----

.. code-block:: sh

    $ mattermost logs -f [pod name]
