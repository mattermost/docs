Connect ServiceNow to Mattermost
=================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |product-menu| image:: ../images/products_E82F.svg
  :alt: The Product menu is located in the top left corner of the Mattermost screen.
  :class: theme-icon

Minimize distractions and reduce context switching by bridging the gap between IT service management (ITSM) and team communication. Create and manage incident reports, change requests, and service tickets, as well as manage event-driven notification subscriptions for ServiceNow record changes, in real-time, and automate routine tasks to decrease response times without leaving Mattermost.

Setup
------

Setup starts in ServiceNow and finishes in Mattermost.

Create an OAuth app in ServiceNow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to your ServiceNow instance and then to **All > System OAuth > Application Registry**.
2. Select New in the top right corner, and then select **Create an OAuth API endpoint for external clients**.
3. Enter the name for your app and set the redirect URL to: ``https://<YOUR-MATTERMOST-URL>/plugins/mattermost-plugin-servicenow/api/v1/oauth2/complete``, replacing ``YOUR-MATTERMOST-URL`` with the Mattermost URL you want the ServiceNow events to post to, using lowercase characters.

 .. note:: 

  A client secret is generated automatically. Copy the secret and the Client ID. You'll need these values for the Mattermost configuration.

Upload the update set in ServiceNow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Changing your ServiceNow instance to support subscriptions, record changes, and send change notifications to Mattermost is done by a Mattermost and ServiceNow system admin using an `update set <https://docs.servicenow.com/bundle/washingtondc-application-development/page/build/system-update-sets/concept/system-update-sets.html>`_. Once created, you can download the update set from Mattermost and upload it into ServiceNow. 

1. In the Mattermost System Console, download the update set XML file.
2. In your ServiceNow instance, go to **All > System Update Sets > Retrieved Update Sets**.
3. Select the **Import Update Set from XML** link at the bottom of the page.
4. Select the downloaded XML update set file and upload it. You'll see an update set named **ServiceNow for Mattermost Notifications**.
5. Select that update set, and then select **Preview Update Set**.
6. Select **Commit Update Set**.
7. Confirm the data loss notification, and select **Proceed with Commit**. Your update set is uploaded and committed to ServiceNow.

Set up user permissions in ServiceNow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the update set is uploaded, it creates a new role called ``x_830655_mm_std.user``. Users must have this role in ServiceNow to add or manage Mattermost subscriptions. You need to be a ServiceNow system admin to add the ``x_830655_mm_std.user`` role to all users who should have the ability to add or manage subscriptions through Mattermost.

1. In your ServiceNow instance, go to **All > User Administration > Users**.
2. On the Users page, open a user's profile where you want the role added.
3. Select the **Roles** tab in the table, and select **Edit**.
4. Search for the ``x_830655_mm_std.user`` role, and add that role to the user's **Roles** list, and select **Save**. That user can now add or manage Mattermost subscriptions.

Update the API secret on the change of ServiceNow Webhook Secret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In Mattermost, copy the **Webhook Secret** from your Mattermost instance by going to **System Console > Plugins > ServiceNow**.
2. In your ServiceNow instance, go to **All > x_830655_mm_std_servicenow_for_mattermost_notifications_auth.list**. (**Note**: You must enter the complete name and search.)
3. On the page, select the row containing your Mattermost Server URL. If that row doesn't exist, create it manually by selecting **New** located in the top-right corner, and adding your Mattermost Server URL.
4. Update the **API Secret** in the ServiceNow instance with the **Webhook Secret** from Mattermost, and select **Update**.

What changes are made to ServiceNow instance?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **GetStates scripted REST API**: Returns different states available for the records. Records supported: incident, task, change_task, and cert_follow_on_task
- An application with the name **ServiceNow for Mattermost Notifications**.

 - **ServiceNow for Mattermost Notifications** application handles the storing of subscription details and sending notifications on the subscribed events.
 - **ServiceNow for Mattermost Notifications** ``Auth`` table to store different Mattermost server URLs with their webhook secrets.
 - **ServiceNow for Mattermost** ``Subscriptions`` table to store the subscription details.
 - **Business rules** to handle different events (example: new record created, comment added on record, record state updated, etc.)
 - **Script actions** to send notifications based on the subscription events.
 - **Events registration** to register different record-type events.

ServiceNow tables accessible in Mattermost
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``incident``
- ``problem``
- ``change_request``
- ``kb_knowledge``
- ``task``
- ``change_task``
- ``cert_follow_on_task``
- ``x_830655_mm_std_servicenow_for_mattermost_notifications_auth``
- ``x_830655_mm_std_servicenow_for_mattermost_subscriptions``
- All the tables extending these tables above

Mattermost configuration
~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost.

Install the ServiceNow integration from the in-product App Marketplace:

1. In Mattermost, from the Product menu |product-menu|, select **App Marketplace**.
2. Search for or scroll to ServiceNow, and select **Install**.
3. Once installed, select **Configure**. You're taken to the System Console.
4. On the ServiceNow configuration page, enable and configure ServiceNow interoperability as follows, and then select **Save**:

  - **ServiceNow Server Base URL**: Enter the base URL of your ServiceNow instance.
  - **ServiceNow Webhook Secret**: Regenerate the webhook secret for ServiceNow. Regenerating this key will stop the subscription notifications. See the documentation on `creating an OAuth app in ServiceNow <#create-an-oauth-app-in-servicenow>`__ for details on updating the secret in the ServiceNow instance and start receiving notifications again.
  - **ServiceNow OAuth Client ID**: The clientID of your registered OAuth app in ServiceNow.
  - **ServiceNow OAuth Client Secret**: The client secret of your registered OAuth app in ServiceNow.
  - **Encryption Secret**: Select **Regenerate** to generate a new encryption secret. This encryption secret is used to encrypt and decrypt the OAuth token.
  - **Download ServiceNow Update Set**: Download the update set XML file to upload to ServiceNow.

Enable
------

Notify your teams that they can `connect their ServiceNow accounts to Mattermost <#connect-a-servicenow-account-to-mattermost>`__.

Upgrade
-------

We recommend updating this integration as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.
Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-servicenow/releases>`__ for the latest release, available releases, and compatibiilty considerations.

Usage
-----

Users who want to use ServiceNow interconnectivity must connect a ServiceNow account to Mattermost. 

Once connected, you'll receive direct messages from the ServiceNow bot in Mattermost for ServiceNow activity.

Connect a ServiceNow account to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In Mattermost, run the ``/servicenow connect`` slash command in any Mattermost channel to link your Mattermost account with your ServiceNow account. Follow the link into your ServiceNow instance, and select **Allow**. You can disconnect your accounts by running the ``/servicenow disconnect`` slash command.

.. tip:: 
  You can also select the **ServiceNow** icon in the apps bar on the right to connect your ServiceNow account.

2. Once connected, run the ``/servicenow help`` slash command to see what you can do.

Get help
--------

Mattermost customers can open a `Mattermost support case <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost ServiceNow plugin repository <https://github.com/mattermost/mattermost-plugin-servicenow>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance.

Customize
---------

This integration contains both a server and web app portion.

ServiceNow itself provides developer instances to anyone who wishes to develop on ServiceNow. Developers can get a ServiceNow developer instance by logging in to their ServiceNow developer account, and selecting **Request Instance** in the top right corner. Once the instance is created, open the menu from the top right corner, go to **Manage Instance Password**, and log in to the developer instance in a new tab.

See the `Development <https://github.com/mattermost/mattermost-plugin-servicenow/blob/master/docs/developer_docs.md#development>`_ section of the Mattermost ServiceNow Plugin GitHub repository for details on customizing this integration.

Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`__ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.