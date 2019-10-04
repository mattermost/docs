.. _install-kubernetes-mattermost:

Deploy a Mattermost Installation
============================

Deploying a Mattermost installation is very simple and just requires creating and applying a single manifest.

**1. (Enterprise only) Create your Mattermost license secret**

Save the following in a file named ``mattermost-license-secret.yaml``:

.. code-block:: yaml

  apiVersion: v1
  kind: Secret
  metadata:
    name: mattermost-license
  type: Opqaue
  stringData:
    license: %LICENSE_FILE_CONTENTS%

Replace ``%LICENSE_FILE_CONTENTS%`` with the contents of your Mattermost license file. 

Apply it with:

.. code-block:: sh

  $ kubectl apply -f /path/to/mattermost-license-secret.yaml

**2. Create your installation manifest file**

Save the following into a file named ``mattermost-installation.yaml``:

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

**3. Edit your installation manifest file**

Depending on your desired configuration, edit the following fields in your manifest. There are a few fields that must be modified, which are marked accordingly in the table below.

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

**4. Apply your installation manifest file**

To deploy your installation, apply it with:

.. code-block:: sh

  $ kubectl create ns mattermost
  $ kubectl apply -n mattermost -f /path/to/mattermost-installation.yaml

Make sure to replace ``/path/to/mattermost-installation.yaml`` with the correct path.

**4. Configure DNS and Use Mattermost**

After waiting 3-5 minutes for your deployment to complete, run the following to get the hostname or IP address to access Mattermost at:

.. code-block:: sh

  $ kubectl -n mattermost get ingress

This will give you either a hostname or IP address under the ``ADDRESS`` column. Copy that address.

Use your domain registration service to create a canonical name or IP address record for the ``ingressName`` in your manifest, pointing to the address you just copied. For example, on AWS you would do this within a hosted zone in Route53.

Go to your ``ingressName`` URL in your browser and use Mattermost.
