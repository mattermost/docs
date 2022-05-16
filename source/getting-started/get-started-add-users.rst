Onboard users
=============

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.


Invite people to teams: https://docs.mattermost.com/welcome/about-teams.html#invite-people-to-teams
Enable automatic account creation: https://docs.mattermost.com/configure/configuration-settings.html#enable-account-creation

Using AD/LDAP user groups for team or channel membership: https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html
GitLab SSO: https://docs.mattermost.com/onboard/sso-gitlab.html
Google SSO: https://docs.mattermost.com/onboard/sso-google.html
Office 365 SSO: https://docs.mattermost.com/onboard/sso-office.html
OpenID Connect SSO: https://docs.mattermost.com/onboard/sso-openidconnect.html


Migrate from email-based authentication to AD/LDAP or SAML
----------------------------------------------------------

When you purchase a subscription, you can migrate your users from email authentication to Active Directory/LDAP or to SAML Single Sign-on. 

- To set up Active Directory/LDAP, see `Active Directory/LDAP Setup <https://docs.mattermost.com/onboard/ad-ldap.html#active-directory-ldap-setup>`_. 
- To set up SAML Single Sign-on, see `SAML Single-Sign-On <https://docs.mattermost.com/onboard/sso-saml.html>`_.

After the new authentication method is enabled, existing users cannot use the new method until they go to **Settings > Security > Sign-in method** and select **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After they have switched, they can no longer use their email and password to sign in.  
  

Integrate with your directory services
You already have your users grouped by role, location, or level, so Mattermost makes it easy to integrate with your existing identity and access management (IAM) services and systems with Active Directory and LDAP and SAML 2.0 SSO integrations featuring providers like Active Directory Federation Services, Okta, GitLab, Google, and Office 365.

Bulk Onboarding
For bulk onboarding, enable AD/LDAP Group Synchronization to ensure new users are added to default teams and channels as they join Mattermost. See our AD/LDAP Groups documentation to learn more.

User roles: https://docs.mattermost.com/welcome/about-user-roles.html
User permissions: http://mattermost-docs-preview-pulls.s3-website-us-east-1.amazonaws.com/5469/getting-started/admin-onboarding-tasks.html#configure-user-permissions
Manage users, groups, teams, channels: https://docs.mattermost.com/configure/user-management-configuration-settings.html

+ welcome email to users here (perhaps an include?)