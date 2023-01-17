Add people to your workspace
============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Getting people set up with a Mattermost account is something that happens when deploying and configuring the Mattermost workspace. A Mattermost system admin can `provision Mattermost users </onboard/user-provisioning-workflows.html>`__ using one or more of the following methods:

- `Enable account creation </configure/authentication-configuration-settings.html#enable-account-creation>`__.
- Use `mmctl user create </manage/mmctl-command-line-tool.html#mmctl-user-create>`__ or Mattermost `APIs <https://api.mattermost.com/#tag/users>`__ to create user accounts.
- `Migrate user accounts </onboard/migrating-to-mattermost.html#migration-guide>`__ from other collaboration systems and `bulk load </onboard/bulk-loading-data.html>`__ that user data into Mattermost.
- Connect an authentication service to assist with user provisioning, such as `AD/LDAP authentication </onboard/ad-ldap.html#active-directory-ldap-setup>`__ or `SAML authentication </onboard/sso-saml.html>`__.

Add people on demand
--------------------

By default, `team admins </welcome/about-user-roles.html#team-admin>`__ can `invite people </welcome/about-teams.html#invite-people-to-teams>`__, including `guests </onboard/guest-accounts.html>`__, to a Mattermost team, and all users can add existing Mattermost users to a Mattermost team or channel, unless the system admin has restricted the ability for you to do so.

- Inviting people to a team sends an email prompting recipients to create a Mattermost account on your Mattermost workspace.
- Adding an existing user to a team or to a channel makes those users team or channel members.

.. tip::

    - Add users to a channel by selecting the channel name and selecting **Add Members**. 
    - Add groups of users to a channel by `creating a custom group </welcome/manage-custom-groups.html>`__ and `@mentioning </channels/mention-people.html>`__ the custom group in a channel. Mattermost will prompt to you to add any users who aren't already members of that channel.
    - Guests are restricted to only the channels you select.