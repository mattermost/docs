System Attributes
=================

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

System attributes configuration settings provide system admins with centralized control over key user account properties.

Review and manage the following system attributes configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **System Attributes**.

You can define, manage, and enforce specific attributes, including:

- **Custom attributes for user profiles**: Display details such as job titles, departments, or other metadata, on user profiles that align with your organizational structures and workflows. Learn more about :doc:`managing custom user profile attributes </administration-guide/manage/admin/user-attributes>`.
- **Granular access controls based on user attributes**: Ensure users have access to only the resources and functionality relevant to their roles, bolstering security and compliance across the organization. Learn more about :doc:`managing access based on user attributes </administration-guide/manage/admin/attribute-based-access-control>`.

----

Allow user-editable attributes in access control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-adv-cloud-selfhosted.rst
  :start-after: :nosearch:

.. config:setting:: allow-user-editable-attributes-in-abac
  :displayname: Allow user-editable attributes in access control (System Attributes)
  :systemconsole: System Attributes > Attribute-Based Access
  :configjson: .SystemAttributeSettings.UseUserEditableAttributesInAccessControl
  :environment: MM_SYSTEMATTRIBUTESETTINGS_USEUSEREDITABLEATTRIBUTESINaccesscontrol

  - **true**: Allows user-editable attributes to be used in attribute-based access control policies. This option must be explicitly enabled by system administrators.
  - **false**: **(Default from v10.11)** User-editable attributes cannot be used in attribute-based access control policies, preventing users from bypassing access controls by modifying their own profile attributes.

**True**: Allows user-editable attributes to be used in attribute-based access control policies. When enabled, attributes that users can modify in their profile can be used as criteria for channel access controls. 

.. warning::
  
  Enabling this setting may introduce security risks, as users could potentially bypass access controls by modifying their own profile attributes. Only enable this setting if your organization's security policy permits user control over access-related attributes.

**False**: **(Default from v10.11)** User-editable attributes cannot be used in attribute-based access control policies. This security enhancement prevents users from bypassing channel access controls by editing their own profile attributes that are used in ABAC policies.

.. note::

  This configuration setting was introduced in Mattermost v10.11 to enhance security of attribute-based access controls. Prior to v10.11, user-editable attributes could be used in ABAC policies without restriction. System administrators must explicitly enable this setting to restore the previous behavior.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseUserEditableAttributesInAccessControl": false`` with boolean input.               |
+-------------------------------------------------------------------------------------------------------------------------------------+
