..  _auth_mfa:
Multi-factor Authentication
===========================

For organizations that require multi-factor authentication (MFA) as part of their IT security policy, and choose not to secure Mattermost behind a firewall with their existing MFA infrastructure, Mattermost offers a smartphone-based MFA check, in addition to email-password or Active Directory/LDAP authentication, to sign in to the Mattermost server.

Supported smartphones include iOS, Android, Blackberry, and Windows Phone devices that are able to install `Google Authenticator <https://support.google.com/accounts/answer/1066447?hl=en>`__. Other than requiring internet access to download and install Google Authenticator, the phone used for Mattermost MFA does not require internet access.

Prerequisite
-------------
Ensure that your server system time is accurate as the MFA implementation relies on Time-based One-time passwords (TOTP).

Enabling MFA
------------

This option can be enabled by the System Admin in the `System Console <http://docs.mattermost.com/administration/config-settings.html#mfa>`__ under **Authentication > MFA > Enable Multi-factor Authentication**. End users can set up this feature in the `Account Settings <http://docs.mattermost.com/help/settings/account-settings.html#multi-factor-authentication-enterprise>`__ menu under **Security > Multi-factor Authentication**.

Enforcing MFA (E10)
-------------------

This option can be enabled by the System Admin in the `System Console <http://docs.mattermost.com/administration/config-settings.html#mfa>`__ under **Authentication > MFA > Enforce Multi-factor Authentication**.

When MFA enforcement is set to **true**, all users with email or LDAP authentication without MFA set up will be sent to the MFA setup page. They will not be able to access the site until MFA setup is complete. Any new users will be required to set up MFA during the sign up process.

Users will not be able to remove MFA from their account while enforcement is on.

.. note::
  Turning on MFA enforcement prevents users from accessing the site until set up is complete. It is recommended that you turn on enforcement during non-peak hours when people are less likely to be using Mattermost.
