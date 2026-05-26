Configure Azure Blob Storage as the Mattermost file store
==========================================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Mattermost can store user uploads -- attachments, profile images, plugin assets, emoji, compliance exports -- in an Azure Storage account. This guide walks an administrator through the steps to provision the Azure side and point a Mattermost server at it via the System Console.

Prerequisites
-------------

- An Azure subscription where you can create resources, with **Storage Account Contributor** or higher on the target resource group.
- Either the Azure portal, or the `Azure CLI <https://learn.microsoft.com/en-us/cli/azure/install-azure-cli>`__ (``az``) installed and signed in with ``az login``. Both are documented below.
- A Mattermost deployment (v11.x or later) with System Console access for a System Admin account.

If you plan to migrate existing files from another backend, take a backup of the current storage location (S3 bucket, local disk, etc.) before changing the configuration. Switching the file driver does not migrate existing files automatically.

Step 1: Create a storage account
--------------------------------

Pick a globally unique name for the storage account (3-24 characters, lowercase letters and numbers only). The name becomes part of the public DNS host ``<account>.blob.core.windows.net``, so customers usually pick something like ``acmemattermost`` or ``mattermost<env>``.

**Azure portal**

1. Go to **Storage accounts** > **Create**.
2. Choose the subscription and resource group. Create a new resource group if needed.
3. Enter the storage account name and region.
4. **Performance**: *Standard*. **Redundancy**: *Locally-redundant storage (LRS)* for a single-region deployment, or *Geo-redundant storage (GRS)* for cross-region durability.
5. On the **Advanced** tab, set **Minimum TLS version** to ``1.2`` and leave **Allow Blob anonymous access** disabled. Mattermost serves files through its own authenticated API and the container does not need to be public.
6. Select **Review + create**.

**Azure CLI**

.. code-block:: bash

  az group create \
      --name mm-prod-files \
      --location eastus

  az storage account create \
      --name acmemattermost \
      --resource-group mm-prod-files \
      --location eastus \
      --sku Standard_LRS \
      --kind StorageV2 \
      --min-tls-version TLS1_2 \
      --allow-blob-public-access false

Step 2: Create a container
--------------------------

All Mattermost uploads land in a single container. The container name must be lowercase and may contain letters, numbers, and hyphens (3-63 characters).

**Azure portal**

1. Open the storage account, then **Containers** > **+ Container**.
2. Name it (for example, ``mattermost``).
3. **Public access level**: **Private (no anonymous access)**.

**Azure CLI**

.. code-block:: bash

  az storage container create \
      --name mattermost \
      --account-name acmemattermost \
      --auth-mode login

Step 3: Choose an authentication mode
-------------------------------------

Mattermost supports two ways for the server to authenticate to Azure. Pick the one that fits how the server runs:

- **Shared key**: the server signs each request with the Storage Account access key. Works anywhere Mattermost runs (on-premises, non-Azure cloud, local development) because it does not depend on the host having an Azure identity. The trade-off is that the key is a long-lived secret stored in ``config.json``.
- **Default credential (Microsoft Entra ID)**: the server obtains a token from Microsoft Entra ID and signs requests with it. No long-lived secret in Mattermost configuration. This is the recommended mode for deployments running on Azure, where the host environment already provides an identity (managed identity on Azure VM / App Service / AKS, workload identity for federated workloads, or a service principal).

The Azure-side setup differs slightly between the two modes. Follow the subsection that matches your choice; you can switch modes later by changing the **Azure authentication** setting in the System Console.

Option A: Shared key
~~~~~~~~~~~~~~~~~~~~

Retrieve the Storage Account access key.

**Azure portal**

1. Open the storage account, then **Security + networking** > **Access keys**.
2. Select **Show** next to ``key1`` (or ``key2``) and copy the value.

**Azure CLI**

.. code-block:: bash

  az storage account keys list \
      --account-name acmemattermost \
      --resource-group mm-prod-files \
      --query "[0].value" -o tsv

.. note::

  Treat the shared key as a secret -- anyone with it has full access to the account. Azure provides two keys so you can rotate without downtime: update Mattermost to ``key2``, regenerate ``key1``, then swap on the next rotation cycle. Plan a rotation cadence that matches your organisation's policy.

Option B: Default credential (Microsoft Entra ID)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The server uses ``DefaultAzureCredential`` from the Azure SDK, which discovers a working identity at runtime in this order: ``EnvironmentCredential`` (service-principal environment variables), ``WorkloadIdentityCredential`` (federated workload identity), ``ManagedIdentityCredential`` (the platform-provided managed identity), then ``AzureCLICredential`` (the signed-in ``az`` session, useful for local development). The first source that returns a token is used.

Whichever identity the SDK selects, **that** identity needs **Storage Blob Data Contributor** (or a custom role with the equivalent ``read/write/list/delete`` data-plane actions) on the storage account or container. Without it, ``TestConnection`` returns ``AuthorizationPermissionMismatch``.

Pick the identity source that matches the host:

.. list-table::
  :header-rows: 1
  :widths: 25 75

  * - Host
    - Identity source
  * - Azure VM, App Service, AKS, Container Apps
    - Assign a **system-assigned** or **user-assigned managed identity** to the compute resource. ``DefaultAzureCredential`` resolves to ``ManagedIdentityCredential`` with no extra configuration. For user-assigned identities, set ``AZURE_CLIENT_ID`` in the server's environment so the SDK picks the right one.
  * - AKS with workload-identity federation
    - Annotate the Mattermost ``ServiceAccount`` with the client ID and configure the OIDC issuer per the `AKS workload identity guide <https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview>`__. ``DefaultAzureCredential`` resolves to ``WorkloadIdentityCredential``.
  * - Non-Azure host or container
    - Create a service principal and set ``AZURE_TENANT_ID``, ``AZURE_CLIENT_ID``, and ``AZURE_CLIENT_SECRET`` (or ``AZURE_CLIENT_CERTIFICATE_PATH``) in the server's environment. ``DefaultAzureCredential`` resolves to ``EnvironmentCredential``.
  * - Local development on an admin's workstation
    - Sign in with ``az login``. ``DefaultAzureCredential`` resolves to ``AzureCLICredential``.

Assign the role with the Azure CLI (substituting the principal of the identity Mattermost will authenticate as):

.. code-block:: bash

  STORAGE_ACCOUNT_ID=$(az storage account show \
      --name acmemattermost \
      --resource-group mm-prod-files \
      --query id -o tsv)

  # For a managed identity (system-assigned on a VM/App Service/AKS pod):
  az role assignment create \
      --assignee-object-id "<principalId-of-the-managed-identity>" \
      --assignee-principal-type ServicePrincipal \
      --role "Storage Blob Data Contributor" \
      --scope "$STORAGE_ACCOUNT_ID"

  # For a service principal:
  az role assignment create \
      --assignee "<appId-of-the-service-principal>" \
      --role "Storage Blob Data Contributor" \
      --scope "$STORAGE_ACCOUNT_ID"

.. note::

  Granting the role requires **User Access Administrator** or **Owner** on the storage account; ``Contributor`` is not enough. Plan to have an administrator with that role run the ``az role assignment create`` step. If you scope the role to a single container instead of the whole storage account, replace ``--scope "$STORAGE_ACCOUNT_ID"`` with ``--scope "$STORAGE_ACCOUNT_ID/blobServices/default/containers/<container>"``. Functionally equivalent for Mattermost, narrower in blast radius.

.. tip::

  Azure RBAC role assignments can take 30-120 seconds to propagate. If the first ``TestConnection`` returns ``AuthorizationPermissionMismatch`` immediately after the role assignment, wait a minute and retry before assuming a misconfiguration.

Step 4: Configure Mattermost
----------------------------

Sign in as a System Admin and open **System Console > Environment > File Storage**.

1. **File storage system**: select **Azure Blob Storage**. The Azure-specific fields appear and the S3/local fields are hidden.
2. **Azure cloud**: select the Azure cloud that hosts the storage account:

   - **Azure Commercial** (default): the global Azure cloud (``{account}.blob.core.windows.net``). Only the storage account name is required.
   - **Azure Government**: the US Government cloud (``{account}.blob.core.usgovcloudapi.net``). Only the storage account name is required.
   - **Custom Endpoint**: any other Azure cloud (for example, Azure China), an Azurite emulator, or a reverse proxy. Provide the full Blob service URL via **Azure endpoint** below.

3. **Azure Storage account**: the storage account name from step 1 (for example, ``acmemattermost``).
4. **Azure container**: the container name from step 2 (for example, ``mattermost``).
5. **Azure path prefix**: optional. Set this if you want Mattermost to write under a sub-path inside the container, for example ``prod/``. Leave empty to use the container root.
6. **Azure authentication**: select the mode you set up in step 3:

   - **Shared key** (default): Mattermost signs each request with the Storage Account access key. Choose this if you completed `Option A: Shared key`_.
   - **Default credential (Microsoft Entra ID)**: Mattermost authenticates as the identity provided by the host environment. Choose this if you completed `Option B: Default credential (Microsoft Entra ID)`_. The **Azure Storage account key** field below is hidden because the access key is not used in this mode.

7. **Azure Storage account key** (visible only when **Azure authentication** is **Shared key**): paste the shared key from `Option A: Shared key`_.
8. **Azure endpoint** (visible only when **Azure cloud** is set to **Custom Endpoint**): the full Blob service URL, including scheme and storage account. Mattermost passes this URL to the Azure SDK unchanged, so the storage account must already be embedded in the hostname (vhost-style, for example ``https://acmemattermost.blob.core.chinacloudapi.cn/``) or in the path (path-style, for example ``http://localhost:10000/devstoreaccount1/`` for Azurite). The chosen authentication mode signs against the host this URL points at, so the host must serve the storage account named above.
9. **Enable secure Azure Blob Storage connections** (visible only when **Azure cloud** is **Azure Commercial** or **Azure Government**): keep this enabled (the default). The Custom Endpoint cloud determines the scheme from the **Azure endpoint** URL, so this toggle is hidden for that mode.
10. **Azure request timeout (milliseconds)**: default is ``30000`` (30 seconds). Increase only if your network needs more time for large objects.

Select **Test Connection**. Mattermost issues a no-op write/read/delete against the configured container using the credentials submitted in the form. A green ``Connection was successful`` message confirms the credentials, container name, and endpoint all work. A red error message includes the underlying reason; common ones are listed in `Troubleshooting`_.

Once the test succeeds, select **Save**.

.. warning::

  **Restart required.** The Mattermost server caches the file storage backend at startup and does not re-create it when the file storage configuration changes. After saving, restart every Mattermost server in the deployment (``systemctl restart mattermost``, recycle the container, or roll the deployment in your cluster) for the new driver to take effect. **Test Connection** works before the restart because it builds a temporary backend from the submitted form values.

.. note::

  Switching the file driver does **not** migrate existing files. If you are moving an existing deployment from Amazon S3, see `Migrate existing files from Amazon S3`_ below before changing the driver. For migrations from local disk, copy the directory contents into the Azure container using ``azcopy`` (`docs <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10>`__). In either case, files uploaded before the switch are unreachable once the driver changes unless they are present at the same key in the destination.

Step 5: Verify
--------------

1. After the restart, reload the System Console or any channel.
2. Upload an attachment in any channel. A small image is a good test, because Mattermost stores three blobs for an image (original, preview, thumbnail), which exercises the upload path more thoroughly than a plain file.
3. The post should render the attachment and preview as usual.
4. In the Azure portal, open the container and confirm new blobs appeared under the path ``<YYYYMMDD>/teams/<team>/channels/<channel>/users/<user>/<file_id>/`` (the same layout the local-disk and S3 backends use). For an image you will see ``<name>.<ext>``, ``<name>_preview.<ext>``, and ``<name>_thumb.<ext>``.

Migrate existing files from Amazon S3
-------------------------------------

If you are switching an existing deployment from S3 to Azure Blob Storage, the file content must be present in the Azure container at the same key Mattermost would have written to. Mattermost itself does not move files between backends, so this is an out-of-band copy that you run once before flipping the driver.

Mattermost writes blobs at the same relative path on every backend:

.. code-block:: text

  {path-prefix}/{YYYYMMDD}/teams/{teamID}/channels/{channelID}/users/{userID}/{fileID}/{filename}

This means a straight key-for-key copy from the S3 bucket to the Azure container is sufficient. If you use ``AmazonS3PathPrefix`` on the S3 side, set ``AzurePathPrefix`` to the same value on the Azure side (or rewrite the prefix during the copy).

Recommended pattern: minimal-downtime cutover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For deployments where users keep writing to S3 during the migration, run a long trickle sync first, then a short final sync during a maintenance window:

#. **Phase 1 -- trickle sync** with `rclone <https://rclone.org/azureblob/>`__ on a schedule. Mattermost stays on S3; users keep uploading. Each tick copies only the new or changed objects.
#. **Phase 2 -- maintenance window**. Put Mattermost into a read-only state or stop accepting new uploads, run one last sync (with `AzCopy <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-s3>`__ for the server-side copy speed-up), verify, then switch the driver and restart.
#. **Phase 3 -- soak**. Keep the S3 bucket readable for at least 30 days so you can roll back if needed.

For deployments that already have a planned downtime window (and no concurrent uploads to worry about), skip phase 1 and run AzCopy once.

Prerequisites
~~~~~~~~~~~~~

- A migration host. A small Linux VM in your destination Azure region is recommended -- ingress to Azure is free, so this minimises bandwidth costs on the AWS side.
- `AzCopy v10.25 or later <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10>`__ on the migration host.
- `rclone 1.66 or later <https://rclone.org/install/>`__ on the migration host.
- An AWS access key + secret with ``s3:ListBucket`` and ``s3:GetObject`` on the source bucket.
- The Azure Storage account name + shared key from `Step 3: Retrieve a shared key`_, or a container-scoped SAS with read/add/create/write/list/delete permissions.
- An estimate of the migration cost. AWS charges egress for objects leaving S3; as of 2026 the rate is approximately ``$0.09``/GB for the first 10 TB. A 1 TB bucket costs around ``$92`` in S3 egress. Refer to the `AWS S3 pricing page <https://aws.amazon.com/s3/pricing/>`__ for current numbers.

Phase 1: Trickle sync with rclone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure rclone remotes for the source bucket and the destination container:

.. code-block:: bash

  rclone config create s3src s3 \
      provider AWS \
      access_key_id "$AWS_ACCESS_KEY_ID" \
      secret_access_key "$AWS_SECRET_ACCESS_KEY" \
      region "$AWS_REGION"

  rclone config create azdst azureblob \
      account "<storage-account>" \
      key "<shared-key>"

Run a dry-run first to confirm what will be transferred:

.. code-block:: bash

  rclone sync s3src:<bucket> azdst:<container> --dry-run --fast-list

Then schedule the sync from cron (every 30 minutes is a reasonable starting point for buckets in the tens-to-hundreds of GB range):

.. code-block:: bash

  */30 * * * * /usr/local/bin/rclone sync s3src:<bucket> azdst:<container> \
      --transfers=32 --checkers=64 --fast-list --update \
      --log-file=/var/log/rclone-mm-sync.log --log-level=INFO

Notes:

- ``--update`` skips objects where the destination is newer or the same age.
- ``--fast-list`` issues one S3 ``ListObjectsV2`` request per 1000 objects instead of one per object, which is much cheaper for large buckets.
- Do **not** add ``--checksum`` here. S3 ETags are not MD5 sums for multi-part uploads, so a checksum compare across providers will trigger a full retransfer every tick. Save checksum verification for phase 3.

Let phase 1 run until the delta-per-tick is small (under a few minutes of work).

Phase 2: Final sync during the maintenance window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Announce the maintenance window and stop accepting new uploads. Common approaches: put the load balancer into drain mode, set Mattermost behind a maintenance page, or stop the server. Existing reads against S3 can continue.
#. Wait ``60`` seconds for in-flight uploads to settle.
#. Run one final AzCopy pass. AzCopy uses Azure's `Put Block From URL <https://learn.microsoft.com/en-us/rest/api/storageservices/put-block-from-url>`__ for S3 sources, so the data path does not flow through your migration host -- bytes move directly from S3 to Azure:

   .. code-block:: bash

     export AWS_ACCESS_KEY_ID=...
     export AWS_SECRET_ACCESS_KEY=...
     azcopy login --tenant-id "<tenant-id>"

     azcopy copy 'https://s3.amazonaws.com/<bucket>' \
                 'https://<account>.blob.core.windows.net/<container>' \
                 --recursive=true --from-to=S3Blob \
                 --overwrite=ifSourceNewer \
                 --s2s-handle-invalid-metadata=RenameIfInvalid \
                 --log-level=INFO

   AzCopy does not support ``sync`` against an S3 source, so use ``copy --overwrite=ifSourceNewer`` to pick up only the deltas from phase 1.

Phase 3: Verify, cut over, soak
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Object count parity.**

   .. code-block:: bash

     aws s3 ls --recursive --summarize s3://<bucket>/ | tail -2
     az storage blob list --container-name <container> --account-name <account> \
         --account-key <key> --query 'length(@)' --num-results '*'

   The counts should match. If they do not, find the delta:

   .. code-block:: bash

     rclone check --one-way s3src:<bucket> azdst:<container>

#. **Content spot-check.** Pick a sample of objects and compare ``sha256`` between the two sides:

   .. code-block:: bash

     aws s3 ls --recursive s3://<bucket>/ | awk '{print $4}' | shuf | head -100 | \
       while read k; do
         s=$(aws s3 cp "s3://<bucket>/$k" - 2>/dev/null | sha256sum | awk '{print $1}')
         a=$(az storage blob download --container-name <container> --name "$k" \
             --account-name <account> --account-key <key> --file - 2>/dev/null \
             | sha256sum | awk '{print $1}')
         [ "$s" = "$a" ] || echo "MISMATCH: $k"
       done

   Any output from this loop indicates a mismatch and should be investigated before the cutover.

#. **Switch the driver.** In **System Console > Environment > File Storage**, change **File storage system** from **Amazon S3** to **Azure Blob Storage** and complete the Azure fields as in `Step 4: Configure Mattermost`_. If your S3 configuration set ``AmazonS3PathPrefix``, set ``AzurePathPrefix`` to the same value.

#. **Test Connection**, then **Save**.

#. **Restart every Mattermost server.** The file backend is built at startup and not hot-reloaded.

#. **Smoke test.** Upload a new image (which writes three blobs: original, preview, thumbnail) to confirm writes work, then open an older attachment uploaded before the cutover to confirm reads against the migrated content work. Both reads validate the key layout matches.

#. **Soak.** Keep the S3 bucket readable for at least 30 days. If a regression appears, switch the **File storage system** back to **Amazon S3**, restart, and run ``rclone sync`` in reverse (``rclone sync azdst:<container> s3src:<bucket>``) to bring S3 up to date with anything uploaded after the cutover.

After the soak period, delete or archive the S3 bucket according to your retention policy.

Caveats
~~~~~~~

- **Only the latest version of each object is migrated.** If the source bucket has versioning enabled, S3 object versions are not copied -- the destination receives only the current version of each key. Mattermost never writes multiple versions of the same key, so this only matters if you need version history for compliance.
- **Sync mode versus copy mode.** ``rclone sync`` mirrors the source, including deletes; ``rclone copy`` is additive. Use ``sync`` so files deleted from S3 (for example, through Mattermost's own deletion paths) also disappear from Azure.
- **Different path prefixes.** If you change ``AzurePathPrefix`` to a different value than your S3 ``AmazonS3PathPrefix``, rewrite the prefix during the copy. ``rclone`` handles this by specifying full paths on both sides; ``azcopy`` requires per-prefix invocations.
- **Cross-region cost.** If your S3 bucket and your destination Azure region are in different geographies, you pay AWS inter-region egress in addition to inter-cloud egress. Co-locate the migration host with the destination region.
- **Tooling preview status.** Azure Storage Mover's cloud-to-cloud feature also supports S3 as a source and may simplify operations once it reaches general availability. As of this writing it is in public preview and not recommended for production cutovers.

(Optional) Configure the export backend
---------------------------------------

Compliance and data exports can be stored separately from regular file uploads. The **File Storage (Exports)** section directly below **File Storage** in the System Console mirrors the fields above and accepts the same Azure credentials. Customers typically point exports at a different container (or a different account) so the export retention policy can differ from regular uploads.

See :ref:`Enable dedicated export filestore target <administration-guide/configure/environment-configuration-settings:enable dedicated export filestore target>` for the full list of ``ExportAzure*`` keys.

Troubleshooting
---------------

.. list-table::
  :header-rows: 1
  :widths: 35 65

  * - Symptom
    - Likely cause
  * - ``AuthenticationFailed`` on **Test Connection**
    - When **Azure authentication** is **Shared key**: wrong account name or shared key. Confirm both in the **Access keys** blade of the Azure portal. When **Azure authentication** is **Default credential**: no identity source was available -- the host has no managed identity, the workload-identity federation is not set up, and no ``AZURE_TENANT_ID`` / ``AZURE_CLIENT_ID`` / ``AZURE_CLIENT_SECRET`` environment variables are set.
  * - ``AuthorizationPermissionMismatch`` on **Test Connection**
    - Only applies when **Azure authentication** is **Default credential**. The identity the SDK selected does not hold a data-plane role on the storage account. Grant **Storage Blob Data Contributor** to that identity per `Option B: Default credential (Microsoft Entra ID)`_, then wait 30-120 seconds for the role assignment to propagate.
  * - ``ContainerNotFound``
    - Container name is wrong or was created under a different storage account.
  * - ``connection refused`` or TLS errors
    - When **Azure cloud** is **Custom Endpoint**, the **Azure endpoint** URL points at a host that isn't reachable or uses the wrong scheme. When **Azure cloud** is **Azure Commercial** or **Azure Government**, **Enable secure Azure Blob Storage connections** is disabled in front of a TLS-only destination.
  * - **Test Connection** succeeds but uploads in channels fail
    - Check **System Console > Reporting > Server Logs** for the Azure error returned by the SDK. The most common cause is a forgotten server restart after **Save**.
  * - Files uploaded before the switch are no longer visible
    - The existing files are still on the previous backend. For S3 migrations, follow `Migrate existing files from Amazon S3`_ to copy the bucket into the Azure container at matching keys. For other backends, copy the contents into the Azure container with ``azcopy`` (or equivalent) and confirm the destination path matches the layout Mattermost uses.

Reference
---------

Each Azure setting is documented in detail in :ref:`Environment configuration settings <administration-guide/configure/environment-configuration-settings:file storage>`:

- :ref:`File storage system <administration-guide/configure/environment-configuration-settings:file storage system>` (``FileSettings.DriverName``)
- :ref:`Azure Storage account <administration-guide/configure/environment-configuration-settings:azure storage account>` (``FileSettings.AzureStorageAccount``)
- :ref:`Azure container <administration-guide/configure/environment-configuration-settings:azure container>` (``FileSettings.AzureContainer``)
- :ref:`Azure path prefix <administration-guide/configure/environment-configuration-settings:azure path prefix>` (``FileSettings.AzurePathPrefix``)
- :ref:`Azure authentication <administration-guide/configure/environment-configuration-settings:azure authentication>` (``FileSettings.AzureAuthMode``)
- :ref:`Azure Storage account key <administration-guide/configure/environment-configuration-settings:azure storage account key>` (``FileSettings.AzureAccessKey``)
- :ref:`Azure cloud <administration-guide/configure/environment-configuration-settings:azure cloud>` (``FileSettings.AzureCloud``)
- :ref:`Azure endpoint <administration-guide/configure/environment-configuration-settings:azure endpoint>` (``FileSettings.AzureEndpoint``)
- :ref:`Enable secure Azure Blob Storage connections <administration-guide/configure/environment-configuration-settings:enable secure azure blob storage connections>` (``FileSettings.AzureSSL``)
- :ref:`Azure request timeout <administration-guide/configure/environment-configuration-settings:azure request timeout>` (``FileSettings.AzureRequestTimeoutMilliseconds``)
