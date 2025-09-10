Attribute-Based Access Control
================================

.. include:: ../../../_static/badges/ent-adv-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v10.9, system admins in large or complex organizations who require Zero Trust Security when handling with sensitive information can prevent unauthorized access through attribute-based access controls.

Enforcing strict access controls based on user attributes eliminates manual role adjustment processes that can lead to security risks, inefficiencies, or inappropriate access, while maintaining security and compliance by ensuring that only authorized users can access specific Mattermost channels.

ABAC provides two levels of control:

- **System-wide policies** (managed by System Admins): Centralized policies that can be applied across multiple channels from the System Console.
- **Channel-specific rules** (managed by Channel Admins): Self-service access rules that Channel Admins can configure directly in Channel Settings for individual channels.

Before you begin
------------------

Attribute-based access controls require defined user attributes that are either synchronized from an external system (such as LDAP or SAML) or manually configured and enabled on your Mattermost server. You'll need to :doc:`configure user attributes </administration-guide/manage/admin/user-attributes>` in the System Console first before creating access policies.

Once user attributes are defined, go to **System Console > System Attributes > Attribute-Based Access** to enable attribute-based access controls for your Mattermost instance. This functionality requires a Mattermost Enterprise Advanced license.

From Mattermost v10.11, user-managed attributes are excluded from attribute-based access control (ABAC) rules by default for security reasons. This prevents access control policies from being circumvented by users editing their own profile attributes. To include user-managed attributes in ABAC rules, a system admin must explicitly enable the ``EnableUserManagedAttributes`` configuration setting. See the :ref:`user attribute <administration-guide/manage/admin/user-attributes:before you begin>` documentation for details on enabling this feature. This configuration setting is available only in Enterprise Edition Advanced and is disabled by default.

Once enabled, you have multiple ways to configure access policies in Mattermost:

**System Admins can:**

- Create `system-wide access policies <#define-access-control-policies>`__ that can be assigned across multiple channels from the System Console.
- Assign `individual channel policies <#define-access-controls-per-channel>`__ to specific channels from the System Console.

**Channel Admins can:**

- Configure `channel-specific access rules <#configure-channel-access-rules>`__ directly in Channel Settings without requiring System Admin intervention.

Define access control policies
-------------------------------

You can add multiple rules to a single policy, and each rule can include multiple attribute values.

1. In the System Console, go to **System Attributes > Attribute-Based Access** and select **Add Policy**.
2. Enter a unique policy name.
3. Choose whether to automatically add users who match your configured attribute values as new members. Automatic synchronization is disabled by default. 

    * **True**: Automatically maintains channel membership according to the defined rules as user attributes change.
    * **False** (**Default**): Only removes members and restricts adding them to the channel if they don’t match defined rules. Users are not automatically added.

    Regardless of whether this configuration setting, users who no longer match the configured attribute values in the future will be removed from the channel after the next channel synchronization.

4. Define the attribute-based access rules to restrict channel membership.

    .. tab:: Simple Mode

      Simple Mode is ideal for simple and straightforward access control scenarios. Each row is a single condition that must be met for a user to comply with the policy. Simple Mode only supports simple conditions without nested logic or mixed logical operators. All rules are combined with a logical AND operator ``&&``.

      1. Select **Add attribute** and select the attribute you want to use for access control.
      2. Specify how you want the attribute to match the user profile. You can choose from the following options:

          - **Is**: The attribute must be an exact match of the value.
          - **Is not**: The attribute must not contain specified value.
          - **In**: The attribute must match at least one value.
          - **Starts with**: The attribute value must start with the specified value.
          - **Ends with**: The attribute value must end with the specified value.
          - **Contains**: The attribute value must exist somewhere with the specified value.

      3. Specify the attribute values that users must have to be granted access to the channel. 

    .. tab:: Advanced Mode

      Advanced Mode is ideal for complex access control scenarios that require CEL syntax to combine multiple conditions with logical operators that support rules like ``user.<attribute> == <value>``, using ``&&`` / ``||`` (and/or) for multiple conditions, and ``()`` to group conditions. The CEL Expression Editor provides real-time syntax validation and feedback, as well as context-aware autocomplete for attributes, operators, and attribute values.

      You can also start defining rules in Simple Mode and then switch to Advanced Mode to refine the rules further as needed. However, you'll be blocked from switching from Advanced back to Simple Mode if one of the following are true:

      * Mixed logical operators are used between conditions.
      * Nested logic/grouping (parentheses) are present.
      * Unsupported operators or expressions are detected.

      The syntax structure is ``user.<attribute> <operator> <value>``.

      As you type, autocompletes show available attributes. As you select attributes, autocomplete suggests appropriate CEL operators. After selecting an operator, when attribute values are pre-defined, autocomplete suggests values to choose from. Mattermost will explicitly indicate issues such as missing operators, incorrect syntax, or incomplete conditions.

      Select the **Validate syntax** bar to check the syntax of your rule. If the syntax is valid, the bar will turn green and display a message indicating that the syntax is valid. If there are any issues, the bar will turn red and display an error message.

Test rules
~~~~~~~~~~~

Select **Test access rule** to test the rule against your user base to return how many users would be granted access to the channel based on the current rule. Test your rules to ensure the intended scope and avoid unexpected access changes.

Manage rules
~~~~~~~~~~~~~

You can apply changes to existing rules or remove rules at any time using either Simple Mode or Advanced Mode. Select **Save** to save your changes.

Assign policies to private channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the private channel that your access control policy applies to by selecting **Add channels** to search for and select the channels you want. You can assign the policy to multiple channels at once, or you can `assign it to individual channels <#define-access-controls-per-channel>`__ later. Select **Save** to save your changes.

.. note::

  Private channels with attribute-based access control policies can't have guest users invited to them. Only users who match the defined attribute criteria can be added to ABAC-controlled channels, ensuring strict adherence to access control policies.

Delete policies
~~~~~~~~~~~~~~~~

To delete a policy, select the **Delete** button next to the policy you want to remove. You can only delete policies that are not currently assigned to any channels. If a policy is assigned to channels, you must first remove it from those channels before you can delete it.

Define access controls per channel
-----------------------------------

You can assign an existing access control policy to a private channels for more granular control over channel membership. This is useful when you need to apply different rules for different channels.

1. In the System Console, go to **User Management > Channels** to select the private channel you want to configure, and select **Edit**.
2. In the **Channel Management** section, enable the **Enable attribute-based channel access** option.
3. Under **Access policy**, select **Link to a policy** to select an existing policy.

Remove channel policies
~~~~~~~~~~~~~~~~~~~~~~~~

Disable the policy for the channel by selecting **Remove Policy**. You can then link the channel to a different policy if preferred.

Configure channel access rules
--------------------------------

Channel Admins can self-manage access controls for their channels directly through the Channel Settings modal, without requiring System Admin intervention. This provides flexibility for confidential discussions while maintaining organizational security policies.

**Who can use this feature:**

- Channel Admins and above with the ``manage_channel_access_rules`` permission
- Available only for private channels
- Requires ABAC to be enabled by a System Admin

**Key capabilities:**

- Create channel-specific access rules using a simple interface
- Rules are **additive** to any system policies (both must be satisfied)
- Automatic member synchronization with immediate feedback
- Self-exclusion prevention to avoid locking yourself out

Access the Channel Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In a private channel where you have Channel Admin permissions, select the channel name at the top of the center pane.
2. Select **Channel Settings** from the dropdown menu.
3. Navigate to the **Access Control** tab.

.. note::
  
  The Access Control tab is only visible for private channels when you have the appropriate permissions and ABAC is enabled system-wide.

Configure access rules
~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~

The **Auto-add members based on access rules** toggle controls automatic membership management:

- **Enabled**: Users matching the rules are automatically added to the channel, and users who no longer match are removed
- **Disabled**: Rules act as a gate (preventing unauthorized joins) but don't automatically add qualifying users

.. important::

  - If a system policy has auto-sync enabled, Channel Admins cannot disable it at the channel level
  - If a system policy has auto-sync disabled, Channel Admins can choose to enable it for their channel
  - When no rules are configured, this toggle is automatically disabled

Validation and safety
~~~~~~~~~~~~~~~~~~~~~~

Before saving changes, Mattermost validates your rules to prevent common issues:

- **Required fields**: All attribute selections and values must be completed
- **Self-exclusion prevention**: You cannot create rules that would remove yourself from the channel
- **Conflict detection**: Rules that create impossible conditions are identified

When you save changes that affect membership, a confirmation dialog shows:

- How many users will be added or removed
- Option to view the specific users affected
- Confirmation required before applying changes

Understanding policy inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When both system policies and channel rules are configured:

1. **System policies** are displayed in a blue banner at the top (read-only)
2. **Channel rules** are managed in the access rules section below
3. **Users must satisfy BOTH** system policies and channel rules to access the channel
4. Channel rules **add restrictions** but cannot weaken system policies

Use cases and recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

- Information banner at the top explaining that attribute-based access is enabled
- Display of required attribute values as tags (e.g., "Engineering", "Confidential")
- Tooltip on hover showing the attribute name for each value

**Add Members modal:**

- Similar information banner and attribute value display
- Users who don't match the access criteria won't appear in search results
- Only eligible users can be selected and added to the channel

Functional restrictions
~~~~~~~~~~~~~~~~~~~~~~~~

When ABAC is enabled for a channel:

- **Search limitations**: Users not matching access criteria don't appear in member search results
- **Invitation restrictions**: Only users meeting attribute requirements can be added to the channel
- **Guest user exclusions**: Private channels with ABAC policies cannot have guest users invited
- **Automatic removal**: Users who lose required attributes are automatically removed during sync

.. note::

  These restrictions apply across all Mattermost clients (web, desktop, and mobile) to ensure consistent security enforcement.

Troubleshooting and FAQs
---------------------------

Common questions about attribute-based access control implementation and usage.

Permission and access questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Q: Why can't I see the Access Control tab in Channel Settings?**

A: The Access Control tab is only visible when all of these conditions are met:

- You have Channel Admin role or higher for the channel
- The channel is a private channel (not public, group message, or direct message)
- ABAC is enabled system-wide by a System Admin
- The Channel Admin ABAC is enabled via the configuration setting AccessControlSettings - EnableUserManagedAttributes
- Your user role includes the ``manage_channel_access_rules`` permission

**Q: Can Channel Admins override system policies?**

A: No. Channel rules are always **additive** to system policies. Users must satisfy both system policies AND channel rules to access the channel. Channel Admins cannot weaken or override restrictions set by System Admins.

**Q: What happens if I create rules that would exclude myself?**

A: Mattermost prevents this with self-exclusion validation. If your rules would remove you from the channel, you'll see an error message and cannot save the changes until you adjust the rules or reset them.

Rule configuration questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Q: Can I use advanced CEL expressions in Channel Settings?**

A: No. Channel Settings only supports Basic Mode with simple attribute conditions. For complex expressions with nested logic or mixed operators, System Admins need to create policies in the System Console.

**Q: How do I remove all access rules from a channel?**

A: Delete all attribute conditions from the access rules table. When no rules are configured and no system policies are applied, the channel returns to standard access behavior.

**Q: Why is the auto-sync toggle disabled?**

A: The auto-sync toggle is automatically disabled when:

- No access rules are configured
- A system policy with auto-sync enabled is applied (Channel Admins cannot disable it)
- There are validation errors in the current rules

Synchronization and membership questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Q: How quickly are membership changes applied?**

A: When you save access rules, membership sync job is created and changes are applied as soon as the job is completed. Additionally, Mattermost runs synchronization jobs every 30 minutes to handle attribute changes from external systems (LDAP, SAML).

**Q: Will users be notified when they're removed from a channel?**

A: Yes, users receive standard Mattermost notifications when they're removed from channels due to access rule changes, similar to manual removals.

**Q: Can I see who was added or removed during synchronization?**

A: Yes, the confirmation modal before saving shows exactly which users will be affected. System Admins can also view detailed synchronization logs in the System Console.

Attribute and data questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Q: Which user attributes can I use in access rules?**

A: You can use any user attributes either synchronized via LDAP/SAML or manually configured by System Admins in **System Console > System Attributes > User Attributes**.

**Q: What happens if a user attribute changes?**

A: During the next synchronization (every 30 minutes), users who no longer match the access rules will be removed from the channel, and new users who now match will be added (if auto-sync is enabled).

**Q: Do guest users work with ABAC channels?**

A: No. Private channels with attribute-based access control cannot have guest users. This ensures strict adherence to access control policies based on organizational attributes.