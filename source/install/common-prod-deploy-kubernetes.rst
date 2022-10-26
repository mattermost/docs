:orphan:
:nosearch:
.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

You can install and deploy a production-ready Mattermost system on a Kubernetes cluster using the Mattermost Kubernetes Operator in practically any environment with less IT overhead and more automation.

You'll need a `Kubernetes cluster <https://kubernetes.io/docs/setup/>`__ running version 1.16 or higher,  Kubernetes CLI `kubectl <https://kubernetes.io/docs/reference/kubectl/overview/>`__ installed on local machine, and a basic understanding of Kubernetes concepts (such as deployments, pods) and actions (such as applying manifests, viewing pod logs). Running Mattermost in Kubernetes requires resources based on your total number of users. See the `Mattermost Kubernetes Operator </install/mattermost-kubernetes-operator.html>`__ documentation to learn more about the minimum Kubernetes cluster resources Mattermost requires at different scales.

.. tip::
    
    If you’re unsure about which environment you want to use for your Kubernetes cluster, we suggest using a managed service such as as `Amazon EKS <https://aws.amazon.com/eks/>`__, `Azure Kubernetes Service <https://azure.microsoft.com/en-ca/services/kubernetes-service/>`__, `Google Kubernetes Engine <https://cloud.google.com/kubernetes-engine/>`__, or `DigitalOcean Kubernetes <https://www.digitalocean.com/products/kubernetes/>`__.

**Install the operators**

Operators are installed using ``kubectl``, and each operator is created in its own namespace. You can install and run multiple Mattermost installations in the same cluster using different namespaces.

1. Install NGINX ingress controller by following the instructions `here <https://kubernetes.github.io/ingress-nginx/deploy/>`__.

2. Install the Mattermost Operator:

   .. code-block:: sh

    $ kubectl create ns mattermost-operator
    $ kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml

.. tip::

    To install the operators using the Mattermost Operator Helm chart, follow the instructions `here <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-operator>`__.

**Deploy Mattermost**
  
1. (Mattermost Enterprise only) Create a Mattermost license secret by opening a text editor and creating a secret manifest containing the Mattermost license. Replace ``[LICENSE_FILE_CONTENTS]`` below with the contents of your Mattermost license file. Save the file as ``mattermost-license-secret.yaml``.

  .. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: mattermost-license
    type: Opaque
    stringData:
      license: [LICENSE_FILE_CONTENTS]

2. Create an installation manifest file locally in a text editor by copying and pasting contenst from the Mattermost installation manifest, and adjusting fields for your configuration and environment. 

  .. code-block:: yaml

    apiVersion: installation.mattermost.com/v1beta1
    kind: Mattermost
    metadata:
      name: mm-example-full                         # Chose the desired name
    spec:
      size: 5000users                               # Adjust to your requirements
      ingress:
        enabled: true
        host: example.mattermost-example.com        # Adjust to your domain
        annotations:
          kubernetes.io/ingress.class: nginx
      version: 6.0.1
      licenseSecret: ""                             # If you have created secret in step 1, put its name here
    
  Save the file as ``mattermost-installation.yaml``. While recommended file names are provided, your naming conventions may differ. 

  Some of the most commonly-used fields include:

  .. csv-table::
    :header: "Field", "Description", "Must Edit"

    "metadata.name", "The name of your Mattermost as it will be shown in Kubernetes. The shorter the better.", "Yes"
    "spec.size", "The size of your installation. This can be '100users', '1000users, '5000users', '10000users', or '25000users'.", "Yes"
    "spec.ingress.host", "The DNS for your Mattermost installation.", "Yes"
    "spec.version", "The Mattermost version.", "No"
    "spec.licenseSecret", "The name of the Kubernetes secret containing your license (e.g. mattermost-license). Required for Enterprise deployments.", "No"
    "spec.mattermostEnv", "List of custom environment variables for the Mattermost instance.", "No"
    
    Additional fields are documented `in the example <https://github.com/mattermost/mattermost-operator/blob/master/docs/examples/mattermost_full.yaml>`__.
    If you have previous experience with Kubernetes Custom Resources, you can also check the `Custom Resource Definition <https://github.com/mattermost/mattermost-operator/blob/master/config/crd/bases/installation.mattermost.com_mattermosts.yaml>`__.

3. Create external database secret. (Skip if using MySQL and MinIO operators).

  The database secret needs to be created in the namespace that will hold the Mattermost installation. The secret should contain the following data:

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

    - For PostgreSQL databases, the connection is checked with `pg_isready <https://www.postgresql.org/docs/9.3/app-pg-isready.html>`__ so the ``DB_CONNECTION_CHECK_URL`` is the same as connection string.
    - For MySQL databases, the check is performed via HTTP call; therefore ``DB_CONNECTION_CHECK_URL`` should be an HTTP URL.

4. Create external filestore secret (Skip if using MySQL and MinIO operators).

  The filestore secret needs to be created in the namespace that will hold the Mattermost installation. The secret should contain the following data:

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

5. Adjust installation manifest (Skip if using MySQL and MinIO operators).

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
      version: 6.0.1
      licenseSecret: ""
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

  a. Create the Mattermost namespace:

    .. code-block:: sh

        $ kubectl create ns mattermost

  b. (Mattermost Enterprise only) apply the license file by specifying the path to the file you created in step 1:

    .. code-block:: sh

        $ kubectl apply -n mattermost -f [PATH_TO_LICENCE_SECRET_MANIFEST]

  c. Apply the installation file by specifying the path to the file you created in step 2:

    .. code-block:: sh

        $ kubectl apply -n mattermost -f [PATH_TO_MATTERMOST_MANIFEST]

  The deployment process can be monitored in the Kubernetes user interface or in command line by running:

  .. code-block:: sh

    $ kubectl -n mattermost get mm -w

  The installation should be deployed successfully, when the Custom Resource reaches the ``stable`` state.

7. Configure DNS and use Mattermost.

  When the deployment is complete, obtain the hostname or IP address of your Mattermost deployment using the following command:

  .. code-block:: sh

    $ kubectl -n mattermost get ingress

  Copy the resulting hostname or IP address from the ``ADDRESS`` column, open your browser, and connect to Mattermost.

  Use your domain registration service to create a canonical name or IP address record for the ``ingress.host`` in your manifest, pointing to the address you just copied. For example, on AWS you would do this within a hosted zone in Route53.

  Navigate to the ``ingress.host`` URL in your browser and use Mattermost.

  If you just want to try it out on your local machine without configuring the domain, run:

  .. code-block:: sh

    $ kubectl -n mattermost port-forward svc/[YOUR_MATTERMOST_NAME] 8065:8065

  Then navigate to http://localhost:8065.








 



