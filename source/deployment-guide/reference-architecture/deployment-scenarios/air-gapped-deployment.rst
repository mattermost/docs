Deploy in Air-Gapped Environments
=================================

An air-gapped environment is one that is isolated from the public internet, requiring all necessary components to be available locally. This guide outlines what you'll need to deploy Mattermost in a self-hosted air-gapped environment, focusing on appropriate preparation, deployment guidance and configurations required for a successful deployment.

Overview
--------

At a high level, deploying Mattermost in an air-gapped environment requires preparing all necessary software, container images, and configuration resources in advance, since the target system has no direct internet access; transferring these artifacts to the isolated network using secure media; and then installing, configuring, and validating the deployment within the air-gapped environment. This is a summary of the steps involved:

1. **Select your preferred Mattermost deployment option:**

This step is often dictated by the infrastruture already running in your air-gapped environment. If you're deploying from scratch, we recommend reviewing our :ref:`server deployment documentation <deployment-guide/server/server-deployment-planning:deployment options>` to select the optimal option given your organizations needs.

2. **Setup a private container registry or package mirror:**

Ideally the air-gapped environment already has a private container registry or package mirror available. If not, we recommend following `our frequently asked questions <#frequently-asked-questions>`__ or referencing online resources specific to your environment.

3. **Prepare your Bill of Materials:**

Depending on your deployment method method, you'll need to download, tag, and push required materials into your private registry or mirror.

4. **Transfer materials into the air-gapped environment:**

If the private registry cannot access the public internet, you can prepare an archive of the registry data on your internet connected machine and securely transfer it using approved data transfer methods - for example, burning to a disk.

5. **Install Mattermost Server**

Once you have all the necessary resources in your air-gapped environment, you can move forward with deployment following the instructions for :doc:`Linux </deployment-guide/server/deploy-linux>`, :doc:`Kubernetes </deployment-guide/server/deploy-kubernetes>`, or :doc:`Docker </deployment-guide/server/deploy-containers>`.

6. **Install Mattermost Desktop Apps**

Since air-gapped devices cannot access the publicly available app stores, you'll need to install the apps directly from the latest `packages available on our GitHub release page <https://github.com/mattermost/desktop/releases>`_. You'll find :doc:`installation instructions </deployment-guide/desktop/desktop-app-deployment>` in our documentation based on your desired deployment method.

6. **Configure Mattermost for air-gapped operation**

The `configuration settings <#server-configuration>`__ recommended in this document accomodate for the lack of internet access to operate Mattermost in an air-gapped environment.


.. note::
  Consider `talking to a Mattermost expert <https://mattermost.com/contact-sales/>`__ if your organization needs support deploying Mattermost and supporting services in an air-gapped environment.

Bill of Materials
-----------------

On an internet connected machine, you must gather all required packages, container images, and dependencies needed for the installation process. The resources you'll need will depend on your deployment method, specifically:

.. tab:: Linux

  Using our provided tarball is recommeded as the simplest installation method for air-gapped environments. You can install the Mattermost Server in a few minutes on any air-gapped 64-bit Linux system.

    **Prerequisites**

    - :doc:`Mattermost tarball </product-overview/version-archive>`. We recommend using the latest :ref:`ESR <product-overview/release-policy:extended support releases>` for extended support where server upgrades may be infrequent.
    - Database: PostgreSQL `installation packages <https://www.postgresql.org/download/>`_ or container images for your Linux distribution
    - File Storage: Local filesystem storage is sufficient for deployments under 2,000 users. For larger deployments requiring high availability, we recommend using an S3-compatible object storage solution or an NFS (Network File System) server for shared storage needs.
    - Load balancer: If you already have a load balancer running in your air-gapped environment you can skip this resource, otherwise we recommend deploying :doc:`NGINX </deployment-guide/server/setup-nginx-proxy>` from these `Linux packages <https://nginx.org/en/linux_packages.html>`_.
    - Desktop app: Download the `required package <https://github.com/mattermost/desktop/releases>`_ based on your deployment method.

    **(Optional) Supporting Services**
    Consider downloading these additional resources if you plan to enable these optional components:

    - :doc:`Mattermost Calls </administration-guide/configure/calls-deployment>`: `mattermost-calls-offloader <https://github.com/mattermost/calls-offloader/releases>`__ (required for recording, transcription and live captions) and `mattermost-rtcd <https://github.com/mattermost/rtcd/releases>`__ (required for performance and scalability).
    - `Elasticsearch <https://www.elastic.co/downloads/elasticsearch>`__ can be `deployed <https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch>`__ for enhanced search performance at scale.
    - `Prometheus <https://prometheus.io/download/>`_ and `Grafana <https://grafana.com/grafana/download>`__ for monitoring and observability

.. tab:: Kubernetes

   Kubernetes is recommended for a highly scalable and robust deployment if your organization is already running a Kubernetes cluster in the air-gapped environment.

    **Prerequisites**

    -  `Mattermost Operator <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-operator>`_ and `values <https://github.com/mattermost/mattermost-helm/blob/master/charts/mattermost-operator/values.yaml>`__
    - Database: We recommend options such as the `Postgres Operator <https://access.crunchydata.com/documentation/postgres-operator/latest/quickstart>`_ from Crunchy Data, `CloudNativePG <https://cloudnative-pg.io/documentation/1.27/installation_upgrade/>`__ or `pgEdge <https://github.com/pgEdge/pgedge-helm>`__.
    - File Storage: We recommend using an S3-compatible storage service or a mounted NFS volume for shared storage needs.
    - Load balancer: If you already have a load balancer running in your air-gapped environment you can skip this resource, otherwise we recommend deploying :doc:`NGINX </deployment-guide/server/setup-nginx-proxy>`, using the `NGINX Ingress Controller operator <https://docs.nginx.com/nginx-ingress-controller/installation/installing-nic/installation-with-operator/>`__.
    - Desktop app: Download the `required package <https://github.com/mattermost/desktop/releases>`_ based on your deployment method.

    **(Optional) Supporting Services**
    Consider downloading these additional resources if you plan to enable these optional components:

    - :doc:`Mattermost Calls </administration-guide/configure/calls-deployment>` helm charts: `mattermost-calls-offloader <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-calls-offloader>`__ and `values <https://github.com/mattermost/mattermost-helm/blob/master/charts/mattermost-calls-offloader/values.yaml>`__ (required for recording, transcription and live captions), `mattermost-rtcd <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-rtcd>`__ and `values <https://github.com/mattermost/mattermost-helm/blob/master/charts/mattermost-rtcd/values.yaml>`__ (required for performance and scalability).
    - `Elasticsearch <https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s>`__ can be `deployed in air-gapped k8 environments <https://www.elastic.co/guide/en/cloud-on-k8s/2.8/k8s-air-gapped.html>`__ for enhanced search performance at scale.
    - `Prometheus <https://github.com/prometheus-operator/prometheus-operator>`__ and `Grafana <https://github.com/grafana/grafana-operator>`__ operators for monitoring and observability

.. tab:: Docker

   Docker can be used if you don't have a running Kubernetes cluster in the air-gapped environment, but want to use containers for simplified installation and dependency management. Docker is not recommended for production environments at high scale, as it doesn’t support clustered deployments or High Availability (HA) configurations out-of-the-box.

    **Prerequisites**

    - `Mattermost Enterprise Edition <https://hub.docker.com/r/mattermost/mattermost-enterprise-edition>`__ image.
    - Database: `PostgreSQL <https://hub.docker.com/_/postgres>`__ image.
    - Load balancer: If you already have a load balancer running in your air-gapped environment you can skip this resource, otherwise we recommend deploying :doc:`NGINX </deployment-guide/server/setup-nginx-proxy>` from this `images <https://hub.docker.com/_/nginx>`__.
    - Desktop app: Download the `required package <https://github.com/mattermost/desktop/releases>`_ based on your deployment method.

    **(Optional) Supporting Services**
    Consider downloading these additional resources if you plan to enable these optional components:

    - :doc:`Mattermost Calls </administration-guide/configure/calls-deployment>` images: `calls-offloader <https://hub.docker.com/r/mattermost/calls-offloader>`__ (required for recording, transcription and live captions) and `rtcd <https://hub.docker.com/r/mattermost/rtcd>`__ (required for performance and scalability).
    - `Elasticsearch <https://hub.docker.com/_/elasticsearch>`__ image for enhanced search performance at scale.
    - `Prometheus <https://hub.docker.com/r/prom/prometheus>`__ and `Grafana <https://hub.docker.com/r/grafana/grafana>`__ images for monitoring and observability.

Mattermost Plugins
~~~~~~~~~~~~~~~~~~

Mattermost includes a number of :doc:`pre-built integrations </integrations-guide/popular-integrations>` for mission-critical tools. If you'd like to use any plugins beyond those that are pre-built in the Mattermost package you'll need to download the plugin binaries from the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_. Once you have Mattermost deployed, these plugin binaries can be uploaded directly in the System Console.

SSL/TLS Certificates and Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your deployment requires SSL, ensure you have the necessary certificates. This includes certificates and keys for enabling HTTPS with Mattermost, as well as any CA files or certificates needed to access internal services such as LDAP or SAML.

Local Documentation
~~~~~~~~~~~~~~~~~~~

Mattermost documenation can be `built locally <https://github.com/mattermost/docs?tab=readme-ov-file#build-locally>`__ so you'll have access to installation and configuration documentation in the air-gapped environment. Otherwise, you can download the necessary deployment and configuration documents directly from the `GitHub docs repository <https://github.com/mattermost/docs>`__.

**Prerequisites**
The following software is required to build the documentation locally:

- Git `[download] <https://git-scm.com/downloads>`__
- Python 3.11 or later `[download] <https://www.python.org/downloads>`__
- Pipenv `[download] <https://pipenv.pypa.io>`__
- GNU Make 3.82 or later `[download] <https://ftp.gnu.org/gnu/make/>`__

Server configuration
--------------------

After successful deployment, you'll need to configure Mattermost for air-gapped operation. The following sections describe these configuration options and offers recommendations for settings.

Mobile push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost can use mobile push notifications to notify users of new messages and activity. These notifications require a server component to be deployed to send the notifications to the mobile devices. By default, Mattermost will use the public push notification service which is not available in an air-gapped environment. We recommend :ref:`disabling push notifications <administration-guide/configure/environment-configuration-settings:enable push notifications>` in **System Console > Environment > Push Notification Server**.

Email
~~~~~

Unless you have setup an internal air-gapped email service, we recommend disabling email invitations and email verification from **System Console > Authentication > Signup**.

Website link previews
~~~~~~~~~~~~~~~~~~~~~~~

Website link previews require a connection to the internet to fetch the content of the links. We recommend :ref:`disabling website link previews <administration-guide/configure/site-configuration-settings:enable website link previews>` in **System Console > Site Configuration > Posts**.

GIF picker
~~~~~~~~~~

The GIF picker relies on a third-party service which has a dependency on external internet access. You can disable it in **System Console > Integrations > GIF**.

Notices
~~~~~~~

:doc:`In-product notices </administration-guide/manage/in-product-notices>` require internet access to periodcally inform administrators and end users of new product improvements, features, and releases. You can disable notices in **System Console > Site Configuration > Notices**.

Telemetry
~~~~~~~~~

To avoid log errors we recommend disabling :doc:`Telemetry-related features </administration-guide/manage/telemetry>`, including the security update check, and error and diagnostics reporting features.

Frequently Asked Questions
--------------------------

What if my air-gapped environment doesn't have a private container registry or package mirror?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A private container registry securely stores the Docker images necessary for air-gapped deployments, ensuring compliance with data isolation requirements. Similarly, a private package mirror stores operating system packages necessary for air-gapped deployments in Ubuntu or RHEL/CentOS Linux environments. Setting up a local registry or mirror is a critical step in deploying Mattermost to ensure all images, dependencies and packages are available to you in the air-gapped environment. The steps below outline the process required to setup a local registry or mirror, depending on the deployment method you are using. These steps are a rough guide, and can be supplemented with online resources depending on your specific deployment needs.


.. tab:: Linux

   **(Ubuntu) Set up a private Debian package mirror**

   We will use Aptly to create a local mirror, although you can also use other options such as debmirror.

   1. **Install Aptly** (on an internet-connected machine):

      .. code-block:: bash

         apt-get update
         apt-get install aptly gnupg

   2. **Create GPG key for signing packages**:

      .. code-block:: bash

         gpg --gen-key

   3. **Create a mirror configuration**:

      .. code-block:: bash

         aptly mirror create -architectures=amd64 debian-bullseye http://deb.debian.org/debian bullseye main contrib non-free

   4. **Update the mirror to download packages**:

      .. code-block:: bash

         aptly mirror update debian-bullseye

   5. **Create and publish a snapshot**:

      .. code-block:: bash

         aptly snapshot create debian-bullseye-$(date +%Y%m%d) from mirror debian-bullseye
         aptly publish snapshot debian-bullseye-$(date +%Y%m%d)

   6. **Serve the repository**:

      .. code-block:: bash

         aptly serve

   7. **Client configuration:** Configure apt to use your local mirror:

      .. code-block:: bash

         cat > /etc/apt/sources.list << EOF
         deb http://mirror.example.com/debian bullseye main contrib non-free
         EOF


   **(RHEL/CentOS) Set up a private RHEL package mirror**

   We will use reprosync for a local mirror.

   1. **Install required tools** (on an internet-connected RHEL system):

      .. code-block:: bash

         yum install yum-utils createrepo

   2. **Download packages**:

      .. code-block:: bash

         mkdir -p /var/www/html/repos/rhel8
         reposync -p /var/www/html/repos/rhel8 --download-metadata --repo=rhel-8-for-x86_64-baseos-rpms
         reposync -p /var/www/html/repos/rhel8 --download-metadata --repo=rhel-8-for-x86_64-appstream-rpms

   3. **Create repository metadata**:

      .. code-block:: bash

         createrepo /var/www/html/repos/rhel8/rhel-8-for-x86_64-baseos-rpms
         createrepo /var/www/html/repos/rhel8/rhel-8-for-x86_64-appstream-rpms

   4. **Set up a web server**:

      .. code-block:: bash

         yum install httpd
         systemctl enable httpd
         systemctl start httpd

   5. **Client configuration:** Disable existing repositories:

      .. code-block:: bash

         cd /etc/yum.repos.d/
         mkdir backup
         mv *.repo backup/

   6. **Client configuration:** Create new repository files:

      .. code-block:: bash

         cat > /etc/yum.repos.d/local-baseos.repo << EOF
         [local-baseos]
         name=Red Hat Enterprise Linux 8 BaseOS
         baseurl=http://mirror.example.com/repos/rhel8/rhel-8-for-x86_64-baseos-rpms
         enabled=1
         gpgcheck=0
         EOF

         cat > /etc/yum.repos.d/local-appstream.repo << EOF
         [local-appstream]
         name=Red Hat Enterprise Linux 8 AppStream
         baseurl=http://mirror.example.com/repos/rhel8/rhel-8-for-x86_64-appstream-rpms
         enabled=1
         gpgcheck=0
         EOF

   7. **Client configuration:** Clear cache and test:

      .. code-block:: bash

         yum clean all
         yum repolist


.. tab:: Kubernetes

   **Set up a self-hosted private container registry**

   1. **Install Docker Registry**:

      .. code-block:: bash

         docker run -d -p 5000:5000 --restart=always --name registry registry:2

   2. **Configure persistent storage**:

      .. code-block:: bash

         docker run -d -p 5000:5000 --restart=always --name registry \
         -v /mnt/registry:/var/lib/registry \
         registry:2

   3. **Add TLS security** (recommended):

      a. Generate self-signed certificates:

         .. code-block:: bash

            mkdir -p certs
            openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key \
            -x509 -days 365 -out certs/domain.crt

      b. Run the registry with TLS:

         .. code-block:: bash

            docker run -d -p 5000:5000 --restart=always --name registry \
            -v /mnt/registry:/var/lib/registry \
            -v $(pwd)/certs:/certs \
            -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
            -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
            registry:2


   **Configure Kubernetes to use private image registries**

   When using Kubernetes in an air-gapped environment, you need to configure it to use your private registry.

   1. **Create a kubernetes secret for registry authentication**:

      .. code-block:: bash

         kubectl create secret docker-registry regcred \
         --docker-server=registry.example.com:5000 \
         --docker-username=your_username \
         --docker-password=your_password \
         --docker-email=your_email@example.com

   2. **Reference the secret in pod specifications**:

      .. code-block:: yaml

         apiVersion: v1
         kind: Pod
         metadata:
           name: mattermost-pod
         spec:
           containers:
           - name: mattermost
             image: registry.example.com:5000/mattermost/mattermost-enterprise-edition:latest
           imagePullSecrets:
           - name: regcred

   3. **For Helm deployments**, specify the registry in ``values.yaml``:

      .. code-block:: yaml

         image:
           repository: registry.example.com:5000/mattermost/mattermost-enterprise-edition
           tag: latest
           pullPolicy: IfNotPresent

         imagePullSecrets:
           - name: regcred

.. tab:: Docker

   **Set up a self-hosted private container registry**

   1. **Install Docker Registry**:

      .. code-block:: bash

         docker run -d -p 5000:5000 --restart=always --name registry registry:2

   2. **Configure persistent storage**:

      .. code-block:: bash

         docker run -d -p 5000:5000 --restart=always --name registry \
         -v /mnt/registry:/var/lib/registry \
         registry:2

   3. **Add TLS security** (recommended):

      a. Generate self-signed certificates:

         .. code-block:: bash

            mkdir -p certs
            openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key \
            -x509 -days 365 -out certs/domain.crt

      b. Run the registry with TLS:

         .. code-block:: bash

            docker run -d -p 5000:5000 --restart=always --name registry \
            -v /mnt/registry:/var/lib/registry \
            -v $(pwd)/certs:/certs \
            -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
            -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
            registry:2


   **Populate your private registry**

   Ensure the required images from the `Bill of Materials <bill-of-materials>`__ are downloaded and pushed to the private registry.

   **Configure Docker to use private image registries**

   Configure Docker on all hosts to trust and use your private registry.

   1. **Add your registry to Docker's trusted registries**:

      Edit or create ``/etc/docker/daemon.json``:

      .. code-block:: json

         {
           "insecure-registries": ["registry.example.com:5000"]
         }

      For registries using self-signed certificates:

      .. code-block:: bash

         mkdir -p /etc/docker/certs.d/registry.example.com:5000
         cp domain.crt /etc/docker/certs.d/registry.example.com:5000/ca.crt

   2. **Restart Docker daemon**:

      .. code-block:: bash

         systemctl restart docker

   3. **Test the configuration**:

      .. code-block:: bash

         docker pull registry.example.com:5000/mattermost/mattermost-enterprise-edition:latest
