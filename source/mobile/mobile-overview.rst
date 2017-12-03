Mobile Applications Guide
=========================

There are three main options for deploying the Mattermost Mobile Apps.

Install from Apple App Store and Google Play
-----------------------------------------------------------------------------

For quick and easy deployment, you can download the Mattermost mobile apps directly from the Apple App Store and Google Play.

This option is recommended for:

1. Testing out the mobile applications
2. Team Edition servers using push notifications from TPNS
3. Enterprise Edition servers who do not need app customization

Build the apps yourself
-------------------------------------------------------

To customize the mobile apps, you can fork the open source repository and compile your own versions of the Mattermost mobile applications and Mattermost push proxy server.

This option is recommended for:

1. Organizations that want to customize the mobile apps
2. Team Edition servers that need encrypted push notifications

Use an EMM provider
---------------------------------------------

To meet other security and compliance policies, you can deploy the Mattermost apps with any EMM provider that supports `AppConfig <https://www.appconfig.org/members/>`_, such as MobileIron, Blackberry UEM, or Airwatch. You will still need to choose either the App Store/Google Play versions or apps compiled yourself to use in conjunction with the EMM provider.

This option is recommended for:

1. Organizations that typically use EMM solutions to deploy mobile apps to meet security and compliance policies
