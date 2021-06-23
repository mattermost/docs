.. _install-kubernetes-cluster:

Setting Up a Kubernetes Cluster
-------------------------------

Prerequisites
~~~~~~~~~~~~~

Prerequisites for using the Mattermost Operator:

- Kubernetes cluster in version 1.16 or higher.
- Kubernetes CLI `kubectl <https://kubernetes.io/docs/reference/kubectl/overview/>`__ installed on local machine.

It’s recommended that you have a basic understanding of Kubernetes concepts (such as deployments, pods) and actions (such as applying manifests, viewing pod logs). It's also advisable to consult the `official Kubernetes setup documentation <https://kubernetes.io/docs/setup/>`__ on how to set up a cluster in your environment.

If you’re unsure about which environment you want to use for your Kubernetes cluster, we suggest using a managed service such as as `Amazon EKS <https://aws.amazon.com/eks/>`__, `Azure Kubernetes Service <https://azure.microsoft.com/en-ca/services/kubernetes-service/>`__, `Google Kubernetes Engine <https://cloud.google.com/kubernetes-engine/>`__, or `DigitalOcean Kubernetes <https://www.digitalocean.com/products/kubernetes/>`__.

Confirm Resource Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running Mattermost in Kubernetes requires different resources based on your total number of users. The table below details the minimum Kubernetes cluster resources that Mattermost requires at different scales.

**Note:** These are minimum requirements and yours may differ significantly.

.. csv-table::
    :header: "User Count", "Node Count", "Memory per Node", "vCPU per Node"

    "5,000", "6", "8 GB", "4"
    "10,000", "8", "16 GB", "4"
    "25,000", "14", "16 GB", "4"


- These resources take into account all components required for Mattermost, including proxy, database, and file storage.
- Requirements may be significantly lower when using an external database and filestore (recommended).  
- Resource requirements may vary depending on user usage and bot activity.
- For larger installations, it may be beneficial to use nodes for the databases that have more memory and/or are optimized for memory.
- For installations of more than 25,000 users please `contact us <https://mattermost.com/contact-us/>`__ for sizing guidelines.
