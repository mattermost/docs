.. _install-kubernetes-cluster:

Using a Custom Configuration
=================================

Custom Resource Requirements
-----------------------------

Running Mattermost in Kubernetes requires different resources based on your total number of users.
The table below details the minimum Kubernetes cluster resources that Mattermost requires at different scales.


.. csv-table::
    :header: "User Count", "Node Count", "Memory per Node", "vCPU per Node"

    "5,000", "6", "8 GB", "4"
    "10,000", "8", "16 GB", "4"
    "25,000", "14", "16 GB", "4"

**Note:**

    - These are minimum requirements and yours may differ significantly.
    - These resources take into account all components required for Mattermost, including proxy, database and file storage.
    - Resource requirements may vary depending on user usage and bot activity.
    - For larger installations, it may be beneficial to use nodes for the databases that have more memory and/or are optimized for memory.
    - For installations of more than 25,000 users please `contact us <https://mattermost.com/contact-us/>`__ for sizing guidelines.

Custom Configuration
--------------------

You can opt to install the Mattermost operator on top of your existing infrastructure in which case you only need to install the Mattermost operator:

.. code-block:: sh

   $ kubectl create ns mattermost-operator
   $ kubectl apply -n mattermost-operator -f https://raw.githubusercontent.com/mattermost/mattermost-operator/master/docs/mattermost-operator/mattermost-operator.yaml
