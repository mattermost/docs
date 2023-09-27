Troubleshooting high scale deployments
=======================================

This page provides troubleshooting guidance for high scale Mattermost deployments with 100 users or more.

If these steps do not resolve the issue, and you have a `paid subscription to a Mattermost offering </about/editions-and-offerings.html>`_, please reach out to our customer support team via our `online support portal <https://support.mattermost.com/hc/en-us/requests/new>`_. 

Additionally, peer-to-peer support is available for all Mattermost users in our `troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot>`__ and on our `community server <https://community.mattermost.com/core/channels/peer-to-peer-help>`_. 

My system keeps hanging when I search for a message in Mattermost
---------------------------------------------------------------------

First, check how many messages have been posted on your system, including deleted posts and posts made using automations.

Go to the **System Console > Reporting > Site Statistics** and review the **Total Posts** figure reported. If this figure is above 3,000,000 posts, we recommend deploying Elasticsearch alongside your Mattermost server for improved search performance. Follow our guides to `deploy an Elasticsearch server </scale/elasticsearch.html>`__.

How to troubleshoot server-side performance issues without Prometheus or Grafana?
-----------------------------------------------------------------------------------

Enable slow query logging in PostgreSQL and leave it enabled to gather data over time. PostgreSQL's slow query log helps you identify queries that take longer than a specified amount of time. The slow query log isn't enabled by default, and must be enabled manually.

To enable slow query logging globally, change the following line in ``postgresql.conf``: ``log_min_duration_statement = 1000``, then restart PostgreSQL. When you this value to ``1000``, PostgreSQL considers queries that take longer than 1 second to be slow queries and logs them in the log file. Alternatively, you can run ``SELECT pg_reload_conf();`` to reload the configuration without a restart.

To enable slow query logging for a specific database, use ``ALTER DATABASE`` to change the configuration parameter for a single database. 