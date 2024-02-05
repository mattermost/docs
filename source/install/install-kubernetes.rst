Install Mattermost on Kubernetes
================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

You can install and deploy a production-ready Mattermost system on a Kubernetes cluster using the Mattermost Kubernetes Operator in practically any environment with less IT overhead and more automation.

You'll need a `Kubernetes cluster <https://kubernetes.io/docs/setup/>`__ running `a version that is currently supported with patch releases <https://kubernetes.io/releases/>`__,  Kubernetes CLI `kubectl <https://kubernetes.io/docs/reference/kubectl/overview/>`__ installed on local machine, and a basic understanding of Kubernetes concepts (such as deployments, pods) and actions (such as applying manifests, viewing pod logs). Running Mattermost in Kubernetes requires resources based on your total number of users. See the `Mattermost Kubernetes Operator </install/mattermost-kubernetes-operator.html>`__ documentation to learn more about the minimum Kubernetes cluster resources Mattermost requires at different scales.

.. tip::
    
    - If you’re unsure about which environment you want to use for your Kubernetes cluster, we suggest using a managed service such as as `Amazon EKS <https://aws.amazon.com/eks/>`__, `Azure Kubernetes Service <https://azure.microsoft.com/en-ca/services/kubernetes-service/>`__, `Google Kubernetes Engine <https://cloud.google.com/kubernetes-engine/>`__, or `DigitalOcean Kubernetes <https://www.digitalocean.com/products/kubernetes/>`__.
    - Looking for a quick way to evaluate Mattermost or to try out the latest Mattermost deployment? See this article for details on creating your own Mattermost instance on Kubernetes using Minicube: https://medium.com/@Erez.Tamam/create-your-own-mattermost-instance-on-kubernetes-in-10-minutes-d13f576ed794.

Install the operators
---------------------

Operators are installed using ``kubectl``, and each operator is created in its own namespace. You can install and run multiple Mattermost installations in the same cluster using different namespaces.

1. Install NGINX ingress controller by following the instructions `here <https://kubernetes.github.io/ingress-nginx/deploy/>`__.

2. Install the Mattermost Operator:

  .. code-block:: sh
    :class: mm-code-block 

    kubectl create ns mattermost-operator

    kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml

.. tip::

    To install the operators using the Mattermost Operator Helm chart, follow the instructions `here <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-operator>`__.

Deploy Mattermost
-----------------
  
1. (Mattermost Enterprise only) Create a Mattermost license secret by opening a text editor and creating a secret manifest containing the Mattermost license. Replace ``[LICENSE_FILE_CONTENTS]`` below with the contents of your Mattermost license file. Save the file as ``mattermost-license-secret.yaml``.

  .. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-mattermost-license
    type: Opaque
    stringData:
      license: <LICENSE_FILE_CONTENTS>

2. Create an installation manifest file locally in a text editor by copying and pasting contenst from the Mattermost installation manifest, and adjusting fields for your configuration and environment. 

  .. code-block:: yaml

      apiVersion: installation.mattermost.com/v1beta1
      kind: Mattermost
      metadata:
        name: <INSTALLATION_NAME_HERE>                # Chose the desired installation name. Example = mm-example-full
      spec:
        size: <SIZE_VALUE_HERE>                       # Adjust to your requirements. Example = 5000users
        ingress:
          enabled: true
          host: <FULL_DOMAIN_NAME_HERE>               # Adjust to your domain. Example = example.mattermost-example.com
          annotations:
            kubernetes.io/ingress.class: nginx
        version: <VERSION_HERE>                       # Select a recent supported version of Mattermost. Example = 9.3.0
        licenseSecret: ""                             # If you created a license secret in step 1, put the secret name here
    
  Save the file as ``mattermost-installation.yaml``. While recommended file names are provided, your naming conventions may differ. 

  Some of the most commonly-used fields include:

  .. csv-table::
    :header: "Field", "Description"

    "metadata.name", "The name of your Mattermost as it will be shown in Kubernetes. The shorter the better."
    "spec.size", "The size of your installation. This can be '100users', '1000users, '5000users', '10000users', or '25000users'."
    "spec.ingress.host", "The DNS for your Mattermost installation."
    "spec.version", "The Mattermost version. Refer to `the version archive page <https://docs.mattermost.com/upgrade/version-archive.html>`__ when selecting a mattermost version."
    "spec.licenseSecret", "The name of the Kubernetes secret containing your license (e.g. mattermost-license). Required for Enterprise deployments."
    "spec.mattermostEnv", "List of custom environment variables for the Mattermost instance. Only required when tweaking Mattermost configuration is required."
    
  Additional fields are documented `in the example <https://github.com/mattermost/mattermost-operator/blob/master/docs/examples/mattermost_full.yaml>`__. If you have previous experience with Kubernetes Custom Resources, you can also check the `Custom Resource Definition <https://github.com/mattermost/mattermost-operator/blob/master/config/crd/bases/installation.mattermost.com_mattermosts.yaml>`__.

3. Create external database secret. The database secret needs to be created in the namespace that will hold the Mattermost installation. The secret should contain the following data:

  .. csv-table::
    :header: "Key", "Description", "Required"

    "DB_CONNECTION_STRING", "Connection string to the database.", "Yes"
    "MM_SQLSETTINGS_DATASOURCEREPLICAS", "Connection string to read replicas of the database.", "No"
    "DB_CONNECTION_CHECK_URL", "The URL used for checking that the database is accessible.", "No"

  Example secret for AWS Aurora compatible with PostgreSQL:

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

  .. note:: 

    For PostgreSQL databases, the connection is checked with `pg_isready <https://www.postgresql.org/docs/9.3/app-pg-isready.html>`__ so the ``DB_CONNECTION_CHECK_URL`` is the same as connection string.

4. Create external filestore secret. The filestore secret needs to be created in the namespace that will hold the Mattermost installation. The secret should contain the following data:

  .. csv-table::
    :header: "Key", "Description", "Required"

    "accesskey", "Filestore access key.", "Yes"
    "secretkey", "Filestore secret key.", "Yes"

  Example secret for AWS S3:

  .. code-block:: yaml

    apiVersion: v1
    data:
      accesskey: QUNDRVNTX0tFWQo=
      secretkey: U1VQRVJfU0VDUkVUX0tFWQo=
    kind: Secret
    metadata:
      name: my-s3-iam-access-key
    type: Opaque

5. Adjust installation manifest.

  To instruct Mattermost Operator to use the external database, modify Mattermost manifest by adding the following fields:

  .. code-block:: yaml

    spec:
    ...
      database:
        external:
          secret: my-postgres-connection

  To instruct Mattermost Operator to use the external filestore, modify Mattermost manifest by adding the following fields:

  .. code-block:: yaml

    spec:
    ...
      fileStore:
        external:
          url: s3.amazonaws.com
          bucket: my-s3-bucket
          secret: my-s3-iam-access-key

  Additionally when using Amazon S3, set the ``MM_FILESETTINGS_AMAZONS3SSE`` and ``MM_FILESETTINGS_AMAZONS3SSL`` environment variables to ``true``:

  .. code-block:: yaml

    spec:
    ...
      mattermostEnv:
        ...
        - name: MM_FILESETTINGS_AMAZONS3SSE
          value: "true"
        - name: MM_FILESETTINGS_AMAZONS3SSL
          value: "true"

  Example Mattermost manifest configured with both external databases and filestore:

  .. code-block:: yaml

    apiVersion: installation.mattermost.com/v1beta1
    kind: Mattermost
    metadata:
      name: mm-example-external-db
    spec:
      size: 5000users
      ingress:
        enabled: true
        host: example.mattermost-example.com
        annotations:
          kubernetes.io/ingress.class: nginx
      version: 9.3.0
      licenseSecret: my-mattermost-license
      database:
        external:
          secret: my-postgres-connection
      fileStore:
        external:
          url: s3.amazonaws.com
          bucket: my-s3-bucket
          secret: my-s3-iam-access-key
      mattermostEnv:
      - name: MM_FILESETTINGS_AMAZONS3SSE
        value: "true"
      - name: MM_FILESETTINGS_AMAZONS3SSL
        value: "true"

6. Apply the installation manifest file. Manifests are applied with ``kubectl``. Before running the commands make sure you are connected to your Kubernetes cluster.

  a. Create a namespace for this new Mattermost installation:

    .. code-block:: sh
      :class: mm-code-block

      kubectl create ns mattermost

  b. (Mattermost Enterprise only) apply the license file by specifying the path to the file you created in step 1:

    .. code-block:: sh
      :class: mm-code-block

      kubectl apply -n mattermost -f [PATH_TO_LICENCE_SECRET_MANIFEST]

  c. Apply the installation file by specifying the path to the file you created in step 2:

    .. code-block:: sh
      :class: mm-code-block

      kubectl apply -n mattermost -f [PATH_TO_MATTERMOST_MANIFEST]

  The deployment process can be monitored in the Kubernetes user interface or in command line by running:

    .. code-block:: sh
      :class: mm-code-block

      kubectl -n mattermost get mm -w

  The installation should be deployed successfully, when the Custom Resource reaches the ``stable`` state.

7. Configure DNS and use Mattermost.

  a. When the deployment is complete, obtain the hostname or IP address of your Mattermost deployment using the following command:

    .. code-block:: sh
      :class: mm-code-block

      kubectl -n mattermost get ingress

  b. Copy the resulting hostname or IP address from the ``ADDRESS`` column, open your browser, and connect to Mattermost.

  c. Use your domain registration service to create a canonical name or IP address record for the ``ingress.host`` in your manifest, pointing to the address you just copied. For example, on AWS you would do this within a hosted zone in Route53.

  d. Navigate to the ``ingress.host`` URL in your browser and use Mattermost.

.. note::
  
  If you just want to try it out on your local machine without configuring the domain, run the following command, and then navigate to http://localhost:8065.

    .. code-block:: sh
      :class: mm-code-block

      kubectl -n mattermost port-forward svc/[YOUR_MATTERMOST_NAME] 8065:8065

Frequently asked questions
--------------------------

.. include:: faq_kubernetes.rst
  :start-after: :nosearch: