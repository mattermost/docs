Attribute-Based Access Control
================================

.. include:: ../../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

  /administration-guide/manage/admin/abac-system-wide-policies
  /administration-guide/manage/admin/abac-team-channel-policies
  /administration-guide/manage/admin/abac-channel-access-rules

From Mattermost v10.9, system admins in large or complex organizations who require Zero Trust Security when handling with sensitive information can prevent unauthorized access through attribute-based access controls.

Enforcing strict access controls based on user attributes eliminates manual role adjustment processes that can lead to security risks, inefficiencies, or inappropriate access, while maintaining security and compliance by ensuring that only authorized users can access specific Mattermost channels.

Attribute-based access control (ABAC) can be used with the following policy types:

- **System-wide access policies** (managed by System Admins): Centralized policies created in the System Console that can be applied across multiple channels. See :doc:`System-wide attribute-based access policies </administration-guide/manage/admin/abac-system-wide-policies>`.
- **Permission policies** (managed by System Admins): Attribute-based restrictions on user actions such as file upload and file download. See :ref:`Permission policies <administration-guide/manage/admin/abac-system-wide-policies:permission policies>`.
- **Team-scoped membership policies** (managed by Team Admins): Channel membership policies that Team Admins can create, edit, and delete directly from Team Settings for channels in their team. See :ref:`Manage team-scoped membership policies in Team Settings <administration-guide/manage/admin/abac-channel-access-rules:manage team-scoped membership policies in team settings>`.
- **Channel-specific access rules** (managed by Channel Admins): Self-service access rules that Channel Admins can configure directly in Channel Settings for individual channels. See :doc:`Channel-specific access rules </administration-guide/manage/admin/abac-channel-access-rules>`.

Before you begin
------------------

Attribute-based access controls require defined user attributes that are either synchronized from an external system (such as LDAP or SAML) or manually configured and enabled on your Mattermost server. You'll need to :doc:`configure user attributes </administration-guide/manage/admin/user-attributes>` in the System Console first before creating access policies.

Each attribute becomes a user profile option users can populate, unless you disable the **Editable by Users** option, available from Mattermost v11. Admin-managed attributes can be used in addition to the LDAP/SAML synchronized attributes for attribute-based access control rules.

Once user attributes are defined, go to **System Console > System Attributes > Attribute-Based Access** to enable attribute-based access controls for your Mattermost instance. This functionality requires a Mattermost Enterprise Advanced license.

From Mattermost v10.11, user-managed attributes are excluded from attribute-based access control (ABAC) rules by default for security reasons. This prevents access control policies from being circumvented by users editing their own profile attributes. To include user-managed attributes in ABAC rules, a system admin must explicitly enable the ``EnableUserManagedAttributes`` configuration setting. See the :ref:`user attribute <administration-guide/manage/admin/user-attributes:before you begin>` documentation for details on enabling this feature. This configuration setting is available only in Enterprise Edition Advanced and is disabled by default.

Configure access policies
--------------------------

Once enabled, you have multiple ways to configure access policies in Mattermost:

From Mattermost v11.8.0, admins can configure membership policies for both public and private channels, permission policies for file upload and file download, and simulate policy outcomes before saving.

**System Admins can:**

- Create :doc:`system-wide access policies </administration-guide/manage/admin/abac-system-wide-policies>` that can be assigned across multiple channels in the System Console. Membership policies can be applied to both public and private channels, with :ref:`advisory behavior on public channels <administration-guide/manage/admin/abac-channel-access-rules:public and private channel behavior>`.
- Assign :ref:`individual channel policies <administration-guide/manage/admin/abac-system-wide-policies:define access controls per channel>` to specific channels in the System Console.
- Define :ref:`permission policies <administration-guide/manage/admin/abac-system-wide-policies:permission policies>` that restrict actions such as file upload and file download based on user attributes.
- :ref:`Simulate policy outcomes <administration-guide/manage/admin/abac-system-wide-policies:simulate access>` to preview whether selected users can perform actions such as joining a channel or uploading and downloading files before saving policy changes.

**Team Admins can:**

- Create, edit, and delete :ref:`team-scoped channel membership policies <administration-guide/manage/admin/abac-channel-access-rules:manage team-scoped membership policies in team settings>` for channels in their team directly from Team Settings, when granted the ``manage_team_access_rules`` permission.

**Team Admins can:**

- Create and manage :doc:`team-level channel membership policies </administration-guide/manage/admin/abac-team-channel-policies>` in Team Settings, scoping attribute-based rules to one or more private channels within their team.

**Channel Admins can:**

- Configure :doc:`channel-specific access rules </administration-guide/manage/admin/abac-channel-access-rules>` directly in Channel Settings without requiring a system admin.