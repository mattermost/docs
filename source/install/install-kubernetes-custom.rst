.. _install-kubernetes-custom:

Using a Custom Configuration
=================================

You can opt to install the Mattermost operator on top of your existing infrastructure in which case you only need to install the Mattermost operator:

.. code-block:: sh

   $ kubectl create ns mattermost-operator
   $ kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml

Understanding Resource Requirements
-----------------------------------

Running Mattermost in Kubernetes requires different resources based on your total number of users.
The table below details the minimum Kubernetes cluster resources that Mattermost requires at different scales.

.. csv-table::
   :header: "User Count", "Node Count", "Memory per Node", "vCPU per Node"
   "5,000", "6", "8 GB", "4"
   "10,000", "8", "16 GB", "4"
   "25,000", "14", "16 GB", "4"

The resource requirements, as well as the ingress name are added to the relevant field in the Mattermost manifest file, which is then deployed in your cluster.

Open a text editor and create a text file with the following details.

.. code-block:: yaml

  apiVersion: mattermost.com/v1alpha1
  kind: ClusterInstallation
  metadata:
    name: mm-example-full
  spec:
    size:
    ingressName:
    ingressAnnotations:
      kubernetes.io/ingress.class:
    version: 5.14.0
    mattermostLicenseSecret: ""
    database:
      storageSize:
    minio:
      storageSize:
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

The deployment process can be monitored in the Kubernetes user interface. Once complete, you can access Mattermost using the ingress name specified in the manifest.
