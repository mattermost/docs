Channel-specific access rules
=============================

.. include:: ../../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

Channel and Team Admins can self-manage access controls for their channels directly through the Channel Settings modal, without requiring System Admin intervention. For organization-wide policies created by System Admins, see :doc:`System-wide attribute-based access policies </administration-guide/manage/admin/abac-system-wide-policies>`.

From Mattermost v11.8, channel access rules can be applied to **both private and public channels**. The two channel types behave differently under ABAC:

- **Private channels** are hard-gated. Non-matching members are removed during synchronization, and only matching users can be added or invited.
- **Public channels** are advisory. Non-matching members are *never* removed (anyone can still join a public channel by browsing or via a direct link). With auto-add enabled the policy still pulls matching users in; with auto-add disabled the channel surfaces under **Browse Channels > Recommended channels** for users whose attributes match.

Each ABAC channel access policy has an explicit active state that determines whether the policy will automatically add users who meet the policy's criteria but are not yet channel members. For private channels, the policy's rules are always enforced to remove members who no longer meet the required attribute rules, regardless of the active state. For public channels, no member is ever removed by ABAC — the rules are advisory only.

With channel access rules, Channel and Team Admins can:

- Create channel-specific access rules using a simple interface.
- Rules are **additive** to any system policies (both must be satisfied).
- Automatic member synchronization with immediate feedback.
- Self-exclusion prevention to avoid locking yourself out (private channels only).

Prerequisites
-------------

- :doc:`Attribute-Based Access Control (ABAC) </administration-guide/manage/admin/attribute-based-access-control>` must be enabled by a System Admin in **System Console > System Attributes > Attribute-Based Access**.
- You need Channel Admin permissions and the ``manage_channel_access_rules`` permission.
- Channel access rules are available for private and public channels. Default channels (such as Town Square and Off-Topic), shared channels, and group-synced channels remain ineligible.

Access Channel Settings
~~~~~~~~~~~~~~~~~~~~~~~~

1. In a private or public channel where you have Channel Admin permissions, select the channel name at the top of the center pane.
2. Select **Channel Settings** from the dropdown menu.
3. Navigate to the **Membership Policy** tab. This tab is only visible for eligible channels when you have the appropriate permissions and ABAC is enabled system-wide. The tab is hidden on default channels, shared channels, and group-synced channels.

.. tip::

  You can also assign ABAC rules to a channel directly from a channel's details page in the System Console under **Channel Management** by enabling the **Enable attribute-based channel access** option. Under **Access policy**, select **Link to a policy** to select an existing policy.

Configure access rules
----------------------

Channel access rules use the same simple interface as system policies, allowing you to create attribute-based conditions without complex syntax.

1. In the **Membership Policy** tab, you'll see any inherited system policies at the top in a blue information banner (if applicable).
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

The **Auto-add members based on access rules** toggle controls automatic membership management. The behavior differs by channel type:

- **Private channels (hard gate)**: Membership stays consistently aligned with the rules, similar to how LDAP group channels work.

  - **Enabled**: Users matching the rules are automatically added. If users temporarily lose attributes and later regain them, they will be automatically re-added.
  - **Disabled**: Rules act as a gate (preventing unauthorized joins) but don't automatically add qualifying users.

- **Public channels (advisory)**: ABAC never removes members — anyone can still join a public channel.

  - **Enabled**: Matching users are automatically added (a convenience, not a gate).
  - **Disabled**: The channel appears under **Browse Channels > Recommended channels** for users whose attributes match, surfacing the channel without adding anyone.

.. important::

  - Auto-add/auto-sync is checked on a per-channel policy basis, not inherited from parent system-wide policies.
  - If a system policy has auto-sync enabled, Channel and Team Admins cannot disable it at the channel level.
  - If a system policy has auto-sync disabled, Channel and Team Admins can choose to enable it for their channel.
  - When no rules are configured, this toggle is automatically disabled.
  - On **private** channels, users who no longer meet required attribute rules are always removed during synchronization regardless of the auto-sync setting. On **public** channels, no member is ever removed by ABAC.

Validation and safety
~~~~~~~~~~~~~~~~~~~~~

Before saving changes, Mattermost validates your rules to prevent common issues:

- **Required fields**: All attribute selections and values must be completed.
- **Self-exclusion prevention**: For private channels, you cannot save rules that would remove yourself from the channel. The check is skipped for public channels because they are advisory under ABAC and can't lock anyone out.
- **Conflict detection**: Rules that create impossible conditions are identified.

When you save changes that affect membership, a confirmation dialog shows you:

- How many users will be added or removed.
- Option to view the specific users affected.
- Confirmation required before applying changes.

Once a policy is attached to a channel, the channel cannot be converted between public and private until the policy is removed. The two modes have different semantics (advisory vs. hard gate), so a silent conversion would change what an existing policy actually does to its members.

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

- Information banner at the top explains that attribute-based access is enabled. The wording differs by channel type: private channels say *"Channel access is restricted by user attributes"*; public channels say *"This channel has recommended members based on user attributes"*.
- Displays required attribute values as tags (e.g., "Engineering", "Confidential").
- Tooltip on hover shows the attribute name for each value.

**Add Members modal:**

- Similar information banner and attribute value display.
- On **private** channels, users who don't match the access criteria won't appear in search results — only eligible users can be added.
- On **public** channels, the full team list is shown and matching users are surfaced with a **Recommended** tag at the top of the list. Anyone can still be added because public-channel ABAC is advisory.

**Browse Channels:**

- A **Recommended channels** filter is available in the channel-type dropdown when ABAC is enabled. Selecting it lists the public channels whose policies the user matches — useful when auto-add is disabled and the channel is offered as a recommendation rather than auto-joined.

Functional restrictions
~~~~~~~~~~~~~~~~~~~~~~~~

When ABAC is enabled for a **private** channel:

- **Search limitations**: Users who don't match access criteria don't appear in member search results.
- **Invitation restrictions**: Only users meeting attribute requirements can be added to the channel.
- **Guest user exclusions**: Private channels with ABAC policies cannot have guest users invited.
- **Automatic removal**: Users who lose required attributes are automatically removed during the next synchronization.

When ABAC is enabled for a **public** channel:

- **Search results are unfiltered**: All eligible team members appear in the Add Members modal so admins can still invite anyone; matching users carry a **Recommended** tag.
- **Recommendations**: With auto-add disabled, the channel surfaces under **Browse Channels > Recommended channels** for matching users.
- **Auto-add (when enabled)**: Matching users are added automatically. **Members are never removed** by ABAC — users can always leave on their own, and joining freely is unaffected because the channel is public.

.. note::

  These behaviors apply across all Mattermost clients, including web, desktop, and mobile, to ensure consistent enforcement.

Troubleshooting and FAQs
---------------------------

Common questions about attribute-based access control implementation and usage.

Permission and access
~~~~~~~~~~~~~~~~~~~~~~

Why can't I see the Membership Policy tab in Channel Settings?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Membership Policy** tab is only visible when all of these conditions are met:

- You have Channel Admin role or higher for the channel.
- The channel is a private or public channel (not a default channel like Town Square or Off-Topic, group message, direct message, shared, or group-synced channel).
- ABAC is enabled system-wide by a System Admin in **System Console > System Attributes > Attribute-Based Access**.
- Your user role includes the ``manage_channel_access_rules`` permission.

Can Channel and Team Admins override system policies?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Channel rules are always **additive** to system policies. Users must satisfy both system policies AND channel rules to access the channel. Channel and Team Admins cannot weaken or override restrictions set by System Admins.

What happens if I create rules that would exclude myself?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For **private** channels, Mattermost prevents this with self-exclusion validation. If your rules would remove you from the channel, you'll see an error message and cannot save the changes until you adjust the rules or reset them.

For **public** channels, the self-exclusion check is skipped — public-channel ABAC is advisory, the policy can't kick anyone out, and you can always re-join a public channel directly. This lets you author a policy intended for a different team (for example, a Sales admin configuring an Engineering recommendation) without being blocked.

Can I convert a public channel to private (or vice versa) while a policy is attached?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. The two modes have different semantics — a public-channel policy is advisory while a private-channel policy is a hard gate that removes non-matching members. A silent conversion would change what the existing policy does to its members, so Mattermost requires you to remove the policy first, convert the channel, and re-attach the policy if you still want it.

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