Channel-specific access rules
=============================

.. include:: ../../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

Channel and Team Admins can self-manage access controls for their private channels directly through the Channel Settings modal, without requiring System Admin intervention. For organization-wide policies created by System Admins, see :doc:`System-wide attribute-based access policies </administration-guide/manage/admin/abac-system-wide-policies>`. For team-scoped policies that apply rules across multiple private channels within a team, see :doc:`Team-level channel membership policies </administration-guide/manage/admin/abac-team-channel-policies>`.

Each ABAC channel access policy has an explicit active state that determines whether the policy will automatically add users who meet the policy's criteria but are not yet channel members. When a policy is applied to a channel, the policy's rules are always enforced to remove members who no longer meet the required attribute rules, regardless of the active state.

With channel access rules, Channel and Team Admins can:

- Create channel-specific access rules using a simple interface.
- Rules are **additive** to any system policies (both must be satisfied).
- Automatic member synchronization with immediate feedback.
- Self-exclusion prevention to avoid locking yourself out.

Prerequisites
-------------

- :doc:`Attribute-Based Access Control (ABAC) </administration-guide/manage/admin/attribute-based-access-control>` must be enabled by a System Admin in **System Console > System Attributes > Attribute-Based Access**.
- You need Channel Admin permissions and the ``manage_channel_access_rules`` permission.
- Self-service access rules in the **Access Control** tab of Channel Settings apply only to private channels. Membership policies apply to both public and private channels, with behavior that varies by channel type. See :ref:`Public and private channel behavior <administration-guide/manage/admin/abac-channel-access-rules:public and private channel behavior>`.

Access Channel Settings
~~~~~~~~~~~~~~~~~~~~~~~~

1. In a private channel where you have Channel Admin permissions, select the channel name at the top of the center pane.
2. Select **Channel Settings** from the dropdown menu.
3. Navigate to the **Access Control** tab. This tab is only visible for private channels when you have the appropriate permissions and ABAC is enabled system-wide.

.. tip::

  You can also assign ABAC rules to a channel directly from a channel's details page in the System Console under **Channel Management** by enabling the **Enable attribute-based channel access** option. Under **Access policy**, select **Link to a policy** to select an existing policy.

Configure access rules
----------------------

Channel access rules use the same simple interface as system policies, allowing you to create attribute-based conditions without complex syntax.

1. In the **Access Control** tab, you'll see any inherited system policies at the top in a blue information banner (if applicable).
2. Use the **Add attribute** button to create new access conditions:

   - **Select attribute**: Choose from available user attributes
   - **Choose operator**: Select how the attribute should match:

     - **Is**: Exact match with specified value
     - **Is not**: Must not match specified value  
     - **In**: Must match any of multiple specified values
     - **Contains**: Attribute value must contain specified text

   - **Set values**: Enter the required attribute values

3. Add multiple conditions as needed. All conditions are combined with logical AND (all must be satisfied).

4. Select **Test access rules** to preview which users would be granted access based on your current rules.

Auto-sync membership
~~~~~~~~~~~~~~~~~~~~

The **Auto-add members based on access rules** toggle controls automatic membership management. This setting ensures that channel membership stays consistently aligned with the defined attribute rules, similar to how LDAP group channels work:

- **Enabled**: Users matching the rules are automatically added to the channel. If users temporarily lose attributes and later regain them, they will be automatically re-added
- **Disabled**: Rules act as a gate (preventing unauthorized joins) but don't automatically add qualifying users

.. important::

  - Auto-add/auto-sync is checked on a per-channel policy basis, not inherited from parent system-wide policies.
  - If a system policy has auto-sync enabled, Channel and Team Admins cannot disable it at the channel level.
  - If a system policy has auto-sync disabled, Channel and Team Admins can choose to enable it for their channel.
  - When no rules are configured, this toggle is automatically disabled.
  - Regardless of the auto-sync setting, users who no longer meet required attribute rules are always removed during synchronization.

Validation and safety
~~~~~~~~~~~~~~~~~~~~~

Before saving changes, Mattermost validates your rules to prevent common issues:

- **Required fields**: All attribute selections and values must be completed
- **Self-exclusion prevention**: You cannot create rules that would remove yourself from the channel
- **Conflict detection**: Rules that create impossible conditions are identified

When you save changes that affect membership, a confirmation dialog shows you:

- How many users will be added or removed
- Option to view the specific users affected
- Confirmation required before applying changes

Public and private channel behavior
-----------------------------------

Membership policies behave differently depending on the type of channel they're applied to:

- **Private channels**: Membership policies are enforced. Users who match the policy's rules are added, and users who don't match the rules are removed during synchronization.
- **Public channels**: Membership policies are advisory. Matching users may be automatically added when auto-add is enabled, but non-matching members are not removed.
- When auto-add is disabled for a public channel, matching channels are surfaced as **recommended** rather than enforcing membership.
- Direct messages and group messages aren't eligible for membership policies.
- Default channels such as **Town Square** and **Off-Topic** are excluded.

.. note::

  Public channels with membership policies may appear in **Browse Channels** under **Recommended**, and matching users may be marked **Recommended** in the channel invite flow. See :doc:`Browse channels </end-user-guide/collaborate/browse-channels>` and :doc:`Manage channel members </end-user-guide/collaborate/manage-channel-members>` for the end-user experience.

Channel-level permission policies
---------------------------------

From Mattermost v11.8.0, admins can define channel-level permission rules for file upload and file download based on user attributes and channel role. Applicable roles include **channel admin**, **channel member**, and **channel guest**.

For system-wide permission policies that restrict file upload and download actions, see :ref:`Permission policies <administration-guide/manage/admin/abac-system-wide-policies:permission policies>`.

Simulate access
----------------

From Mattermost v11.8.0, admins can use **Simulate access** in Channel Settings to preview whether selected users can perform actions such as joining a channel, uploading files, or downloading files before saving policy changes.

- Simulation can evaluate draft rules before they're saved, so you can confirm the intended scope without affecting live channel access.
- Some denied results may indicate that the decision came from another policy. In that case, Mattermost shows that access was denied by another policy without exposing policy details you aren't authorized to see.

Manage team-scoped membership policies in Team Settings
-------------------------------------------------------

From Mattermost v11.7, Team Admins can create, edit, and delete channel membership policies directly from Team Settings, scoped to channels within their team. This lets teams self-manage attribute-based membership for their own channels without requiring a System Admin to create or modify a system-wide policy.

Prerequisites
~~~~~~~~~~~~~

- :doc:`Attribute-Based Access Control (ABAC) </administration-guide/manage/admin/attribute-based-access-control>` must be enabled by a System Admin in **System Console > System Attributes > Attribute-Based Access**.
- You need Team Admin permissions for the team and the ``manage_team_access_rules`` permission.
- Team-scoped membership policies can be assigned to both public and private channels within the team.

Team Admin workflow
~~~~~~~~~~~~~~~~~~~

1. Open **Team Settings** from the team menu, and go to the **Membership Policies** tab. This tab is only visible to Team Admins with the ``manage_team_access_rules`` permission when ABAC is enabled system-wide.
2. Select **Add Policy** and enter a name for the policy. Parent policy names must be unique; if you enter a name that's already in use, Mattermost displays a user-friendly error and prevents the policy from being saved.
3. Define the attribute rules that determine which users can be members of channels assigned to this policy. Rules use the same attribute conditions available for channel-specific access rules.
4. Assign the applicable private channels in the team to the policy.
5. Select **Save** to create or update the policy. Team-scoped policies can be edited or deleted from the same tab at any time.

Team Settings sync status footer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Membership Policies** tab includes a sync status footer that shows:

- **Last sync time**: The time of the most recent membership synchronization for policies in this team.
- **Sync now**: An on-demand action that triggers an immediate synchronization for the team's policies.

Team-scoped sync is limited to the team admin's team scope. Triggering **Sync now** from Team Settings does not affect channels or policies outside the current team.

Sync behavior by channel type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sync behavior for team-scoped membership policies depends on the type of channel the policy is assigned to:

- **Public channels**: Sync is advisory and add-only. Users who match the policy's rules are added to the channel, but no users are removed if their attributes change.
- **Private channels**: Sync is enforced. Users who match the policy's rules are added to the channel, and users who no longer match the rules are removed during the next synchronization.

Automatic sync on policy changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost automatically runs a sync job whenever a team-scoped membership policy is created, or its rules, assigned channels, or active state change. Team Admins don't need to manually trigger **Sync now** for these updates; the sync runs as part of the change.

Policy inheritance
--------------------

Channel-level (child) ABAC policies now behave independently and consistently, even when parent system-wide policies exist. Each policy maintains its own active state and configuration.

When both :doc:`system policies </administration-guide/manage/admin/abac-system-wide-policies>` and channel rules are configured:

1. **System policies** are displayed in a blue banner at the top (read-only)
2. **Channel rules** are managed in the access rules section below
3. **Users must satisfy BOTH** system policies and channel rules to access the channel
4. Channel rules **add restrictions** but cannot weaken system policies
5. **Auto-add behavior** is determined by the individual channel policy, not inherited from parent system-wide policies. System-wide policies can pass down their rules, but auto-add/auto-sync is evaluated per channel.

Use cases and recommendations
-----------------------------

**Ideal use cases for channel access rules:**

- **Project-specific channels**: Restrict access to team members working on specific projects
- **Clearance-based discussions**: Ensure only users with appropriate security clearance can participate
- **Department communications**: Limit channel access to specific organizational units
- **Temporary access**: Create rules for short-term project teams or contractor access

**Best practices:**

- **Start simple**: Begin with basic attribute conditions before adding complexity
- **Test before saving**: Always use the "Test access rules" feature to verify your intended scope
- **Document changes**: Consider posting a message in the channel when access rules change
- **Regular review**: Periodically review rules to ensure they remain appropriate
- **Coordinate with IT**: Work with System Admins for complex organizational policies

**When to use system policies vs. channel rules:**

- **System policies**: Use for organization-wide standards, compliance requirements, or policies affecting multiple channels
- **Channel rules**: Use for channel-specific restrictions, project-based access, or when you need immediate control without IT involvement

End-user experience
--------------------

When channels have attribute-based access controls applied, users will see clear indicators and experience specific behaviors designed to maintain security while providing transparency.

Visual indicators
~~~~~~~~~~~~~~~~~~

**Channel Members panel:**

- Information banner at the top explains that attribute-based access is enabled.
- Displays required attribute values as tags (e.g., "Engineering", "Confidential").
- Tooltip on hover shows the attribute name for each value.

**Add Members modal:**

- Similar information banner and attribute value display.
- Users who don't match the access criteria won't appear in search results.
- Only eligible users can be selected and added to the channel.

Functional restrictions
~~~~~~~~~~~~~~~~~~~~~~~~

When ABAC is enabled for a channel:

- **Search limitations**: Users who don't match access criteria don't appear in member search results.
- **Invitation restrictions**: Only users meeting attribute requirements can be added to the channel.
- **Guest user exclusions**: Private channels with ABAC policies cannot have guest users invited.
- **Automatic removal**: Users who lose required attributes are automatically removed during the next synchronization.

.. note::

  These restrictions apply across all Mattermost clients, including web, desktop, and mobile, to ensure consistent security enforcement.

Troubleshooting and FAQs
---------------------------

Common questions about attribute-based access control implementation and usage.

Permission and access
~~~~~~~~~~~~~~~~~~~~~~

Why can't I see the Access Control tab in Channel Settings?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Access Control** tab is only visible when all of these conditions are met:

- You have Channel Admin role or higher for the channel
- The channel is a private channel (not public, group message, or direct message)
- ABAC is enabled system-wide by a System Admin in **System Console > System Attributes > Attribute-Based Access**
- Your user role includes the ``manage_channel_access_rules`` permission

Can Channel and Team Admins override system policies?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Channel rules are always **additive** to system policies. Users must satisfy both system policies AND channel rules to access the channel. Channel and Team Admins cannot weaken or override restrictions set by System Admins.

What happens if I create rules that would exclude myself?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost prevents this with self-exclusion validation. If your rules would remove you from the channel, you'll see an error message and cannot save the changes until you adjust the rules or reset them.

Rule configuration
~~~~~~~~~~~~~~~~~~~

Can I use advanced CEL expressions in Channel Settings?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Channel Settings only supports Basic Mode with simple attribute conditions. For complex expressions with nested logic or mixed operators, System Admins need to create policies in the System Console.

How do I remove all access rules from a channel?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete all attribute conditions from the access rules table. When no rules are configured and no system policies are applied, the channel returns to standard access behavior.

Why is the auto-sync toggle disabled?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The auto-sync toggle is automatically disabled when:

- No access rules are configured
- A system policy with auto-sync enabled is applied (Channel and Team Admins cannot disable it)
- There are validation errors in the current rules
- The channel's access control policy is not in an active state

.. note::

  **Troubleshooting auto-sync issues**: If auto-sync functionality (automatic adding/re-adding of members) is not working as expected, verify that the channel's access control policy is in an active state. An inactive policy will prevent automatic member additions from occurring. Note that enforcement of rules (removal of members who no longer meet requirements) happens regardless of the policy's active state.

Synchronization and membership 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How quickly are membership changes applied?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you save access rules, membership sync job is created and changes are applied as soon as the job is completed. Additionally, Mattermost runs synchronization jobs every 30 minutes to handle attribute changes from external systems (LDAP, SAML).

Will users be notified when they're removed from a channel?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, users receive standard Mattermost notifications when they're removed from channels due to access rule changes, similar to manual removals.

Can I see who was added or removed during synchronization?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, the confirmation modal before saving shows exactly which users will be affected. System Admins can also view detailed synchronization logs in the System Console.

Attribute and data questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Which user attributes can I use in access rules?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use any user attributes either synchronized via LDAP/SAML or manually configured by System Admins in **System Console > System Attributes > User Attributes**.

What happens if a user attribute changes?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During the next synchronization (every 30 minutes), users who no longer match the access rules will be removed from the channel, and new users who now match will be added (if auto-sync is enabled).

Do guest users work with ABAC channels?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Private channels with attribute-based access control cannot have guest users. This ensures strict adherence to access control policies based on organizational attributes.

Can group-sync channels use ABAC?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Channels configured with group synchronization cannot use attribute-based access control. Group-sync and ABAC are mutually exclusive features - you must choose one method of access control per channel.