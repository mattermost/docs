Mattermost Kubernetes Operator
===============================

What is an operator?
--------------------

In Kubernetes, an operator is a set of product- or application-specific instructions packaged into its own program. It tells an application what to run, where to find it, and how to configure it. An operator can automate complex application deployment and operation activities, such as installation, configuration changes, software updates, failure recovery, and more.

.. warning::

  If you used the Mattermost Kubernetes Operator prior to v1.12.x, or you're still using the ``ClusterInstallation`` Custom Resource, check out `this guide <https://github.com/mattermost/mattermost-operator/blob/master/docs/migration.md>`__ to learn how to migrate to thenew ``Mattermost`` resource.

Confirm resource requirements for production
--------------------------------------------

Running Mattermost in Kubernetes requires different resources based on your total number of users. Minimum requirements are listed in the following table:

.. csv-table::
    :header: "User Count", "Node Count", "Memory per Node", "vCPU per Node"

    "5,000", "6", "8 GB", "4"
    "10,000", "8", "16 GB", "4"
    "25,000", "14", "16 GB", "4"

- These resources take into account all components required for Mattermost, including proxy, database, and file storage.
- Requirements may be significantly lower when using an external database and filestore (recommended).  
- Resource requirements may vary depending on user usage and bot activity.
- For larger installations, it may be beneficial to use nodes for the databases that have more memory and/or are optimized for memory.
- For installations of more than 25,000 users please `contact us <https://mattermost.com/contact-us/>`__ for sizing guidelines.

Try out the Mattermost Operator
-------------------------------

The MySQL operator and MinIO operator are a good way to try out the Mattermost Operator or develop it on a local cluster; however, it's not recommended for production deployments.

1. Install the MySQL operator:

  .. code-block:: sh

    $ kubectl create ns mysql-operator
    $ kubectl apply -n mysql-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mysql-operator/mysql-operator.yaml

2. Install the MinIO operator:

  .. code-block:: sh

    $ kubectl create ns minio-operator
    $ kubectl apply -n minio-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/minio-operator/minio-operator.yaml 

Rolling upgrades
----------------

The Mattermost Kubernetes Operator supports rolling upgrades, so you can upgrade your Mattermost deployment with zero downtime. This process requires at least two replicas as a rolling upgrade cannot be performed if there is only one pod. Replicas are created when a user count is selected and exceeds 100.

New Mattermost releases are announced via our community server, as well as social media and email.

Perform a rolling upgrade
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to your Kubernetes instance.
2. Open the ``mattermost-installation.yaml`` manifest (the one created during installation).
3. Update the ``spec.version`` value to the new version.
4. Save the changes.

Apply the changes with ``kubectl``:

.. code-block:: sh

  $ kubectl apply -n mattermost -f [PATH_TO_MATTERMOST_MANIFEST]

The operator initiates a job in the Kubernetes cluster and once migration is complete the pods are restarted. If necessary, a database migration is also performed.

To view information about the running job, use

.. code-block:: sh

  $ kubectl -n mattermost get jobs

At least one pod is available at all times and once all pods are restarted with the new version the upgrade is complete.

To view the status of the pods and to confirm their state, use

.. code-block:: sh

  $ kubectl -n mattermost get pods

The *STATUS* of the pods should be running/ready, with an *AGE* of 10-15 seconds.

Restore an existing Mattermost MySQL database
---------------------------------------------

The Mattermost Operator can be used in a backup and restore scenario to apply an existing Mattermost MySQL database to a new Mattermost installation, in its own namespace. This can also be helpful in the event that you need to revert your Mattermost instance's database to the most recent backup point, on your existing installation. In both cases, you will need a backup of your database.

The steps you follow to create and upload your backup depends on the provider you're using and your use case. It's recommended that you consult the relevant documentation or, if your deployment is managed in a different way, consult your Administrator.

It is important to note that this process requires the creation of a new Mattermost installation - editing the existing ``.yaml`` files is not recommended and can result in data loss.

The process described below needs to be completed prior to proceeding with the Mattermost deployment.

1. Create a backup of your database (e.g. using *mysqldump*).
2. Deploy a new server (e.g. an AWS instance).
3. Install a backup program and back up the database on the new server/instance.
4. Upload the backed up database to your cloud storage provider (e.g. Amazon S3).
5. Create a ``secret.yaml`` file:

  a. Open a text editor and create a text file containing your credentials which will be used to access the uploaded database.

  b. Save the file as ``secret.yaml``. The example below is for AWS/S3, where ``name`` indicates the name of this manifest referenced in the install manifest.

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

6. Create a Mattermost cluster installation manifest by opening a text editor and creating a text file with the following details. The Mattermost installation manifest contains fields which must be edited in line with your configuration and environment requirements. Save the file as ``mattermost-installation.yaml``:

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

7. Create a restore manifest by opening a text editor and creating a text file with the following details. Save the file as ``restore.yaml``:

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

.. include:: faq_kubernetes.rst
  :start-after: :nosearch: