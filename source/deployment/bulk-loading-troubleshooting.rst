.. _bulk-loading-troubleshooting:

Troubleshooting
---------------

Running bulk loading tool hangs and doesn't complete
-----------------------------------------------------

If you have Bleve search indexing enabled, temporarily disable it in **System Console > Experimental > Bleve** and run the command again.

Bleve does not support multiple processes opening and manipulating the same index. Therefore, if the Mattermost server is running, an attempt to run the bulk loading tool will lock when trying to open the indeces.

If you are not using the Bleve search indexing, feel free to post in our `Troubleshooting forum <https://mattermost.org/troubleshoot/>`__ for help.
