Mattermost Workspace Migration
==============================

This document outlines the process for migrating from Mattermost Cloud to a Mattermost self-hosted instance. In the future, a process for migrating from Mattermost self-hosted to Mattermost Cloud will also be documented and provided here.

Migrating between two installations follows the same process that's documented below, regardless as to whether the source or destination of the migration is in the Cloud or self-hosted. **These steps will work for any Mattermost instance**, as long as the instances are running Mattermost v5.33 or later.

Migrating from Cloud to self-hosted
-----------------------------------

If, after completing your 14-day free Cloud trial, you've decided to self-host your own Mattermost deployment, you can migrate your Cloud data to your self-hosted instance.

How does the process work?
--------------------------

Before you export and migrate your data, you must `install Mattermost <https://docs.mattermost.com/guides/deployment.html#install-guides>`_ on the server you’ll be using to run Mattermost. The migration is done using the mmctl CLI tool, which is a remote CLI tool for Mattermost that's installed locally and uses the Mattermost API. From Mattermost v6.0 onwards, mmctl is pre-installed. For versions prior to 6.0, first download the newest release from `the releases page <https://github.com/mattermost/mmctl/releases/tag/v6.1.0>`_, `install mmctl <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#install-mmctl>`_, and place the binary on your ``PATH``.

The `mmctl usage notes <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-usage-notes>`_ provide some additional context and information which you can reference before and during the process.

You'll be using the `mmctl export <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-export>`__ commands to export your Cloud data for channels, messages, users, etc. The export file is downloaded to a location specified in the export commands. Once the export is complete, you'll import the data into your self-hosted instance.

.. note::
  
  The export process doesn’t include integrations or any custom data. Other aspects of your instance, such as specific security settings and requirements, are also not included. For assistance with migrating additional data and settings, see our support options: https://mattermost.com/support/.

Once mmctl is installed, we can generate the export from the source instance.

Authenticate
------------

Authentication is done with either Mattermost login credentials or an authentication token. First, use your administrator credentials to log into the instance with mmctl, replacing `example-source-domain.com` with the network address of the source instance:

.. code::

   $ mmctl auth login https://yourdomain.cloud.mattermost.com
   
You'll be prompted for a username (use your admin user), password, and for a connection name. The connection name can be anything you want, and it's used to identify this set of credentials in the future, for your convenience. Then you will be able to start the export process:

Create the export
-----------------

Once you're logged in, run:

.. code::

   $ mmctl export create --attachments

This will create a full export of the server, and include attached files. Leave out ``--attachments`` if you do not wish to export attached files from your instance. This process can take some time, so ``mmctl`` will return immediately, and the job will run in the background on the Mattermost instance until the export is fully created. If successful, the command will immediately output a job ID, like this:

.. code::

   Export process job successfully created, ID: yfrr9ku5i7fjubeshs1ksrknzc

While the job is running, its status can be checked using the ID that was provided when it was created, and when it's done the output will look similar to this:

.. code::

  $ mmctl export job show yfrr9ku5i7fjubeshs1ksrknzc
    ID: yfrr9ku5i7fjubeshs1ksrknzc
    Status: success
    Created: 2021-11-03 10:44:13 -0500 CDT
    Started: 2021-11-03 10:44:23 -0500 CDT

Download the export
-------------------

Once the status is ``success``, you can download the export onto your local machine. First, discover the name of the completed export file with ``mmctl export list``:

.. code::

   $ mmctl export list
   r3kcj8yuwbramdt714doafi3oo_export.zip

This will show all of the exports on the server, so be sure to download the latest one and to delete it when you're done to save storage. Download the file with a command like the following, but with the filename of the export on your server:

.. code::

   $ mmctl export download r3kcj8yuwbramdt714doafi3oo_export.zip

Upload the export to the new server
-----------------------------------

Finally, it's time to take our export from the source server and use it as an import into the destination server. First, log into the destination server using mmctl the same way you logged into the source server:

.. code::

   $ mmctl auth login https://localinstance.company.com

Use the following command to upload the export to the destination server. The speed of the upload may vary based on connection speed. When the upload is complete the command will return with the ID of the import:

.. code::
  
   mmctl import upload r3kcj8yuwbramdt714doafi3oo_export.zip
   Upload session successfully created, ID: cfuq6q9kkjrqfgnph1pew3db4e
   Import file successfully uploaded, name: xrzs9wrzufntbfcxpy39mdq9hy

Complete the import into the new server
---------------------------------------

.. code::

   $ mmctl import list available
   cfuq6q9kkjrqfgnph1pew3db4e_r3kcj8yuwbramdt714doafi3oo_export.zip

Run the import job to process to import the export file into the server. The speed of this process may vary based on connection speed. First, start the import process:

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

Then extract the export file to use it by running the following mmctl command:

.. code::
   
   mmctl extract run [flags].

Once your migration is complete and you’ve imported your data into your self-hosted instance we recommend that you take a few days to validate your data and ensure everything is working as expected before taking down your Cloud instance.

If you encounter any issues or problems, please contact our Support team via https://customers.mattermost.com/cloud/contact-us, or through the `Mattermost Help Center <https://support.mattermost.com/>`_.
