Downgrade Enterprise Edition to Team Edition
===========================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

This documentation describes how to downgrade Mattermost Enterprise Edition to Team Edition without data loss. This is useful when Enterprise features are no longer needed or when licenses expire.

.. important::

   - **Data preservation**: No data is lost when downgrading from Enterprise to Team Edition.
   - **Feature compatibility**: Enterprise-specific features will be disabled after downgrade.
   - **Testing recommended**: Test the downgrade process in a staging environment first.
   - **License implications**: Remove the Enterprise license key to complete the downgrade.

Overview
--------

Mattermost Enterprise Edition can be downgraded to Team Edition at any time without data loss. The process involves:

1. Disabling Enterprise-specific features
2. Removing the license key
3. Optionally replacing the binary (for certain deployment types)

The core Mattermost functionality remains identical between editions, ensuring seamless operation after downgrade.

Data handling during downgrade
------------------------------

**What happens to your data:**

- **User accounts**: All user accounts, passwords, and profile information are preserved
- **Messages and files**: All channel messages, direct messages, and file attachments remain intact  
- **Channels and teams**: All team and channel structures are maintained
- **Integrations**: Basic integrations continue to work; Enterprise-specific integrations are disabled
- **System settings**: Core configuration settings are preserved; Enterprise settings become inactive

**Enterprise features that will be disabled:**

- Advanced authentication (SAML, OAuth 2.0, AD/LDAP sync)
- Guest accounts
- Advanced permissions and granular administration
- Compliance exports and data retention policies
- High availability clustering
- Read replicas
- Elasticsearch/OpenSearch
- Advanced reporting and analytics
- Enterprise integrations and plugins

Preparation steps
-----------------

Before downgrading, complete these preparation steps:

1. **Back up your system**: Create full backups of your database and application files as described in the :doc:`backup and disaster recovery </deployment-guide/backup-disaster-recovery>` documentation.

2. **Review Enterprise features in use**: 

   a. Go to **System Console > About > Enterprise Edition** to see active Enterprise features
   b. Document any Enterprise-specific configurations you may need to reconfigure
   c. Notify users about upcoming changes to Enterprise features

3. **Prepare alternative authentication**: If using Enterprise authentication methods (SAML, LDAP, etc.), ensure you have alternative login methods available for administrators.

4. **Export compliance data**: If using compliance features, export any required data before downgrading.

General downgrade process
-------------------------

This process applies to most deployment types. Specific deployment scenarios are covered in the sections below.

1. **Disable Enterprise features**:

   a. Go to **System Console > Authentication** and disable any Enterprise authentication methods
   b. Go to **System Console > User Management** and convert any guest accounts to regular users if needed
   c. Review and disable any Enterprise-specific system settings

2. **Remove the license key**:

   a. Go to **System Console > Edition and License**
   b. Select **Remove License and Downgrade**
   c. Confirm the downgrade action

3. **Restart the server**: Restart your Mattermost server to complete the downgrade

4. **Verify the downgrade**: Check that **System Console > About** shows "Mattermost Team Edition"

Deployment-specific procedures
------------------------------

High availability environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For High Availability deployments:

.. important::
   High Availability clustering is an Enterprise feature. After downgrading, only one server node will remain active.

1. **Choose a primary node**: Identify which server will remain active after downgrade
2. **Stop secondary nodes**: Shut down all secondary Mattermost servers in the cluster
3. **Update load balancer**: Configure your load balancer to direct all traffic to the primary node
4. **Follow general downgrade process**: Complete the standard downgrade on the primary node
5. **Update proxy configuration**: Remove references to secondary nodes from your proxy configuration

**Post-downgrade considerations:**
- Database remains shared and accessible
- File storage should be accessible from the remaining active node
- Consider implementing traditional backup strategies to replace HA redundancy

Connected workspaces (shared channels)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For environments using connected workspaces:

.. important::
   Connected workspaces are an Enterprise feature and will be disabled after downgrade.

1. **Document shared channels**: Record which channels are shared between workspaces
2. **Notify stakeholders**: Inform users that shared channels will become local channels
3. **Export shared content**: Export any critical content from shared channels if needed
4. **Follow general downgrade process**: Complete the standard downgrade procedure
5. **Reconfigure collaboration**: Set up alternative methods for cross-workspace collaboration

Docker deployments
~~~~~~~~~~~~~~~~~~~

For Docker-based deployments:

1. **Stop the Mattermost container**:

   .. code-block:: bash

      docker stop mattermost

2. **Complete the license removal**:

   a. Start the container temporarily to access the System Console
   b. Follow the general downgrade process to remove the license
   c. Stop the container again

3. **Update Docker image** (optional):

   You can continue using the Enterprise Edition docker image (it will function as Team Edition) or switch to Team Edition image:

   .. code-block:: bash

      # Option A: Continue with Enterprise image (functions as Team Edition)
      docker start mattermost

      # Option B: Switch to Team Edition image  
      docker pull mattermost/mattermost-team-edition:latest
      # Update your docker-compose.yml or startup scripts
      docker start mattermost

4. **Verify downgrade**: Check the System Console shows "Mattermost Team Edition"

Kubernetes deployments
~~~~~~~~~~~~~~~~~~~~~~~

For Kubernetes deployments using Helm charts or operators:

1. **Scale down the deployment**:

   .. code-block:: bash

      kubectl scale deployment mattermost --replicas=0

2. **Access the database directly** to remove the license (if needed):

   .. code-block:: bash

      # Connect to your database and remove license
      kubectl exec -it <postgres-pod> -- psql -U mattermost -d mattermost
      DELETE FROM Licenses;

3. **Update deployment configuration**:

   a. Edit your Helm values or deployment manifests
   b. Remove Enterprise-specific configurations (HA settings, replicas > 1, etc.)
   c. Optionally change container image to Team Edition

4. **Apply updated configuration**:

   .. code-block:: bash

      # For Helm
      helm upgrade mattermost mattermost/mattermost-team-edition -f values.yaml

      # For kubectl
      kubectl apply -f mattermost-deployment.yaml

5. **Scale back up**:

   .. code-block:: bash

      kubectl scale deployment mattermost --replicas=1

Azure Marketplace Container deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Azure Container Instances deployments:

1. **Stop the container instance**:

   .. code-block:: bash

      az container stop --name mattermost --resource-group myResourceGroup

2. **Update container configuration**:

   a. Follow general downgrade process using Azure CLI or portal
   b. Optionally update container image to Team Edition
   c. Remove Enterprise-specific environment variables

3. **Restart container**:

   .. code-block:: bash

      az container start --name mattermost --resource-group myResourceGroup

Oracle Cloud Marketplace deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Oracle Cloud deployments:

1. **Stop the compute instance**:

   Use Oracle Cloud Console or CLI to stop the Mattermost instance

2. **Follow general downgrade process**:

   a. Start the instance in maintenance mode if available
   b. Access the System Console and remove the license key
   c. Complete the standard downgrade procedure

3. **Update instance configuration**:

   Remove any Enterprise-specific configurations from the Oracle Cloud deployment

4. **Restart the instance**: Start the compute instance normally

Linux deployments (tarball)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For manual installations via tarball:

1. **Stop Mattermost service**:

   .. code-block:: bash

      sudo systemctl stop mattermost

2. **Follow general downgrade process**:

   a. Start Mattermost temporarily: ``sudo systemctl start mattermost``
   b. Access System Console and remove the license key
   c. Stop the service again: ``sudo systemctl stop mattermost``

3. **Optional: Replace binary with Team Edition**:

   .. code-block:: bash

      # Download Team Edition binary
      wget https://releases.mattermost.com/[VERSION]/mattermost-team-[VERSION]-linux-amd64.tar.gz
      
      # Extract and replace (backup current installation first)
      sudo tar -xzf mattermost-team-[VERSION]-linux-amd64.tar.gz -C /opt/

4. **Restart service**:

   .. code-block:: bash

      sudo systemctl start mattermost

Ubuntu deployments
~~~~~~~~~~~~~~~~~~~

For Ubuntu package installations:

1. **Stop Mattermost**:

   .. code-block:: bash

      sudo systemctl stop mattermost

2. **Remove license via database** (if System Console is inaccessible):

   .. code-block:: bash

      sudo -u postgres psql mattermost
      DELETE FROM Licenses;
      \q

3. **Optionally install Team Edition package**:

   .. code-block:: bash

      # Remove Enterprise package
      sudo apt remove mattermost

      # Install Team Edition package  
      sudo apt install mattermost-team

4. **Start service**:

   .. code-block:: bash

      sudo systemctl start mattermost

RHEL/CentOS deployments
~~~~~~~~~~~~~~~~~~~~~~~

For Red Hat Enterprise Linux/CentOS installations:

1. **Stop Mattermost service**:

   .. code-block:: bash

      sudo systemctl stop mattermost

2. **Follow general downgrade process** or remove license via database:

   .. code-block:: bash

      sudo -u postgres psql mattermost -c "DELETE FROM Licenses;"

3. **Optionally switch packages**:

   .. code-block:: bash

      # Remove Enterprise RPM
      sudo yum remove mattermost

      # Install Team Edition RPM
      sudo yum install mattermost-team

4. **Start service**:

   .. code-block:: bash

      sudo systemctl start mattermost

Post-downgrade verification
---------------------------

After completing the downgrade process:

1. **Verify edition**: Check **System Console > About** displays "Mattermost Team Edition"

2. **Test core functionality**:

   - User login and authentication
   - Channel messaging and file uploads  
   - Basic integrations and webhooks
   - Mobile and desktop app connectivity

3. **Review system settings**: Ensure all configurations are appropriate for Team Edition

4. **Update documentation**: Document the change for your users and support team

5. **Monitor system health**: Watch for any issues in the first few days after downgrade

Troubleshooting
---------------

License removal fails
~~~~~~~~~~~~~~~~~~~~~~

If you cannot remove the license through the System Console:

1. **Stop the Mattermost server**
2. **Access the database directly**:

   .. code-block:: sql

      DELETE FROM Licenses;

3. **Restart the server**

Enterprise features still showing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If Enterprise features appear to still be active:

1. **Clear browser cache** and reload the System Console
2. **Restart the Mattermost server**
3. **Check for multiple license entries** in the database

Authentication issues after downgrade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If users cannot log in after downgrade:

1. **Verify basic authentication is enabled** in System Console
2. **Reset passwords** for affected admin accounts if needed
3. **Check database connectivity** and user account status

Reverting the downgrade
~~~~~~~~~~~~~~~~~~~~~~~~

To upgrade back to Enterprise Edition:

1. **Install a valid Enterprise license key**
2. **Re-enable desired Enterprise features**
3. **Follow the :doc:`upgrade documentation </administration-guide/upgrade/enterprise-install-upgrade>` for detailed steps**

Getting help
------------

If you encounter issues during the downgrade process:

1. **Check the troubleshooting section** above
2. **Review system logs** for error messages
3. **Contact Mattermost support** if you have an active support agreement
4. **Visit the Mattermost community forums** for community assistance

For questions about feature compatibility or technical requirements, refer to the `Mattermost feature comparison <https://mattermost.com/pricing/>`_ documentation.