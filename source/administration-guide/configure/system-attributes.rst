System Attributes
=================

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

System attributes configuration settings provide system admins with centralized control over key user account properties.

Review and manage the following system attributes configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **System Attributes**.

You can define, manage, and enforce specific attributes, including:

- **Custom attributes for user profiles**: Display details such as job titles, departments, or other metadata, on user profiles that align with your organizational structures and workflows. Learn more about :doc:`managing custom user profile attributes </administration-guide/manage/admin/user-attributes>`. API responses for custom profile attributes return default visibility and sort order when those values are missing.
- **Granular access controls based on user attributes**: Ensure users have access to only the resources and functionality relevant to their roles, bolstering security and compliance across the organization. Learn more about :doc:`managing access based on user attributes </administration-guide/manage/admin/attribute-based-access-control>`.
- **Control user-managed attributes in attribute-based access control (ABAC)**: From Mattermost v10.11 (Enterprise Edition Advanced), user-managed attributes are excluded from ABAC rules by default to prevent unauthorized access. System admins can enable them with a configuration setting. Learn more about enabling user-managed attributes in ABAC rules in the :ref:`User Attributes documentation <administration-guide/manage/admin/user-attributes:before you begin>`.
