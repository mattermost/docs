Deploy Mattermost on Kubernetes
===============================

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost server can be deployed on various Kubernetes platforms, providing a scalable and robust infrastructure for your team communication needs. This guide covers deployment options for major cloud providers and general Kubernetes installations.

.. tip::

  To learn how to safely upgrade your deployment in Kubernetes for High Availability with Active/Active support, see the :doc:`Upgrading Mattermost in Kubernetes and High Availability Environments </upgrade/upgrade-mattermost-kubernetes-ha>` documenation.

Platform
--------

Choose your preferred platform below for specific deployment instructions:

.. tab:: Mattermost Operator
  :parse-titles:

  .. include:: kubernetes/deploy-k8s.rst
    :start-after: :nosearch:

.. tab:: Azure
  :parse-titles:

  .. include:: kubernetes/deploy-k8s-aks.rst
    :start-after: :nosearch:

.. tab:: Oracle
  :parse-titles:

  .. include:: kubernetes/deploy-k8s-oke.rst
    :start-after: :nosearch:

Frequently Asked Questions
--------------------------

Why are my pods failing with a ``CrashLoopBackOff`` error after adding a custom CA certificate to my Docker image?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may see a ``CrashLoopBackOff`` error after adding a custom CA certificate to your Docker image's ``/etc/ssl/certs`` directory and deploying it to your Kubernetes environment via the Mattermost Enterprise Edition Helm Chart. This issue typically arises because the custom CA certificate is not being recognized by the system's certificate trust store, leading to TLS handshake failures when the application attempts to connect to services that require the custom CA.

While core functionality may remain operational, you may notice the following symptoms:

- Pods stuck in a crashloop with the error message: backoff - restarting failed container in pod.
- Debugging commands like ``kubectl describe`` and ``kubectl logs`` provide little to no valuable information.
- Integrations may be blocked.

Can I resolve this issue without rebuilding the Docker image?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. We recommend using Kubernetes-native solutions to manage custom CA certificates to simplify deployment processes and minimize disruptions caused by image rebuilds. You can inject the certificate directly into the pod using Kubernetes resources instead of modifying the Docker image to manage custom CA certificates dynamically without needing to rebuild and redeploy your Docker image every time the certificate changes.

Use a Kubernetes secret to store your custom CA certificate and then mount it into the pod:

1. Create a Kubernetes secret with your custom CA certificate.
2. Mount the certificate into the pod using the Helm chart’s configuration options. This method simplifies management and avoids the need to rebuild your Docker image for future certificate updates.

Alternatively, to dynamically inject certificates without modifying the Docker image, use an ``initContainer`` to copy the certificate into the pod's filesystem and update the certificate trust store before the main container starts.

How to troubleshoot the root cause of the ``CrashLoopBackOff`` error?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``kubectl describe pods`` to check detailed event logs.

Consider logging tools like Grafana to aggregate and analyze logs for additional insights.

Where is data stored in a self-hosted Kubernetes deployment?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where data is stored depends on the backend database (such as RDS, Azure Postgres, self-hosted PostgreSQL), and the backend filestore (such as AWS S3, Minio, Mounted volume) configured during deployment.

We recommend the following S3 Options:

- AWS S3
- MinIO (Self-Hosted)

For Volume Mounts, the following options use Kubernetes Volume Mounting to provide filestores as a "local" directory to the Mattermost server:

- NFS
- AzureBlob

Not all types of `Kubernetes persistent volumes <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#types-of-persistent-volumes>`_ have been tested with Mattermost, and some may have limitations or specific configurations that may require additional setup to ensure proper permissions and access. We recommend system admins review documentation for their preferred persistent volume types and test to ensure compatibility with Mattermost.
