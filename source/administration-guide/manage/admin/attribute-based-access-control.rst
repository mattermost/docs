Attribute-Based Access Control
================================

.. include:: ../../../_static/badges/ent-adv-cloud-selfhosted.rst
  :start-after: :nosearch:

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

  /administration-guide/manage/admin/abac-system-wide-policies
  /administration-guide/manage/admin/abac-channel-access-rules

From Mattermost v10.9, system admins in large or complex organizations who require Zero Trust Security when handling with sensitive information can prevent unauthorized access through attribute-based access controls.

Enforcing strict access controls based on user attributes eliminates manual role adjustment processes that can lead to security risks, inefficiencies, or inappropriate access, while maintaining security and compliance by ensuring that only authorized users can access specific Mattermost channels.

Access-based access control (ABAC) provides 2 levels of control:

- **System-wide policies** (managed by System Admins): Centralized policies that can be applied across multiple channels in the System Console. See :doc:`System-wide attribute-based access policies </administration-guide/manage/admin/abac-system-wide-policies>`.
- **Channel-specific rules** (managed by Channel Admins): Self-service access rules that Channel Admins can configure directly in Channel Settings for individual channels. See :doc:`Channel-specific access rules </administration-guide/manage/admin/abac-channel-access-rules>`.

Before you begin
------------------

Attribute-based access controls require defined user attributes that are either synchronized from an external system (such as LDAP or SAML) or manually configured and enabled on your Mattermost server. You'll need to :doc:`configure user attributes </administration-guide/manage/admin/user-attributes>` in the System Console first before creating access policies.

Once user attributes are defined, go to **System Console > System Attributes > Attribute-Based Access** to enable attribute-based access controls for your Mattermost instance. This functionality requires a Mattermost Enterprise Advanced license.

From Mattermost v10.11, user-managed attributes are excluded from attribute-based access control (ABAC) rules by default for security reasons. This prevents access control policies from being circumvented by users editing their own profile attributes. To include user-managed attributes in ABAC rules, a system admin must explicitly enable the ``EnableUserManagedAttributes`` configuration setting. See the :ref:`user attribute <administration-guide/manage/admin/user-attributes:before you begin>` documentation for details on enabling this feature. This configuration setting is available only in Enterprise Edition Advanced and is disabled by default.

Configure access policies
--------------------------

Once enabled, you have multiple ways to configure access policies in Mattermost:

**System Admins can:**

- Create :doc:`system-wide access policies </administration-guide/manage/admin/abac-system-wide-policies>` that can be assigned across multiple channels in the System Console.
- Assign :ref:`individual channel policies <administration-guide/manage/admin/abac-system-wide-policies:define access controls per channel>` to specific channels in the System Console.

**Channel Admins can:**

- Configure :doc:`channel-specific access rules </administration-guide/manage/admin/abac-channel-access-rules>` directly in Channel Settings without requiring a system admin.