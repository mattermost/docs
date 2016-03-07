# Push Notifications

This section explains how push notifications work with pre-compiled iOS and Android applications. 

See [Push Notification Settings](http://docs.mattermost.com/administration/config-settings.html#push-notification-settings) to configure the settings for use with: 

- [Mattermost iOS App on iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8)
- Mattermost Android App on Google Play (pending release)

## Why do push notifications seem so complicated? 

iOS apps require a private key issued by Apple for each iOS app in order to receive push notifications. To self-host Mattermost, teams need to request their own key from Apple to be used from behind their firewall. 

Mattermost provides:  
1. Source code to use your own key with your own iOS apps in an Enterprise App Store, or as an Android .apk file.  
2. A free test service, http://push-test.mattermost.com, for you to use pre-compiled iOS and Android apps for testing before your compiled your own.  
3. As an alternative to compiling your own, a [commercial service](https://about.mattermost.com/pre-compiled/) with pre-compiled apps and an encrypted push notification service is available.

The following explains the details of how mobile applications and push notifications are set up. 

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

   Trade-offs:
   - Requires time and effort - An in-house developer would be required to properly compile, deploy and maintain the MPNS and mobile apps.

   For Team Edition users, prior to compiling your own applications and MPNS service, you can set your Push Notification Service to `http://push-test.mattermost.com` in the System Console to test your deployment using the iOS app on iTunes and Android app on Google Play. This is a test-quality, unencrypted push notification service that is not recommended for production use. If you use the service on a day-to-day basis, please make sure to join the [Mattermost announcement mailing list](https://mattermost.us11.list-manage.com/subscribe?u=6cdba22349ae374e188e7ab8e&id=2add1c8034) for updates on availability. 

- **Option B) Use the Mattermost Pre-compiled Mobile Applications Service (MPMAS)**  

   Instead of compiling your own MPNS and mobile apps, you can purchase a subscripton to the [Mattermost Pre-compiled Mobile Application Service (PMAS)](https://about.mattermost.com/pre-compiled/) and have your users install the [iOS app from iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8) or the Android app from Google Play (release pending). 
   
   Advantages: 
   - Saves time - No need to compile open source applications 
   
   Trade-offs:
   - Team Edition users incur an additional financial cost (Enterprise Edition customers do not incur additional cost, since the service is included with their subscription). 
   - As with any hosted service, MPMAS is a dependency that exists outside your firewall.
