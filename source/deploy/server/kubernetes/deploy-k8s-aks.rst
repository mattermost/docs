.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

You can use a supported `Azure Marketplace Container Offer <https://azuremarketplace.microsoft.com/en-us/marketplace/apps/mattermost.mattermost-operator>`__ to install Mattermost on your existing Azure infrastructure.

**Before you begin**

Before deploying, make sure you have the following: 

- **An AKS cluster**: with the `Application Gateway Ingress Controller (AGIC) add-on <https://learn.microsoft.com/en-us/azure/application-gateway/tutorial-ingress-controller-add-on-new>`_ enabled or another Ingress controller deployed.  

- **PostgreSQL v13.0+ database**: `Azure Database for PostgreSQL - Flexible Server with Private Access <https://learn.microsoft.com/en-us/azure/postgresql/>`_ is recommended. Deploy one by following `this Microsoft quick start guide <https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal>`_. 

- **Private Network Connectivity**: Verify that there is network connectivity between your AKS cluster and the PostgreSQL database. 

- **Valid DNS name and TLS certificate**: You must have access to a DNS zone and provide a valid TLS key and certificate for the Ingress Controller. 

- **Node Capacity**: At least 2 AKS nodes for high availability when deploying for 100 users or more. 

- **License Key**: Trial or Enterprise license to test high availability and other Enterprise features. 

**Installation steps**

The installation process includes deploying Mattermost and updating the server.

**Step 1: Deploy Mattermost**

1. Deploy Mattermost from the `Azure Marketplace Container Offer <https://azuremarketplace.microsoft.com/en-us/marketplace/apps/mattermost.mattermost-operator>`_ and select **Get it now**. 

  - Alternatively, you can go to the ``Extensions + Applications`` section of your AKS cluster and install the Mattermost offering from there. Visit the `Microsoft cluster extensions documentation <https://learn.microsoft.com/en-gb/azure/aks/cluster-extensions?tabs=azure-cli>`_ to learn more.

2. Choose the **Resource Group** and the **Region** of your installed AKS and PostgreSQL database.

  .. image:: /_static/images/azure/basics.png
    :alt: An example of the Azure AKS Project details screen.

3. Choose your AKS cluster.

  .. image:: /_static/images/azure/aks-cluster.png
    :alt: An example of the Azure AKS cluster setup screen.

4. Fill in the details for your PostgreSQL database. Ensure the user specified has full access.

  .. image:: /_static/images/azure/postgreSQL.png
    :alt: An example of the Azure AKS Database setup screen.


5. Specify Deployment Details including Deployment Name and Deployment Size. Click the checkbox to Deploy Minio, a required utility for this installation that will provide filestore functionality for your Mattermost instance. 

  .. image:: /_static/images/azure/deployment-details.png
    :alt: An example of the Azure AKS Deployment Details setup screen.

6. Configure Mattermost installation hostname and Ingress details. The AGIC add-on is used in the following example to show the ingress annotations required.

  a. You can use any pre-installed Ingress Controller in your cluster as long as it supports Kubernetes Ingress and TLS termination.

    .. code-block:: yaml

      kubernetes.io/ingress.class: azure/application-gateway
      appgw.ingress.kubernetes.io/ssl-redirect: "true"
  
7. Additionally, we recommend considering:   

  a. Enforcing a minimum TLS version (e.g., TLS 1.2).  
  b. Deploying a Web Application Firewall (WAF) for additional protection, if supported by your ingress controller.  
  c. Limiting access using Kubernetes Network Policies. 

  .. image:: /_static/images/azure/networking-details.png
    :alt: An example of the Azure AKS Networking Details setup screen.

8. Ensure that everything is running. You should be able to check the installed plugin from the **AKS Extensions + Applications** page under the **Settings** menu.

  a. When the deployment is complete, obtain the hostname or IP address of your Mattermost deployment using the following command:

    .. code-block:: sh

      kubectl -n mattermost-operator get ingress

9. Use your IP address from the ``ADDRESS`` column, and create a DNS record in your domain registration service. 

10. Access your working Mattermost installation at the URL you’ve determined in your DNS record.

Learn more about administrating your Mattermost server by visiting the :doc:`Administration Guide </guides/administration-guide>`.

**Step 2: Upgrade Mattermost via your AKS cluster**

1. Visit the ``Extensions + Applications`` section of your AKS cluster where your Mattermost installation is deployed.
2. You can enable minor version auto upgrades since these are not updating Mattermost version
3. Expand the ``Configuration Settings`` table and add the below configuration and the version you want to install as a value.

  .. code:: 

    global.azure.mattermost.version

   .. image:: /_static/images/global-azure-mattermost-version.png
    :alt: An example of using custom Mattermost version.

4. Select **Save** and wait for the upgrade.

.. important::

  You are responsible for Azure costs associated with any infrastructure you spin up to host a Mattermost server, and Azure credits cannot be applied towards the purchase of a Mattermost license.