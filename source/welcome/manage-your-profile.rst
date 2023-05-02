Manage your Mattermost profile
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You can configure your `profile <#profile>`__ and `security <#security>`__ preferences by selecting **Profile** from your profile picture. 

.. tip::
  
  How you access your profile settings depends on the version of Mattermost you're using. See the `what's changed in Mattermost v6.0 </welcome/what-changed-in-v60.html#account-settings>`__ documentation for details. 

Profile
-------

See the following table to learn how to configure your name, username, nickname, email, and profile picture.

+---------------------+-------------------------------------------------------------------------------------------------+
| **Profile setting** | **Description**                                                                                 |
+=====================+=================================================================================================+
| Full, first, and    | Your name appears in the direct messages member list and team management modal.                 |
| last name           | By default, you'll receive mention notifications when someone types your first name             |
|                     | in a message.                                                                                   |
|                     |                                                                                                 |
|                     | **Note**: If your name is configured through a login provider, you'll need to manage name       |
|                     | changes through the login provider.                                                             |
+---------------------+-------------------------------------------------------------------------------------------------+
| Username            | Usernames are unique identifiers appearing next to all posts.                                   |
|                     | Usernames must begin with a letter, and contain between 3 to 22                                 |
|                     | lowercase characters made up of numbers, letters, and the                                       |
|                     | symbols '.', '-', and '_'.                                                                      |
|                     |                                                                                                 |
|                     | Pick something easy for teammates to recognize and recall.                                      |
|                     | By default, you will receive mention notifications when someone                                 |
|                     | types your username.                                                                            |
|                     |                                                                                                 |
|                     | **Notes**:                                                                                      |
|                     |                                                                                                 |
|                     | - To maintain message integrity, changing your username doesn't update @mentions                |
|                     |   in posted messages.                                                                           |
|                     | - If your username is configured through a login provider, you'll need to manage                |
|                     |   username changes through the login provider.                                                  |
+---------------------+-------------------------------------------------------------------------------------------------+
| Nickname            | (Optional) Nicknames appear in the direct messages member list and team management modal.       |
|                     | You won't receive mention notifications when someone types your nickname unless you add         |
|                     | it to the **Words That Trigger Mentions** notifications list as a `Notifications                |
|                     | </channels/channels-settings.html#notifications>`__ preference.                                 |
+---------------------+-------------------------------------------------------------------------------------------------+
| Position            | (Optional) Position can be used to describe your role or job title.                             |
|                     | Your position appears in the profile popup that displays when you select                        |
|                     | a user's name in the center channel or right-hand sidebar.                                      |
|                     |                                                                                                 |
|                     | **Note**: If your position is configured through a login provider, you'll need to manage        |
|                     | position changes through the login provider.                                                    |
+---------------------+-------------------------------------------------------------------------------------------------+
| Email               | Email is used for signing in, notifications, and password reset.                                |
|                     |                                                                                                 |
|                     | **Note**: If your email is configured through an SSO service, you can't edit your               |
|                     | email address, and you'll receive email notifications to the email you used to                  |
|                     | sign up to your SSO service.                                                                    |
+---------------------+-------------------------------------------------------------------------------------------------+
| Profile picture     | Profile pictures appear next to all posts, and you can select your                              |
|                     | profile picture to access your profile settings. To change your profile picture:                |
|                     |                                                                                                 |
|                     | **Using the web or the desktop app**                                                            |
|                     |                                                                                                 |
|                     | 1. Select **Edit** next to the **Profile Picture** option.                                      |
|                     | 2. Choose **Select**, pick the profile image you want to use, and select **Save**.              |
|                     |                                                                                                 |
|                     | **Using the mobile app**                                                                        |
|                     |                                                                                                 |
|                     | 1. Tap your current profile picture.                                                            |
|                     | 2. Take a photo using your device, or select an image to use.                                   |
|                     |                                                                                                 |
|                     | **Tip**: For best results, choose an image that's at least 128 x 128 pixels in size.            |
|                     | Supported image formats include: BMP, JPG, JPEG, and PNG. The GIF file format is not supported. |
+---------------------+-------------------------------------------------------------------------------------------------+

Security
--------

See the following table to learn how to configure your password, view access history, and view or logout of active sessions.

+----------------------+--------------------------------------------------------------------------------------------------------+
| **Security setting** | **Description**                                                                                        |
+======================+========================================================================================================+
| Password             | You may change your password if you've logged in by email using Mattermost in                          |
|                      | a web browser or using the desktop app.                                                                |
|                      |                                                                                                        |
|                      | **Note**: If you sign in to Mattermost using a single sign-on                                          |
|                      | service, you must update your password through your SSO                                                |
|                      | service account.                                                                                       |
+----------------------+--------------------------------------------------------------------------------------------------------+
| Multi-factor         | If your system admin has enabled `multi-factor authentication                                          |
| authentication (MFA) | </configure/configuration-settings.html#enable-multi-factor-authentication>`__                         |
|                      | (MFA), you can require a passcode in addition to your password to log-in to your Mattermost account.   |
|                      |                                                                                                        |
|                      | You'll need to download a MFA passcode generation app, such as Google Authenticator or a similar app,  |
|                      | and then set-up MFA in your Mattermost account.                                                        |
|                      |                                                                                                        |
|                      | **Set-up MFA in Mattermost**                                                                           |
|                      |                                                                                                        |
|                      | 1. Open Mattermost in a web browser or the desktop app.                                                |
|                      | 2. In Mattermost, from your profile picture, select **Profile > Security**.                            |
|                      | 3. Under **Multi-factor Authentication**, select **Edit**.                                             |
|                      |                                                                                                        |
|                      | .. image:: ../images/multi-factor-authentication.png                                                   |
|                      |   :alt: Enable multi-factor authentication through your Mattermost user profile.                       |
|                      |                                                                                                        |
|                      | 4. Select **Add MFA to Account**.                                                                      |
|                      |                                                                                                        |
|                      | .. image:: ../images/add-mfa-to-account.png                                                            |
|                      |   :alt: Add multi-factor authentication to your Mattermost user profile.                               |
|                      |                                                                                                        |
|                      | 5. Scan the QR code or enter the **Secret** provided by Mattermost into the authenticator app.         |
|                      | 6. In Mattermost, enter the **MFA Code** generated by the authenticator app.                           |
|                      | 7. Select **Save**.                                                                                    |
+----------------------+--------------------------------------------------------------------------------------------------------+
| Sign-in method       | This option allows you to switch your `login method </welcome/log-in.html>`__ from                     |
|                      | `email/username and password </welcome/log-in.html#email-address-or-username>`__                       |
|                      | to a `single sign-on option </welcome/log-in.html#single-sign-on-sso>`__, and back again.              |
|                      |                                                                                                        |
|                      | You can configure this setting using Mattermost in a browser or using the desktop app.                 |
|                      |                                                                                                        |
|                      | **Note**: While you can choose to log in with either set of credentials, you can only enable           |
|                      | one login method at a time. For example, if AD/LDAP single sign-on is enabled, you can select          |
|                      | **Switch to using AD/LDAP**, and enter your AD/LDAP credentials to switch login over to AD/LDAP.       |
|                      | You'll need to enter the password for your email account to verify your existing credentials.          |
|                      | Following the change, you'll receive an email to confirm the action.                                   |
+----------------------+--------------------------------------------------------------------------------------------------------+
| View access history  | Using Mattermost in a browser or using the desktop app, you can access a chronological list            |
|                      | of the last 20 login and logout attempts, channel creations and deletions, account settings changes,   |
|                      | or channel setting modifications made with your account.                                               |
|                      |                                                                                                        |
|                      | The details of the Session ID, which is a unique identifier for each Mattermost browser session,       |
|                      | and IP Address of the action is recorded for audit log purposes.                                       |
+----------------------+--------------------------------------------------------------------------------------------------------+
| View and log out     | Sessions are created when you log in with your credentials a new browser on a device.                  |
| of active sessions   | Sessions let you use Mattermost for up to 30 days without having to log in again.                      |
|                      |                                                                                                        |
|                      | Using Mattermost in a browser or using the desktop app:                                                |
|                      |                                                                                                        |
|                      | - Select **Logout** during an active session if you want to revoke automatic login privileges          |
|                      |   for a specific browser or device.                                                                    |
|                      | - Select **More Info** to view browser and system details.                                             |
+----------------------+--------------------------------------------------------------------------------------------------------+
