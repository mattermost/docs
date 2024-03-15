Scale Mattermost up to 15000 users
==================================

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

This page describes the Mattermost reference architecture designed for the load of up to 15000 concurrent users. Unsure which reference architecture to use? See the `scaling for enterprise </scale/scaling-for-enterprise.html>`__ documentation for details.

- **High Availability**: Required
- **Database Configuration**: writer, multiple readers

.. note::
    Usage of CPU, RAM, and storage space can vary significantly based on user behavior. These hardware recommendations are based on traditional deployments and may grow or shrink depending on how active your users are.

Requirements
------------

+------------------------+----------+------------------+----------------+------------------+
| **Resource Type**      | **vCPU** | **Memory (GiB)** | **# of Nodes** | **AWS Instance** |
+========================+==========+==================+================+==================+
| Mattermost Application | 4        | 8                | 2              | c6i.xlarge       |
+------------------------+----------+------------------+----------------+------------------+
| RDS Writer             | 4        | 32               | 1              | db.r6g.xlarge    |
+------------------------+----------+------------------+----------------+------------------+
| RDS Reader             | 4        | 32               | 1              | db.r6g.xlarge    |
+------------------------+----------+------------------+----------------+------------------+

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

A 15000-person team with medium usage (with a safety factor of 2x) would require between 1.8TB :sup:`1` and 9TB :sup:`2` of free space per annum.

:sup:`1` 15000 users * 5 MB * 12 months * 2x safety factor

:sup:`2` 15000 users * 25 MB * 12 months * 2x safety factor

We strongly recommend that you review storage utilization at least quarterly to ensure adequate free space is available.

Additional considerations
-------------------------

.. include:: ../scale/additional-ha-considerations.rst
  :start-after: :nosearch: