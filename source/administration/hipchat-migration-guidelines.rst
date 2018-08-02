Migrating from HipChat to Mattermost
===========================

Migrating from HipChat to Mattermost is made simple with the use of our Bulk Load Tool and comprehensive documentation to help you along the way.  Please use the following guidelines to help you extract, transform and load your data from HipChat to Mattermost. 

Guidelines for Success
-------------------------------
+ Review the high level steps outlined below in this guide.
+ Review links to in-depth documentation to help you with more detailed instructions on configuration settings.
+ Customize your instance to meet your unique end-user and security requirements. 
+ Contact us at any time to assist you.

Step 1:  Set up your Mattermost Instance
-------------------------------
#. Download the `latest version <https://about.mattermost.com/download/>`_ of Mattermost.
#. `Deploy <https://docs.mattermost.com/guides/administrator.html#installing-mattermost)>`_ Mattermost in your environment using the configuration that meets your organization’s needs for performance and scalability.


Step 2:  Export your data from HipChat 
-------------------------------

HipChat Server / HipChat Data Server:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Atlassian recommends upgrading to the latest version of HipChat Server or HipChat Data Center for access to the Group Export Dashboard.  You can view their instructions on exporting your data `here <https://www.atlassian.com/partnerships/slack/migration>`_.

**Using the Group Export Dashboard:**

#. Log in to your Hipchat Server (e.g. hipchat.yourcompany.com)
#. Click on Server Admin > Export.
#. Select the data to export.
#. In the Password and Confirm Password fields, create a password to protect your archive files. (Store this password as it is not saved anywhere else)
#. Click Export, and once the export is done you will receive an email with a link to download the file.

**Using the Command Line Interface**

#. Go to CLI.
#. Enter hipchat export --export  -p your_password.
#. Once the export is done you will receive an email with a link to download the file.

More detailed instructions for the Command Line Interface can be found `here <https://confluence.atlassian.com/hipchatdc3/export-data-from-hipchat-data-center-913476832.html>`_.


HipChat Cloud: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Log in at yourdomain.hipchat.com/admin/
#. Click on the Data Export tab
#. Select the data to export.
#. In the Password and Confirm Password fields, create a password to protect your archive files. (Store this password as it is not saved anywhere else.)
#. Click Export, and once the export has completed, the export will be available to you in the admin console.


Step 3: Transform your data to the Mattermost import format  
-------------------------------
#. Format your HipChat data to JSONL format.  We offer a comprehensive `guide <https://docs.mattermost.com/deployment/bulk-loading.html#data-format>`_ to assist in the data formatting requirements for our bulk loading process.  
#. Alternatively, consider using a partner to assist you through this step.  Please `contact us <https://about.mattermost.com/contact/>`_ if you would like some recommendations.  


Step 4:  Import your data into Mattermost 
-------------------------------
#. Using our Bulk Loading Tool and detailed `guide <https://docs.mattermost.com/deployment/bulk-loading.html>`_, validate your data is ready for import.
#. Once validated, use the same Bulk Loading Tool to import your data.
#. Verify your data imported correctly.


Step 5:  Optimize Mattermost to meet your organization’s unique end-user and security requirements  
-------------------------------
#. Set `system and team level permissions <https://docs.mattermost.com/deployment/advanced-permissions.html>`_. 
#. Review other `administration settings <https://docs.mattermost.com/administration/config-settings.html>`_ to help you manage your instance.
#. Install `integrations <https://about.mattermost.com/community-applications/>`_ to increase your team’s efficiency.
#. Provide `instructions to your user's <https://docs.mattermost.com/guides/user.html>`_ on how to use Mattermost to help them get acclimated with the system. 

