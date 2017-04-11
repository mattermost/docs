Searching
=========

Use the search box to find messages and replies that match the search terms that you enter. All channels that you are a member of in the current team are searched.

- Multiple-word search terms return results that contain all of the terms.
- When results appear, click the **Jump** link to view that post in the
   channel archive.
- File attachments and their filenames are not searched. If file attachments show up in the search results, it's because they are attached to messages that match the search query.
-  You can use search modifiers such as ``from:dave`` to return results only from certain people or in certain channels. For more information about this, see the `Search Modifiers`_ section.

Like many search engines, common words such as ``the``, ``which``, and ``are`` (known as "stop words"), as well as two-letter and one-letter
search terms, are not shown in search because they typically return too
many results. See database documentation on `MySQL`_ and
`Postgres`_ for a full list.

Search Modifiers
----------------

From: and In:
^^^^^^^^^^^^^

Use ``from:`` to find posts from specific users and ``in:`` to find
posts in specific channels.

-  For example: Searching ``Mattermost in:town-square`` only returns
   messages in Town Square that contain ``Mattermost``.

Quotation Marks
^^^^^^^^^^^^^^^^^

Use quotation marks to return search results for exact terms.

-  For example: Searching ``"Mattermost website"`` returns messages
   containing the exact phrase ``Mattermost website``, but not messages
   containing ``Mattermost`` and ``website`` separately.

Wildcard
^^^^^^^^^

Use the ``*`` character for wildcard searches that match within words.

-  For example: Searching for ``rea*`` brings back messages containing
   ``reach``, ``reason`` and other words starting with ``rea``.

Hashtags
--------

Hashtags are searchable labels for posts. Search for any posts
containing a hashtag by clicking the hashtag in an existing post or
typing the hashtag with the pound symbol into the search bar. Create
hashtags in any post by using the pound sign ``#`` followed by
alphanumeric or other unicode characters.

Valid hashtags:

- Do not start with a number.
- Are at least 3 characters long, not including the ``#``.
- Are made up of alphanumeric or other unicode characters.
- May contain dots, dashes or underscores.

Examples: ``#bug``, ``#marketing``, ``#user_testing``,
``#per.iod``, ``#check-in``, ``#마케팅``

Hashtags do not link to channels. For example, if you have a channel
named “Marketing”, clicking a ``#marketing`` hashtag does not redirect
you to that channel. You can link to public channels using ``~`` followed
by the channel name, for example ``~marketing``.

Other notes:

-  IP addresses, for example ``10.100.200.101``, do not return results.

Technical Notes
---------------

Searching Chinese, Korean and Japanese
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The best experience for searching in Chinese, Korean and Japanese is
   to use MySQL 5.7.6 or later with special configuration. Please see
   `documentation`_.
-  You can search to some degree without this configuration by adding
   ``*`` to the end of search terms.

Differences between MySQL and Postgres search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, Mattermost uses full text search support included in MySQL
and PostgreSQL. These databases have slightly different search behavior.
Check **Main Menu** > **About Mattermost** to see which database you’re
using.

For example, different databases have different “stop words” filtered
out of search results. See database documentation on `MySQL`_ and
`Postgres`_ for a full list. Other differences include:

PostgreSQL:

- Email addresses do not return results.
- Hashtags or recent mentions of usernames containing a dash do not return search results.
- Terms containing a dash return incorrect results as dashes are ignored in the search engine.

MySQL:

- Hashtags or recent mentions of usernames containing a dot do not return search results.

.. _documentation: https://docs.mattermost.com/install/i18n.html
.. _MySQL: http://dev.mysql.com/doc/refman/5.7/en/fulltext-stopwords.html
.. _Postgres: http://apt-browse.org/browse/ubuntu/precise/main/i386/postgresql-9.1/9.1.3-2/file/usr/share/postgresql/9.1/tsearch_data/english.stop
