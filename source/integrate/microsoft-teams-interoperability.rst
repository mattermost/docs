Connect Microsoft Teams to Mattermost
=====================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |product-menu| image:: ../images/products_E82F.svg
  :alt: The Product menu is located in the top left corner of the Mattermost screen.
  :class: theme-icon

Break through siloes in a mixed Mattermost and Microsoft Teams environment by forwarding real-time chat notifications from Teams to Mattermost.

Setup
-----

.. include:: /about/install-mattermost-for-microsoft-teams-plugin.rst
    :start-after: :nosearch:

Usage
-----

See the :doc:`collaborate within connected microsoft teams </collaborate/collaborate-within-connected-microsoft-teams>` product documentation to get started using Microsoft Teams interoperability.

Frequently asked questions
--------------------------

My email address in Mattermost doesn't match my email address in Microsoft Teams: can I still connect?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Currently, only accounts with the same email addresses are allowed to be connected. Specify the email address that matches your Mattermost account. 

If connecting a Mattermost account to a Microsoft Teams account with a different email address is something your workspace requires, there is an open `GitHub issue <https://github.com/mattermost/mattermost-plugin-msteams/issues/519>`__ for you to share your feedback.

How is encryption handled at rest and in motion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configured client secret, stored in the Mattermost configuration, is used for app-only access to the the Microsoft Graph API. As users connect to Microsoft Teams using the integration, the resulting access tokens are encrypted and stored in the Mattermost database to be used for access on behalf of the connected user. All communication between the integration and the Microsoft Graph API is conducted via TLS.

When notifications are enabled, chats and file attachments received by connected users will be stored as posts in the direct message channel between that user and the bot account created by the integration. When linked channels are enabled, messages and file attachments sent in Microsoft Teams will be stored as posts in the linked Mattermost channel. Similarly, messages and file attachments sent in a linked Mattermost channel will be sent to Microsoft Teams using the Microsoft Graph API.

Are there any database or network security considerations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is nothing specific to the integration that is beyond what would apply to a Mattermost instance.

Are there any compliance considerations (ie. GDPR, PCI)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is nothing specific to the integration that is beyond what would apply to a Mattermost instance.

How is this integration architectured?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The integration subscribes to change notifications from the Microsoft Graph API. These change notifications inform Mattermost about new or updated chats and channel messages within Microsoft Teams. Upon receipt of the change notification, the integration use a combination of its app-only access (via the client secret) and delegated acess (via connected users) to fetch the contents of these chats and channel messages and represent them appropriately within Mattermost.

Get help
--------

If you face issues while installing this integration, gather relevant information, including reproduction steps to accelerate troubleshooting. You're welcome to open a new issue in the `Mattermost for Microsoft Teams GitHub repository <https://github.com/mattermost/mattermost-plugin-msteams/issues/new>`_.

- **Mattermost Commercial Customers (including Enterprise and Professional plans)**: Visit `Mattermost Support <https://mattermost.com/support/>`_ to `submit a support ticket <https://support.mattermost.com/hc/en-us/requests/new>`_.

- **Mattermost Team Edition and Free customers** Visit the Mattermost `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`_ where you can access the global Mattermost Community for assistance.
