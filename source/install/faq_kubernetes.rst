.. _faq_kubernetes:

Frequently Asked Questions
--------------------------

What's the difference between the Mattermost Operator and Helm Charts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost Operator is a self-contained set of application/product-specific instructions that runs inside Kubernetes and facilitates application
management and deployment.

Helm is a tool used to deploy Kubernetes manifests to a cluster, but does not facilitate application management.

Does the Mattermost Operator replace the Helm Chart?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Helm is a good mechanism to deploy operators and other applications but doesn't facilitate application management. 

Is minIO the only available storage option?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, other options and operators can be added.

Do I have to install a separate SQL server to use the Mattermost Operator?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, you can use the operator on top of your existing deployment without setting up another database. We will shortly
be providing steps for this configuration.

Can you use blue-green deployments with different database schemas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently this is not supported as it introduces the possibility of missing a data entry in the database.

Are environment variables supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. However, ``config.json`` file settings will be overridden if the `$MM_SQLSETTINGS_DATASOURCE` environment variable is set. See the `Environment Variables <https://docs.mattermost.com/configure/configuration-settings.html#environment-variables>`__ configuration settings documentation for details.

Issues configuring Login with SAML on Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For some SAML authentication configurations, ``502`` status code response can appear during login attempts due to requests being too large.
This can be caused by the default ``proxy-buffer-size`` setting for NGINX Ingress being too low.
To fix this issue, configure an appropriate buffer size (8k or 16k should be sufficient for most cases) with NGINX annotation by adding it to the Mattermost manifest under ``spec.ingressAnnotations``:

.. code-block:: yaml

  ...
  spec:
  ...
    ingress:
    ...
      annotations:
        nginx.ingress.kubernetes.io/proxy-buffer-size: 16k
  ...

Use caution when changing the buffer size as it may slightly impact NGINX performance. Exact values are machine-dependent.
