..  _install-mmte-helm-gitlab-helm:

How to deploy Mattermost Team Edition Helm Chart in the GitLab Helm Chart deployment
=====================================================================================

This document will describe in how to deploy MM TE Helm Chart in an existing GitLab Helm Chart deployment.

You will need:
  - A running Kubernetes cluster :)
  - A running GitLab Helm Chart
  - The name of the secret that holds the Postgres password. If you installed the Gilab Helm  Chart using the chart name as ``gitlab`` then the secret name will be ``gitlab-postgresql-password``
  - The name of the secret that holds the Minio keys. If you installed the Gilab Helm  Chart using the chart name as ``gitlab`` then the secret name will be ``gitlab-minio-secret``
  - The service name for Postgres and the port. If you installed the Gilab Helm  Chart using the chart name as ``gitlab`` and in the ``default`` namespace then the service name will be ``gitlab-postgresql`` and port ``5432``
  - The service name for Minio and the port.  If you installed the Gilab Helm  Chart using the chart name as ``gitlab`` and in the ``default`` namespace then the service name will be ``gitlab-minio-svc`` and port ``9000``
  - The names of ``kubernetes.io/ingress.class``, ``kubernetes.io/ingress.provider`` and ``certmanager.k8s.io/issuer``


**Deploy GitLab Helm Chart**
----------------------------

To deploy you can follow the instructions described `here <https://docs.gitlab.com/ee/install/kubernetes/gitlab_chart.html>`_.

A light way to install is:

.. code-block:: bash

  $ helm upgrade --install gitlab gitlab/gitlab \
    --timeout 600 \
    --set global.hosts.domain=<YOUR.DOMAIN> \
    --set global.hosts.externalIP=<EXTERNAL.IP> \
    --set certmanager-issuer.email=<EMAIL>

- **<YOUR.DOMAIN>**: Domain that you want to have GitLab, eg. gitlab.example.com
- **<EXTERNAL.IP>**: the external ip pointing to your k8s cluster
- **<EMAIL>**: email to register in the lets encrypt to get the TLS certificates

After all pods get in the running state you can login in your GitLab.

**Create the OAUTH with GitLab**
--------------------------------

To create the OAUTH to set Mattermost to use Gitlab auth please follow the instructions `here <https://docs.mattermost.com/administration/config-settings.html?highlight=gitlab#gitlab>`_.

Please take note on the ``Application ID``, ``Application Secret Key``, ``User API Endpoint``, ``Auth Endpoint``, ``Token Endpoint`` we will use those values later when deploying Mattermost.


**Deploy Mattermost Team Edition Helm Chart**
---------------------------------------------

Requirements:
  - Mattermost Team Edition Helm Chart Version => 1.4.0

To deploy Mattermost together with GitLab Helm Chart you will need to set some values in the ``values.yaml`` for the InitContainer and Environment Variables and also disable the ``MySql`` chart.
Below you can see the modified ``values.yaml``:

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


Values that you need to replace in the ``values.yaml``:

- **<YOUR.MATTERMOST.DOMAIN>**: Your desired Mattermost domain. eg, ``mattermost.gitlab.example.com``
- **<NAME.OF.YOUR.TLS.SECRET>**: A name to store the TLS certificate for you domains, eg. ``mattermost-tls``
- **<INGRESS.CLASS>**: the ingress class, in a basic deployment of GitLab will be ``gitlab-nginx``
- **<INGRESS.PROVIDER>**: the ingress provider, in a basic deployment of GitLab will be ``nginx``
- **<CERTMANAGER.ISSUER>**: the cert manager issuer, in a basic deployment of GitLab will be ``gitlab-issuer``
- **<GITLAB.APP.SECRET>**: The Application secret. The value you created in the step `Create the OAUTH with GitLab`_
- **<GITLAB.APP.ID>**: The Application secret. The value you created in the step `Create the OAUTH with GitLab`_
- **<YOUR.GITLAB.DOMAIN>**: The GitLab domain name. eg. ``gitlab.example.com``
- **<GITLAB.POSTGRES.USERNAME>**: The GitLab Postgres username. Default ``gitlab``
- **<GITLAB.POSTGRES.PASSWD.SECRET>**: Secret that holds the Postgres password. Default ``gitlab-postgresql-password``
- **<GITLAB.POSTGRES.HOST>**: Postgres host. Check the Kubernetes service. Default ``gitlab-postgresql``
- **<GITLAB.POSTGRES.PORT>**: Postgres port. Check the Kubernetes service. Default ``5432``
- **<MATTERMOST.DATABASE.NAME>**: Mattermost database name that you choose, eg. ``mattermost-db``
- **<GITLAB.MINIO.HOST>**: Minio host. Check the Kubernetes service. Default ``gitlab-minio-svc``
- **<GITLAB.MINIO.PORT>**: Minio port. Check the Kubernetes service. Default ``9000``
- **<GITLAB.MINIO.SECRET>**: Secret that holds the Minio keys. Default ``gitlab-minio-secret``
- **<MATTERMOST.MINIO.BUCKET.NAME>**: Mattermost Minio bucket, eg. ``mattermost-data``

After the changes you can deploy the Mattermost Team Edition Helm Chart running the following command:

.. code-block:: bash

  $ helm upgrade --install --name mattermost -f values.yaml stable/mattermost-team-edition

Wait for the pods get in a running state and after that you can try to access the Mattermost instance and login with the user you have in the GitLab.

Happy Mattermosting and GitLab :)
