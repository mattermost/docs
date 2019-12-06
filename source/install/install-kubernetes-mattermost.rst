.. _install-kubernetes-mattermost:

Deploying a Mattermost Installation
===================================

This guide describes deploying a complete Mattermost installation in Kubernetes including a database. In most
cases you'll create and apply a single manifest. In the case of an Enterprise installation, two manifests will be applied - one
for the license and one for the cluster installation.

Manifest files contain the configurations needed for the
operator to perform tasks and communicate with Kubernetes. Create the manifest file locally in a text editor,
copy and paste the contents, and save the file. Recommended file names are provided, but your naming conventions may differ.

**1. (Enterprise only) Create a Mattermost License Secret**

Open a text editor and create a text file with the following details.

**Note:** Replace ``%LICENSE_FILE_CONTENTS%`` with the contents of your Mattermost license file.

.. code-block:: yaml

  apiVersion: v1
  kind: Secret
  metadata:
    name: mattermost-license
  type: Opqaue
  stringData:
    license: %LICENSE_FILE_CONTENTS%

Save the file as ``mattermost-license-secret.yaml``. Apply the file, specifying the correct path, using:

.. code-block:: sh

  $ kubectl apply -f /path/to/mattermost-license-secret.yaml

**2. Create an Installation Manifest File**

The Mattermost installation manifest contains fields which must be edited in line with your configuration and environment requirements.

.. csv-table::
    :header: "Field", "Description", "Must Edit"

    "metadata.name", "The name of your Mattermost as it will be shown in Kubernetes. The shorter the better.", "Yes"
    "spec.size", "The size of your installation. This can be '100users', '1000users, '5000users', '10000users', or '25000users'.", "Yes"
    "spec.ingressName", "The DNS for your Mattermost installation.", "Yes"
    "spec.version", "The Mattermost version.", "No"
    "spec.mattermostLicenseSecret", "The name of the Kubernetes secret containing your license (e.g. mattermost-license). Required for enterprise deployments.", "Yes"
    "spec.database.storageSize", "The storage size for your database. Your Kubernetes cluster must have volumes this size or larger.", "No"
    "spec.minio.storageSize", "The storage size for your file storage. Your Kubernetes cluster must have volumes this size or larger.", "No"
    "spec.elasticSearch", "The section for Elasticsearch settings. Remove this section if you will not be using Elasticsearch.", "No"
    "spec.elasticSearch.host", "The hostname for your Elasticsearch instance.", "No"
    "spec.elasticSearch.username", "The username for your Elasticsearch instance.", "No"
    "spec.elasticSearch.password", "The password for your Elasticsearch instance.", "No"

There are more advanced fields documented `here <https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/examples/full.yaml>`__.

Open a text editor and create a text file with the following details.

.. code-block:: yaml

  apiVersion: mattermost.com/v1alpha1
  kind: ClusterInstallation
  metadata:
    name: mm-example-full
  spec:
    size: 5000users
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

Save the file as ``mattermost-installation.yaml``.

**3. Apply the Installation Manifest File**

To initiate deployment, apply the file, specifying the correct path, using:

.. code-block:: sh

  $ kubectl create ns mattermost
  $ kubectl apply -n mattermost -f /path/to/mattermost-installation.yaml

The deployment process can be monitored in the Kubernetes user interface.

**4. Configure DNS and Use Mattermost**

When the deployment is complete, obtain the hostname or IP address of your Mattermost deployment using the following command:

.. code-block:: sh

  $ kubectl -n mattermost get ingress

Copy the resulting hostname or IP address from the ``ADDRESS`` column, open your browser, and connect to Mattermost.

Use your domain registration service to create a canonical name or IP address record for the ``ingressName`` in your manifest,
pointing to the address you just copied. For example, on AWS you would do this within a hosted zone in Route53.

Navigate to the ``ingressName`` URL in your browser and use Mattermost.

Restoring an Existing Mattermost MySQL Database
-----------------------------------------------

>> I wonder whether this wouldn't be better off in the Install Cluster section of the guide because it covers installation/deployment
and has a bit more complexity to it? 

You can use the Mattermost Kubernetes Operator and utilize an existing Mattermost MySQL database with a new Mattermost installation.
The steps you follow to create and upload your backup depends on the provider you're using and your use case. It's
recommended that you consult their documentation or, if your deployment is managed in a different way, consult your Administrator.

The following steps provide an overview of the process.

1. Create a backup of your database (e.g., using *mysqldump*).
2. Deploy a new server (e.g., an AWS instance).
3. Install a backup program and back up the database on the new server/instance.
4. Upload the backed up database to your cloud storage provider (e.g., Amazon S3).
5. Create a ``secret.yaml``` file:

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

Where


6. Create a Mattermost cluster installation manifest. (should we link to the install documentation which will also shortly include
the custom settings and mention that this is a separate installation of Mattermost and should be sized appropriately?)

Open a text editor and create a text file with the following details. Save the file as ``mattermost-installation.yaml``:

.. code-block:: yaml

  apiVersion: mattermost.com/v1alpha1
  kind: ClusterInstallation
  metadata:
    name: mm-example-full
  spec:
    size: 5000users
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

Where:


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
    mattermostDBUser: mmuser
    restoreSecret: myawscreds

Where:
- mattermostClusterName defines the ClusterInstallation name (is this the mattermost installation yaml file created in previous step?)
- RestoreSecret defines where the backup file is located (is this the secret.yaml file and, if so, why is it called myawscreds?)
- mattermostDBPassword defines the password used to access the database (which database? the one uploaded to AWS?)
- mattermostDBUser defines the username required to access the database (the MM database? Or the uploaded one?)
- initBucketURL defines the URL of the storage instance/server where the backed up DB is stored (yes?)

8. To initiate deployment, apply the file and specify the path where the newly-created files have been saved:

.. code-block:: sh

      $ kubectl create ns mattermost
      $ kubectl apply -n mattermost -f /path/to/mattermost-installation.yaml

Where
ns defines the new mattermost installation where the backed up database will be restored. (is this a separate namespace to
the initial one and, if so, should we specify this?)

The deployment process can be monitored in the Kubernetes user interface.

Once complete, access your Mattermost instance and confirm that the database has been restored.

Issues experienced: check MM log or MySQL log for guidance.
