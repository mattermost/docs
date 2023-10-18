App deployment
==============

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

    Settings </guides/configure-app-framework>
    HTTP </guides/deploy-http>
    AWS </guides/deploy-aws>
    Package Apps for AWS </guides/package-aws>
    OpenFaaS </guides/deploy-openfaas>

- In **Mattermost Cloud**, all apps are deployed to the Marketplace by Mattermost staff. They can be installed onto a specific Mattermost instance using the ``/apps install listed`` command. No special configuration is required; the ``/apps install`` command should be enabled and functional by default.

- **Self-managed Mattermost** installations can use external Apps as HTTP services that have already been deployed, or can deploy App bundles on self-managed hosting or serverless platforms. Currently, `AWS Lambda <deploy-aws>`_, `OpenFaaS <deploy-openfaas>`_, and Kubeless deployments are supported. The `appsctl` command can be used to deploy app bundles to these environments.

  Self-managed customers can also install external `HTTP <deploy-http>`_ apps, with no need to deploy them.

  The ``appsctl`` CLI tool is provided to deploy AWS and OpenFaaS apps in self-managed environments. To install ``appsctl``, use the following command:

  .. code-block:: shell

      go install github.com/mattermost/mattermost-plugin-apps/cmd/appsctl@latest

.. note::

    If you have a self-hosted Mattermost instance running on AWS EC2, the default Golang version is 1.13.8.

Because of this, the Golang install command will give an error stating:

.. code-block:: shell

    can't load package: package github.com/mattermost/mattermost-plugin-apps/cmd/appsctl@latest: cannot use path@version syntax in GOPATH mode

To fix this, update your Golang version to the latest release and run the command again. When deploying to AWS, the ``appsctl`` binary is present in the ``Home`` directory inside the ``go/bin`` folder.

To use ``appsctl``, run the following command: ``./go/bin/appsctl``
