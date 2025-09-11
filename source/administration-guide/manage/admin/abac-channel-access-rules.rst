Channel-specific access rules
=============================

.. include:: ../../../_static/badges/ent-adv-cloud-selfhosted.rst
  :start-after: :nosearch:

Channel Admins can self-manage access controls for their private channels directly through the Channel Settings modal, without requiring System Admin intervention. For organization-wide policies created by System Admins, see :doc:`System-wide attribute-based access policies </administration-guide/manage/admin/abac-system-wide-policies>`.

With channel access rules, Channel Admins can:

- Create channel-specific access rules using a simple interface.
- Rules are **additive** to any system policies (both must be satisfied).
- Automatic member synchronization with immediate feedback.
- Self-exclusion prevention to avoid locking yourself out.

Prerequisites
-------------

- :doc:`Attribute-Based Access Control (ABAC) </administration-guide/manage/admin/attribute-based-access-control>` must be enabled by a System Admin in **System Console > System Attributes > Attribute-Based Access**.
- You need Channel Admin permissions and the ``manage_channel_access_rules`` permission.
- Channel access rules are available only for private channels.

Access Channel Settings
~~~~~~~~~~~~~~~~~~~~~~~~

1. In a private channel where you have Channel Admin permissions, select the channel name at the top of the center pane.
2. Select **Channel Settings** from the dropdown menu.
3. Navigate to the **Access Control** tab.

.. note::

  The **Access Control** tab is only visible for private channels when you have the appropriate permissions and ABAC is enabled system-wide.

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

The **Auto-add members based on access rules** toggle controls automatic membership management:

- **Enabled**: Users matching the rules are automatically added to the channel, and users who no longer match are removed
- **Disabled**: Rules act as a gate (preventing unauthorized joins) but don't automatically add qualifying users

.. important::

  - If a system policy has auto-sync enabled, Channel Admins cannot disable it at the channel level.
  - If a system policy has auto-sync disabled, Channel Admins can choose to enable it for their channel.
  - When no rules are configured, this toggle is automatically disabled.

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

Policy inheritance
--------------------

When both :doc:`system policies </administration-guide/manage/admin/abac-system-wide-policies>` and channel rules are configured:

1. **System policies** are displayed in a blue banner at the top (read-only)
2. **Channel rules** are managed in the access rules section below
3. **Users must satisfy BOTH** system policies and channel rules to access the channel
4. Channel rules **add restrictions** but cannot weaken system policies

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
- ABAC is enabled system-wide by a System Admin
- The Channel Admin ABAC is enabled via the configuration setting AccessControlSettings - EnableUserManagedAttributes
- Your user role includes the ``manage_channel_access_rules`` permission

Can Channel Admins override system policies?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Channel rules are always **additive** to system policies. Users must satisfy both system policies AND channel rules to access the channel. Channel Admins cannot weaken or override restrictions set by System Admins.

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
- A system policy with auto-sync enabled is applied (Channel Admins cannot disable it)
- There are validation errors in the current rules

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