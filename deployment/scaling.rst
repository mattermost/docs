=========
Scaling for Enterprise 
=========

Mattermost is designed to scale from small teams hosted on a single server to large enterprises running in cluster-based, highly available deployment configurations. 

Server requirements vary based on usage and it is highly recommended that pilots are run before enterprise-wide deployments in order to estimate full scale usage based on your specific organizational needs. 

Small Teams 
^^^^^^^^^^^^^^^^^^^^^^^

Small teams can run Mattermost on a single server. 

- See `install guides for step-by-step configuration instructions for single machine setup. <https://docs.mattermost.com/#install-guides>`_
- See `hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html>`_

Vertical Scaling 
^^^^^^^^^^^^^^^^^^^^^^^

For deployments with fewer than 10,000 to 20,000 registered users with moderate usage, deployments can be supported by adding more powerful hardware to Mattermost's multi-machine production deployment installation. 

- See `install guides for step-by-step configuration instructions for multi-machine setup. <https://docs.mattermost.com/#install-guides>`_
- See `hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html>`_

Horizontal Scaling 
^^^^^^^^^^^^^^^^^^^^^^^

For deployments over 10,000 to 20,000 registered users with moderate usage, deployments can be supported by both adding more powerful hardware and by scaling horizontally in cluster-based high availability deployment configurations. 

- See `install guides for step-by-step configuration instructions for multi-machine setup. <https://docs.mattermost.com/#install-guides>`_
- See `hardware and software requirements for hardware sizing <https://docs.mattermost.com/install/requirements.html>`_
- See `high availability deployment guide for horizontal scaling setup (Enterprise E20 only) <https://docs.mattermost.com/deployment/cluster.html>`_
