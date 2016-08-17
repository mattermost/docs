=========
Scaling for Enterprise 
=========

Mattermost is designed to scale from small teams hosted on a single server to large enterprises running in cluster-based, highly available deployment configurations. 

- Server requirements vary based on usage and it is highly recommended that pilots are run before enterprise-wide deployments in order to estimate full scale usage based on your specific organizational needs. 

Single Machine Deployment 
^^^^^^^^^^^^^^^^^^^^^^^

Organizations less than 500 users can typically run on a single server. 

- See `install guides for step-by-step configuration instructions for single machine setup. <https://docs.mattermost.com/#install-guides>`_
- See `hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html>`_

Multi-Machine Deployment 
^^^^^^^^^^^^^^^^^^^^^^^

For deployments between 500 and 20,000 registered users with moderate usage can run on a standard three machine Mattermost deployment with a proxy, an application server, and a database server. At this scale, demands of larger organizations can typically be met by using powerful hardware in a standard configuration. 

- See `install guides for step-by-step configuration instructions for multi-machine setup. <https://docs.mattermost.com/#install-guides>`_
- See `hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html>`_

Cluster-based Deployment 
^^^^^^^^^^^^^^^^^^^^^^^

*Available in Enterprise Edition E20*

Deployments over 10,000 to 20,000 registered users with moderate usage can be supported by adding additional servers in cluster-based, high availability configuration. This configuration uses a load balancer to distribute requests from users across multiple Mattermost application servers, allowing the system to scale beyond the limits of any single server. 

- See `high availability deployment guide for horizontal scaling setup (Enterprise E20 only) <https://docs.mattermost.com/deployment/cluster.html>`_
