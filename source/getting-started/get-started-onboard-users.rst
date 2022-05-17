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

On this page, you'll learn how to add users to your Mattermost workspace, make it easy for your users to access Mattermost every day, and how to control product access through roles and permissions. 

Invite people
-------------

You can add people to a Mattermost team by sending `a direct invitation <https://docs.mattermost.com/welcome/about-teams.html#send-a-direct-invite>`__ or a `public team invite link <https://docs.mattermost.com/welcome/about-teams.html#send-a-team-invite-link>`__. You can also `manually add people to a team <https://docs.mattermost.com/welcome/about-teams.html#adding-someone-to-your-team>`__ when those users already have a Mattermost account on the server.

.. tip::
  Mattermost creates user accounts automatically when you invite users or share a team invitation link. See the `authentication configuration settings <https://docs.mattermost.com/configure/configuration-settings.html#authentication>`__ documentation for additional account creation options.

Onboard users in bulk
----------------------

Make onboarding, account provisioning, and user authentication easier through automation with directory services integrations. You likely already have your users grouped by role, location, or level. Mattermost makes it easy to integrate with your existing identity and access management (IAM) services, systems with `Active Directory and LDAP <https://docs.mattermost.com/onboard/ad-ldap.html>`__, as well as `SAML 2.0 Single Sign-On <https://docs.mattermost.com/onboard/sso-saml.html>`__ and `OpenID Connect Single Sign-On <https://docs.mattermost.com/onboard/sso-openidconnect.html>`__ integrations with providers such as Active Directory Federation Services, `Okta <https://docs.mattermost.com/onboard/sso-saml-okta.html>`__, `OneLogin <https://docs.mattermost.com/onboard/sso-saml-onelogin.html>`__,  `GitLab <https://docs.mattermost.com/onboard/sso-gitlab.html>`__, `Google <https://docs.mattermost.com/onboard/sso-google.html>`__, and `Office 365 <https://docs.mattermost.com/onboard/sso-office.html>`__.

Mattermost Enterprise customers can enable `AD/LDAP group synchronization <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ to ensure new users are added to default teams and channels as they join Mattermost. Use our `sample email template <https://docs.mattermost.com/getting-started/welcome-email-to-end-users.html>`__ to make it easy for your end users to start using Mattermost right away.

.. tip::
  
  - See the `migration guide <https://docs.mattermost.com/onboard/migrating-to-mattermost.html>`__ and `bulk loading <https://docs.mattermost.com/onboard/bulk-loading-data.html>`__ documentation for additional bulk onboarding options.
  - When you purchase a subscription, you can migrate your users from email authentication to Active Directory/LDAP or to SAML Single Sign-on. After the new authentication method is enabled, existing users can't use the new method until they go to **Settings > Security > Sign-in method** and select **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After users have switched their authenticatio method, they can't use their email and password to sign in.  

Control product access
----------------------

Once your Mattermost workspace is :doc:`configured for your production needs </getting-started/get-started-configure>`, ensure the right people can see and do the right things throughout Mattermost. 

Start by learning more about `teams <https://docs.mattermost.com/welcome/about-teams.html>`__ `working with channels <https://docs.mattermost.com/guides/channels.html#work-with-channels>`__, and `managing users, groups, teams, and channels <https://docs.mattermost.com/configure/user-management-configuration-settings.html>`__ in the System Console. 

Then learn how to control product access with `user roles <https://docs.mattermost.com/welcome/about-user-roles.html>`__ and `advanced permissions <https://docs.mattermost.com/onboard/advanced-permissions.html>`__. With permissions, you have controls in place over who can do what and where based on the roles and areas of ownership in your organization. 

.. image:: ../images/advanced-permissions.png
    :alt: Control product access with granular Mattermost permissions.

.. tip::

  Mattermost won’t limit you to the number of teams you can create; however, a public team and an internal team are typically sufficient. See our `creating teams <https://docs.mattermost.com/welcome/about-teams.html#create-a-team>`__ and our `team settings <https://docs.mattermost.com/welcome/team-settings.html>`__ documentation for more information on working with teams.