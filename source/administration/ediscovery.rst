.. _ediscovery:

Electronic Discovery
=====================================

Electronic discovery (also known as eDiscovery) refers to a process where where electronic data is searched with the intent to use it as evidence in a legal case.

This page describes how to extract data from Mattermost for eDiscovery. There are three primary methods that can be used to accomplish the goal or extracting user post data from Mattermost:

- `Mattermost Compliance Exports <https://docs.mattermost.com/administration/compliance-export.html>`_;
- Mattermost RESTful API;
- Mattermost database using standard SQL queries.

Each of the options is discussed in detail below.

.. note::

  Litigation hold (also known as legal hold) is an extension of eDiscovery where in addition to searching for records, no electronically stored information nor paper documents may be discarded if they may be deemed relevant for a present or future legal case.

Mattermost Compliance Exports
------------------------------------

Mattermost Enterprise E20 has compliance report export capabilities.

Mattermost can export compliance related data, including the content of messages and who might have seen those messages in three formats: Actiance XML, Global Relay EML, and generic CSV. Reports can be configured to run on a delay basis and stored in a shared location.

For more information about the exports feature and how to set up reporting, see `our documentation <https://docs.mattermost.com/administration/compliance-export.html>`_.

Mattermost RESTful API
------------------------------------


