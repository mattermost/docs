..  _push_test:
Push Notifications and Mobile Devices
======

For Mattermost iOS apps and Android mobile apps to receive puch notifications the service sending notifications needs to be verified as an authorized sender. There are 3 options to provide this verification: 

1. Use the **Hosted Push Notification Service (HPNS)** from Mattermost.com that is trusted by Mattermost iOS and Android applications on iTunes and Google Play.

    - Pros: 
        - Push notifications are encrypted.
        - Saves time over deploying to an Enterprise App Store. 
        - Production quality uptime offered via commercial subscription. 		  
        - Commercial support from Mattermost.com included with subscription.
    - Cons: 
        - Some IT policies only allow mobile apps via Enteprise App Store.

2. Use an **Enterprise App Store (EAS)** by compiling your own push notification service and mobile applications from source code to manually establish verification.

    - Pros: 
        - Push notifications are encrypted.
        - Enterprise App Store provides the highest level of mobile apps security. 
        
    - Cons: 
        - Requires developer time to compile, secure, deploy and maintain components.

    EAS is most convenient when an organization has access to developers experienced in iOS mobile development, Android mobile development, Golang programming, Enterprise App Store administration and system security. 

3. Use the **Test Push Notification Service (TPNS)** and pre-compiled applications with unencrypted push notifications prior to selecting one of the above options.

    - Pros:
        - Easy and free solution to setting up and evaluating mobile apps.
    - Cons: 
        - Does not offer encrypted push notifications.
        - Not intended as a production quality service.
        - No commercial support from Mattermost.com

The below explains each option in detail. 

**Note:** By default, push notifications do not contain specific message contents. When the Mattermost server is installed, push notifications only give generic alerts like "@frank was mentioned in Town Square" but DO NOT display the contents of messages. The contents of messages are only included in push notifications after a System Administrator explicitly configure the option to include them. 


Hosted Push Notifications Service (HPNS)
-----

Mattermost.com offers a `Hosted Push Notification Service (HPNS) <https://about.mattermost.com/pre-compiled/>`_ via commercial subscription for organizations who want encrypted push notifications sent from behind their firewall, with production-quality uptime and commercial support, as an alternative to deploying their own Enterprise App Store (EAS) solution described below. 

With HPNS, end users can use publicly available iOS and Android mobile applications on iTunes and Google Play over encrypted connections: 

- `Mattermost iOS App on iTunes <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_
- `Mattermost Android App on Google Play <https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en>`_

`HPNS is available with Mattermost Enterprise Edition <https://about.mattermost.com/pricing/>`_. After purchasing and installing a license key, you can turn on HPNS using **System Console** > **Email Settings** > **Send Push Notifications** > **Use encrypted, production-quality HPNS connection to iOS and Android apps**.

Enterprise App Store (EAS)
-----

To set up an Enterprise App Store, teams can set up verified relationships by compiling, deploying, securing and maintaining the following open source repositories: 

- `Open source repository for the Mattermost Push Notification Service <https://github.com/mattermost/push-proxy>`_
- `Open source repository for the Mattermost iOS application <https://github.com/mattermost/ios>`_
- `Open source repository for the Mattermost Android application <https://github.com/mattermost/android>`_

After deploying the mobile applications and push notification service, go to **System Console** > **Email Settings** > **Send Push Notifications** > **Manually enter Push Notification Service location** and enter the location of your Push Notification Service in the **Push Notification Server** field. 

Test Push Notifications Service (TPNS) 
-----

Mattermost.com also offers a free, unencrypted push notification service for trying out the Mattermost mobile applications prior to deciding whether to use the EAS or HPNS option. 

End users of TPNS can use the publicly available iOS and Android mobile applications on iTunes and Google Play, with unencrypted push notifications: 

- `Mattermost iOS App on iTunes <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_
- `Mattermost Android App on Google Play <https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en>`_

You can connect to the TPNS by going to **System Console** > **Email Settings** > **Send Push Notifications** > **Use iOS and Android apps on iTunes and Google Play with TPNS.**

Note: TPNS is a test service that does not encrypt push notifications and does not offer production-quality uptime. 

What happens when a Mattermost push notification is sent? 
``````

To ensure only push notifications from authorized senders are processed by iOS and Android mobile application, each push notifications need to come from a trusted source.  

Here is the full process: 

1. When triggered, a push notification is sent from the Mattermost server to the Mattermost Push Notification Service over TLS

2. The Mattermost Push Notification Service forwards the message to either Apple Push Notification Service (APNS) or to the Google Cloud Messaging (GCM) service depending on whether you're sending to an iOS or Android device. The message from the Mattermost Push Notification Service is signed with a key that's registered with the recieving service, corresponding to the target mobile app, so its authenticity is verified. 
 
3. The APNS or GCM service confirms that the message from the Mattermost Push Notification Service is authorized for the target mobile application and forwards the message to the app to be displayed. 
