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

Commands to Build the App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The set of commands for building the app are used in conjunction with Fastlane.  For most of them, you will need to modify the Fastfile in order to make it work since they are very tightly coupled with Mattermost's build and deployment process.

You will always be able to build an unsigned version of the app as it does not need provisioning profiles or certificates as long as you set up Fastlane in your environment.

 - make build-ios: Builds the iOS app and generates the .ipa file to be distributed. This make command expects an argument as the target which can be dev, beta or release. Depending on the target a Fastlane script runs and each lane has the appropriate certificates and steps according to the Mattermost release process.
 - make build-android: Builds the Android app and generates the .apk file to be distributed. This make command expects an argument as the target which can be dev, alpha or release. Depending on the target, a Fastlane script runs and each lane has the appropriate certificates and steps according to the Mattermost release process.
 - make unsigned-ios: Builds the iOS app and generates an unsigned Mattermost-unsigned.ipa file in the project's root directory.
 - make unsigned-ios: Builds the Android app and generates an unsigned Mattermost-unsigned.apk file in the project's root directory.

If you plan to use the make build-* commands be sure to modify Fastlane to suit your needs as they will fail otherwise.
