.. _guest-accounts:

Guest accounts
==============

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

Guest accounts are a way to collaborate with individuals, such as vendors and contractors, outside of your organization by controlling their access to channels and team members. For example, guest accounts can be used to collaborate with customers on a support issue or work on a website project with resources from an external design firm.

.. include:: /onboard/guest-account-access.rst
  :start-after: :nosearch:

Additionally, guest accounts count as a paid user in your Mattermost workspace, but guests aren't automatically added to the default **Town-square** and **Off-topic** channels when they log in. Guests must be invited/added to these channels manually.

Enable guest accounts
----------------------

1. Go to **System Console > Authentication > Guest Access**.
2. Set **Enable Guest Access** to **true**.
3. (Optional) Specify the **Whitelisted Guest Domains** that are acceptable for guest access. This allows the system admin to set a list of approved guest domains.
4. (Optional) Set **Enforce Multi-factor Authentication** to **true**. If you're enforcing MFA for your users, you can optionally choose to also enforce MFA for your guest users.
 
.. note::

  If you have team domain restrictions, you also need to add your guest domain in **System Console > User Management > Teams**. Select a team, then enable **Only specific email domains can join this team**.

Guest authentication
---------------------

Guests can access the Mattermost server via email invitation, and be authenticated using AD/LDAP or SAML 2.0.

Before you proceed, ensure that the authentication method you wish to use is correctly configured on your server and enabled in Mattermost. For configuration steps and technical documentation, see :doc:`Active Directory/LDAP setup </onboard/ad-ldap>` and :doc:`SAML Single-Sign-On </onboard/sso-saml>`.

Converting a member user to a guest won't change the channels they are in. However, they will be restricted from discovering additional channels and are unable to direct message/group message users outside of the channels they are in. They can be added to channels by system admins and other roles that have the correct permissions to invite guests.

Invite guests to the Mattermost server via email
-------------------------------------------------

Guests can be invited into one or more Mattermost channels within a team by system admins and other roles that have the correct permission to invite guests. A guest can be invited into channels on multiple teams.

.. note::
  
  Guest invitations are revoked after 48 hours per the member email invitation process. If your guest has not accepted the invitation within that period, please follow the steps below to resend an invitation to the guest.

To invite guests into one or more Mattermost channels:

1. Go to **System Console > Signup > Enable Email Invitations** to enable email invites.
2. Select your team's name at the top of the channel sidebar and choose **Invite People**.
3. Select **Invite Guests**.
4. Enter the guest’s email address.
5. Choose the channels the guest can join (excluding managed teams).
6. (Optional) Enter a custom message.

.. image:: ../images/Guest_Invite_Screen.png

Configure AD/LDAP authentication
---------------------------------

When enabled, the **Guest Filter** in Mattermost identifies external users whose AD/LDAP role is ``guest`` and who are invited to join your Mattermost server. These users will have the ``guest`` role applied immediately upon first login instead of the default member user role. This eliminates having to manually assign the role in the System Console.

1. Go to **System Console > Authentication > Guest Access** to enable guest access.
2. Go to **System Console > Authentication > AD/LDAP**.
3. Complete the **Guest Filter** field.
4. Select **Save**.

If a Mattermost guest user has the ``guest`` role removed in the AD/LDAP system, the synchronization process will not automatically promote them to a member user role. This is done manually via **System Console > User Management**. If a member user has the **Guest Attribute** added, the synchronization processes will automatically demote the member user to the guest role.

When a guest logs in without having any channels assigned to their account, they're advised to contact a Mattermost system admin. 

Configure SAML 2.0 authentication
----------------------------------

When enabled, the **Guest Attribute** in Mattermost identifies external users whose SAML assertion is guest and who are invited to join your Mattermost server. These users will have the ``guest`` role applied immediately upon first login instead of the default member user role. This eliminates having to manually assign the role in the System Console.

If a Mattermost guest user has the guest role removed in the SAML system, the synchronization processes will not automatically promote them to a member user role. This is done manually via **System Console > User Management**. If a member user has the **Guest Attribute** added, the synchronization processes will automatically demote the member user to the guest role.

1. Go to **System Console > Guest Access** to enable guest access.
2. Go to **System Console > Authentication > SAML 2.0**.
3. Complete the **Guest Attribute** field.
4. Select **Save**.

When a guest logs in without having any channels assigned to their account, they're advised to contact a Mattermost System Admin.

Guest permission settings
-------------------------

In Mattermost Enterprise and Professional, you can control which users can invite guests. By default, only the System Admins can invite guests.

There are :doc:`additional permissions </onboard/advanced-permissions>` in Mattermost Enterprise that can be adjusted under **System Console > User Management > Permissions > System Scheme** to control a guest’s ability to:

 - Edit posts
 - Delete posts
 - Post reactions
 - Create private channels with members they are allowed to collaborate with

Guest identification
---------------------

Guests are identified with a **Guest** badge unless your system admin has :ref:`disabled guest badges <configure/authentication-configuration-settings:guest access>`. When visible, this badge is visible in various places in the Mattermost interface, such as on a guest’s profile and next to their name on user lists, including @mentions. Additionally, when badges are visible, and guests are added to a channel, a system message notifies other channel members that the added user is a guest.

Additionally, when guest badges are visible, channels containing guests display the message: *This channel has guests*.

.. image:: ../images/Guest_Badges.png

Manage guests
--------------

Add guests to additional channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users with the permissions to invite guests can **Invite Guests** to additional channels. A system message will be posted in the channels to let other members know a guest user has been added.

Remove guests from channels and teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Guests can be removed from a channel through **Manage members**, or by using the ``/kick`` or ``/remove`` slash commands.

When a guest has been removed from all channels within a team, and if they belong to other teams, they will default into the last channel on the last team they have accessed. If they are removed from all channels on all teams, they'll be taken to a screen letting them know they have no channels assigned.

Promote and demote user roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System admins can demote a user from a member to a guest by updating the user's role in **System Console > User Management > Users**. Select the member, then select **Demote to Guest**. All system and custom roles assigned to the demoted user are removed. System admins should also purge all of the demoted guest's sessions by selecting the guest user, then selecting **Revoke Sessions**.

The demoted guest user retains their existing channel and team memberships, but is restricted from discovering public channels and collaborating with users outside of the channels they're in. This is useful if you're already collaborating with external contractors, and want to restrict their abilities within Mattermost.

System admins can also promote a guest to member by updating their role in **System Console > User Management > Users**. Select the guest, then select **Promote to Member**.

.. note::
  
  You can filter the list in **System Console > User Management > Users** to view all guests in the system.

Disable guest accounts
-----------------------

To disable the guest accounts feature, go to **System Console > Authentication > Guest Access**, then set **Enable Guest Access** to **False**. To deactivate individual guest accounts, go to **System Console > User Management > Users**. Select a user, then select **Deactivate**. You can re-activate individual guest accounts by selecting **Activate**.

- When a single guest account is deactivated or the guest account feature is disabled, guests are marked as ``deactivated``, are logged out of Mattermost, and all guest sessions are revoked. In Mattermost Server versions prior to 5.18, disabling the guest account feature leaves current guest accounts as activated until they are manually deactivated.
- If you're using AD/LDAP and the guest access setting is disabled, the ``guest`` filter and existing guest users in System Console are deactivated. Additionally, no new guests can be invited or added using the filter as an authentication method. If a previous guest's credentials match the user filter (the only filter which is active when guest access is disabled), they will be reactivated and promoted to a member user upon their next login.
- Similarly, for SAML, when the guest access setting is disabled, the ``guest`` attribute and existing guest users in System Console are deactivated. Additionally, no new guests can be invited or added using the attribute as an authentication method. If a previous guest's credentials match the user attribute (the only attribute which is active when guest access is disabled), they will be reactivated and promoted to a member user upon their next login.

You can disable individual guest accounts in **System Console > User Management** via **Manage Members**. When a single guest account is disabled or the feature is disabled, the guest will be marked as ``deactivated``, be logged out of Mattermost, and all their sessions will be revoked.

Reinstate guest accounts
-------------------------

When guest access is re-enabled for AD/LDAP, the ``guest`` filter is reinstated. 

New users matching the ``guest`` filter will be authenticated as new guest users on login.

Previous guest users will be activated with the next synchronization. If their credentials still match the ``guest`` filter, they will retain their guest status. If they no longer match the ``guest`` filter but do match the ``user`` filter, they will be not be promoted to member user automatically on login - this must be done manually. If a previous guest was reactivated as a member user when guest access was disabled, and now are identified by the ``guest`` filter once again, they will automatically be demoted to Guest upon their login.

Similarly, for SAML, when guest access is re-enabled, the SAML ``guest`` attribute is reinstated. New users matching the ``guest`` attribute will be authenticated as new guest users on login.

Previous guest users will be activated with the next synchronization. If their credentials still match the ``guest`` attribute, they will retain their guest status. If they no longer match the ``guest`` attribute but do match the ``user`` filter, they will be not be promoted to member user automatically on login - this must be done manually. If a previous guest was reactivated as a member user when guest access was disabled, and now are identified by the ``guest`` attribute once again, they will automatically be demoted to guest upon their login.

Frequently asked questions
---------------------------

How am I charged for guest accounts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Guests are charged as a user seat.

Why doesn’t Mattermost have single-channel guests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We wanted to support collaboration with external guests for the broadest use cases without limiting guests' access to channels. In the future, we may consider adding single-channel guests.

Can I set an expiration date for guests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, you cannot. This feature may be added at a later stage.

Can MFA be applied selectively?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If MFA is enforced for your users, it can be applied to guest accounts. Guests can configure MFA in by going to their profile picture and selecting **Profile > Security**. If MFA is not enforced for your users, it can't be applied to guest accounts.

Has the guest accounts feature been reviewed by an external security firm?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The guest account feature was reviewed by the Mattermost security team. We do not have an external firm review scheduled but will include this feature in future reviews.

How can I validate my guests' identity?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Guests can be authenticated via SAML and/or AD/LDAP to ensure that only the named guest can log in. Alternatively, you can whitelist domains via **System Console > Authentication > Guest Access > Whitelisted Guest Domains**.

Can I restrict guests' ability to upload content?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is not currently possible to selectively disable upload/download functionality as it is a server-wide configuration.
