:orphan:
:nosearch:

What's the difference between the Mattermost Operator and Helm Charts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost Operator is a self-contained set of application/product-specific instructions that runs inside Kubernetes and facilitates application
management and deployment.

Helm is a tool used to deploy Kubernetes manifests to a cluster, but does not facilitate application management.

We provide a `helm chart <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-operator>`__ that can be used to to install the Mattermost Operator.

Does the Mattermost Operator replace the Mattermost Helm Chart?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although the Mattermost Operator is the recommended deployment option for running Mattermost in Kubernetes, a helm chart for directly deploying Mattermost resources is still available.

What database and filestore should I use for Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Always refer to the Mattermost server documentation for what databases and filestores are supported.

The following documentation on :doc:`scaling for enterprise </scale/scaling-for-enterprise>` is a good place to start.

What are the Operator-Managed database and filestore options?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost Operator provides an option to directly provision a database and filestore for a Mattermost installation to use,
but this option is only meant for validation and testing. These options rely on specific releases of operators that we don't maintain.
For production deployments of Mattermost, one of the other database and filestore configuration options should be chosen.

In particular, the Operator-Managed database option relies on a MySQL operator and MySQL databases are now deprecated in Mattermost.

Note that you can choose to manage your Mattermost database and filestore in Kubernetes with other operators, but these should
be provisioned separately first and then connected to the Mattermost installation as ``external`` backends.

Can you use blue-green deployments with different database schemas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently this is not supported as it introduces the possibility of missing a data entry in the database.

Are environment variables supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. However, ``config.json`` file settings will be overridden if the `$MM_SQLSETTINGS_DATASOURCE` environment variable is set. See the `Environment Variables </configure/configuration-settings.html#environment-variables>`__ configuration settings documentation for details.

Issues configuring login with SAML on Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For some SAML authentication configurations, ``502`` status code response can appear during login attempts due to requests being too large.
This can be caused by the default ``proxy-buffer-size`` setting for NGINX Ingress being too low.
To fix this issue, configure an appropriate buffer size (8k or 16k should be sufficient for most cases) with NGINX annotation by adding it to the Mattermost manifest under ``spec.ingressAnnotations``:

.. code-block:: yaml
  :class: mm-code-block 

  ...
  spec:
  ...
    ingress:
    ...
      annotations:
        nginx.ingress.kubernetes.io/proxy-buffer-size: 16k
  ...

Use caution when changing the buffer size as it may slightly impact NGINX performance. Exact values are machine-dependent.