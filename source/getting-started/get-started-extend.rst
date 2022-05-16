Get started: extend functionality
=================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.


Extend MM functionality with integrations: http://mattermost-docs-preview-pulls.s3-website-us-east-1.amazonaws.com/5469/getting-started/admin-onboarding-tasks.html#extend-mattermost-functionality-with-integrations

Teleconferencing:
Zoom plugin: https://mattermost.com/marketplace/zoom-plugin/

Dev tooling:
GitLab plugin: https://mattermost.com/marketplace/gitlab-plugin/
GitHub plugin: https://mattermost.com/marketplace/github-plugin/

Rich user experience:
Welcome Bot plugin: https://mattermost.com/marketplace/welcomebot-plugin/
Wrangler plugin: https://github.com/gabrieljackson/mattermost-plugin-wrangler
GIFs: https://mattermost.com/marketplace/giphy-plugin/
Emoji: https://docs.mattermost.com/channels/react-to-messages.html
Custom Emoji: https://docs.mattermost.com/channels/react-to-messages.html#upload-custom-emojis
Link Previews: https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews
Mattermost Marketplace: https://mattermost.com/marketplace



**Install and manage plugins**

To enable and manage plugins, go to **System Console > Plugins**. Next, install plugins from **Product menu > Marketplace**. See the `Marketplace  <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/#marketplace>`__ documentation for details.

Consider installing and enabling the following productivity plugins for your users:   
  - Enable audio/video calling and screen sharing with `Jitsi <https://mattermost.com/blog/mattermost-and-jitsi/>`__ or `Zoom <https://mattermost.com/marketplace/zoom-plugin/>`__.
  - Create polls with `Matterpoll <https://mattermost.com/marketplace/matterpoll/>`__.
  - Share GIFs with `GIF Commands <https://mattermost.com/marketplace/giphy-plugin/>`__.
  - Create and share memes with `Memes <https://mattermost.com/marketplace/memes-plugin/>`__.
  - Set personal reminders with `Remind <https://mattermost.com/marketplace/remind-plugin/>`__.
  - Create and share to do items with `Todo <https://github.com/mattermost/mattermost-plugin-todo>`__.
  - Customize welcome messages for new users with `WelcomeBot <https://mattermost.com/marketplace/welcomebot-plugin/>`__.

Explore all plugins and integrations available in the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__.

**2. Install plugins**

You can enable plugins and integrations to connect your team's workflows and toolsets into Mattermost. Plugins and integrations customize and extend the Mattermost platform.

**Enable and manage integrations**


To enable integrations such as webhooks, slash commands, OAuth2.0, and bots, to go **System Console > Integrations**. More information on these integrations can be found `here <https://developers.mattermost.com/integrate/other-integrations/>`_. 


**5. Enable custom emoji**

`Emojis <https://docs.mattermost.com/messaging/using-emoji.html>`__ enable users to express concepts such as emotions and physical gestures in messages. Enable the emoji picker by setting **System Console > Emoji > Enable Emoji Picker** to **true**. See the `Enable emoji picker <https://docs.mattermost.com/configure/configuration-settings.html#enable-emoji-picker>`__ configuration settings documentation for details.

Empower users to create and share their own custom emojis by setting **System Console > Emoji > Enable Custom Emoji** to **true**. See the `Enable custom emoji <https://docs.mattermost.com/configure/configuration-settings.html#enable-custom-emoji>`__ configuration settings documentation for details.

**6. Enable GIF picker**

GIFs are animated images that can make messaging more fun and engaging. Enable users to access the Mattermost GIF picker from the message draft area by setting **System Console > GIF (Beta) > Enable GIF Picker** to **true**. See the `Enable GIF picker <https://docs.mattermost.com/configure/configuration-settings.html#enable-gif-picker>`__ configuration settings documentation for details.

**7. Enable link previews**

Link previews provide a visual glimpse of relevant content for links shared in messages. Enable link previews by setting **System Console > Posts > Enable Link Previews** to **true**. See the `Enable link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ configuration settings documentation for details.