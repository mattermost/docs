# Push Notifications and Mobile Devices 

To send push notifications from your private cloud to iOS apps and Android mobile apps, Apple and Google require a unique key to be compiled into your mobile applications. There are 3 deployment options: 

1. Use a **Hosted Push Notification Service (HPNS)** and pre-compiled mobile applications using a key secured by Mattermost.com. 

    - Pros: 
        - Push notifications are encrypted.
        - Saves time over deploying to an Enterprise App Store. 
        - Service level agreement offered via commercial subscription. 		  

    - Cons: 
        - Some IT policies only allow mobile apps via Enteprise App Store.

2. Use an **Enterprise App Store (EAS)** by compiling your own push notification service and mobile applications from source code with your own key.

    - Pros: 
        - Push notifications are encrypted.
        - Enterprise App Store provides the highest level of mobile apps security. 

    - Cons: 
        - Requires developer time to compile your organization's encryption key into the open source components and to deploy.

    EAS is most convenient when an organization has access to developers experienced in iOS mobile development, Android mobile development, Golang programming, and Enterprise App Store administration. 

3. Use the **Test Push Notification Service (TPNS)** and pre-compiled applications with unencrypted push notifications prior to selecting one of the above options.

    - Pros:
        - Easy and free solution to setting up and evaluating mobile apps.

    - Cons: 
        - Does not offer encrypted push notifications.
        - Does not offer service level agreement.
  
To explain each option in detail: 

## Hosted Push Notifications Service (HPNS) 

Mattermost.com offers a [Hosted Push Notification Service (HPNS)](https://about.mattermost.com/pre-compiled/) via commercial subscription for organizations who prefer using a hosted service to deploying to an Enterprise App Store. 

With HPNS, end users can use publicly available iOS and Android mobile applications on iTunes and Google Play over encrypted connections: 

- [Mattermost iOS App on iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8)
- [Mattermost Android App on Google Play](https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en)

HPNS is included with an Enterprise Edition E1 subscription and can also be purchased separately. 

## Enterprise App Store (EAS)

To set up an Enterprise App Store, teams can compile an encryption key exclusive to their deployment into the following open source Mattermost repositories: 

- [Open source repository for the Mattermost Push Notification Service](https://github.com/mattermost/push-proxy)
- [Open source repository for the Mattermost iOS application](https://github.com/mattermost/ios)
- [Open source repository for the Mattermost Android application](https://github.com/mattermost/android) 

## Test Push Notifications Service (TPNS) 

Mattermost.com also offers a free, unencrypted push notification service for trying out the Mattermost mobile applications prior to deciding whether to use the EAS or HPNS option. 

End users of TPNS can use the publicly available iOS and Android mobile applications on iTunes and Google Play, with unencrypted push notifications: 

- [Mattermost iOS App on iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8)
- [Mattermost Android App on Google Play](https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en)

You can connect to the TPNS by entering `http://push-test.mattermost.com` into **System Console** > **Email Settings** > **Push Notification Server**.

#### Important notes on TPNS

1. **By default, unencrypted push notifications do not expose message-specific data.**  When the Mattermost server is installed, push notifications only give generic alerts like "@frank was mentioned in Town Square" but DO NOT display the contents of messages. The contents of messages are only included in push notifications after a System Administrator explicitly configure the option to include them. 

2. **There is no service level agreement on the TPNS.** It may go down without notice, change or be discontinued. 

### What happens when a Mattermost push notification is sent? 

To ensure only messages from authorized senders are received by a mobile application, each push notifications need to be signed with a private key corresponding to a public key registered with either Apple (for iOS) or Google (for Android). This means each mobile app needs its own key in order to trust messages from the Mattermost server in your private cloud. 

Here is the full process: 

1. When triggered, a push notification is sent from the Mattermost server to the Mattermost Push Notification Service over TLS

2. The Mattermost Push Notification Service decrypts the message, signs it with a private key verifying it as a valid message for the target mobile app (which is registered with the corresponding public key), then encrypts the push notification to send to the Apple Push Notification Service (APNS) or to the Google Cloud Messaging (GCM) service depending on whether you're sending to an iOS or Android device. 
 
3. The APNS or GCM service decrypts the message, uses the public key registered with the mobile app to verify the notification is from an authorized source, then encrypts the message and sends it to the appropriate mobile device where it is decrypted and displayed to the user.
