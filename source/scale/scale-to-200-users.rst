Scale Mattermost up to 200 users
================================

This page describes the Mattermost reference architecture designed for the load of up to 200 concurrent users. Unsure which reference architecture to use? See the :doc:`scaling for enterprise </scale/scaling-for-enterprise>` documentation for details.

- **High Availability**: Not required
- **Database Configuration**: Single

.. note::
    Usage of CPU, RAM, and storage space can vary significantly based on user behavior. These hardware recommendations are based on traditional deployments and may grow or shrink depending on how active your users are.

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
   .scale-requirements-table th,
   .scale-requirements-table td {
     border: 1px solid #ddd;
     padding: 8px;
     vertical-align: top;
     word-wrap: break-word !important;
     overflow-wrap: break-word !important;
   }
   .scale-requirements-table th {
     background-color: #f8f9fa;
     font-weight: bold;
     text-align: left;
   }
   .scale-requirements-table th:nth-child(1) { width: 25%; }
   .scale-requirements-table th:nth-child(2) { width: 10%; }
   .scale-requirements-table th:nth-child(3) { width: 18%; }
   .scale-requirements-table th:nth-child(4) { width: 23%; }
   .scale-requirements-table th:nth-child(5) { width: 24%; }
   
   /* Dark mode support */
   body:not([data-custom-theme="light"]) .scale-requirements-table {
     background-color: #2d3748;
   }
   body:not([data-custom-theme="light"]) .scale-requirements-table th {
     background-color: #4a5568 !important;
     color: #fff;
     border-color: #718096 !important;
   }
   body:not([data-custom-theme="light"]) .scale-requirements-table td {
     color: #e2e8f0;
     border-color: #718096 !important;
   }
   
   /* Mobile responsiveness */
   @media (max-width: 768px) {
     .scale-requirements-table {
       font-size: 0.8em;
     }
     .scale-requirements-table th,
     .scale-requirements-table td {
       padding: 6px 4px;
     }
   }
   </style>

   <table class="scale-requirements-table">
   <thead>
   <tr>
   <th>Resource Type</th>
   <th>Nodes</th>
   <th>vCPU/ Memory (GiB)</th>
   <th>AWS Instance</th>
   <th>Azure Instance</th>
   </tr>
   </thead>
   <tbody>
   <tr>
   <td>Mattermost Application</td>
   <td>1</td>
   <td>2/4</td>
   <td>c7i.large</td>
   <td>F2s v2</td>
   </tr>
   <tr>
   <td>RDS Writer</td>
   <td>1</td>
   <td>2/16</td>
   <td>db.r7g.large</td>
   <td>E2as v6</td>
   </tr>
   <tr>
   <td>RDS Reader</td>
   <td>0</td>
   <td>2/16</td>
   <td>db.r7g.large</td>
   <td>E2as v6</td>
   </tr>
   <tr>
   <td>Elasticsearch Node</td>
   <td>0</td>
   <td>4/32</td>
   <td>r6g.xlarge.search</td>
   <td>E4ads v6</td>
   </tr>
   <tr>
   <td>Proxy</td>
   <td>1</td>
   <td>16/64</td>
   <td>m7i.4xlarge</td>
   <td>D16s v6</td>
   </tr>
   </tbody>
   </table>

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

Smaller deployments will need an increase in resources due to the fact the database is hosted on the same server as the Mattermost application.
