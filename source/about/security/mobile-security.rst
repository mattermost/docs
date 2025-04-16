Mobile Security
================

Mattermost Mobile is built with a robust security framework to protect user data and prevent unauthorized access. The Mattermost Mobile app's comprehensive security framework ensures that user data remains protected against unauthorized access.

Continuous compliance through :ref:`secure SDLC practices and proactive vulnerability management <about/security/mobile-security-features:security compliance>` further reinforces the platform’s resilience.

As the mobile app evolves with future enhancements like file sharing restrictions, Mattermost is committed to delivering a secure, reliable mobile experience.

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    Mobile security features </about/security/mobile-security-features>
    Secure mobile file storage </about/security/secure-mobile-file-storage>

Jailbreak and root detection
-----------------------------

Jailbreaking or rooting a device disables many built-in security measures, making the device prone to malware and unauthorized access. Additionally, a rooted device may stop checking for software updates and security patches, and it might not be able to install them because the kernel is no longer properly signed. 

By detecting such devices, Mattermost ensures that only secure, uncompromised devices can access sensitive data. If enabled by the system admin, this proactive measure minimizes risk in environments where personal device security cannot be guaranteed. Learn more about Mattermost mobile :ref:`jailbreak and root detection <about/security/mobile-security-features:jailbreak and root detection>`.

Biometric authentication
------------------------

Biometric authentication significantly enhances security by ensuring that even if a device is lost or stolen, only an authorized user can access the application. It leverages the strengths of hardware-level security, making it far more challenging for attackers to bypass compared to traditional passwords. Biometrics add a layer of security that is both user-friendly and resistant to unauthorized access, especially in a mobile context. Learn more about Mattermost mobile :ref:`biometric authentication <about/security/mobile-security-features:biometric authentication>`.

Screenshot and screen recording prevention
-------------------------------------------

Preventing screenshots and screen recordings protects sensitive information from being inadvertently or maliciously shared. This control is essential in ensuring that confidential communications and data remain within the secure confines of the app. By blocking unauthorized screen captures, Mattermost significantly reduces the risk of data leakage via visual content. Learn more about Mattermost :ref:`mobile screenshot and screen recording prevention <about/security/mobile-security-features:screenshot and screen recording prevention>`.

App sandboxing and secure data storage
---------------------------------------

Sandboxing is a critical defense that isolates the application’s data from other apps—even if malicious software is present on the device. This isolation helps maintain user privacy and data integrity by ensuring that only Mattermost has access to its stored data. Learn more about Mattermost :ref:`mobile app sandboxing and secure data storage <about/security/mobile-security-features:app sandboxing and secure data storage>`.

Learn more about how Mattermost leverages robust sandboxing mechanisms on both iOS and Android to :doc:`securely store files </about/security/secure-mobile-file-storage>` in its cache folder within the application container, ensuring isolation from unauthorized third-party apps.

