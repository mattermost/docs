..  _install-mmte-helm-gitlab-helm:

How to install Mattermost Team Edition Helm Chart in GitLab Helm Chart deployment
=====================================================================================

This document describes how to install Mattermost Team Edition Helm Chart in an existing GitLab Helm Chart deployment.

Pre-requisites
----------------------------

  - A running Kubernetes cluster with PostgreSQL database.
  - A running GitLab Helm Chart with chart name **<GITLAB>**.
  - The name of the secret that holds your PostgreSQL password, ``<GITLAB>-postgresql-password``.
  - The name of the secret that holds your Minio keys, ``<GITLAB>-minio-secret``.
  - The service name for your PostgreSQL, ``<GITLAB>-postgresql``, and the port. If you installed the GitLab helm chart in ``default`` namespace, then the port is ``5432``.
  - The service name for Minio and the port, ``<GITLAB>-minio-svc``, and the port. If you installed the GitLab helm chart in ``default`` namespace, then the port is ``9000``.
  - The names of ``kubernetes.io/ingress.class``, ``kubernetes.io/ingress.provider`` and ``certmanager.k8s.io/issuer``.

Deploy GitLab Helm Chart
----------------------------

To deploy Gitlab Helm Chart, follow the instructions described `here <https://docs.gitlab.com/ee/install/kubernetes/gitlab_chart.html>`_.

Here is a light way to install it:

.. code-block:: bash

  $ helm upgrade --install gitlab gitlab/gitlab \
    --timeout 600 \
    --set global.hosts.domain=<YOUR.DOMAIN> \
    --set global.hosts.externalIP=<EXTERNAL.IP> \
    --set certmanager-issuer.email=<EMAIL>
 
- **<YOUR.DOMAIN>**: your desired domain, eg. ``gitlab.example.com``
- **<EXTERNAL.IP>**: the external IP pointing to your Kubernetes cluster
- **<EMAIL>**: email to register in Let's Encrypt to retrieve TLS certificates

After all pods are running, log in to GitLab.

Create an OAuth application with GitLab
--------------------------------------------

To create the OAuth application to allow Mattermost to use GitLab as the authentication provider, please follow the instructions `here <https://docs.mattermost.com/deployment/sso-gitlab.html>`_.

Please take note of the ``Application ID``, ``Application Secret Key``, ``User API Endpoint``, ``Auth Endpoint`` and ``Token Endpoint`` settings, as these values will be used later when deploying Mattermost.

Deploy Mattermost Team Edition Helm Chart
--------------------------------------------

Requirements:
  - Mattermost Team Edition Helm Chart Version => 1.4.0

To deploy Mattermost Team Edition with GitLab Helm Chart, disable the running ``MySql`` chart and configure InitContainer and Environment variables in ``values.yaml`` as follows:

.. code-block:: yaml

  persistence:
    data:
      enabled: false

  # Mattermost configuration:
  config:
    siteUrl: "https://<YOUR.MATTERMOST.DOMAIN>"
    siteName: "Mattermost"
    enableSignUpWithEmail: false

  ingress:
    enabled: true
    path: /
    annotations:
      kubernetes.io/ingress.class:  <INGRESS.CLASS>
      kubernetes.io/ingress.provider: <INGRESS.PROVIDER>
      certmanager.k8s.io/issuer:  <CERTMANAGER.ISSUER>
    hosts:
      - <YOUR.MATTERMOST.DOMAIN>
    tls:
      - secretName: <NAME.OF.YOUR.TLS.SECRET>
        hosts:
          - <YOUR.MATTERMOST.DOMAIN>

  auth:
    gitlab:
      Enable: "true"
      Secret: "<GITLAB.APP.SECRET>"
      Id: "<GITLAB.APP.ID>"
      Scope: ""
      AuthEndpoint: "https://<YOUR.GITLAB.DOMAIN>/oauth/authorize"
      TokenEndpoint: "https://<YOUR.GITLAB.DOMAIN>/oauth/token"
      UserApiEndpoint: "https://<YOUR.GITLAB.DOMAIN>/api/v4/user"

  externalDB:
    enabled: true
    existingUser: <GITLAB.POSTGRES.USERNAME>
    existingSecret: "<GITLAB.POSTGRES.PASSWD.SECRET>"

  mysql:
    enabled: false

  ## Additional env vars
  extraEnvVars:
    - name: POSTGRES_PASSWORD_GITLAB
      valueFrom:
        secretKeyRef:
          name: <GITLAB.POSTGRES.PASSWD.SECRET>
          key: postgres-password
    - name: POSTGRES_USER_GITLAB
      value: <GITLAB.POSTGRES.USERNAME>
    - name: POSTGRES_HOST_GITLAB
      value: <GITLAB.POSTGRES.HOST>
    - name: POSTGRES_PORT_GITLAB
      value: "<GITLAB.POSTGRES.PORT>"
    - name: POSTGRES_DB_NAME_MATTERMOST
      value: <MATTERMOST.DATABASE.NAME>
    - name: MM_SQLSETTINGS_DRIVERNAME
      value: "postgres"
    - name: MM_SQLSETTINGS_DATASOURCE
      value: postgres://$(POSTGRES_USER_GITLAB):$(POSTGRES_PASSWORD_GITLAB)@$(POSTGRES_HOST_GITLAB):$(POSTGRES_PORT_GITLAB)/$(POSTGRES_DB_NAME_MATTERMOST)?sslmode=disable&connect_timeout=10
    - name: MINIO_ENDPOINT
      value: <GITLAB.MINIO.HOST>
    - name: MINIO_PORT
      value: "<GITLAB.MINIO.PORT>"
    - name: MM_FILESETTINGS_DRIVERNAME
      value: amazons3
    - name: MM_FILESETTINGS_AMAZONS3ENDPOINT
      value: $(MINIO_ENDPOINT):$(MINIO_PORT)
    - name: MM_FILESETTINGS_AMAZONS3ACCESSKEYID
      valueFrom:
        secretKeyRef:
          name: <GITLAB.MINIO.SECRET>
          key: accesskey
    - name: MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY
      valueFrom:
        secretKeyRef:
          name: <GITLAB.MINIO.SECRET>
          key: secretkey
    - name: MM_FILESETTINGS_AMAZONS3BUCKET
      value: <MATTERMOST.MINIO.BUCKET.NAME>


  ## Additional init containers
  extraInitContainers: |
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
          value: <GITLAB.POSTGRES.USERNAME>
        - name: POSTGRES_HOST_GITLAB
          value:<GITLAB.POSTGRES.HOST>
        - name: POSTGRES_PORT_GITLAB
          value: "<GITLAB.POSTGRES.PORT>"
        - name: POSTGRES_DB_NAME_MATTERMOST
          value: <MATTERMOST.DATABASE.NAME>
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
          value: <GITLAB.MINIO.HOST>
        - name: MINIO_PORT
          value: "<GITLAB.MINIO.PORT>"
        - name: MINIO_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: <GITLAB.MINIO.SECRET>
              key: accesskey
        - name: MINIO_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: <GITLAB.MINIO.SECRET>
              key: secretkey
        - name: MATTERMOST_BUCKET_NAME
          value: <MATTERMOST.MINIO.BUCKET.NAME>
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

Values that you need to replace in the above ``values.yaml`` file:

- **<YOUR.MATTERMOST.DOMAIN>**: URL that users will use to access Mattermost, matching the `Site URL field <https://docs.mattermost.com/administration/config-settings.html#site-url>`_, e.g. ``mattermost.gitlab.example.com``.
- **<NAME.OF.YOUR.TLS.SECRET>**: A name to store the TLS certificate for you domains, e.g. ``mattermost-tls``.
- **<INGRESS.CLASS>**: The ingress class. In a basic GitLab deployment, this is ``gitlab-nginx``.
- **<INGRESS.PROVIDER>**: The ingress provider. In a basic GitLab deployment, this is ``nginx``.
- **<CERTMANAGER.ISSUER>**: The cert manager issuer. In a basic GitLab deployment, this is ``gitlab-issuer``.
- **<GITLAB.APP.SECRET>**: The Application secret, which you created in step `Create the OAUTH with GitLab`_.
- **<GITLAB.APP.ID>**: The Application ID, which you created in step `Create the OAUTH with GitLab`_.
- **<YOUR.GITLAB.DOMAIN>**: The GitLab domain name, e.g. ``gitlab.example.com``.
- **<GITLAB.POSTGRES.USERNAME>**: The GitLab PostgreSQL username. Default is ``gitlab``.
- **<GITLAB.POSTGRES.PASSWD.SECRET>**: Secret that holds your PostgreSQL password. Default is ``gitlab-postgresql-password``.
- **<GITLAB.POSTGRES.HOST>**: Postgres host of your Kubernetes service. Default is ``gitlab-postgresql``.
- **<GITLAB.POSTGRES.PORT>**: Postgres port of your Kubernetes service. Default is ``5432``.
- **<MATTERMOST.DATABASE.NAME>**: Mattermost database, e.g. ``mattermost-db``.
- **<GITLAB.MINIO.HOST>**: Minio host of your Kubernetes service. Default is ``gitlab-minio-svc``.
- **<GITLAB.MINIO.PORT>**: Minio port of your Kubernetes service. Default is ``9000``.
- **<GITLAB.MINIO.SECRET>**: Secret that holds your Minio keys. Default is ``gitlab-minio-secret``.
- **<MATTERMOST.MINIO.BUCKET.NAME>**: Mattermost Minio bucket name, e.g. ``mattermost-data``.

After these changes, deploy the Mattermost Team Edition Helm Chart with following command:

.. code-block:: bash

  $ helm upgrade --install --name mattermost -f values.yaml stable/mattermost-team-edition

Wait for the pods to run. Then access your Mattermost server, and log in with your GitLab credentials.

Troubleshooting
---------------------

If you have any trouble installing Mattermost Team Edition in GitLab Helm Chart deployment, let us know in our `Troubleshooting forum <http://www.mattermost.org/troubleshoot/>`_ and we'll be happy to help.
