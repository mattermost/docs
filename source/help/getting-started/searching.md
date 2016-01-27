# Searching
_____
The search box in Mattermost returns results from any channel of which you’re a member. Use search modifiers to narrow your search results. Click **Jump** on the right of a search result to view that post in the channel archive.

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

## Search Notes and Limitations

- Multiple search terms are connected with “OR” by default. Typing in `Mattermost website` returns results containing “Mattermost” or “website”
- Search in Mattermost uses the full text search features included in either a MySQL or Postgres database.
- Special unsupported cases:
    - Searching for IP addresses, for example `10.100.200.101`, is currently unsupported.
    - Two letter searches and common words like "this", "a" and "is" will not appear in search results
    - Chinese characters may not return exact matches. Try adding `*` to the end of queries to run a wildcard search.
