:orphan:
:nosearch:

Mattermost is published as an **Azure Marketplace** solution that provisions a production-style Mattermost stack in your own subscription using Azure-managed services for compute, database, shared file storage, and load balancing. This option is intended for organizations that want a resilient Mattermost deployment they can scale and operate within their existing Azure tenant.

Prerequisites
-------------

* An active **Azure subscription** with permission to create resource groups and accept **Azure Marketplace** billing terms for the offer.
* Familiarity with the **Azure portal** (resource groups, networking, virtual machines, and Application Gateway).
* For multi-node deployments (more than one application instance), a valid **Mattermost Enterprise license** file. Single-node deployments do not require a license.
* If you plan to enable **HTTPS** at deployment time:

  * A **PFX (PKCS#12)** certificate bundle and its password.
  * A **custom domain (FQDN)** that you will point to the Application Gateway after deployment.

What gets deployed
------------------

The template provisions a self-contained, production-style stack in the resource group you select, including:

1. **Virtual Machine Scale Set (Linux):** Runs Mattermost on Ubuntu Pro 24.04 LTS images published by Mattermost. Instance count and VM size are driven by the scaling tier you choose.
2. **Application Gateway with public IP:** Acts as the entry point for Mattermost traffic, with optional **HTTPS listener** (using your PFX certificate) and HTTP-to-HTTPS redirection when HTTPS is enabled.
3. **Azure Database for PostgreSQL Flexible Server:** Managed PostgreSQL service that stores Mattermost data, with optional **same-zone** or **zone-redundant** high availability and configurable backup retention and geo-redundancy.
4. **Azure Files (NFS) with private endpoint:** Shared storage for Mattermost data (uploads, plugins, and other shared files), reachable only from inside the virtual network.
5. **Virtual network and subnets:** A dedicated VNet for the deployment, with separate subnets for the Application Gateway, the Mattermost application instances, the database, and the storage private endpoint.
6. **NAT gateway:** Provides controlled outbound internet access for the application instances (for example, to fetch packages and the Mattermost configuration scripts).
7. **Private DNS zones:** Used to resolve the PostgreSQL Flexible Server and Azure Files private endpoint from inside the VNet.

Step 1: Select a plan and start creation
----------------------------------------

Open the **Mattermost - Azure-Native (VM-based)** offer in the Azure Marketplace, click **Get it now**, select the plan, and then click **Create** to open the deployment wizard.

Step 2: Basics
--------------

On the **Basics** tab, configure the following:

1. **Subscription:** Choose the Azure subscription where the deployment will live.
2. **Resource group:** Select an existing resource group or create a new one. A **new** resource group keeps the production stack easy to manage and clean up.
3. **Region:** Select the deployment region. Choose a region that supports the PostgreSQL Flexible Server SKUs you plan to use, and that has the **availability zones** you need if you intend to enable PostgreSQL high availability.
4. **Resource name prefix:** Short prefix (2–12 lowercase letters, digits, or hyphens) used to name the Azure resources created by the template (for example, ``mm-prod``).

Step 3: Application
-------------------

On the **Application** tab, configure how the Mattermost application is sized and how administrators access the VMs.

1. **Scaling tier:** Pick the user scale you are planning for. The wizard uses this to suggest sensible defaults for the **VMSS instance count**, **VM size**, and **PostgreSQL SKU**, and to determine whether **read replicas** are created for the database. Suggested tiers:

   * **Up to 200 users:** 1 node, ``Standard_F2s_v2``.
   * **Up to 2,000 users:** 2 nodes, ``Standard_F2s_v2``.
   * **Up to 15,000 users:** 2 nodes, ``Standard_F4s_v2``.
   * **Up to 30,000 users:** 2 nodes, ``Standard_F8s_v2``.

2. **VMSS instance count:** Number of Mattermost application nodes (1–20). Defaults to the suggested value for your scaling tier; adjust if needed.
3. **Enterprise license file:** Required when the instance count is greater than 1 (multi-node high-availability clustering). Upload your Mattermost Enterprise license file. Single-node deployments don't require a license.
4. **VM SKU:** Size of each VMSS instance. The wizard surfaces recommended Linux sizes first; you can select any supported Linux size available in your region.
5. **Admin username:** Linux administrator account used to sign in to the VM instances.
6. **Authentication type:** Choose **Password** or **SSH public key** for Linux sign-in. **SSH public key** is recommended for production deployments.
7. **Mattermost Version:** The Mattermost version to install (for example, ``11.6.0``). See `the Mattermost release policy <https://docs.mattermost.com/product-overview/release-policy.html>`_ for supported versions.

Step 4: Database
----------------

On the **Database** tab, configure the managed PostgreSQL service and the shared NFS file share.

1. **PostgreSQL compute SKU:** Memory-optimized Flexible Server SKU. Defaults to the SKU recommended for your scaling tier; pick a SKU that is supported in your region. Available choices include ``Standard_E2ads_v5/v6``, ``Standard_E4ads_v5/v6``, and ``Standard_E8ads_v5/v6``.
2. **PostgreSQL high availability:** Choose how PostgreSQL is made resilient:

   * **Disabled:** Single primary instance. Suitable for small deployments and lower-cost evaluations.
   * **Same zone:** Primary and standby in the same availability zone.
   * **Zone redundant:** Primary and standby in different availability zones; recommended for production HA.

3. **Primary availability zone** and **standby availability zone:** Shown when HA is enabled. For zone-redundant HA, the primary and standby zones must be different. Pick zones supported in your region for the PostgreSQL SKU you chose.
4. **PostgreSQL admin username and password:** Administrator credentials for the Flexible Server. Avoid reserved names such as ``azure_superuser``. The password must meet `Azure Flexible Server password complexity requirements <https://learn.microsoft.com/azure/postgresql/flexible-server/concepts-security#password>`_.
5. **NFS share size (GiB):** Size of the Azure Files (NFS) share used by Mattermost for shared application data. Minimum 100 GiB.
6. **Geo-redundant backup:** Replicates PostgreSQL backups to Azure's paired region for cross-region disaster recovery. Recommended for production. **This setting cannot be changed after deployment.**

.. note::

  Backup retention for PostgreSQL is set to 35 days at deployment time. You can change retention from the Azure portal after the deployment completes.

Step 5: Networking
------------------

On the **Networking** tab, configure the virtual network and how Mattermost is exposed to users.

1. **VNet address space (CIDR):** The address space for the virtual network created by the template. Defaults to ``10.0.0.0/22``. Pick a range that does not overlap with other VNets you plan to peer with.
2. **Public IP DNS label:** DNS label for the Application Gateway public IP. The wizard generates a default; you can override it. The label must be **globally unique** in the region. Once deployed, your Azure-assigned URL will be in the form ``<dns-label>.<region>.cloudapp.azure.com``.
3. **Enable HTTPS on Application Gateway:** When enabled, the Application Gateway terminates TLS using your PFX certificate and HTTP traffic is redirected to HTTPS. When disabled, Mattermost is served over HTTP on the Azure-assigned hostname (suitable for testing, **not recommended for production**).
4. **PFX certificate** and **PFX password:** Shown when HTTPS is enabled. Upload your PKCS#12 bundle and provide the password used to protect it.
5. **Custom domain (FQDN):** Shown when HTTPS is enabled. The public hostname Mattermost will use (for example, ``mattermost.example.com``). After deployment, you must create a **CNAME** record pointing this hostname to the Azure-assigned DNS name of the Application Gateway public IP.

Step 6: Review and create
-------------------------

Review your settings, accept any **Marketplace** terms if prompted, then select **Create**. Provisioning the full stack typically takes longer than a single-VM deployment because of the database, storage, and Application Gateway resources. First-boot configuration on the Mattermost instances may take additional time before the application is reachable.

**After deployment completes:**

* In the Azure portal, open the **resource group** you used.
* Open the **Application Gateway public IP** resource (named ``<prefix>-ag-pip``). Under **Essentials**, note the **DNS name** (Azure-assigned FQDN).
* If you deployed **without HTTPS**, your site URL is:

  ``http://<dns-label>.<region>.cloudapp.azure.com``

* If you deployed **with HTTPS**, create a **CNAME** record at your DNS provider that points your **custom domain** to the Azure-assigned DNS name of the Application Gateway public IP. Once DNS propagates, your site URL is:

  ``https://<your-custom-domain>``

Step 7: Open Mattermost and create your administrator
-----------------------------------------------------

In a browser, go to your Mattermost URL. Mattermost will prompt you to **create the first user**, which becomes the **System Administrator**. That account is different from the **Linux** username and password (or SSH key) you configured in Step 3.

Congratulations! You've successfully deployed a production-style Mattermost stack on Azure.

Next steps
----------

* For sizing guidance and reference architectures, see :doc:`high-availability-cluster-based-deployment </administration-guide/scale/high-availability-cluster-based-deployment>` and :doc:`server architecture </administration-guide/scale/server-architecture>`.
* For ongoing operations (upgrades, backups, monitoring), follow the standard Mattermost server administration documentation.
