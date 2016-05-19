Compliance exports with oversight protection 
----

Available in `Enterprise Edition E20 <https://about.mattermost.com/pricing/>`_

Turning on this feature enables compliance exports to be produced from the System Console with each export and download action logged in an audit history to enable oversight and prevent unauthorized queries. 

Compliance exports can be filtered to date range, user account, and keyword list and requests from queries can be downloaded from the user interface in .csv format, with a .json metafile documenting the query, as well as placed in a pre-defined directory. 

Each export and each download action taken from the user interface is recorded in an audit log, including the user account taking the action, the action and a datetime stamp. 

An option is also available to generate compliance reports on a daily basis.

Enabling Compliance Reporting 
====

After purchasing and installing a license key for Enterprise Edition E20: 

1. Go to System Console > Compliance Settings > Enable Compliance and set the value to ``true``.
2. (Optional) In Compliance Directory Location specify the directory in which to place completed compliance reports. Defaults to ``./data/`` if left blank.
3. Click **Save**. 

This will enable Compliance Reports to be run from the System Console > OTHER > Compliance and Auditing tab, as well as enable the option to generate Daily Compliance Reports.

Turn on Daily Compliance Reports 
====

After enabling compliance reporting: 

1. Go to System Console > Compliance Settings > Enable Daily Report and set the value to ``true``.
2. Click **Save**. 

Your system will now export all new messages posted within a 24-hour period as a .csv file to the location specified in **Compliance Directory Location**. This feature can be used in conjunction with centralized compliance reporting systems that move 

Run Compliance Reports  
====

Compliance Reports are exports of all messages in Mattermost matching the report criteria. To run a report: 

1. Go to System Console > Compliance and Auditing
2. Fill in the following criteria:  
     - Job Name: Name the compliance report you are about to run, e.g. "HR Audit 455".
     - From: Start Date for search in YYYY-MM-DD format, e.g. "2016-03-11".
     - To:End Date of search in YYYY-MM-DD format, e.g. "2016-05-11".
     - Emails: Comma separated list of email addresses of users who's posted messages you want to search. e.g. "bill@example.com, bob@example.com".
     - Keywords: Indicate the words that would be contained in a message for it to be included in the Compliance Report results.
3. Click "Run Compliance Report" 

The report will be queued in the display below the fields described above. The properties of each Compliance Report run is explained as follows: 

- Timestamp: Time at which the report was requested.  
- Status: `running` indicates the report is being run. `finished` indicates the report is complete and ready for download.
- Records: Shows the number of search results.
- Type: `adhoc` indicates the report was requested by completing query fields, `daily` indicates the report is a daily export (see above section for description). 
- Description: Job Name indicated in request.
- Requested by: Email of person requesting the report.
- Params: Parameters of the compliance report request. 

Each Compliance Report includes a "Download" link which downloads a compressed file named ``adhoc-[UNIQUE_ID].zip``. Inside the file is `meta.json`, which includes the parameters of the search executed and `posts.csv` which includes the contenst of messages found by the request. 

Example of the contents of ``meta.json``:

{
    "id": "ja8z8egap7nq9kqetz3rt98khe",
    "create_at": 1463637842478,
    "user_id": "3bq1shta93yztg3i6aiu1tzi5h",
    "status": "",
    "count": 0,
    "desc": "HR Audit 388",
    "type": "adhoc",
    "start_at": 1451606400000,
    "end_at": 1463529600000,
    "keywords": "drinking",
    "emails": "person@example.com"
}

For each post found, the following information is available: 

- TeamName	
- TeamDisplayName	
- ChannelName	
- ChannelDisplayName	
- UserUsername	
- UserEmail	
- UserNickname	
- PostId	
- PostCreateAt	
- PostUpdateAt	
- PostDeleteAt	
- PostRootId	
- PostParentId	
- PostOriginalId	
- PostMessage	
- PostType	
- PostProps	
- PostHashtags	
- PostFilenames
