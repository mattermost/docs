.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

You can use the supported `Oracle Cloud Marketplace listing <https://cloudmarketplace.oracle.com/marketplace/en_US/listing/188386963>`_ to install Mattermost Enterprise Edition on Oracle Cloud Infrastructure (OCI) using Oracle Kubernetes Engine (OKE).

**Before you begin**

Before deploying, make sure you have the following:

- **Oracle Cloud Account** with appropriate permissions
- **Permissions** to create/manage OKE, Compute, Networking, Database, Resource Manager, and Secrets
- **Compartment** for deployment
- **Domain Name and TLS Certificate** for secure access
- **Mattermost License Key** (Trial or Enterprise)
- **Node Capacity**: At least 2 OKE nodes for high availability when deploying for 100 users or more

**Installation steps**

The installation process includes deploying Mattermost and configuring the necessary components.

**Step 1: Start from Oracle Cloud Marketplace**

Go to the Mattermost listing and select **Launch Stack**.

.. image:: /images/oracle/marketplace-listing.png
   :alt: Oracle Cloud Marketplace listing for Mattermost

**Step 2: Stack Information**

On the **Create stack** page, review the information, and then set the name, compartment, and Terraform version.

.. image:: /images/oracle/stack-info.png
   :alt: Stack information page

**Step 3: Configure Variables**

Set all the details for your Mattermost deployment. Each section is important for a successful and secure installation.

**OKE Cluster Configuration**

- **Create new OKE Cluster:**

  - Check this if you want to create a new Kubernetes cluster.  
  - If you already have a cluster, you can uncheck and select your existing one.
- **Kubernetes Version:**

  - Choose the latest stable version unless you have a specific requirement.
- **Node Pool Shape (Flex/Fixed):**

  - Select a shape that fits your workload. For production, use at least 2 OCPUs and 16GB RAM per node.
- **Number of Nodes:**

  - Minimum 2 for high availability. For testing, 1 is enough. For production environments, always use at least 2 nodes and enable high availability.
- **Operating System:**

  - Oracle Linux 8 is recommended for best compatibility.

**OKE Network Configuration**

- **Worker Node Visibility:**

  - Private is more secure for production. Public is easier for testing. For production environments, use private nodes and restrict access to the API endpoint.
- **API Endpoint Visibility:**

  - Public allows you to manage the cluster from anywhere. Private is more secure but requires VPN or bastion.
- **Create new Virtual Cloud Network (VCN):**

  - Check this to create a new network, or uncheck to use an existing one.
- **VCN CIDR Block:**

  - Set a unique network range (e.g., ``10.20.0.0/16``). Avoid overlap with other networks.

**OKE Worker Nodes**

- **Enable Cluster Autoscaler:**

  - Allows the cluster to automatically add or remove nodes based on usage.
- **Initial/Min Number of Worker Nodes:**

  - Set the minimum number of nodes. For high availability, use at least 2. Autoscaling helps manage costs and performance automatically.
- **Node Shape:**

  - Choose a shape (e.g., ``VM.Standard.E4.Flex``) and set OCPUs and memory.
- **Auto Generate SSH Key:**

  - Enable this if you do not have your own SSH key for node access.
- **Image OS and Version:**

  - Oracle Linux 8 is recommended.

**PostgreSQL Configuration**

- **Admin Username:**

  - The main user for your PostgreSQL database (e.g., ``admin1``).
- **Password Type:**

  - ``PLAIN_TEXT`` for testing, ``SECRET`` for production (uses Oracle Vault). Always use Oracle Vault for production passwords.
- **Password/Secret Name:**

  - Enter a strong password or the name of a secret in Oracle Vault.
- **Database Password:**

  - Required if not using a secret.

**General Configuration**

- **Cluster Name Prefix:**

  - Used to identify all resources (e.g., ``mm-oke``).
- **Show Advanced Options:**

  - Enable for more control (encryption keys, SSH keys, etc.). Use advanced options if you need custom encryption or want to manage your own SSH keys.
- **PostgreSQL Deployment Strategy:**

  - Use "Database For PostgreSQL" for managed service.
- **Object Storage for File Storage:**

  - Enable to use OCI Object Storage for Mattermost files.
- **Mattermost Version:**

  - Use the latest stable version.
- **Namespace:**

  - Default is ``mattermost``.
- **License Key:**

  - Upload or paste your Mattermost license.
- **Helm Repository:**

  - Default is ``https://helm.mattermost.com``.

**Step 4: Review and Apply**

Check all your settings and select **Create** to start the deployment. Monitor the Resource Manager job and logs.

.. image:: /images/oracle/job-monitor.png
   :alt: Resource Manager job monitor

**Step 5: After Deployment**

When the job is finished, your OKE cluster, PostgreSQL database, and Mattermost will be ready. To find the Mattermost web address, run:

.. code-block:: sh

   kubectl -n mattermost-operator get ingress

Copy the address and create a DNS record for your domain. Open your browser and go to your Mattermost URL.

**Step 6: Upgrade Mattermost**

To upgrade your Mattermost installation:

1. Access your OKE cluster through the Oracle Cloud Console
2. Navigate to the Mattermost operator deployment
3. Update the Mattermost version in the configuration
4. Apply the changes and wait for the upgrade to complete

.. tip::

  **Tips for Success**

  - Make sure you have all the permissions you need before you start.
  - Use Oracle Vault to store passwords and sensitive data.
  - Use private nodes and secure your network for production.
  - Always monitor logs from the Resource Manager and pods using ``kubectl logs`` for more specific error messages.
  - For more details, see the official `OCI Database with PostgreSQL documentation <https://www.oracle.com/cloud/postgresql/>`_ and `OKE documentation <https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm>`_.

**Common Errors and How to Avoid Them**

- **Error: Kubernetes API not reachable**

  - *Cause:* API endpoint is private and you're not connected to the VCN via VPN or Bastion.
  - *Solution:* Ensure you have access to the network or make the endpoint public for testing.

- **Error: Stack creation fails with missing permissions**

  - *Cause:* IAM policies are not set properly for the user or group.
  - *Solution:* Ensure you have permissions for Resource Manager, OKE, Networking, and Secrets.

- **Error: No ingress returned by kubectl**

  - *Cause:* Mattermost Ingress might not be ready or was misconfigured.
  - *Solution:* Check with ``kubectl describe ingress`` and validate DNS, TLS, and Helm values.

- **Error: PostgreSQL password rejected**

  - *Cause:* Password not set or mismatched with Oracle Vault.
  - *Solution:* Re-check the password value or Vault secret used during setup.

.. important::

   You are responsible for Oracle Cloud Infrastructure costs for the resources you create. Oracle Cloud credits cannot be used to buy a Mattermost license.

Learn more about managing your Mattermost server by visiting the :doc:`Administration Guide </guides/administration-guide>`.