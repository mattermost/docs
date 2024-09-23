Scale Mattermost up to 70000 users
==================================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

This page describes the Mattermost reference architecture designed for the load of up to 70000 concurrent users. Unsure which reference architecture to use? See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for details.

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
| Mattermost Application | 4         | 16/32          | c6i.4xlarge       |
+------------------------+-----------+----------------+-------------------+
| RDS Writer             | 1         | 16/128         | db.r6g.4xlarge    |
+------------------------+-----------+----------------+-------------------+
| RDS Reader             | 4         | 16/128         | db.r6g.4xlarge    |
+------------------------+-----------+----------------+-------------------+
| Elasticsearch Node     | X         | 4/32           | r6g.xlarge.search |
+------------------------+-----------+----------------+-------------------+
| Proxy                  | X         | 16/64          | m7i.4xlarge       |
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

A 70000-person team with medium usage (with a safety factor of 2x) would require between 8.4TB :sup:`1` and 42TB :sup:`2` of free space per annum.

:sup:`1` 70000 users * 5 MB * 12 months * 2x safety factor

:sup:`2` 70000 users * 25 MB * 12 months * 2x safety factor

We strongly recommend that you review storage utilization at least quarterly to ensure adequate free space is available.

Additional considerations
-------------------------

.. include:: ../scale/additional-ha-considerations.rst
  :start-after: :nosearch: