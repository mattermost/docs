Desktop App Deployment
=======================

.. include:: ../../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The Mattermost desktop app is available for Windows, macOS, and Linux operating systems, and offers :doc:`additional functionality </preferences/customize-desktop-app-experience>` beyond the web-based experience.

Learn more about desktop app :ref:`software requirements <deploy/software-hardware-requirements:desktop apps>`, :doc:`releases and server compatibility </about/mattermost-desktop-releases>` as well as the :doc:`what's changed across releases </about/desktop-app-changelog>`.

Download
---------

Download and install the Mattermost desktop app from the App Store (macOS), Microsoft Store (Windows), or by :doc:`using a package manager (Linux) </deploy/desktop/linux-desktop-install>`. Under **Downloads**, you're notified when new desktop app releases become available, where you can view the changelog and download updates.

We strongly recommend installing the desktop app on a local drive. Network shares aren't supported.

If you prefer to manage distribution of the mobile app to your users, see the deployment options below.

Deployment options
------------------

Learn about installation, configuration, and management options for deploying the desktop app in your environment.

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    /deploy/desktop/linux-desktop-install.rst
    /deploy/desktop/distribute-a-custom-desktop-app.rst
    /deploy/desktop/silent-windows-desktop-distribution.rst
    /deploy/desktop/desktop-msi-installer-and-group-policy-install.rst
    /deploy/desktop/desktop-custom-dictionaries.rst
    /deploy/desktop/desktop-app-managed-resources.rst

* :doc:`Distribute a custom desktop app </deploy/desktop/distribute-a-custom-desktop-app>`
* :doc:`Silent Windows desktop distribution </deploy/desktop/silent-windows-desktop-distribution>`
* :doc:`MSI installer and group policy guide </deploy/desktop/desktop-msi-installer-and-group-policy-install>`
* :doc:`Custom dictionaries for Windows and Linux </deploy/desktop/desktop-custom-dictionaries>`
* :doc:`Managed resources for the desktop app </deploy/desktop/desktop-app-managed-resources>`