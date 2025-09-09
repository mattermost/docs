Deploy Mattermost in Air-Gapped Environments
==============================================

An air-gapped environment is one that is isolated from the public internet, requiring all necessary components to be available locally. This guide outlines what you'll need to deploy Mattermost in a self-hosted air-gapped environment, focusing on appropriate preparation, deployment guidance and configurations required for a successful deployment. 

Prerequisites
-------------

Before disconnecting from the internet, you must gather all required packages, container images, and dependencies needed during the installation process. The resources you'll need will depend on the deployment method you are using, specifically:


.. tab:: Linux

  Recommeded as the simplest installation method for air-gapped environments. You can install the Mattermost Server in a few minutes on any air-gapped 64-bit Linux system using the tarball.

   **Bill of Materials**

   - `Mattermost tarball <https://docs.mattermost.com/product-overview/version-archive.html>`_ (We recommend using the latest `ESR <https://docs.mattermost.com/product-overview/release-policy.html#extended-support-releases>`_ for extended support where server upgrades may be infrequent)
   - Database: PostgreSQL `installation packages <https://www.postgresql.org/download/>`_ or container images for your Linux distribution
   - File Storage: 
   - Load balancer: If you already have a load balancer you can skip this, otherwise you'll need 


.. tab:: Kubernetes

   Recommended if your organization already uses Kubernetes 

   **Bill of Materials**

   - Mattermost `Helm charts <https://helm.mattermost.com>`_ and `operator values <https://github.com/mattermost/mattermost-helm/blob/master/charts/mattermost-operator/values.yaml>`_ 
   - Database: We recommend the `Postgres Operator <https://github.com/CrunchyData/postgres-operator/>`_ from Crunchy Data for air-gapped Kubernetes deployments. 
   - File Storage: 
   - Private container registry: If you don't have a Docker container registry we recommend following the instructions `here <https://www.digitalocean.com/community/developer-center/how-to-set-up-digitalocean-container-registry>`_.


.. tab:: Docker

   **Bill of Materials**
   - Private container registry: If you don't have a Docker container registry we recommend following the instructions `here <https://www.digitalocean.com/community/developer-center/how-to-set-up-digitalocean-container-registry>`_. 


Optional supporting services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider gathering additional resources if you plan to enable these optional components:

- Mattermost Calls: For self-hosted audio and screensharing capabilities
- LDAP/SAML: For authentication and SSO
- `Elasticsearch <https://www.elastic.co/downloads/elasticsearch>`_: For enhanced search performance at scale
- `Prometheus <https://prometheus.io/download/>`_: For monitoring and observability

Mattermost plugins
~~~~~~~~~~~~~~~~~~
Mattermost includes a number of `pre-built integrations <https://docs.mattermost.com/integrations-guide/integrations-guide-index.html#plugins>`_ for mission-critical tools. If you'd like to use any plugins beyond those that are pre-built in the Mattermost package you'll need to download the plugin binaries from the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_ before going offline.   


Documentation
~~~~~~~~~~~~~
Ensure you have local copies of the Mattermost install documenation appropraite for your deployment method. You can access a PDF of our deployment guide here (XXXXXX).  


Server Deployment
-----------------

Now that you have all the necessary resources, you can go offline and follow the deployment instructions for `Linux <https://docs.mattermost.com/deployment-guide/server/deploy-linux.html>`_, `Kubernetes <https://docs.mattermost.com/deployment-guide/server/deploy-kubernetes.html>`_, or `Docker <https://docs.mattermost.com/deployment-guide/server/deploy-containers.html>`_.


Server Configuration
--------------------

After successful deployment, you'll need to configure Mattermost for air-gapped operation. The following covers these configuration options and offers recommendations for settings. 


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
`In-product notices <https://docs.mattermost.com/administration-guide/manage/in-product-notices.html>`_ require internet access to periodcally inform administrators and end users of new product improvements, features, and releases. You can disable notices in **System Console > Site Configuration > Notices**.

Telemetry
~~~~~~~~~
To avoid log errors we recommend disabling `Telemetry related features <https://docs.mattermost.com/administration-guide/manage/telemetry.html#telemetry>`_, including the security update check, and error and diagnostics reporting features.





