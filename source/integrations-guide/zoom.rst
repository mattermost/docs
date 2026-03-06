Connect Zoom to Mattermost
===========================

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:


Reduce friction and time lost to coordinating meetings and switching between apps by integrating Zoom with Mattermost. Make it easy for your teams to start both spontaneous video calls directly from Mattermost channels.

Deploy
------

Setup starts in Zoom and configuration ends in Mattermost.

Register an OAuth app in Zoom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Zoom system admin must perform the following steps in Zoom.

Zoom supports OAuth authentication, and there are 2 types of OAuth Zoom Apps you can register: **Account-Level** and **User-Level**. You can use either type based on your organization's security and preferences.

- **Account-Level**: Individual users in Mattermost are verified by checking their Mattermost email and requesting their Personal Meeting ID via the Zoom API. The user's email address in both Mattermost and Zoom must match. Create a User Level Zoom app instead if you prefer that each user to authorize individually.
- **User-Managed**: Individual users in Mattermost are required to authorize the Mattermost App to access their Zoom account. Create an Account-Level app instead if you prefer that an admin authorizes access on behalf of the whole Zoom organization.

.. important::

  For Account-Level apps, only Zoom users associated with the Zoom Account that created the app can use this integration. You can add users from the **Manage Users** section in the Zoom Account settings.

.. tab:: Account-Level

  Complete the following steps to create an account-level Zoom app for Mattermost.

  1. Go to https://marketplace.zoom.us/ and log in as an admin.
  2. In the top right, select **Develop** and then select **Build App**.
  3. On top, select **Development**. We would choose **Production** if we were publishing to marketplace, but we won't be doing that here.
  4. You can edit the name of your app from top left side by clicking on edit icon.
  5. Choose **Admin-managed app** as the app type.
  6. Next you'll find your **Client ID** and **Client Secret**. Please copy this as these will be needed when you set up Mattermost to use the plugin.
  7. Enter a valid **Redirect URL for OAuth** \(`https://SITEURL/plugins/zoom/oauth2/complete`\) and add the same URL under **Add Allow List**. Note that `SITEURL` should be your Mattermost server URL.
  8. To add user scopes to the app, select **Scopes**, and add the following scopes: ``meeting:read:meeting:admin``, ``meeting:write:meeting:admin``,and ``user:read:user:admin``.

.. tab:: User-Managed

  Complete the following steps to create a user-managed Zoom app for Mattermost.

  1. Go to https://marketplace.zoom.us/ and log in as an admin.
  2. In the top right select **Develop** and then **Build App**.
  3. On top, select **Development**. We would choose **Production** if we were publishing to marketplace, but we won't be doing that here.
  4. You can edit the name of your app from top left side by clicking on edit icon.
  5. Choose **User-managed app** as the app type.
  6. Next you'll find your **Client ID** and **Client Secret**. Please copy this as these will be needed when you set up Mattermost to use the plugin.
  7. Enter a valid **Redirect URL for OAuth** \(`https://SITEURL/plugins/zoom/oauth2/complete`\) and add the same URL under **Add Allow List**. Note that `SITEURL` should be your Mattermost server URL.
  8. To add user scopes to the app, select **Scopes**, and add the following scopes: ``meeting:read:meeting``, ``meeting:write:meeting``,and ``user:read:user``.

Configure webhook events
~~~~~~~~~~~~~~~~~~~~~~~~

When a Zoom meeting ends, the original post shared in the channel can be automatically changed to indicate the meeting has ended and how long it lasted. To enable this functionality, create a webhook subscription in Zoom that tells the Mattermost server every time a meeting ends. The Mattermost server then updates the original Zoom message.

1. While editing the app in Zoom, select **Access** under the **Features** tab on the left.
2. Select **Add New Event Subscription**, and give it a name, such as ``Meeting Ended``.
3. Enter a valid **Event notification endpoint URL** ``https://SITEURL/plugins/zoom/webhook?secret=WEBHOOKSECRET``, replacing ``SITEURL`` with your Mattermost URL. ``WEBHOOKSECRET`` is generated during `Mattermost configuration <#mattermost-configuration>`__.
4. Select **Save** to save the webhook configuration.
5. Copy the **Secret Token** value at the top of the page for use in the next section.

Mattermost configuration
~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost.

Install the Zoom integration from the in-product App Marketplace:

.. note::

  We recommend making a copy of your webhook secret and encryption key, as it will only be visible to you once.

1. In Mattermost, from the Product menu |product-list|, select **App Marketplace**.
2. Search for or scroll to Zoom, and select **Install**.
3. Once installed, select **Configure**. You'll be taken to the System Console.
4. On the Zoom configuration page, enable and configure Zoom interoperability as follows, and then select **Save**.
5. For self-hosted Zoom deployments, enter the **Zoom URL** and **Zoom API URL** for the Zoom server when you're using a self-hosted private cloud or on-premises Zoom server, such as ``https://YOUR-ZOOM.com`` and ``https://api.YOUR-ZOOM.com/v2`` respectively, replacing ``YOUR-ZOOM`` with your Zoom server URL. Leave this field blank if you're using Zoom's vendor-hosted SaaS service.
6. If you've created an `account level Zoom app for Mattermost <#register-an-oauth-app-in-zoom>`__, set **OAuth by Account Level App** to **true**. Leave this value as **false** if you've created a user level Zoom app for Mattermost.
7. Connect your users to Zoom using OAuth. Enter the **Client ID** and **Client Secret** generated when `registering the oauth app in Zoom <#register-an-oauth-app-in-zoom>`__.
8. Select **Regenerate** next to the **At Rest Token Encryption Key** field to generate an AES encryption key. You just need to generate this value, and won't use it anywhere else.
9. If you're configuring webhook events, select **Regenerate** next to the **Webhook Secret** field. This is the ``WEBHOOKSECRET`` value to use in your webhook URL pointing to Mattermost.
10. Paste the **Secret Token** from the Zoom webhook configuration page into the plugin setting **Zoom Webhook Secret**.
11. (Optional) Enable **Restrict Meeting Creation** to restrict users from creating meetings in public channels.
12. Select **Save** to save your changes.


Enable
------

Notify your teams that they can `connect their Zoom accounts to Mattermost <#usage>`__.

Use
-----

You need a paid Zoom account to start a Zoom call within Mattermost. The first time you create a Zoom meeting, you may be prompted to connect your account. Follow the instructions to connect your Zoom account using your credentials.

Start a call by selecting the Zoom icon in the right pane, or by running the ``/zoom start`` slash command in any channel or thread. All channel members can then join the meeting. The meeting host is the person who started the call.

Join the meeting by selecting the call invitation in the channel.

Run the ``/zoom settings`` slash command to set your preference for using your Zoom personal meeting ID as a meeting host. You can choose to always use your personal meeting ID, always use a new unique meeting id, or set Mattermost to prompt you for your preference each time you start a call.

Additional slash commands:

- ``/zoom help`` - Display available commands
- ``/zoom channel-settings`` - Set whether meetings in the current channel use your personal meeting ID or unique meeting ID
- ``/zoom channel-settings list`` - List all channel preferences

For User-Managed apps only:

- ``/zoom connect`` - Connect your Zoom account to Mattermost
- ``/zoom disconnect`` - Disconnect your Zoom account from Mattermost


Customize
----------

This `integration <https://github.com/mattermost/mattermost-plugin-zoom>`_ contains both a server and web app portion.

- Server: Inside the ``/server`` directory, you'll find the Go files that make up the server-side of the integration. Within there, build the plugin like you would any other Go application.
- Web App: Inside the ``/webapp`` directory, you will find the JS and React files that make up the client-side of the plugin. Within there, modify files and components as necessary. Test your syntax by running ``npm run build``.

Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`__ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.

Upgrade
-------

We recommend updating this integration when new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost. Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-zoom/releases>`__ for information on the latest release, previous releases, and compatibiilty considerations.

Get help
--------

Mattermost customers can open a `Mattermost support case <https://support.mattermost.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost Zoom plugin repository <https://github.com/mattermost/mattermost-plugin-zoom>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance.

Mattermost Team Edition and Free customers can visit the Mattermost `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`_ to access the global Mattermost Community for assistance.
