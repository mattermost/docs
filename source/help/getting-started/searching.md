# Searching
_____
The search box in Mattermost returns non-case sensitive results from any channel of which you’re a member. Use search modifiers to narrow your search results. Click **Jump** on the right of a search result to view that post in the channel archive.

It is also possible to expand the right-hand sidebar to make search results easier to read by clicking on the expand/collapse icon with two arrows in the top right corner of the sidebar. 

## Search Modifiers

#### From: and In:
Use `from:` to find posts from specific users and `in:` to find posts in specific channels. 

- For example: Searching `Mattermost in:town-square` only returns messages in Town Square that contain `Mattermost`.

#### “Quotation Marks”
Use quotation marks to return search results for exact terms. 

- For example: Searching `"Mattermost website"` returns messages containing the entire phrase `Mattermost website` and not messages containing only `Mattermost` or `website`.

#### Wildcard* 
Use the `*` character for wildcard searches that match within words.

- For example: Searching for `rea*` brings back messages containing `reach`, `reason` and other words starting with `rea`.

## Hashtags

Hashtags are searchable labels for posts. Search for any posts containing a hashtag by clicking the hashtag in an existing post or typing the hashtag with the pound symbol into the search bar. Create hastags in any post by using the pound sign `#` followed by alphanumeric characters.

Valid hastags:
- Start with a letter
- End with any alphanumeric character (letter or number)
- Are at least 3 characters long, not including the `#` 
- May contain dots, dashs or underscores

Examples:
`#bug`, `#marketing`, `#v2.1`, `#user_testing`, `#per.iod`, `#check-in`

Hashtags do not link to channels. For example, if you have a channel named "Marketing", clicking a `#marketing` hashtag does not redirect you to that channel.

## Search Notes and Known Issues

- Search in Mattermost uses the full text search features included in either a MySQL or Postgres database. To determine what database is being used, go to the **Main Menu** > **About Mattermost** and look for the database type.
- Multiple search terms are connected with “AND” by default. Typing in `Mattermost website` returns results containing “Mattermost” and “website”.
- Deployments requiring searching in Chinese, Japanese and Korean languages require MySQL 5.7.6+ and the configuration of [ngram Full-Text parser](https://dev.mysql.com/doc/refman/5.7/en/fulltext-search-ngram.html). See [CJK discussion](https://github.com/mattermost/platform/issues/2033#issuecomment-183872616) for details.
- Unsupported cases:
    - Stop words will return no results because the words are used too frequently. See a full list of stop words for [MySQL](http://dev.mysql.com/doc/refman/5.7/en/fulltext-stopwords.html) and [Postgres](http://apt-browse.org/browse/ubuntu/precise/main/i386/postgresql-9.1/9.1.3-2/file/usr/share/postgresql/9.1/tsearch_data/english.stop) databases.
    - Two letter searches do not return results.  
- Known Issues:
    - Postgres and MySQL databases:
        - Chinese characters may not return exact matches. Try adding `*` to the end of queries to run a wildcard search.
        - IP addresses, for example `10.100.200.101`, do not return results.
    - Postgres databases:
        - Email addresses do not return results.
    - MySQL databases:
        - Hashtags or recent mentions of usernames containing a dot do return search results.

    
