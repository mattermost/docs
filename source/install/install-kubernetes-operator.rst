.. _install-kubernetes-operator:

Installing the Mattermost Operator
============================

The Mattermost Kubernetes Operator allows you to easily deploy and manage Mattermost installations through a single Kubernetes manifest. This operator is continuously being developed and will include additional features in the future. 

**1. Install the MySQL operator**

.. code-block:: sh

  $ kubectl create ns mysql-operator
  $ kubectl apply -n mysql-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mysql-operator/mysql-operator.yaml

**2. Install the MinIO operator**

.. code-block:: sh

  $ kubectl create ns minio-operator
  $ kubectl apply -n minio-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/minio-operator/minio-operator.yaml

**3. Install NGINX Ingress Controller**

Follow the instructions `here <https://kubernetes.github.io/ingress-nginx/deploy/>`__.

**4. Install the Mattermost operator**

.. code-block:: sh

  $ kubectl create ns mattermost-operator
  $ kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml
