Mattermost Integration Guide
----------------------------

Plugins are our system for extending and changing a Mattermost server’s capabilities. Plugins can be used to integrate external services into Mattermost. A popular example is our Jira plugin that lets users create a Jira ticket directly within the chat UI, which is accomplished using our plugin architecture.

You can also integrate external applications into your Mattermost instance, using webhooks and slash commands.

`Join our Contributors community channel <https://community.mattermost.com/core/channels/tickets>`__, where you can discuss questions with community members and the Mattermost core team. Join our `Developers channel <https://community.mattermost.com/core/channels/developers>`__ for technical discussions and our `Developer Toolkit channel <https://community.mattermost.com/core/channels/developer-toolkit>`__ for all integrations and plugins discussions.

Developer's Guide
^^^^^^^^^^^^^^^^^

For guidance and processes around developing integrations and plugins, see `our developer documentation <https://developers.mattermost.com/>`__.

Administrator's Guide
^^^^^^^^^^^^^^^^^^^^^^

An overview of what capabilities Mattermost offers for integrations.

.. toctree::
   :maxdepth: 1
   :glob:

   /administration/plugins*
   /integrations/jira*
   /integrations/zoom*
   /integrations/zapier*
   
Vist the `Mattermost Integrations Directory <https://integrations.mattermost.com/>`__ for all available plugins.

Components and Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An overview of the depth of customization available.

.. toctree::
   :maxdepth: 1
   :glob:

   /developer/api.rst
   /developer/webhooks*
   /developer/slash*
   /developer/message-attachments*
   /developer/interactive-messages*
   /developer/interactive-dialogs*
   /developer/bot-accounts*
   /developer/personal-access-tokens*
   /developer/oauth*
   /developer/integration*
   /integrations/embedding*
   /integrations/webhook*
