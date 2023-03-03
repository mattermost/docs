Mattermost mobile app requirements
==================================

all plans, cloud & sh

Native applications for iOS and Android are available for interacting with the Mattermost server and receiving encrypted push notifications from your private cloud. Organizations can use `a Hosted Push Notification Service </deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ with encrypted communications to mobile apps on the App Store and Google Play, or deploy to an `Enterprise App Store </deploy/mobile-hpns.html#mobile-push-notifications>`__ on your organization's private network. A `Test Push Notification Service </deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ is available for use while evaluating options.


.. csv-table::
    :header: "Operating System", "Technical Requirement"

    "iOS", "iPhone 5s devices and later with iOS 12.1+"
    "Android", "Android devices with Android 7+"

`*` Integrated Windows Authentication is not supported by Mattermost mobile apps. If you use ADFS we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.


Email client
~~~~~~~~~~~~

Receive emails on desktop and mobile from the Mattermost server.

-  *Mobile clients:* iOS Mail App (iOS 7+), Gmail Mobile App (Android, iOS)
