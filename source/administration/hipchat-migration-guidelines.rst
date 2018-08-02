Migrating from HipChat to Mattermost
===========================

You can migrate HipChat users and message histories to Mattermost using the following guidelines.

Guidelines for Success
-------------------------------
+ Review the high level steps outlined below in this guide.
+ Review links to in-depth documentation to help you with more detailed instructions on configuration settings.
+ Customize your instance to meet your unique end-user and security requirements. 
+ Contact us at any time to assist you.

Step 1:  Set up your Mattermost Instance
-------------------------------
#. `Download the latest version <https://about.mattermost.com/download/>`_ of Mattermost.
#. `Deploy <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`_ Mattermost in your environment using the configuration that meets your organization’s needs for performance and scalability.
#. Request a `trial <https://mattermost.com/trial/>`_ of Mattermost Enterprise for `advanced features <https://mattermost.com/pricing/>`_. 

Questions? Please visit our `trouble shooting forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`_ for help. 

Step 2:  Export your data from HipChat Data Center or HipChat Server
-------------------------------

HipChat Server / HipChat Data Server:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you’re able to upgrade HipChat Server or HipChat Data Center to the latest version, we recommend using Group Export Dashboard to export your data. If you’re unable to upgrade, see Command Line Interface procedure below. 

*Using the Group Export Dashboard:*

#. Log in to your Hipchat Server (e.g. hipchat.yourcompany.com)
#. Click on **Server Admin > Export**.
#. Select the data to export.
#. In the **Password** and **Confirm Password** fields, create a password to protect your archive files. (Store this password as it is not saved anywhere else)
#. Click **Export**. Once the export is done, you will receive an email with a link to download the file.

*If you’re unable to use the Group Export Dashboard, use the Command Line Interface to export:*

#. Go to **CLI**.
#. Enter ``hipchat export --export  -p your_password``.
#. Once the export is done, you will receive an email with a link to download the file.

More detailed instructions can be found at https://confluence.atlassian.com/hipchatdc3/export-data-from-hipchat-data-center-913476832.html.


Step 3: Import your data into Mattermost 
-------------------------------
1. Follow the `Mattermost Bulk Load Tool <https://docs.mattermost.com/deployment/bulk-loading.html>`_ guide to import your data into Mattermost. 

Note: Efforts are underway to source scripts from the Mattermost community to further automate this step. If you’re interested in contributing, please let us know at info@mattermost.com, Twitter or Mattermost forums at https://forum.mattermost.org

2. Alternatively, `contact Mattermost <https://mattermost.com/contact-us/>`_ for partner recommendations for your region to assist in your import. 
  


