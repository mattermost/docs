Mobile Security
================

Mattermost mobile is built with a robust security framework to protect user data and prevent unauthorized access. The Mattermost Mobile app's comprehensive security framework ensures that user data remains protected against unauthorized access.

Continuous compliance through :ref:`secure SDLC practices and proactive vulnerability management <deploy/mobile/mobile-security-features:security compliance>` further reinforces the platform’s resilience.

Mobile Device Management (MDM)
------------------------------

Mattermost supports the ability for an EMM provider to push Mattermost Mobile apps to EMM-enrolled devices. This approach is recommended for organizations that typically use EMM solutions to deploy Mobile apps to meet security and compliance policies. Learn more about :doc:`deploying Mattermost mobile using an EMM provider </deploy/mobile/deploy-mobile-apps-using-emm-provider>`.

Remote wipe capability
~~~~~~~~~~~~~~~~~~~~~~~

Administrators can remotely wipe Mattermost data from mobile devices in case of loss or theft. This capability prevents unauthorized access to sensitive information by ensuring that data is erased from compromised devices. 

Compliance policies
~~~~~~~~~~~~~~~~~~~~

Mattermost can be integrated with mobile device management solutions to enforce compliance policies. These policies ensure that mobile devices accessing the application adhere to security standards, such as encryption, password complexity, and device integrity. Learm more about :doc:`compliance with Mattermost </guides/compliance-with-mattermost>`.

Mobile access platforms
~~~~~~~~~~~~~~~~~~~~~~~

Mattermost mobile applications can be operated under the protection of mobile access platforms like `Hypori <https://www.hypori.com/>`_. These platforms provide an additional layer of security by creating a virtualized environment for mobile applications, ensuring that sensitive data is isolated from the device's operating system. This approach enhances data protection and minimizes the risk of data leakage or unauthorized access.

Jailbreak and root detection
-----------------------------

Jailbreaking or rooting a device disables many built-in security measures, making the device prone to malware and unauthorized access. This protection enables Mattermost administrators to deny access from any mobile device that appears to have been tampered with or is running a non-standard version of the operating system. Additionally, a rooted device may stop checking for software updates and security patches, and it might not be able to install them because the kernel is no longer properly signed. 

By detecting such devices, Mattermost ensures that only secure, uncompromised devices can access sensitive data. When enabled by the system admin, this proactive measure ensures the underlying mobile platform operates reliably and performs the expected kernel and operating system security protections before sending any customer data to the Mattermost application, and minimizes risk in environments where personal device security cannot be guaranteed. Learn more about Mattermost :ref:`mobile jailbreak and root detection <deploy/mobile/mobile-security-features:jailbreak and root detection>`.

Biometric authentication
------------------------

Native biometric authentication ensures only the authorized device owner can access the Mattermost application. By utilizing hardware-level security, biometrics significantly enhance data protection, especially in cases of lost or stolen devices. This advanced security measure is far more robust and user-friendly compared to traditional passwords, adding a resilient layer of protection against unauthorized access.

Administrators can mandate biometric authentication each time users attempt to open the Mattermost application, further safeguarding customer data and mitigating risks. Learn more about Mattermost :ref:`mobile biometric authentication <deploy/mobile/mobile-security-features:biometric authentication>`, and the :ref:`user workflows in which users must authenticate <configure/environment-configuration-settings:enable biometric authentication>`, when biometric authentication is enabled.

Screenshot and screen recording prevention
-------------------------------------------

Preventing screenshots and screen recordings protects sensitive information from being inadvertently or maliciously shared. This control is essential in ensuring that confidential communications and data remain within the secure confines of the app. By blocking unauthorized screen captures, Mattermost significantly reduces the risk of data leakage via visual content by preventing users from taking screenshots or recording their screens on the mobile device. This feature ensures that users can not intentionally or inadvertently capture an image of any information shared in Mattermost. Learn more about Mattermost :ref:`mobile screenshot and screen recording prevention <deploy/mobile/mobile-security-features:screenshot and screen recording prevention>`.

App sandboxing and secure data storage
---------------------------------------

Sandboxing is a critical defense that isolates the application’s data from other apps—even if malicious software is present on the device. This isolation helps maintain user privacy and data integrity by ensuring that only Mattermost has access to its stored data. Learn more about Mattermost :ref:`mobile app sandboxing and secure data storage <deploy/mobile/mobile-security-features:mobile data isolation>`.

Learn more about how Mattermost leverages robust sandboxing mechanisms on both iOS and Android to :doc:`securely store files </deploy/mobile/secure-mobile-file-storage>` in its cache folder within the application container, ensuring isolation from unauthorized third-party apps.

Push notification message visibility
------------------------------------

Push notifications are a convenient way to stay updated, but they can also pose security risks if sensitive information is displayed. Mattermost provides options to :ref:`control the visibility of message content in push notifications <configure/site-configuration-settings:push notification contents>`, ensuring that sensitive information is not inadvertently exposed through locked mobile screens and via relay servers from Apple and Google when sending notifications to iOS or Android mobile apps.

Disable downloads
-----------------

Environments with strict data loss prevention (DLP) policies or where sensitive information must not be stored on mobile devices can benefit from disabling file uploads and downloads on mobile devices. 

Disabling file uploads adds an additional layer of security by reducing the risk of malware or malicious files being introduced into the system, ensuring tighter control over sensitive corporate data, and preventing accidental leaks from unsecure mobile networks. 

Similarly, by disabling downloads, Mattermost ensures that files cannot be saved locally on the device, reducing the risk of unauthorized access or data leakage. Learn more about :ref:`disabling mobile uploads <configure/site-configuration-settings:allow file downloads on mobile>` and :ref:`disabling mobile downloads <configure/site-configuration-settings:allow file uploads on mobile>` in the Mattermost mobile app.