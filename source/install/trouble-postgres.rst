PostgreSQL installation troubleshooting
=======================================

Mattermost supports PostgreSQL v10+.

PostgreSQL v15 introduces changes that may affect compatibility with previous releases. In order to ensure compatability, take note of the following recommendations:

- Remove the ``PUBLIC`` creation permission on the public schema.
- For existing databases, especially those having multiple users, consider revoking ``CREATE`` permission on the public schema to adopt this new default.
- For new databases which have no need to defend against insider threats, granting ``CREATE`` permission will yield the behavior of prior releases.

PostgresSQL full-text search fails to use indexes with non-english ``default_text_search_config``
------------------------------------------------------------------------------------------------

Some of the tables in Mattermost, like ``Posts`` or ``Users``, contain GIN indexes to improve the database full-text search feature in PostgreSQL.

- These indexes need to be built against a specific language, and when they're created they're hard-coded to English.
- For the full-text search feature to leverage the indexes, the language specified in the query needs to match the language specified in the index.
- Full-text search queries are always performed using the ``default_text_search_config`` database setting.
- If the ``default_text_search_config`` is not set to ``english``, the GIN indexes will not be used.
- Database administrators can work around this by dropping the specific GIN index they're interested in and rebuilding it with the value of ``default_text_search_config``.
- For example, if the default language of your server is Spanish:

```sql
# Create the new index with a new name before dropping the old one
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_posts_message_txt_spanish ON posts USING gin(to_tsvector('spanish', message));
# Check that the new index does work. If it does, drop the old one and rename the new one:
DROP INDEX CONCURRENTLY IF EXISTS idx_posts_message_txt;
ALTER INDEX idx_posts_message_txt_spanish RENAME TO idx_posts_message_txt;
```
