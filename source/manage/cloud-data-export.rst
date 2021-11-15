Changing Deployment Types
==========================

This document outlines the process for migrating from Mattermost Cloud to Mattermost self-hosted. In the future, a process for migrating from Mattermost self-hosted to Mattermost Cloud will also be documented and provided here.

Migrating from Cloud to self-hosted
-----------------------------------

If, after completing your 14-day free Cloud trial, you've decided to self-host your own Mattermost deployment, you may want to migrate your Cloud data to your self-hosted instance.

Using the mmctl CLI tool, you can export your channels, messages, users, and files, and store those exported files locally.

How does the process work?
--------------------------

Before you export and migrate your data, you must `install Mattermost <https://docs.mattermost.com/guides/deployment.html#install-guides>`_ on the server you’ll be using to run Mattermost.

The migration is done using the mmctl tool which is a remote CLI tool for Mattermost that's installed locally and uses the Mattermost API. Authentication is done with either login credentials or an authentication token. If you haven’t used mmctl before, first `install mmctl <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#install-mmctl>`_ then read the `mmctl usage notes <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-usage-notes>`_ before you get started.

Once you've installed mmctl, you'll be using the `mmctl export <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-export>`__ commands to export your Cloud data for channels, messages, users, etc. The export file is downloaded to a location specified in the export commands. Once the export is complete, you'll import the data into your self-hosted instance.

.. note::
  
  The export process doesn’t include integrations or any custom data. Other aspects of your instance, such as specific security settings and requirements, are also not included. For assistance with migrating additional data and settings, see our support options: https://mattermost.com/support/.

Log into your Cloud instance and run the following mmctl command: 

.. code:: none

   mmctl export create --attachments [flags]. 

Ensure you set **attachments** to **true** to include file attachments - this creates a zip file of your Mattermost data.

Next, download the export file by running the following mmctl command:

.. code::

   mmctl export download [exportname] [filepath] [flags]

.. note::

  You can indicate the name of the export and its destination path ``$ mmctl export download samplename sample_export.zip``. If you only indicate the name, the path
  will match: ``$ mmctl export download samplename``.

When the file download is complete, log into your Mattermost server. Run the following mmctl command to import your data to your Mattermost server:

.. code::
  
   mmctl import upload [filepath] [flags]. 
   
Then extract the file to use it by running the following mmctl command:

.. code::
   
   mmctl extract run [flags].

Once your migration is complete and you’ve imported your data into your self-hosted instance. We recommend that you take a few days to validate your data and ensure everything is working as expected before taking down your Cloud instance.

If you encounter any issues or problems, please contact our Support team via https://customers.mattermost.com/cloud/contact-us, or through the `Mattermost Help Center <https://support.mattermost.com/>`_.
