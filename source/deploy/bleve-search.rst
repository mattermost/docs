Bleve Search (Experimental)
===========================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Bleve is a search engine that uses Lucene-style full-text search and indexing. This style of search and indexing helps overcome limitations of the default database search such as challenges with characters and advanced search capabilities.

The Bleve search engine works as a library integrated into the Mattermost codebase. As it generates indexes in the filesystem of the server that it is running on, it doesn’t require an external server to function. Because of this, Bleve should not be enabled in High Availability deployments.

.. note::

  From Mattermost v6.1, Bleve search uses the scorch index type on newly created indexes which features efficiency improvements and indexes that use significantly less disk space. 
  
  To use this new type of index, after upgrading Mattermost Server to version to v6.1 or later, go to **System Console > Experimental > Bleve**, then run a purge operation by selecting **Purge Index**, followed by a reindex by selecting **Index Now**. Bleve remains compatible with existing indexes, so currently indexed data will continue to work if a purge and reindex isn't run.

Configuring Bleve in Mattermost
-------------------------------

Follow these steps to configure the Mattermost server to use Bleve and generate required indexes. Once the configuration is saved, new posts made to the database will be automatically indexed with Bleve.

**Note:** During indexing, search results may be incomplete until the indexing job is complete.

1. Open **System Console > Experimental > Bleve**.
2. Set **Enable Bleve Indexing** to **true** to enable the other settings on the page.
3. Set the directory path to use for storing bleve indexes (e.g.: ``/var/opt/mattermost/bleveindexes``). The user running Mattermost should have permissions to access the directory. See our `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html#bleve-settings>`__  documentation for details.
4. Save the configuration.
5. Select **Index Now**. All users, channels, and posts in the database will be indexed oldest to newest.
6. Set **Enable Bleve for search queries** to **true**.
7. Set **Enable Bleve for autocomplete queries** to **true**.

.. note::

  Search results for files shared before upgrading to Mattermost Server v5.35 may be incomplete until an extraction command is run using the `CLI <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-extract-documents-content>`__, or using the `mmctl <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-extract>`__. After running this command, the search index must be rebuilt. Go to **System Console > Experimental > Bleve > Bulk Indexing**, then select **Index Now** to rebuild the search index to include older file contents.

Using Bleve Search
------------------

The following conditions are applied when using Bleve search:

* **Unquoted terms:** Search terms that contain non-alphanumeric characters/special characters outside of quotation marks are removed. For example, using ``abcd "**" && abc`` as a search term will return results for a search for ``abcd "**" abc`` as the ``&&`` characters weren't within the quotation marks.
* **Wildcard search:** Wildcard search (e.g., ``abc*``) is supported.
