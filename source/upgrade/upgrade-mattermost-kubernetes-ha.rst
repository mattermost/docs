Upgrade Mattermost in Kubernetes and High Availability environments
===================================================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

This guide provides a resilient and comprehensive strategy for upgrading Mattermost deployments managed via Kubernetes and the Mattermost Operator, including High Availability (HA) and optional Active/Active failover configurations. It outlines best practices to ensure zero downtime, minimize service risk, and provide robust fallback mechanisms.

Architecture overview
----------------------

Kubernetes-based deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost uses :doc:`Kubernetes </deploy/server/deploy-kubernetes>` for container orchestration, deployed and managed via Helm charts and the :ref:`Mattermost Operator <install-mattermost-operator>`. This model enables scalable, highly available, and automatically managed application lifecycles.

The Mattermost Operator handles the upgrade process automatically, ensuring that pods are updated incrementally and that traffic is routed correctly throughout the upgrade. If an error occurs during the upgrade, the Operator will not apply any changes, allowing you to investigate and resolve the issue or manually roll back without impacting the live environment. See the :doc:`Downgrade Mattermost Server </upgrade/downgrading-mattermost-server>` documentation for rollback details. 

Health monitoring ensures that only healthy pods are replaced, and new pods are brought online only after passing health checks. New pods are deployed with the updated version, while old pods are gracefully terminated.

High Availability
~~~~~~~~~~~~~~~~~

In :doc:`High Availability (HA) cluster-based deployments </scale/high-availability-cluster-based-deployment>`, Mattermost runs multiple application servers in a cluster. This configuration ensures that if one server fails, others can continue to serve requests without downtime. User traffic load balancing is managed with services such as NGINX Ingress or HAProxy. :ref:`PostgreSQL <deploy/server/preparations:database preparation>` and :ref:`file storage <deploy/server/preparations:file storage preparation>` are deployed with replication for redundancy and failover.

Active/Active deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An Active/Active configuration is optional and consists of two or more Mattermost clusters running concurrently across geographically distributed regions or availability zones. Each cluster is capable of serving live user traffic and processing requests independently while remaining in sync with shared backend components such as the database and file storage.

Key benefits for enterprise customers include:

- **Resilience and uptime**: If a site becomes unavailable due to maintenance or an outage, another site can continue to serve users with minimal disruption.
- **Geographic distribution**: Users connect to the nearest cluster for lower latency and faster response times.
- **Load distribution**: Workload can be balanced between clusters to improve performance and system scalability.

These deployments require careful configuration management and coordination to ensure data consistency, upgrade safety, and seamless traffic failover. These clusters must maintain configuration/data consistency and require coordinated upgrades. See the :ref:`Active/Active upgrade considerations <active-active-upgrade-considerations>` section for recommendations.

Step 1: Prepare
-----------------

This phase ensures your environment is healthy, backed up, and ready for an upgrade. Follow each step carefully to avoid disruptions and to ensure rollback readiness. 

.. important::

  - **Backup your data**: Always back up your database and file storage before starting an upgrade. This ensures you can restore to a previous state in case of issues during the upgrade process.
  - **Upgrade safely**: The Mattermost Operator performs upgrade validation checks before rollout. If checks fail, the upgrade is blocked and no changes are applied. If checks pass, the Operator upgrades pods incrementally to maintain uptime.

Pre-upgrade checklist
~~~~~~~~~~~~~~~~~~~~~~

1. **Cluster health**: Ensure all nodes are in a ready state and all pods are running without errors. This step is crucial to avoid issues during the upgrade process. Use the following commands to check cluster health:

  .. code-block:: bash

    kubectl get nodes
    kubectl get pods --all-namespaces

2. **Helm setup**: Verify that Helm is installed and configured correctly in your Kubernetes cluster. Ensure you have the latest version of the Mattermost Operator Helm chart. Use the following commands to check Helm setup:

  .. code-block:: bash

    helm repo update
    helm upgrade mattermost-operator mattermost/mattermost-operator -n <OPERATOR_NAMESPACE_HERE> -f <OPTIONAL_CUSTOM_VALUES_HERE>

3. Confirm Mattermost Operator version. Make sure the image version matches the latest supported release from the Helm repository. Use the following command to check the current image version of the Mattermost Operator:

  .. code-block:: bash

    kubectl get deployment mattermost-operator -n mattermost -o=jsonpath='{.spec.template.spec.containers[0].image}'

4. **Verify available resources**: Ensure your Kubernetes cluster has sufficient CPU and memory resources to handle the upgrade process. Use the following commands to check resource availability:

  .. code-block:: bash

    kubectl top nodes
    kubectl describe node | grep Allocatable

5. Back up database and file storage.

    Use ``pg_dump`` or volume snapshots to create a full backup to a secure, external location (e.g., S3 or NFS). Validate the backup can be restored. See the :doc:`Backup and Disaster Recovery </deploy/backup-disaster-recovery>` documentation for details.

6. Ensure configuration consistency: Validate that ``values.yaml``, secrets, and other configuration files are version-controlled and consistent across all clusters (required for `Active/Active deployments <#active-active-upgrade-considerations>`__). Use tools like GitOps or configuration management systems to ensure all clusters have the same configuration.

7. We strongly recommend performing a dry run by testing the upgrade in a staging environment that mirrors production to catch misconfigurations early.

Step 2: Perform the upgrade
----------------------------

This step involves updating the Mattermost Operator and Mattermost server to a new version. The Operator manages the upgrade process, ensuring that pods are updated incrementally and that traffic is routed correctly throughout the upgrade.

We recommend having a separate Mattermost custom resource. See the :doc:`Deploy Mattermost on Kubernetes </deploy/server/deploy-kubernetes>` documentation for details.

1. In the separate resource, update the ``version`` field in your ``mattermost-installation.yaml`` file by replacing the ``<new-version-tag>`` with the specific version you are upgrading to:

  .. code-block:: yaml

    apiVersion: installation.mattermost.com/v1beta1
    kind: Mattermost
    metadata:
      name: <INSTALLATION_NAME_HERE>
    spec:
      version: <new-version-tag>  # Update this field

  Alternatively, if you're using Helm ``values.yaml`` directly, update it with the desired Mattermost version:

  .. code-block:: yaml

    image:
      repository: mattermost/mattermost-enterprise-edition
      tag: <new-version-tag>

2. Apply the updated configuration:

  For Mattermost custom resource deployments:

  .. code-block:: bash

    kubectl apply -f mattermost-installation.yaml

  For Helm values deployments:

  .. code-block:: bash

    helm upgrade mattermost mattermost/mattermost-operator -f values.yaml


3. Monitor the rollout by tracking upgrade progress and logs with the following commands:

  .. code-block:: bash

    kubectl get pods -n mattermost
    kubectl logs -f <pod-name> -n mattermost

New pods are started with the updated version. Old pods are gracefully terminated after health checks pass, and traffic remains uninterrupted due to rolling upgrade behavior. NGINX, HAProxy, or Ingress configurations continue routing traffic seamlessly during the upgrade process.

.. _active-active-upgrade-considerations:

Step 3: Active/Active upgrade considerations
--------------------------------------------

When your deployment includes an Active/Active configuration with multi-cluster or multi-region deployments, you must ensure that all clusters are upgraded in a coordinated manner to maintain data consistency and service availability.

For coordinated site upgrades, we recommend the following steps:

- Use your global load balancer or DNS to route traffic away from the site being upgraded.
- Upgrade one site at a time while directing traffic to the other. This minimizes downtime and allows for validation of the upgrade process.
- Confirm replication health for databases and storage before proceeding to the next site.
- Monitor performance and logs before resuming traffic to the upgraded site.

To prevent split-brain scenarios during upgrades and ensure data consistency:

- Use a global load balancer or DNS to direct traffic exclusively to the active site.
- Disable writes on the site being upgraded until the upgrade is complete and validated.
- Confirm that only one site is actively writing data at any time.
- Monitor logs for signs of replication lag, file synchronization issues, or data divergence.
- Validate the health of data replication channels before and after each site upgrade.

Step 4: Validate
------------------

After the upgrade:

1. Confirm that all pods are healthy and running the expected version using the following command:

  .. code-block:: bash

    kubectl get pods -n mattermost -o=jsonpath='{.items[*].spec.containers[*].image}'

3. Perform product smoke tests:

  - Log in to the Mattermost web interface and navigate across teams and channels.
  - Test core functionalities such as posting messages and uploading files.
  - Verify that all integrations, webhooks, and plugins are functioning as expected.
  - Check for error messages in the logs.

4. Use monitoring tools to confirm application health and performance. See the :doc:`Performance monitoring with Prometheus and Grafana </scale/deploy-prometheus-grafana-for-performance-monitoring>` documentation or the :doc:`Metrics plugin </scale/performance-monitoring-metrics>` documentation for details on collecting and reviewing performance metrics.

Rollback strategy
------------------

In case of upgrade issues, rollback should be performed by modifying the custom resource and setting the Mattermost version back to its original value.

For Mattermost custom resource deployments, update the ``version`` field in your ``mattermost-installation.yaml`` file to the previous version:

.. code-block:: yaml

    apiVersion: installation.mattermost.com/v1beta1
    kind: Mattermost
    metadata:
      name: <INSTALLATION_NAME_HERE>
    spec:
      version: <previous-version-tag>  # Set back to previous version

Then apply the rollback:

.. code-block:: bash

    kubectl apply -f mattermost-installation.yaml

Alternatively, for Helm values deployments, use Helm's rollback command:

.. code-block:: bash

    helm rollback mattermost <revision_number>

Restore your PostgreSQL database and file store backups if needed. Refer to the :doc:`Backup and Disaster Recovery </deploy/backup-disaster-recovery>` documentation for detailed guidance.

Frequently asked questions
--------------------------

How can I confirm an upgrade was successful?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A successful upgrade is indicated by:

- All pods running the expected image version
- No errors in pod logs
- Functional smoke tests passing (login, messaging, file upload, etc.)
- No anomalies in monitoring dashboards

What should I monitor post-upgrade?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We recommend monitoring the following key metrics after an upgrade:

- Pod health and restarts
- Application logs for errors or warnings
- Database replication health (if HA or Active/Active)
- Performance metrics (latency, error rate) via Prometheus/Grafana

How can I test upgrades without impacting production?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We strongly recommend deploying a separate staging environment that mirrors production, and running a full end-to-end upgrade simulation before upgrading live production clusters.

Can I upgrade the Operator and Mattermost server at the same time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upgrade the Operator first. Validate it’s stable before upgrading the Mattermost server version.

Do I need to upgrade the database separately?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost does not upgrade the database schema by default. You must manually apply database schema updates if required by a newer Mattermost version. Review the :doc:`Mattermost Server changelog </about/mattermost-v10-changelog>` for any migration steps.

What if my pods don’t become ready after the upgrade?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the Operator logs and pod events using ``kubectl`` to identify and resolve issues. Look for common issues such as resource constraints, configuration errors, or network connectivity problems.



What version compatibility should I be aware of between the Mattermost Operator and the application server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running an older Operator version may not support newer Mattermost features or upgrade flows. Always check the `Helm chart release notes <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-operator>`_ for version compatibility between the Operator and the Mattermost server. 

Can I automate this upgrade process using GitOps or CI/CD?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. You can manage upgrades using tools like ArgoCD or FluxCD to apply Helm changes from version-controlled ``values.yaml`` files. Ensure changes are peer-reviewed and validated in staging before promotion.