.. _install-kubernetes-mattermost:

Deploy a Mattermost Installation
============================

Deploying a Mattermost installation is very simple and just requires creating and applying a single manifest.

**1. Create your installation manifest file**

Save the following into a file named ``mattermost-installation.yaml``:

.. code-block:: yaml

  apiVersion: mattermost.com/v1alpha1
  kind: ClusterInstallation
  metadata:
    name: mm-example-full
  spec:
    size: 5000users
    ingressName: example.mattermost-example.com 
    version: 5.14.0
    database:
      storageSize: 50Gi
    minio:
      storageSize: 50Gi
    elasticSearch:
      host: ""
      username: ""
      password: ""

**2. Edit your installation manifest file**

Depending on your desired configuration, edit the following fields in your manifest. There are a few fields that must be modified, which are marked accordingly in the table below.

.. csv-table::
    :header: "Field", "Description", "Must Edit"

    "metadata.name", "The name of your Mattermost as it will be shown in Kubernetes. The shorter the better.", "Yes"
    "spec.size", "The size of your installation. This can be '100users', '1000users, '5000users', '10000users', or '25000users'.", "Yes"
    "spec.ingressName", "The DNS for your Mattermost installation.", "Yes"
    "spec.version", "The Mattermost version.", "No"
    "spec.database.storageSize", "The storage size for your database. Your Kubernetes cluster must have volumes this size or larger.", "No"
    "spec.minio.storageSize", "The storage size for your file storage. Your Kubernetes cluster must have volumes this size or larger.", "No"
    "spec.elasticSearch", "The section for Elasticsearch settings. Remove this section if you will not be using Elasticsearch.", "No"
    "spec.elasticSearch.host", "The hostname for your Elasticsearch instance.", "No"
    "spec.elasticSearch.username", "The username for your Elasticsearch instance.", "No"
    "spec.elasticSearch.password", "The password for your Elasticsearch instance.", "No"

There are more advanced fields documented `here <https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/examples/full.yaml>`__.

**3. Apply your installation manifest file**

To deploy your installation, apply it with:

.. code-block:: sh

  $ kubectl create ns mattermost
  $ kubectl apply -n mattermost -f /path/to/mattermost-installation.yaml

Make sure to replace ``/path/to/mattermost-installation.yaml`` with the correct path.

**4. Use Mattermost**

After waiting 3-5 minutes for your deployment to complete, run the following to get the hostname or IP address to access Mattermost at:

.. code-block:: sh

  $ kubectl -n mattermost get svc

The ``EXTERNAL-IP` of the service with the name matching the ``metadata.name`` entered in your installation manifest file will be how you access Mattermost.
