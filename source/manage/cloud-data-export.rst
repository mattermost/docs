Mattermost workspace migration
==============================

.. include:: ../_static/badges/allplans-cloud.rst
  :start-after: :nosearch:

.. contents:: On this page
  :backlinks: top
  :depth: 1
  :local:

This document outlines the process for migrating from Mattermost Cloud to a Mattermost self-hosted instance. In the future, a process for migrating from Mattermost self-hosted to Mattermost Cloud will also be documented and provided here.

Migrating between two installations follows the same process that's documented below, regardless as to whether the source or destination of the migration is in the Cloud or self-hosted. **These steps will work for any Mattermost instance**.

Migrate from Cloud to self-hosted
---------------------------------

You can migrate your Cloud workspace data to a self-hosted deployment at any time.

How does the process work?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you export and migrate your data, you must `install Mattermost </guides/deployment.html#install-guides>`_ on the server you’ll be using to run Mattermost. The migration is done using the mmctl CLI tool, which is a remote CLI tool for Mattermost that's installed locally and uses the Mattermost API. ``mmctl`` is pre-installed.

The `mmctl usage notes </manage/mmctl-command-line-tool.html#mmctl-usage-notes>`_ provide some additional context and information which you can reference before and during the process.

You'll be using the `mmctl export </manage/mmctl-command-line-tool.html#mmctl-export>`__ commands to export your Cloud data for channels, messages, users, etc. The export file is downloaded to a location specified in the export commands. Once the export is complete, you'll import the data into your self-hosted instance. 

Alternatively, you can export the data to an Amazon S3 cloud storage location in cases where an export is quite large and challenging to download from the Mattermost server. See the `create the export <#create-the-export>`__ section below for details.

.. note::
  
  Prior to migrating your data from Cloud, please ensure you have the appropriate permissions within your organization to carry out the data export which may contain sensitive information. Mattermost is not liable for any actions taken after the data export.
  
  Moreover, the export process doesn’t include integrations or any custom data. Other aspects of your instance, such as specific security settings and requirements, are also not included. For assistance with migrating additional data and settings, see our support options: https://mattermost.com/support/.

Once ``mmctl`` is authenticated, you can generate the export from the source instance.

Authenticate
------------

Authentication is done with either Mattermost login credentials or an authentication token. First, use your administrator credentials to log into the instance with mmctl, replacing `example-source-domain.com` with the network address of the source instance:

.. code::

   mmctl auth login https://yourdomain.cloud.mattermost.com
   
You'll be prompted for a username (use your admin user), password, and for a connection name. The connection name can be anything you want, and it's used to identify this set of credentials in the future, for your convenience. Then you will be able to start the export process.

Create the export
-----------------

Once you're logged in, run the following ``mmctl`` command:

.. code::
         
   mmctl export create

Running this command creates a full export of the server, including attached files. Append ``--no-attachments`` if you do not wish to export attached files from your instance. This process can take some time, so ``mmctl`` will return immediately, and the job will run in the background on the Mattermost instance until the export is fully created. If successful, the command will immediately output a job ID, like this:

.. code::

   Export process job successfully created, ID: yfrr9ku5i7fjubeshs1ksrknzc

While the job is running, its status can be checked using the ID that was provided when it was created, and when it's done the output will look similar to this:

.. code::

   mmctl export job show yfrr9ku5i7fjubeshs1ksrknzc
   ID: yfrr9ku5i7fjubeshs1ksrknzc
   Status: success
   Created: 2021-11-03 10:44:13 -0500 CDT
   Started: 2021-11-03 10:44:23 -0500 CDT

Once the status is ``success``, download the export onto your local machine. First, discover the name of the completed export file with ``mmctl export list``:

.. code::

   mmctl export list
   r3kcj8yuwbramdt714doafi3oo_export.zip

This will show all of the exports on the server, so be sure to download the latest one and to delete it when you're done to save storage. Generate a link to download the file with a command like the following, but with the filename of the export on your server:

.. code::

   mmctl export generate-presigned-url r3kcj8yuwbramdt714doafi3oo_export.zip

.. tip::
   
   - As an alternative to this last step, from your Mattermost Cloud web instance, you can retrieve the file download link to the export by using the Mattermost slash command ``/exportlink [job-id|zip file|latest]``. Use the ``latest`` option to automatically pull the latest export available, or specify the download link by ``job-id`` or ``zip file``. 
   - Mattermost v8.1.0-RC1 is required to use the ``mmctl export generate-presigned-url`` command on a self-hosted Mattermost instance. Access the `Mattermost Enterprise v8.1.0-RC1 binary <https://releases.mattermost.com/8.1.0-rc1/mattermost-enterprise-8.1.0-rc1-linux-amd64.tar.gz>`__ or the `Mattermost Team Edition v8.1.0-RC1 binary <https://releases.mattermost.com/8.1.0-rc1/mattermost-team-8.1.0-rc1-linux-amd64.tar.gz>`__.

Upload the export to the new server
-----------------------------------

Finally, it's time to take our export from the source server and use it as an import into the destination server. Before proceeding, review and modify the following self-hosted Mattermost configuration settings, where applicable, to ensure a smooth and successful import.

+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| **Mattermost configuration setting**                                              | **Large file import recommendation**                                                                                          |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| `Maximum Users Per Team                                                           | Increase this value to a number that **exceeds** the maximum number of users, per team, in the import file.                   |
| </configure/site-configuration-settings.html#max-users-per-team>`__               |                                                                                                                               |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| `Maximum File Size                                                                | Temporarily increase this value to be **larger** than the size of the import file.                                            |
| </configure/environment-configuration-settings.html#maximum-file-size>`__         | Following a successful import, we strongly recommend reverting this value to a reasonable limit for daily expected usage.     |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| `Write Timeout                                                                    | Temporarily adjust this value based on import file speed and network path to enable the file to upload without timeouts.      |
| </configure/environment-configuration-settings.html#write-timeout>`__             | Start with a value of **3600** and adjust if needed.                                                                          |
|                                                                                   | Following a successful import, we strongly recommend reverting this setting to its initial or previous value.                 |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| `Read Timeout                                                                     | Temporarily adjust this value based on import file speed and network path to enable the file to upload without timeouts.      |
| </configure/environment-configuration-settings.html#read-timeout>`__              | Start with a value of **3600** and adjust if needed.                                                                          |
|                                                                                   | Following a successful import, we strongly recommend reverting this setting to its initial or previous value.                 |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| `Amazon S3 Request Timeout                                                        | If using cloud-based file storage, adjust this value to ensure your storage requests don't time out too soon.                 |
| </configure/environment-configuration-settings.html#amazon-s3-request-timeout>`__ |                                                                                                                               |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

Next, log into the destination server using ``mmctl`` the same way you logged into the source server:

.. code::

   mmctl auth login https://localinstance.company.com

Use the following command to upload the export to the destination server. The speed of the upload may vary based on connection speed. When the upload is complete the command will return with the ID of the import:

.. code::
  
   mmctl import upload r3kcj8yuwbramdt714doafi3oo_export.zip
   Upload session successfully created, ID: cfuq6q9kkjrqfgnph1pew3db4e
   Import file successfully uploaded, name: xrzs9wrzufntbfcxpy39mdq9hy

Complete the import into the new server
---------------------------------------

.. code::

   mmctl import list available
   cfuq6q9kkjrqfgnph1pew3db4e_r3kcj8yuwbramdt714doafi3oo_export.zip

Run the import job to process to import the export file into the server. The speed of this process may vary based on connection speed. First, start the import process:

.. code::
   
   mmctl import process cfuq6q9kkjrqfgnph1pew3db4e_r3kcj8yuwbramdt714doafi3oo_export.zip

Once you've marked the file for processing, you can check the status of the job using ``mmctl import job list``:

.. code::

  mmctl --local import job list
  ID: f93jxu1hzty79enwa1xy6f1tbr
  Status: pending
  Created: 2021-10-28 13:32:55 +0200 CEST

When the job is complete, the ``success`` status is displayed:

.. code::

  mmctl --local import job list
  ID: f93jxu1hzty79enwa1xy6f1tbr
  Status: success
  Created: 2021-10-28 13:32:55 +0200 CEST
  Started: 2021-10-28 13:33:05 +0200 CEST

Then extract the export file to use it by running the following mmctl command:

.. code::
   
   mmctl extract run [flags].

Once your migration is complete and you’ve imported your data into your self-hosted instance we recommend that you take a few days to validate your data and ensure everything is working as expected before taking down your Cloud instance.

.. note:: If you are using email/password authentication, your users must reset their passwords.

If you encounter any issues or problems, please contact our Support team via https://customers.mattermost.com/cloud/contact-us, or through the `Mattermost Help Center <https://support.mattermost.com/>`_.

Migrate from self-hosted to Cloud
----------------------------------

When you migrate from self-hosted to Cloud, you'll need to open a ticket with the Mattermost Support team so they can assist you with the process. The information below describes the migration process. Before you get started, visit our `Support site <https://support.mattermost.com/hc/en-us/requests/new>`_ to open a ticket. 

.. note:: This migration process is only available to customers using paid Mattermost editions.

Before you begin your migration, take note of the following information before you begin:

**User Authentication**

If you are using the email login method, users will need to reset their passwords after the migration has been completed. Other authentication methods, such as LDAP and GitLab SSO, required changes to your infrastructure allowing the specific authentication method to function in Mattermost cloud.

**Plugins**

If you’re using plugins that aren’t listed on the Marketplace, they won’t be included in the export and you won’t have access to them going forward. You can view the list of plugins `in the Support knowledgebase <https://support.mattermost.com/hc/en-us/articles/5346624843924>`_.

**Data**

The migration only includes data from Channels. No Playbooks data is exported.

Migration process
~~~~~~~~~~~~~~~~~

**Export from your self-hosted instance**

Use your administrator credentials to log into your self-hosted Mattermost server. Once you're logged in, run:

.. code:: 
   
   mmctl export create --attachments

This creates a full export of the server, and includes attached files. If you don’t want to export attached files, leave out ``--attachments``.

This process can take some time, so ``mmctl`` will return immediately, and the job will run in the background until the export is fully created. If successful, the command will immediately output a job ID, like this:

.. code::
  
  Export process job successfully created, ID: yfrr9ku5i7fjubeshs1ksrknzc

While the job is running, its status can be checked using the ID that was provided when it was created, and when it's done the output will look similar to this:

.. code::

    mmctl export job show yfrr9ku5i7fjubeshs1ksrknzc
    ID: yfrr9ku5i7fjubeshs1ksrknzc
    Status: success
    Created: 2021-11-03 10:44:13 -0500 CDT
    Started: 2021-11-03 10:44:23 -0500 CDT

The completed file will be downloaded to your desktop as a ``.zip`` file.

.. note:: 
   
   Do not rename the file as the file name is referenced in log files, which are used by the Support team to validate the exported file.

The Support team will provide you with S3 credentials so you can upload the exported file. Once you’ve uploaded the file, please contact the Support team and let them know.

Create a new workspace on the Mattermost Cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the meantime, you can log into Mattermost Cloud with your Mattermost credentials and create a Cloud workspace. 

.. note:: 
   
   Do not create any users in your Mattermost Cloud instance as the migration process performs this task for you.

Importing your data into your Mattermost Cloud instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the export upload to the provided S3 bucket is complete and you’ve shared your Mattermost Cloud instance name/URL, Support can begin the import step.

Depending on the size of the export this process can take some time. Support will contact you as soon as the import is complete. During this time it is highly recommended you do not use your Mattermost Cloud instance.

Start using your Mattermost Cloud instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the export is complete, you can log into your Cloud instance and can invite your users to log in. 

.. note:: 
  
  We recommend that you keep your self-hosted Mattermost server until you’ve been using your Cloud instance for a while and all is verified as is as expected.