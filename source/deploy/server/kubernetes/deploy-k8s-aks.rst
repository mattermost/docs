.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

You can use a supported `Azure Marketplace Container Offer <https://azuremarketplace.microsoft.com/en-us/marketplace/apps/mattermost.mattermost-operator>`__ to install Mattermost on your existing Azure infrastructure.

.. important::

  You are responsible for Azure costs associated with any infrastructure you spin up to host a Mattermost server, and Azure credits cannot be applied towards the purchase of a Mattermost license.

Infrastructure pre-requisites
-----------------------------

Deploying Mattermost on Azure AKS requires the following database and cluster prerequisites.

PostgreSQL v13.0+ database
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost requires a pre-existing PostgreSQL database within your infrastructure. We recommend using `Azure Database for PostgreSQL - Flexible Server <https://learn.microsoft.com/en-us/azure/postgresql/>`_. Deploy one by following `this Microsoft quick start guide <https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal>`_.

.. tip::
  We recommend using Private Access for your database.

Running AKS cluster
~~~~~~~~~~~~~~~~~~~

Mattermost Azure Container Offer requires a pre-existing Kubernetes Cluster with an Ingress Controller pre-installed. We recommend creating a new AKS cluster with the `AGIC add-on enabled <https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-overview>`_. 

Follow `this tutorial <https://learn.microsoft.com/en-us/azure/application-gateway/tutorial-ingress-controller-add-on-new>`_ to create a new AKS cluster with the add-on enabled.

.. tip::

  - Connectivity should be already in place between the AKS cluster and the PostgreSQL database.
  - Any pre-installed Ingress Controller within the cluster that supports the Ingress Kubernetes resource and TLS termination should work out of the box.

Deployment pre-requisites
-------------------------

Deploying Mattermost on Azure AKS requires the following deployment prerequisites.

Valid DNS name and TLS certificates 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost relies on strong TLS certification in order to provide all the features to users. You need to have access to a DNS zone and be able to provide a valid TLS key and certificate for the Ingress Controller.

Mattermost License and AKS Capacity  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

If your deployment option is for more than ``100 users``, you must have more than 2 nodes on your AKS cluster to support High Availability, and you must provide a valid Mattermost License file.

.. note:: 
  
  Providing a license is optional at this stage. You can enable a **30 day** Mattermost trial once the server is deployed.

Deploy Mattermost
-----------------
  
1. Navigate to our `Azure Marketplace Container Offer <https://azuremarketplace.microsoft.com/en-us/marketplace/apps/mattermost.mattermost-operator>`_ and get the offer.

  Alternatively, you can go to the ``Extensions + Applications`` section of your AKS cluster and install the Mattermost offering from there. Visit the `Microsoft cluster extensions documentation <https://learn.microsoft.com/en-gb/azure/aks/cluster-extensions?tabs=azure-cli>`_ to learn more.

2. Choose the **Resource Group** and the **Region** of your installed AKS and PostgreSQL database.
  
    .. image:: ../../_static/images/azure/basics.png
      :alt: An example of the Azure AKS Project details screen.

3. Choose your AKS cluster.

    .. image:: ../../_static/images/azure/aks-cluster.png
      :alt: An example of the Azure AKS cluster setup screen.

4. Fill in the details for your PostgreSQL database.

    .. image:: ../../_static/images/azure/postgreSQL.png
      :alt: An example of the Azure AKS Database setup screen.

    .. note::

      - Connectivity should be already in place between the AKS cluster and the database.
      - Database should already exist and the user specified must have full access.

5. Adjust deployment details.

    .. image:: ../../_static/images/azure/deployment-details.png
      :alt: An example of the Azure AKS Deployment Details setup screen.

.. note:: 
  You can define a Deployment size to automatically adjust the installation. A valid Mattermost license is required for deployments of more than 100 users.

6. Configure Mattermost installation hostname and Ingress details. The AGIC add-on is used in the following example to show the ingress annotations required.

    .. code-block:: yaml

      kubernetes.io/ingress.class: azure/application-gateway
      appgw.ingress.kubernetes.io/ssl-redirect: "true"
  
Upload yor own TLS certificates at this stage to take advantage of all Mattermost features.

    .. image:: ../../_static/images/azure/networking-details.png
      :alt: An example of the Azure AKS Networking Details setup screen.

7. Ensure that everything is running. You should be able to check the installed plugin from the **AKS Extensions + Applications** page under the **Settings** menu.

  a. When the deployment is complete, obtain the hostname or IP address of your Mattermost deployment using the following command:

    .. code-block:: sh

      kubectl -n mattermost-operator get ingress

  b. Get the resulting IP address from the ``ADDRESS`` column, and use your domain registration service to create a DNS record.
  c. You should be good to go.

Learn more about managing your Mattermost server by visiting the :doc:`Managing Mattermost </guides/self-hosted-administration>` documentation.

Upgrade Mattermost
-------------------

1. Visit the ``Extensions + Applications`` section of your AKS cluster where your Mattermost installation is deployed.
2. You can enable minor version auto upgrades since these are not updating Mattermost version
3. Expand the ``Configurarion Settings`` table and add the below configuration and the version you want to install as a value.

    .. code:: 

      global.azure.mattermost.version

   .. image:: ../../images/global-azure-mattermost-version.png
    :alt: An example of using custom Mattermost version.
4. Click ``Save`` and wait for the upgrade. 