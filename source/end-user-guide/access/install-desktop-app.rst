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

In Matermost, you're notified under **Downloads** when new desktop app releases become available.

When automatic updates are disabled, you can manually check for updates by selecting **Help > Check for Updates** from the desktop app menu bar.

Upgrade to v6.1.0 (Windows MSI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost Desktop v6.1.0, the Windows MSI installer installs per-machine (system-wide) by default instead of per-user. This change meets enterprise compliance requirements and affects how you upgrade depending on your current version.

**What changed:**

- **Installation location**: Now installs to ``C:\Program Files\Mattermost`` instead of your user folder
- **Admin privileges**: You may need administrator privileges to install
- **Shortcuts**: Created in a shared folder so all users on the machine can access them
- **Registry**: Writes to system-wide registry keys (HKLM) instead of per-user keys (HKCU)

**Upgrade scenarios:**

If upgrading from versions **below v5.9**:

1. The upgrade will succeed automatically.
2. You may see an extra shortcut in your Start Menu after the upgrade.
3. You can safely delete the extra shortcut.

If upgrading from versions **v5.9 through v6.0.4**:

1. First, check your current installation type:

   - Open File Explorer
   - If Mattermost is in ``C:\Program Files\Mattermost`` or ``C:\Program Files (x86)\Mattermost``: You have a per-machine install (upgrade will work normally)
   - If Mattermost is in ``C:\Users\<YourName>\AppData\Local\...``: You have a per-user install (see step 2)

2. If you have a per-user installation (most common for v5.9-v6.0.4):

   - **The new installer cannot automatically upgrade across installation types**
   - You must manually uninstall the old version first:

     a. Save any open work in Mattermost
     b. Go to **Settings > Apps** (or **Control Panel > Programs**)
     c. Uninstall Mattermost Desktop
     d. Download and install v6.1.0 - it will install to ``C:\Program Files\Mattermost``

   - This is a one-time migration; future upgrades will work normally

**Troubleshooting v6.1.0 upgrade (Windows MSI):**

**Symptom**: Installed v6.1.0 but old version still appears, or both versions are present

**Cause**: You had a per-user installation from v5.9-v6.0.4; MSI cannot upgrade across installation contexts (per-user to per-machine)

**Solution**:

1. Uninstall both versions via **Settings > Apps**
2. Download v6.1.0 MSI again
3. Install with administrator privileges (will install to ``C:\Program Files\Mattermost``)