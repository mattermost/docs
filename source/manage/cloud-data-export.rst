Mattermost Workspace Migrations: Moving Workspaces Between the Cloud and Your Own Datacenter
=============================================================================================

This document outlines the process for migrating from Mattermost Cloud to Mattermost self-hosted. In the future, a process for migrating from Mattermost self-hosted to Mattermost Cloud will also be documented and provided here.

The first thing you should know is that migrating a Mattermost Workspace between two installations is the same process regardless as to whether the source or destination of the migration is in the Cloud or self-hosted. **These steps will work for any Mattermost instance**, as long as the instances involved have a version of Mattermost later than 5.33.

Migrating from Cloud to self-hosted
-----------------------------------

If, after completing your 14-day free Cloud trial, you've decided to self-host your own Mattermost deployment, you may want to migrate your Cloud data to your self-hosted instance.

Using the mmctl CLI tool, you can export your channels, messages, users, and files, and store those exported files locally.

How does the process work?
--------------------------

Before you export and migrate your data, you must `install Mattermost <https://docs.mattermost.com/guides/deployment.html#install-guides>`_ on the server you’ll be using to run Mattermost.

The migration is done using the mmctl tool which is a remote CLI tool for Mattermost that's installed locally and uses the Mattermost API. Authentication is done with either login credentials or an authentication token. If you haven’t used mmctl before, first `install mmctl <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#install-mmctl>`_ then read the `mmctl usage notes <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-usage-notes>`_ before you get started. ``mmctl`` works over the network, so download the newest release from [the releases page](https://github.com/mattermost/mmctl/releases/tag/v6.1.0) and place the binary on your ``PATH`.

Once you've installed mmctl, you'll be using the `mmctl export <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-export>`__ commands to export your Cloud data for channels, messages, users, etc. The export file is downloaded to a location specified in the export commands. Once the export is complete, you'll import the data into your self-hosted instance.

.. note::
  
  The export process doesn’t include integrations or any custom data. Other aspects of your instance, such as specific security settings and requirements, are also not included. For assistance with migrating additional data and settings, see our support options: https://mattermost.com/support/.

Now that you have `mmctl` installed, we can generate the export from the source instance. 

Authenticate
------------

First, use your administrator credentials to log into the instance with `mmctl`, replacing `example-source-domain.com` with the network address of the source instance:

.. code::

   $ mmctl auth login https://example-source-domain.com
   
``mmctl`` will prompt you for a username (use your admin user), password, and for a connection name, which can be anything you want, just to identify this set of credentials in the future, for your convenience. Then you will be able to start the export process:

Create the Export
-----------------

.. code::

   $ mmctl export create --attachments

This will create a full export of the server, and include attached files. Leave out ``--attachments`` if you do not wish to export attached files from your instance. This process can take some time, so ``mmctl`` will return immediately, and the job will run in the background on the Mattermost instance until the export is fully created. If successful, the command will immediately output a job ID, like this:

.. code::

   Export process job successfully created, ID: yfrr9ku5i7fjubeshs1ksrknzc

While the job is running, its status can be checked using the ID that was provided when it was created, and when it is done the output will look similar to this:

.. code::

  $ mmctl export job show yfrr9ku5i7fjubeshs1ksrknzc
    ID: yfrr9ku5i7fjubeshs1ksrknzc
    Status: success
    Created: 2021-11-03 10:44:13 -0500 CDT
    Started: 2021-11-03 10:44:23 -0500 CDT

Download the export
-------------------

Once the status is `success`, you can download the export onto your local machine. First, discover the name of the completed export file with `mmctl export list`:

.. code::

   $ mmctl export list
   r3kcj8yuwbramdt714doafi3oo_export.zip

This will show all of the exports on the server, so be sure to download the latest one and to delete it when you're done to save storage. Download the file with a command like the following, but with the filename of the export on your server:

.. code::

   $ mmctl export download r3kcj8yuwbramdt714doafi3oo_export.zip

Upload the export to the new server
-----------------------------------

Finally, it is time to take our export from the source server and use it as an import into the destination server. For clarity, the file exported from the source server will be referred to as "the archive" for the rest of the article, in order to avoid confusion about whether it is an export or an import (since it's both). First, log into the destination server with `mmctl` the same way you logged into the source server:

.. code::

   $ mmctl auth login https://my-destintation-server.example

Use the following command to upload the archive to the destination server. The upload may take awhile, depending upon Internet speeds, and when the upload is complete the command will return with the ID of the import

.. code::
  
   mmctl import upload r3kcj8yuwbramdt714doafi3oo_export.zip
   Upload session successfully created, ID: cfuq6q9kkjrqfgnph1pew3db4e
   Import file successfully uploaded, name: xrzs9wrzufntbfcxpy39mdq9hy

Complete the import into the new server
---------------------------------------

.. code::

   $ mmctl import list available
   cfuq6q9kkjrqfgnph1pew3db4e_r3kcj8yuwbramdt714doafi3oo_export.zip

Run the import job to process to actually import the archive into the server. This process, like export, can take awhile. First, start the import process:

.. code::
   
   $ mmctl import process cfuq6q9kkjrqfgnph1pew3db4e_r3kcj8yuwbramdt714doafi3oo_export.zip

Once you've marked the file for processing, you can check the status of the job using ``mmctl import job list``:

.. code::

  $ mmctl --local import job list
    ID: f93jxu1hzty79enwa1xy6f1tbr
    Status: pending
    Created: 2021-10-28 13:32:55 +0200 CEST

When the job is complete, the ``success`` status is displayed:

.. code::

  $ mmctl --local import job list
    ID: f93jxu1hzty79enwa1xy6f1tbr
    Status: success
    Created: 2021-10-28 13:32:55 +0200 CEST
    Started: 2021-10-28 13:33:05 +0200 CEST

Then extract the file to use it by running the following mmctl command:

.. code::
   
   mmctl extract run [flags].

Once your migration is complete and you’ve imported your data into your self-hosted instance we recommend that you take a few days to validate your data and ensure everything is working as expected before taking down your Cloud instance.

If you encounter any issues or problems, please contact our Support team via https://customers.mattermost.com/cloud/contact-us, or through the `Mattermost Help Center <https://support.mattermost.com/>`_.
