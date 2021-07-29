.. _faq_kubernetes:

Frequently Asked Questions
--------------------------

What's the difference between the Mattermost Operator and Helm Charts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost Operater is a self-contained set of application/product-specific instructions that runs inside Kubernetes and facilitates application
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

Currently this is not supported as it introduces the possiblilty of missing a data entry in the database.

Issues configuring Login with SAML on Kubernetes.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For some configuration of authentication with SAML there might be an issue wtih requests being to large and ``502`` status code response appear during login attempts.
This may be caused by the default ``proxy-buffer-size`` on Nginx Ingress being to low.
To fix the issue configure appropriate buffer size (8 or 16k should be sufficient for most cases) with Nginx anntoation by adding it to Mattermost manifest under ``spec.ingressAnnotations``:

.. code-block:: yaml
    ...
    spec:
    ...
      ingressAnnotations:
        nginx.ingress.kubernetes.io/proxy-buffer-size: 16k
    ...

Be careful when changing the buffer size as it may slightly impact Nginx performence. Exact values are machine dependant.
