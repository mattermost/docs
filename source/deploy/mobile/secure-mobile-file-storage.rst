Secure file storage
====================

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

This document outlines the security measures governing file storage in the Mattermost mobile app for iOS and Android. It describes how files are stored, accessed, and protected within the application container, addressing concerns related to sensitive data—including Controlled Unclassified Information (CUI) and HIPAA-regulated data—on mobile devices. The objective is to ensure that only authorized personnel can view, access, or share such data while preventing exposure to unauthorized parties and ensuring isolation from third-party applications.

Mattermost leverages robust sandboxing mechanisms on both iOS and Android to securely store files in its cache folder within the application container, ensuring isolation from unauthorized third-party apps. User-initiated actions (download, share, copy link) are controlled by server-side permissions, allowing administrators to restrict access to sensitive data like CUI or HIPAA-regulated information to authorized personnel only. 

File storage and app sandbox security
-------------------------------------

Files uploaded or accessed via the Mattermost mobile app are stored in the app’s cache folder, which resides within the app’s private storage container. This storage location is isolated by each platform’s sandboxing model:

iOS – app sandbox
~~~~~~~~~~~~~~~~~~

- **Sandboxing & storage:**

  iOS employs a rigorous sandboxing model that relies on containerized file systems and strict process isolation. Each app operates within its own sandbox, with its home directory randomly assigned during installation. As a result, files stored within the Mattermost app’s cache folder remain accessible only to the app unless explicitly shared by the user.

- **Secure file viewing:**

  - Non-image and non-video files are rendered using secure frameworks such as QLPreviewController. This controller displays file previews within the app’s sandbox, ensuring that raw file data isn’t exposed to external processes.
  - Supported image and video files are previewed directly within the app, with the files downloaded to the app's cache folder located within its secure sandbox. For unsupported image and video formats, the Mattermost mobile app uses the QLPreviewController framework, just as it does for other file types.
  - If the file format is also unsupported by QLPreviewController and :ref:`mobile downloads are enabled <configure/site-configuration-settings:allow file downloads on mobile>` on the server, users can download the file to a location of their choosing. However, if mobile downloads are disabled, these files become unavailable to the user.

- **Official references:**

  - `Apple App Sandbox Design Guide <https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html>`_
  - `Security of runtime process in iOS, iPadOS and visionOS <https://support.apple.com/en-gb/guide/security/sec15bfe098e/web>`_
  - `Apple Security Guide <https://help.apple.com/pdf/security/en_GB/apple-platform-security-guide-b.pdf>`_

Android – scoped storage
~~~~~~~~~~~~~~~~~~~~~~~~

- **Sandboxing & storage:**

  Android employs scoped storage by assigning each app its own Linux user ID and a dedicated private directory. This model prevents other applications from accessing an app’s cache without explicit permission. As a result, the Mattermost app’s files remain inaccessible to other apps—unless the device is rooted, or the user explicitly shares the data.

- **Secure file viewing:**

  - When users attempt to view non-image/video files, Mattermost uses an ``Intent.ACTION_VIEW`` to open the file. This intent delegates rendering to an external app only if the user explicitly triggers the action, while the file remains securely stored within Mattermost’s cache folder.
  - Viewing non-image/video files is available only if :ref:`mobile downloads are enabled <configure/site-configuration-settings:allow file downloads on mobile>` on the server.
  - Image and video files with supported formats are previewed directly within the app, with the files downloaded to the app's cache folder located within its secure sandbox. For unsupported image and video formats, the Mattermost mobile app uses ``Intent.ACTION_VIEW`` to open the file with an external application, just as it does for other file types.

- **Official reference:**

  - `Scoped Storage <https://developer.android.com/about/versions/10/privacy/changes#scoped-storage>`_

Additionally, both platforms may clear cached data automatically (e.g., under low storage conditions or upon user logout), thereby reducing the risk of sensitive information like CUI remaining on the device.

Differentiating file handling to external applications
------------------------------------------------------

- **Previewing files:** 

  File previewing follows the secure viewing practices described above in the “Secure File Viewing” sections for iOS and Android. All files prior to being previewed are stored in the cache folder of the Mattermost app sandbox. Images and videos with supported formats are previewed directly within the Mattermost mobile app. Non‑image and non‑video files are also previewed in-app in iOS but are handed off to an external application in Android while the raw data remains securely stored in the app’s cache. Previewing non-image/non-video files is possible only if :ref:`mobile downloads are enabled <configure/site-configuration-settings:allow file downloads on mobile>` on the server side.

- **Downloading files:**

  - When a user initiates a file download, the file is first stored in Mattermost’s private cache directory. The user is then immediately prompted to save it to another destination via platform-specific sharing methods.
  - On **iOS** devices:

    - The built-in sandboxing ensures that the downloaded files remain inaccessible to other apps unless the user explicitly shares or saves them through the system’s file sharing mechanisms. Once downloaded, the file appears in the gallery.
    - If the server has the download setting enabled, the user has two options:

      1. Download the file: Opens the **Files** app, allowing the user to save the file to any permitted location, including iCloud.
      2. Share the file: Launches the native share sheet, enabling the user to share the file with other compatible applications.

  - On **Android** devices, the app employs the system’s file picker. This allows the end-user to select a preferred storage location. Once saved, the file becomes accessible to other apps based on the chosen location and the device’s file sharing permissions.

File accessibility options
---------------------------

Depending on server configuration, users may download files, share them, or copy a public link directly from the Mattermost mobile app. These actions are always user‑initiated, ensuring that sensitive data is only exposed with explicit consent. 

Additionally, administrators have the option to restrict mobile file uploading and downloading to ensure that sensitive content remains within approved channels. When mobile file downloads are disabled, the app allows only image and video file previews. However, if general file sharing is enabled on the Mattermost server, file operations via mobile browsers will still be possible.

Layered defense strategies for sensitive eata
----------------------------------------------

Mattermost is designed to protect sensitive data—such as CUI and HIPAA-regulated information—by ensuring that only authorized personnel can access or share it. The platform combines secure mobile app features with powerful server-side controls, providing a layered defense that minimizes the risk of data exposure.

Core defense pillars
~~~~~~~~~~~~~~~~~~~~~

- **Robust authentication:** Mattermost requires user authentication through SSO (e.g., SAML, LDAP, OpenID Connect) or traditional username/password logins. This authentication is managed by server-side identity controls, ensuring that only verified users can access the app and its data. For more details, see the `Mattermost Security Overview <https://docs.mattermost.com/about/security.html#authentication-safeguards>`_.

- **Server-side access controls:** Administrators can enforce policies through the System Console to restrict file downloads, sharing, and public link generation. Currently, policies are applied at the server level. For more details, see `Configuration Settings - File Sharing and Downloads <https://docs.mattermost.com/configure/site-configuration-settings.html#file-sharing-and-downloads>`_.

- **Sandbox isolation:** As discussed earlier, Mattermost’s mobile apps store files in a sandboxed environment. This isolation ensures that even if a device is shared or compromised, other apps cannot access the cached files without explicit user action.

- **Controlled file previews:** File previews (via QLPreviewController on **iOS** or open intent on **Android**) occur within the application’s controlled environment or delegate to OS-approved apps without duplicating sensitive data outside the sandbox.

- **OS-Level encryption:** While files in the cache folder are stored unencrypted by default, they are protected at rest by OS-level encryption (iOS File Data Protection and Android Full Disk Encryption).

By combining strict authentication, server-side controls, sandbox isolation, and secure file handling, Mattermost ensures that sensitive data remains confined to authorized users, with access and sharing tightly controlled by server policies, platform security features, and explicit user consent.

Testing procedure to validate file isolation
---------------------------------------------

The playbook below aims to test and confirm that files stored in the Mattermost app’s private cache folder—where sensitive data like CUI may reside—are not accessible by unauthorized third-party applications. The tests are designed to show that while public directories, such as Downloads/ can be accessed, the private Mattermost cache remains isolated unless a file is explicitly shared by an authorized user.

1. **Preparation**

   - On **Android**:
      - Install Adobe Acrobat Reader for PDF viewing.
      - Install Files by Google as a file manager.
      - Install Google Chrome as a system browser.
   - On **iOS**:
      - Install Adobe Acrobat Reader (from the App Store).
      - Use the built-in Files app.
      - Use Safari as the default browser.
   - Any PDF viewer, file manager, or browser can be used for these steps.
   
2. **Control test: Verify public directory accessibility**

   - **Android:**
      - Open Files by Google.
      - Navigate to a known public directory (e.g., Downloads/).
      - Confirm that files in this location are visible and can be opened.

   - **iOS:**
      - Open the Files app.
      - Browse to an accessible directory (e.g., iCloud Drive or “On My iPhone” public folders).
      - Confirm these files are accessible.

   This step demonstrates that allowed directories can be accessed, setting a baseline for comparison.

3. **Attempt unauthorized access to Mattermost’s private cache**

   - **Android:**
      - In Files by Google, try navigating through the directory structure to identify files of the Mattermost application.
      - Verify that you cannot access private directories such as Mattermost app’s private cache folder.

   - **iOS:**
      - Open the Files app.
      - Verify that the Mattermost app’s private cache folder does not appear under “On My iPhone/iPad.”

4. **Attempt unauthorized access to a specific file in Mattermost’s private cache**

   - **Android:**
      - Use the search functionality in Files by Google to search for a known file name from the Mattermost cache.
      - Verify that the file does not appear in search results.

   - **iOS:**
      - Use the Files app’s search capability to look for a specific file name from the Mattermost cache.
      - Confirm that the file does not appear in search results.

5. **Attempt authorized access to downloaded file**

   - **Android:**
      - Confirm that mobile downloads are enabled on the server.
      - Download a file using the Mattermost mobile app.
      - Open the Files by Google app and verify that the downloaded file is visible and opens correctly.

   - **iOS:**
      - Confirm that mobile downloads are enabled on the server.
      - Download a file using the Mattermost mobile app.
      - Open the iOS Files app and verify that the downloaded file appears and can be opened successfully.

6. **Repeat across multiple apps and devices**

   The steps above use the Files app of Google and iOS. Repeat these tests using each suggested app on different devices and OS versions (both Android and iOS) to ensure that the private cache folder remains inaccessible under all conditions.

Test execution & findings
--------------------------

Mattermost executed the playbook above, including scanning for hidden files, both during normal operation and after forcing the app to stop or crash, and observed the following results:

- **Devices Tested**: iPhone 12, iOS 18.4, Android 11 
- **Apps Used**: Adobe Reader, Google Files app, Android’s native Files app, iOS Files app, Files Media Manager, Hidden Files Finder, Hidden Files Finder & Recover
- **Results**: Third-party file browsers and recovery tools consistently failed to access the Mattermost app’s cache folder or its contents. Access was only possible when files were explicitly downloaded or shared via Mattermost’s controlled functionality by an authorized user.
- **Outcome**: Files remain isolated within the app container, adhering to platform security guidelines and protecting against unauthorized access.  

The documented testing procedures confirm that the app’s file storage remains inaccessible to unauthorized third-party applications, thereby maintaining a strong security posture. Coupled with strong authentication and native OS encryption, the Mattermost mobile app provides a robust framework that keeps sensitive data on mobile devices confined to authorized users while addressing key access control and risk mitigation requirements.