Deploy Apps to OpenFaas and faasd
=================================

OpenFaaS Apps
-------------

What is OpenFaaS?
~~~~~~~~~~~~~~~~~

OpenFaaS makes it relatively simple to deploy both serverless functions and existing code in stateless containers on Kubernetes or directly on Linux hosts, on any public or private cloud. Learn more at |OpenFaas.com|.

Package an App for OpenFaaS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For details on how to develop and package apps for AWS, see |serverless example|.

Deploy with ``appsctl``
~~~~~~~~~~~~~~~~~~~~~~~~

An App designed and bundled for OpenFaaS can be deployed to the customer's own OpenFaaS or faasd environments, and then installed on a self-managed ("on-prem") Mattermost server, using the ``appsctl openfaas deploy`` command.

This command requires that |faas-cli| is installed and configured, with credentials sufficiently privileged to deploy functions.

OpenFaaS requires a |docker registry| to pass the images that it builds to the function instances, so ``docker`` must have been configured, and ``docker login`` done, with sufficient credentials to push to the registry of choice.

To deploy OpenFaaS Apps use ``appsctl openfaas deploy {openfaas-bundle.zip}`` command. It will deploy all functions in the bundle, and "list" (upload the manifest of) the app in Mattermost server. ``--install`` can be used to automatically install the app once it's deployed.

**Flags:**

- ``--docker-registry``: the docker registry name (will be used as a prefix for the image name) to push the function images to.
- ``--install``: install the app onto the Mattermost server once it's been successfully deployed.
- ``--update``: update the function that already exists.

The command requires that the following environment variables are set:

- ``MM_SERVICESETTINGS_SITEURL``: must be set to where the Mattermost server APIs can be accessed.
- ``MM_ADMIN_TOKEN``: must be set to access the Mattermost REST APIs.
- ``OPENFAAS_URL``: must be set to the admin (root) URL of the OpenFaaS installation.

Once deployed, apps can be installed interactively in Mattermost using ``/apps install listed`` command.

.. |OpenFaas.com| raw:: html

    <a href="https://www.openfaas.com" target="_blank">OpenFaas.com</a>

.. |serverless example| raw:: html

    <a href="https://developers.mattermost.com/integrate/apps/quickstart/quick-start-serverless" target="_blank">serverless example</a>

.. |faas-cli| raw:: html

    <a href="https://github.com/openfaas/faas-cli" target="_blank">faas-cli</a>

.. |docker registry| raw:: html

    <a href="https://docs.docker.com/registry/" target="_blank">docker registry</a>