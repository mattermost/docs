# Push Notifications and Mobile Devices 

To send push notifications from your private cloud to iOS apps and Android mobile apps, Apple and Google require a key to be compiled into your mobile applications.  

There are 3 options for configuring push notifications to your Mattermost mobile apps: 

1. Use a **Hosted Push Notification Service (HPNS)** and pre-compiled mobile applications using a key secured by Mattermost.com. 

    - Pros: 
        - Push notifications are encrypted.
        - Saves time over deploying to an Enterprise App Store. 
        - Service level agreement offered via commercial subscription. 		  

    - Cons: 
        - Some IT policies only allow mobile apps via Enteprise App Store.

2. Use an **Enterprise App Store (EAS)** by compiling your own push notification service and mobile applications from source code with your own encryption key.

    - Pros: 
        - Push notifications are encrypted.
        - Enterprise App Store provides the highest level of mobile apps security. 

    - Cons: 
        - Requires developer time to compile your organization's encryption key into the open source components and to deploy.

3. Use the **Test Push Notification Service (TPNS)** and pre-compiled applications with unencrypted push notifications prior to selecting one of the above options.

    - Pros:
        - Easy and free solution to setting up and evaluating mobile apps.

    - Cons: 
        - Does not offer encrypted push notifications.
        - Does not offer service level agreement.
  
To explain each option in detail: 

## Hosted Push Notifications Service (HPNS) 

Mattermost.com offers a [Hosted Push Notification Service (HPNS)](https://about.mattermost.com/pre-compiled/) for organizations who prefer using a hosted commercial service over deploying Mattermost mobile applications into an on-premises Enterprise App Store. 

With HPNS, end users can use publicly available iOS and Android mobile applications on iTunes and Google Play over encrypted connections: 

- [Mattermost iOS App on iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8)
- [Mattermost Android App on Google Play](https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en)

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

