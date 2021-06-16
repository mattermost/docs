Client-side Data Storage FAQ
============================

Mobile Web Experience
---------------------

**1. What data is stored?**
  Similar to a desktop web browser, data may be stored in the mobile web browser cache which resides on the storage system of the device operating system which is protected by security measures in the physical device and its operating system.
**2. How is the data protected?**
  Security for mobile web experience is similar to the security for a desktop web experience.
**3. When is the data deleted?**
  If you log out or your account is deactivated, the data in the browser cache may reside until the cache expires or the temporary file system store on the operating system is cleared, depending on your operating system.


Mobile App Experience
---------------------

To speed up initial loading time, Mattermost mobile apps cache data locally on the device for v1.1 and later. Below are common questions on cached data: 

**1. What data is stored locally with the new mobile apps on a mobile device?**

  The data that can be found on the device depends solely on whether or not the user is logged in to the Mattermost server, and is independent of the state of the device's connection or the state of the app. While logged in, anything that the user is normally allowed to see is eligible for storage on the device, which includes the following content:

  - messages
  - files and images that are attached to messages
  - avatars, usernames, and email addresses of people in the currently open channel

  In addition, metadata that the app uses for keeping track of its operations is also cached. The metadata includes user IDs, channel IDs, team IDs, and message IDs.
  
  Currently, cache cannot be reset remotely on connected mobile devices.

**2. What about push notifications?**
  Push notification storage is managed by the operating system on the device. Mattermost can be configured to send limited amounts of information that does not include the message text or channel name, and it can also be configured to not send push notifications at all.

**3. Where is the data stored and how is that data protected?**
  The data is stored in the app's local storage. It is protected by the security measures that a device normally provides to the apps that are installed on it.

**4. How long is the data stored?**
  Data is stored until the user logs out, or until it is purged during normal cache management. Deactivating a user account forces a logout and subsequent purging of data from the device.

**5. Are messages pre-loaded?**
  No. Messages are sent to the device on demand. They are not pre-loaded in anticipation of users scrolling up or switching channels.

**6. What happens to messages that are deleted on the server after a user has seen them?**
  The messages are deleted from the client.

**7. What data is stored on a mobile device after an account is deactivated in the following cases:**
  1. *The mobile device is connected with app running.*
    All the data listed in Questions 1 and 2, but within 60 seconds after an account is deactivated on the server, all app data is deleted from the cache.
  2. *The mobile device is disconnected with app running.*
    All the data listed in Questions 1 and 2, but within 60 seconds after the device reconnects, all app data is deleted from the cache.
  3. *The mobile device is connected with the app not running.*
    All the data listed in Questions 1 and 2, but within 60 seconds after the app is started, all app data is deleted from the cache.
  4. *The mobile device is disconnected and app is not running.*
    All the data listed in Questions 1 and 2, but within 60 seconds after the device reconnects and the app is started, all app data is deleted from the cache.

**8. What data might be on the device after a user account is deactivated and all data is deleted from the cache?**
  If file attachments are enabled on the server, users can download files that are attached to messages and store them on their local file system. After they are downloaded, the files are outside the control of the app and can remain on the device indefinitely.
