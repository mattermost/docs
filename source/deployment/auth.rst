..  _auth_mfa:
Multi-Factor Authentication (E10)
=================================

For organizations who require multi-factor authentication ("MFA") as part of their IT security policy, and who choose not to secure Mattermost behind a firewall with their existing MFA infrastructure, Mattermost Enterprise Edition offers a smartphone-based MFA check, in addition to email-password or Active Directory/LDAP authentication, to sign in to the Mattermost server. 

Supported smartphones include iOS, Android, Blackberry and Windows Phone devices that are able to install `Google Authenticator <https://support.google.com/accounts/answer/1066447?hl=en>`_. Other than requiring internet access to download and install Google Authenticator, the phone used for Mattermost MFA does not require internet access.

- **Note:** The open source Mattermost Team Edition is designed to offer "modern communication behind your firewall" and is used extensively by security professionals, `including former members of the United States FBI, CIA, and NSA in addition to the former CIO of the U.S. Whitehouse. <https://about.mattermost.com/open-source-mattermost-software-helps-ex-cia-nsa-fbi-hunt-us-fugitives/>`_ The MFA feature in Mattermost Enterprise Edition is considered an optional convenience feature in lieu of operating on a secured private network. 

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




