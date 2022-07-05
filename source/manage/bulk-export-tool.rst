.. _bulk-export:

Bulk export tool
================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Moving data from one Mattermost instance into another begins with exporting data to a `JSONL <https://jsonlines.org>`__ file using the
`bulk loading feature <https://docs.mattermost.com/onboard/bulk-loading-data.html>`__. This tool is useful if you have created a server for a proof of concept, have created another server for production use, and now want to retain the history from the proof of concept instance.

You can export the following data types:

- Teams
- Channels (Public and Private)
- Users
- Users' Team memberships
- Users' Channel memberships
- Posts (Posts in the Public/Private channels and also replies to those posts)

.. include:: bulk-export-data.rst
  :start-after: :nosearch: