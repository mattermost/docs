# Support Handbook

## Database Issues

Questions to ask when providing support for database issues.

__IMPORTANT: Before asking for any database queries to be run, suggest a back-up is completed to prevent accidental data loss or corruption.__

#### PostgreSQL or MySQL?
Find out which database they are using. We only support PostgreSQL and MySQL currently.

If they're using Amazon Aurora MySQL, and their issue seems like a race condition, it might be due to the multi-region lag that Aurora can have. If this is the case there may be a race in code we need to fix. @christopher will know more.

#### What is the database version?
Make sure it's a [version we support](https://docs.mattermost.com/install/requirements.html#database-software). If we don't support it, ask them to use a version we do support.

#### Read replicas?
Check if they have any read replicas set up. If these are misconfigured, it could be the source of some issues, such as rows not being propagated to the replicas and looking like missing/old data to a user.

If the read replicas are not being used, make sure they have an enterprise license uploaded.

#### Connection errors?
If their Mattermost server is unable to connect to the database, make sure the connection string being used is correct. It could also be a networking issue where the database isn't on the same network or the right ports are not open.

#### Other
If they are receiving a specific error from the database, try using that to troubleshoot the issue.
