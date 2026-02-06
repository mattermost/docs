Desktop App Deployment
=======================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

The Mattermost desktop app is available for Windows, macOS, and Linux operating systems, and offers :doc:`additional functionality </end-user-guide/preferences/customize-desktop-app-experience>` beyond the web-based experience.

Learn more about desktop app :ref:`software requirements <deployment-guide/software-hardware-requirements:desktop apps>`, :doc:`releases and server compatibility </product-overview/mattermost-desktop-releases>` as well as the :doc:`what's changed across releases </product-overview/desktop-app-changelog>`.

Download
---------

Download and install the Mattermost desktop app from the `App Store (macOS) <https://www.apple.com/app-store/>`_, `Microsoft Store (Windows) <https://apps.microsoft.com/home?hl=en-US&gl=US>`_, or by :doc:`using a package manager (Linux) </deployment-guide/desktop/linux-desktop-install>`. We strongly recommend installing the desktop app on a local drive. Network shares aren't supported.

.. important::

   **Update Mechanism Change in v6.1.0**

   From Mattermost Desktop v6.1.0, automatic updates have been replaced with an in-app notification system. The desktop app checks Mattermost's website for new versions and displays notifications in the **Downloads** dropdown. Users must manually download and install updates.

   - Provides more reliable update notifications across all platforms (including Mac App Store and Microsoft Store)
   - Users control when to update (no automatic downloads or installations)
   - Administrators can disable update notifications via Group Policy for centrally managed deployments
   - For more information, see `this forum post <https://forum.mattermost.com/t/important-update-changes-to-desktop-app-auto-updater/25657>`__.

In Mattermost, users are notified under **Downloads** when new desktop app releases become available. If managing the distribution of the desktop app on behalf of users, you can recommend that your users disable desktop update notifications by going to **… > File > Settings** on Windows or **Mattermost > Settings** on Mac and clearing the **Automatically check for updates** option.

See additional deployment options below to manage distribution of the desktop app to your users.

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

* :doc:`Distribute a custom desktop app </deployment-guide/desktop/distribute-a-custom-desktop-app>`
* :doc:`Silent Windows desktop distribution </deployment-guide/desktop/silent-windows-desktop-distribution>`
* :doc:`MSI installer and group policy guide </deployment-guide/desktop/desktop-msi-installer-and-group-policy-install>`
* :doc:`Custom dictionaries for Windows and Linux </deployment-guide/desktop/desktop-custom-dictionaries>`
* :doc:`Managed resources for the desktop app </deployment-guide/desktop/desktop-app-managed-resources>`