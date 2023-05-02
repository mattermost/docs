..  _auth_mfa:

Multi-factor authentication
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Multi-factor authentication (MFA) is a secondary layer of user authentication applied to your Mattermost server.

With MFA enabled, users need to provide a secure one-time code in addition to their username and password in order to log in to Mattermost. MFA is useful in organizations that have specific security and compliance policies. It can also be used in organizations where Mattermost is not behind a firewall and doesn't have access to existing MFA infrastructure.

Mattermost offers a smartphone-based MFA check in addition to email-password or Active Directory/LDAP authentication to log in to the Mattermost server.

Supported smartphones include iOS, Android, or other devices that are able to install Google Authenticator or a similar app. After the app is installed, the device does not require internet access.

.. note::
  
  As the MFA implementation relies on Time-based One-time passwords (TOTP) ensure that your server system time is accurate. If there is a discrepancy, users may not be able to log in successfully.

Enabling MFA
------------

System Admins can enable this option by going to **System Console > Authentication > MFA**, then setting **Enable Multi-factor Authentication** to **true**.

Once enabled, users can opt to `set up multi-factor authentication </messaging/manage-profile-settings.html#multi-factor-authentication>`__ on their account by selecting **Profile > Security > Multi-factor Authentication** from their profile picture.

.. include:: common-disable-mfa.rst
  :start-after: :nosearch:

Enforcing MFA
--------------

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E10/E20*

This option can be enabled by the System Admin by going to **System Console > Authentication > MFA**, then setting **Enforce Multi-factor Authentication** to **true**.

When MFA enforcement is set to **true**, users with email or LDAP authentication who don't have MFA set up will be directed to the MFA setup page when they log in to Mattermost. They will not be able to access the site until MFA setup is complete. Any new users will be required to set up MFA during the sign up process.

Users will not be able to remove MFA from their account while enforcement is on.

.. note::

  Turning on MFA enforcement prevents users from accessing the site until set up is complete. We recommended that you turn on enforcement during non-peak hours when people are less likely to be using Mattermost.
