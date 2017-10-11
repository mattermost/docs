Build Your Own Version of the Mattermost Mobile Apps
====================================================

To deploy in production with privately-hosted mobile apps compiled by your organization in an Enterprise App Store:

1. Compile your own iOS and Android mobile applications from the `open source repository <https://github.com/mattermost/mattermost-mobile>`_
  - Note: If your server version is not supported by the Mattermost apps, you will need to use the Mattermost Classic app repositories for `iOS <https://github.com/mattermost/mattermost-ios-classic>`_ and `Android  <https://github.com/mattermost/mattermost-android-classic>`_

2. Compile your own Mattermost Push Notification Service (MPNS) from the `open source repository <https://github.com/mattermost/push-proxy>`_
  - To secure your push notifications, make sure to use encrypted TLS connections between:

    - MPNS and Apple Push Notification Service
    - MPNS and Google’s Firebase Cloud Messaging
    - MPNS and your Mattermost server

3. Set up a way to connect to your private network Mattermost instance, using:
  - An external proxy with encrypted transport through HTTPS and WSS network connections
  - (Optional) A mobile VPN client
  - Note: If a mobile VPN client with multi-factor authentication is not used, we recommend requiring multi-factor authentication through Mattermost Enterprise Edition or your SSO provider

4. Enable mobile push notifications
  - Go to **System Console** > **Notifications** > **Mobile Push**
  - Under **Send Push Notifications**, select **Manually enter Push Notification Service location**
  - Enter the location of your Mattermost Push Notification Service in the **Push Notification Server** field

.. image:: ../images/mobile_manual_mpns.png

5. (Optional) Customize mobile push notification contents
  - Go to **System Console** > **Notifications** > **Mobile Push**
  - Select an option for **Push Notification Contents** to specify what type of information to include in push notifications
  - Most deployments choose to include the full message snippet in push notifications unless they have policies against it to protect confidential information

.. image:: ../images/mobile_push_contents.png

6. Deploy to an Enterprise App Store
