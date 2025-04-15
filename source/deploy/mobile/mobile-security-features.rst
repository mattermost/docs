Mobile Security Features
========================

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Mobile is built with a robust security framework to protect user data and prevent unauthorized access. This document outlines the key security features implemented in the mobile application, explains the significance of each control, and details our continuous security practices to maintain an up-to-date security posture.

Jailbreak and root detection
-----------------------------

Jailbreaking or rooting a device disables many built-in security measures, making the device prone to malware and unauthorized access. Additionally, a rooted device may stop checking for software updates and security patches, and it might not be able to install them because the kernel is no longer properly signed. 

By detecting such devices, Mattermost ensures that only secure, uncompromised devices can access sensitive data. If enabled by the system admin, this proactive measure minimizes risk in environments where personal device security cannot be guaranteed. 

Mattermost leverages built-in checks from the Expo framework to identify jailbroken (iOS) and rooted (Android) devices:

- On **Android**, the app looks for the presence of known jailbreak/root binaries —such as the "su" binary in /system/xbin/su, which is a common indicator that the device has been rooted to allow unauthorized elevated access. 
- On **iOS**, the detection process involves checking for unusual apps (e.g., Cydia), modified system paths, and testing whether the app can alter protected system files—all signs that the device may be jailbroken.

See the :ref:`jailbreak/root protection configuration setting <configure/environment-configuration-settings:enable jailbreak/root protection>` documentation for details on enabling this feature.

.. note::

    Client-side detection methods are not bulletproof and can be bypassed by a sufficiently motivated user with root or jailbreak access. Determined users can employ reverse engineering to disable or modify these checks to produce false positives/negatives or even modify and recompile the source code to remove them entirely, allowing app usage on rooted/jailbroken devices. 

Biometric authentication
------------------------

Biometric authentication significantly enhances security by ensuring that even if a device is lost or stolen, only an authorized user can access the application. It leverages the strengths of hardware-level security, making it far more challenging for attackers to bypass compared to traditional passwords. Biometrics add a layer of security that is both user-friendly and resistant to unauthorized access, especially in a mobile context. 

Mattermost integrates with iOS Face ID/Touch ID and Android’s Biometric API. When enabled by the server administrator, biometric checks are required before accessing specific servers, and the Mattermost mobile app mandates that a device PIN or biometric lock is active.

See the :ref:`biometric authentication configuration setting <configure/environment-configuration-settings:enable biometric authentication>` documentation for details on enabling this feature.

.. note::

    Biometric authentication, such as Face ID or fingerprint recognition, is handled by the device’s operating system. Mattermost does not provide or warrant the biometric functionality. The app will unlock if the OS determines that the biometric input is a positive match. Accuracy, security, and availability of biometric authentication depend entirely on the device and its underlying platform. 

Screenshot and screen recording prevention
-------------------------------------------

Preventing screenshots and screen recordings protects sensitive information from being inadvertently or maliciously shared. This control is essential in ensuring that confidential communications and data remain within the secure confines of the app. By blocking unauthorized screen captures, Mattermost significantly reduces the risk of data leakage via visual content. 

- On **iOS**, the app detects attempts to capture the screen. For screen recordings, it immediately applies a blur overlay to the view to obscure any sensitive information, while screenshots will capture no content at all. 

- On **Android**, the app utilizes the FLAG_SECURE flag to block screen captures and recordings. 

See the :ref:`prevent screen capture configuration setting <configure/environment-configuration-settings:prevent screen capture>` documentation for details on enabling this feature.

.. note::

    This feature prevents screen recording and screenshot capture on the mobile device where the Mattermost app is running. It cannot control or prevent recording from external devices, such as another phone or camera pointed at the screen. Mattermost provides these protections through mobile OS-level capabilities but cannot guarantee absolute prevention of visual data capture through other means.  

App sandboxing and secure data storage
---------------------------------------

Sandboxing is a critical defense that isolates the application’s data from other apps—even if malicious software is present on the device. This isolation helps maintain user privacy and data integrity by ensuring that only Mattermost has access to its stored data. 

Mattermost stores 3 types of data within the mobile app: 

- **SQLite Database**: For offline access to posts and channels that the user has viewed.
- **Cached Files**: For temporary storage (e.g., PDFs) of viewed files. They are periodically purged. 
- **Logs**: Minimal logs kept for troubleshooting purposes.

Security measures
~~~~~~~~~~~~~~~~~~

- **OS sandboxing & app access isolation**: Mattermost’s data is confined within its app-specific sandbox (see `Apple’s iOS sandboxing <https://support.apple.com/guide/security/security-of-runtime-process-sec15bfe098e/web>`_ and `Android’s sandboxing <https://source.android.com/docs/security/app-sandbox>`_ guidelines). This sandboxing mechanism ensures that all stored data—whether in the SQLite databases, cached files, or logs—is isolated and inaccessible to other applications. This is why TikTok, and any other application is blocked from accessing Mattermost data. 

  - **iOS** employs a rigorous sandboxing model that relies on containerized file systems and strict process isolation. Each app operates within its own sandbox, with its home directory randomly assigned during installation. As a result, data stored within the Mattermost app’s sandbox directory remains accessible only to the app unless explicitly shared by the user. 

  - **Android** employs scoped storage by assigning each app its own Linux user ID and a dedicated private directory. This model prevents other applications from accessing an app’s private directory without explicit permission. As a result, the Mattermost app’s data remain inaccessible to other apps—unless the device is rooted, or the user explicitly shares the data.

  - Learn more about how Mattermost leverages robust sandboxing mechanisms on both iOS and Android to :doc:`securely store files </deploy/mobile/secure-file-storage>` in its cache folder within the application container, ensuring isolation from unauthorized third-party apps.

- **Cache invalidation**: Cached files are periodically deleted.   

- **No Google or Apple Cloud backup**: Mattermost files are not backed up during normal cloud backup procedures.  

  - On **Android**, the application explicitly disables backups (using the appropriate manifest settings), ensuring that all Mattermost files remain strictly on-device. 

  - On **iOS**, although the operating system automatically backs up files stored in the app's "Documents" folder, Mattermost intentionally stores its files in the "Library/Caches" directory, which is excluded from iCloud backups. 

- **Controlled data export**: Data only leaves Mattermost through explicit user actions such as: 

  - Manually exporting a file.
  - Takes a screenshot (if not blocked by policy or with a secondary camera).
  - Sharing content using OS features (e.g., share sheet).


.. note::

    This feature restricts direct access to stored data through robust OS-level sandboxing and storage controls. However, it cannot prevent unauthorized extraction if attackers employ alternative methods. For instance, on jailbroken (iOS) or rooted (Android) devices, where system integrity is compromised, an attacker may bypass standard security measures. 

    Similarly, exploiting zero-day or known OS vulnerabilities—or malicious apps that exploit permission weaknesses—could grant access to device storage. Mattermost uses mobile OS-level safeguards but cannot guarantee absolute prevention of such unauthorized data access. 

Security compliance
--------------------

- **Secure SDLC**: The mobile app adheres to the same secure Software Development Lifecycle (SDLC) process as all Mattermost components. This guarantees that new mobile features undergo comprehensive security reviews and that any issues are addressed before release. 

- **Vulnerability management**: The Mattermost mobile app is included in Mattermost’s public bug bounty program, inviting security researchers to rigorously assess the application. Additionally, established remediation SLAs ensure that any security issues are resolved promptly. 

- **Continuous dependency scanning**: Mattermost uses Snyk Open Source to conduct daily scans of all dependencies. This continuous approach ensures that any newly disclosed vulnerabilities are quickly identified and addressed within defined SLAs.  

- **BESPIN compliance**: Mattermost adheres to strict security evaluations including: 

  - Device Protection Profiles (NIAP Evaluation)
  - Security Dependency & Code Analysis
  - Code Complexity & Testing Standards