Desktop App deployment
=======================

.. include:: ../../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The Mattermost desktop app is available for Windows, macOS, and Linux operating systems, and offers :doc:`additional functionality </preferences/customize-desktop-app-experience>` beyond the web-based experience.

Learn more about desktop app :ref:`software requirements <deploy/server/software-hardware-requirements:desktop apps>`, :doc:`releases and server compatibility </about/mattermost-desktop-releases>` as well as the :doc:`what's changed across releases </about/desktop-app-changelog>`.

Download
---------

Download the Mattermost desktop app directly from the `Mattermost website <https://mattermost.com/apps>`_. Additional :doc:`desktop installation options </deploy/additional-desktop-installs>` are also available.

Log in
~~~~~~

The first time you log in to Mattermost using the desktop app, select **Get Started** to connect to a Mattermost server, and enter a **Server URL** and **Server display name**, then select **Connect**.

.. tip::

  Can't find your Mattermost server URL? Ask your company’s IT department or your Mattermost system admin for your organization’s **Mattermost Site URL**. It’ll look something like ``https://example.com/company/mattermost``, ``mattermost.yourcompanydomain.com``, or ``chat.yourcompanydomain.com``. These URLs could also end in ``.net``.

Deployment options
------------------

Learn about installation, configuration, and management options for deploying the desktop app in your environment.

.. toctree::
    :maxdepth: 2
    :hidden:
    :titlesonly:

    /deploy/desktop/additional-desktop-installs.rst
    /deploy/desktop/distribute-a-custom-desktop-app.rst
    /deploy/desktop/silent-windows-desktop-distribution.rst
    /deploy/desktop/desktop-msi-installer-and-group-policy-install.rst
    /deploy/desktop/desktop-custom-dictionaries.rst

* :doc:`Additional desktop app installation options </deploy/desktop/additional-desktop-installs>`
* :doc:`Distribute a custom desktop app </deploy/desktop/distribute-a-custom-desktop-app>`
* :doc:`Silent Windows desktop distribution </deploy/desktop/silent-windows-desktop-distribution>`
* :doc:`MSI installer and group policy guide </deploy/desktop/desktop-msi-installer-and-group-policy-install>`
* :doc:`Custom dictionaries for Windows and Linux </deploy/desktop/desktop-custom-dictionaries>`