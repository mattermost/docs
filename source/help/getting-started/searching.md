# Searching
_____

The search box in Mattermost returns search results from any channel of which you’re a member. 

- Searching multiple words returns results with any one of the words listed. 
- When results appear, click the **Jump** link to view that post in the channel archive.
- You can expand the search results window by clicking the "Expand" button in the top right corner. 
- Use search modifiers, like `from:dave`, to return results only from certain people or in certain channels (see below)

Like many search engines, highly common words like `the`, `which`, `are` (known as "stop words"), as well as two-letter and one-letter search terms, are not shown in search because they typically return too may results. 

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

Other notes: 

- IP addresses, for example `10.100.200.101`, do not return results.

## Technical Notes

### Searching Chinese, Korean and Japanese
- The best experience for searching in Chinese, Korean and Japanese is to use MySQL 5.7.6 or later with special configuration. Please see [documentation](https://docs.mattermost.com/install/i18n.html).
- You can search to some degree without this configuration by adding `*` to the end of search terms. 

### Differences between MySQL and Postgres search 

By default, Mattermost uses full text search support included in MySQL and PostgreSQL. These databases have slightly different search behavior. Check **Main Menu** > **About Mattermost** to see which database you're using.

For example, different databases have different "stop words" filtered out of search results. See database documentation on [MySQL](http://dev.mysql.com/doc/refman/5.7/en/fulltext-stopwords.html) and [Postgres](http://apt-browse.org/browse/ubuntu/precise/main/i386/postgresql-9.1/9.1.3-2/file/usr/share/postgresql/9.1/tsearch_data/english.stop) for a full list. Other differences include: 

PostgreSQL: 
- Email addresses do not return results.
- Hashtags or recent mentions of usernames containing a dash do not return search results.
- Terms containing a dash return incorrect results as dashes are ignored in the search engine.

MySQL 
- Hashtags or recent mentions of usernames containing a dot do not return search results.

    
