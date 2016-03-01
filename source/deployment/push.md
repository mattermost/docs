# Mobile Apps and Push Notifications

This section explains how push notifications work with pre-compiled iOS and Android applications. 

See [Push Notification Settings](http://docs.mattermost.com/administration/config-settings.html#push-notification-settings) to understand how they are configured.

## How push notifications are sent

Sending a push notification to a user's mobile device consists of three steps: 

- **Step 1:** the Mattermost server sends notifications to the [Mattermost Push Notification Service](https://github.com/mattermost/push-proxy) (MPNS).
- **Step 2:** The MPNS encrypts the message with a private key matching the public key registered with the mobile application and forwards the message to the push notification service of either Apple or Google. 
- **Step 3:** Apple or Google decrypts the message using the public key matching the MPNS server re-ecrypts the message and forwards it the user's mobile device.

Because the MPNS server connected to the pre-compiled Mattermost iOS App on iTunes and Mattermost Android App on Google Play needs to contain the private key for the native apps, a pre-compiled version of the MPNS server cannot be offered. 

Users need to either use a hosted service or compile their own MPNS and mobile apps (see below).

## Configuration options for push notifications

There are two options for setting up the MPNS to offer push notifications: 

- **Option A) Compile and deploy your own MPNS and mobile apps**  

   If your IT policy requires use of an Enterprise AppStore, or if you have expertise in mobile app development, you may choose to compile your own MPNS using the [open source repository](https://github.com/mattermost/push-proxy) provided, along with compiling the official open source [iOS app](https://github.com/mattermost/ios) or [Android app](https://github.com/mattermost/android). 

   Advantages: 
   - Fewer dependencies - All communication between Step 1 and Step 2 happens behind your firewall, only Step 3 happens outside your firewall. 

   Disadvantages:
   - Requires time and effort - An in-house developer would be required to properly compile, deploy and maintain the MPNS and mobile apps  

- **Option B) Use a hosted MPNS service**  

   Instead of compiling your own MPNS, you can put the address of a hosted MPNS supporting SSL into the **Push Notification Server** field inside the System Console and have your users install the iOS or Android native applications connected to the hosted service. 
   
   Advantages: 
   - Saves time - No need to compile open source applications 
   
   Disadvantages:
   - Requires trusting provider of hosted MPNS service - With this option, Step 2 happens outside of your firewall over an encrypted SSL connection which terminates at the MPNS. This means the MPNS decrypts the notification and re-encrypts it to send on to Step 3, so there is a moment when an unencrypted push notification message exists in the MPNS service. By default this is not an issue, since by default push notification messages only include generic descriptions and the names of users and channels (e.g. "@bob mentioned you in Town Square channel"). However, if in future you decide to enable push notifications to contain the contents from messages, you may need to review your internal IT policies to see whether Option A or Option B is most appropriate.

## Push notifications for Enterprise Edition customers

Subscriptions to Mattertmost Enterprise Edition include the use of a hosted, production-quality MPNS service with SSL, available at `https://push.mattermost.com`, which connects to the [official Mattermost iOS application on iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8) and the official Mattermost Android application in the Google Play Store (release pending).

## Push notifications for Team Edition users 

For users of Mattermost Team Edition, an additional MPNS service for testing server setups connected to the same mobile applications is available at `http://push-test.mattermost.com`. The test service can be used prior to compiling your own components from the open source repositories and does not include encryption for push notifications and does not offer a production-quality service-level agreement. 

If you choose to use the test service day-to-day, please subscribe to the [Mattermost announcement mailing list](https://mattermost.us11.list-manage.com/subscribe?u=6cdba22349ae374e188e7ab8e&id=2add1c8034) for updates on availability. 

Some users of Mattermost Team Edition have requested Mattermost.com provide a paid service for encrypted push notifications, as an alternative to compiling their own MPNS and mobile apps from the source code provided. If you're interested in such a service, please mail commercial@mattermost.com to be notified when it is available. 
