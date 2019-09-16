.. _install-kubernetes-cluster:

Set Up a Kubernetes Cluster
============================

If you do not already have a production-ready Kubernetes cluster you will need to set one up. If you already have a Kubernetes cluster you can skip to step 2.

Your Kubernetes cluster must be version 1.12 or higher.

**1. Set up a Kubernetes cluster**

Kubernetes can be set up in practically any environment. See the `official Kubernetes setup documentation <https://kubernetes.io/docs/setup/>`__ to discover how to set up a cluster in your environment.

If you are unsure about what environment you want to run Kubernetes in, we suggest using a managed service such as `Amazon EKS <https://aws.amazon.com/eks/>`__, `Azure Kubernetes Service <https://azure.microsoft.com/en-ca/services/kubernetes-service/>`__, `Google Kubernetes Engine <https://cloud.google.com/kubernetes-engine/>`__, or `DigitalOcean Kubernetes <https://www.digitalocean.com/products/kubernetes/>`__.

Make sure to also install and configure `kubectl <https://kubernetes.io/docs/reference/kubectl/overview/>`__.

**2. Make sure your cluster has enough resources**

Running Mattermost in Kubernetes will require different resources based on your total number of users. Here are some guidelines for the resources that Mattermost will require at different scales:

.. csv-table::
    :header: "User Count", "Node Count", "Memory per Node", "vCPU per Node"

    "5,000", "6", "8 GB", "4"
    "10,000", "8", "16 GB", "4"
    "25,000", "14", "16 GB", "4"

Note:

- These resources take into account all components required for Mattermost, including proxy, database and file storage
- Resource requirements may vary depending on user usage and bot activity
- For larger installations, it may be beneficial to use nodes for the databases that have more memory and/or are optimized for memory
- For installations of more than 25,000 users please `contact us <https://mattermost.com/contact-us/>`__ for sizing guidelines

Make sure your Kubernetes cluster has enough nodes to run Mattermost at your desired scale.
