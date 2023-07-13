Search for messages
===================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |product-list| image:: ../images/products_E82F.svg
  :alt: Navigate between channels, playbooks, and Boards using the product menu icon.

.. |search-icon| image:: ../images/magnify_F0349.svg
  :alt: Navigate between channels, playbooks, and Boards using the product menu icon.
  
.. |channel-info| image:: ../images/information-outline_F02FD.svg
  :alt: Use the Channel Info icon to access additional channel management options.

.. |channel-files-icon| image:: ../images/file-text-outline_F09EE.svg
  :alt: Use the Channel Files icon to search for files attached to messages in a given channel.

Use Mattermost search to find messages, replies, and the contents of files shared across all channels you're a member of in your team's conversation history. You can also search by `hashtags <#hashtags>`__ or perform more advanced searches using `search modifiers <#search-modifiers>`__.

Search for message and files 
-----------------------------

.. tabs::

  .. tab:: Desktop

    **Search for messages**

    1. Select the Search field, select **Messages**, then enter your search criteria. 

      .. image:: ../images/search-messages.png
        :alt: Use the Search field to search for messages.

    2. When message results display in the Search Results pane, select **Jump** to view a full message in context.

      .. image:: ../images/jump-to-message.png
        :alt: From search results, you can go to the full message by selecting Jump.

    **Search for files**

    File content search is available in Mattermost Server and in Mattermost Cloud. Select the **Search** field, select **Files**, then type your search criteria. 

      .. image:: ../images/search-files.png
        :alt: Use the Search field to serach for files attached to messages.

    File contents that match on file name, or contain matching text content within supported document types, are returned in the Search Results pane. Each search result includes file name, extension, and size details, as well as details about when and where the file was originally shared.

    - For Mattermost Cloud workspaces, supported document file formats include PDF, PPTX, DOCX, ODT, HTML, and plain text documents. DOC, RTF, and PAGES file formats, as well as the contents of ZIP files, are not supported.
    - For Mattermost self-hosted deployments, supported document file formats include PDF, PPTX, DOCX, ODT, HTML, and plain text documents. 

    .. note::
      
      System admins can extend file content search support for self-hosted deployments to include:
  
      - `files shared before upgrading to Mattermost Server v5.35 </manage/command-line-tools.html#mattermost-extract-documents-content>`__.
      - `DOC, RTF, and PAGES file formats </configure/configuration-settings.html#enable-document-search-by-content>`__.
      - `documents within ZIP files </configure/configuration-settings.html#enable-searching-content-of-documents-within-zip-files>`__.

    **Filter results by file type**
    
    To narrow search results further, in the Search Results pane, select the **File Type Filter** option, then select specific file types, such as documents, spreadsheets, or images.
  
    .. image:: ../images/file-search-filter.png
      :alt: You can filter search results by file type.

    .. tip::
      Select the **Channel Files** icon below the channel name to access files recently shared in the current channel. 
  
      .. image:: ../images/channel-files-icon.png
        :alt: Use the Channel Files option to access recently shared files in the current channel.

  .. tab:: Mobile

    1. Tap the **Search** |search-icon| icon at the bottom of the app to search for messages or files attached to messages.
    2. To the right of search options, tap to select which team to search.
    3. Enter your search criteria, including applicable `hashtags <#hashtags>`__.
    4. Tap to apply `search modifiers <#search-modifiers>`__ to your search.

.. tip::
  To access files recently shared in a channel:
  
  - Select the |channel-files-icon| icon below the channel name to access files recently shared in that channel. 
  - Select the channel name, select the **View Info** |channel-info| icon, then select **Files** in the right pane.

Search modifiers
----------------

You can apply search modifiers to any search to reduce the number of results returned. Select a search modifier to add it to the Search field. Supported modifiers are described below. Your search results include messages from all of your teams.

.. image:: ../images/search-modifiers.png

``from:`` and ``in:``
~~~~~~~~~~~~~~~~~~~~~

- Use ``from:`` to find messages or files from specific users. 

  * For example, searching ``from:john.smith`` only returns content from your direct message history with John Smith.

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

- Use ``on:`` to find messages files posted on a specific date. Use the date picker to select a date, or type it in YYYY-MM-DD format.

  * For example, searching ``website on: 2018-09-01`` returns messages or files containing the term ``website`` posted on September 1, 2018.

.. image:: ../images/calendar2.png

Exclusions
~~~~~~~~~~

Use the hyphen ``-`` symbol to exclude terms from your search results. For example, searching ``test -release`` only returns results that include the term ``test`` and exclude the term ``release``.

This exclusion modifier can be used in combination with other modifiers to further refine search results. For example, searching ``test -release -in:release-discussion -from:eric`` returns all results with the term ``test``, excludes posts with the term ``release``, excludes posts made in the ``release-discussion`` channel, and excludes messages sent in direct messages by ``eric``.

Quotation marks
~~~~~~~~~~~~~~~

Use quotation marks ``" "`` to return search results for exact terms. For example, searching ``"Mattermost website"`` returns messages containing the exact phrase ``Mattermost website``, but doesn't return results containing ``Mattermost`` and ``website`` as separate terms.

Wildcards
~~~~~~~~~

Use the asterisk ``*`` symbol for wildcard searches that match within words. For example, searching ``rea*`` returns messages or files containing ``reach``, ``reason``, ``reality``, ``real``, and other words starting with ``rea``.

Hashtags
--------

Hashtags are searchable labels for messages. Anyone can create a hashtag in a message by using the pound sign ``#`` followed by alphanumeric or other unicode characters. Hashtag examples include: ``#bug``, ``#marketing``, ``#user_testing``, ``#per.iod``, ``#check-in``, ``#마케팅``.

Valid hashtags:

- Don't start with a number.
- Are at least three characters long, excluding the ``#``.
- Are made up of alphanumeric or other unicode characters.
- May contain dots, dashes, or underscores.

To search for messages containing hashtags, select a hashtag in an existing post, or type the hashtag (including the pound ``#`` symbol) into the search bar. 

.. note::
  
  Hashtags don't link to channels. If you have a channel named “Marketing”, selecting a ``#marketing`` hashtag does not take you to the Marketing channel. To link to public channels, use the tilde ``~`` symbol followed by the channel name. For example ``~marketing``.

Use sockets for the database
----------------------------


Notes about performing Mattermost searches
-------------------------------------------

- Multiple-word searches return results that contain *all* of your search criteria.
- Search modifiers can help narrow down searches. See the `search modifiers <#search-modifiers>`__ section for details.
- You can search Archived channels as long as you're a member of that channel.

  - If you're unable to see messages or files in archived channels in your search results, ask your system admin if **Allow users to view archived channels** has been disabled under **System Console > Site Configuration > Users and Teams**.
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