.. _install-kubernetes-operator:

Installing the Operators
------------------------

The operators are installed using ``kubectl`` and each operator is created in its own namespace. You can install and run multiple Mattermost installations in the same cluster using different namespaces.

**1. Install NGINX ingress controller**

Follow the instructions `here <https://kubernetes.github.io/ingress-nginx/deploy/>`__.

**2. Install the Mattermost Operator**

.. code-block:: sh

  $ kubectl create ns mattermost-operator
  $ kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml

Installing MySQL and MinIO operator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MySQL operator and MinIO operator are a good way to try out the Mattermost Operator or develop it on a local cluster but they **are not recommended for production usage**.

**1. Install the MySQL operator**

.. code-block:: sh

  $ kubectl create ns mysql-operator
  $ kubectl apply -n mysql-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mysql-operator/mysql-operator.yaml

**2. Install the MinIO operator**

.. code-block:: sh

  $ kubectl create ns minio-operator
  $ kubectl apply -n minio-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/minio-operator/minio-operator.yaml
