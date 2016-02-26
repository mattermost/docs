# Searching
_____
The search box in Mattermost returns non-case sensitive results from any channel of which you’re a member. Use search modifiers to narrow your search results. Click **Jump** on the right of a search result to view that post in the channel archive.

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

## Search Notes and Limitations

- Multiple search terms are connected with “OR” by default. Typing in `Mattermost website` returns results containing “Mattermost” or “website”
- Search in Mattermost uses the full text search features included in either a MySQL or Postgres database. 
- Special unsupported cases:
    - There are a number of stop words that will return no results because the words are too frequently used to provide meaningful search results. See a full list of stop words for [MySQL](http://dev.mysql.com/doc/refman/5.7/en/fulltext-stopwords.html) and [Postgres](http://apt-browse.org/browse/ubuntu/precise/main/i386/postgresql-9.1/9.1.3-2/file/usr/share/postgresql/9.1/tsearch_data/english.stop) databases.
    - Searching for IP addresses, for example `10.100.200.101`, is currently unsupported.
    - Two letter searches and common words like "this", "a" and "is" will not appear in search results
    - Chinese characters may not return exact matches. Try adding `*` to the end of queries to run a wildcard search.
    - Wildcard searches on Postgres databases are currently unsupported.
