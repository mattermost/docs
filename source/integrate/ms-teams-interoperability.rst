Connect Microsoft Teams to Mattermost (Beta)
=============================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |product-menu| image:: ../images/products_E82F.svg
  :alt: The Product menu is located in the top left corner of the Mattermost screen.
  :class: theme-icon

Bridge communications between Mattermost and Microsoft Teams, transforming them into a unified platform. Empower your users to stay on their preferred platform while ensuring seamless, cross-functional collaboration and project alignment, while leveraging the strengths of both platforms without significantly increasing operational costs., 

Setup
-----

.. include:: /about/install-mattermost-for-microsoft-teams-plugin.rst
    :start-after: :nosearch:

Usage
-----

See the :doc:`collaborate within connected microsoft teams </collaborate/collaborate-within-connected-microsoft-teams>` product documentation to get started using Microsoft Teams interoperability.

Frequently asked questions
--------------------------

Can users connect their Mattermost account to a different Microsoft Teams account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Currently, only accounts with the same email addresses are allowed to be connected. Specify the email address that matches your Mattermost account. 

If connecting a Mattermost account to a Microsoft Teams account with a different email address is something your workspace requires, there is an open `GitHub issue <https://github.com/mattermost/mattermost-plugin-msteams/issues/519>`__ for you to share your feedback.

How is encryption handled at rest and in motion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Everything is stored in the Mattermost databases. AES encryption is used to encrypt the MS Teams auth/access token. Other encryption at rest would be dependent on how the Mattermost instance is setup. All communication between the plugin and MS Teams/Graph API are conducted over SSL/HTTPS.

Are there any database or network security considerations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is nothing specific to the plugin that is beyond what would apply to a Mattermost instance.

Are there any compliance considerations (ie. GDPR, PCI)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is nothing specific to the plugin that is beyond what would apply to a Mattermost instance.

How often will users sync from Microsoft Teams to Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The frequency of user synchronizing is customizable within the System Console's plugin configuration page.

Is a service account required for this integration to sync users from MS Teams to Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. User synchronizing is done by the "application" itself.

Can I embed Mattermost within Microsoft Teams?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. See the :doc:`collaborate within embedded microsoft teams </collaborate/collaborate-within-embedded-microsoft-teams>` documentation to learn more.

How is this integration architectured?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the following diagram showing the architecture for this Mattermost integration:

.. images:: ../images/brightscout-msteams-sync-v1.0.png
  :alt: Mattermost for Microsoft Teams interoperability architecture diagram, version 1.0.

Get help
--------

If you face issues while installing this plugin, gather relevant information, including reproduction steps to accelerate troubleshooting. You're welcome to open a new issue in the `Mattermost for Microsoft Teams GitHub repository <https://github.com/mattermost/mattermost-plugin-msteams/issues/new>`_.

- **Mattermost Commercial Customers (including Enterprise and Professional plans)**: Visit `Mattermost Support <https://mattermost.com/support/>`_ to `submit a support ticket <https://support.mattermost.com/hc/en-us/requests/new>`_.

- **Mattermost Team Edition and Free customers** Visit the Mattermost `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`_ where you can access the global Mattermost Community for assistance.