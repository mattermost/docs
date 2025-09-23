Workflow Orchestration Platforms
================================

**Technical complexity: No-code**

Platforms like n8n, Zapier, or Make provide powerful visual editors that support thousands of connected tools, with triggers and actions that integrate Mattermost to external services, enabling teams to build complex workflows without writing code. Admins migrating from tools like Slack Workflow Builder can recreate familiar automations in Mattermost using these platforms.

When used in comination with outgoing webhooks or custom slash commands, users can trigger complex workflows and automations without leaving Mattermost. By pointing a webhook or slash command at the unique URL these automation tools provide, any message or keyword in Mattermost can initiate a workflow. This allows you to capture context from conversations and pass it into external systems — for example, creating tickets, updating records, or starting multi-step automations.

Choosing the best platform for your team depends on your specific integration requirements, hosting preferences, and technical capabilities. Learn more about the capabilities of each platform below:  

.. tab:: n8n
  :parse-titles:

  `n8n <https://n8n.io/>`_ is ideal for organizations prioritizing data residency and security, since it is self-hosted and can be supported in air-gapped environments where cloud solutions like Zapier and Make might not be feasible. 

  Additonally, n8n supports both no-code and low-code approaches, making it flexible for technical and semi-technical users. Being open source means there’s a large community of people sharing their custom workflows and automations that can either be used directly or iterated on to meet your specific requirements.

  n8n stands out for offering rich AI integration, enabling you to combine automation with AI-powered workflows. Its `native AI Agent node <https://n8n.io/ai/>`_ lets you integrate large language models, vector databases, and other AI services directly into your automations. This means you can build workflows in Mattermost that not only react to events but also analyze context, summarize discussions, or make decisions based on AI output.

  Explore building workflows with the `Mattermost n8n integration <https://n8n.io/integrations/mattermost/>`_.

  Supported Triggers
  -------------------

  - MattermostTrigger (community node): Listens for Mattermost events via WebSocket events, such as new post and users added.

  You can also use outgoing webhooks or slash commands in Mattermost as triggers using the `Webhook node <https://n8n.io/integrations/webhook/>`_.

  Supported Actions
  ------------------

  - Channels

    - Add a user to a channel
    - Create a new channel
    - Soft delete a channel
    - Restore a soft deleted channel
    - Get statistics for a channel

  - Messages

    - Post a message into a channel
    - Post an ephemeral message into a channel
    - Soft delete a post

  - Reactions

    - Add a reaction to a post
    - Remove a reaction from a post
    - Get all reactions to one or more posts

  - Users

    - Create a new user
    - Deactivate a user (archive, revoke sessions)
    - Invite user to a team

  Supported Searches
  -------------------

  - Search for a channel 
  - Get a user by email  
  - Get a user by ID
  - Retrieve all users
  - Retrieve members of a channel

.. tab:: Make
  :parse-titles:

  Make offers a more visual and flexible approach to automation, allowing you to build complex workflows with advanced logic and data manipulation. Make offers one of the most expansive sets of out-of-the-box triggers and actions for Mattermost. 

  Make is hosted in the cloud, and excels at more complex multi-step workflows while still keeping the configuration non-technical.

  Explore building workflows with the `Mattermost Make integration <https://www.make.com/en/integrations/mattermost>`_.

  Supported Triggers
  ------------------

  - Watch New Posts: Fires when a new post is added.
  - Watch New Posts Pinned for a Channel: Fires when a post is pinned in a channel.
  - Watch New Users: Fires when a new user is added.

  Supported Actions
  ------------------

  - Add a User to a Team: Add a user into a specific team.
  - Check if the Team Exists: Verify whether a team exists by name.
  - Create a Command: Add a custom command within a team.
  - Create a New User: Create a user account on the Mattermost system.
  - Create a Post: Post a message in a channel.
  - Deactivate a User Account: Archive or disable a user account.
  - Delete a Command: Remove a command by its ID.
  - Delete a Post: Remove a post.
  - Execute a Command: Run or trigger an existing command.

  You can also use outgoing webhooks or slash commands in Mattermost as triggers using the `Webhook app <https://www.make.com/en/integrations/gateway>`_.

  Supported Searches
  -------------------

  - Get a Channel: Retrieve a channel by its ID.
  - Get a Post: Retrieve a post by its ID.
  - Get a File: Retrieve an uploaded file by its ID.
  - Get a User: Retrieve a user by their user ID.
  - Get a Team by Name: Retrieve team information by team name.

.. tab:: Zapier
  :parse-titles:

  Zapier is ideal for non-technical users who want the fastest path to connect Mattermost with over 7000+ SaaS apps. It’s hosted in the cloud, easy to set up, and best for common business workflows.

  Zapier’s strength is the breadth of integrations. Without coding, you can integrate Mattermost with everything from CRMs to social media. This is perfect for non-technical users who want to automate notifications or routine tasks, such as posting daily reports or sending Mattermost channel messages when forms are submitted. Zapier provides a user-friendly wizard and template library to get started quickly.

  Explore building workflows with the `Mattermost Zapier integration <https://n8n.io/integrations/mattermost/>`_.

  Supported Triggers
  -------------------

  - Zapier does not natively support triggers in Mattermost. If you want Mattermost to trigger a Zapier workflow, you can use outgoing webhooks or slash commands in combination with `Zapier’s Webhooks trigger <https://zapier.com/apps/webhook/integrations>`_. For example, you could configure an outgoing webhook in Mattermost to hit Zapier when a certain keyword is posted, which Zapier treats as a trigger to then perform actions in other apps.

  Supported Actions
  ------------------

  - Compared with the wide range of triggers and actions supported by n8n or Make, Zapier supports only one action: posting a message. 