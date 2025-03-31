Server architecture reference
==============================

The following diagrams detail suggested architecture configurations of enterprise deployments of Mattermost at different scales. Hardware and infrastructure requirements will vary significantly based on usage and policies. See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for details.

Reference architectures
------------------------

There are 3 versions of each diagram: general, AWS, and Azure.

- Each generalized diagram represents a full High Availability deployment across all critical components. The proxy, database, file storage, and Elasticsearch layers can be replaced by cloud services. 
- Each AWS diagram represents a full High Availability deployment on Amazon Web Services making full use of the available services.
- Each Azure diagram represents a full High Availability deployment on Microsoft Azure making full use of the available services.
- Push proxy can be replaced by the Mattermost :ref:`hosted push notification service <configure/environment-configuration-settings:hosted push notifications service (hpns)>`.

.. tab:: 5000 users

    **General**

    .. image:: /images/MattermostDeployment5kUsers.png
        :class: bg-white

    **AWS**

    .. image:: /images/MattermostDeployment5kaws.png
        :class: bg-white

    **Azure**

    .. image:: /images/MattermostDeployment5kAzure.png
        :class: bg-white

.. tab:: 10,000 users

    **General**

    .. image:: /images/MattermostDeployment10kUsers.png
        :class: bg-white

    **AWS**

    .. image:: /images/MattermostDeployment10kaws.png
        :class: bg-white

    **Azure**

    .. image:: /images/MattermostDeployment10kAzure.png
        :class: bg-white

.. tab:: 25,000 users

    **General**

    .. image:: /images/MattermostDeployment25kUsers.png
        :class: bg-white

    **AWS**

    .. image:: /images/MattermostDeployment25kaws.png
        :class: bg-white

    **Azure**

    .. image:: /images/MattermostDeployment25kAzure.png
        :class: bg-white

.. tab:: 50,000 users

    **AWS**

    .. image:: /images/MattermostDeployment50kaws.png
        :class: bg-white

    **Azure**

    .. image:: /images/MattermostDeployment50kAzure.png
        :class: bg-white

Database with Virtual IPs
--------------------------

We recommend the following configuration for Highly-Available databases through virtual IPs.

.. image:: /images/DatabasewithVIPs.png
  :class: bg-white