Connect Zoom to Mattermost
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |product-menu| image:: ../images/products_E82F.svg
  :alt: The Product menu is located in the top left corner of the Mattermost screen.
  :class: theme-icon

Reduce friction and time lost to coordinating meetings and switching between apps by integrating Zoom with Mattermost. Make it easy for your teams to start both spontaneous and scheduled video calls directly from Mattermost channels.

Setup
------

Setup starts in Zoom and configuration ends in Mattermost.

Register an OAuth app in Zoom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Zoom system admin must perform the following steps in Zoom.

Zoom supports OAuth authentication, and there are 2 types of OAuth Zoom Apps you can register: **Account-Level** and **User-Level**. You can use either type based on your organization's security and preferences.

- **Account-Level**: Individual users in Mattermost are verified by checking their Mattermost email and requesting their Personal Meeting ID via the Zoom API. The user's email address in both Mattermost and Zoom must match. Create a User Level Zoom app instead if you prefer that each user to authorize individually.
- **User-Managed**: Individual users in Mattermost are required to authorize the Mattermost App to access their Zoom account. Create an Account-Level app instead if you prefer that an admin authorizes access on behalf of the whole Zoom organization.

.. tab:: Account-Level

  Complete the following steps to create an account-level Zoom app for Mattermost.

  1. Go to https://marketplace.zoom.us/ and log in as an admin.
  2. In the top left, select **Develop** and then select **Build App**.
  3. Under **Choose your app type**, select **OAuth**.
  4. Enter a name for your app.
  5. Choose **Account-level app** as the app type.
  6. Choose whether to publish this app on Zoom Marketplace. In most cases you'll want this disabled. See notes below for details on publishing the app on the Zoom Marketplace.
  7. Select **Create**.

  .. note::

    - To publish the account level Zoom app on the Zoom Marketplace, go to the **App Credentials** tab on the left.
      - Copy the production values for **Client ID** and **Client Secret**. You'll provide these values during `Mattermost configuration <#mattermost-configuration>`__.

      - Enter a valid **Redirect URL for OAuth** ``https://YOUR-MATTERMOST-URL.COM/plugins/zoom/oauth2/complete``, replacing ``https://YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. This value must match the Mattermost server URL you use to log in.
      - Add the same ``https://YOUR-MATTERMOST-URL.COM`` under **Add Allow List**.
      - To set up a deauthorization URL to deauthorize users directly from Zoom, go to the **Information** tab on the left. Under **Deauthorization Notification**, enter a valid **Endpoint URL** ``https://YOUR-MATTERMOST-URL.COM/plugins/zoom/deauthorization?secret=WEBHOOKSECRET``, replacing ``https://YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. ``WEBHOOKSECRET`` is generated during `Mattermost configuration <#mattermost-configuration>`__.

    - To add user scopes to the OAuth app, go to the **Scopes** tab on the left. Add the following scopes: ``meeting:read:meeting:admin``, ``meeting:write:meeting:admin``,and ``user:read:user:admin``.
    - Zoom has one last option called **Install**. There is no need to perform this action. However, if you perform this action inadvertently, you'll see an error on Mattermost. This is expected.

.. tab:: User-Managed

  Complete the following steps to create a user-managed Zoom app for Mattermost. 

  1. Go to https://marketplace.zoom.us/ and log in as an admin.
  2. In the top left, select **Develop** and then select **Build Legacy App**.
  3. Under **Choose your app type**, select **OAuth**.
  4. Enter a name for your app.
  5. Choose **User-managed app** as the app type.
  6. Choose whether topublish this app on Zoom Marketplace. In most cases you'll want this disabled. See notes below for details on publishing the app on the Zoom Marketplace.
  7. Select **Create**.

  .. note::

    - To publish the user level Zoom app on the Zoom Marketplace, go to the **App Credentials** tab on the left.

      - Copy the production values for **Client ID** and **Client Secret**. You'll provide these values during `Mattermost configuration <#mattermost-configuration>`__.
      - Enter a valid **Redirect URL for OAuth** ``https://YOUR-MATTERMOST-URL.COM/plugins/zoom/oauth2/complete``, replacing ``https://YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. This value must match the Mattermost server URL you use to log in.
      - Add the same ``https://YOUR-MATTERMOST-URL.COM`` under **Add Allow List**.
      - To set up a deauthorization URL to deauthorize users directly from Zoom, go to the **Information** tab on the left. Under **Deauthorization Notification**, enter a valid **Endpoint URL** ``https://YOUR-MATTERMOST-URL.COM/plugins/zoom/deauthorization?secret=WEBHOOKSECRET``, replacing ``https://YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. ``WEBHOOKSECRET`` is generated during `Mattermost configuration <#mattermost-configuration>`__.

    - To add user scopes to the OAuth app, go to the **Scopes** tab on the left. Add the following scopes: ``meeting:read:meeting``, ``meeting:write:meeting``,and ``user:read:user``.
    - Zoom has one last option called **Install**. There is no need to perform this action. However, if you perform this action inadvertently, you'll see an error on Mattermost. This is expected.

.. important::

  If you've been using an older version of the Zoom plugin prior to release v1.4, you likely have a legacy webhook-type app configured in Zoom. 

  - Legacy webhook apps are no longer supported by Zoom or Mattermost and aren't compatible prior to release v1.4. 
  - You may experience issues with the meeting status message information not being updated when a meeting ends. This is because the webhook endpoint expects a JSON format request, and newer webhooks use different formats. 
  - From version 1.4 of this integration, you can configure and associate your webhooks with an app you've already created. We recommend removing the previous webhook app before configuring a new webhook.

Configure webhook events
~~~~~~~~~~~~~~~~~~~~~~~~

When a Zoom meeting ends, the original link shared in the channel can be changed to indicate the meeting has ended and how long it lasted. To enable this functionality, create a webhook subscription in Zoom that tells the Mattermost server every time a meeting ends. The Mattermost server then updates the original Zoom message.

1. While logged in to https://marketplace.zoom.us/ as an admin, go to the **Feature** tab on the left.
2. Enable **Event Subscriptions**.
3. Select **Add New Event Subscription**, and give it a name, such as ``Meeting Ended``.
4. Enter a valid **Event notification endpoint URL** ``https://SITEURL/plugins/zoom/webhook?secret=WEBHOOKSECRET``, replacing ``https://YOUR-MATTERMOST-URL.COM`` with your Mattermost URL. ``WEBHOOKSECRET`` is generated during `Mattermost configuration <#mattermost-configuration>`__.
5. Select **Add events**, and then select the **End Meeting** event.
6. Select **Done** and then save your app.

Mattermost configuration
~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost.

Install the Zoom integration from the in-product App Marketplace:

1. In Mattermost, from the Product menu |product-menu|, select **App Marketplace**.
2. Search for or scroll to Zoom, and select **Install**.
3. Once installed, select **Configure**. You're taken to the System Console.
4. On the Zoom configuration page, enable and configure Zoom interoperability as follows, and then select **Save**:

  - For Mattermost Cloud deployments, leave the **Zoom API URL** and **Zoom URL** fields blank.
  - For self-hosted Mattermost deployments, enter the **Zoom URL** and **Zoom API URL** for the Zoom server when you're using a self-hosted private cloud or on-premises Zoom server, such as ``https://YOUR-ZOOM.com`` and ``https://api.YOUR-ZOOM.com/v2`` respectively, replacing ``YOUR-ZOOM`` with your Zoom server URL. Leave this field blank if you're using Zoom's vendor-hosted SaaS service.
- If you've created an `account level Zoom app for Mattermost <#register-an-oauth-app-in-zoom>`__, set **OAuth by Account Level App** to **true**. Leave this value as **false** if you've created a user level Zoom app for Mattermost.

  - Connect your users to Zoom using OAuth. Enter the **Client ID** and **Client Secret** generated when `registering the oauth app in Zoom <#register-an-oauth-app-in-zoom>`__.
  - Select **Regenerate** next to the **At Rest Token Encryption Key** field to generate an AES encryption key.
  - If you're configuring webhook events, or setting up deauthorization, select **Regenerate** next to the **Webhook Secret** field. Configure this secret as the **Zoom Webhook Secret** on the **Features** tab in Zoom.
  - Select **Save** to save your changes.

Enable
------

Notify your teams that they can `connect their Zoom accounts to Mattermost <#usage>`__.

Upgrade
-------

We recommend updating this integration when new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost. Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-zoom/releases>`__ for the latest release, available releases, and compatibiilty considerations.

Usage
-----

You need a paid Zoom account to start a Zoom call within Mattermost. The first time you create a Zoom meeting, you may be prompted to connect your account. Follow the instructions to connect your Zoom account using your credentials.

Start a call by selecting the Zoom icon in the right pane, or by running the ``/zoom start`` slash command in any channel. All channel members are invited to join the call. The call host is the person who started the call.

Join a call by selecting the call invitation in the channel.

Run the ``/zoom settings`` slash command to set your preference for using your Zoom personal meeting ID as a call host. You can always use your personal meeting ID, never use it, or set Mattermost to prompt you for your preference each time you start a call.

Get help
--------

Mattermost customers can open a `Mattermost support case <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost Zoom plugin repository <https://github.com/mattermost/mattermost-plugin-zoom>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance, or join us on the  `Mattermost Discussion Forum <https://forum.mattermost.org/c/plugins>`_.

Customize
----------

This integration contains both a server and web app portion.

- Server: Inside the ``/server`` directory, you'll find the Go files that make up the server-side of the plugin. Within there, build the plugin like you would any other Go application.
- Web App: Inside the ``/webapp`` directory, you will find the JS and React files that make up the client-side of the plugin. Within there, modify files and components as necessary. Test your syntax by running ``npm run build``.

Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`__ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.