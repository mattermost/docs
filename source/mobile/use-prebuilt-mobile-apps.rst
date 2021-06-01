Using Mattermost's Pre-Built Mobile Apps
========================================

We strongly recommend using Mattermost’s pre-built Mobile App. This approach is recommended for Mattermost Cloud and Enterprise Edition customers.

Deployment Options
------------------

When you decide to use the pre-built Mattermost Mobile apps, you have two ways to deploy them: through public app stores, or through an Enterprise Mobile Management (EMM) provider.
  
Using Public App Stores
~~~~~~~~~~~~~~~~~~~~~~~

Your users can download the Mattermost Mobile app as an `iOS app <https://about.mattermost.com/mattermost-ios-app/>`__ or an `Android app <https://about.mattermost.com/mattermost-android-app/>`__ from a public app store. When users launch the Mattermost Mobile app, they must enter the address of your Mattermost server to connect their Mobile app to the server.

Using an EMM Provider
~~~~~~~~~~~~~~~~~~~~~

See our `Deploying Using an EMM Provider <https://docs.mattermost.com/mobile/deploy-mobile-apps-using-emm-provider.html>`__ documentation to learn more about deploying Mattermost Mobile apps through an EMM provider.

Setting Up Push Notifications
-----------------------------

Mattermost hosts a push proxy option available for Mattermost Cloud and Enterprise Edition deployments. The HPNS offers:

- An explicit `privacy policy <https://mattermost.com/data-processing-addendum/>`__ for the contents of unencrypted messages.
- Encrypted TLS connections:
    - Between HPNS and Apple Push Notification Services
    - HPNS and Google’s Firebase Cloud Messaging service
    - HPNS and your Mattermost Server
- Production-level uptime expectations.
- Compatibility with EMM Providers.

Configuring your Mattermost instance to use the Mattermost HPNS is a single, one-time step. Learn more about securing and configuring the `HPNS <https://docs.mattermost.com/mobile/mobile-hpns.html>`__ in our product documentation. 

ID-Only Push Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud and Enterprise customers can limit the data sent to the HPNS through a configuration setting. 

When enabled, a message containing only an ID is transmitted. Once the mobile client receives this ID, the message contents are loaded from the server, and are never transmitted through Apple Push Notification Service (APNS) or Firebase Cloud Messaging (FCM). See our `Configuration Settings <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`__ documentation to learn more about ID-only push notifications.

Test Push Notifications Service (TPNS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After setting up push notifications, we strongly recommend that you test push notifications to ensure they're working.

Mattermost offers a free basic hosted service to test push notifications for self-managed deployments. The TPNS isn’t recommended for use in Production environments, and doesn’t offer production-level update service level agreements (SLAs). To use the Mattermost TPNS:

1. In System Console, go to **Environment > Push Notification Server > Enable Push Notifications**, then select **Use TPNS connection to send notifications to iOS and Android apps**.
2. Specify the URL of the **Push Notification Server** based on your Mattermost edition.

   - Mattermost Enterprise Edition: ``https://push.mattermost.com``
   - Mattermost Team Edition: ``https://push-test.mattermost.com``

See our `Testing Push Notifications <https://docs.mattermost.com/mobile/mobile-testing-notifications.html>`__ documentation to learn more.

Success! Your Public App Store Deployment is Complete
-----------------------------------------------------

If you don't need the additional security provided via an EMM provider, your deployment is complete! Feel free to point your users to our `Mattermost user documentation <https://docs.mattermost.com/guides/user.html>`__ to learn more about using Mattermost.
