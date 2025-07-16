Attribute-Based Access Control
================================

.. include:: ../../_static/badges/ent-adv-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v10.9, system admins in large or complex organizations who require Zero Trust Security when handling with sensitive information can prevent unauthorized access through attribute-based access controls.

Enforcing strict access controls based on user attributes eliminates manual role adjustment processes that can lead to security risks, inefficiencies, or inappropriate access, while maintaining security and compliance by ensuring that only authorized users can access specific Mattermost channels.

Before you begin
------------------

Attribute-based access controls require defined user attributes that are either synchronized from an external system (such as LDAP or SAML) or manually configured and enabled on your Mattermost server. You'll need to :doc:`configure user attributes </manage/admin/user-attributes>` in the System Console first befopre creating access policies.

Once user attributes are defined, go to **System Console > System Attributes > Attribute-Based Access** to enable attribute-based access controls for your Mattermost instance. This functionality requires a Mattermost Enterprise Advanced license.

Once enabled, you have 2 ways to configure access policies in Mattermost:

- `Attribute-based access rules <#define-access-control-policies>`__ you can assign across multiple channels.
- `Channel-specific rules <#define-access-controls-per-channel>`__ you can assign to individual channels.

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