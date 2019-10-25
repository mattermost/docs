.. _install-kubernetes-operator:

Installing the Operators
============================

To get started, first install the required operators using kubectl.

**1. Install the MySQL Operator**

.. code-block:: sh

  $ kubectl create ns mysql-operator
  $ kubectl apply -n mysql-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mysql-operator/mysql-operator.yaml

**2. Install the MinIO Operator**

.. code-block:: sh

  $ kubectl create ns minio-operator
  $ kubectl apply -n minio-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/minio-operator/minio-operator.yaml

**3. Install NGINX Ingress Controller**

Follow the instructions `here <https://kubernetes.github.io/ingress-nginx/deploy/>`__.

**4. Install the Mattermost Operator**

.. code-block:: sh

  $ kubectl create ns mattermost-operator
  $ kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml

Once completed, the installed components are listed in the configuration of your cluster.
