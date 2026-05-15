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

Step 3: Retrieve a shared key
-----------------------------

Mattermost authenticates to Azure with a Storage Account shared key (account name + key).

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

Step 4: Configure Mattermost
----------------------------

Sign in as a System Admin and open **System Console > Environment > File Storage**.

1. **File storage system**: select **Azure Blob Storage**. The Azure-specific fields appear and the S3/local fields are hidden.
2. **Azure Storage account**: the storage account name from step 1 (for example, ``acmemattermost``).
3. **Azure container**: the container name from step 2 (for example, ``mattermost``).
4. **Azure path prefix**: optional. Set this if you want Mattermost to write under a sub-path inside the container, for example ``prod/``. Leave empty to use the container root.
5. **Azure Storage account key**: paste the shared key from step 3.
6. **Azure endpoint**: leave empty to use the default ``{account}.blob.core.windows.net`` host, where ``{account}`` is the configured **Azure Storage account**. Set this only if you need a non-default host, for example ``azurite:10000`` for an Azurite emulator or a reverse-proxy ``host[:port]`` in front of Blob Storage.
7. **Enable secure Azure Blob Storage connections**: keep this enabled (the default). Only disable it when pointing at a local emulator without TLS.
8. **Azure request timeout (milliseconds)**: default is ``30000`` (30 seconds). Increase only if your network needs more time for large objects.

Select **Test Connection**. Mattermost issues a no-op write/read/delete against the configured container using the credentials submitted in the form. A green ``Connection was successful`` message confirms the credentials, container name, and endpoint all work. A red error message includes the underlying reason -- common ones are listed in `Troubleshooting`_.

Once the test succeeds, select **Save**.

.. note::

  Sovereign clouds (Azure Government, Azure China) use account-style hosts that Mattermost selects automatically when the **Azure endpoint** field is left empty. They are not configured through the endpoint override.

.. warning::

  **Restart required.** The Mattermost server caches the file storage backend at startup and does not re-create it when the file storage configuration changes. After saving, restart every Mattermost server in the deployment (``systemctl restart mattermost``, recycle the container, or roll the deployment in your cluster) for the new driver to take effect. **Test Connection** works before the restart because it builds a temporary backend from the submitted form values.

.. note::

  Switching the file driver does **not** migrate existing files. If you are moving an existing deployment from local disk or S3, copy the contents into the Azure container first (for example with `azcopy <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10>`__) before changing the driver. Files uploaded before the switch will not be reachable once the driver changes.

Step 5: Verify
--------------

1. After the restart, reload the System Console or any channel.
2. Upload an attachment in any channel. A small image is a good test, because Mattermost stores three blobs for an image (original, preview, thumbnail), which exercises the upload path more thoroughly than a plain file.
3. The post should render the attachment and preview as usual.
4. In the Azure portal, open the container and confirm new blobs appeared under the path ``<YYYYMMDD>/teams/<team>/channels/<channel>/users/<user>/<file_id>/`` (the same layout the local-disk and S3 backends use). For an image you will see ``<name>.<ext>``, ``<name>_preview.<ext>``, and ``<name>_thumb.<ext>``.

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
    - Wrong account name or shared key. Confirm both in the **Access keys** blade of the Azure portal.
  * - ``ContainerNotFound``
    - Container name is wrong or was created under a different storage account.
  * - ``connection refused`` or TLS errors
    - **Azure endpoint** is set to a host that isn't reachable, or **Enable secure Azure Blob Storage connections** is disabled when the destination requires TLS.
  * - **Test Connection** succeeds but uploads in channels fail
    - Check **System Console > Reporting > Server Logs** for the Azure error returned by the SDK. The most common cause is a forgotten server restart after **Save**.
  * - Files uploaded before the switch are no longer visible
    - The existing files are still on the previous backend. Copy them into the Azure container with ``azcopy`` (or equivalent) and confirm the destination path matches the layout Mattermost uses.

Reference
---------

Each Azure setting is documented in detail in :ref:`Environment configuration settings <administration-guide/configure/environment-configuration-settings:file storage>`:

- :ref:`File storage system <administration-guide/configure/environment-configuration-settings:file storage system>` (``FileSettings.DriverName``)
- :ref:`Azure Storage account <administration-guide/configure/environment-configuration-settings:azure storage account>` (``FileSettings.AzureStorageAccount``)
- :ref:`Azure container <administration-guide/configure/environment-configuration-settings:azure container>` (``FileSettings.AzureContainer``)
- :ref:`Azure path prefix <administration-guide/configure/environment-configuration-settings:azure path prefix>` (``FileSettings.AzurePathPrefix``)
- :ref:`Azure Storage account key <administration-guide/configure/environment-configuration-settings:azure storage account key>` (``FileSettings.AzureAccessKey``)
- :ref:`Azure endpoint <administration-guide/configure/environment-configuration-settings:azure endpoint>` (``FileSettings.AzureEndpoint``)
- :ref:`Enable secure Azure Blob Storage connections <administration-guide/configure/environment-configuration-settings:enable secure azure blob storage connections>` (``FileSettings.AzureSSL``)
- :ref:`Azure request timeout <administration-guide/configure/environment-configuration-settings:azure request timeout>` (``FileSettings.AzureRequestTimeoutMilliseconds``)
