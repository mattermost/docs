Bleve Search (Experimental)
===========================

Bleve is a search engine that uses Lucene-style full-text search and indexing. This style of search and indexing helps overcome limitations of the default database search such as challenges with characters and advanced search capabilities. 

The Bleve search engine works as a library integrated into the Mattermost codebase. As it generates indexes in the filesystem of the server that it is running on, it doesn’t require an external server to function. Because of this, Bleve should not be enabled in High Availability deployments.

Configuring Bleve in Mattermost
------------------------------

Follow these steps to configure the Mattermost server to use Bleve and generate required indexes. Once the configuration is saved, new posts made to the database will be automatically indexed with Bleve.

**Note:** During indexing, search results may be incomplete until the indexing job is complete.

1. Open **System Console > Experimental > Bleve**.
2. Set **Enable Bleve Indexing** to **true** to enable the other settings on the page. 
3. Set the directory path to use for storing bleve indexes (e.g.: ``/var/opt/mattermost/bleveindexes``). The user running Mattermost should have permissions to access the directory.
4. Save the configuration.
5. Click the **Index Now** button. All users, channels, and posts in the database will be indexed oldest to newest.  
6. Set **Enable Bleve for search queries** to **true**.
7. Set **Enable Bleve for autocomplete queries** to **true**.
