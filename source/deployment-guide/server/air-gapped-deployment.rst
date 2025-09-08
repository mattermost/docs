Deploy Mattermost in Air-Gapped Environments
==============================================

This guide outlines how to deploy Mattermost in a self-hosted air-gapped environment, focusing on gathering required resources before going offline and then deploying using your preferred method. An air-gapped environment is one that is isolated from the public internet, requiring all necessary components to be available locally.

Prerequisites: Gather Required Resources
----------------------------------------

Before disconnecting from the internet, you must gather all required packages, container images, and dependencies for your chosen deployment method. Failure to collect these resources beforehand will prevent successful deployment in the air-gapped environment.

Essential Resources for All Deployment Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Database**: PostgreSQL installation packages or container images
2. **File Storage**: Object storage solution or shared filesystem setup
3. **SSL/TLS Certificates**: Required for secure HTTPS connections
4. **DNS Configuration**: Plan your internal DNS setup

Optional Supporting Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider gathering resources for these optional components:

- **SMTP Server**: For email functionality
- **LDAP/SAML**: For authentication integration  
- **Elasticsearch**: For enhanced search performance
- **Prometheus**: For monitoring and observability

Deployment Method-Specific Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab:: Linux (Tarball)

    **Required Downloads:**
    
    - Mattermost Server tarball: https://releases.mattermost.com/
    - PostgreSQL packages for your Linux distribution
    - Any additional system dependencies
    
    **Recommended Setup:**
    
    - Create a local package mirror for ongoing updates
    - See `DigitalOcean's guide <https://www.digitalocean.com/community/tutorials/how-to-set-up-a-local-apt-repository-with-reprepro>`_ for APT repositories
    - For RHEL/CentOS: Use ``reposync`` to create local YUM repositories

.. tab:: Kubernetes

    **Required Container Images:**
    
    - ``mattermost/mattermost-enterprise-edition:latest`` (or specific version)
    - ``postgres:15`` (or your preferred PostgreSQL version)
    - Any additional images for your storage solution
    
    **Container Registry Setup:**
    
    - Set up a private container registry before going offline
    - See `DigitalOcean Container Registry guide <https://www.digitalocean.com/community/developer-center/how-to-set-up-digitalocean-container-registry>`_ for setup instructions
    - Alternative: Use Harbor for advanced features: https://goharbor.io/
    
    **Additional Resources:**
    
    - Kubernetes manifests or Helm charts
    - kubectl and helm binaries if not already installed

.. tab:: Docker

    **Required Container Images:**
    
    - ``mattermost/mattermost-enterprise-edition:latest`` (or specific version)
    - ``postgres:15`` (or your preferred PostgreSQL version)
    - Any additional images for your storage solution
    
    **Container Registry Setup:**
    
    - Set up a private container registry before going offline
    - See `DigitalOcean Container Registry guide <https://www.digitalocean.com/community/developer-center/how-to-set-up-digitalocean-container-registry>`_ for setup instructions
    - Alternative: Use Harbor for advanced features: https://goharbor.io/
    
    **Additional Resources:**
    
    - Docker Compose files
    - Docker engine installation packages if not already installed

Deploy Mattermost
-----------------

Once you have gathered all required resources and are in your air-gapped environment, follow the deployment method that matches your infrastructure:

.. tab:: Linux (Tarball)

    Follow the standard Mattermost Linux installation process using your gathered resources:
    
    1. **Install Dependencies**: Use your local package mirror to install PostgreSQL and other dependencies
    2. **Deploy Mattermost**: Follow the :doc:`Linux installation guide </deployment-guide/server/production-install-ubuntu>` using your downloaded tarball
    3. **Configure Database**: Set up PostgreSQL using local packages
    4. **Configure File Storage**: Implement your chosen storage solution

.. tab:: Kubernetes

    Deploy using your private container registry:
    
    1. **Configure Registry Access**: Set up Kubernetes to use your private registry
    2. **Deploy Database**: Install PostgreSQL using images from your private registry
    3. **Deploy Mattermost**: Follow the :doc:`Kubernetes deployment guide </deployment-guide/kubernetes>` with your private registry images
    4. **Configure Storage**: Set up persistent volumes for file storage

.. tab:: Docker

    Deploy using your private container registry:
    
    1. **Configure Docker**: Set up Docker to use your private registry
    2. **Deploy with Compose**: Follow the :doc:`Docker deployment guide </deployment-guide/server/production-docker-setup>` using your private registry images
    3. **Configure Storage**: Set up volumes for database and file storage

Air-Gapped Configuration Requirements
-------------------------------------

After successful deployment, configure Mattermost for air-gapped operation:

Disable Internet-Dependent Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mobile Push Notifications**

Mobile push notifications require external connectivity to Mattermost's push notification service. Disable this feature in **System Console > Environment > Push Notification Server** by setting **Enable Push Notifications** to ``false``.

**Website Link Previews**

Website link previews require internet access to fetch external content. Disable this feature in **System Console > Site Configuration > Posts** by setting **Enable Website Link Previews** to ``false``.

Plugin Considerations
~~~~~~~~~~~~~~~~~~~~~

Review all installed plugins for external dependencies:

1. **Audit Plugin Requirements**: Check each plugin's documentation for internet dependencies
2. **Disable Non-Compatible Plugins**: Remove or disable plugins that require external connectivity
3. **Test Functionality**: Verify remaining plugins work correctly in the air-gapped environment

Network Security Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implement additional security measures appropriate for air-gapped environments:

**Firewall Configuration**

1. **Implement strict firewall rules** to control traffic between network segments
2. **Use network segmentation** to isolate critical infrastructure components
3. **Regularly audit network access** to ensure the environment remains properly isolated

**Certificate Management**

1. **Use internal Certificate Authority** for SSL/TLS certificates
2. **Implement certificate rotation procedures** that work without external connectivity
3. **Document certificate expiration dates** for proactive renewal

Ongoing Maintenance
-------------------

Maintaining Security in Air-Gapped Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Regular Updates**

1. **Schedule periodic updates** to your local package mirrors and container registries
2. **Maintain a consistent testing process** for all updates before deployment
3. **Keep comprehensive documentation** of all packages and versions in use

**Data Transfer Procedures**

1. **Use approved data diodes** or one-way transfer devices for bringing updates into the environment
2. **Implement strict media control** for any physical media entering the air-gapped environment
3. **Scan all incoming data** for malware before allowing it into the environment

**Monitoring and Logging**

1. **Deploy local monitoring solutions** that don't require internet access (such as Prometheus and Grafana)
2. **Establish baselines** for normal system behavior
3. **Implement centralized logging** for security analysis and troubleshooting
4. **Regular security audits** to ensure the environment remains secure

Additional Considerations
-------------------------

**Backup Strategy**

Implement comprehensive backup procedures that work within air-gapped constraints:

1. **Database backups** with tested restore procedures
2. **File storage backups** including user uploads and attachments
3. **Configuration backups** for all system settings
4. **Disaster recovery planning** specific to air-gapped limitations

**Compliance Requirements**

Ensure your air-gapped deployment meets organizational compliance needs:

1. **Data retention policies** configured appropriately
2. **Audit logging** enabled and properly configured
3. **Access controls** implemented according to security policies
4. **Documentation maintenance** for compliance reporting

For additional deployment guidance, refer to the main Mattermost :doc:`deployment documentation </deployment-guide/deployment-guide-index>` and adapt the instructions for your air-gapped environment using the resources gathered in the prerequisites section.