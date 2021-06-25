.. _bulk-loading:

Bulk Loading Data
=================

Large quantities of data can be imported from a `JSONL
<https://jsonlines.org>`__ file into Mattermost at the command line using the bulk loading feature. This feature is most suitable for migrating data from an existing messaging system, or for pre-populating a new installation with data.

You can import the following data types:

- Teams
- Channels (Public and Private)
- Users
- Users' Team memberships
- Users' Channel memberships
- Users' notification preferences
- Posts (regular, non-reply posts)
- Posts' Replies
- Posts' Reactions
- Posts' File Attachments
- Direct Message and Group Message channels
- Direct Messages and Group Messages
- Direct Messages from a user to themselves
- Permissions Schemes
- Custom Emoji

Importing additional types of posts is not yet supported.

.. contents:: Contents
  :backlinks: top
  :local:
  :depth: 2

.. include:: bulk-loading-about.rst
.. include:: run-bulk-loading-command.rst
.. include:: bulk-loading-data-format.rst
.. include:: bulk-loading-troubleshooting.rst
