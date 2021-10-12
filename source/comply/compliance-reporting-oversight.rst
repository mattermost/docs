Compliance Reporting and Oversight
==================================

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Mattermost Enterprise Edition E20*

.. important::
   
   This feature has been replaced by a new :doc:`Compliance Export feature <compliance-export>`, and has been removed from Mattermost v6.0. We recommend migrating to the new system. For a sample CSV output of the new compliance export system, `download a CSV export file here <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip>`__.

This feature enables compliance exports to be produced from the System Console, with all query and download actions logged in an audit history to enable oversight and prevent unauthorized queries.

Compliance exports can be filtered to date range, user account, and keyword list. Requests from queries can be downloaded from the user interface in ``.csv`` format, with a ``.json`` metafile documenting the query, as well as placed in a directory set by the System Admin.

Daily compliance reports may also be generated, supporting integration with compliance solutions like `Global Relay <#global-relay-support>`__.

By default, all Mattermost Editions retain all messages, including edits and deletes, along with all files uploaded.

Enabling Compliance Reporting 
-----------------------------

To enable the option to generate daily compliance reports:

1. Go to **System Console > Compliance > Compliance Monitoring** and set the **Enable Compliance Reporting** value to **true**.
2. (Optional) In **Compliance Report Directory** specify the directory in which to place completed compliance reports. Defaults to ``./data/`` if left blank.
3. Select **Save**.

Turn on Daily Compliance Reports 
--------------------------------

After enabling compliance reporting: 

1. Go to **System Console > Compliance > Compliance Monitoring** and set the **Enable Daily Report** value to **true**.
2. Select **Save**. 

Your system will now export all new messages posted within a 24-hour period as a ``.csv`` file to the location specified in **Compliance Report Directory**. This feature can be used in conjunction with centralized compliance reporting systems that move.

Run Compliance Reports  
----------------------

Compliance reports are exports of all messages in Mattermost that match the report criteria. To run a report:

1. Go to **System Console > Compliance > Compliance Monitoring**.
2. Fill in the following:

     - **Job Name:** Name the compliance report you are about to run (e.g. "HR Audit 455").
     - **From:** Start date for search in YYYY-MM-DD format (e.g. "2016-03-11").
     - **To:** End date of search in YYYY-MM-DD format (e.g. "2016-05-11").
     - **Emails:** Comma-separated list of email addresses of users whose posted messages you want to search (e.g. ``bill@example.com, bob@example.com``).
     - **Keywords:** Indicate the words that would be contained in a message for it to be included in the compliance report results.
3. Select **Run Compliance Report**.

The report will be queued in the display below the fields described above. The properties of each compliance report run is explained as follows: 

- **Timestamp:** Time at which the report was requested.
- **Status:** ``running`` indicates the report is being run; ``finished`` indicates the report is complete and ready for download.
- **Records:** Shows the number of search results.
- **Type:** ``adhoc`` indicates the report was requested by completing query fields; ``daily`` indicates the report is a daily export.
- **Description:** Job Name indicated in request.
- **Requested by:** Email of person requesting the report.
- **Params:** Parameters of the compliance report request.

Each compliance report includes a **Download** link which downloads a compressed file named ``adhoc-[UNIQUE_ID].zip``. Inside the file is ``meta.json``, which includes the parameters of the search executed and ``posts.csv`` which includes the contents of messages found by the request.

Compliance query definition stored in ``meta.json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``meta.json`` file contains the following information about the compliance query:

+---------------------+---------------------------------------------------------------+-----------------------------------+
| Field               | Description                                                   | Example                           |
+=====================+===============================================================+===================================+
| id                  | Unique identifier for compliance query                        | ja8z8egap7nq9kqetz3rt98khe        |
+---------------------+---------------------------------------------------------------+-----------------------------------+
| create_at           | Timestamp at which compliance query was executed              | 1463637842478                     |
+---------------------+---------------------------------------------------------------+-----------------------------------+
| user_id             | Mattermost User ID for person creating query                  | 3bq1shta93yztg3i6aiu1tzi5h        |
+---------------------+---------------------------------------------------------------+-----------------------------------+
| status              | Status of query: *finished* or *failed*                       | "finished"                        |
+---------------------+---------------------------------------------------------------+-----------------------------------+
| count               | Count of messages found matching keyword                      | 36                                |
+---------------------+---------------------------------------------------------------+-----------------------------------+
| desc                | User entered description of compliance query                  | Example Compliance Report         | 
+---------------------+---------------------------------------------------------------+-----------------------------------+
| type                | Type of compliance query: *adhoc* or *daily*                  | "adhoc"                           | 
+---------------------+---------------------------------------------------------------+-----------------------------------+
| start_at            | Timestamp at which query began to run                         | 1451606400000                     | 
+---------------------+---------------------------------------------------------------+-----------------------------------+
| end_at              | Timestamp at which query ended                                | 1463529600000                     | 
+---------------------+---------------------------------------------------------------+-----------------------------------+
| keywords            | Comma-separated, case insensitive keywords to match in query  | "drinking"                        | 
+---------------------+---------------------------------------------------------------+-----------------------------------+
| emails              | Comma-separated emails of users to search. Blank returns all  | ``frank.yu@ha.ca, mary.li@hi.co`` |  
+---------------------+---------------------------------------------------------------+-----------------------------------+

Compliance query results stored in ``posts.csv`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``posts.csv`` contains the following information about the compliance query results, one search result per row:

+---------------------+---------------------------------------------------------------+-------------------------------+
| Field               | Description                                                   | Example                       |
+=====================+===============================================================+===============================+
| TeamName            | URL name of team                                              | contosi                       |
+---------------------+---------------------------------------------------------------+-------------------------------+
| TeamDisplayName     | Display name of team                                          | Contosi Corporation           | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| ChannelDisplayName  | Display name of channel where keyword was found               | Community Heartbeat           | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| ChannelName         | URL name of channel                                           | community-heartbeat           | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| UserUsername        | Username of user posting the message containing keyword       | frank.yu                      |
+---------------------+---------------------------------------------------------------+-------------------------------+
| UserEmail           | Email of user posting the message containing keyword          | "frank.yu@contosi.com"        | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| UserNickname        | Nickname of user posting the message containing keyword       | fan du                        | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| UserType            | Type of user posting the message ("user" or "bot")            | user                          |
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostId              | Unique ID of message post containing keyword                  | xt9anyx6x3fx9y84aehgakdpze    | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostCreateAt        | Timestamp at which post was created                           | 2016-03-02T16:01:59Z          | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostDeletedAt       | Timestamp at which post was deleted (if applicable)           | 2016-03-02T16:01:59Z          | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostUpdatedAt       | Timestamp at which post was last edited (if applicable)       | 2016-03-02T16:01:59Z          | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostParentId        | Unique ID of parent post if post is a comment                 | xt9anyx6x3fx9y84aehgakdpze    | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostOriginalId      | Unique ID of post if deleted or edited                        | xt9anyx6x3fx9y84aehgakdpze    | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostMessage         | Message containing keyword                                    | Drinking from the fire hose   | 
+---------------------+---------------------------------------------------------------+-------------------------------+
| PostFilenames       | Comma separated list of filesnames attached to post           | ["/f../ho.png","/f../hi.png"] |
+---------------------+---------------------------------------------------------------+-------------------------------+

Global Relay Support
--------------------

Mattermost daily compliance reports are compatible with Global Relay compliance solutions through the conversion of Mattermost ``.CSV`` exports into Global Relay ``EML`` files.

- This conversion can be done by in-house developers who have previously written scripts to convert other communication systems into Global Relay format based on your organization's specific needs.
- You can also contact your Global Relay account manager about a services project to establish this conversion.

We recommend using the new :doc:`Compliance Export feature <compliance-export>` for Global Relay exports.
