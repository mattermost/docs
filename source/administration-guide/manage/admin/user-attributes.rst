User attributes
=======================

.. include:: ../../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v10.8, ensure your teams always have the critical information they need to collaborate effectively by defining and managing organization-specific user profile attributes as system attributes that you can synchronize with your AD/LDAP or SAML identity provider. 

System attributes enable you to customize user profile attributes to match your organization's unique needs and streamline collaboration while keeping user data centralized and consistent. The attributes you define, such as position, rank, or location, are :doc:`attributes users can manage as part of their user profile </end-user-guide/preferences/manage-your-profile>`. These custom profile attributes supplement existing user details visible from the user's profile picture.

.. image:: ../../../images/cpa-properties.png
  :alt: Mobile examples of a user profile with custom user attributes added as system attributes.

Before you begin
~~~~~~~~~~~~~~~~~

.. tab:: Mattermost Enterprise v10.9 or later

  From Mattermost Enterprise v10.9, the ability to create and manage system properties as a Mattermost system admin requires no manual setup. 

.. tab:: Mattermost Enterprise v10.8

  You'll need Mattermost Enterprise v10.8 or later deployment, and be a Mattermost system admin to enable the system properties feature flag, ``MM_FEATUREFLAGS_CUSTOMPROFILEATTRIBUTES`` to create and manage system properties. See the Mattermost developer documentation for details on `enabling feature flags in a self-hosted deployment <https://developers.mattermost.com/contribute/more-info/server/feature-flags/#self-hosted-and-local-development>`_. Mattermost Cloud customers can request this feature flag be enabled by contacting their Mattermost Account Manager or by `creating a support ticket <https://support.mattermost.com/hc/en-us/requests/new?ticket_form_id=11184911962004>`_ request.

If you plan to synchronize system properties with your AD/LDAP or SAML identity provider, ensure AD/LDAP or SAML synchronization is already enabled and configured. See the :doc:`AD/LDAP groups </administration-guide/onboard/ad-ldap-groups-synchronization>` product documentation or :ref:`SAML 2.0 <administration-guide/configure/authentication-configuration-settings:saml 2.0>` configuration settings documentation for details.

Mobile support
~~~~~~~~~~~~~~~

From Mattermost v10.11 and mobile app v2.25.0 onward, user attributes are fully supported on mobile devices. Mobile users can both view and edit all attribute types including multi-select, select, and text attributes directly from the mobile app.

**Mobile compatibility requirements:**

- Mattermost server v10.5 or later
- Mattermost mobile app v2.25.0 or later (for viewing attributes)
- Mattermost mobile app v2.27.0 or later (for editing attributes)
- Enterprise license
- User attributes feature enabled (enabled by default from v10.9)

**Mobile attribute functionality:**

- **View attributes**: Users can view custom profile attributes in user profiles on mobile devices
- **Edit attributes**: Users can edit their own custom profile attributes through **Settings > Edit Profile** in the mobile app  
- **All attribute types supported**: Multi-select, select, text, phone, and URL attribute types are fully functional on mobile
- **Attribute synchronization**: Attributes synchronized from AD/LDAP or SAML identity providers are automatically available on mobile

**Known limitations:**

- Samsung Galaxy S22 devices may experience display issues with custom profile attributes

.. note::
   
   Mobile attribute support requires the same server-side configuration as web and desktop clients. No additional mobile-specific setup is required.

Add attributes
~~~~~~~~~~~~~~

You can define and manage up to 20 system attributes using the System Console. Each attribute becomes a user profile option users can populate. Once you reach the maximum of 20 attributes, you can't create new attributes until you `delete attributes <#manage-attributes>`__ you no longer need.

1. In the System Console, go to **Site Configuration > System Attributes > User Attributes** and select **Add Attribute**.
2. Enter the following details:

    - **Attribute name**: Enter a unique name for the attribute. Attribute names can be up to 40 characters long.
    - **Type**: Specify the type of attribute as one of the following:

      - **Text** for text-based profile attributes.
      - **Phone** for phone number-based profile attributes.
      - **URL** for web site address-based profile attributes.
      - **Select** for a list of profile attribute values users can choose from. Specify each value followed by pressing **TAB** or **ENTER**. Values can be up to 64 characters long, and users can choose a single value.
      - **Multi-select** for a list of profile attribute values users can select from. Specify each value followed by pressing **TAB** or **ENTER**. Values can be up to 64 characters long, and users can choose multiple values.

3. Specify the attribute's visibility as one of the following:

  - **Always show**: The attribute is always visible in user profiles.
  - **Hide when empty**: The attribute is only visible in user profiles when it has a value.
  - **Always hide**: The attribute is never visible in user profiles.

4. Save your changes.

.. tip::

  Duplicate existing attributes by selecting **More** |more-icon| and selecting **Duplicate attribute**. This creates a new attribute with the same name and type as the original attribute. You can then edit the new attribute to change its name, type, and visibility as needed.

Manage attributes
~~~~~~~~~~~~~~~~~~

- **Modify**: Select the attribute fields to make inline changes to the attribute's name, type, or values. Select **More** |more-icon| to change a attribute's visibility.

- **Order**: Control the order you want attributes to appear in user profiles by dragging and dropping them in the list.

- **Delete**: Delete attributes you no longer need or want by selecting **More** |more-icon| and selecting **Delete property**.

In cases where multiple system admins manage system attributes, refresh your web browser instance to see real-time updates to system attributes made by other admins.

Sync attributes with your identity provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Synchronize a attribute with AD/LDAP or SAML by selecting **More** |more-icon| and selecting **Link attribute to AD/LDAP** or **Link attribute to SAML**. Mattermost takes you directly to the **AD/LDAP** or **SAML 2.0** configuration settings page in the System Console where you can map the attributes you want to synchronize.

2. Scroll to the **Custom profile attributes sync** section to specify the attribute used to populate the attribute in user profiles.

3. Specify the attribute mapping for the attribute by entering the attribute name in the system attribute's **Attribute** field. The attribute name must match the attribute name in your identity provider.

4. Save your changes.
