.. _install-kubernetes-mattermost:

Deploying a Mattermost Installation
-----------------------------------

.. warning::
  If you used the Mattermost Operator in version prior to v1.12.x or are still using ``ClusterInstallation`` Custom Resource 
  check out `this guide <https://github.com/mattermost/mattermost-operator/blob/master/docs/migration.md>`__ to see how to migrate to new ``Mattermost`` resource.
  
  The ``ClusterInstallation`` is deprecated and will be removed in version v2.0.

This guide describes deploying a complete Mattermost installation in Kubernetes.

Manifest files contain the configurations needed for the Operator to properly set up the Mattermost installation.
Create the manifest files locally in a text editor, copy and paste the contents, and save the file. Recommended file names are provided, but your naming conventions may differ.
Manifests are applied with ``kubectl``. Before running the commands make sure you are connected to your Kubernetes cluster.

**1. (Enterprise only) Create a Mattermost license secret**

Open a text editor and create a secret manifest containing the Mattermost license.

Make sure to replace ``[LICENSE_FILE_CONTENTS]`` with the contents of your Mattermost license file.

.. code-block:: yaml

  apiVersion: v1
  kind: Secret
  metadata:
    name: mattermost-license
  type: Opaque
  stringData:
    license: [LICENSE_FILE_CONTENTS]

Save the file as ``mattermost-license-secret.yaml``.

**2. Create an installation manifest file**

The Mattermost installation manifest contains fields which must be adjusted for your configuration and environment requirements.

Some of the most commonly-used fields are:

.. csv-table::
    :header: "Field", "Description", "Must Edit"

    "metadata.name", "The name of your Mattermost as it will be shown in Kubernetes. The shorter the better.", "Yes"
    "spec.size", "The size of your installation. This can be '100users', '1000users, '5000users', '10000users', or '25000users'.", "Yes"
    "spec.ingressName", "The DNS for your Mattermost installation.", "Yes"
    "spec.version", "The Mattermost version.", "No"
    "spec.licenseSecret", "The name of the Kubernetes secret containing your license (e.g. mattermost-license). Required for Enterprise deployments.", "No"
    "spec.mattermostEnv", "List of custom environment variables for the Mattermost instance.", "No"
    
More fields are documented `in the example <https://github.com/mattermost/mattermost-operator/blob/master/docs/examples/mattermost_full.yaml>`__.
If you have previous experience with Kubernetes Custom Resources you can also check the `Custom Resource Definition <https://github.com/mattermost/mattermost-operator/blob/master/config/crd/bases/installation.mattermost.com_mattermosts.yaml>`__.

Open a text editor and create a Mattermost installation manifest:

.. code-block:: yaml

  apiVersion: installation.mattermost.com/v1beta1
  kind: Mattermost
  metadata:
    name: mm-example-full                         # Chose the desired name
  spec:
    size: 5000users                               # Adjust to your requirements
    ingressName: example.mattermost-example.com   # Adjust to your domain
    ingressAnnotations:
      kubernetes.io/ingress.class: nginx
    version: 5.31.0
    licenseSecret: ""                             # If you have created secret in step 1, put its name here
    
Save the file as ``mattermost-installation.yaml``.

.. note::
    Steps 3 to 5 cover configuring Mattermost with external database and filestore which is recommended installation configuration. 

    When using MySQL and MinIO operators these steps can be skipped. 
    It requires both Operators to be installed on the cluster and it is **not recomended for production usage**.

**3. Create external database secret**

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
  For PostgreSQL the connection is checked with `pg_isready <https://www.postgresql.org/docs/9.3/app-pg-isready.html>`__ so the ``DB_CONNECTION_CHECK_URL`` is the same as connection string.
  For MySQL the check is performed via HTTP call therefore ``DB_CONNECTION_CHECK_URL`` should be an HTTP URL.

**4. Create external filestore secret**

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

**5. Adjust installation manifest**

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
    ingressName: example.mattermost-example.com
    ingressAnnotations:
      kubernetes.io/ingress.class: nginx
    version: 5.31.0
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

**6. Apply the installation manifest file**

First, create the Mattermost namespace:

.. code-block:: sh

  $ kubectl create ns mattermost

If you're deploying Mattermost Enterprise Edition, apply the license file by specifying the path to the file you created in step 1:

.. code-block:: sh

  $ kubectl apply -n mattermost -f [PATH_TO_LICENCE_SECRET_MANIFEST]

Finally, apply the installation file, specifying path to file you created in step 2:

.. code-block:: sh

  $ kubectl apply -n mattermost -f [PATH_TO_MATTERMOST_MANIFEST]

The deployment process can be monitored in the Kubernetes user interface or in command line by running:

.. code-block:: sh

  $ kubectl -n mattermost get mm -w

The installation should be deployed successfuly, when the Custom Resource reaches the ``stable`` state.

**7. Configure DNS and use Mattermost**

When the deployment is complete, obtain the hostname or IP address of your Mattermost deployment using the following command:

.. code-block:: sh

  $ kubectl -n mattermost get ingress

Copy the resulting hostname or IP address from the ``ADDRESS`` column, open your browser, and connect to Mattermost.

Use your domain registration service to create a canonical name or IP address record for the ``ingressName`` in your manifest, pointing to the address you just copied. For example, on AWS you would do this within a hosted zone in Route53.

Navigate to the ``ingressName`` URL in your browser and use Mattermost.

If you just want to try it out on your local machine without configuring the domain, run:

.. code-block:: sh

  $ kubectl -n mattermost port-forward svc/[YOUR_MATTERMOST_NAME] 8065:8065

And navigate to http://localhost:8065.

Restoring an Existing Mattermost MySQL Database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost Operator can be used in a backup and restore scenario to apply an existing Mattermost MySQL database to a new Mattermost installation, in its own namespace. This can also be helpful in the event that you need to revert your Mattermost instance's database to the most recent backup point, on your existing installation. In both cases, you will need a backup of your database.

The steps you follow to create and upload your backup depends on the provider you're using and your use case. It's recommended that you consult the relevant documentation or, if your deployment is managed in a different way, consult your Administrator.

It is important to note that this process requires the creation of a new Mattermost installation - editing the existing ``.yaml`` files is not recommended and can result in data loss.

The process described below needs to be completed prior to proceeding with the Mattermost deployment.

1. Create a backup of your database (e.g. using *mysqldump*).
2. Deploy a new server (e.g. an AWS instance).
3. Install a backup program and back up the database on the new server/instance.
4. Upload the backed up database to your cloud storage provider (e.g. Amazon S3).
5. Create a ``secret.yaml`` file:

Open a text editor and create a text file containing your credentials which will be used to access the uploaded database.

Save the file as ``secret.yaml``. The example below is for AWS/S3.

.. code-block:: yaml

   apiVersion: v1
   kind: Secret
   metadata:
    name: test-restore
   type: Opaque
   stringData:
    AWS_ACCESS_KEY_ID: XXXXXXXXXXXX
    AWS_SECRET_ACCESS_KEY: XXXXXXXXXXXX/XXXXXXXXXXXX
    AWS_REGION: us-east-1
    S3_PROVIDER: AWS

**Parameters**

- ``name``: The name of this manifest which is referenced in the installation manifest.

6. Create a Mattermost cluster installation manifest:

Open a text editor and create a text file with the following details. Save the file as ``mattermost-installation.yaml``:

.. code-block:: yaml

  apiVersion: mattermost.com/v1alpha1
  kind: ClusterInstallation
  metadata:
    name: mm-example-full
  spec:
    size: ""
    ingressName: example.mattermost-example.com
    ingressAnnotations:
      kubernetes.io/ingress.class: nginx
    version: 5.14.0
    mattermostLicenseSecret: ""
    database:
      storageSize: 50Gi
    minio:
      storageSize: 50Gi
    elasticSearch:
      host: ""
      username: ""
      password: ""

The Mattermost installation manifest contains fields which must be edited in line with your configuration and environment requirements.

7. Create a restore manifest:

Open a text editor and create a text file with the following details. Save the file as ``restore.yaml``:

.. code-block:: yaml

  apiVersion: mattermost.com/v1alpha1
  kind: MattermostRestoreDB
  metadata:
    name: example-mattermostrestoredb
  spec:
    initBucketURL: s3://my-sample/my-backup.gz
    mattermostClusterName: example-clusterinstallation
    mattermostDBName: mattermostdb
    mattermostDBPassword: supersecure
    mattermostDBUser: ""
    restoreSecret: ""

**Parameters**

- ``mattermostClusterName``: The ClusterInstallation file name.
- ``restoreSecret``: The location of the backup file.
- ``mattermostDBPassword``: The password used to access the database.
- ``mattermostDBUser``: The username required to access the database.
- ``initBucketURL``: The URL of the storage instance/server where the backed up DB is stored.

8. To initiate deployment, apply the file and specify the path where the newly-created files have been saved:

.. code-block:: sh

      $ kubectl create ns mattermost
      $ kubectl apply -n mattermost -f /path/to/secret.yaml
      $ kubectl apply -n mattermost -f /path/to/mattermost-installation.yaml
      $ kubectl apply -n mattermost -f /path/to/restore.yaml

The deployment process can be monitored in the Kubernetes user interface. If errors or issues are experienced, review the Mattermost, Operator, and MySQL logs for guidance including error messages. If remediation is not successful, contact Mattermost customer support for assistance.

Once complete, access your Mattermost instance and confirm that the database has been restored.
