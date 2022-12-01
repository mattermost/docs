.. _bulk-export:

Bulk export tool
================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Moving data from one Mattermost instance into another begins with exporting data to a `JSONL <https://jsonlines.org>`__ file using the
`bulk loading feature </onboard/bulk-loading-data.html>`__. This tool is useful if you have created a server for a proof of concept, have created another server for production use, and now want to retain the history from the proof of concept instance.

You can export the following data types:

- Teams
- Channels (public, private, and direct)
- Users
- Users' team memberships
- Users' channel memberships
- Posts (messages in public or private channels and replies to those messages)

.. include:: bulk-export-data.rst
  :start-after: :nosearch: