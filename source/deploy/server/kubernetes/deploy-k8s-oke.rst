.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

You can use the supported `Oracle Cloud Marketplace listing <https://cloudmarketplace.oracle.com/marketplace/en_US/listing/188386963>`__ to install Mattermost Enterprise Edition on Oracle Cloud Infrastructure (OCI) using Oracle Kubernetes Engine (OKE).

**Before you begin**

Before deploying, make sure you have the following:

- **Oracle Cloud Account**
- **Permissions** to create/manage OKE, Compute, Networking, Database, Resource Manager, and Secrets
- **Compartment** for deployment
- **Domain Name and TLS Certificate**
- **Mattermost License Key**

---

**Step 1: Start from Oracle Cloud Marketplace**

Go to the Mattermost listing and click **Launch Stack**.

.. image:: /_static/images/oracle/marketplace-listing.png
   :alt: Oracle Cloud Marketplace listing for Mattermost

---

## Step 2: Stack Information

On the **Create stack** page, check the information, set the name, compartment, and Terraform version.

.. image:: /_static/images/oracle/stack-info.png
   :alt: Stack information page

---

**Step 3: Configure Variables**

On this screen, you will set all the details for your Mattermost deployment. Each section is important for a successful and secure installation.

### OKE Cluster Configuration

- **Create new OKE Cluster:**  
  - Check this if you want to create a new Kubernetes cluster.  
  - If you already have a cluster, you can uncheck and select your existing one.
- **Kubernetes Version:**  
  - Choose the latest stable version unless you have a specific requirement.
- **Node Pool Shape (Flex/Fixed):**  
  - Select a shape that fits your workload. For production, use at least 2 OCPUs and 16GB RAM per node.
- **Number of Nodes:**  
  - Minimum 2 for high availability. For testing, 1 is enough.
- **Operating System:**  
  - Oracle Linux 8 is recommended for best compatibility.

**Tip:** For production, always use at least 2 nodes and enable high availability.

---

### OKE Network Configuration

- **Worker Node Visibility:**  
  - Private is more secure for production. Public is easier for testing.
- **API Endpoint Visibility:**  
  - Public allows you to manage the cluster from anywhere. Private is more secure but requires VPN or bastion.
- **Create new Virtual Cloud Network (VCN):**  
  - Check this to create a new network, or uncheck to use an existing one.
- **VCN CIDR Block:**  
  - Set a unique network range (e.g., `10.20.0.0/16`). Avoid overlap with other networks.

**Tip:** For production, use private nodes and restrict access to the API endpoint.

---

### OKE Worker Nodes

- **Enable Cluster Autoscaler:**  
  - Allows the cluster to automatically add or remove nodes based on usage.
- **Initial/Min Number of Worker Nodes:**  
  - Set the minimum number of nodes. For high availability, use at least 2.
- **Node Shape:**  
  - Choose a shape (e.g., `VM.Standard.E4.Flex`) and set OCPUs and memory.
- **Auto Generate SSH Key:**  
  - Enable this if you do not have your own SSH key for node access.
- **Image OS and Version:**  
  - Oracle Linux 8 is recommended.

**Tip:** Autoscaling helps manage costs and performance automatically.

---

### PostgreSQL Configuration

- **Admin Username:**  
  - The main user for your PostgreSQL database (e.g., `admin1`).
- **Password Type:**  
  - `PLAIN_TEXT` for testing, `SECRET` for production (uses Oracle Vault).
- **Password/Secret Name:**  
  - Enter a strong password or the name of a secret in Oracle Vault.
- **Database Password:**  
  - Required if not using a secret.

**Tip:** Always use Oracle Vault for production passwords.

---

### General Configuration

- **Cluster Name Prefix:**  
  - Used to identify all resources (e.g., `mm-oke`).
- **Show Advanced Options:**  
  - Enable for more control (encryption keys, SSH keys, etc.).
- **PostgreSQL Deployment Strategy:**  
  - Use "Database For PostgreSQL" for managed service.
- **Object Storage for File Storage:**  
  - Enable to use OCI Object Storage for Mattermost files.
- **Mattermost Version:**  
  - Use the latest stable version.
- **Namespace:**  
  - Default is `mattermost`.
- **License Key:**  
  - Upload or paste your Mattermost license.
- **Helm Repository:**  
  - Default is `https://helm.mattermost.com`.

**Tip:** Use advanced options if you need custom encryption or want to manage your own SSH keys.

---

Common Errors and How to Avoid Them
===================================

1. Invalid Password for PostgreSQL Database
-------------------------------------------

Error Example::

   Error: 400-InvalidParameter, Invalid Invalid password received.

Why this happens:
   The admin password for your PostgreSQL database does not meet Oracle Cloud's password policy.

OCI PostgreSQL Password Policy:

- Must be **8–30 characters** long
- Must include **at least 1 uppercase letter**
- Must include **at least 1 lowercase letter**
- Must include **at least 1 number**
- Must include **at least 1 special character** (Allowed: ``!@#$%^&*()_+=[]{}|:;<>,.?/``)

Example of a valid password::

   S3cur3P@ssword!

What to do:
   When setting the admin password, make sure it follows all the above rules. If you see this error, update your password and try again.

----

2. Invalid Compartment OCID in Object Storage
---------------------------------------------

Error Example::

   Error: 400-InvalidCompartmentId, OCID doesn't match expected pattern or contains invalid characters. var.tenacy_ocid

Why this happens:
   There is a typo in your Terraform variable name or the OCID value is not correct.

How to fix:

- Double-check your variable names. The correct variable is ``tenancy_ocid`` (not ``tenacy_ocid``).
- Make sure the value is a valid OCID, for example: ``ocid1.tenancy.oc1..aaaaaaaaxyz123...``

What to do:
   Correct the variable name and verify the OCID value. If you copy-paste, check for extra spaces or missing characters.

----

Summary Table
-------------

+--------------------------+--------------------------------------------------------------------------+
| Issue                    | Fix/Action                                                               |
+==========================+==========================================================================+
| Invalid DB password      | Use a strong password matching OCI policy (see above for requirements)   |
+--------------------------+--------------------------------------------------------------------------+
| Invalid compartment OCID | Correct the variable name to ``tenancy_ocid`` and verify its value/format|
+--------------------------+--------------------------------------------------------------------------+

Tip:
   If you see a 400 error, always check for typos, missing required fields, or values that do not match Oracle's requirements.

---

.. image:: /_static/images/oracle/configure-variables.png
   :alt: Configure stack variables

---

**Validation:**  
If you see errors or missing fields, check your permissions and quotas. Make sure all required fields are filled and passwords are strong.

---

## Step 4: Review and Apply

Check all your settings and click **Create** to start the deployment. Monitor the Resource Manager job and logs.

  .. image:: /_static/images/oracle/job-monitor.png
    :alt: Resource Manager job monitor

---

## Step 5: After Deployment

When the job is finished, your OKE cluster, PostgreSQL database, and Mattermost will be ready. To find the Mattermost web address, run:

.. code-block:: sh

   kubectl -n mattermost-operator get ingress

Copy the address and create a DNS record for your domain. Open your browser and go to your Mattermost URL.

---

## Tips for Success

- Make sure you have all the permissions you need before you start.
- Use Oracle Vault to store passwords and sensitive data.
- Use private nodes and secure your network for production.
- For more details, see the official `OCI Database with PostgreSQL documentation <https://www.oracle.com/cloud/postgresql/>`__ and `OKE documentation <https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm>`__.

---

.. important::

   You are responsible for Oracle Cloud Infrastructure costs for the resources you create. Oracle Cloud credits cannot be used to buy a Mattermost license.
