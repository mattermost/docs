Scale Mattermost up to 200000 users
====================================

.. include:: ../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

This page describes the Mattermost reference architecture designed for the load of up to 200000 concurrent users. Unsure which reference architecture to use? See the :doc:`scaling for enterprise </administration-guide/scale/scaling-for-enterprise>` documentation for details.

- **High Availability**: Required
- **Database Configuration**: writer, multiple readers

.. note::
  - Usage of CPU, RAM, and storage space can vary significantly based on user behavior. These hardware recommendations are based on traditional deployments and may grow or shrink depending on how active your users are.
  - From Mattermost v10.4, Mattermost Enterprise customers can configure `Redis <https://redis.io/>`_ (Remote Dictionary Server) as an alternative cache backend. Using Redis can help ensure that Mattermost remains performant and efficient, even under heavy usage. See the :ref:`Redis cache backend <administration-guide/configure/environment-configuration-settings:redis cache backend>` configuration settings documentation for details.
  - While the following Elasticsearch specifications may be more than sufficient for some use cases, we have not extensively tested configurations with lower resource allocations for this user scale. If cost optimization is a priority, admins may choose to experiment with smaller configurations, but we recommend starting with the tested specifications to ensure system stability and performance. Keep in mind that under-provisioning can lead to degraded user experience and additional troubleshooting effort.

User login scalability
-----------------------

Tests across all architectures were conducted at a rate of 4 user logins per second (14,400 users per hour). For this architecture, we performed additional testing at higher rates, reaching up to 30 user logins per second. 

Results show that this architecture supports logging in up to 150,000 users within 1.5 hours at the higher rate. Beyond this 150,000-user mark, the only available data is at the base rate of 4 logins per second, and no conclusive performance data exists at larger rates.

Requirements
------------

.. raw:: html

   <style>
   .scale-requirements-table {
     width: 100% !important;
     table-layout: fixed !important;
     border-collapse: collapse;
     font-size: 0.9em;
     overflow-wrap: break-word !important;
     word-wrap: break-word !important;
   }
   .scale-requirements-table th, .scale-requirements-table td {
     border: 1px solid #ddd;
     padding: 8px;
     text-align: left;
     vertical-align: top;
     word-wrap: break-word;
     overflow-wrap: break-word;
   }
   .scale-requirements-table th {
     background-color: #f8f9fa;
     font-weight: bold;
   }
   .scale-requirements-table col:nth-child(1) { width: 25%; }
   .scale-requirements-table col:nth-child(2) { width: 10%; }
   .scale-requirements-table col:nth-child(3) { width: 18%; }
   .scale-requirements-table col:nth-child(4) { width: 23%; }
   .scale-requirements-table col:nth-child(5) { width: 24%; }
   </style>

   <table class="scale-requirements-table">
   <colgroup>
   <col style="width: 25%">
   <col style="width: 10%">
   <col style="width: 18%">
   <col style="width: 23%">
   <col style="width: 24%">
   </colgroup>
   <thead>
   <tr>
   <th>Resource Type</th>
   <th>Nodes</th>
   <th>vCPU/Memory (GiB)</th>
   <th>AWS Instance</th>
   <th>Azure Instance</th>
   </tr>
   </thead>
   <tbody>
   <tr>
   <td>Mattermost Application</td>
   <td>14</td>
   <td>16/32</td>
   <td>c7i.4xlarge</td>
   <td>F16s v2</td>
   </tr>
   <tr>
   <td>RDS Writer</td>
   <td>1</td>
   <td>16/128</td>
   <td>db.r7g.4xlarge</td>
   <td>E16as v6</td>
   </tr>
   <tr>
   <td>RDS Reader</td>
   <td>6</td>
   <td>16/128</td>
   <td>db.r7g.4xlarge</td>
   <td>E16as v6</td>
   </tr>
   <tr>
   <td>Elasticsearch cluster</td>
   <td>4</td>
   <td>8/64</td>
   <td>r6g.2xlarge.search</td>
   <td>E8ads v6</td>
   </tr>
   <tr>
   <td>Proxy</td>
   <td>4</td>
   <td>32/128</td>
   <td>m6in.8xlarge</td>
   <td>D32s v6</td>
   </tr>
   <tr>
   <td>Redis</td>
   <td>1</td>
   <td>8/32</td>
   <td>cache.m7g.2xlarge</td>
   <td>Azure Cache Redis P3</td>
   </tr>
   </tbody>
   </table>

Lifetime storage
----------------

.. include:: lifetime-storage.rst
  :start-after: :nosearch:

Estimated storage per user, per month
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: estimated-storage-per-user-per-month.rst
  :start-after: :nosearch:

Example
~~~~~~~

A 200000-person team with medium usage (with a safety factor of 2x) would require between 21.12TB :sup:`1` and 105.6TB :sup:`2` of free space per annum.

:sup:`1` 200000 users * 5 MB * 12 months * 2x safety factor

:sup:`2` 200000 users * 25 MB * 12 months * 2x safety factor

We strongly recommend that you review storage utilization at least quarterly to ensure adequate free space is available.

Additional considerations
-------------------------

.. include:: additional-ha-considerations.rst
  :start-after: :nosearch:

`Book a live demo <https://mattermost.com/request-demo/>`_  or `talk to a Mattermost expert <https://mattermost.com/contact-sales/>`_ to explore tailored solutions for your organization's secure collaboration needs. Or try Mattermost yourself with a `1-hour preview <https://mattermost.com/sign-up/>`_ for instant access to a live sandbox environment.
