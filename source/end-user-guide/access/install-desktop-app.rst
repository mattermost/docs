Install the Mattermost desktop app
==================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Download and install the Mattermost desktop app `for macOS from the App Store <https://apps.apple.com/us/app/mattermost-desktop/id1614666244?mt=12>`_, `for Windows from the Microsoft Store <https://apps.microsoft.com/detail/xp8br8mh3lpklt?hl=en-US&gl=US>`_, or by :doc:`using a package manager (Linux) </deployment-guide/desktop/linux-desktop-install>`. When new desktop app releases become available, your desktop app is automatically updated.

We strongly recommend installing the desktop app on a local drive. Network shares aren't supported. 

1. When prompted, enter the Mattermost server link and a display name for the Mattermost instance. The display name is helpful in cases where you connect to multiple Mattermost instances. See the :doc:`server connections </end-user-guide/preferences/connect-multiple-workspaces>` documentation for details.
2. Enter your user credentials to log into Mattermost. 
3. The team that displays first in the team sidebar opens. If you're not a member of a team yet, you're prompted to select a team to join.

.. note::

    When you log into Mattermost using external user credentials, such as Google or Entra ID, you'll temporarily leave the desktop app during login while authenticating your credentials. Once you're successfully logged in to Mattermost, you'll be returned to the desktop app. See the `Single Sign-On (SSO) <#single-sign-on-sso>`__ section below for details on the external providers that Mattermosts supports.

Upgrade the desktop app
------------------------

In Matermost, you’re notified under **Downloads** when new desktop app releases become available.

When automatic updates are disabled, you can manually check for updates by selecting **Help > Check for Updates** from the desktop app menu bar.