:orphan: :nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

A complete Mattermost installation consists of three major components: a proxy server, a database server, and the Mattermost server. You can install all components on one machine, or you can install each component on its own machine. If you have only two machines, then install the proxy and the Mattermost server on one machine, and install the database on the other machine.

For the database, you can install either PostgreSQL or MySQL. The proxy is NGINX.

.. note::
  If you have any problems installing Mattermost, see the :doc:`troubleshooting guide </install/troubleshooting>`, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`_.
  
  For help with inviting users to your system, see :doc:`inviting team members </collaborate/manage-channel-members>` and other :ref:`getting started information <getting-started/admin-onboarding-tasks:getting started tasks>`.
  
  To submit an improvement or correction to this page, select **Edit** in the top-right corner of the page.