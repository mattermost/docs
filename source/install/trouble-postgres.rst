PostgreSQL installation troubleshooting
=======================================

Mattermost supports PostgreSQL v10+.

PostgreSQL v15 introduces changes that may affect compatibility with previous releases. If you're deploying a fresh installation of Postgres v15, run this command: ``GRANT CREATE ON SCHEMA public TO PUBLIC`` to ensure that you can use Mattermost.

PostgresSQL full-text search fails to use indexes with non-english ``default_text_search_config``
------------------------------------------------------------------------------------------------

Mattermost uses ``default_text_search_config`` for full-text search in PostgresSQL databases, as opposed to a hardcoded text search config. However, indexes are still created with a hardcoded text search config (english) and as a result, full-text search may never use the indexes.

Some of the tables in Mattermost, like ``Posts`` or ``Users``, contain GIN indexes to improve the database full-text search feature in PostgreSQL.

These indexes need to be built against a specific language, and when they're created they're hard-coded to English. Full-text search queries are always performed using the ``default_text_search_config`` database setting. In order for the full-text search feature to leverage the indexes, the language specified in the query needs to match the language specified in the index.

If the ``default_text_search_config`` is not set to ``english``, the GIN indexes will not be used. Database administrators can work around this by dropping the specific GIN index they're interested in and rebuilding it with the value of ``default_text_search_config``.

For example, if the default language of your server is Spanish:

```sql
# Create the new index with a new name before dropping the old one
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_posts_message_txt_spanish ON posts USING gin(to_tsvector('spanish', message));
# Check that the new index does work. If it does, drop the old one and rename the new one:
DROP INDEX CONCURRENTLY IF EXISTS idx_posts_message_txt;
ALTER INDEX idx_posts_message_txt_spanish RENAME TO idx_posts_message_txt;
```
