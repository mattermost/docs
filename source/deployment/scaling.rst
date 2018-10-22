
Scaling for Enterprise 
======================

Mattermost is designed to scale from small teams hosted on a single server to large enterprises running in cluster-based, highly available deployment configurations. 

Server requirements vary based on usage and it is highly recommended that pilots are run before enterprise-wide deployments in order to estimate full scale usage based on your specific organizational needs. 

Single Machine Deployment 
^^^^^^^^^^^^^^^^^^^^^^^^^

Organizations can typically run Mattermost on a single server with up to 2,000 users, though more users have been observed based on different usage and server configurations.

- See `install guides for step-by-step configuration instructions for single machine setup <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`_.
- See `hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html>`_.

Multi Machine Deployment 
^^^^^^^^^^^^^^^^^^^^^^^^

Deployments between 2,000 and 10,000 registered users with moderate usage can run on a standard three-machine Mattermost deployment with a proxy, an application server and a database server. At this scale, demands of larger organizations can typically be met by using powerful hardware in a standard configuration. 

- See `install guides for step-by-step configuration instructions for multi-machine setup. <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`_
- See `hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html>`_.

Cluster Based Deployment 
^^^^^^^^^^^^^^^^^^^^^^^^

*Available in Enterprise Edition E20*

Deployments over 10,000 registered users with moderate usage can be supported by adding additional servers in cluster-based, high availability configuration. To date, the largest simulation included `70,000 concurrent users on a single Mattermost instance <https://mattermost.com/blog/performance-scale-mattermost/>`_.

This configuration uses a load balancer to distribute requests from users across multiple Mattermost application servers, allowing the system to scale beyond the limits of any single server. 

For more information, see `high availability deployment guide for horizontal scaling setup <https://docs.mattermost.com/deployment/cluster.html>`_.

Sample Scaling Guide 
^^^^^^^^^^^^^^^^^^^^^^^^

This guide demonstrates how to budget for and build large-scale Mattermost deployments.

Mattermost can be deployed on-premises or on the cloud platform of your choice, including AWS, Google Cloud, Microsoft Azure and Oracle Cloud. This guide uses AWS as an example.

Based on the `hardware requirements <https://docs.mattermost.com/install/requirements.html#hardware-requirements>`_, here’s what Mattermost’s server architecture looks like for a 10,000-user deployment:

.. image:: ../images/scaling-1.png

**Sizing Guide Using AWS**

On AWS, we recommend using the following EC2 server types as a baseline:

* App servers:  m5.xlarge
* Database servers:  r4.xlarge

For the purposes of this guide, we will assume medium usage (10 MB/user/month with a 2x safety factor) for `storage estimates <https://docs.mattermost.com/install/requirements.html#alternate-storage-calculations>`_ and 200 MB/user/month for data transfer estimates. We will also assume on-demand pricing with no upfront payments, though more savings (typically 40% or more) can be achieved with reserved servers on 1–3 year commitments and upfront payments.

As deployments scale above 5,000 users, additional servers are added for performance load-balancing and to provide additional redundancy (see our `High Availability Cluster guide <https://docs.mattermost.com/deployment/cluster.html#mattermost-server-configuration>`_).

`This spreadsheet <https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRkhRPFsf1_91AXFbqnmUT0UnpdZ1ZagbiTw9sfuBAL21ncnu7fynZ3yDrp22-LXCeXh0-xF_NFFPp3/pubhtml>`_ shows how much hardware you’ll need for different-sized Mattermost deployments and provides an estimate of how much each will cost. It includes links to AWS’s cost calculator for various deployment sizes. The smaller deployment examples (i.e., 1,000 users and 5,000 users) are on the conservative side, with separate servers per function that can easily be scaled out as Mattermost is rolled out. 

Here’s an example of the hardware you’ll need for a 10,000-user deployment:

.. image:: ../images/scaling-3.PNG

For more information, check out our `Administrator's Guide <https://docs.mattermost.com/guides/administrator.html>`_.
