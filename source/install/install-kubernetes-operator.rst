.. _install-kubernetes-operator:

Installing the Operators
============================

The required operators are installed using ``kubectl`` and each operator is created in its own namespace. Shorter namespace names
are recommended. You can install and run multiple Mattermost installations in the same cluster using different namespaces.

The steps provided below include database and storage operators. To install only the Mattermost
operator, see `Using a Custom Configuration <https://kubernetes.github.io/ingress-nginx/deploy/>`__.


**1. Install the MySQL operator**

.. code-block:: sh

  $ kubectl create ns mysql-operator
  $ kubectl apply -n mysql-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mysql-operator/mysql-operator.yaml

**2. Install the MinIO operator**

.. code-block:: sh

  $ kubectl create ns minio-operator
  $ kubectl apply -n minio-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/minio-operator/minio-operator.yaml

**3. Install NGINX Ingress controller**

Follow the instructions `here <https://kubernetes.github.io/ingress-nginx/deploy/>`__.

**4. Install the Mattermost operator**

.. code-block:: sh

  $ kubectl create ns mattermost-operator
  $ kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml

Once completed, the installed components are listed in the configuration of your cluster.
