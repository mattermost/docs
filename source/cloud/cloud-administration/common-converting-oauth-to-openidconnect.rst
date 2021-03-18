OAuth 2.0 is being deprecated in the System Console and replaced by OpenID Connect. Using the System Console, you can migrate your OAuth configuration to the OpenID Connect standard. 

A one-time, one-click conversion tool is available within the existing **OAuth 2.0** page. You can also go to **System Console > Authentication > OpenID Connect**.

.. image:: /images/Convert-to-OpenID-Connect.png

Select **Convert to OpenID Connect** to migrate your active service provider configuration to the new standard. No further changes are required. 

.. note::
  Inactive service providers configured for OAuth 2.0 are also migrated to the new OpenID Connect standard. Converting to OpenID Connect removes the **OAuth 2.0** option from the System Console menu.
