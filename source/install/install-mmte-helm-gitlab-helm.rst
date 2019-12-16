..  _install-mmte-helm-gitlab-helm:

How to install Mattermost Team Edition Helm Chart in GitLab Helm Chart deployment
=====================================================================================

This document describes how to install Mattermost Team Edition Helm Chart in proximity with an existing GitLab Helm Chart deployment, utilizing shared configurations to streamline authentication, storage, encryption, and traffic routing.

As the Mattermost Helm Chart is installed in a separate namespace, it is recommended that cert-manager and nginx-ingress be configured to manage cluster-wide ingress and certificate resources. 

The steps in this document presume in-chart Minio instance usage. For information about out-of-chart object storage configuration, review `this document <https://gitlab.com/gitlab-org/charts/gitlab/tree/master/doc/charts/registry#storage>`__ for GCS and S3 examples. Alternatively, visit your provider's Help documentation for configuration settings. 


Prerequisites
----------------------------

  - A running Kubernetes cluster with a PostgreSQL database.
  - A running GitLab Helm Chart release.
  - The name of the secret that holds your PostgreSQL password ``<gitlab>-postgresql-password``.
  - The name of the secret that holds your Minio keys ``<gitlab>-minio-secret``.
  - The service name for your PostgreSQL, ``<gitlab>-postgresql``, and the port. If you installed the GitLab helm chart in ``default`` namespace, then the port is ``5432``.
  - The service name for Minio and the port, ``<gitlab>-minio-svc``, and the port. If you installed the GitLab helm chart in ``default`` namespace, then the port is ``9000``.
  - The names of ``kubernetes.io/ingress.class``, ``kubernetes.io/ingress.provider`` and ``certmanager.k8s.io/issuer``.
  
**Note:**
There is an option to use external database services (PostgreSQL or MySQL) for your Mattermost installation. If you use an external database you will need to disable the MySQL chart in the ``values.yaml`` as per the example in this document.

Deploy GitLab Helm Chart
----------------------------

To deploy Gitlab Helm Chart, follow the instructions described `here <https://docs.gitlab.com/ee/install/kubernetes/gitlab_chart.html>`__.

Here is a light way to install it:

.. code-block:: bash

  $ helm upgrade --install gitlab gitlab/gitlab \
    --timeout 600 \
    --set global.hosts.domain=``<your-domain>`` \
    --set global.hosts.externalIP=``<external-ip>`` \
    --set certmanager-issuer.email=``<email>``

- ``<your-domain>``: your desired domain, eg. ``gitlab.example.com``.
- ``<external-ip>``: the external IP pointing to your Kubernetes cluster.
- ``<email>``: email to register in Let's Encrypt to retrieve TLS certificates.

Once all pods are running, log in to GitLab. 

Create an OAuth application with GitLab
--------------------------------------------

To create the OAuth application to allow Mattermost to use GitLab as the authentication provider, please follow the instructions `here <https://docs.mattermost.com/deployment/sso-gitlab.html>`__.

Please take note of the ``Application ID``, ``Application Secret Key``, ``User API Endpoint``, ``Auth Endpoint`` and ``Token Endpoint`` settings, as these values will be used later when deploying Mattermost.

Deploy Mattermost Team Edition Helm Chart
--------------------------------------------

Requirements:

  - Mattermost Team Edition Helm Chart Version: 3.8.2

To deploy Mattermost Team Edition with GitLab Helm Chart, disable the running ``MySql`` chart and configure InitContainer and Environment variables in ``values.yaml``. The list below indicates the values that should be changed. Note that we assume the GitLab chart name is ``gitlab``.

- ``<your-mattermost-domain>``: URL that users will use to access Mattermost, matching the `Site URL field <https://docs.mattermost.com/administration/config-settings.html#site-url>`__, e.g. ``mattermost.gitlab.example.com``.
- ``<name-of-your-tls-secret>``: A name to store the TLS certificate for your domains, e.g. ``mattermost-tls``.
- ``<ingress-class>``: The ingress class. In a basic GitLab deployment, this is ``gitlab-nginx``.
- ``<ingress-provider>``: The ingress provider. In a basic GitLab deployment, this is ``nginx``.
- ``<certmanager-issuer>``: The cert manager issuer. In a basic GitLab deployment, this is ``gitlab-issuer``.
- ``<gitlab-ap-secret>``: The Application secret, which you created in step `Create an OAuth application with GitLab`_.
- ``<gitlab-app-id>``: The Application ID, which you created in step `Create an OAuth application with GitLab`_.
- ``<your-gitlab-domain>``: The GitLab domain name, e.g., ``gitlab.example.com``.
- ``<gitlab-postgres.username>``: The GitLab PostgreSQL username. Default is ``gitlab``.
- ``<gitlab-postgres.passwd-secret>``: Secret that holds your PostgreSQL password. Default is ``gitlab-postgresql-password``.
- ``<gitlab-postgres-host>``: Postgres host of your Kubernetes service. Default is ``gitlab-postgresql``.
- ``<gitlab-postgres-port>``: Postgres port of your Kubernetes service. Default is ``5432``.
- ``<mattermost-database-name>``: Mattermost database, e.g., ``mattermost-db``.
- ``<gitlab-minio-host>``: Minio host of your Kubernetes service. Default is ``gitlab-minio-svc``.
- ``<gitlab-minio-port>``: Minio port of your Kubernetes service. Default is ``9000``.
- ``<gitlab-minio-secret>``: Secret that holds your Minio keys. Default is ``gitlab-minio-secret``.
- ``<mattermost-minio-bucket-name>``: Mattermost Minio bucket name, e.g., ``mattermost-data``.


.. code-block:: yaml

  persistence:
    data:
      enabled: false

  # Mattermost configuration:
  configJSON:
    SiteUrl: "https://<your-mattermost-domain>"
    SiteName: "Mattermost"
    EnableSignUpWithEmail: false

  ingress:
    enabled: true
    path: /
    annotations:
      kubernetes.io/ingress.class:  <ingress-class>
      kubernetes.io/ingress.provider: <ingress-provider>
      certmanager.k8s.io/issuer:  <certmanager-issuer>
    hosts:
      - <your-mattermost-domain>
    tls:
      - secretName: <name-of-your-tls-secret>
        hosts:
          - <your-mattermost-domain>

  auth:
    gitlab:
      Enable: "true"
      Secret: "<gitlab-app-secret>"
      Id: "<gitlab-app-id>"
      Scope: ""
      AuthEndpoint: "https://<your-gitlab-domain>/oauth/authorize"
      TokenEndpoint: "https://<your-gitlab-domain>/oauth/token"
      UserApiEndpoint: "https://<your-gitlab-domain>/api/v4/user"

  externalDB:
    enabled: true
    existingUser: <gitlab-postgres-username>
    existingSecret: "<gitlab-postgres.passwd-secret>"

  mysql:
    enabled: false

  ## Additional env vars
  extraEnvVars:
    - name: POSTGRES_PASSWORD_GITLAB
      valueFrom:
        secretKeyRef:
          name: <gitlab-postgres-passwd-secret>
          key: postgres-password
    - name: POSTGRES_USER_GITLAB
      value: <gitlab-postgres-username>
    - name: POSTGRES_HOST_GITLAB
      value: <gitlab-postgres-host>
    - name: POSTGRES_PORT_GITLAB
      value: "<gitlab-postgres-port>"
    - name: POSTGRES_DB_NAME_MATTERMOST
      value: <mattermost-database-name>
    - name: MM_SQLSETTINGS_DRIVERNAME
      value: "postgres"
    - name: MM_SQLSETTINGS_DATASOURCE
      value: postgres://$(POSTGRES_USER_GITLAB):$(POSTGRES_PASSWORD_GITLAB)@$(POSTGRES_HOST_GITLAB):$(POSTGRES_PORT_GITLAB)/$(POSTGRES_DB_NAME_MATTERMOST)?sslmode=disable&connect_timeout=10
    - name: MINIO_ENDPOINT
      value: <gitlab-minio-host>
    - name: MINIO_PORT
      value: "<gitlab-minio-port>"
    - name: MM_FILESETTINGS_DRIVERNAME
      value: amazons3
    - name: MM_FILESETTINGS_AMAZONS3ENDPOINT
      value: $(MINIO_ENDPOINT):$(MINIO_PORT)
    - name: MM_FILESETTINGS_AMAZONS3ACCESSKEYID
      valueFrom:
        secretKeyRef:
          name: <gitlab-minio-secret>
          key: accesskey
    - name: MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY
      valueFrom:
        secretKeyRef:
          name: <gitlab-minio-secret>
          key: secretkey
    - name: MM_FILESETTINGS_AMAZONS3BUCKET
      value: <mattermost-minio-bucket-name>

  ## Additional init containers
  extraInitContainers: 
    - name: bootstrap-database
      image: "postgres:9.6-alpine"
      imagePullPolicy: IfNotPresent
      env:
        - name: POSTGRES_PASSWORD_GITLAB
          valueFrom:
            secretKeyRef:
              name: gitlab-postgresql-password
              key: postgres-password
        - name: POSTGRES_USER_GITLAB
          value: <gitlab-postgres-username>
        - name: POSTGRES_HOST_GITLAB
          value:<gitlab-postgres-host>
        - name: POSTGRES_PORT_GITLAB
          value: "<gitlab-postgres-port>"
        - name: POSTGRES_DB_NAME_MATTERMOST
          value: <mattermost-database-name>
      command:
        - sh
        - "-c"
        - |
          if PGPASSWORD=$POSTGRES_PASSWORD_GITLAB psql -h $POSTGRES_HOST_GITLAB -p $POSTGRES_PORT_GITLAB -U $POSTGRES_USER_GITLAB -lqt | cut -d \| -f 1 | grep -qw $POSTGRES_DB_NAME_MATTERMOST; then
          echo "database already exist, exiting initContainer"
          exit 0
          else
          echo "Database does not exist. creating...."
          PGPASSWORD=$POSTGRES_PASSWORD_GITLAB createdb -h $POSTGRES_HOST_GITLAB -p $POSTGRES_PORT_GITLAB -U $POSTGRES_USER_GITLAB $POSTGRES_DB_NAME_MATTERMOST
          echo "Done"
          fi
    - name: create-minio-bucket
      image: "minio/mc:RELEASE.2018-07-13T00-53-22Z"
      env:
        - name: MINIO_ENDPOINT
          value: <gitlab-minio-host>
        - name: MINIO_PORT
          value: "<gitlab-minio-port>"
        - name: MINIO_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: <gitlab-minio-secret>
              key: accesskey
        - name: MINIO_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: <gitlab-minio-secret>
              key: secretkey
        - name: MATTERMOST_BUCKET_NAME
          value: <mattermost-minio-bucket-name>
      command:
        - sh
        - "-c"
        - |
          echo "Connecting to Minio server: http://$MINIO_ENDPOINT:$MINIO_PORT"
          mc config host add myminio http://$MINIO_ENDPOINT:$MINIO_PORT $MINIO_ACCESS_KEY $MINIO_SECRET_KEY
          /usr/bin/mc ls myminio
          echo $?
          /usr/bin/mc ls myminio/$MATTERMOST_BUCKET_NAME > /dev/null 2>&1
          if [ $? -eq 1 ] ; then
            echo "Creating bucket '$MATTERMOST_BUCKET_NAME'"
            /usr/bin/mc mb myminio/$MATTERMOST_BUCKET_NAME
          else
            echo "Bucket '$MATTERMOST_BUCKET_NAME' already exists."
            exit 0
          fi

After these changes, deploy the Mattermost Team Edition Helm Chart with following command:

.. code-block:: bash

  $ helm upgrade --install mattermost -f values.yaml mattermost/mattermost-team-edition

Wait for the pods to run. Then access your Mattermost server, and log in with your GitLab credentials.

Troubleshooting
---------------------

If you have any trouble installing Mattermost Team Edition in GitLab Helm Chart deployment, let us know in our `Troubleshooting forum <http://www.mattermost.org/troubleshoot/>`__ and we'll be happy to help.
