.. _guest-accounts:

Guest Accounts (Beta) (E10/E20)
===================================

Available in `Enterprise Edition E10 and higher <https://about.mattermost.com/pricing/>`__.

Guest Accounts are a new role within Mattermost Enterprise editions which allow organizations to collaborate with individuals (such as vendors and contractors) outside of their organization.
The Guest Account feature controls access to channels and other members within the organization.

For example, an organization may use Guest Accounts to work on a website project with resources from an external design firm. Guest Accounts could also be used to collaborate with customers on a support issue.

Guests can:

- Pin messages to channels
- Use slash commands (excluding restricted commands such as invite members, rename channels, change headers, etc)
- Favorite channels
- Mute channels
- Update their account settings

Guests cannot:

- Discover public channels
- Join open teams
- Create direct messages or group messages with members who aren’t within the same channel
- Invite people

Additionally, guests are not automatically added to the default ``Town-square`` and ``Off-topic`` channels upon logging in.  To access these channels, they will need to be invited or added to them. 


Enabling Guest Accounts
------------------------

1. Navigate to **System Console > Authentication > Guest Access**.
2. Set **Enable Guest Access** to ``True``.
3. (Optional) **Whitelist domains that are acceptable for Guest Access**.
 - This allows the System Administrators to set a list of approved guest domains. If you have team domain restrictions, you will also need to add your guest domain to **Team Settings > Allow only users with a specific email domain to join this team**.
4. (Optional) **Enforce Multi-Factor Authentication (MFA) for your Guests**.
 - If you are enforcing MFA for your users, you can optionally choose to enforce MFA for your guest users.

Guest Authentication
---------------------

Guests can access the Mattermost server via email invitation, and be authenticated using AD/LDAP or SAML 2.0.
Before you proceed, ensure that the authentication method you wish to use is correctly configured on your server and enabled in Mattermost.
For configuration steps and technical documentation, see `Active Directory/LDAP Setup <https://docs.mattermost.com/deployment/sso-ldap.html>`_
and `SAML Single-Sign-On <https://docs.mattermost.com/deployment/sso-saml.html>`_.

Converting a member user to a guest will not change the channels they are in; however they will be restricted from discovering additional channels and unable to direct message / group message users outside of the channels they are in. They can be added to channels by System Admins and other roles that have the correct permissions to invite guests.


Inviting Guests to the Mattermost Server via Email
------------------------------------------------------

Guests can be invited into one for more Mattermost channels within a team by System Admins and roles that have the correct permission to invite guests. A guest can also be invited into channels on multiple teams.

**Note:** Guest invitations will be revoked after 48 hours per the member email invitation process. If your guest has not accepted the invitation within that period, please follow the steps below to resend an invitation to the guest.

To invite guests into one or more Mattermost channels:

1. Enable email invites from **System Console > Signup > Enable Email Invitations**.
2. Navigate to **Main Menu > Invite People**.  This is a new invitation option that combines inviting guests and members and consolidates **Send Email**, **Get Team Invite Link**, and **Add Members to the Team**.
3. Select **Invite Guests**.
4. Enter the guest’s email address.
5. Choose the channels the guest can join (excluding managed teams).
6. (Optional) Enter a custom message.

.. image:: ../images/Guest_Invite_Screen.png

Configuring AD/LDAP Authentication
----------------------------------

When enabled, the **Guest Filter** in Mattermost identifies external users whose AD/LDAP role is guest and who are invited to join
your Mattermost server. These users will have the Guest role applied immediately upon first sign-in instead of the default member user role.
This eliminates having to manually assign the role in the System Console.

1. Enable Guest Access via **System Console > Guest Access (Beta)**.
2. Navigate to **System Console > Authentication > AD/LDAP**.
3. Complete the **Guest Filter** field.
4. Choose **Save**.

If a Mattermost Guest user has the guest role removed in the AD/LDAP system, the synchronization process
will not automatically promote them to a member user role. This is done manually via **System Console > User Management**. If a
member user has the **Guest Attribute** added, the synchronization processes will automatically demote the member user to the guest role.

When a guest logs in without having any channels assigned to their account, they are presented with an alert advising them to contact an administrator. 

Configuring SAML 2.0 Authentication
------------------------------------

When enabled, the **Guest Attribute** in Mattermost identifies external users whose SAML assertion is guest and who are invited to join
your Mattermost server. These users will have the Guest role applied immediately upon first sign-in instead of the default member user role.
This eliminates having to manually assign the role in the System Console.

If a Mattermost Guest user has the guest role removed in the SAML system, the synchronization processes will not automatically
promote them to a member user role. This is done manually via **System Console > User Management**.
If a member user has the **Guest Attribute** added, the synchronization processes will automatically demote the member user to the guest role.

1. Enable Guest Access via **System Console > Guest Access (Beta)**.
2. Navigate to **System Console > Authentication > SAML 2.0**.
3. Complete the **Guest Attribute** field.
4. Choose **Save**.

When a guest logs in without having any channels assigned to their account, they are presented with an alert advising them to contact an administrator. 


Guest Permission Settings
---------------------------------------

In E10 and E20, you can also control which users can invite guests. By default, only the System Administrator can invite guests. There are `additional permissions <https://docs.mattermost.com/deployment/advanced-permissions.html>`_ in E20 that can be adjusted under **System Console > Advanced Permissions > System Scheme** to control a guest’s ability to:

 - Edit posts
 - Delete posts
 - Post reactions
 - Create private channels with members they are allowed to collaborate with

Guest Identification
---------------------------

Guests are identified with a guest badge. This badge is visible in various places on the interface and mobile apps such as on a guest’s profile and next to their name on user lists, including at-mentions and quick switcher lists. When guests are added to a channel, a system message informs other channel members that the added user is a guest.

Channels that contain guests will have their header automatically updated with a message stating: *This channel has guests*.

.. image:: ../images/Guest_Badges.png

Managing Guests
-------------------------

Adding Guests to Additional Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users with the permissions to invite guests can use the **Invite Guests** modal to add a guest to additional channels.

A system message will be posted in the channels to let other members know a guest user has been added.

Removing Guests from Channels and Teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Guests can be removed from a channel through the normal **Manage members** modals, or by using the ``/kick`` or ``/remove`` commands. 

When a guest has been removed from all channels within a team and they belong to other teams, they will default into the last channel on the last team they have accessed. If they are removed from all channels on all teams, they will be taken to a screen letting them know they have no channels assigned.

Promoting and Demoting User Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

System Administrators can demote a *Member* to *Guest* by updating their role in **System Console > User Management > Users**. The demoted user will retain their existing channel and team memberships but will be restricted from discovering public channels and collaborating with users outside of the channels they are in.  This is useful if you are already collaborating with external contractors and want to restrict their abilities within your Mattermost instance.

System Administrators can also promote a *Guest* to *Member* by updating their role in **System Console > User Management > Users**.

**Note:** You can filter the list in **System Console >  User Management > Users** to view all guests on the system.

Disabling Guest Accounts
------------------------

To disable the Guest Accounts feature, go to **System Console > Authentication > Guest Access > Enable Guest Access** and select ``False``. In versions
prior to 5.18, current Guest Accounts will remain active until guest users are manually marked ``inactive`` in **System Console > User Management > Users**.

From 5.18, if you are using AD/LDAP and the Guest Access setting is disabled, the Guest Filter and existing guest users in System Console are deactivated.
Additionally, no new guests can be invited or added using the filter as an authentication method. If a previous guest's
credentials match the user filter (the only filter which is active when Guest Access is disabled), they will be reactivated and promoted to a member user
upon their next login.

To disable the Guest Accounts feature, go to **System Console > Authentication > Guest Access > Enable Guest Access** and select ``False``. In versions prior to 5.18, current Guest Accounts will remain active until guest users are manually marked ``inactive`` in **System Console > User Management > Users**. 

Similarly, for SAML, when the Guest Access setting is disabled, the Guest Attribute and existing guest users in System Console are deactivated.
Additionally, no new guests can be invited or added using the attribute as an authentication method. If a previous guest's
credentials match the user attribute (the only attribute which is active when Guest Access is disabled), they will be reactivated and promoted
to a member user upon their next login.

You can disable individual guest accounts in **System Console > User Management** via the **Manage Members** modal. In version 5.18,
when a single Guest Account is disabled or the feature is disabled, the guests will be marked as ``inactive``, be logged out of Mattermost, and all their sessions will be revoked.

Reinstating Guest Accounts
--------------------------

When Guest Access is re-enabled for AD/LDAP, the Guest Filter is reinstated. New users matching the Guest Filter will be authenticated as new guest users on login.
Previous guest users will be activated with the next synchronization. If their credentials still match the Guest filter, they will retain their guest status. If they no longer match the Guest Filter but do match the User Filter, they will be not be promoted to member user automatically on login - this must be done manually. If a previous guest was reactivated as a member user when Guest Access was disabled, and now are identified by the Guest Filter once again, they will automatically be demoted to Guest upon their login.

Similarly, for SAML, when Guest Access is re-enabled, the SAML Guest Attribute is reinstated. New users matching the Guest Attribute will be authenticated as new guest users on login.
Previous guest users will be activated with the next synchronization.  If their credentials still match the Guest Attribute, they will retain their guest status. If they no longer match the Guest Attribute but do match the User Filter, they will be not be promoted to member user automatically on login - this must be done manually. If a previous guest was reactivated as a member user when Guest Access was disabled, and now are identified by the Guest Attribute once again, they will automatically be demoted to Guest upon their login.

Frequently Asked Questions
---------------------------

How am I charged for Guest Accounts?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Guests are charged as a user seat.

Why doesn’t Mattermost have single-channel guests?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We wanted to support collaboration with external guests for the broadest use cases without limiting guests' access to channels. In the future, we may consider adding single-channel guests.

Can I set an expiration date for guests?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, you cannot. This feature may be added at a later stage.

Can MFA be applied selectively?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If MFA is enforced for your users, it can be applied to Guest Accounts. Guests can configure MFA in **Account Settings > Security**. If MFA is not enforced for your users, it can't be applied to Guest Accounts.

Why is the Guest Account feature in Beta?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Guest Account feature is in beta while we address feedback from our customers on the feature. We anticipate it being in general production in early 2020.

Has the Guest Accounts feature been reviewed by an external security firm?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Guest Account feature was reviewed by the Mattermost security team. We do not have an external firm review scheduled but will include this feature in future reviews.

How can I validate my guests' identity?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Guests can be authenticated via SAML and/or AD/LDAP to ensure that only the named guest can sign in.
Alternatively, you can whitelist domains via **System Console > Guest Access > Whitelisted Guest Domains**.

Can I restrict guests' ability to upload content?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is not currently possible to selectively disable upload/download functionality as it is a server-wide configuration.
