..  _auth_mfa:

Multi-factor Authentication
===========================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Multi-factor authentication (MFA) is a secondary layer of user authentication applied to your Mattermost server.

With MFA enabled, users need to provide a secure one-time code in addition to their username and password in order to log in to Mattermost. MFA is useful in organizations that have specific security and compliance policies. It can also be used in organizations where Mattermost is not behind a firewall and doesn't have access to existing MFA infrastructure.

Mattermost offers a smartphone-based MFA check in addition to email-password or Active Directory/LDAP authentication to sign in to the Mattermost server.

Supported smartphones include iOS, Android, Blackberry, and Windows Phone devices that are able to install `Google Authenticator <https://support.google.com/accounts/answer/1066447?hl=en>`__. Other than requiring internet access to download and install Google Authenticator, the phone used for Mattermost MFA does not require internet access.

.. note::
  
  As the MFA implementation relies on Time-based One-time passwords (TOTP) ensure that your server system time is accurate. If there is a discrepancy, users may not be able to log in successfully.

Enabling MFA
------------

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

System Admins can enable this option by going to **System Console > Authentication > MFA**, then setting **Enable Multi-factor Authentication** to **true**.

Once enabled, users can opt to `set up multi-factor authentication <https://docs.mattermost.com/messaging/manage-profile-settings.html#multi-factor-authentication>`__ on their account by selecting **Profile > Security > Multi-factor Authentication** from their avatar.

.. include:: common-disable-mfa.rst

Enforcing MFA
--------------

|enterprise| |professional| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Mattermost Enterprise Edition E10*

This option can be enabled by the System Admin by going to **System Console > Authentication > MFA**, then setting **Enforce Multi-factor Authentication** to **true**.

When MFA enforcement is set to **true**, users with email or LDAP authentication who don't have MFA set up will be directed to the MFA setup page when they log in to Mattermost. They will not be able to access the site until MFA setup is complete. Any new users will be required to set up MFA during the sign up process.

Users will not be able to remove MFA from their account while enforcement is on.

.. note::

  Turning on MFA enforcement prevents users from accessing the site until set up is complete. We recommended that you turn on enforcement during non-peak hours when people are less likely to be using Mattermost.
