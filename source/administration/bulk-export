.. _bulk-export:

=================
Bulk Export Tool
=================

Data from one Mattermost instance can be exported in the a `JSONL
<http://jsonlines.org>`_ file for import into another instance using the command line using the `bulk loading feature <https://docs.mattermost.com/deployment/bulk-loading.html>`_. This tool is useful if you have created a server for a proof of concept and have created another server for production use and want to retain the history from the proof of concept instance. 

You can export the following basic data types:

- Version
- Teams
- Channels (Public & Private)
- Users
- Users' Team memberships
- Users' Channel memberships
- Users' notification preferences
- Posts (regular, non-reply posts)

.. include:: bulk-export-data.rst

Running the bulk export command
===============================
The export command runs in the `CLI <https://docs.mattermost.com/administration/command-line-tools.html>`_ and operates in the security context of the CLI.  It has permissions to access all information in the Mattermost database. 

To run the export command: 

1.  Navigate to the directory where the Mattermost server is installed. On a default install of Mattermost, the directory is ``/opt/mattermost/bin``.
2.  Run the following command to extract data from all teams on the server. Note that you can change the file name if you desire: 
  
  ``sudo ./mattermost export bulk --all-teams file.json'''
  
3.  Retrieve your file from your local storage location configured at **System Console > Files > Storage > Local Storage Directory**.  Your data will be located in the ``./exports/`` folder

