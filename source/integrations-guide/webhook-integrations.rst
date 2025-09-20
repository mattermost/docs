Webhook integrations
=======================

Imagine your CI/CD pipeline just finished a build. Rather than digging through logs, a Mattermost channel instantly shows a new message:

✅ Build Successful – Project X, Version 2.3 deployed to staging.

That’s the power of Mattermost webhooks. They provide a simple yet powerful way to connect Mattermost with external systems, applications, and services so that information flows in real time, and your team stays aligned without constant manual updates.

With webhooks, you can:

- Receive updates in Mattermost from other systems via incoming webhooks.
- Send data out of Mattermost to external endpoints via outgoing webhooks based on channel activity.

Because webhooks use lightweight HTTP POST requests with JSON payloads, they're easy to set up with virtually any tool or platform, whether you need quick notifications or deep integration with enterprise workflows.

Common uses include:

- Posting monitoring alerts directly to your incident-response channel.
- Sending deployment updates from CI/CD pipelines.
- Triggering external actions like creating tickets or running scripts from inside Mattermost.

Mattermost webhooks bridge your collaboration hub with the rest of your toolset, enabling faster decisions, smoother operations, and teams that can act on information the moment it matters. Learn more about how to set up and use webhooks in the sections below:

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

  Incoming Webhooks </integrations-guide/incoming-webhooks>
  Outgoing Webhooks </integrations-guide/outgoing-webhooks>

* :doc:`Incoming Webhooks </integrations-guide/incoming-webhooks>` - Learn how to send messages to Mattermost from external applications.
* :doc:`Outgoing Webhooks </integrations-guide/outgoing-webhooks>` - Learn how to send messages from Mattermost to external applications.