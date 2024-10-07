Scale Mattermost up to 30000 users
==================================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

This page describes the Mattermost reference architecture designed for the load of up to 30000 concurrent users. Unsure which reference architecture to use? See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for details.

- **High Availability**: Required
- **Database Configuration**: writer, multiple readers

.. note::
    Usage of CPU, RAM, and storage space can vary significantly based on user behavior. These hardware recommendations are based on traditional deployments and may grow or shrink depending on how active your users are.

Requirements
------------

+------------------------+-----------+----------------+-------------------+
| **Resource Type**      | **Nodes** | **vCPU/        | **AWS Instance**  |
|                        |           | Memory (GiB)** |                   |
+========================+===========+================+===================+
| Mattermost Application | 2         | 8/16           | c7i.2xlarge       |
+------------------------+-----------+----------------+-------------------+
| RDS Writer             | 1         | 8/64           | db.r7g.2xlarge    |
+------------------------+-----------+----------------+-------------------+
| RDS Reader             | 1         | 8/64           | db.r7g.2xlarge    |
+------------------------+-----------+----------------+-------------------+
| Elasticsearch Node     | 2         | 4/32           | r6g.xlarge.search |
+------------------------+-----------+----------------+-------------------+
| Proxy                  | 1         | 16/64          | m7i.4xlarge       |
+------------------------+-----------+----------------+-------------------+

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

A 30000-person team with medium usage (with a safety factor of 2x) would require between 3TB :sup:`1` and 15TB :sup:`2` of free space per annum.

:sup:`1` 30000 users * 5 MB * 12 months * 2x safety factor

:sup:`2` 30000 users * 25 MB * 12 months * 2x safety factor

We strongly recommend that you review storage utilization at least quarterly to ensure adequate free space is available.

Additional considerations
-------------------------

.. include:: ../scale/additional-ha-considerations.rst
  :start-after: :nosearch: