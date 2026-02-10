Desktop App Deployment
=======================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

The Mattermost desktop app is available for Windows, macOS, and Linux operating systems, and offers :doc:`additional functionality </end-user-guide/preferences/customize-desktop-app-experience>` beyond the web-based experience.

Learn more about desktop app :ref:`software requirements <deployment-guide/software-hardware-requirements:desktop apps>`, :doc:`releases and server compatibility </product-overview/mattermost-desktop-releases>` as well as the :doc:`what's changed across releases </product-overview/desktop-app-changelog>`.

Download
---------

Download and install the Mattermost desktop app from the `App Store (macOS) <https://www.apple.com/app-store/>`_, `Microsoft Store (Windows) <https://apps.microsoft.com/home?hl=en-US&gl=US>`_, or by :doc:`using a package manager (Linux) </deployment-guide/desktop/linux-desktop-install>`. We strongly recommend installing the desktop app on a local drive. Network shares aren't supported.

From Mattermost Desktop v6.1, Linux users can also install using `Flatpak packages <https://docs.mattermost.com/deployment-guide/desktop/linux-desktop-install.html#itab--Flatpak--0_1-Flatpak>`_ (currently in beta).

In Matermost, users are notified under **Downloads** when new desktop app releases become available. If managing the distribution of the Desktop app on behalf of users, you can recommend that your users disable desktop update notifications by going to **… > File > Settings** on Windows or **Mattermost > Settings** on Mac and clearing the **Automatically check for updates** option.

See additional deployment options below to manage distribution of the desktop app to your users.

Windows distribution channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From desktop v6.1, organizations deploying on Windows have 2 primary distribution options:

- **Windows Store** (recommended): Provides automatic updates through the Microsoft Store infrastructure. This is the recommended option for most organizations seeking streamlined update management.
- **MSI packages**: Traditional deployment method with full control over installation timing. See the :doc:`MSI installer and group policy guide </deployment-guide/desktop/desktop-msi-installer-and-group-policy-install>` for details.

The desktop v6.1 app includes in-app update notifications. All distribution channels (Windows Store, MSI, Mac App Store, Flathub, APT/RPM) release simultaneously to prevent notification and availability mismatches across deployment methods.

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
    /deployment-guide/desktop/desktop-troubleshooting.rst

* :doc:`Distribute a custom desktop app </deployment-guide/desktop/distribute-a-custom-desktop-app>`
* :doc:`Silent Windows desktop distribution </deployment-guide/desktop/silent-windows-desktop-distribution>`
* :doc:`MSI installer and group policy guide </deployment-guide/desktop/desktop-msi-installer-and-group-policy-install>`
* :doc:`Custom dictionaries for Windows and Linux </deployment-guide/desktop/desktop-custom-dictionaries>`
* :doc:`Managed resources for the desktop app </deployment-guide/desktop/desktop-app-managed-resources>`
* :doc:`Desktop app troubleshooting </deployment-guide/desktop/desktop-troubleshooting>`

Privacy and data handling
--------------------------

Error reporting
~~~~~~~~~~~~~~~~

From Mattermost Desktop v6.1, the desktop app includes automatic error reporting to help identify and fix crashes and stability issues.

**What information is sent**

Error reports include:

- Crash information and stack traces
- App version and platform details (OS type, architecture)
- Error messages and context

**What is NOT sent**

- Message content or user communications
- User credentials, passwords, or authentication tokens
- Personally identifiable information (PII)
- Server URLs or team names

**Privacy and user control**

Error reporting is **enabled by default**. Users can disable it at any time by going to **Settings > Advanced > Send error reports to help improve the app**. Restart the app to apply the change.

Organizations with data handling policies should inform users about this feature and provide guidance on whether to disable it. For organizations building the Desktop app from source, error reporting can be disabled at build time by omitting the ``MM_DESKTOP_BUILD_SENTRYDSN`` environment variable.