Search for messages
===================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Use Mattermost search to find messages, replies, and the contents of files. You can also search by `hashtags <#hashtags>`__ and perform more advanced searches using `search modifiers <#search-modifiers>`__.

Search for message
-------------------

.. tab:: Web/Desktop

  1. Select the Search field, select **Messages**, enter your search criteria.

    .. image:: ../../images/search-messages.png
      :alt: Use the Search field to search for messages.

    .. image:: ../../images/search-messages-expanded.png
      :alt: Use the expanded Search field to search for messages.

  2. By default, your search results include messages from all channels within your current team. From Mattermost v10.8, you can select **All Teams** to search all channels across all teams, select a specific team instead, or continue searching within the current team.

    .. image:: ../../images/search-all-teams.png
      :alt: Select All Teams to search all channels across all teams.

    .. tip::
      
      From Mattermost v10.10, the ``from:`` search modifier is available for cross-team searches. When searching all teams, you must manually add the ``from:`` modifier as part of your search criteria to search by specific users across teams.

  3. When message results display in the Search Results pane, select **Jump** to view a full message in context. 

    .. image:: ../../images/jump-to-message.png
      :alt: From search results, you can go to the full message by selecting Jump.

  .. tip::

    From Mattermost v10.8, you can also adjust your search results to show messages from the current team, a specific team, or all teams.

.. tab:: Mobile

  1. Tap the **Search** |search-icon| icon at the bottom of the app to search for messages or files attached to messages.

    .. image:: ../../images/mobile-search-for-messages.jpg
        :alt: Tap on the Search icon to search for messages.
        :scale: 30

  2. By default, your search results include messages from all channels within your current team. From mobile v2.28, tap **All Teams** to search all channels across all teams, or select a specific team instead.

    .. image:: ../../images/mobile-search-message-team-selection.jpg
        :alt: Tap on the Team selector to select the team you want to search in.
        :scale: 30

  3. Enter your search criteria.

    .. image:: ../../images/mobile-search-message-criteria-with-hashtags.jpg
        :alt: Type your search criteria along with applicable hashtags.
        :scale: 30

  4. Tap to apply `search modifiers <#search-modifiers>`__ to your search.

    .. image:: ../../images/mobile-search-message-with-modifiers.jpg
        :alt: Apply search modifiers to further refine your search.
        :scale: 30
  
    .. image:: ../../images/mobile-search-message-results.jpg
        :alt: Check the search results to find your required message or file from the list.
        :scale: 30

  .. tip::

    You can adjust search results to show messages from the current team, a specific team, or all teams.

Search for files
----------------

From the **Search** field, select **Files** to search for files attached to messages. From Mattermost v10.8 and mobile v2.28, you can specify whether you want to search all channels you're a member of in the current team, a specific team, or all channels across all teams. 

.. image:: ../../images/search-files.png
  :alt: Use the Search field to serach for files attached to messages.

File contents that match on file name, or contain matching text content within supported document types, are returned in the Search Results pane. Each search result includes file name, extension, and size details, as well as details about when and where the file was originally shared. You can adjust search results to show messages from the current team, a specific team, or all teams.

- For Mattermost Cloud :doc:`workspaces </end-user-guide/end-user-guide-index>`, supported document file formats include PDF, PPTX, DOCX, ODT, HTML, and plain text documents. DOC and RTF file formats, as well as the contents of ZIP files, are not supported.
- For Mattermost self-hosted deployments, supported document file formats include PDF, PPTX, DOCX, ODT, HTML, and plain text documents. 

.. note::

  System admins can extend file content search support for self-hosted deployments to include:

  - :ref:`files shared before upgrading to Mattermost Server v5.35 <administration-guide/manage/mmctl-command-line-tool:mmctl extract>`.
  - :ref:`DOC and RTF file formats <administration-guide/configure/environment-configuration-settings:enable document search by content>`.
  - :ref:`documents within ZIP files <administration-guide/configure/environment-configuration-settings:enable searching content of documents within zip files>`.

Filter results by file type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using Mattermost in a web browser or the desktop app, you can narrow search results further by selecting the **File Type Filter** option, then selecting specific file types, such as documents, spreadsheets, or images.

.. image:: ../../images/file-search-filter.png
  :alt: You can filter search results by file type.

Access recently shared files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can access files recently shared in a channel:

.. tab:: Web/Desktop

  Select the |channel-files-icon| icon to the right of the channel name to access files recently shared in that channel. 

  .. image:: ../../images/channel-files-icon.png
    :alt: Use the Channel Files option to access recently shared files in the current channel.

  Alternatively, you can select the channel name, select the **View Info** |channel-info| icon, then select **Files** in the right pane.

.. tab:: Mobile

  Tap the channel name to view channel options, then tap **Files**.

Search modifiers
----------------

You can apply search modifiers to any search to reduce the number of results returned. Select a search modifier to add it to the Search field. Supported modifiers are described below. Your search results include messages from all of your teams.

``from:`` and ``in:``
~~~~~~~~~~~~~~~~~~~~~

- Use ``from:`` to find messages or files from specific users. 

  * For example, searching ``from:john.smith`` only returns content from your direct message history with John Smith.
  * From Mattermost v10.10, you can use ``from:`` in cross-team searches to find messages from specific users across all teams you're a member of.

- Use ``in:`` to find messages or files posted in specific public channels, private channels, direct messages, or group messages. You can specify channels by display name or channel ID. 
  
  * For example, searching ``Mattermost in:town-square`` only returns results in the Town Square public channel that contains the term ``Mattermost``, while searching ``Mattermost in:john.doe`` only returns results that contains the term ``Mattermost`` in your direct message history with John Smith.

``before:``, ``after:``, and ``on:``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Use ``before:`` to find messages or files posted before a specified date.

  * For example, searching ``website before: 2018-09-01`` returns messages or files containing the term ``website`` posted prior to September 1, 2018.

- Use ``after:`` to find messages or files posted after a specified date.

  * For example, searching ``website after: 2018-08-01`` returns messages or files containing the term ``website`` posted after August 1, 2018.

- Use both ``before:`` and ``after:`` together to search in a specified date range.

  * For example, searching ``website before: 2018-09-01 after: 2018-08-01`` returns all messages or files containing the term ``website`` posted between August 1, 2018 and September 1, 2018.

- Use ``on:`` to find messages or files posted on a specific date. Use the date picker to select a date, or type it in YYYY-MM-DD format.

  * For example, searching ``website on: 2018-09-01`` returns messages or files containing the term ``website`` posted on September 1, 2018.

  .. image:: ../../images/calendar2.png
    :alt: Select the on modifier to specify messages or files for a specific a date.
    :scale: 50

Exclusions
~~~~~~~~~~

Use the hyphen ``-`` symbol to exclude terms from your search results. For example, searching ``test -release`` only returns results that include the term ``test`` and exclude the term ``release``.

This exclusion modifier can be used in combination with other modifiers to further refine search results. For example, searching ``test -release -in:release-discussion -from:eric`` returns all results with the term ``test``, excludes posts with the term ``release``, excludes posts made in the ``release-discussion`` channel, and excludes messages sent in direct messages by ``eric``.

Quotation marks
~~~~~~~~~~~~~~~

Use quotation marks ``" "`` to return search results for exact terms. For example, searching ``"Mattermost website"`` returns messages containing the exact phrase ``Mattermost website``, but doesn't return results containing ``Mattermost`` and ``website`` as separate terms.

Wildcards
~~~~~~~~~

Use the asterisk ``*`` symbol at the end of the word to perform a wildcard search. The wildcard search returns all words that begin with the specified letters. The wildcard in search cannot be used at the beginning or in the middle of a word. For example, searching ``rea*`` returns messages or files containing words like ``reach``, ``reason``, ``reality``, ``real``, and other words starting with ``rea``. However, searches like ``*each`` and ``re*ch`` are invalid wildcard searches.

Hashtags
~~~~~~~~~

Hashtags are searchable labels for messages. Anyone can create a hashtag in a message by using the pound sign ``#`` followed by alphanumeric or other unicode characters. Hashtag examples include: ``#bug``, ``#marketing``, ``#user_testing``, ``#per.iod``, ``#check-in``, ``#마케팅``.

Valid hashtags:

- Don't start with a number.
- Are at least three characters long, excluding the ``#``.
- Are made up of alphanumeric or other unicode characters.
- May contain dots, dashes, or underscores.

To search for messages containing hashtags, select a hashtag in an existing post, or type the hashtag (including the pound ``#`` symbol) into the search bar. 

.. note::
  
  Hashtags don't link to channels. If you have a channel named “Marketing”, selecting a ``#marketing`` hashtag does not take you to the Marketing channel. To link to public channels, use the tilde ``~`` symbol followed by the channel name. For example ``~marketing``.

Notes about performing Mattermost searches
-------------------------------------------

- Multiple-word searches return results that contain *all* of your search criteria.
- Search modifiers can help narrow down searches. See the `search modifiers <#search-modifiers>`__ section for details.
- You can search Archived channels as long as you're a member of that channel.

  - If you're unable to see messages or files in archived channels in your search results, ask your system admin if **Allow users to view archived channels** has been disabled via **System Console > Site Configuration > Users and Teams**.
  - To remove archived channels from your search results, you can leave the Archived channels.
- Like many search engines, common words such as ``the``, ``which``, and ``are`` (known as "stop words"), as well as two-letter and one-letter search terms, are not shown in search results because they typically return too many results. See the `Technical notes about searching <#technical-notes-about-searching>`__ section below for details.
- IP addresses (e.g. ``10.100.200.101``) don't return results.

Technical notes about searching
-------------------------------

By default, Mattermost uses full text search support included in PostgreSQL. Select the **product menu** |product-list| then select **About Mattermost** to see which database you’re using.

- Stop words are filtered out of search results. See `PostgreSQL <https://www.postgresql.org/docs/10/textsearch-dictionaries.html#TEXTSEARCH-STOPWORDS>`__ database documentation for a full list of applicable stop words.
- URLs don’t return results.
- Hashtags or recent mentions of usernames containing a dash don't return results.
- Terms containing a dash return incorrect results since dashes are ignored in the search engine.
- From Mattermost v7.1, search results respect the ``default_text_search_config`` value instead of being hardcoded to English. We recommend that Mattermost system admins review this value to ensure it's set correctly.
