.. _bulk-export:

=================
Bulk Export Tool
=================

Data from one Mattermost instance into another can be exported in the `JSONL
<http://jsonlines.org>`_ file using the `bulk loading feature <https://docs.mattermost.com/deployment/bulk-loading.html>`_. This tool is useful if you have created a server for a proof of concept, have created another server for production use and now want to retain the history from the proof of concept instance.

You can export the following data types:

- Teams
- Channels (Public & Private)
- Users
- Users' Team memberships
- Users' Channel memberships
- Posts (Posts in the Public/Private channels and also replies to those posts)

.. include:: bulk-export-data.rst

Running the bulk export command
===============================
The export command runs in the `CLI <https://docs.mattermost.com/administration/command-line-tools.html>`_.  It has permissions to access all information in the Mattermost database. 

To run the export command: 

1.  Navigate to the directory where the Mattermost server is installed. On a default install of Mattermost, the directory is ``/opt/mattermost/bin``.
2.  Run the following command to extract data from all teams on the server. Note that you can change the file name and specify an absolute or relative path to dictate where the file is exported. 
  
  ``sudo ./mattermost export bulk --all-teams file.json``

  ``sudo ./mattermost export bulk --all-teams /home/user/bulk_data.json``
  
3.  Retrieve your file from the location you specified.  

