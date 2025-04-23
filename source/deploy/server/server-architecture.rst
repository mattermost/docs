Reference Architecture for Mattermost Server
=============================================

The following diagrams detail suggested architecture configurations of :ref:`high availability Mattermost deployments <scale/high-availability-cluster-based-deployment:deployment guide>` at different scales. Hardware and infrastructure requirements will vary significantly based on usage and policies. See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for reference architecture guidance at scale, including hardware and infrastructure requirements.

High availability in Mattermost consists of running redundant Mattermost application servers, redundant database servers, and redundant load balancers so that failure of any one of these components does not interrupt operation of the system. Upon failure of one component, the remaining application servers, database servers, and load balancers must be sized and configured to carry the full load of the system. If this requirement is not met, an outage of one component can result in an overload of the remaining components, causing a complete system outage.

.. important::

   Mattermost does not support high availability deployments spanning multiple datacenters. All nodes in a high availability cluster must reside within the same datacenter to ensure proper functionality and performance.

You can apply most configuration changes and dot release security updates without interrupting service, provided that you update the system components in the correct sequence. Changes to configuration settings that require a server restart, and server version upgrades that involve a change to the database schema, require a short period of downtime. Downtime for a server restart is around 5 seconds. For a database schema update, downtime can be up to 30 seconds.

Designed for scale
------------------

Mattermost is designed to be able to handle a large number of concurrent users, and the architecture can be scaled up or down as needed. The architecture is also designed to be flexible, allowing for the addition of new components or services as needed. The following diagrams show the recommended architecture for Mattermost deployments at 5,000, 10,000, 25,000, and 50,000 users. The diagrams are organized by user count and include a general diagram and AWS and Azure versions of each diagram. See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for more information on scaling Mattermost deployments.

- Each generalized diagram represents a full High Availability deployment across all critical components. The proxy, database, file storage, and Elasticsearch layers can be replaced by cloud services. 
- Each AWS diagram represents a full High Availability deployment on Amazon Web Services making full use of the available services.
- Each Azure diagram represents a full High Availability deployment on Microsoft Azure making full use of the available services.
- Push proxy can be replaced by the Mattermost :ref:`hosted push notification service <configure/environment-configuration-settings:hosted push notifications service (hpns)>`.

.. tab:: AWS

    .. tab:: 5,000 users

        .. image:: /images/MattermostDeployment5kaws.png
            :class: bg-white

    .. tab:: 10,000 users

        .. image:: /images/MattermostDeployment10kaws.png
            :class: bg-white

    .. tab:: 25,000 users

        .. image:: /images/MattermostDeployment25kaws.png
            :class: bg-white

    .. tab:: 50,000 users

        .. image:: /images/MattermostDeployment50kaws.png
            :class: bg-white

.. tab:: Azure

    .. tab:: 5,000 users

        .. image:: /images/MattermostDeployment5kAzure.png
            :class: bg-white

    .. tab:: 10,000 users

        .. image:: /images/MattermostDeployment10kAzure.png
            :class: bg-white

    .. tab:: 25,000 users

        .. image:: /images/MattermostDeployment25kAzure.png
            :class: bg-white

    .. tab:: 50,000 users

        .. image:: /images/MattermostDeployment50kAzure.png
            :class: bg-white
