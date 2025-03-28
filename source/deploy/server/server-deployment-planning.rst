Server deployment planning
==========================

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    Preparations </deploy/server/preparations>
    Deploy with Kubernetes </deploy/server/deploy-kubernetes>
    Deploy with Containers </deploy/server/deploy-containers>
    Deploy with Linux </deploy/server/deploy-linux>
    Architecture reference </deploy/server/server-architecture>

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

2. :doc:`Container-Based Deployment </deploy/server/deploy-containers>`

   Docker containers are suitable for smaller deployments that offer:

   * Simplified installation and updates
   * Consistent environments
   * Easy dependency management

3. :doc:`Traditional Linux Installation </deploy/server/deploy-linux>`

   A direct installation on Linux servers offers:

   * Simple, straightforward setup
   * Full control over the installation
   * For situations where containers aren't preferred

Prerequisites
--------------

Before deploying Mattermost, ensure you have reviewed the :doc:`software and hardware requirements </deploy/server/software-hardware-requirements>`, and have:

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