.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

You can use the Mattermost Kubernetes Operator to deploy Mattermost on Kubernetes using S3-compatible storage and a managed database service. While the operator supports a range of configurations, we strongly recommend using a cloud-native approach for production environments.

**Prerequisites**

Before you begin, ensure you have the following:

* A functioning Kubernetes cluster (see the `Kubernetes setup guide <https://kubernetes.io/docs/setup/>`__). Your cluster should be running a `supported Kubernetes version <https://kubernetes.io/releases/>`__.
* The `kubectl` command-line tool installed on your local machine (see the `kubectl installation guide <https://kubernetes.io/docs/reference/kubectl/>`__).
* A fundamental understanding of Kubernetes concepts, such as deployments, pods, and applying manifests.
* Sufficient Kubernetes resources allocated based on your expected user load. Consult the `Mattermost Kubernetes Operator <#install-the-mattermost-operator>`__ documentation for resource requirements at different scales.

**Installation steps**

The installation process involves setting up necessary operators and then deploying Mattermost itself.

**Step 1: Install the NGINX Ingress Controller**

Follow the instructions in the `Kubernetes deployment documentation <https://kubernetes.github.io/ingress-nginx/deploy/>`_ to install the NGINX ingress controller on your Kubernetes cluster. Mattermost recommends installing the Nginx Operator via helm, regardless of platform you are installing to. 

**Step 2: Install the Mattermost Operator**

The Mattermost Kubernetes Operator can be installed using Helm.

1. Install Helm (version 3.13.0 or later). See the `Helm quickstart documentation <https://helm.sh/docs/using_helm/>`_ for installation instructions.

2. Add the Mattermost Helm repository:

  .. code-block:: sh

    helm repo add mattermost https://helm.mattermost.com

3. Create a file named ``config.yaml`` and populate it with the contents of the `Mattermost operator values file <https://github.com/mattermost/mattermost-helm/blob/master/charts/mattermost-operator/values.yaml>`_. This file allows for customization of the operator.

4. Create a namespace for the Mattermost Operator:

  .. code-block:: sh

    kubectl create ns mattermost-operator

5. Install the Mattermost Operator. If you don't specify a version, the latest version of the Mattermost Operator will be installed.

  .. code-block:: sh

    helm install <your-release-name> mattermost/mattermost-operator -n <namespace_name>

  For example:

  .. code-block:: sh

      helm install mattermost-operator mattermost/mattermost-operator -n mattermost-operator

  To use your custom ``config.yaml`` file:

  .. code-block:: sh

    helm install mattermost-operator mattermost/mattermost-operator -n mattermost-operator -f config.yaml

**Step 3: Deploy Mattermost**

.. note::

  - A Mattermost Enterprise license is required for multi-server deployments. 
  - For single-server deployments without an Enterprise license, add ``Replicas: 1`` to the ``spec`` section in step 2 below. See the :doc:`high availability documentation </scale/high-availability-cluster-based-deployment>` for more on highly-available deployments.

1. **(Mattermost Enterprise only)** Create a Mattermost license secret. Create a file named ``mattermost-license-secret.yaml`` with the following content, replacing ``[LICENSE_FILE_CONTENTS]`` with your actual license:

  .. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-mattermost-license
    type: Opaque
    stringData:
      license: <LICENSE_FILE_CONTENTS>

2. Create a Mattermost installation manifest file named ``mattermost-installation.yaml``. File names in this guide are suggestions; you can use different names. Use the following template, adjusting the values as needed:

  .. code-block:: yaml

    apiVersion: installation.mattermost.com/v1beta1
    kind: Mattermost
    metadata:
      name: <INSTALLATION_NAME_HERE>        # Example: mm-example-full
    spec:
      size: <SIZE_VALUE_HERE>               # Example: 5000users
      ingress:
        enabled: true
        host: <FULL_DOMAIN_NAME_HERE>       # Example: example.mattermost-example.com
        annotations:
          kubernetes.io/ingress.class: nginx
    version: <VERSION_HERE>               # Example: 9.3.0
    licenseSecret: ""                     # If you created a license secret, put the name here

  Key fields in the manifest include:

  * ``metadata.name``: The name of your Mattermost deployment in Kubernetes.
  * ``spec.size``: The size of your installation (e.g., "100users", "1000users", etc.).
  * ``spec.ingress.host``: The DNS name for your Mattermost installation.
  * ``spec.version``: The Mattermost version. See the :doc:`server version archive </about/version-archive>` for available versions.
  * ``spec.licenseSecret``: The name of the Kubernetes secret containing your license (required for Enterprise).

  For a full list of configurable fields, see the `example manifest <https://github.com/mattermost/mattermost-operator/blob/master/docs/examples/mattermost_full.yaml>`_ and the `Custom Resource Definition <https://github.com/mattermost/mattermost-operator/blob/master/config/crd/bases/installation.mattermost.com_mattermosts.yaml>`_.

3. Create a file named ``mattermost-database-secret.yaml`` for database credentials. This secret must be in the same namespace as the Mattermost installation.

  .. code-block:: yaml

      apiVersion: v1
      data:
        DB_CONNECTION_CHECK_URL: <DB_CONNECTION_CHECK_URL>
        DB_CONNECTION_STRING: <DB_CONNECTION_STRING>
        MM_SQLSETTINGS_DATASOURCEREPLICAS: <MM_SQLSETTINGS_DATASOURCEREPLICAS>
      kind: Secret
      metadata:
        name: my-postgres-connection
      type: Opaque

  Example for AWS Aurora with PostgreSQL:

  .. code-block:: yaml

    apiVersion: v1
    data:
      DB_CONNECTION_CHECK_URL: cG9zdGdyZXM6Ly91c2VyOnN1cGVyX3NlY3JldF9wYXNzd29yZEBteS1kYXRhYmFzZS5jbHVzdGVyLWFiY2QudXMtZWFzdC0xLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvbWF0dGVybW9zdD9jb25uZWN0X3RpbWVvdXQ9MTAK
      DB_CONNECTION_STRING: cG9zdGdyZXM6Ly91c2VyOnN1cGVyX3NlY3JldF9wYXNzd29yZEBteS1kYXRhYmFzZS5jbHVzdGVyLWFiY2QudXMtZWFzdC0xLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvbWF0dGVybW9zdD9jb25uZWN0X3RpbWVvdXQ9MTAK
      MM_SQLSETTINGS_DATASOURCEREPLICAS: cG9zdGdyZXM6Ly91c2VyOnN1cGVyX3NlY3JldF9wYXNzd29yZEBteS1kYXRhYmFzZS5jbHVzdGVyLXJvLWFiY2QudXMtZWFzdC0xLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvbWF0dGVybW9zdD9jb25uZWN0X3RpbWVvdXQ9MTAK
    kind: Secret
    metadata:
      name: my-postgres-connection
    type: Opaque

**Step 4: Create the Filestore Secret**

Create a file named ``mattermost-filestore-secret.yaml`` to store the credentials for your object storage service (e.g., AWS S3, MinIO). This secret must be created in the same namespace where you intend to install Mattermost. The file should contain the following YAML structure:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: <secret-name>  # Choose a descriptive name (e.g., my-s3-credentials)
    type: Opaque
    data:
      accesskey: <base64-encoded-access-key>
      secretkey: <base64-encoded-secret-key>

.. csv-table::
  :header: "Key", "Description", "Required"

  "accesskey", "Base64-encoded access key for your storage service.", "Yes"
  "secretkey", "Base64-encoded secret key for your storage service.", "Yes"
  "metadata.name", "The name of the Kubernetes secret.", "Yes"

.. important::

  The ``accesskey`` and ``secretkey`` values must be **base64-encoded**. Do not enter the raw keys directly. Use a command-line tool or online encoder to generate the base64 strings.

  **Example (AWS S3):**

  .. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-s3-credentials
    type: Opaque
    data:
      accesskey: QUNDRVNTX0tFWQo=  # Example: Replace with your actual encoded key
      secretkey: U1VQRVJfU0VDUkVUX0tFWQo=  # Example: Replace with your actual encoded key

**Step 5: Configure the Mattermost Installation Manifest**

1. Modify the ``mattermost-installation.yaml`` file (created in step 2) to connect Mattermost to your external database and object storage. Refer to the supported fields for guidance on where to add these configurations within the YAML structure.

2. Connect to the database:

  a. Add the following to the ``spec`` section of your manifest:

    .. code-block:: yaml

      spec:
        database:
          external:
            secret: <database-secret-name>  # The name of the database secret (e.g., my-postgres-connection)

3. Connect to Object Storage:

  a. Add the following to the ``spec`` section of your manifest:

    .. code-block:: yaml

      spec:
        fileStore:
          external:
            url: <storage-service-url>  # The URL of your storage service (e.g., s3.amazonaws.com)
            bucket: <bucket-name>      # The name of your storage bucket
            secret: <filestore-secret-name> # The name of the filestore secret (e.g., my-s3-credentials)

4. If you are using Amazon S3, it's recommended to enable server-side encryption (SSE) and SSL. Add the following environment variables to the ``mattermostEnv`` section: 

TBD


**Review Mattermost Resource Status**

After a Mattermost installation has been created with the Operator, you can review its status with the following:

.. code-block:: sh

  kubectl -n [namespace] get mattermost

The ``kubectl describe`` command can be used to obtain more information about the Mattermost server pods:

.. code-block:: sh

  kubectl -n [namespace] describe pod

**Follow logs**

The following command can be used to follow logs on any kubernetes pod:

.. code-block:: sh

  kubectl -n [namespace] logs -f [pod name]

If the ``-n [namespace]`` is omitted, then the default namespace of the current context is used. We recommend specifying the namespace based on your deployment.

This command can be used to review the Mattermost Operator or Mattermost server logs as needed.

.. note::

  - If you're new to Kubernetes or prefer a managed solution, consider using a service like `Amazon EKS <https://aws.amazon.com/eks/>`_, `Azure Kubernetes Service <https://azure.microsoft.com/en-ca/products/kubernetes-service/>`_, `Google Kubernetes Engine <https://cloud.google.com/kubernetes-engine/>`_, or `DigitalOcean Kubernetes <https://www.digitalocean.com/products/kubernetes/>`_.- While this guidance focuses on using external, managed services for your database and file storage, the Mattermost Operator *does* offer the flexibility to use other solutions. For example, you could choose to deploy a PostgreSQL database within your Kubernetes cluster using the CloudNative PG operator (or externally however you wish), or use a self-hosted MinIO instance for object storage.
  - While using managed cloud services is generally simpler to maintain and our recommended approach for production deployments, using self-managed services like MinIO for storage and CloudNative PG for PostgreSQL are also valid options if you have the expertise to manage them. 
  - If you choose to use self-managed components, you'll need to adapt the instructions accordingly, pointing to your internal services instead.
  - To customize your production deployment, refer to the :doc:`configuration settings documentation </configure/configuration-settings>`.
  - If you encounter issues during deployment, consult the :doc:`deployment troubleshooting guide </guides/deployment-troubleshooting>`.