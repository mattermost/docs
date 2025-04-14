Server deployment planning
==========================

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    Preparations </deploy/server/preparations>
    Deploy with Kubernetes </deploy/server/deploy-kubernetes>
    Deploy with Linux </deploy/server/deploy-linux>
    Deploy with Containers </deploy/server/deploy-containers>
    Reference Architecture </deploy/server/server-architecture>
    Scale for Enterprise </scale/scaling-for-enterprise>

This section provides comprehensive guidance on deploying and managing your Mattermost server. Mattermost is a flexible, high-performance messaging platform built with Go and React, designed to provide secure team collaboration at scale.

Core technology stack
----------------------

Mattermost's architecture is built on modern, reliable technologies:

* **Backend**: Written in Go, providing high performance and concurrent processing
* **Frontend**: React-based web application and mobile apps
* **Database**: PostgreSQL for primary data storage
* **Search**: Elasticsearch (optional) for advanced search capabilities
* **File Storage**: Local filesystem or cloud storage (S3, MinIO) for media and attachments
* **Caching**: Built-in support for Redis for enhanced performance

Deployment options
-------------------

Mattermost offers several deployment options to suit your organization's needs:

1. :doc:`Kubernetes (Recommended) </deploy/server/deploy-kubernetes>`

   Our recommended approach for production deployments offers:

   * Scalability and high availability
   * Automated updates and rollbacks
   * Infrastructure as code
   * Built-in monitoring and logging
   * Easy integration with existing DevOps workflows


2. :doc:`Linux Server Installation </deploy/server/deploy-linux>`

   A direct installation on Linux servers offers:

   * Simple, straightforward setup
   * Full control over the installation
   * For situations where containers aren't preferred

3. :doc:`Container-Based Deployment </deploy/server/deploy-containers>`

   Docker containers are suitable for smaller deployments only as it offers:

   * Simplified installation and updates
   * Consistent environments
   * Easy dependency management
   * No support for high availability

Prerequisites
--------------

Before deploying Mattermost, ensure you have reviewed the :doc:`software and hardware requirements </deploy/software-hardware-requirements>`, and have:

* A supported Linux distribution
* Database server (PostgreSQL 13+)
* Reverse proxy (NGINX recommended)
* SSL/TLS certificates for secure communication
* Adequate storage for files and database
* Network access and firewall configurations
* System requirements met based on expected user load

Plan your deployment
----------------------

When planning your Mattermost deployment, consider the following when choosing the deployment method that best aligns with your organization's requirements, technical expertise, and infrastructure capabilities:

* Expected user count and growth
* High availability requirements
* Backup and disaster recovery needs
* Integration with existing systems
* Security and compliance requirements
* Monitoring and maintenance strategy

The following server, desktop, and mobile application sections provide detailed instructions for each deployment approach.

Minimum database version policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make planning easier and ensure your Mattermost deployment remains fast and secure, we are introducing a policy for updating the minimum supported version of PostgreSQL. The oldest supported PostgreSQL version Mattermost supports will match the oldest version supported by the PostgreSQL community. This ensures you benefit from the latest features and security updates.

This policy change takes effect from Mattermost v10.6, where the minimum PostgreSQL version required will be PostgreSQL 13. This aligns with the PostgreSQL community's support policy, which provides 5 years of support for each major version.

.. note::

  Mattermost v10.6 is not an :ref:`Extended Support Release (ESR) <about/release-policy:extended support releases>`. Going forward, this database version support policy will only apply to ESR releases.

When a PostgreSQL version reaches its end of life (EOL), Mattermost will require a newer version starting with the next scheduled ESR release. This means the following future PostgreSQL minimum version increases as follows:

+-----------------------------------------------------------+------------------+--------------------------------+
| **Mattermost Version**                                    | **Release Date** | **Minimum PostgreSQL Version** |
+===========================================================+==================+================================+
| :ref:`v9.11 ESR <release-v9-11-extended-support-release>` | 2024-8-15        | 11.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| :ref:`v10.5 ESR <release-v10.5-extended-support-release>` | 2025-2-15        | 11.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| :ref:`v10.6 <release-v10.6-feature-release>`              | 2025-3-15        | 13.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| v10.11 ESR                                                | 2025-8-15        | 13.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| v11.5 ESR ``*``                                           | 2026-2-15        | 14.x (EOL 2026-11-12)          |
+-----------------------------------------------------------+------------------+--------------------------------+

``*`` Forcasted release version and date.

Customers will have 9 months to plan, test, and upgrade their PostgreSQL version before the new requirement takes effect. This policy aims to provide clarity and transparency so you can align database upgrades with the Mattermost release schedule. Contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_. to discuss your options.
