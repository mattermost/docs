Extend functionality with integrations
======================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

On this page, you'll learn about the types of integrations available in Mattermost, and how they extend Mattermost functionality. 

What integrations are available?
--------------------------------

Help your teams stay connected with teleconferening integrations like `Zoom <https://mattermost.com/marketplace/zoom-plugin/>`__.

Accelerate your workflows, reduce context switching, and stay informed with development tools like `Jira <https://mattermost.com/marketplace/jira-plugin/>`__, `GitHub <https://mattermost.com/marketplace/github-plugin/>`__ or `GitLab <https://mattermost.com/marketplace/gitlab-plugin/>`__.

More common Mattermost integrations your users will love:

- Welcome your newest Mattermost users with `WelcomeBot <https://mattermost.com/marketplace/welcomebot-plugin/>`__.
- Make it easy for your users to express themselves using GIFs, memes, and `emojis <https://docs.mattermost.com/channels/react-to-messages.html>`__.

  - Share GIFs with `GIF Commands <https://mattermost.com/marketplace/giphy-plugin/>`__.
  - Create and share memes with `Memes <https://mattermost.com/marketplace/memes-plugin/>`__.

- Make it easy for your users to move conversations to the right place with the `Wrangler plugin <https://github.com/gabrieljackson/mattermost-plugin-wrangler>`__.
- Create polls with `Matterpoll <https://mattermost.com/marketplace/matterpoll/>`__.
- Set personal reminders with `Remind <https://mattermost.com/marketplace/remind-plugin/>`__.
- Create and share to do items with `Todo <https://github.com/mattermost/mattermost-plugin-todo>`__.

Learn more below about the types of Mattermost integrations available.

Mattermost Apps
---------------

Mattermost Apps are lightweight, interactive add-ons to Mattermost implemented as a collection of HTTP endpoints. Developers and integrators can use the Mattermost Apps Framework to write Mattermost apps in their language of choice that's supported on all Mattermost clients, including web, desktop, and mobile. You can host your Mattermost Apps as HTTP services or as serverless functions running without dedicated infrastructure. 

Using the Mattermost Apps Framework, you can:

- Include full slash command control, including autocompletion.
- Post messages to channels using the Mattermost REST APIs.
- Add buttons to channel headers and post menus.
- Receive webhooks from Mattermost and third-party systems.
- Deliver an interactive app experience with dynamic fields and on-demand functions.

See the `Mattermost Apps <https://developers.mattermost.com/integrate/apps/>`__ developer documentation to learn more.

Mattermost plugins
------------------

Mattermost plugins deeply integrate with the server, the web app, and Desktop Apps. A number of plugins are available for download on the `Mattermost Marketplace <https://mattermost.com/marketplace>`__. See the `Mattermost plugins overview <https://developers.mattermost.com/integrate/plugins/overview/>`__ developer documentation to learn more about developing your own Mattermost plugins.

Plugins are enabled by default. You can disable them in the System Console by going to **System Console > Plugins**.

Incoming and outgoing webhooks
------------------------------

Webhooks are designed to easily allow your organization to post messages in Mattermost. Outgoing webhooks send an HTTP POST request to a web service and process a response back to Mattermost when the message meets specific conditions. A BOT indicator appears next to posts coming from webhooks regardless of what username is specified.

Both incoming and outgoing webhooks are enabled by default. You can disable them in the System Console by going to **System Console > Integrations**.

Slash commands
--------------

Slash commands send an HTTP POST request to a web service and process a response back to Mattermost. Some `built-in slash commands <https://developers.mattermost.com/integrate/admin-guide/admin-slash-commands/>`__ are enabled by default. 

You can also enable users to `create custom slash commands <https://docs.mattermost.com/configure/configuration-settings.html#enable-custom-slash-commands>`__ in the System Console by going to **System Console > Integrations** and enabling **Enable Custom Slash Commands**. See the `custom slash command <https://developers.mattermost.com/integrate/admin-guide/admin-slash-commands/#custom-slash-command>`__ developer documentation to learn more.

Bots
-----

Bot accounts access the `Mattermost RESTful API <https://api.mattermost.com/>`__ through the use of the `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`__. Bot accounts are just like user accounts, except they:

- Can’t be logged into.
- Can’t be used to create other bot accounts.
- Don’t count as a registered user and therefore don’t count towards the total number of users for licensed deployment.

See the `bot accounts <https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/>`__ developer documentation to learn more about creating and working with Mattermost bots.

What's next?
------------

You've now experienced a full self-hosted Mattermost :doc:`deployment <getting-started/get-started-deploy>`. You :doc:`configured </getting-started/get-started-configure>` your Mattermost workspace, :doc:`onboarded your users <getting-started/get-started-onboard-users>`, learned how to :doc:`customize notifications </getting-started/get-started-notifications>`, know how to :doc:`monitor your deployment </getting-started/get-started-monitor>`, and know that Mattermost supports integrations.

- Explore the many ways you can customize your Mattermost deployment and workspace using the System Console. See the `configuration settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation for details.
- Review product `changelogs <https://docs.mattermost.com/guides/deployment.html#scale-mattermost>`__ for current and previous release details.
- Learn about `advanced self-hosted configurations <https://docs.mattermost.com/guides/administration.html#advanced-configurations>`__, `server management <https://docs.mattermost.com/guides/administration.html#self-hosted-server-management>`__, `compliance <https://docs.mattermost.com/guides/administration.html#self-hosted-compliance>`__, and how to `scale Mattermost <https://docs.mattermost.com/guides/deployment.html#scale-mattermost>`__ for enterprise.
- Learn more about Mattermost `Channels <https://docs.mattermost.com/welcome/get-started-mattermost-channels.html>`__, `Playbooks <https://docs.mattermost.com/playbooks/get-started-with-playbooks.html>`__, and `Boards <https://docs.mattermost.com/boards/get-started-with-boards.html>`__ features and functionality.
- Learn about the many ways you can `customize your Mattermost experience <https://docs.mattermost.com/guides/welcome-to-mattermost.html#customize-your-mattermost-experience>`__.