Desktop App Deployment
=======================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

The Mattermost desktop app is available for Windows, macOS, and Linux operating systems, and offers :doc:`additional functionality </end-user-guide/preferences/customize-desktop-app-experience>` beyond the web-based experience.

Learn more about desktop app :ref:`software requirements <deployment-guide/software-hardware-requirements:desktop apps>`, :doc:`releases and server compatibility </product-overview/mattermost-desktop-releases>` as well as the :doc:`what's changed across releases </product-overview/desktop-app-changelog>`.

Privacy and data handling
--------------------------

Error reporting (v6.1.0 and later)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost Desktop v6.1.0, the desktop app includes automatic error reporting to help identify and fix crashes and stability issues. This feature sends error data to Sentry, a third-party error tracking service.

**Default behavior**

- Error reporting is **enabled by default** for all users
- Error reports help Mattermost identify and fix desktop app issues proactively
- Users can disable error reporting via **Settings > Advanced > Send error reports to help improve the app**

**Data collected**

Error reports include:

- Crash information and stack traces
- App version and build information
- Platform details (OS type, architecture, memory stats)
- Error messages and context

**Privacy protections**

- **No personally identifiable information (PII)** is included in error reports
- Message content, user credentials, and authentication tokens are not sent
- Error reporting only activates in production/release builds (not in development or test builds)

**Organizational considerations**

If your organization has policies restricting external telemetry or data transmission:

1. **Communicate with users**: Inform users about this default-enabled feature and provide guidance on whether to disable it based on your organization's data handling policies
2. **User control**: Users can disable error reporting at any time through the desktop app Settings. The setting requires an app restart to take effect
3. **Compliance considerations**: Organizations subject to data residency requirements or strict data handling policies should evaluate whether Sentry's error tracking aligns with their compliance needs

For more information on disabling error reporting, see the :doc:`desktop app troubleshooting guide </deployment-guide/desktop/desktop-troubleshooting>`. For comprehensive privacy and compliance information, see :doc:`Desktop app privacy and data handling </deployment-guide/desktop/desktop-app-privacy>`.

Download
---------

Download and install the Mattermost desktop app from the `App Store (macOS) <https://www.apple.com/app-store/>`_, `Microsoft Store (Windows) <https://apps.microsoft.com/home?hl=en-US&gl=US>`_, or by :doc:`using a package manager (Linux) </deployment-guide/desktop/linux-desktop-install>`. We strongly recommend installing the desktop app on a local drive. Network shares aren't supported.

In Matermost, users are notified under **Downloads** when new desktop app releases become available. If managing the distribution of the mobile app on behalf of users, you can recommend that your users disable desktop update notifications by going to **… > File > Settings** on Windows or **Mattermost > Settings** on Mac and clearing the **Automatically check for updates** option.

See additional deployment options below to manage distribution of the mobile app to your users.

Deployment options
------------------

Learn about installation, configuration, and management options for deploying the desktop app in your environment.

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    /deployment-guide/desktop/linux-desktop-install.rst
    /deployment-guide/desktop/distribute-a-custom-desktop-app.rst
    /deployment-guide/desktop/silent-windows-desktop-distribution.rst
    /deployment-guide/desktop/desktop-msi-installer-and-group-policy-install.rst
    /deployment-guide/desktop/desktop-custom-dictionaries.rst
    /deployment-guide/desktop/desktop-app-managed-resources.rst
    /deployment-guide/desktop/desktop-app-privacy.rst
    /deployment-guide/desktop/desktop-troubleshooting.rst

* :doc:`Distribute a custom desktop app </deployment-guide/desktop/distribute-a-custom-desktop-app>`
* :doc:`Silent Windows desktop distribution </deployment-guide/desktop/silent-windows-desktop-distribution>`
* :doc:`MSI installer and group policy guide </deployment-guide/desktop/desktop-msi-installer-and-group-policy-install>`
* :doc:`Custom dictionaries for Windows and Linux </deployment-guide/desktop/desktop-custom-dictionaries>`
* :doc:`Managed resources for the desktop app </deployment-guide/desktop/desktop-app-managed-resources>`
* :doc:`Desktop app privacy and data handling </deployment-guide/desktop/desktop-app-privacy>`
* :doc:`Desktop app troubleshooting </deployment-guide/desktop/desktop-troubleshooting>`