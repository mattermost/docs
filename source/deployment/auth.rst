..  _auth_mfa:
Multi-Factor Authentication (E10)
=================================

For increased security, Mattermost Enterprise Edition offers the option to require a phone-based passcode, in addition to email-password or Active Directory/LDAP authentication, to sign in to the Mattermost server. 

Supported phones include iOS, Android, Blackberry and Windows Phone devices that are able to install `Google Authenticator <https://support.google.com/accounts/answer/1066447?hl=en>`_. Other than requiring internet access to download and install Google Authenticator, the phone used for Mattermost MFA does not require internet access.

Enabling MFA
------------

This option can be enabled by the System Administrator in the `System Console <http://docs.mattermost.com/administration/config-settings.html#mfa>`_ under **Authentication** > **MFA** > **Enable Multi-factor Authentication**

End users can set up this feature in the `Account Settings <http://docs.mattermost.com/help/settings/account-settings.html#multi-factor-authentication-enterprise>`_ menu under **Security** > **Multi-factor Authentication**.

Enforcing MFA
-------------

This option can be enabled by the System Administrator in the `System Console <http://docs.mattermost.com/administration/config-settings.html#mfa>`_ under **Authentication** > **MFA** > **Enforce Multi-factor Authentication**

When MFA enforcement is set to true, all users with email or LDAP authentication without MFA set up will be sent to the MFA setup page. They will not be able to access the site until MFA setup is complete. Any new users will be required to set up MFA during the sign up process. 

Users will not be able to remove MFA from their account while enforcement is on.

Since turning on MFA enforcement prevents users from accessing the site until set up is complete, it is recommended you turn on enforcement during non-peak hours when people are less likely to be using the system.




