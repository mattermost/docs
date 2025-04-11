Scale Mattermost up to 200 users
================================

This page describes the Mattermost reference architecture designed for the load of up to 200 concurrent users. Unsure which reference architecture to use? See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for details.

- **High Availability**: Not required
- **Database Configuration**: Single

.. note::
    Usage of CPU, RAM, and storage space can vary significantly based on user behavior. These hardware recommendations are based on traditional deployments and may grow or shrink depending on how active your users are.

Requirements
------------

+------------------------+-----------+----------------+-------------------+
| **Resource Type**      | **Nodes** | **vCPU/        | **AWS Instance**  |
|                        |           | Memory (GiB)** |                   |
+========================+===========+================+===================+
| Mattermost Application | 1         | 2/4            | c7i.large         |
+------------------------+-----------+----------------+-------------------+
| RDS Writer             | 1         | 2/16           | db.r7g.large      |
+------------------------+-----------+----------------+-------------------+
| RDS Reader             | 0         | 2/16           | db.r7g.large      |
+------------------------+-----------+----------------+-------------------+
| Elasticsearch Node     | 0         | 4/32           | r6g.xlarge.search |
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

A 200-person team with medium usage (with a safety factor of 2x) would require between 12GB :sup:`1` and 60GB :sup:`2` of free space per annum.

:sup:`1` 200 users * 5 MB * 12 months * 2x safety factor

:sup:`2` 200 users * 25 MB * 12 months * 2x safety factor

We strongly recommend that you review storage utilization at least quarterly to ensure adequate free space is available.

Additional considerations
-------------------------

Smaller deployments, or deployments using the :doc:`Mattermost Omnibus installer </deploy/server/deploy-linux>`, will need an increase in resources due to the fact the database is hosted on the same server as the Mattermost application.