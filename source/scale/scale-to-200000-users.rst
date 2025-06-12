Scale Mattermost up to 200000 users
====================================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

This page describes the Mattermost reference architecture designed for the load of up to 200000 concurrent users. Unsure which reference architecture to use? See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for details.

- **High Availability**: Required
- **Database Configuration**: writer, multiple readers

.. note::
  - Usage of CPU, RAM, and storage space can vary significantly based on user behavior. These hardware recommendations are based on traditional deployments and may grow or shrink depending on how active your users are.
  - From Mattermost v10.4, Mattermost Enterprise customers can configure `Redis <https://redis.io/>`_ (Remote Dictionary Server) as an alternative cache backend. Using Redis can help ensure that Mattermost remains performant and efficient, even under heavy usage. See the :ref:`Redis cache backend <configure/environment-configuration-settings:redis cache backend>` configuration settings documentation for details.
  - While the following Elasticsearch specifications may be more than sufficient for some use cases, we have not extensively tested configurations with lower resource allocations for this user scale. If cost optimization is a priority, admins may choose to experiment with smaller configurations, but we recommend starting with the tested specifications to ensure system stability and performance. Keep in mind that under-provisioning can lead to degraded user experience and additional troubleshooting effort.

User login scalability
-----------------------

Tests across all architectures were conducted at a rate of 4 user logins per second (14,400 users per hour). For this architecture, we performed additional testing at higher rates, reaching up to 30 user logins per second. 

Results show that this architecture supports logging in up to 150,000 users within 1.5 hours at the higher rate. Beyond this 150,000-user mark, the only available data is at the base rate of 4 logins per second, and no conclusive performance data exists at larger rates.

Requirements
------------

.. tip::

  Scroll horizontally to see additional columns in the table below.

+------------------------+-----------+----------------+--------------------+----------------------+
| **Resource Type**      | **Nodes** | **vCPU/        | **AWS Instance**   | **Azure Instance**   |
|                        |           | Memory (GiB)** |                    |                      |
+========================+===========+================+====================+======================+
| Mattermost Application | 14        | 16/32          | c7i.4xlarge        | F16s v2              |
+------------------------+-----------+----------------+--------------------+----------------------+
| RDS Writer             | 1         | 16/128         | db.r7g.4xlarge     | E16as v6             |
+------------------------+-----------+----------------+--------------------+----------------------+
| RDS Reader             | 6         | 16/128         | db.r7g.4xlarge     | E16as v6             |
+------------------------+-----------+----------------+--------------------+----------------------+
| Elasticsearch cluster  | 4         | 8/64           | r6g.2xlarge.search | E8ads v6             |
+------------------------+-----------+----------------+--------------------+----------------------+
| Proxy                  | 4         | 32/128         | m6in.8xlarge       | D32s v6              |
+------------------------+-----------+----------------+--------------------+----------------------+
| Redis                  | 1         | 8/32           | cache.m7g.2xlarge  | Azure Cache Redis P3 |
+------------------------+-----------+----------------+--------------------+----------------------+

Lifetime storage
----------------

.. include:: ../scale/lifetime-storage.rst
  :start-after: :nosearch:

Estimated storage per user, per month
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../scale/estimated-storage-per-user-per-month.rst
  :start-after: :nosearch:

Example
~~~~~~~

A 200000-person team with medium usage (with a safety factor of 2x) would require between 21.12TB :sup:`1` and 105.6TB :sup:`2` of free space per annum.

:sup:`1` 200000 users * 5 MB * 12 months * 2x safety factor

:sup:`2` 200000 users * 25 MB * 12 months * 2x safety factor

We strongly recommend that you review storage utilization at least quarterly to ensure adequate free space is available.

Additional considerations
-------------------------

.. include:: ../scale/additional-ha-considerations.rst
  :start-after: :nosearch:
