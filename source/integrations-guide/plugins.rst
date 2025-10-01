Plugins
========

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   popular-integrations

Pre-built plugins
^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`No-code <no-code>`

Mattermost's pre-built plugins make it simple for teams to extend Mattermost with powerful integrations for project management, incident response, monitoring, and collaboration. With simple configuration steps, you can quickly connect Mattermost to widely used tools such as Jira, GitHub, GitLab, Zoom, ServiceNow and others, enabling powerful integrations that enhance collaboration and streamline workflows out of the box.

Learn more about what popular :doc:`pre-built integrations are available and how to install them </integrations-guide/popular-integrations>`.

.. tip::
  The `Mattermost Marketplace <https://mattermost.com/marketplace/>`_ offers an expanded selection of community supported integrations.

Custom-built plugins
^^^^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`Pro-code <pro-code>`

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Building a custom plugin is a **software development** task, using ``Go`` for the server-side functionality and optionally ``TypeScript/React`` for UI components. Developers should be comfortable with Git, modern build tooling, and the `Mattermost Plugin API <https://developers.mattermost.com/integrate/reference/server/server-reference/>`_, including lifecycle hooks, KV storage, slash commands, and interactivity. Knowledge of testing, logging, and security best practices is essential for production-ready plugins, along with experience packaging and deploying plugins through the System Console or CLI. For teams without these skills, simpler options like webhooks, slash commands, or no-code workflow tools may be more practical.

Plugins can authenticate and interact with Mattermost through `bot accounts <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_, utilizing the `RESTful API <https://developers.mattermost.com/api-documentation/>`_.

Learn more about `building your own plugin <https://developers.mattermost.com/integrate/plugins/>`_.