.. _install-kubernetes-mattermost:

Deploying a Mattermost Installation
===================================

This guide describes deploying a complete Mattermost installation in Kubernetes including a database. In most
cases you'll create and apply a single manifest. In the case of an Enterprise installation, two manifests will be applied.

Manifest files contain the configurations needed for the
operator to perform tasks and communicate with Kubernetes. Create the manifest file locally,
copy and paste the contents, and save the file with the relevant name.

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

Open a text editor and create a text file with the following details.

Save the file as ``mattermost-installation.yaml``:

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

**3. Edit the Installation Manifest File**

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

**4. Apply the Installation Manifest File**

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

You can use an existing Mattermost MySQL database with a new Mattermost installation using the Mattermost Kubernetes Operator. In order to do this,
you'll need to have created a backup of your MySQL database which is stored somewhere accessible (e.g., in AWS S3). The steps you follow to
create and upload your backup depends on the provider you're using and your use case. It's recommended that you consult their documentation or,
if your deployment is managed in a different way, consult your Administrator.

In a production deployment the basic flow is to create a backup (mysqldump) > create a new instance > install MySQL > restore the
dump to this instance > install a backup program > perform the backup of the dump > upload it to your cloud storage provider > create
a Mattermost cluster(is this yaml?) > create a restore/backup secret (yaml?) > create the restore manifest and deploy it.

Your Mattermost cluster will look like the same file as above. You may also need a restore/backup secret that you'd add to the file. Then,
in the Mattermost cluster file you add the following section to "spec" (leaving in the previous section as well)

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

To initiate deployment, apply the file, specifying the correct path, using:

.. code-block:: sh

      $ kubectl create ns mattermost
      $ kubectl apply -n mattermost -f /path/to/mattermost-installation.yaml

The deployment process can be monitored in the Kubernetes user interface.
