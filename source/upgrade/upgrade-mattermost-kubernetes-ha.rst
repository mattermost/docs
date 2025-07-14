Upgrade Mattermost in Kubernetes and High Availability environments
===================================================================

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

This guide provides a comprehensive approach to upgrading Mattermost deployments managed via Kubernetes and the Mattermost Operator, including support for High Availability (HA) and Active/Active failover configurations. It outlines best practices to ensure minimal downtime and service continuity during upgrades.

Architecture overview
----------------------

Mattermost leverages Kubernetes for orchestration, utilizing Helm charts and the Mattermost Operator for deployment and lifecycle management. This setup facilitates scalability, high availability, and automated upgrades. See the :doc:`Kubernetes deployment </deploy/server/deploy-kubernetes>` documentation for details.

In :doc:`High Availability (HA) </scale/high-availability-cluster-based-deployment>` configurations, Mattermost runs multiple application servers in a cluster, with load balancing handled by tools like NGINX, HAProxy, or Kubernetes Ingress controllers. The database layer employs replication strategies to ensure redundancy and failover capabilities.

Active/Active (multi-site) deployments involve multiple Mattermost clusters operating concurrently across different regions or availability zones. This optional but recommended setup requires careful coordination to maintain data consistency and service availability during upgrades.

How the Operator handles upgrades
---------------------------------

The :ref:`Mattermost Operator <deploy/server/deploy-kubernetes:itab--Mattermost-Operator--3_1-step-2-install-the-mattermost-operator>` automates the upgrade process by:

Performing pre-upgrade compatibility checks.

Halting the upgrade if issues are detected.

Rolling out upgrades incrementally across pods.

Maintaining live traffic routing during pod transitions.

Safety and recovery features

    Failed upgrades do not modify the live cluster.

    Health monitoring ensures replacement of unhealthy pods.

    New pods replace old ones only after passing health checks.

Prepare for an upgrade
-----------------------

Before initiating an upgrade:

    Ensure your Kubernetes cluster and nodes are healthy.

    Confirm the Mattermost Operator is up-to-date.

    Backup all relevant data:

        Database

        File storage

        Helm release values

    Validate that storage backends and database replicas are in sync.

Refer to the Backup and Disaster Recovery Guide for detailed instructions.

Perform the upgrade
--------------------

5.1 Via Helm and the Mattermost Operator

To upgrade Mattermost using Helm:

    Update your values.yaml file with the desired Mattermost version.

    Run the Helm upgrade command:

    helm upgrade mattermost mattermost/mattermost-operator -f values.yaml

    Monitor the rollout progress using kubectl and Operator logs.

5.2 Traffic Routing and Load Balancing

During the upgrade:

    HAProxy or Ingress configurations continue routing traffic.

    Rolling pod upgrades ensure zero-downtime behavior.

Active/Active failover considerations
--------------------------------------

    Applicable only for deployments with multiple active Mattermost clusters across regions or availability zones.

    Upgrade one site at a time while directing traffic to the other.

    Validate sync and data replication before failover.

    Ensure configuration consistency across clusters.

    Monitor for potential split-brain scenarios during partial upgrades.

Post-upgrade validation
-----------------------

After the upgrade:

    Confirm all pods are running the new version.

    Check accessibility of file storage, database, and services.

    Perform admin console and functional smoke tests.

    Validate health metrics and logs for anomalies.

Rollback strategy
------------------

In case of upgrade issues:

    Use Helm’s rollback command:

    helm rollback mattermost <revision_number>

    Restore from backups if necessary.

    Refer to the Disaster Recovery Guide for detailed procedures.

Frequently asked questions
--------------------------

Q: Can I upgrade the Operator and Mattermost simultaneously?
A: It's recommended to upgrade the Operator first, ensure stability, and then proceed with the Mattermost upgrade.

Q: What if my pods don’t become ready after the upgrade?
A: Check the Operator logs and pod events using kubectl to identify and resolve issues.

Q: How can I test upgrades in a staging environment first?
A: Deploy a separate staging environment mirroring production, and perform the upgrade there to validate the process.